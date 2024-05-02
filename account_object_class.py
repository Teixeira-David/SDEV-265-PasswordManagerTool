"""
Project Name: Password Manager Tool
Developer: David Teixeira, Kara Jacobs, Jennifer Dillehay
Date: 03/28/2024
Abstract: This project is vol 0.0.1 for SDEV-265 Final Project. Please refer to the GitHub repository 
for the most up-to-date version.

    Repository: https://github.com/Teixeira-David/SDEV-265-PasswordManagerTool.git
    
    
    File Abstract: This file is the account object class for all data structures and methods.
"""

# Import Python Libraries
from pyisemail import is_email
import re
from tkinter import *
from tkinter import messagebox, ttk, Listbox
import tkinter as tk
from datetime import date, datetime, timedelta

# Import project modules
from database_script import Database_Query_Handler
from user_object_class import User
from password_object_class import PasswordWithPolicy

#######################################################################################################
# Account Class
#######################################################################################################         
class Account(User):
    """
    Class Name: Account
    Class Description: This class gets and sets Account information (fName, lName, Email)
    """
    # Create class variable shared amongst all Account methods
    account_id_list = []   
    
    # Common base class for all Accounts information. Instantiates the base class
    def __init__(self, account_id=0, user_id=0, account_name="", account_username="", account_password="",  account_email="", category="", notes=""):
        # Initialize User part of this Account
        super().__init__(user_id=user_id, username=account_username, user_password=account_password, user_email=account_email)
        self.user_id = user_id
        self.account_id = account_id
        self.account_name = account_name
        self.category = category
        self.notes = notes
        
    # Property decorator object get function to access private Account ID
    @property
    def account_id(self):
        return self._account_id

    # Property decorator object get function to access private User ID
    @property
    def user_id(self):
        return super().user_id
    
    # Property decorator object get function to access private Account name
    @property
    def account_name(self):
        return self._account_name

    # Property decorator object utilizing the user class setter
    @property
    def username(self):
        return super().username
    
    # Property decorator object utilizing the user class setter
    @property
    def user_password(self):
        return super().user_password         

    # Property decorator object utilizing the user class setter
    @property
    def user_email(self):
        return super().user_email

    # Property decorator object get function to access private category
    @property
    def category(self):
        return self._category
    
    # Property decorator object get function to access private category
    @property
    def notes(self):
        return self._notes
        
    # setter method 
    @account_id.setter 
    def account_id(self, value): 
        # The value should be an integer and greater than zero
        if not isinstance(value, int) or value < 0:
            raise ValueError('ID must be a non-negative integer')
        self._account_id = value

    # setter method 
    @user_id.setter 
    def user_id(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("User ID cannot contain 'specialcase'")
        self._user_id = value
        
    # setter method 
    @account_name.setter 
    def account_name(self, value): 
        # The value should be a string and not be empty. Can contain underscores and hyphens.
        if not isinstance(value, str) or value.isspace():
            raise ValueError('Account name must be a non-empty string')
        if not re.match(r"^[a-zA-Z0-9_-]+$", value):
            raise ValueError('Account name must be alphanumeric and can include underscores and hyphens')
        self._account_name = value

    # setter method 
    @username.setter 
    def username(self, value):
        if 'specialcase' in value:
            raise ValueError("Username cannot contain 'specialcase'")
        super(Account, Account).username.fset(self, value) # Call the User class's setter method

    # setter method 
    @user_password.setter 
    def user_password(self, value): 
        # Do additional checks specific to Account
        if 'specialcase' in value:
            raise ValueError("Password cannot contain 'specialcase'")
        # Use the User class's setter method
        super(Account, Account).user_password.fset(self, value)

    # setter method 
    @user_email.setter 
    def user_email(self, value): 
        # Do additional checks specific to Account
        if 'specialcase' in value:
            raise ValueError("Email cannot contain 'specialcase'")
        # Use the User class's setter method
        super(Account, Account).user_email.fset(self, value)                 

    # setter method 
    @category.setter 
    def category(self, value): 
        # The value must be a string and not empty
        if not isinstance(value, str) or value.isspace():
            raise ValueError('Category cannot be empty')
        self._category = value

    # setter method 
    @notes.setter 
    def notes(self, value): 
        # The value must be a string and can be empty.
        if not isinstance(value, str):
            raise ValueError('Notes must be a string')
        self._notes = value
    
    @staticmethod
    def get_all_account_info():
        """ 
        Function Name: get_all_account_info
        Function Description: This function gets all the account records from the database
        """   
        # Set the view query
        view = 'vAccountsInfo'
        
        # Execute the query to get all the records from the database
        return Account.fetch_all_db_records(view)

    @staticmethod
    def get_all_social_media_info():
        """ 
        Function Name: get_all_social_media_info
        Function Description: This function gets all the social media account records from the database
        """   
        # Set the view query
        view = 'vAccountsInfo_Social_Media'
        
        # Execute the query to get all the records from the database
        return Account.fetch_all_db_records(view)
    
    @staticmethod
    def get_all_web_service_info():
        """ 
        Function Name: get_all_web_service_info
        Function Description: This function gets all the web service account records from the database
        """   
        # Set the view query
        view = 'vAccountsInfo_Web_Services'
        
        # Execute the query to get all the records from the database
        return Account.fetch_all_db_records(view)
    
    @staticmethod
    def get_all_finance_info():
        """ 
        Function Name: get_all_finance_info
        Function Description: This function gets all the finance account records from the database
        """   
        # Set the view query
        view = 'vAccountsInfo_Finance'
        
        # Execute the query to get all the records from the database
        return Account.fetch_all_db_records(view)

    @staticmethod
    def get_all_personal_info():
        """ 
        Function Name: get_all_personal_info
        Function Description: This function gets all the personal account records from the database
        """   
        # Set the view query
        view = 'vAccountsInfo_Personal'
        
        # Execute the query to get all the records from the database
        return Account.fetch_all_db_records(view)

    @staticmethod
    def fetch_all_db_records(sql_view, col_name_list='*'):
        """ 
        Function Name: fetch_all_db_records
        Function Description: This function gets all the records from the database and returns the 
        results of the query.
        """   
        # Execute the query to get all the records from the database
        db_qh = Database_Query_Handler()
        result = db_qh.get_all_db_record(col_name_list, sql_view)

        return result

    @staticmethod
    def get_max_account_id():
        """ 
        Function Name: get_max_account_id
        Function Description: This function gets the max account id from the database
        """   
        # Set the table and column names
        table = 'TAccounts'
        id_col = 'intAccountID'
        
        # SQL to fetch id for the given username
        sql = f"SELECT MAX({id_col}) FROM {table}"

        # Execute the query to get the max id
        db_qh = Database_Query_Handler()
        max_id = db_qh.get_target_db_record(sql)

        # Result should contain the max id or None if no records exist
        return max_id if max_id is not None else 0
            
    def add_new_account(self):
        """ 
        Function Name: add_new_account
        Function Description: This function adds a new account to the database
        """   
        # Get the key for encrypting the password
        key = PasswordWithPolicy.get_key()
        
        # Get today's date in YYYY-MM-DD format
        todays_date = date.today().isoformat()
        
        # Define parameters for the insert_or_update_values method
        table_name = 'TAccounts'
        table_col_list = [
            'intAccountID', 
            'intUserID', 
            'strAppName', 
            'strAppUserName', 
            'strAppPassword', 
            'strAppEmail', 
            'strCategory', 
            'strNotes',
            'dtmLastUpdate',
            'strModifiedReason'
            ]
        table_values_list = [
            self.user_id,
            self.account_name,
            self.username,
            PasswordWithPolicy.encrypt_password(self.user_password, key=key),
            self.user_email,
            self.category,
            self.notes,
            todays_date,
            'New Account Registration',
        ]
        prim_id = 'intAccountID'
        
        # Package parameters
        params = (table_name, table_col_list, table_values_list, prim_id)
        # Call insert_or_update_values with the prepared parameters
        self.insert_or_update_values(params)
        
    def edit_account(self):
        """ 
        Function Name: edit_account
        Function Description: This function edits an old account to the database
        """   
        # Get the key for encrypting the password
        key = PasswordWithPolicy.get_key()
        
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
            'strModifiedReason'
            ]
        table_values_list = [
            self.user_id,
            self.account_name,
            self.username,
            PasswordWithPolicy.encrypt_password(self.user_password, key=key),
            self.user_email,
            self.category,
            self.notes,
            todays_date,
            'Edit Account Registration',
        ]
        prim_id = 'intAccountID'
        key_id = self.account_id
        
        # Package parameters
        params = (table_name, table_col_list, table_values_list, prim_id, key_id)
        # Call insert_or_update_values with the prepared parameters
        self.insert_or_update_values(params)
        
    def delete_account_data(self):
        """ 
        Function Name: delete_account_data
        Function Description: This function removes all the objects in the class
        """   
        self._account_id = 0
        self._account_name = ""
        self._account_username = ""
        self._account_password = ""
        self._account_email = ""
        self._category = "" 
        self._notes = ""
        Account.account_id_list = []   

