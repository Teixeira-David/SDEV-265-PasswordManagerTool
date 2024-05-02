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
import re
import sys
from tkinter import *
from tkinter import messagebox, ttk, Listbox
import tkinter as tk
from tkinter.font import Font
from datetime import date, datetime, timedelta
from PIL import Image, ImageTk

# Import project modules
from account_object_class import Account
from tool_tip import CreateToolTip
from base_account_ui_methods import Base_AccountInfo_UiComposable

#######################################################################################################
# View Account Information Class
#######################################################################################################  

class View_All_Accounts_UiComposable(tk.Frame):
    """
    Class Name: View_All_Accounts_UiComposable
    Class Description: This class views all of the user's account information.
    """
    def __init__(self, parent, controller, *args, **kwargs):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """   
        # Create the root tkinter variable
        super().__init__(parent, *args, **kwargs)
        self.controller = controller 
        self.parent = parent

        # Set the tag name that controls what to load
        self.tag = "Account_Info"
        
        # Instantiate the base account ui composable
        self.ba_ui = Base_AccountInfo_UiComposable(parent=self.parent, controller=self.controller, tag=self.tag)
        
        # Create the main Ui Frame
        self.ba_ui.create_ui_frame()   

    def destroy_ui_composable(self):
        """ 
        Function Name: destroy_ui_composable
        Function Purpose: This function executes when the user clicks away from the current composable
        """
        self.ba_ui.destroy_base_composable()
        
class View_SocialMedia_Accounts_UiComposable(tk.Frame):
    """
    Class Name: View_All_Accounts_UiComposable
    Class Description: This class views all of the user's account information.
    """
    def __init__(self, parent, controller, *args, **kwargs):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """   
        # Create the root tkinter variable
        super().__init__(parent, *args, **kwargs)
        self.controller = controller 
        self.parent = parent

        # Set the tag name that controls what to load
        self.tag = "Social_Media"
        
        # Instantiate the base account ui composable
        self.ba_ui = Base_AccountInfo_UiComposable(parent=self.parent, controller=self.controller, tag=self.tag)
        
        # Create the main Ui Frame
        self.ba_ui.create_ui_frame()   

    def destroy_ui_composable(self):
        """ 
        Function Name: destroy_ui_composable
        Function Purpose: This function executes when the user clicks away from the current composable
        """
        self.ba_ui.destroy_base_composable()

class View_WebService_Accounts_UiComposable(tk.Frame):
    """
    Class Name: View_All_Accounts_UiComposable
    Class Description: This class views all of the user's account information.
    """
    def __init__(self, parent, controller, *args, **kwargs):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """   
        # Create the root tkinter variable
        super().__init__(parent, *args, **kwargs)
        self.controller = controller 
        self.parent = parent

        # Set the tag name that controls what to load
        self.tag = "Web_Service"
        
        # Instantiate the base account ui composable
        self.ba_ui = Base_AccountInfo_UiComposable(parent=self.parent, controller=self.controller, tag=self.tag)
        
        # Create the main Ui Frame
        self.ba_ui.create_ui_frame()   

    def destroy_ui_composable(self):
        """ 
        Function Name: destroy_ui_composable
        Function Purpose: This function executes when the user clicks away from the current composable
        """
        self.ba_ui.destroy_base_composable()
        
class View_Fiance_Accounts_UiComposable(tk.Frame):
    """
    Class Name: View_All_Accounts_UiComposable
    Class Description: This class views all of the user's account information.
    """
    def __init__(self, parent, controller, *args, **kwargs):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """   
        # Create the root tkinter variable
        super().__init__(parent, *args, **kwargs)
        self.controller = controller 
        self.parent = parent

        # Set the tag name that controls what to load
        self.tag = "Finance"
        
        # Instantiate the base account ui composable
        self.ba_ui = Base_AccountInfo_UiComposable(parent=self.parent, controller=self.controller, tag=self.tag)
        
        # Create the main Ui Frame
        self.ba_ui.create_ui_frame()   

    def destroy_ui_composable(self):
        """ 
        Function Name: destroy_ui_composable
        Function Purpose: This function executes when the user clicks away from the current composable
        """
        self.ba_ui.destroy_base_composable()
        
class View_Personal_Accounts_UiComposable(tk.Frame):
    """
    Class Name: View_Personal_Accounts_UiComposable
    Class Description: This class views all of the user's account information.
    """
    def __init__(self, parent, controller, *args, **kwargs):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """   
        # Create the root tkinter variable
        super().__init__(parent, *args, **kwargs)
        self.controller = controller 
        self.parent = parent

        # Set the tag name that controls what to load
        self.tag = "Personal"
        
        # Instantiate the base account ui composable
        self.ba_ui = Base_AccountInfo_UiComposable(parent=self.parent, controller=self.controller, tag=self.tag)
        
        # Create the main Ui Frame
        self.ba_ui.create_ui_frame()   

    def destroy_ui_composable(self):
        """ 
        Function Name: destroy_ui_composable
        Function Purpose: This function executes when the user clicks away from the current composable
        """
        self.ba_ui.destroy_base_composable() 