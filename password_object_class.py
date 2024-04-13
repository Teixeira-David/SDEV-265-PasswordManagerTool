"""
Project Name: Password Manager Tool
Developer: David Teixeira, Kara Jacobs, Jennifer Dillehay
Date: 03/28/2024
Abstract: This project is vol 0.0.1 for SDEV-265 Final Project. Please refer to the GitHub repository 
for the most up-to-date version.

    Repository: https://github.com/Teixeira-David/SDEV-265-PasswordManagerTool.git
    
    
    File Abstract: This file is the passwordd object class for all data structures and methods.
"""

# Import Python Libraries
import re
from tkinter import *
from tkinter import messagebox, ttk, Listbox
import tkinter as tk
from datetime import date, datetime, timedelta
import random
import string

# Import project modules



#######################################################################################################
# PasswordWithPolicy Class
#######################################################################################################         

class PasswordWithPolicy():
    """
    Class Name: Password
    Class Description: This class gets and sets password information 
    """
    # Establish Class Constants
    VALID_LENGTHS = [8, 10, 12, 16, 32]
    VALID_EXPIRY_PERIODS = [30, 90, 180, 365]
    
    # Common base class for all passwords information. Instantiates the base class
    def __init__(self, password_policy_id=0, char_min_length=8, include_uppercase=True, include_lowercase=True, 
                include_digits=True, include_special=True, expiry_period_length=30):
        self.password_policy_id = password_policy_id
        self.char_min_length = char_min_length
        self.include_uppercase = include_uppercase
        self.include_lowercase = include_lowercase
        self.include_digits = include_digits
        self.include_special = include_special
        self.expiry_period_length = expiry_period_length
        
        # Set the default values for the class attributes
        self.password = ""
        self.creation_date = datetime.now()
        self.expiry_date = self.creation_date + timedelta(days=self.expiry_period_length) # use timedelta to add days to the current date
         
    def generate_password(self):
        """
        Function Name: generate_password
        Description: Generate a random password based on the specified criteria.
        """
        # Get the character set 
        character_set = ''
        if self.include_uppercase:
            character_set += string.ascii_uppercase
        if self.include_lowercase:
            character_set += string.ascii_lowercase
        if self.include_digits:
            character_set += string.digits
        if self.include_special:
            character_set += string.punctuation

        # Convert the character set to a list for random sampling
        self.password = ''.join(random.choice(character_set) for _ in range(self.char_min_length))

    def is_password_expired(self):
        """
        Function Name: is_password_expired
        Description: Checks if the password has expired.
        """
        return datetime.now() > self.expiry_date

    def change_password(self, new_password):
        """
        Function Name: change_password
        Description: Changes the password if it meets the policy requirements.
        """
        if self.validate_password(new_password):
            self.password = new_password
            self.creation_date = datetime.now()  # Reset creation date
            self.set_expiry(self.expiry_period_length)  # Reset expiry date
            return True
        else:
            return False

    def update_policy(self, char_min_length=None, include_uppercase=None, include_lowercase=None, 
                      include_digits=None, include_special=None, expiry_period_length=None):
        """
        Function Name: update_policy
        Description: Updates the password policy based on provided arguments.
        """
        if char_min_length is not None:
            self.char_min_length = char_min_length
        if include_uppercase is not None:
            self.include_uppercase = include_uppercase
        if include_lowercase is not None:
            self.include_lowercase = include_lowercase
        if include_digits is not None:
            self.include_digits = include_digits
        if include_special is not None:
            self.include_special = include_special
        if expiry_period_length is not None:
            self.expiry_period_length = expiry_period_length
            self.set_expiry(self.expiry_period_length)  
                    
    def set_expiry(self, period_days):
        """
        Function Name: set_expiry
        Description: Set the expiry date of the password based on the period_days.
        """
        if period_days not in [30, 90, 180, 365]:
            raise ValueError("Invalid expiry period. Choose from 30, 90, 180, or 365 days.")
        
        # Set the expiry date of the password based on the period_days
        self.expiry_date = datetime.now() + timedelta(days=period_days)         

    def validate_password(self, password):
        """
        Function Name: validate_password
        Description: Validates a user-created password against the password policy.
        """
        # Create a list of all the possible conditions(bool) of the password policy and return 
        conditions = [
            len(password) >= self.char_min_length,
            any(c.isupper() for c in password) if self.include_uppercase else True,
            any(c.islower() for c in password) if self.include_lowercase else True,
            any(c.isdigit() for c in password) if self.include_digits else True,
            any(c in string.punctuation for c in password) if self.include_special else True
        ]
        return all(conditions)

    def assess_password_strength(self, password=None):
        """
        Function Name: assess_password_strength
        Description: Assess the strength of the password's password.
        Directly shows a messagebox if the password is weak with suggestions for improvement.
        """
        if password is None:
            password = self.password

        # Hide the root window
        root = tk.Tk()
        root.withdraw()  

        # Use policy attributes for dynamic validation
        if self.validate_password(password):
            messagebox.showinfo("Password Strength", "Your password meets the data protection policy and is considered strong.")
        else:
            suggestions = [
                "increase its length to at least {} characters".format(self.char_min_length),
                "include at least one digit" if self.include_digits else "",
                "include both uppercase and lowercase letters" if self.include_uppercase or self.include_lowercase else "",
                "include at least one special character" if self.include_special else ""
            ]
            suggestions = [s for s in suggestions if s]  # Remove empty suggestions
            warning_message = "Your password does not meet the data protection policy. Consider to " + ", ".join(suggestions) + "."
            messagebox.showwarning("Password Strength", warning_message)
                
    def delete_password_data(self):
        """ 
        Function Name: delete_password_data
        Function Description: This function removes all the objects in the class
        """   
        self._password = ""
        self._creation_date = datetime.now()
        self._expiry_date = None

