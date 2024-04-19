"""
Project Name: Password Manager Tool
Developer: David Teixeira, Kara Jacobs, Jennifer Dillehay
Date: 03/28/2024
Abstract: This project is vol 0.0.1 for SDEV-265 Final Project. Please refer to the GitHub repository 
for the most up-to-date version.

    Repository: https://github.com/Teixeira-David/SDEV-265-PasswordManagerTool.git
    
    
    File Abstract: This file is the main =entry point for the SDEV-265 Password Manager Tool.
"""

# Import Python Libraries
import configparser
from datetime import date, datetime
import getpass
import glob
import os
import platform
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import pyzipper

# Import Project Modules



#######################################################################################################
# Database Class
#######################################################################################################

class Database():
    """
    Class Name: Database
    Class Description: This class is the main NOSQL database (SQLite3) for the entire program
    """    
    def __init__(self, db_name=None, db_path=None, db_backup_path=None, db_password=None):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes 
        """           
        self.db_name = db_name
        self.db_path = db_path
        self.db_backup_path = db_backup_path
        self.db_password = db_password
        self.conn = None
        self.current_user = None
        
    # Create a string of the database info
    def __str__(self):
        return f"Database(db_name={self.db_name}, db_path={self.db_path}, db_backup_path={self.db_backup_path}, db_password=PROTECTED)"
    
    # Property decorator object get function to access private db_name
    @property
    def db_name(self):
        return self._db_name

    # Property decorator object get function to access private db_path
    @property
    def db_path(self):
        return self._db_path
    
    # Property decorator object get function to access private db_backup_path
    @property
    def db_backup_path(self):
        return self._db_backup_path

    # Property decorator object get function to access private db_password
    @property
    def db_password(self):
        return self._db_password
        
    # setter method 
    @db_name.setter 
    def db_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Database name must be a string.')
        if not value.strip():
            raise ValueError('Database name cannot be empty.')
        self._db_name = value

    # setter method 
    @db_path.setter 
    def db_path(self, value):
        if not isinstance(value, str):
            raise TypeError('Database path must be a string.')
        if not value.strip():
            raise ValueError('Database path cannot be empty.')
        self._db_path = value

    # setter method 
    @db_backup_path.setter 
    def db_backup_path(self, value): 
        if not isinstance(value, str):
            raise TypeError('Backup file path name must be a string.')
        if not value.strip():
            raise ValueError('Backup file path name cannot be empty.')
        self._db_backup_path = value

    # setter method 
    @db_password.setter 
    def db_password(self, value):
        if not isinstance(value, str):
            raise TypeError('Database password must be a string.')
        if not value.strip():
            raise ValueError('Database password cannot be empty.')
        self._db_password = value
            
    def get_current_user(self):
        """
        Function Name: get_current_user
        Function Purpose: This function used to get the current user name and return to the database or other modules
        to store the name of the current user.
        """   
        # Select the dropbox item 
        current_user = getpass.getuser()
        return current_user

    def db_set_database_attr(self):
        """ 
        Function Name: db_set_database_attr
        Function Abstract: Set the database attributes from the configuration file.
        """      
        # Init the database file handler
        db_fh = Database_File_Handler()
        
        # Ensure RecordsDir exists on the desktop
        backup_dir = os.path.join(db_fh.get_os_desktop(), db_fh.db_backups_dir)
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            
        # Set the records directory path
        self.db_backup_path = backup_dir
        
        # First get the database and config file from the primary package
        config_path = db_fh.resource_path('config.ini')
        database_path = db_fh.resource_path('cipher_shield.db')
        
        # Check if the config path exists, if not None, proceed to extract the data from the config file
        if not config_path:
            return

        # Make sure to comment this out when pushed to production    
        config_path = db_fh.config_file_path(config_path)
        database_path = db_fh.config_file_path(database_path)
                        
        # Create a ConfigParser instance
        config = configparser.ConfigParser()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, 'config.ini')
        
        # Read the configuration file
        try:
            config.read(config_path)
            config_db_name = config.get('Database', 'database')
            config_db_pswrd = config.get('Database', 'password')
        except configparser.NoSectionError as e:
            print(f"Section error: {e}")
            return
        except configparser.NoOptionError as e:
            print(f"Option error: {e}")
            return

        # Set the database password and find the oldest .bak file. If no .bak file, create the default database.
        db = Database(db_name=config_db_name, db_path=database_path, db_password=config_db_pswrd)
        self.db_name = db.db_name
        self.db_path = db.db_path
        self.db_password = db.db_password     
        self.current_user = db.get_current_user()

        # Instantiate the class db connection handler
        db_conn_h = Database_Connection_Handler()

        # Instantiate the class db management handler
        db_mgm_h = Database_Management_Handler()

        # Instantiate the  class   
        oldest_backup_db = db_fh.find_last_backup_file()            

        # Check if the database path exists, if not None, proceed to make the database
        if not oldest_backup_db:
            # Check if the DB file exists, if not, create and execute the database script
            if not os.path.exists(database_path): 
                # Write the database script
                db_mgm_h.db_create_script()
                
                # Close the connection after creating it
                db_conn_h.db_disconnect()
        
        # If the .bak file exists, proceed to connect to it
        else:
            # Ensure you're disconnected from the DB before modifying the file
            db_conn_h.db_disconnect()
                        
            # Set the default database to the latest backup database snapshot.
            db_fh.replace_bundled_db_with_backup(database_path, oldest_backup_db[1])            
            
        # Connect to the database
        db_conn_h.db_connect()

                # Update the session context
        db_mgm_h.update_session_context(self.current_user)
    
    
#######################################################################################################
# Database Connection Handler Class
#######################################################################################################

class Database_Connection_Handler(Database):
    """
    Class Name: Database_Connection_Handler
    Class Description: This class is the main NOSQL database (SQLite3) for the entire program
    """    
    def __init__(self):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes 
        """
        self.conn = None
        
    def db_connect(self):
        """ 
        Function Name: db_connect
        Function Purpose: Disconnect the SQLite database 
        """  
        # Access to db_path
        if not self.db_path:
            raise ValueError("Database path has not been set.")
        try:
            self.conn = sqlite3.connect(self.db_path)
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")
            raise e
            
    def db_disconnect(self):
        """ 
        Function Name: db_disconnect
        Function Purpose: Disconnect the SQLite database 
        """          
        if self.conn:
            self.conn.close()

    def set_no_count_on(self):
        """
        Function Name: set_no_count_on
        Function Purpose: Set NOCOUNT ON for the SQLite database
        """
        sql = "PRAGMA count_changes = OFF;"
        self.db_execute_statement(sql)

    def set_foreign_key_on(self):
        """
        Function Name: set_foreign_key_on
        Function Purpose: Set Foreign Keys ON for the SQLite database
        """
        # Enable foreign keys support
        sql = "PRAGMA foreign_keys = ON;"
        self.db_execute_statement(sql)

    def db_execute_statement(self, sql):
        """
        Function Name: db_execute_statement
        Function Purpose: Execute the given SQL statement
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(f"Error executing SQL statement: {sql}, Error: {e}")
            
    def db_initialize(self):
        """ 
        Function Name: db_initialize
        Function Purpose: Initialize the database by setting NOCOUNT ON and XACT_ABORT ON
        """        
        self.set_no_count_on()
        self.set_foreign_key_on()  

#######################################################################################################
# Database File Handler Class
#######################################################################################################

class Database_File_Handler(Database):
    """
    Class Name: Database_File_Handler
    Class Description: This class is the main NOSQL database (SQLite3) for the entire program
    """    
    def __init__(self):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes 
        """    
        self.db_backups_dir = "cipher_shield_backups"
        
    @staticmethod
    def get_os_desktop():
        """
        Function Name: get_os_desktop
        Function Description: This function determines the os desktop dir and returns the desktop path
        """              
        # Get the operating system
        operating_system = platform.system()
    
        # Determine the desktop path based on the operating system
        if operating_system in ['Windows', 'Linux', 'Darwin']:
            return os.path.join(os.path.expanduser("~"), "Desktop")
        else:
            print(f"Unsupported operating system: {operating_system}")
            return None       

    @staticmethod
    def config_file_path(start_path=None):
        """
        Function Name: config_file_path
        Function Purpose: Find a file path with the given name in the directory tree starting at start_path. 
        Returns the absolute path of the file if found in Main.
        """
        # if 'Main' not in start_path:
        #     # Insert the 'Main' folder before the filename
        #     directory, filename = os.path.split(start_path)
        #     start_path = os.path.join(directory, 'Main', filename)
                    
        return start_path   
    
    @staticmethod
    def find_file(file_name, start_path=None):
        """
        Function Name: find_file
        Function Purpose: Find a file with the given name in the directory tree starting at start_path. 
        Returns the absolute path of the file if found, otherwise None.
        """
        for dirpath, dirnames, filenames in os.walk(start_path):
            if file_name in filenames:
                return os.path.abspath(os.path.join(dirpath, file_name))
        return None 
    
    @staticmethod
    def resource_path(relative_path):
        """
        Function Name: resource_path
        Function Abstract: This function Get absolute path to resource, works for dev and for PyInstaller 
        """                
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def replace_bundled_db_with_backup(self, bundled_db_path, backup_path):
        """
        Function Name: replace_bundled_db_with_backup
        Function Abstract: This function replaces the default database with the backup database snapshot.
        """            
        # Declare Local Variables
        temp_file_name = 'temp_backup_cipher_shield_database.db'
        
        # Check the backup file's existence and its extension
        if not os.path.exists(backup_path) or not backup_path.endswith('.bak'):
            print(f"Invalid backup file: {backup_path}")
            return False

        # Create a temporary copy using the tempfile module
        temp_file_handle, temp_db_path = tempfile.mkstemp(suffix='.db')
        os.close(temp_file_handle)  # Close the file handle returned by mkstemp

        # Copy the original bundled DB to the temporary path
        shutil.copy2(bundled_db_path, temp_db_path)

        # Rename the .bak file to .db, then overwrite the temporary copy
        temp_backup_db_path = os.path.join(os.path.dirname(backup_path), temp_file_name)
        os.rename(backup_path, temp_backup_db_path)

        try:
            # Copy the backup database over the temporary database
            shutil.copy2(temp_backup_db_path, temp_db_path)

            # Merge the backup database with the new tables into the temp database
            self.merge_databases(bundled_db_path, temp_db_path, temp_backup_db_path)
            
            # Replace the original bundled DB with the modified temp DB
            shutil.move(temp_db_path, bundled_db_path)
            return True
        
        except Exception as e:
            print(f"Error: {e}")
            print(f"Failed operation path details: Backup path: {backup_path}, Temp DB path: {temp_db_path}, Temp Backup DB path: {temp_backup_db_path}")
            return False
        finally:
            # Clean up any temporary files
            if os.path.exists(temp_backup_db_path):
                os.remove(temp_backup_db_path)
            if os.path.exists(temp_db_path):
                os.remove(temp_db_path)

    def find_last_backup_file(self):
        """ 
        Function Name: find_last_backup_file
        Function Purpose: Find the oldest .zip file matching the pattern cipher_shield_database.db_YYYYMMDD_HHMMSS.zip 
            in the specified backup directory and create a copy of the unzipped database.
        """   
        # Declare Local Variables  
        backup_dir = os.path.join(self.db_backup_path)

        # Check if the backup directory exists
        if not os.path.exists(backup_dir):
            print(f"'cipher_shield_backups' directory not found at: {backup_dir}")
            return None

        # First, check the contents of back up dir for .zip files
        zip_files = glob.glob(f"{backup_dir}/cipher_shield.db_????????_??????.zip")

        # If no .zip files were found in back up dir, check its subdirectories
        if not zip_files:
            zip_files = glob.glob(f"{backup_dir}/**/cipher_shield.db_????????_??????.zip", recursive=True)

        # If still no .zip files are found, return None
        if not zip_files:
            return None

        # Find the newest .zip file based on creation time
        last_zip = max(zip_files, key=os.path.getctime)
        
        # Assuming the destination directory is the same as backup_dir, adjust as needed
        decryption_password = self.db_password
        last_backup_file = self.unzip_decrypt(last_zip, backup_dir, decryption_password)

        # Constructing the path to the unzipped database file based on the zip file's name
        unzipped_db_filename = os.path.basename(last_backup_file)
        unzipped_db_path = os.path.join(backup_dir, unzipped_db_filename)

        # Copy the unzipped database to a new file
        db = Database(db_name=unzipped_db_filename, db_path=unzipped_db_path, db_password=decryption_password)

        return db.db_name, db.db_path

    def merge_databases(self, bundled_db_path, temp_db_path, backup_db_path):
        """
        Function Name: merge_databases
        Function Purpose: Merge new tables to the rolling database.
        """
        try:
            # Create the database management handler instance
            db_mg = Database_Management_Handler()
            
            # Connect to the temporary database
            db_mg.conn = sqlite3.connect(temp_db_path)
            cursor = db_mg.conn.cursor()
            
            # Drop all the new views in the backup database
            db_mg.drop_views_in_backup_db("main", cursor)

            # Attach the backup database
            cursor.execute(f"ATTACH DATABASE '{backup_db_path}' AS backup_db")
            cursor.execute(f"ATTACH DATABASE '{bundled_db_path}' AS bundled_db")
            
            # Drop all the new views in the backup and bundled databases
            db_mg.drop_views_in_backup_db("backup_db", cursor)
            db_mg.drop_views_in_backup_db("bundled_db", cursor)
            
            # Dictionary mapping table names to functions to be executed if those tables are missing
            table_list = db_mg.table_dict
            
            # Dictionary mapping views to functions to be executed if those tables are missing
            view_list = db_mg.view_dict       
            
            for table, action in table_list.items():
                flag = "table"
                # Check if the table does not exist in the main (temporary) database
                if not db_mg.check_type_exists(cursor, table, flag):
                    # Now, check if the table exists in the backup database
                    if not db_mg.check_type_exists(cursor, table, flag, "backup_db") or db_mg.check_type_exists(cursor, table, flag, "bundled_db"):
                        # Execute the function linked to the table name in table_list
                        action()  
            
            # Load views from view_list
            for view, action in view_list.items():
                flag = "view"
                # If the view does not exist in the main database or is outdated
                if not db_mg.check_type_exists(cursor, view, flag, "main") or (not db_mg.check_type_exists(cursor, view, flag, "backup_db")) or (not db_mg.check_type_exists(cursor, view, flag, "bundled_db")):
                    if view == "vAccountsInfo_":
                        # Execute the method to get the SQL view name and SQL statement
                        sql_view_name, sql_statement = action()
                        # Remove the view from the backup database
                        for i, view_name in enumerate(sql_view_name):
                            # Create or update the view using the action function in the main database
                            db_mg.db_create_views(view_name, sql_statement[i])                   
                    else:
                        # Create or update the view using the action function in the main database
                        sql_view_name, sql_statement = action()       
                        db_mg.db_create_views(sql_view_name, sql_statement)    
                
            # Commit any changes and detach the backup database
            db_mg.conn.commit()
            cursor.execute("DETACH DATABASE 'backup_db'")
            cursor.execute("DETACH DATABASE 'bundled_db'")
        except sqlite3.Error as e:
            print(f"An error occurred during merging: {e}")
            db_mg.conn.rollback()
        finally:
            cursor.close()
            db_mg.conn.close()
            
    @staticmethod
    def zip_encrypt(directory_path, zip_file_path, password):
        """ 
        Function Name: zip_encrypt
        Function Purpose: This function zips and encrypts the backup directory
        Parameters:
            - directory_path (str): The path to the directory to be zipped.
            - zip_file_path (str): The path where the zip file will be saved.
            - password (str): The password to encrypt the zip file.
        """
        with pyzipper.AESZipFile(zip_file_path, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zipf:
            if password:
                zipf.setpassword(bytes(password, 'utf-8'))
            zipf.write(directory_path, os.path.basename(directory_path))
    
    @staticmethod
    def unzip_decrypt(zip_file_path, dest_dir, password):
        """ 
        Function Name: unzip_decrypt
        Function Purpose: This function unzips and decrypts the backup directory
        Parameters:
            - zip_file_path (str): The path to the zip file to be unzipped.
            - dest_dir (str): The destination directory where the unzipped files will be saved.
            - password (str): The password to decrypt the zip file.
        """
        if not os.path.exists(zip_file_path):
            print(f"Zip file not found at: {zip_file_path}")
            return None

        if not os.path.exists(dest_dir):
            print(f"Destination directory not found. Creating: {dest_dir}")
            os.makedirs(dest_dir)

        # Unzip the file and extract the .bak file
        try:
            with pyzipper.AESZipFile(zip_file_path) as zip_ref:
                if password:
                    zip_ref.pwd = bytes(password, 'utf-8')

                # Extract all files
                zip_ref.extractall(path=dest_dir)

                # Find the .bak file from extracted items
                extracted_files = [name for name in zip_ref.namelist()]
                bak_file = next((file for file in extracted_files if file.endswith('.bak')), None)

                if bak_file:
                    return os.path.join(dest_dir, bak_file)
                else:
                    print(f"No .bak file found among extracted items in {zip_file_path}")
                    return None

        except Exception as e:
            print(f"Failed to decrypt or unzip the directory. Error: {str(e)}")
            return None

    def open_records_dir(self): 
        """ 
        Function Name: open_records_dir
        Function Purpose: This button executes when the user wants to open the parent dir. Pops up
        the file dialog and displays contents within the parent dir.
        """    
        # Get the directory path
        dirPath = self.records_file_path
            
        # Open the directory using the default file explorer for the respective OS
        if sys.platform.startswith('darwin'):
            # MacOS (using Finder)
            subprocess.call(['open', dirPath])
        elif sys.platform.startswith('linux'):
            # For Linux using xdg-open (generic)
            subprocess.call(['xdg-open', dirPath])
        elif sys.platform.startswith('win32'):
            # Windows (using Explorer)
            subprocess.call(['start', dirPath], shell=True)

    def backup_volume(self):
        """ 
        Function Name: backup_volume
        Function Purpose: Back up the previously created database volume and append the new volume to the database
        """      
        # Declare Local Variables
        db_path = self.db_path
        db_backup_path = self.db_backup_path

        # Ensure DatabaseDir exists in the CWD
        backup_dir = os.path.join(db_backup_path)
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            
        # Get the latest backup file
        latest_backup = max(glob.glob(f"{backup_dir}/*.bak"), key=os.path.getctime) if glob.glob(f"{backup_dir}/*.bak") else None

        try:
            # Create a backup file path with a timestamp
            if backup_dir is None:
                backup_file = f"{db_backup_path}/{os.path.basename(db_path)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"
            else:
                # Use the given backup path
                backup_file = f"{backup_dir}/{os.path.basename(db_path)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bak"

            if latest_backup:
                # Copy the latest backup file to the new backup path
                shutil.copy2(latest_backup, backup_file)
            else:
                # Copy the database file to the backup path if no previous backups exist
                shutil.copy2(db_path, backup_file)

            # Zip and encrypt the database back up file
            zip_file_path = os.path.join(db_backup_path, f"{os.path.basename(db_path)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip")
            self.zip_encrypt(backup_file, zip_file_path, self.db_password)

            # Remove the .bak file to save only the zip file
            os.remove(backup_file)
                    
        except Exception as e:
            print(f"Backup failed. Error: {str(e)}")

#######################################################################################################
# Database Management Handler Class
#######################################################################################################

class Database_Management_Handler(Database_Connection_Handler):
    """
    Class Name: Database_Management_Handler
    Class Description: This class is the main NOSQL database (SQLite3) for the entire program
    """    
    def __init__(self):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes 
        """
        # First set the connection to none
        self.conn = None

        # Dictionary mapping table names to functions to be executed if those tables are missing
        self.table_dict = {
                "TSessionContext": self.create_session_table,
                "TUsers": self.create_user_table,
                "TAccounts": self.create_account_table,
                "TPasswordPolicies": self.create_password_policy_table,
                "TPasswordHistory": self.create_password_history_table,
                "TBackupDBs": self.create_backup_db_records_table,
            }
        
        self.view_dict = {
                "vAccountsInfo": self.set_accounts_view,
                "vAccountsInfo_": self.db_set_all_accounts_by_category_view,
            } 
        
    @staticmethod
    def check_type_exists(cursor, type_name, flag, db_alias="main"):
        """
        Function Name: check_type_exists
        Function Purpose: Check if a type (table, view, trigger, etc.) exists in the currently connected database.
        """ 
        # Check if the flag is a valid type
        if flag not in ["table", "view", "trigger"]:
            print(f"Invalid type flag: {flag}")
            return False
        
        # Try to check if the type exists and if not return False    
        try:
            query = f"SELECT name FROM {db_alias}.sqlite_master WHERE type='{flag}';"
            cursor.execute(query)
            objects = cursor.fetchall()
            
            # Print the items for debugging purposes
            print(f"{flag} in {db_alias} database: {[obj[0] for obj in objects]}")
            
            # Check if the type name exists in the list of objects
            if any(type[0] == type_name for type in objects):
                return True
            else:
                return False

        except sqlite3.Error as e:
            print(f"Error checking table existence: {e}")
            return False

    def drop_db_object(self, cursor, object_name, object_type='table', db_alias="main"):
        """
        Function Name: drop_db_object
        Function Purpose: Drops an object from the database.

        :param cursor: The database cursor.
        :param object_name: The name of the table or view to drop.
        :param object_type: The type of database object ('table' or 'view').
        :param db_alias: The alias of the database, defaults to 'main'.
        """
        # Validate object_name against a pattern or known list
        if not re.match("^[a-zA-Z0-9_]+$", object_name):
            print(f"Invalid {object_type} name: {object_name}")
            return
        
        # Set the object type plural for the print message
        object_type_plural = 'tables' if object_type == 'table' else 'views'
        
        try:
            # SQL command to drop the table or view
            cursor.execute(f"DROP {object_type.upper()} IF EXISTS {db_alias}.{object_name}")
            print(f"{object_type.capitalize()} '{object_name}' dropped successfully from {object_type_plural}.")
        except sqlite3.Error as e:
            print(f"Error dropping {object_type} '{object_name}' in database {db_alias}: {e}")
            
    def drop_views_in_backup_db(self, db_alias, cursor):
        """
        Function Name: drop_views_in_backup_db
        Description: Drops all views in the specified database.
        
        :param db_alias: Alias of the database where views will be dropped.
        :param cursor: Cursor object for executing SQL commands.
        """
        # Drop each view in the dict key list
        for view in self.view_dict.keys():
            if view == "vAccountsInfo_":
                # Get the SQL view name and SQL statement
                set_method = self.view_dict[view]

                # Execute the method to get the SQL view name and SQL statement
                sql_view_name_tuple = set_method()
                # Remove the view from the backup database
                for view_name in sql_view_name_tuple[0]:
                    self.drop_db_object(cursor, view_name, 'view', db_alias)
            else:
                self.drop_db_object(cursor, view, 'view', db_alias)
        
    def db_create_script(self):
        """ 
        Function Name: db_create_script
        Function Purpose: Create the script for the sqlite database
        """        
        # Connect to the database
        self.db_connect()        
        
        # Initialize the database
        self.db_initialize()
        
        # Create the tables and insert the base data into the database
        self.db_load_tables()
        
        # Create the views
        self.db_load_views()

        # Create the test data and insert the data into the database -> Make sure to comment this out for production
        self.db_load_test_data()
        
    def db_load_tables(self):
        """ 
        Function Name: db_load_tables
        Function Purpose: Loads all the tables and audit tables for the database
        """                
        self.set_tables()
        
    def db_load_views(self):
        """ 
        Function Name: db_load_views
        Function Purpose: Loads all the views for the database
        """              
        self.set_views()

    def db_load_test_data(self):
        """ 
        Function Name: db_load_test_data
        Function Purpose: Loads all the tables with test data to the db. This function should be used only for 
        testing purposes and to be removed before production.
        """                
        self.insert_user_test_data()
        self.insert_account_test_data()
        self.insert_password_policy_test_data()
        self.insert_password_history_test_data()
        self.insert_backup_log_test_data()
        
    def set_tables(self):
        """ 
        Function Name: set_tables
        Function Purpose: Insert the table statements into the database
        """ 
        # Check if the database connection is available         
        if not self.conn:
            raise Exception("Database is not connected.")
        
        # Loop through the view dictionary and create the views
        for table_name, set_method in self.table_dict.items():
            set_method() 
            
    def set_views(self, target_db="main"):
        """ 
        Function Name: set_views
        Function Purpose: Insert the view statements into the database
        """ 
        # Check if the database connection is available         
        if not self.conn:
            raise Exception("Database is not connected.")
        
        # Loop through the view dictionary and create the views
        for sql_view_name, set_method in self.view_dict.items():
            sql_view_name, sql_statement = set_method()
            full_view_name = f"{target_db}.{sql_view_name}" if target_db != "main" else sql_view_name
            # Check the full_view_name to see if it is a list instead of a string
            if isinstance(full_view_name, list):
                for i, view_name in enumerate(full_view_name):
                    self.db_create_views(view_name, sql_statement[i])
            else:
                self.db_create_views(full_view_name, sql_statement)          
                
    def db_create_views(self, view_name, sql):
        """
        Function Name: db_create_views
        Function Description: This function is used to create views inside the sqlite3 database
        """
        try:
            sql_command = f"CREATE VIEW IF NOT EXISTS {view_name} AS {sql}"
            self.db_exe_statement(sql_command)
        except sqlite3.Error as e:
            print(f"Error creating view '{view_name}': {e}")   
                
    def db_exe_statement(self, sql_command):
        """
        Function Name: db_exe_statement
        Function Purpose: Execute the given SQL statement
        """
        if self.conn is None:
            print("Database is not connected.")
            return
        
        # First set the cursor to none
        cursor = None
        # Execute the SQL command
        try:
            cursor = self.conn.cursor()
            # If the sql command contains semicolons, assume it's a script with multiple statements.
            if ';' in sql_command:
                cursor.executescript(sql_command)
            else:
                cursor.execute(sql_command)
            # Commit the changes
            self.conn.commit()
            
            # For debugging purposes
            #print("SQL executed successfully.")
            
        except sqlite3.Error as e:
            self.conn.rollback()  
            print(f"Error executing SQL: {e}")
        finally:
            if cursor:
                cursor.close()
            
    def get_max_prim_keys(self, table, prim_key_col):
        """
        Function Name: get_max_prim_keys
        Function Description: This function is used to get the max value
        """
        # Declare Local Variables
        max_prim_key = None
        
        # Declare Primary sql statement and pass in the table and primary key column
        sql_query = f"SELECT MAX({prim_key_col}) FROM {table}"
        sql_max_query = f"SELECT MAX({prim_key_col}) + 1 FROM {table}"
        sql_coal_query = f"SELECT COALESCE(MAX({prim_key_col}), 1) FROM {table}"
                
        try:
            # Execute the SQL query
            cursor = self.conn.cursor()
            cursor.execute(sql_query)
            
            # Fetch the result
            result = cursor.fetchone()
            max_prim_key = result[0]
            
            # Check if the table is empty 
            if max_prim_key is None:
                cursor.execute(sql_coal_query)
                
                # Fetch the result
                result = cursor.fetchone()
                max_prim_key = result[0]
                
            else:
                cursor.execute(sql_max_query)
                                
                # Fetch the result
                result = cursor.fetchone()
                max_prim_key = result[0]  

            # Close the connection 
            cursor.close()

            # Return the result
            return max_prim_key
            
        except sqlite3.Error as e:
            print(f"Error executing SQL statement: {e}")  
            
    def insert_or_update_values(self, params):
        """
        Function Name: insert_or_update_values
        Function Description: Checks if the specified table has any content. If not, inserts values; if there is content, updates the values.
        """
        # Declare Local Variables
        table_name = params[0]
        table_col_list = params[1]
        table_values_list = params[2]
        prim_id = params[3] if len(params) > 3 else None
        key_id = params[4] if len(params) > 4 else None

        # Check if the connection is available
        if not self.conn:
            try: 
                self.db_connect()
            except sqlite3.Error as e:
                print(f"Error connecting to the database: {e}")
                return

        # Check for existing content in the table
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = cursor.fetchone()[0]

            # If the table is empty, insert new values
            if (count == 0) or key_id is None:
                # First check if the prim key is none
                if not key_id:
                    # Get the max primary key
                    key_id = self.get_max_prim_keys(table_name, prim_id)
                    
                # Insert the prim_id into the first position of the values list
                table_col_list.insert(0, prim_id) if count == 0 else table_col_list
                table_values_list.insert(0, key_id)
                insert_params = (table_name, table_col_list, table_values_list)
                self.insert_values(insert_params)
            else:
                # If the table has content and primary key is provided, update values
                if prim_id and key_id:
                    self.update_values(params)
                else:
                    print(f"Table {table_name} is not empty, and no primary key was provided for an update.")
                    
        except sqlite3.Error as e:
            print(f"Error checking content in {table_name}: {e}")
            self.conn.rollback()
        finally:
            cursor.close()
            
    def insert_values(self, params):
        """
        Function Name: insert_values
        Function Description: This function is used to insert values into non-Standard Tables.
        """
        # Set the parameters
        table_name, table_col_list, table_values_list = params
        
        # Formatting column names for the SQL statement
        cols = ', '.join(table_col_list)
        
        # Creating placeholders for the values
        placeholders = ', '.join('?' * len(table_values_list))

        try:
            # Constructing the SQL insert statement with placeholders
            sql_insert_statement = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
            
            # Execute the SQL query with parameterized values
            cursor = self.conn.cursor()
            cursor.execute(sql_insert_statement, table_values_list)
            self.conn.commit()
            
            # For debugging purpose
            #print(f"Values inserted successfully into {table_name}.")
        
        except sqlite3.Error as e:
            print(f"Error executing SQL statement: {e}")   
            self.conn.rollback()
        finally:
            cursor.close()

    def update_values(self, params):
        """
        Function Name: update_values
        Function Description: This function is used to update values into non-Standard Tables.
        """
        table_name = params[0]
        table_col_list = params[1]
        table_values_list = params[2]
        prim_id = params[3]
        key_id = params[4]
        
        try:
            # Create the SET part of the SQL query dynamically
            set_part = ', '.join(f"{col} = ?" for col in table_col_list)
            sql_update_statement = f"UPDATE {table_name} SET {set_part} WHERE {prim_id} = ?"

            # Prepare values for the parameterized query
            values_to_update = list(table_values_list) 
            values_to_update.append(key_id)

            # Execute the SQL query
            cursor = self.conn.cursor()
            cursor.execute(sql_update_statement, values_to_update)
            cursor.close()

        except sqlite3.Error as e:
            print(f"Error executing SQL statement: {e}")
            self.conn.rollback()      
            
    def db_exe_add_values(self, params):
        """
        Function Name: db_exe_add_values
        Function Description: This function is used to insert values into non-Standard Tables.
        """
        try:
            if self.conn:            
                # Begin the transaction
                cursor = self.conn.cursor()
                cursor.execute("BEGIN TRANSACTION")
                
                # Insert the new primary key into the database
                self.insert_values(params)
                
                # Commit the transaction
                cursor.execute("COMMIT")
                self.conn.commit()
                
                # Close the connection 
                cursor.close()

        except sqlite3.Error as e:
            print(f"Error executing SQL statement: {e}")   
            self.conn.rollback()

    def db_exe_update_values(self, params):
        """
        Function Name: db_exe_update_values
        Function Description: This function is used to update values into non-Standard Tables.
        """
        try:
            if self.conn:            
                # Begin the transaction
                cursor = self.conn.cursor()
                cursor.execute("BEGIN TRANSACTION")
                
                # Update the specific primary key and columns
                self.update_values(params)

                # Commit the transaction
                cursor.execute("COMMIT")
                self.conn.commit()
                
                # Close the connection 
                cursor.close()                
                
        except sqlite3.Error as e:
            print(f"Error executing SQL statement: {e}")   
            self.conn.rollback()
            
    def remove_attribute_query(self, strTable, intPrimID, intKeyID):
        """ 
        Function Name: remove_attribute_query
        Function Description: This function updates the database by removing objects inside the db table
        """    
        try:
            # First check if connected to the database   
            if not self.conn:
                raise Exception("Database is not connected.")
                                    
            # Create the SQL delete query
            sql_query = f"DELETE FROM {strTable} WHERE {intPrimID} = {intKeyID}"

            # Execute the SQL query   
            self.db_exe_statement(self, sql_query)
            self.conn.commit()

        except sqlite3.Error as e:
            print(f"Error executing SQL statement: {e}")
            self.conn.rollback()   
            
    #######################################################################################################
    # Database Tables
    #######################################################################################################         

    def create_session_table(self):
        """ 
        Function Name: create_session_table
        Function Purpose: Create the Session Table to capture the user session information
        """          
        # Create the table
        sql_table = """
            -- Create Session Table
            CREATE TABLE IF NOT EXISTS TSessionContext 
            (
                intSessionID                       INTEGER NOT NULL
                ,strCurrentUser                    VARCHAR(1000) NOT NULL
                ,dtmLastUpdated                    DATETIME DEFAULT CURRENT_TIMESTAMP

                ,CONSTRAINT TSessionContext_PK PRIMARY KEY (intSessionID)                 
            );
            """
            
        # Execute the SQL statements
        self.db_exe_statement(sql_table)
        #self.update_session_context(self.current_user)
    
    def create_user_table(self):
        """ 
        Function Name: create_user_table
        Function Purpose: Create the User Table and Z Tables inside the database
        """          
        # Create the table
        sql_table = """
            -- Create User Table
            CREATE TABLE IF NOT EXISTS TUsers 
            (
                intUserID                           INTEGER NOT NULL
                ,strUserName                        VARCHAR(1000) NOT NULL
                ,strUserPassword                    VARCHAR(1000) NOT NULL
                ,strUserEmail                       VARCHAR(1000) NOT NULL
                ,dtmRegistrationDate                DATETIME DEFAULT CURRENT_TIMESTAMP
                ,strModifiedReason                  VARCHAR(1000)

                ,CONSTRAINT TUsers_PK PRIMARY KEY (intUserID)                 
            );
            """ 
        # Create the audit table    
        sqlAudit = f"""                
            -- Create Z Table: User Table
            CREATE TABLE IF NOT EXISTS Z_TUsers 
            (
                intUserAuditID                      INTEGER NOT NULL
                ,intUserID                          INTEGER NOT NULL
                ,strUserName                        VARCHAR(1000) NOT NULL
                ,strUserPassword                    VARCHAR(1000) NOT NULL
                ,strUserEmail                       VARCHAR(1000) NOT NULL
                ,dtmRegistrationDate                DATETIME DEFAULT CURRENT_TIMESTAMP
                ,strUpdatedBy                       VARCHAR(225) NOT NULL
                ,dtmUpdatedOn                       DATETIME DEFAULT CURRENT_TIMESTAMP
                ,strAction                          VARCHAR(1) NOT NULL
                ,strModifiedReason                  VARCHAR(1000)
                
                ,CONSTRAINT Z_TUsers_PK PRIMARY KEY (intUserAuditID)
            );
            """
        # Create the table trigger    
        sqlTrigger = f"""
            -- Create Trigger: User Table - Insert Trigger
            CREATE TRIGGER IF NOT EXISTS Z_TUsers_AuditTrigger_Insert
            AFTER INSERT ON TUsers
            BEGIN
                INSERT INTO Z_TUsers 
                (
                    intUserID
                    ,strUserName
                    ,strUserPassword
                    ,strUserEmail
                    ,dtmRegistrationDate
                    ,strUpdatedBy
                    ,dtmUpdatedOn
                    ,strAction
                    ,strModifiedReason
                )
                VALUES 
                (
                    NEW.intUserID
                    ,NEW.strUserName
                    ,NEW.strUserPassword
                    ,NEW.strUserEmail
                    ,DATETIME('now')
                    ,COALESCE((SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1), 'Unknown') -- Provide a default value if subquery fails
                    ,DATETIME('now')
                    ,'I' -- Insert
                    ,NEW.strModifiedReason
                );
            END;

            -- Create Trigger: User Table - Update Trigger
            CREATE TRIGGER IF NOT EXISTS Z_TUsers_AuditTrigger_Update
            AFTER UPDATE ON TUsers
            BEGIN
                INSERT INTO Z_TUsers 
                (
                    intUserID
                    ,strUserName
                    ,strUserPassword
                    ,strUserEmail
                    ,dtmRegistrationDate
                    ,strUpdatedBy
                    ,dtmUpdatedOn
                    ,strAction
                    ,strModifiedReason
                )
                VALUES 
                (
                    NEW.intUserID
                    ,NEW.strUserName
                    ,NEW.strUserPassword
                    ,NEW.strUserEmail
                    ,DATETIME('now')
                    ,COALESCE((SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1), 'Unknown') -- Provide a default value if subquery fails
                    ,DATETIME('now')
                    ,'U' -- Update
                    ,NEW.strModifiedReason
                );
            END;

            -- Create Trigger: User Table - Delete Trigger
            CREATE TRIGGER IF NOT EXISTS Z_TUsers_AuditTrigger_Delete
            AFTER DELETE ON TUsers
            BEGIN
                INSERT INTO Z_TUsers 
                (
                    intUserID
                    ,strUserName
                    ,strUserPassword
                    ,strUserEmail
                    ,dtmRegistrationDate
                    ,strUpdatedBy
                    ,dtmUpdatedOn
                    ,strAction
                    ,strModifiedReason
                )
                VALUES 
                (
                    OLD.intUserID
                    ,OLD.strUserName
                    ,OLD.strUserPassword
                    ,OLD.strUserEmail
                    ,DATETIME('now')
                    ,COALESCE((SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1), 'Unknown') -- Provide a default value if subquery fails
                    ,DATETIME('now')
                    ,'D' -- Delete
                    ,OLD.strModifiedReason
                );
            END;
            """
            
        # Execute the SQL statements
        self.db_exe_statement(sql_table)
        self.db_exe_statement(sqlAudit)
        self.db_exe_statement(sqlTrigger)    

    def create_account_table(self):
        """ 
        Function Name: create_account_table
        Function Purpose: Create the Account Table and Z Tables inside the database
        """          
        # Create the table
        sql_table = """
            -- Create Account Table
            CREATE TABLE IF NOT EXISTS TAccounts 
            (
                intAccountID                        INTEGER NOT NULL
                ,intUserID                          INTEGER NOT NULL
                ,strAppName                         VARCHAR(1000) NOT NULL
                ,strAppUserName                     VARCHAR(1000) 
                ,strAppPassword                     VARCHAR(1000) NOT NULL
                ,strAppEmail                        VARCHAR(1000) 
                ,strCategory                        VARCHAR(1000) NOT NULL
                ,strNotes                           VARCHAR(1000) 
                ,dtmLastUpdate                      DATETIME DEFAULT CURRENT_TIMESTAMP
                ,strModifiedReason                  VARCHAR(1000)
                
                ,FOREIGN KEY ( intUserID ) REFERENCES TUsers ( intUserID )
                ,CONSTRAINT TAccounts_PK PRIMARY KEY ( intAccountID )                 
            );
            """
        # Create the audit table    
        sqlAudit = f"""                
            -- Create Z Table: Account Table
            CREATE TABLE IF NOT EXISTS Z_TAccounts 
            (
                intAccountAuditID                   INTEGER NOT NULL
                ,intAccountID                       INTEGER NOT NULL
                ,intUserID                          INTEGER NOT NULL
                ,strAppName                         VARCHAR(1000) NOT NULL
                ,strAppUserName                     VARCHAR(1000) 
                ,strAppPassword                     VARCHAR(1000) NOT NULL
                ,strAppEmail                        VARCHAR(1000) 
                ,strCategory                        VARCHAR(1000) NOT NULL
                ,strNotes                           VARCHAR(1000) 
                ,dtmLastUpdate                      DATETIME DEFAULT CURRENT_TIMESTAMP
                ,strUpdatedBy                       VARCHAR(225) NOT NULL
                ,dtmUpdatedOn                       DATETIME DEFAULT CURRENT_TIMESTAMP
                ,strAction                          VARCHAR(1) NOT NULL
                ,strModifiedReason                  VARCHAR(1000)
                
                ,CONSTRAINT Z_TAccounts_PK PRIMARY KEY (intAccountAuditID)
            );
            """
        # Create the table trigger    
        sqlTrigger = f"""
            -- Create Trigger: Account Table - Insert Trigger
            CREATE TRIGGER IF NOT EXISTS Z_TAccounts_AuditTrigger_Insert
            AFTER INSERT ON TAccounts
            BEGIN
                INSERT INTO Z_TAccounts 
                (
                    intAccountID
                    ,intUserID
                    ,strAppName
                    ,strAppUserName
                    ,strAppPassword
                    ,strAppEmail
                    ,strCategory
                    ,strNotes
                    ,dtmLastUpdate
                    ,strUpdatedBy
                    ,dtmUpdatedOn
                    ,strAction
                    ,strModifiedReason
                )
                VALUES 
                (
                    NEW.intAccountID
                    ,NEW.intUserID
                    ,NEW.strAppName
                    ,NEW.strAppUserName
                    ,NEW.strAppPassword
                    ,NEW.strAppEmail
                    ,NEW.strCategory
                    ,NEW.strNotes
                    ,DATETIME('now')
                    ,COALESCE((SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1), 'Unknown') -- Provide a default value if subquery fails
                    ,DATETIME('now')
                    ,'I' -- Insert
                    ,NEW.strModifiedReason
                );
            END;

            -- Create Trigger: Account Table - Update Trigger
            CREATE TRIGGER IF NOT EXISTS Z_TAccounts_AuditTrigger_Update
            AFTER UPDATE ON TAccounts
            BEGIN
                INSERT INTO Z_TAccounts 
                (
                    intAccountID
                    ,intUserID
                    ,strAppName
                    ,strAppUserName
                    ,strAppPassword
                    ,strAppEmail
                    ,strCategory
                    ,strNotes
                    ,dtmLastUpdate
                    ,strUpdatedBy
                    ,dtmUpdatedOn
                    ,strAction
                    ,strModifiedReason
                )
                VALUES 
                (
                    NEW.intAccountID
                    ,NEW.intUserID
                    ,NEW.strAppName
                    ,NEW.strAppUserName
                    ,NEW.strAccountName
                    ,NEW.strAppPassword
                    ,NEW.strAppEmail
                    ,NEW.strCategory
                    ,NEW.strNotes
                    ,DATETIME('now')
                    ,COALESCE((SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1), 'Unknown') -- Provide a default value if subquery fails
                    ,DATETIME('now')
                    ,'U' -- Update
                    ,NEW.strModifiedReason
                );
            END;

            -- Create Trigger: Account Table - Delete Trigger
            CREATE TRIGGER IF NOT EXISTS Z_TAccounts_AuditTrigger_Delete
            AFTER DELETE ON TAccounts
            BEGIN
                INSERT INTO Z_TAccounts 
                (
                    intAccountID
                    ,intUserID
                    ,strAppName
                    ,strAppUserName
                    ,strAppPassword
                    ,strAppEmail
                    ,strCategory
                    ,strNotes
                    ,dtmLastUpdate
                    ,strUpdatedBy
                    ,dtmUpdatedOn
                    ,strAction
                    ,strModifiedReason
                )
                VALUES 
                (
                    OLD.intAccountID
                    ,OLD.intUserID
                    ,OLD.strAppName
                    ,OLD.strAppUserName
                    ,OLD.strAppPassword
                    ,OLD.strAppEmail
                    ,OLD.strCategory
                    ,OLD.strNotes
                    ,DATETIME('now')
                    ,COALESCE((SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1), 'Unknown') -- Provide a default value if subquery fails
                    ,DATETIME('now')
                    ,'D' -- Delete
                    ,OLD.strModifiedReason
                );
            END;
            """
            
        # Execute the SQL statements
        self.db_exe_statement(sql_table)
        self.db_exe_statement(sqlAudit)
        self.db_exe_statement(sqlTrigger)  
            
    def create_password_policy_table(self):
        """ 
        Function Name: create_password_policy_table
        Function Purpose: Create the password policy record Table and Z Tables inside the database
        """          
        # Create the table
        sql_table = """ 
            -- Create Password Policy Table
            CREATE TABLE IF NOT EXISTS TPasswordPolicies 
            (
                intPolicyID                         INTEGER NOT NULL
                ,intAccountID                       INTEGER NOT NULL
                ,intMinCharLength                   INTEGER NOT NULL
                ,strRequiredChar                    VARCHAR(1000) NOT NULL
                ,intExpirePeriod                    INTEGER NOT NULL
                ,strModifiedReason                  VARCHAR(1000)
                
                ,FOREIGN KEY ( intAccountID ) REFERENCES TAccounts ( intAccountID )
                ,CONSTRAINT TPasswordPolicies_PK PRIMARY KEY ( intPolicyID )               
            );
            """
        # Create the audit table    
        sqlAudit = f"""                
            -- Create Z Table: Password Policy Table
            CREATE TABLE IF NOT EXISTS Z_TPasswordPolicies 
            (
                intPolicyAuditID                    INTEGER NOT NULL
                ,intPolicyID                        INTEGER NOT NULL
                ,intAccountID                       INTEGER NOT NULL
                ,intMinCharLength                   INTEGER NOT NULL
                ,strRequiredChar                    VARCHAR(1000) NOT NULL
                ,intExpirePeriod                    INTEGER NOT NULL
                ,strUpdatedBy                       VARCHAR(225) NOT NULL 
                ,dtmUpdatedOn                       DATETIME DEFAULT CURRENT_TIMESTAMP
                ,strAction                          VARCHAR(1) NOT NULL
                ,strModifiedReason                  VARCHAR(1000)
                
                ,CONSTRAINT Z_TPasswordPolicies_PK PRIMARY KEY (intPolicyAuditID)
            );
            """
        # Create the table trigger    
        sqlTrigger = f"""
            -- Create Trigger: Password Policy Table - Insert Trigger
            CREATE TRIGGER IF NOT EXISTS Z_TPasswordPolicies_AuditTrigger_Insert
            AFTER INSERT ON TPasswordPolicies
            BEGIN
                INSERT INTO Z_TPasswordPolicies 
                (
                    intPolicyID
                    ,intAccountID
                    ,intMinCharLength
                    ,strRequiredChar
                    ,intExpirePeriod
                    ,strUpdatedBy
                    ,dtmUpdatedOn
                    ,strAction
                    ,strModifiedReason
                )
                VALUES 
                (
                    NEW.intPolicyID
                    ,NEW.intAccountID
                    ,NEW.intMinCharLength
                    ,NEW.strRequiredChar
                    ,NEW.intExpirePeriod
                    ,COALESCE((SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1), 'Unknown') -- Provide a default value if subquery fails
                    ,DATETIME('now')
                    ,'I' -- Insert
                    ,NEW.strModifiedReason
                );
            END;

            -- Create Trigger: Password Policy Table - Update Trigger
            CREATE TRIGGER IF NOT EXISTS Z_TPasswordPolicies_AuditTrigger_Update
            AFTER UPDATE ON TPasswordPolicies
            BEGIN
                INSERT INTO Z_TPasswordPolicies 
                (
                    intPolicyID
                    ,intAccountID
                    ,intMinCharLength
                    ,strRequiredChar
                    ,intExpirePeriod
                    ,strUpdatedBy
                    ,dtmUpdatedOn
                    ,strAction
                    ,strModifiedReason
                )
                VALUES 
                (
                    NEW.intPolicyID
                    ,NEW.intAccountID
                    ,NEW.intMinCharLength
                    ,NEW.strRequiredChar
                    ,NEW.intExpirePeriod
                    ,COALESCE((SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1), 'Unknown') -- Provide a default value if subquery fails
                    ,DATETIME('now')
                    ,'U' -- Update
                    ,NEW.strModifiedReason
                );
            END;

            -- Create Trigger: Password Policy Table - Delete Trigger
            CREATE TRIGGER IF NOT EXISTS Z_TPasswordPolicies_AuditTrigger_Delete
            AFTER DELETE ON TPasswordPolicies
            BEGIN
                INSERT INTO Z_TPasswordPolicies 
                (
                    intPolicyID
                    ,intAccountID
                    ,intMinCharLength
                    ,strRequiredChar
                    ,intExpirePeriod
                    ,strUpdatedBye
                    ,dtmUpdatedOn
                    ,strAction
                    ,strModifiedReason
                )
                VALUES 
                (
                    OLD.intPolicyID
                    ,OLD.intAccountID
                    ,OLD.intMinCharLength
                    ,OLD.strRequiredChar
                    ,OLD.intExpirePeriod
                    ,COALESCE((SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1), 'Unknown') -- Provide a default value if subquery fails
                    ,DATETIME('now')
                    ,'D' -- Delete
                    ,OLD.strModifiedReason
                );
            END;
            """
            
        # Execute the SQL statements
        self.db_exe_statement(sql_table)
        self.db_exe_statement(sqlAudit)
        self.db_exe_statement(sqlTrigger)
            
    def create_password_history_table(self):
        """ 
        Function Name: create_password_history_table
        Function Purpose: Create the password history Table and Z Tables inside the database
        """          
        # Create the table
        sql_table = """
            -- Create Account Password History Table
            CREATE TABLE IF NOT EXISTS TPasswordHistory 
            (
                intPasswordHistoryID                INTEGER NOT NULL
                ,intAccountID                       INTEGER NOT NULL
                ,strOldPassword                     VARCHAR(1000) NOT NULL 
                ,dtmDateChanged                     DATETIME DEFAULT CURRENT_TIMESTAMP
                ,strModifiedReason                  VARCHAR(1000)
                ,FOREIGN KEY ( intAccountID ) REFERENCES TAccounts ( intAccountID )
                ,CONSTRAINT TPasswordHistory_PK PRIMARY KEY ( intPasswordHistoryID )               
            );
            """
        # Create the audit table    
        sqlAudit = f"""                
            -- Create Z Table: Account Password History Table
            CREATE TABLE IF NOT EXISTS Z_TPasswordHistory 
            (
                intPasswordHistoryAuditID           INTEGER NOT NULL
                ,intPasswordHistoryID               INTEGER NOT NULL
                ,intAccountID                       INTEGER NOT NULL
                ,strOldPassword                     VARCHAR(1000) NOT NULL
                ,dtmDateChanged                     DATETIME DEFAULT CURRENT_TIMESTAMP
                ,strUpdatedBy                       VARCHAR(225) NOT NULL 
                ,dtmUpdatedOn                       DATETIME DEFAULT CURRENT_TIMESTAMP
                ,strAction                          VARCHAR(1) NOT NULL
                ,strModifiedReason                  VARCHAR(1000)
                
                ,CONSTRAINT Z_TPasswordHistory_PK PRIMARY KEY (intPasswordHistoryAuditID)
            );
            """
        # Create the table trigger    
        sqlTrigger = f"""
            -- Create Trigger: Account Password History Table - Insert Trigger
            CREATE TRIGGER IF NOT EXISTS Z_TPasswordHistory_AuditTrigger_Insert
            AFTER INSERT ON TPasswordHistory
            BEGIN
                INSERT INTO Z_TPasswordHistory 
                (
                    intPasswordHistoryID
                    ,intAccountID
                    ,strOldPassword
                    ,dtmDateChanged
                    ,strUpdatedBy
                    ,dtmUpdatedOn
                    ,strAction
                    ,strModifiedReason
                )
                VALUES 
                (
                    NEW.intPasswordHistoryID
                    ,NEW.intAccountID
                    ,NEW.strOldPassword
                    ,DATETIME('now')
                    ,COALESCE((SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1), 'Unknown') -- Provide a default value if subquery fails
                    ,DATETIME('now')
                    ,'I' -- Insert
                    ,NEW.strModifiedReason
                );
            END;

            -- Create Trigger: Account Password History Table - Update Trigger
            CREATE TRIGGER IF NOT EXISTS Z_TPasswordHistory_AuditTrigger_Update
            AFTER UPDATE ON TPasswordHistory
            BEGIN
                INSERT INTO Z_TPasswordHistory 
                (
                    intPasswordHistoryID
                    ,intAccountID
                    ,strOldPassword
                    ,dtmDateChanged
                    ,strUpdatedBy
                    ,dtmUpdatedOn
                    ,strAction
                    ,strModifiedReason
                )
                VALUES 
                (
                    NEW.intPasswordHistoryID
                    ,NEW.intAccountID
                    ,NEW.strOldPassword
                    ,DATETIME('now')
                    ,COALESCE((SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1), 'Unknown') -- Provide a default value if subquery fails
                    ,DATETIME('now')
                    ,'U' -- Update
                    ,NEW.strModifiedReason
                );
            END;

            -- Create Trigger: Account Password History Table - Delete Trigger
            CREATE TRIGGER IF NOT EXISTS Z_TPasswordHistory_AuditTrigger_Delete
            AFTER DELETE ON TPasswordHistory
            BEGIN
                INSERT INTO Z_TPasswordHistory 
                (
                    intPasswordHistoryID
                    ,intAccountID
                    ,strOldPassword
                    ,dtmDateChanged
                    ,strUpdatedBy
                    ,dtmUpdatedOn
                    ,strAction
                    ,strModifiedReason
                )
                VALUES 
                (
                    OLD.intPasswordHistoryID
                    ,OLD.intAccountID
                    ,OLD.strOldPassword
                    ,DATETIME('now')
                    ,COALESCE((SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1), 'Unknown') -- Provide a default value if subquery fails
                    ,DATETIME('now')
                    ,'D' -- Delete
                    ,OLD.strModifiedReason
                );
            END;
            """
            
        # Execute the SQL statements
        self.db_exe_statement(sql_table)
        self.db_exe_statement(sqlAudit)
        self.db_exe_statement(sqlTrigger) 
        
    def create_backup_db_records_table(self):
        """ 
        Function Name: create_backup_db_records_table
        Function Purpose: Create the backup database record Table and Z Tables inside the database
        """          
        # Create the table
        sql_table = """
            -- Create Backup DB Record Table
            CREATE TABLE IF NOT EXISTS TBackupDBs 
            (
                intBackupID                         INTEGER NOT NULL
                ,intUserID                          INTEGER NOT NULL
                ,dtmBackupDate                      DATETIME DEFAULT CURRENT_TIMESTAMP
                ,strFilePath                        VARCHAR(1000) NOT NULL 
                ,strModifiedReason                  VARCHAR(1000)
                ,FOREIGN KEY ( intUserID ) REFERENCES TUsers ( intUserID )
                ,CONSTRAINT TBackupDBs_PK PRIMARY KEY ( intBackupID )               
            );
            """
        # Create the audit table    
        sqlAudit = f"""                
            -- Create Z Table: Backup DB Record Table
            CREATE TABLE IF NOT EXISTS Z_TBackupDBs 
            (
                intBackupDBAuditID                  INTEGER NOT NULL
                ,intBackupID                        INTEGER NOT NULL
                ,intUserID                          INTEGER NOT NULL
                ,dtmBackupDate                      DATETIME DEFAULT CURRENT_TIMESTAMP
                ,strFilePath                        VARCHAR(1000) NOT NULL
                ,strUpdatedBy                       VARCHAR(225) NOT NULL 
                ,dtmUpdatedOn                       DATETIME DEFAULT CURRENT_TIMESTAMP
                ,strAction                          VARCHAR(1) NOT NULL
                ,strModifiedReason                  VARCHAR(1000)
                
                ,CONSTRAINT Z_TBackupDBs_PK PRIMARY KEY (intBackupDBAuditID)
            );
            """
        # Create the table trigger    
        sqlTrigger = f"""
            -- Create Trigger: Backup DB Record Table - Insert Trigger
            CREATE TRIGGER IF NOT EXISTS Z_TBackupDBs_AuditTrigger_Insert
            AFTER INSERT ON TBackupDBs
            BEGIN
                INSERT INTO Z_TBackupDBs 
                (
                    intBackupID
                    ,intUserID
                    ,dtmBackupDate
                    ,strFilePath
                    ,strUpdatedBy
                    ,dtmUpdatedOn
                    ,strAction
                    ,strModifiedReason
                )
                VALUES 
                (
                    NEW.intBackupID
                    ,NEW.intUserID
                    ,NEW.dtmBackupDate
                    ,NEW.strFilePath
                    ,COALESCE((SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1), 'Unknown') -- Provide a default value if subquery fails
                    ,DATETIME('now')
                    ,'I' -- Insert
                    ,NEW.strModifiedReason
                );
            END;

            -- Create Trigger: Backup DB Record Table - Update Trigger
            CREATE TRIGGER IF NOT EXISTS Z_TBackupDBs_AuditTrigger_Update
            AFTER UPDATE ON TBackupDBs
            BEGIN
                INSERT INTO Z_TBackupDBs 
                (
                    intBackupID
                    ,intUserID
                    ,dtmBackupDate
                    ,strUpdatedBy
                    ,dtmUpdatedOn
                    ,strAction
                    ,strModifiedReason
                )
                VALUES 
                (
                    NEW.intBackupID
                    ,NEW.intUserID
                    ,NEW.dtmBackupDate
                    ,NEW.strFilePath
                    ,COALESCE((SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1), 'Unknown') -- Provide a default value if subquery fails
                    ,DATETIME('now')
                    ,'U' -- Update
                    ,NEW.strModifiedReason
                );
            END;

            -- Create Trigger: Backup DB Record Table - Delete Trigger
            CREATE TRIGGER IF NOT EXISTS Z_TBackupDBs_AuditTrigger_Delete
            AFTER DELETE ON TBackupDBs
            BEGIN
                INSERT INTO Z_TBackupDBs 
                (
                    intBackupID
                    ,intUserID
                    ,dtmBackupDate
                    ,strUpdatedBy
                    ,dtmUpdatedOn
                    ,strAction
                    ,strModifiedReason
                )
                VALUES 
                (
                    OLD.intBackupID
                    ,OLD.intUserID
                    ,OLD.dtmBackupDate
                    ,NEW.strFilePath
                    ,COALESCE((SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1), 'Unknown') -- Provide a default value if subquery fails
                    ,DATETIME('now')
                    ,'D' -- Delete
                    ,OLD.strModifiedReason
                );
            END;
            """
            
        # Execute the SQL statements
        self.db_exe_statement(sql_table)
        self.db_exe_statement(sqlAudit)
        self.db_exe_statement(sqlTrigger) 
            
    #######################################################################################################
    # Database View Creation
    #######################################################################################################         

    def set_accounts_view(self):
        """ 
        Function Name: set_accounts_view
        Function Purpose: Sets the base Accounts view for the database if the view does not exists in the db
        """     
        # Create the view names
        sql_view_name = 'vAccountsInfo'
        
        # Create the sql_statement for the view
        sql_statement = """
                        SELECT
                            TA.strAppName                                       AS 'Application Name'
                            ,TA.strAppUserName                                  AS 'User Name'
                            ,TA.strAppEmail                                     AS 'Email'
                            ,TA.strAppPassword                                  AS 'Account Password'
                            ,TA.dtmLastUpdate                                   AS 'Last Update'
                            ,TA.strCategory                                     AS 'Category'
                        FROM 
                            TAccounts AS TA;
                        """                    
        # To debug the view
        # print(f"View '{sql_view_name}' created or already exists.")
        
        return (sql_view_name, sql_statement)

    def db_set_all_accounts_by_category_view(self):
        """ 
        Function Name: db_set_all_accounts_by_category_view
        Function Purpose: Sets the base Accounts view for the database if the view does not exist in the db, filtered by category.
        
        Parameters:
            - category: The category of accounts to include in the view.
        """     
        # Create the category list
        categories = [
            'Social_Media', 
            'Web_Services', 
            'Finance', 
            'Personal', 
            ]
        sql_view_list = []
        sql_statement_list = []
        
        for category in categories:
            # Create the view names
            sql_view_name = f'vAccountsInfo_{category}'

            # Create the sql_statement for the view, filtering by the provided category
            sql_statement = f"""
                            SELECT
                                TA.strAppName                                       AS 'Application Name'
                                ,TA.strAppUserName                                  AS 'User Name'
                                ,TA.strAppEmail                                     AS 'Email'
                                ,TA.strAppPassword                                  AS 'Account Password'
                                ,TA.dtmLastUpdate                                   AS 'Last Update'
                                ,TA.strNotes                                        AS 'Notes'
                            FROM 
                                TAccounts AS TA
                            WHERE 
                                TA.strCategory = '{category}';
                            """                    
            # Append the created view to the list
            sql_view_list.append(sql_view_name)
            sql_statement_list.append(sql_statement)
            
        # To debug the view
        # print(f"View '{sql_view_name}' created or already exists.")
        
        return (sql_view_list, sql_statement_list)  
            
    #######################################################################################################
    # Database Update Creation
    #######################################################################################################         

    def update_session_context(self, currentUser):
        """
        Function Name: update_session_context
        Function Description: This function is used to update the session context with the current user
        """
        # Get today's date in YYYY-MM-DD format
        todays_date = date.today().isoformat()
        
        # Define parameters for the update_values method
        table_name = 'TSessionContext'
        table_col_list = ['strCurrentUser', 'dtmLastUpdated']
        table_values_list = [currentUser, todays_date]
        prim_id = 'intSessionID'
        key_id = 1

        # Package parameters
        params = (table_name, table_col_list, table_values_list, prim_id, key_id)

        # Call update_values with the prepared parameters
        self.insert_or_update_values(params)

    #######################################################################################################
    # Database Testing Data
    #######################################################################################################         

    def insert_user_test_data(self):
        """ 
        Function Name: insert_user_test_data
        Function Purpose: Insert the user test data into the tables for debugging and testing purposes
        """          
        # Get today's date in YYYY-MM-DD format
        todays_date = date.today().isoformat()
        
        # Define parameters for the insert_or_update_values method
        table_name = 'TUsers'
        table_col_list = [
            'strUserName', 
            'strUserPassword', 
            'strUserEmail', 
            'dtmRegistrationDate', 
            'strModifiedReason'
            ]
        table_values_list = [
            'cipher_admin',
            '03447b830d36c4def996d565bef520e58286867d0d19e20d40b87701d3fa221ea03bd091fc3161ed2d85ac7853534ab9219bbe1af1eefbb662670c0c57937308',
            'admin@ciphershield.com',
            todays_date,
            'Test Data Insertion',
        ]
        prim_id = 'intUserID'
        
        # Package parameters
        params = (table_name, table_col_list, table_values_list, prim_id)
        # Call insert_or_update_values with the prepared parameters
        self.insert_or_update_values(params)
        
    def insert_account_test_data(self):
        """ 
        Function Name: insert_account_test_data
        Function Purpose: Insert the user test data into the tables for debugging and testing purposes
        """          
        # Get today's date in YYYY-MM-DD format
        todays_date = date.today().isoformat()
        
        # Define parameters for the insert_or_update_values method
        table_name = 'TAccounts'
        table_col_list = [
            'intUserID', 
            'strAppName', 
            'strAppUserName', 
            'strAppPassword', 
            'strAppEmail',
            'strCategory',
            'strNotes',
            'dtmLastUpdate',
            'strModifiedReason',
            ]
        prim_id = 'intAccountID'
        
        # Define data to be inserted
        table_values_list = [
            [1, 'Facebook', 'fbuser123', 'fbpass456', 'admin@ciphershield.com', 'Social_Media', '', todays_date, 'Test Data Insertion'],
            [1, 'Twitter', 'twitteruser123', 'twitterpass789', 'admin@ciphershield.com', 'Social_Media', '', todays_date, 'Test Data Insertion'],
            [1, 'Google', 'googleuser123', 'googlepass789', 'admin@ciphershield.com', 'Web_Services', '', todays_date, 'Test Data Insertion'],
            [1, 'PNC Bank', 'pncuser123', 'pncpass789', 'admin@ciphershield.com', 'Finance', '', todays_date, 'Test Data Insertion'],
            [1, 'Fitness Tracking App', 'fitbituser123', 'fitbitpass789', 'admin@ciphershield.com', 'Personal', '', todays_date, 'Test Data Insertion']
        ]
        
        # Insert each set of data into the table
        for values in table_values_list:
            params = (table_name, table_col_list, values, prim_id)
            self.insert_or_update_values(params)
            
    def insert_password_policy_test_data(self):
        """ 
        Function Name: insert_password_policy_test_data
        Function Purpose: Insert the password policy test data into the tables for debugging and testing purposes
        """          
        # Define parameters for the insert_or_update_values method
        table_name = 'TPasswordPolicies'
        table_col_list = [
            'intAccountID', 
            'intMinCharLength', 
            'strRequiredChar', 
            'intExpirePeriod', 
            'strModifiedReason',
            ]
        prim_id = 'intPolicyID'
        
        # Define data to be inserted
        table_values_list = [
            [1, 4, 'Uppercase, Lowercase,', 30, 'Test Data Insertion'],
            [2, 8, 'Numerics, Special Symbols', 30, 'Test Data Insertion'],
            [3, 12, 'Uppercase, Lowercase, Numerics', 180, 'Test Data Insertion'],
            [4, 16, 'Lowercase, Numerics, Special Symbols', 365, 'Test Data Insertion'],
            [5, 32, 'Uppercase, Lowercase, Numerics, Special Symbols', 90, 'Test Data Insertion'],
        ]
        
        # Insert each set of data into the table
        for values in table_values_list:
            params = (table_name, table_col_list, values, prim_id)
            self.insert_or_update_values(params)

    def insert_password_history_test_data(self):
        """ 
        Function Name: insert_password_history_test_data
        Function Purpose: Insert the password history test data into the tables for debugging and testing purposes
        """    
        # Get today's date in YYYY-MM-DD format
        todays_date = date.today().isoformat()
              
        # Define parameters for the insert_or_update_values method
        table_name = 'TPasswordHistory'
        table_col_list = [
            'intAccountID', 
            'strOldPassword', 
            'dtmDateChanged',  
            'strModifiedReason',
            ]
        prim_id = 'intPasswordHistoryID'
        
        # Define data to be inserted
        table_values_list = [
            [1, 'pass123', todays_date, 'Initial password'],
            [1, 'newpass456', todays_date, 'Password change'],
            [2, 'oldpassword', todays_date, 'Initial password'],
            [2, 'newpassword', todays_date, 'Password change'],
            [3, 'abc@123', todays_date, 'Initial password'],
            [3, 'xyz@789', todays_date, 'Password change'],
            [4, 'p@ssw0rd', todays_date, 'Initial password'],
            [4, 'newpass123', todays_date, 'Password change'],
            [5, 'securepass', todays_date, 'Initial password'],
            [5, 'updatedpass', todays_date, 'Password change'],
        ]
            
        # Insert each set of data into the table
        for values in table_values_list:
            params = (table_name, table_col_list, values, prim_id)
            self.insert_or_update_values(params)
            
    def insert_backup_log_test_data(self):
        """ 
        Function Name: insert_backup_log_test_data
        Function Purpose: Insert the backup db log test data into the tables for debugging and testing purposes
        """    
        # Get today's date in YYYY-MM-DD format
        todays_date = date.today().isoformat()
        
        # Define parameters for the insert_or_update_values method
        table_name = 'TBackupDBs'
        table_col_list = [
            'intUserID', 
            'dtmBackupDate', 
            'strFilePath',  
            'strModifiedReason',
            ]
        prim_id = 'intBackupID'
        
        # Define data to be inserted
        table_values_list = [
            [1, todays_date, self.db_backup_path, 'Test Data Insertion'],
        ]
            
        # Insert each set of data into the table
        for values in table_values_list:
            params = (table_name, table_col_list, values, prim_id)
            self.insert_or_update_values(params)


#######################################################################################################
# Database Query Handler Class
#######################################################################################################

class Database_Query_Handler(Database_Connection_Handler):
    """
    Class Name: Database_Connection_Handler
    Class Description: This class is the main NOSQL database (SQLite3) for the entire program
    """    
    def __init__(self):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes 
        """
        # First set the connection to none
        self.conn = None
        
    def get_target_db_record(self, sql, values=None):
        """
        Function Name: get_target_db_record
        Function Purpose: Execute the given SQL statement and return the desired DB value
        """
        # Check if the connection is available
        if not self.conn:
            try: 
                self.db_connect()
            except sqlite3.Error as e:
                print(f"Error connecting to the database: {e}")
                return
            
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            result = cursor.fetchone()
            cursor.close()
            return result[0] if result else None
        except sqlite3.Error as e:
            print(f"Error executing SQL statement: {e}")
            return None
