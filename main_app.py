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
import sys
from tkinter import *
import tkinter as tk

# Import project modules
from base_methods import Base_Ui_Methods
from user_login_ui import UserLogin_UiComposable, AddNewUser_UiComposable
from database_script import Database, Database_File_Handler
from generate_password_ui import CustomPasswordGen_UiComposable
from dashboard_ui import MainDashboard_UiComposable


#######################################################################################################
# Main Ui Composable Class
#######################################################################################################

class Main_UiComposable(tk.Tk, Base_Ui_Methods):
    """
    Class Name: Main_UiComposable
    Class Description: This class is the main frame of the program.
    """
    def __init__(self, *args, **kwargs):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """               
        # Create the root tkinter variable
        super().__init__(*args, **kwargs)
        
        # Set the window to open with the full screen width and height
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        
        # Set the maximized state of the window
        self.state('zoomed')  
                
        # Create the Window attributes
        self.title("Cipher Shield v0.0.1")
        self.resizable(True, True)
        
        # Create the main container
        self.create_main_container()    
        
        # Set the shared data variable
        self.shared_data = {}
        
        # Create the main frame directory
        self.init_frames()
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()    
        
        # Exit the program if the user closes the window
        sys.exit()      

    def create_main_container(self):
        """
        Function Name: create_main_container
        Description: This function creates the main container for the main UI
        """
        # Main container for the main UI
        self.main_container = Frame(self)
        self.main_container.pack(fill="both", expand=True)
        
    def init_frames(self):
        """
        Function Name: init_frames
        Description: This function creates the frame container stack for the main UI
        """
        # Create the frames for the main UI
        frame_classes = [
            UserLogin_UiComposable, 
            AddNewUser_UiComposable, 
            CustomPasswordGen_UiComposable,
            MainDashboard_UiComposable
        ]

        # Initialize frames
        self.standard_frame = {}

        # Iterate over frame classes and instantiate each one
        for FrameClass in frame_classes:
            frame = FrameClass(parent=self.main_container, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")
            frame.grid_remove()  # Initially remove from grid
            self.standard_frame[FrameClass.__name__] = frame  # Add the frame to the stack
        
        # Set the container to allow frames to expand and fill
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

        # Initialize and setup the MainDashboard_UiComposable frame
        dash = self.standard_frame['MainDashboard_UiComposable']
        dash.create_ui_frame()  # Setup the MainDashboard
        
        # Show initial frame
        #self.show_grid_frame("MainDashboard_UiComposable")
        self.show_grid_frame("UserLogin_UiComposable")
    
def init_primary_boot_methods():
    """ 
    Function Name: init_primary_boot_methods
    Function Description: This function holds all the main methods for the program
    """
    # Call the database attribute method
    Database.db_set_database_attr(Database)
    
    # Start the main GUI window  
    root = Main_UiComposable()  
    
#######################################################################################################
# Main Start of Program
#######################################################################################################         

def Main():
    """ 
    Function Name: Main Start Program
    Function Description: This function begins the program. Open the GUI launch Page
    """
    try:
        # Start the main GUI window  
        init_primary_boot_methods()

    # Display error message if the entry is invalid
    except Exception as err:
        print("Exception occurred because", err)
    finally:
        # Backup the database if the user closes the window
        Database_File_Handler.backup_volume(Database_File_Handler)
# This is the start of main program
if __name__ == '__main__':
    Main()