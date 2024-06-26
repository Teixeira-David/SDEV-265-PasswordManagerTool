"""
Project Name: Password Manager Tool
Developer: David Teixeira, Kara Jacobs, Jennifer Dillehay
Date: 03/28/2024
Abstract: This project is vol 0.0.1 for SDEV-265 Final Project. Please refer to the GitHub repository 
for the most up-to-date version.

    Repository: https://github.com/Teixeira-David/SDEV-265-PasswordManagerTool.git
    
    
    File Abstract: This file is the user object class for all data structures and methods.
"""

# Import Python Libraries
from pyisemail import is_email
import re
from tkinter import *
from datetime import date, datetime
from dateutil import parser

# Import project modules
from password_object_class import PasswordWithPolicy
from database_script import Database_Query_Handler, Database_Management_Handler


#######################################################################################################
# User Class
#######################################################################################################         
class User(Database_Query_Handler, Database_Management_Handler):
    """
    Class Name: User
    Class Description: This class gets and sets User information 
    """
    # Create class variable shared amongst all User methods
    user_id_list = []   
    user_id = 0
    
    # Common base class for all Users information. Instantiates the base class
    def __init__(self, user_id=0, username="", user_password="",  user_email="default@gmail.com", registration_date=datetime.now()):
        self.user_id = user_id
        self.username = username
        self.user_password = user_password
        self.user_email = user_email 
        self.registration_date = registration_date
        self.conn = None
        
    # Property decorator object get function to access private User ID
    @property
    def user_id(self):
        return self._user_id

    # Property decorator object get function to access private Username
    @property
    def username(self):
        return self._username

    # Property decorator object get function to access private Password
    @property
    def user_password(self):
        return self._user_password         

    # Property decorator object get function to access private Email
    @property
    def user_email(self):
        return self._user_email

    # Property decorator object get function to access private Registration Date
    @property
    def registration_date(self):
        return self._registration_date
    
    # setter method 
    @user_id.setter 
    def user_id(self, value): 
        # The value should be an integer and greater than zero
        if not isinstance(value, int) or value < 0:
            raise ValueError('ID must be a positive integer')
        self._user_id = value
    
    # setter method 
    @username.setter 
    def username(self, value): 
        # The value must be a string, not empty, and can include underscores and hyphens
        if not isinstance(value, str) or value.isspace() or not re.match(r"^[a-zA-Z0-9_-]+$", value):
            raise ValueError('Username must be alphanumeric and can include underscores and hyphens')
        self._username = value

    # setter method 
    @user_password.setter 
    def user_password(self, value): 
        # The value must be a string and must not be empty
        if not isinstance(value, str) or value.isspace():
            self.delete_user_data()
            raise ValueError('Password cannot be empty')
        
        # Validate the password based off password policy
        pp = PasswordWithPolicy()
        pp.assess_password_strength(value)
        
        # If the password is valid, proceed. If not, raise an error and user needs a new password
        if pp.get_password_validation_status() == True:
            self._user_password = value
            pp.delete_password_data()
        else:
            self.delete_user_data()
            pp.delete_password_data()
            raise ValueError(pp.warning_message)

    # setter method 
    @user_email.setter 
    def user_email(self, value): 
        # Value must be a string and a valid email address
        if not isinstance(value, str) or not is_email(value, allow_gtld=True):
            raise ValueError('Email must be a valid email address')
        self._user_email = value                  

    # setter method
    @registration_date.setter
    def registration_date(self, value):
        # The value must be a datetime object, a recognizable date string, and not none
        if isinstance(value, datetime):
            self._registration_date = value
        elif isinstance(value, str):
            try:
                self._registration_date = parser.parse(value)
            except ValueError:
                raise ValueError('Could not parse the registration date. Ensure it contains a year, month, and day.')
        elif value is None:
            self._registration_date = value
        else:
            raise TypeError('Registration date must be a datetime object, a recognizable date string, or None')

    def get_user_id(self):
        """ 
        Function Name: get_user_id
        Function Description: This function gets the user id from the database
        """   
        # Set the table and column names
        table = 'TUsers'
        username_col = 'strUserName'
        id_col = 'intUserID'
        
        # SQL to fetch id for the given username
        sql = f"""
                SELECT 
                    {id_col}
                FROM 
                    {table}
                WHERE 
                    {username_col} = ?
                """

        # Execute the query to get the id
        db_qh = Database_Query_Handler()
        result = db_qh.get_target_db_record(sql, (self.username,))

        # Result should contain the user id
        if result is not None:
            User.user_id = result
        
    def validate_user_login_cred(self):
        """ 
        Function Name: validate_user_login_cred
        Function Description: This function validates the user login credentials
        """   
        # First get the user id
        self.get_user_id()
        
        # Set the table and column names
        table = 'TUsers'
        username_col = 'strUserName'
        password_col = 'strUserPassword'
        
        # SQL to fetch the hashed password from the database for the given username
        sql = f"""
                SELECT 
                    {password_col}
                FROM 
                    {table}
                WHERE 
                    {username_col} = ?
                """

        # Execute the query to get the hashed password
        db_qh = Database_Query_Handler()
        result = db_qh.get_target_db_record(sql, (self.username,))

        # Result should contain the hashed password
        hashed_password = result
            
        # Verify the user-provided password against the hashed password
        if PasswordWithPolicy.verify_password(self.user_password, hashed_password):
            # Get the user ID
            self.get_user_id()
            self.delete_user_data()
            return True
        else:
            self.delete_user_data()
            return False
        
    def validate_unique_user_login_cred(self):
        """ 
        Function Name: validate_unique_user_login_cred
        Function Description: This function validates the unique user login credentials
        """   
        # Set the table and column names
        table = 'TUsers'
        col_name_list = ['strUserName']
        
        # Execute the query to get all the records from the database
        db_qh = Database_Query_Handler()
        result = db_qh.get_all_db_record(col_name_list, table)

        # Verify the user-provided username against the database does not exist
        for i in result:
            if self.username in i:
                return False
        
        return True
        
    def add_new_user(self):
        """ 
        Function Name: add_new_user
        Function Description: This function adds a new user to the database
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
            self.username,
            PasswordWithPolicy.hash_password(self.user_password),
            self.user_email,
            todays_date,
            'New User Registration',
        ]
        prim_id = 'intUserID'
        
        # Package parameters
        params = (table_name, table_col_list, table_values_list, prim_id)
        
        # Call insert_or_update_values with the prepared parameters
        self.insert_or_update_values(params)
        
    def delete_user_data(self):
        """ 
        Function Name: delete_user_data
        Function Description: This function removes all the objects in the class
        """             
        #self._user_id = 0 if self.user_id == 0 else self.user_id
        self._user_id = 0
        self._username = ""
        self._user_password = ""
        self._user_email = ""
        self._registration_date = None 
        User.user_id_list = []   
