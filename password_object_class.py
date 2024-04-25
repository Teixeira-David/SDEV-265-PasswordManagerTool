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
import bcrypt
import hashlib
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
        self.valid_password = False
        self.creation_date = datetime.now()
        self.expiry_date = self.creation_date + timedelta(days=self.expiry_period_length) # use timedelta to add days to the current date
        
    @staticmethod
    def hash_password(password, cost=12):
        """ 
        Function Name: hash_password
        Function Description: Hash the password using bcrypt, applying a specified work factor (cost).
        
        Parameters:
        - password (str): The plain text password to hash.
        - cost (int): The cost factor that defines the complexity of the salt generation.
        
        Returns:
        - str: A hashed password which includes the salt.
        """
        # Convert the password to bytes
        password = password.encode()

        # Generate a salt with the specified cost factor
        salt = bcrypt.gensalt(rounds=cost)

        # Hash the password with the generated salt
        hashed_password = bcrypt.hashpw(password, salt)

        # Return the hashed password as a string to store in the database
        return hashed_password.decode()
    
    @staticmethod
    def verify_password(plain_password, hashed_password):
        """
        Verify that a plaintext password matches the hashed version.
        
        Parameters:
        - plain_password (str): The plain text password to verify.
        - hashed_password (str): The hashed password from the database.
        
        Returns:
        - bool: True if passwords match, False otherwise.
        """
        # Encode the plain password and hashed password to bytes
        plain_password = plain_password.encode()
        hashed_password = hashed_password.encode()

        # Use bcrypt to check if the hashed password matches the plain password
        return bcrypt.checkpw(plain_password, hashed_password)
    
    def generate_password(self):
        """
        Function Name: generate_password
        Description: Generate a random password based on the specified criteria.
        """
        # Declare Local Variables
        character_set = ''
        guaranteed_characters = []

        # Create a character set based on the password policy
        if self.include_uppercase:
            character_set += string.ascii_uppercase
            guaranteed_characters.append(random.choice(string.ascii_uppercase))
        
        if self.include_lowercase:
            character_set += string.ascii_lowercase
            guaranteed_characters.append(random.choice(string.ascii_lowercase))
        
        if self.include_digits:
            character_set += string.digits
            guaranteed_characters.append(random.choice(string.digits))
        
        if self.include_special:
            character_set += string.punctuation
            guaranteed_characters.append(random.choice(string.punctuation))
        
        # Calculate the remaining length after guaranteed characters
        remaining_length = self.char_min_length - len(guaranteed_characters)
        
        # Generate the rest of the password with random characters from the full set
        if remaining_length > 0:
            random_characters = [random.choice(character_set) for _ in range(remaining_length)]
            complete_password = guaranteed_characters + random_characters
        else:
            # In rare cases where char_min_length is exceeded by guaranteed characters, truncate appropriately
            complete_password = guaranteed_characters[:self.char_min_length]

        # Shuffle the complete password to remove any patterns
        random.shuffle(complete_password)
        self.password = ''.join(complete_password)

        #print(self.password)  # To see the output immediately for testing
        
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
            (len(password) >= self.char_min_length, "increase its length to at least {} characters".format(self.char_min_length)),
            (any(c.isupper() for c in password), "include at least one uppercase letter") if self.include_uppercase else (True, ""),
            (any(c.islower() for c in password), "include at least one lowercase letter") if self.include_lowercase else (True, ""),
            (any(c.isdigit() for c in password), "include at least one digit") if self.include_digits else (True, ""),
            (any(c in string.punctuation for c in password), "include at least one special character") if self.include_special else (True, "")
        ]
        #print(conditions)
        # Returns False and list of failed conditions if not all are True
        return all(cond[0] for cond in conditions), [cond[1] for cond in conditions if not cond[0]]

    def assess_password_strength(self, password=None):
        """
        Function Name: assess_password_strength
        Description: Assess the strength of the password's password.
        Directly shows a messagebox if the password is weak with suggestions for improvement.
        """
        # Hide the root window
        root = tk.Tk()
        root.withdraw()
        
        # If no password is provided, use the current password
        if password is None:
            password = self.password
            
        # Use policy attributes for dynamic validation
        valid, suggestions = self.validate_password(password)

        # Use policy attributes for dynamic validation
        if not valid:
            # Filter out empty suggestions and join the remaining with a comma
            suggestions = filter(None, suggestions)
            self.warning_message = ("Your password is considered weak and does not meet the data protection policy. "
                            "\n\nWe strongly recommend that you "
                            + ", ".join(suggestions) + " to enhance your security.\n\nPlease either create a new password or "
                            "update your password to meet our policy requirements.")
            self.set_password_invalid()
        else:
            self.set_password_valid()

    def delete_password_data(self):
        """ 
        Function Name: delete_password_data
        Function Description: This function removes all the objects in the class
        """   
        self._password = ""
        self._creation_date = datetime.now()
        self._expiry_date = None

    def set_password_valid(self):
        """ 
        Function Name: set_password_valid
        Function Description: This function sets the password to a valid state.
        """
        self.valid_password = True 
        
    def set_password_invalid(self):
        """ 
        Function Name: set_password_invalid
        Function Description: This function sets the password to an invalid state.
        """
        self.valid_password = False

    def get_password_validation_status(self):
        """ 
        Function Name: get_password_validation_status
        Function Description: This function gets the password state.
        """
        return self.valid_password