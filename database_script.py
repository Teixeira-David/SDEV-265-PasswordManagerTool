"""
Project Name: Password Manager Tool
Developer: David Teixeira, Kara Jacobs, Jennifer Dillehay
Date: 03/28/2024
Abstract: This project is vol 0.0.1 for SDEV-265 Final Project. Please refer to the GitHub repository 
for the most up-to-date version.

    Repository: https://github.com/Teixeira-David/SDEV-265-PasswordManagerTool.git
    
    
    File Abstract: This file is the main entry point for the SDEV-265 Password Manager Tool.
"""

# Import Python Libraries
import configparser
import getpass
import glob
import os
import platform
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
    def __init__(self, db_name=None, db_path=None, db_backup_path=None, records_file_path=None, db_password=None):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes 
        """           
        self.db_name = db_name
        self.db_path = db_path
        self.db_backup_path = db_backup_path
        self.records_file_path = records_file_path
        self.db_password = db_password
        self.conn = None
        self.current_user = None
        
    # Create a string of the database info
    def __str__(self):
        return f"Database(db_name={self.db_name}, db_path={self.db_path}, db_backup_path={self.db_backup_path}, records_file_path={self.records_file_path}, db_password=PROTECTED)"
    
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

    # Property decorator object get function to access private records_file_path
    @property
    def records_file_path(self):
        return self._records_file_path
    
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
    @records_file_path.setter 
    def records_file_path(self, value): 
        if not isinstance(value, str):
            raise TypeError('Records file path name must be a string.')
        if not value.strip():
            raise ValueError('Records file path name cannot be empty.')
        self._records_file_path = value 
        
    # setter method 
    @db_password.setter 
    def db_password(self, value):
        if not isinstance(value, str):
            raise TypeError('Database password must be a string.')
        if not value.strip():
            raise ValueError('Database password cannot be empty.')
        self._db_password = value

    def db_connect(self):
        """ 
        Function Name: db_connect
        Function Purpose: Disconnect the SQLite database 
        """  
        if not self._db_path:
            raise ValueError("Database path has not been set.")
        try:
            self.conn = sqlite3.connect(self._db_path)
            self.set_no_count_on()
            self.set_foreign_key_on()
        except sqlite3.Error as e:
            print(f"Error connecting to the database: {e}")
            
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
        self.dbExeStatement(sql)

    def set_foreign_key_on(self):
        """
        Function Name: set_foreign_key_on
        Function Purpose: Set Foreign Keys ON for the SQLite database
        """
        # Enable foreign keys support
        sql = "PRAGMA foreign_keys = ON;"
        self.dbExeStatement(sql)
        
    def db_initialize(self):
        """ 
        Function Name: db_initialize
        Function Purpose: Initialize the database by setting NOCOUNT ON and XACT_ABORT ON
        """        
        self.set_no_count_on()
        self.set_foreign_key_on()  
        
    def get_os_desktop():
        """
        Function Name: get_os_desktop
        Function Abstract: This function determines the os desktop dir and returns the desktop path
        """              
        # Get the operating system
        operating_system = platform.system()
    
        # Determine the desktop path based on the operating system
        if operating_system == 'Windows':
            # Code for Windows
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        elif operating_system == 'Linux' or operating_system == 'Darwin':
            # Code for Linux and macOS (Darwin)
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        else:
            # For unknown or unsupported operating systems
            print(f"Unsupported operating system: {operating_system}")
            return None
        
        return desktop_path        
    
    def get_current_user(self):
            """
            Function Name: get_current_user
            Function Purpose: This function used to get the current user name and return to the database or other modules
            to store the name of the current user.
            """   
            # Select the dropbox item 
            current_user = getpass.getuser()
            self.current_user = current_user

    def config_file_path(start_path=None):
        """
        Function Name: config_file_path
        Function Purpose: Find a file path with the given name in the directory tree starting at start_path. 
        Returns the absolute path of the file if found in Main.
        """
        if 'Main' not in start_path:
            # Insert the 'Main' folder before the filename
            directory, filename = os.path.split(start_path)
            start_path = os.path.join(directory, 'Main', filename)
                    
        return start_path   
    
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
        temp_backup_db_path = os.path.join(os.path.dirname(backup_path), 'temp_backup_cipher_shield_database.db')
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
            print(f"Error replacing the database: {e}")
            return False
        finally:
            # Clean up any temporary files
            if os.path.exists(temp_backup_db_path):
                os.remove(temp_backup_db_path)
            if os.path.exists(temp_db_path):
                os.remove(temp_db_path)

    def find_oldest_backup_file(self):
        """ 
        Function Name: find_oldest_backup_file
        Function Purpose: Find the oldest .zip file matching the pattern cipher_shield_database.db_YYYYMMDD_HHMMSS.zip 
            in the specified backup directory and create a copy of the unzipped database.
        """         
        backup_dir = os.path.join(self.db_backup_path, "BackupDir")

        if not os.path.exists(backup_dir):
            print(f"'BackupDir' not found at: {backup_dir}")
            return None

        # First, check the contents of BackupDir for .zip files
        zip_files = glob.glob(f"{backup_dir}/cipher_shield_database.db_????????_??????.zip")

        # If no .zip files were found in BackupDir, check its subdirectories
        if not zip_files:
            zip_files = glob.glob(f"{backup_dir}/**/cipher_shield_database.db_????????_??????.zip", recursive=True)

        # If still no .zip files are found, return None
        if not zip_files:
            return None

        oldest_zip = max(zip_files, key=os.path.getctime)
        
        # Assuming the destination directory is the same as backup_dir, adjust as needed
        decryption_password = self.db_password
        oldest_backup_file = self.unzip_decrypt(oldest_zip, backup_dir, decryption_password)

        # Constructing the path to the unzipped database file based on the zip file's name
        unzipped_db_filename = os.path.basename(oldest_backup_file)
        unzipped_db_path = os.path.join(backup_dir, unzipped_db_filename)

        # Copy the unzipped database to a new file
        db = Database(db_name=unzipped_db_filename, db_path=unzipped_db_path, db_password=decryption_password)

        return db.db_name, db.db_path
    
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
            
    def check_table_exists(cursor, table_name, db_alias="main"):
        """
        Function Name: check_table_exists
        Function Purpose: Check if a table exists in the currently connected database.
        """        
        try:
            query = f"SELECT name FROM {db_alias}.sqlite_master WHERE type='table';"
            cursor.execute(query)
            tables = cursor.fetchall()
            # Print the tables for debugging purposes
            # print(f"Tables in {db_alias} database: {[table[0] for table in tables]}")
            
            # Check if the table name exists in the list of tables
            if any(table[0] == table_name for table in tables):
                return True
            else:
                return False

        except sqlite3.Error as e:
            print(f"Error checking table existence: {e}")
            return False
        
    def check_view_exists(cursor, view_name, db_alias="main"):
        """
        Function Name: check_view_exists
        Function Purpose: Check if a view exists in the currently connected database.
        """
        try:
            # Modify the query to check for views instead of tables
            query = f"SELECT name FROM {db_alias}.sqlite_master WHERE type='view';"
            cursor.execute(query)
            views = cursor.fetchall()

            # Check if the view name exists in the list of views
            if any(view[0] == view_name for view in views):
                return True
            else:
                return False

        except sqlite3.Error as e:
            print(f"Error checking view existence: {e}")
            return False
        
    def merge_databases(self, bundled_db_path, temp_db_path, backup_db_path):
        """
        Function Name: merge_databases
        Function Purpose: Merge new tables to the rolling database.
        """
        try:
            # Get the current user 
            self.Get_Current_User()
            
            # Connect to the temporary database
            self.conn = sqlite3.connect(temp_db_path)
            cursor = self.conn.cursor()
            
            # Drop all the new views in the backup database
            self.drop_views_in_backup_db("main", cursor)

            # Attach the backup database
            cursor.execute(f"ATTACH DATABASE '{backup_db_path}' AS backup_db")
            cursor.execute(f"ATTACH DATABASE '{bundled_db_path}' AS bundled_db")
            
            # Drop all the new views in the backup and bundled databases
            self.drop_views_in_backup_db("backup_db", cursor)
            self.drop_views_in_backup_db("bundled_db", cursor)
            
            # Dictionary mapping table names to functions to be executed if those tables are missing
            loadList = {
                "TUsers": self.create_user_table,
            }
            
            # Dictionary mapping views to functions to be executed if those tables are missing
            viewList = {
                "vUserInfo": self.some_view_creation_method,
            }         
            
            for table, action in loadList.items():
                # Check if the table does not exist in the main (temporary) database
                if not self.check_table_exists(cursor, table):
                    # Now, check if the table exists in the backup database
                    if not self.check_table_exists(cursor, table, "backup_db") or self.check_table_exists(cursor, table, "bundled_db"):
                        # Execute the function linked to the table name in loadList
                        action(Database)  
            
            # Load views from viewList
            for view, action in viewList.items():
                # If the view does not exist in the main database or is outdated
                if not self.check_view_exists(cursor, view, "main") or (not self.check_view_exists(cursor, view, "backup_db")) or (not self.check_view_exists(cursor, view, "bundled_db")):
                    # Create or update the view using the action function in the main database
                    action(Database)             
                
            # Commit any changes and detach the backup database
            self.conn.commit()
            cursor.execute("DETACH DATABASE 'backup_db'")
            cursor.execute("DETACH DATABASE 'bundled_db'")
        except sqlite3.Error as e:
            print(f"An error occurred during merging: {e}")
            self.conn.rollback()
        finally:
            cursor.close()
            self.conn.close()

    def check_table_exists(cursor, table_name, db_alias="main"):
        """
        Function Name: check_table_exists
        Function Purpose: Check if a table exists in the currently connected database.
        """        
        try:
            query = f"SELECT name FROM {db_alias}.sqlite_master WHERE type='table';"
            cursor.execute(query)
            tables = cursor.fetchall()
            # Print the tables for debugging purposes
            # print(f"Tables in {db_alias} database: {[table[0] for table in tables]}")
            
            # Check if the table name exists in the list of tables
            if any(table[0] == table_name for table in tables):
                return True
            else:
                return False

        except sqlite3.Error as e:
            print(f"Error checking table existence: {e}")
            return False

    def check_view_exists(cursor, view_name, db_alias="main"):
        """
        Function Name: check_view_exists
        Function Purpose: Check if a view exists in the currently connected database.
        """
        try:
            # Modify the query to check for views instead of tables
            query = f"SELECT name FROM {db_alias}.sqlite_master WHERE type='view';"
            cursor.execute(query)
            views = cursor.fetchall()

            # Check if the view name exists in the list of views
            if any(view[0] == view_name for view in views):
                return True
            else:
                return False

        except sqlite3.Error as e:
            print(f"Error checking view existence: {e}")
            return False

    def drop_view(self, cursor, view_name):
        """
        Function Name: drop_view
        Function Purpose: Drops a view from the database.

        :param cursor: The database cursor.
        :param view_name: The name of the view to drop.
        """
        try:
            # SQL command to drop the view
            cursor.execute(f"DROP VIEW IF EXISTS {view_name}")
            print(f"View '{view_name}' dropped successfully.")
        except sqlite3.Error as e:
            print(f"Error dropping view '{view_name}': {e}")
            
    def drop_views_in_backup_db(self, db_alias, cursor):
        """
        Function Name: drop_views_in_backup_db
        Description: Drops all views in the specified database.
        
        :param db_alias: Alias of the database where views will be dropped.
        :param cursor: Cursor object for executing SQL commands.
        """
        # Create the view names
        sql_view_name = [
            'vSomeView',

            ]        
        try:
            # Drop each view in the list
            for view in sql_view_name:
                cursor.execute(f"DROP VIEW IF EXISTS {db_alias}.{view};")

        except sqlite3.Error as e:
            print(f"Error dropping views in database {db_alias}: {e}")
            
    def db_create_script(self):
        """ 
        Function Name: db_create_script
        Function Purpose: Create the script for the sqlite database
        """        
        # Get the current user 
        self.get_current_user()
        
        # Connect to the database
        self.db_connect()        
        
        # Initialize the database
        self.db_initialize()
        
        # Create the tables and insert the base data into the database
        self.db_load_tables()
        
        # Create the views
        self.db_load_views()
        
    def db_load_tables(self):
        """ 
        Function Name: db_load_tables
        Function Purpose: Loads all the tables and audit tables for the database
        """                
        # Load the Inspection Status tables
        self.createInspectionStatusTable()
        
    def db_load_views(self):
        """ 
        Function Name: db_load_views
        Function Purpose: Loads all the views for the database
        """              
        self.set_views()

    def set_views(self, target_db="main"):
        """ 
        Function Name: set_views
        Function Purpose: Insert the view statements into the database
        """          
        # Create the view names
        sql_view_name = [
            'vInspectors', 
            
            ]
                        
        # Create the sqlStatement for the view
        sqlStatement = [
            # vInspectors
            "SELECT strLastName || ',' || strFirstName AS InspectorName FROM TInspectors",

            ]

        # First check if connected to the database outside the loop (optional based on your use case)
        if not self.conn:
            raise Exception("Database is not connected.")

        # Execute the SQL statements
        for view_name, sql in zip(sql_view_name, sqlStatement):
            full_view_name = f"{target_db + '.' if target_db != 'main' else ''}{view_name}"
            try:
                self.db_create_views(full_view_name, sql)
            except sqlite3.Error as e:
                print(f"Error creating view '{view_name}': {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")            

    def create_new_views(self, viewName, sql):
        """
        Function Name: dbCreateViews
        Function Description: This function is used to create new views inside the sqlite3 database
        """
        try:
            # First check if connected to the database   
            if not self.conn:
                raise Exception("Database is not connected.")
                        
            # Declare Local Variables
            sql_command = f"CREATE VIEW IF NOT EXISTS {viewName} AS {sql}"
            
            # Create the view
            self.db_exe_statement(sql_command)

            # Commit the changes and close the connection
            self.conn.commit()

        except sqlite3.Error as e:
            print(f"Error creating SQLite view: {e}")

    def db_create_views(self, full_view_name, sql):
        """
        Function Name: db_create_views
        Function Description: This function is used to create views inside the sqlite3 database
        """
        try:
            # First check if connected to the database   
            if not self.conn:
                raise Exception("Database is not connected.")

            # Split the full_view_name to extract the target_db and viewName
            parts = full_view_name.split('.')
            if len(parts) == 2:
                target_db, viewName = parts
            else:
                # If the view name does not include a period, assume it's in the main database
                target_db = "main"
                viewName = full_view_name

            # Construct the SQL command
            sql_command = f"CREATE VIEW IF NOT EXISTS {viewName} AS {sql}"
            
            # Determine which execution method to use
            if target_db == "main":
                # Execute the SQL command
                self.db_exe_statement(sql_command)

                # Commit the changes
                self.conn.commit()
            else:
                # Direct execution for other databases
                cursor = self.conn.cursor()
                try:                
                    # Execute the SQL command
                    cursor.executescript(sql_command)

                    # Commit the changes
                    self.conn.commit()
                    # print(f"SQL executed successfully for {target_db} database:", sql)
                except sqlite3.Error as e:
                    print(f"Error executing SQL statement: {e}")
                finally:
                    cursor.close()
                    
        except sqlite3.Error as e:
            print(f"Error creating SQLite view: {e}")   
            
#######################################################################################################
# Database Queries
#######################################################################################################         

    def db_exe_statement(self, sql):
        """
        Function Name: db_exe_statement
        Function Purpose: Execute the given SQL statement
        """
        # Check if the database connection is available
        if self.conn is None:
            print("Database is not connected.")
            return

        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.executescript(sql)
            # print("SQL executed successfully:", sql)
        except sqlite3.Error as e:
            print(f"Error executing SQL statement: {e}")
        finally:
            # Ensure the cursor is closed in any situation
            if cursor:
                cursor.close()

    def insert_values(self, params):
        """
        Function Name: insert_values
        Function Description: This function is used to insert values into non-Standard Tables.
        """
        str_table = params[0]
        table_col_list = params[1]
        table_values_list = params[2]
                
        try:
            # Declare Primary sql statement and pass in the table and primary key column
            sqlQuery = f"INSERT INTO {str_table} {table_col_list} VALUES {table_values_list}"
            
            # Execute the SQL query
            cursor = self.conn.cursor()
            cursor.execute(sqlQuery)

            # Close the connection 
            cursor.close()
                        
        except sqlite3.Error as e:
            print(f"Error executing SQL statement: {e}")   
            self.conn.rollback()

    def update_values(self, params):
        """
        Function Name: update_values
        Function Description: This function is used to update values into non-Standard Tables.
        """
        str_table = params[0]
        table_col_list = params[1]
        table_values_list = params[2]
        prim_id = params[3]
        key_id = params[4]
        
        try:
            # Create the SET part of the SQL query dynamically
            set_part = ', '.join(f"{col} = ?" for col in table_col_list)
            sqlQuery = f"UPDATE {str_table} SET {set_part} WHERE {prim_id} = ?"

            # Prepare values for the parameterized query
            values_to_update = list(table_values_list) 
            values_to_update.append(key_id)

            # Execute the SQL query
            cursor = self.conn.cursor()
            cursor.execute(sqlQuery, values_to_update)
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
# Database Object Creation
#######################################################################################################         

    def create_user_table(self):
        """ 
        Function Name: create_user_table
        Function Purpose: Create the User Table and Z Tables inside the database
        """          
        try:
            # First check if connected to the database   
            if not self.conn:
                raise Exception("Database is not connected.")
        
            # Create the table
            sqlTable = """
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
                    ,strUpdatedBy                       VARCHAR(225) NOT NULL DEFAULT '{self.currentUser}'
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
                        ,NEW.dtmRegistrationDate
                        ,DATETIME('now')
                        ,'{self.currentUser}'
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
                        ,'{self.currentUser}'
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
                        ,'{self.currentUser}'
                        ,DATETIME('now')
                        ,'D' -- Delete
                        ,OLD.strModifiedReason
                    );
                END;
                """
                
            # Execute the SQL statements
            Database.db_exe_statement(self, sqlTable)
            Database.db_exe_statement(self, sqlAudit)
            Database.db_exe_statement(self, sqlTrigger)    
            
            # Commit the changes 
            self.conn.commit()

        except sqlite3.Error as e:
            print(f"Error creating User tables: {e}")   

    def create_account_table(self):
        """ 
        Function Name: create_account_table
        Function Purpose: Create the Account Table and Z Tables inside the database
        """          
        try:
            # First check if connected to the database   
            if not self.conn:
                raise Exception("Database is not connected.")
        
            # Create the table
            sqlTable = """
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
                    ,strUpdatedBy                       VARCHAR(225) NOT NULL DEFAULT '{self.currentAccount}'
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
                        ,strAccountName
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
                        ,'{self.currentAccount}'
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
                        ,'{self.currentAccount}'
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
                        ,'{self.currentAccount}'
                        ,DATETIME('now')
                        ,'D' -- Delete
                        ,OLD.strModifiedReason
                    );
                END;
                """
                
            # Execute the SQL statements
            Database.db_exe_statement(self, sqlTable)
            Database.db_exe_statement(self, sqlAudit)
            Database.db_exe_statement(self, sqlTrigger)    
            
            # Commit the changes 
            self.conn.commit()

        except sqlite3.Error as e:
            print(f"Error creating Account tables: {e}")
            
    def create_password_policy_table(self):
        """ 
        Function Name: create_password_policy_table
        Function Purpose: Create the password policy record Table and Z Tables inside the database
        """          
        try:
            # First check if connected to the database   
            if not self.conn:
                raise Exception("Database is not connected.")
        
            # Create the table
            sqlTable = """ 
                -- Create Password Policy Table
                CREATE TABLE IF NOT EXISTS TPasswordPolicies 
                (
                    intPolicyID                         INTEGER NOT NULL
                    ,intUserID                          INTEGER NOT NULL
                    ,intMinCharLength                   INTEGER NOT NULL
                    ,strRequiredChar                    VARCHAR(1000) NOT NULL
                    ,intExpirePeriod                    INTEGER NOT NULL
                    ,strModifiedReason                  VARCHAR(1000)
                    ,FOREIGN KEY ( intUserID ) REFERENCES TUsers ( intUserID )
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
                    ,intUserID                          INTEGER NOT NULL
                    ,intMinCharLength                   INTEGER NOT NULL
                    ,strRequiredChar                    VARCHAR(1000) NOT NULL
                    ,intExpirePeriod                    INTEGER NOT NULL
                    ,strUpdatedBy                       VARCHAR(225) NOT NULL DEFAULT '{self.currentAccount}'
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
                        ,intUserID
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
                        ,NEW.intUserID
                        ,NEW.intMinCharLength
                        ,NEW.strRequiredChar
                        ,NEW.intExpirePeriod
                        ,'{self.currentAccount}'
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
                        ,intUserID
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
                        ,NEW.intUserID
                        ,NEW.intMinCharLength
                        ,NEW.strRequiredChar
                        ,NEW.intExpirePeriod
                        ,'{self.currentAccount}'
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
                        ,intUserID
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
                        OLD.intPolicyID
                        ,OLD.intUserID
                        ,OLD.intMinCharLength
                        ,OLD.strRequiredChar
                        ,OLD.intExpirePeriod
                        ,'{self.currentAccount}'
                        ,DATETIME('now')
                        ,'D' -- Delete
                        ,OLD.strModifiedReason
                    );
                END;
                """
                
            # Execute the SQL statements
            Database.db_exe_statement(self, sqlTable)
            Database.db_exe_statement(self, sqlAudit)
            Database.db_exe_statement(self, sqlTrigger)    
            
            # Commit the changes 
            self.conn.commit()

        except sqlite3.Error as e:
            print(f"Error creating Password Policy tables: {e}")
            
    def create_password_history_table(self):
        """ 
        Function Name: create_password_history_table
        Function Purpose: Create the password history Table and Z Tables inside the database
        """          
        try:
            # First check if connected to the database   
            if not self.conn:
                raise Exception("Database is not connected.")
        
            # Create the table
            sqlTable = """
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
                    ,strUpdatedBy                       VARCHAR(225) NOT NULL DEFAULT '{self.currentAccount}'
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
                        ,'{self.currentAccount}'
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
                        ,'{self.currentAccount}'
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
                        ,'{self.currentAccount}'
                        ,DATETIME('now')
                        ,'D' -- Delete
                        ,OLD.strModifiedReason
                    );
                END;
                """
                
            # Execute the SQL statements
            Database.db_exe_statement(self, sqlTable)
            Database.db_exe_statement(self, sqlAudit)
            Database.db_exe_statement(self, sqlTrigger)    
            
            # Commit the changes 
            self.conn.commit()

        except sqlite3.Error as e:
            print(f"Error creating Account Password History tables: {e}")

    def create_backup_db_records_table(self):
        """ 
        Function Name: create_backup_db_records_table
        Function Purpose: Create the backup database record Table and Z Tables inside the database
        """          
        try:
            # First check if connected to the database   
            if not self.conn:
                raise Exception("Database is not connected.")
        
            # Create the table
            sqlTable = """
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
                    ,strUpdatedBy                       VARCHAR(225) NOT NULL DEFAULT '{self.currentAccount}'
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
                        ,'{self.currentAccount}'
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
                        ,'{self.currentAccount}'
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
                        ,'{self.currentAccount}'
                        ,DATETIME('now')
                        ,'D' -- Delete
                        ,OLD.strModifiedReason
                    );
                END;
                """
                
            # Execute the SQL statements
            Database.db_exe_statement(self, sqlTable)
            Database.db_exe_statement(self, sqlAudit)
            Database.db_exe_statement(self, sqlTrigger)    
            
            # Commit the changes 
            self.conn.commit()

        except sqlite3.Error as e:
            print(f"Error creating Backup DB Record tables: {e}")
            
#######################################################################################################
# Database Object View Creation
#######################################################################################################         

    def db_set_accounts_view(self):
        """ 
        Function Name: db_set_accounts_view
        Function Purpose: Sets the base Accounts view for the database if the view does not exists in the db
        """     
        try:
            # First check if connected to the database   
            if not self.conn:
                raise Exception("Database is not connected.")

            # Create the view names
            sql_view_name = 'vAccountsInfo'
            
            # Create the sqlStatement for the view
            sqlStatement = """SELECT
                                TA.strAppName                                       AS Application_Name
                                ,TA.strAppUserName                                  AS User_Name
                                ,TA.strAppEmail                                     AS Email
                                ,TA.strAppPassword                                  AS Account_Password
                                ,TA.dtmLastUpdate                                   AS Last_Update
                                ,TA.strCategory                                     AS Category
                            FROM 
                                TAccounts AS TA;"""                    
        
                        
            # Execute the SQL statements
            self.create_new_views(sql_view_name, sqlStatement)       
            
            # Commit the changes 
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error Inserting Data: {e}")   
            
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
        
        try:
            # First check if connected to the database   
            if not self.conn:
                raise Exception("Database is not connected.")

            for category in categories:
                # Create the view names
                sql_view_name = f'vAccountsInfo_{category}'

                # Create the sqlStatement for the view, filtering by the provided category
                sqlStatement = f"""SELECT
                                    TA.strAppName                                       AS Application_Name
                                    ,TA.strAppUserName                                  AS User_Name
                                    ,TA.strAppEmail                                     AS Email
                                    ,TA.strAppPassword                                  AS Account_Password
                                    ,TA.dtmLastUpdate                                   AS Last_Update
                                    ,TA.strNotes                                        AS Notes
                                FROM 
                                    TAccounts AS TA
                                WHERE 
                                    TA.strCategory = '{category}';"""                    

                # Execute the SQL statements
                self.create_new_views(sql_view_name, sqlStatement)       

            # Commit the changes Query
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error Inserting Data: {e}")   