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
from dataclasses import dataclass

#######################################################################################################
# Data Model Class
#######################################################################################################  
@dataclass
class Crud_Account_Data:
    """
    Class Name: Crud_Account_Data
    Class Description: This class is the data model for the CRUD account data.
    """
    category: str = ""
    app_name: str = ""
    username: str = ""
    password: str = ""
    email: str = ""
    hint: str = ""  
    
    def get_all_data(self):
        """
        Function Name: get_all_data
        Function Purpose: Get all the data from the class in dictionary form
        """
        return [
            self.app_name,
            self.username,
            self.email,
            self.password,
            self.hint,
            self.category
        ]
