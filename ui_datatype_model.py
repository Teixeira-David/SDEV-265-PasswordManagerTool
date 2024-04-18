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
from enum import Enum

#######################################################################################################
# Ui Data Type State Class
#######################################################################################################  
class ItemType(Enum):
    """
    Class Name: ItemType
    Class Description: This Enum class sets the enumeration types for the items
    """    
    SETTINGS = ("Settings", "Rope")
    FAVORITES = ("Favorites", "Device")
    SOCIAL_MEDIA = ("Social Media", "Device")
    WEB_SERVICES = ("Web Services", "Device")
    FINANCES = ("Finance", "Harness")
    PERSONAL = ("Personal", "Device")
    
    def __init__(self, type_name, label):
        self.type_name = type_name
        self.label = label