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
from tkinter import messagebox, ttk, Listbox
import tkinter as tk
from datetime import date, datetime, timedelta
from dateutil import parser

# Import project modules




#######################################################################################################
# User Class
#######################################################################################################         
class User():
    """
    Class Name: User
    Class Description: This class gets and sets User information 
    """
    # Create class variable shared amongst all User methods
    auser_id = []   
    
    # Common base class for all Users information. Instantiates the base class
    def __init__(self, user_id=0, username="", user_password="",  user_email="", registration_date=None):
        self.user_id = user_id
        self.username = username
        self.user_password = user_password
        self.user_email = user_email 
        self.registration_date = registration_date
        
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
            raise ValueError('Password cannot be empty')
        self._user_password = value

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

    def delete_user_data(self):
        """ 
        Function Name: delete_user_data
        Function Description: This function removes all the objects in the class
        """   
        self._user_id = 0
        self._username = ""
        self._user_password = ""
        self._user_email = ""
        self._registration_date = None 
        User.auser_id = []   
