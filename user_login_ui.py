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
from datetime import date, datetime, timedelta
import random
import string
from PIL import Image, ImageTk

# Import project modules
from user_object_class import User
from password_object_class import PasswordWithPolicy
from base_methods import Base_Ui_Methods




#######################################################################################################
# User Login Class
#######################################################################################################

class UserLogin_UiComposable(tk.Frame, Base_Ui_Methods):
    """
    Class Name: UserLogin_UiComposable
    Class Description: This class is the main start up page of the program where the user logs into the program.
    """
    def __init__(self, parent, controller, *args, **kwargs):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """            
        # Create the root tkinter variable
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        
        # Create the main Ui Frame
        self.create_ui_frame()    

    def create_ui_frame(self):
        """
        Function Name: create_ui_frame
        Description: Creates a fixed-size frame for UI elements.
        """
        # Adjust the size as needed
        self.parent_ui_frame(600, 400)
        
        # Call this method to set up the header frame
        self.create_logo_image()
        
        # Call the methods to set labels, entry fields, and buttons within this ui_frame 
        self.create_labels()
        self.create_entry_fields()
        self.create_buttons()

    def create_logo_image(self):
        """
        Function Name: create_logo_image
        Description: Sets up the frame containing the application's logo.
        """
        logo_path = "ic_logo_small_medium.png" # logo file path. Should be stored in cwd
        self.create_med_center_image_canvas(
            image_path=logo_path, 
            canvas_width=200, 
            canvas_height=200, 
            image_width=200, 
            image_height=200, 
            padding=20) # Call the method to create the image frame
        
    def create_labels(self):
        """
        Function Name: create_labels
        Description: This function creates the labels for the main UI
        """
        # Stylize labels to match the image
        Label(self.ui_frame, text="Username:", bg='white').place(relx=0.4, y=240, anchor="e")
        Label(self.ui_frame, text="Password:", bg='white').place(relx=0.4, y=280, anchor="e")

    def create_entry_fields(self):
        """
        Function Name: create_entry_fields
        Description: This function creates the entry fields for the main UI
        """
        # Create and place entry fields to match the image, centered
        self.username_entry = Entry(self.ui_frame, width=30)
        self.password_entry = Entry(self.ui_frame, width=30, show='*')
        
        # Position the entry fields at the center
        self.username_entry.place(relx=0.6, y=240, anchor="center")
        self.password_entry.place(relx=0.6, y=280, anchor="center")
        
        # Create the entry widget list
        self.entry_widget_list = [self.username_entry, self.password_entry]
        
    def create_buttons(self):
        """
        Function Name: create_buttons
        Description: This function creates the buttons for the main UI
        """
        # Stylize buttons to match the image
        Button(self.ui_frame, text="Exit", width=10, command=self.exit_app_btn).place(relx=0.3, y=340, anchor="center")
        Button(self.ui_frame, text="New", width=10, command=self.add_new_user_btn).place(relx=0.5, y=340, anchor="center")
        Button(self.ui_frame, text="Submit", width=10, command=self.submit_btn).place(relx=0.7, y=340, anchor="center")
                                                                                                            
    def get_user_input(self):
        """ 
        Function Name: get_user_input
        Function Purpose: This function gets and sets the user input.
        """   
        # This function would actually get input from GUI fields or console input
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Call the function to validate the user input
        self.validate_and_set_user_info(username, password)
            
    def submit_btn(self):
        """ 
        Function Name: submit_btn
        Function Purpose: This function is executed once the user enters their user name and password
        """
        # Get the user input
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            # Attempt to create a User object with the provided credentials
            user = User(username=username, user_password=password)
            
            # At this point, the input is valid as per our setters
            
            # Now you would proceed with a database check here for getting the primary key ID's
            
            # Set the user content and prep for db dump
            
            # Delete the username and password entry fields so the data does not persist in some address in RAM
            
            # Destroy the window and open the main dashboard
            
            
        except ValueError as e:
            # If setters raise a ValueError, inform the user
            messagebox.showwarning("Input Error", str(e))
            # Here, clear the entries or highlight them to indicate an error
            self.set_bg_to_white(self.entry_widget_list)                     
            
    def clear_entry(self):
        """ 
        Function Name: clear_entry
        Function Purpose: This function is executed if the user clicks clear. The fields should be deleted
        """
        # Delete the content of the entry widgets
        self.clear_entry_widget(self.entry_widget_list)
        self.set_bg_to_white(self.entry_widget_list)
        
        # Return focus to first input
        self.entry_widget_list[0].focus()

    def add_new_user_btn(self):
        """ 
        Function Name: add_new_user_btn
        Function Purpose: This function executes when the user clicks on 'New' button to add a new user
        """
        self.controller.show_frame("AddNewUser_UiComposable")
            
            
#######################################################################################################
# Add New User Class
#######################################################################################################

class AddNewUser_UiComposable(tk.Frame, Base_Ui_Methods):
    """
    Class Name: AddNewUser_UiComposable
    Class Description: This class is the to add a new user to the application.
    """
    def __init__(self, parent, controller, *args, **kwargs):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """            
        # Create the root tkinter variable
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        
        # Create the main Ui Frame
        self.create_ui_frame()    

    def create_ui_frame(self):
        """
        Function Name: create_ui_frame
        Description: Creates a fixed-size frame for UI elements.
        """
        # Adjust the size as needed
        self.parent_ui_frame(600, 400)
        
        # Call this method to set up the header frame
        self.create_logo_image()
        
        # Call the methods to set labels, entry fields, and buttons within this ui_frame 
        self.create_labels()
        self.create_entry_fields()
        self.create_buttons()

    def create_logo_image(self):
        """
        Function Name: create_logo_image
        Description: Sets up the frame containing the application's logo.
        """
        logo_path = "ic_logo_small_medium.png" # logo file path. Should be stored in cwd
        self.create_sml_ul_image_canvas(
            image_path=logo_path, 
            canvas_width=100, 
            canvas_height=100, 
            image_width=75, 
            image_height=75, 
            padding=20) # Call the method to create the image frame
        
    def create_labels(self):
        """
        Function Name: create_labels
        Description: This function creates the labels for the main UI
        """
        # Stylize labels to match the image
        Label(self.ui_frame, text="Username:", bg='white').place(relx=0.4, y=240, anchor="e")
        Label(self.ui_frame, text="Password:", bg='white').place(relx=0.4, y=280, anchor="e")
        Label(self.ui_frame, text="Password:", bg='white').place(relx=0.4, y=320, anchor="e")
        Label(self.ui_frame, text="Email:", bg='white').place(relx=0.4, y=360, anchor="e")

    def create_entry_fields(self):
        """
        Function Name: create_entry_fields
        Description: This function creates the entry fields for the main UI
        """
        # Create and place entry fields to match the image, centered
        self.username_entry = Entry(self.ui_frame, width=30)
        self.first_password_entry = Entry(self.ui_frame, width=30, show='*')
        self.second_password_entry = Entry(self.ui_frame, width=30, show='*')
        self.email_entry = Entry(self.ui_frame, width=30)
        
        # Position the entry fields at the center
        self.username_entry.place(relx=0.6, y=240, anchor="center")
        self.first_password_entry.place(relx=0.6, y=280, anchor="center")
        self.second_password_entry.place(relx=0.6, y=320, anchor="center")
        self.email_entry.place(relx=0.6, y=360, anchor="center")
        
        # Create the entry widget list
        self.entry_widget_list = [
            self.username_entry, 
            self.first_password_entry, 
            self.second_password_entry, 
            self.email_entry
            ]
        
    def create_buttons(self):
        """
        Function Name: create_buttons
        Description: This function creates the buttons for the main UI
        """
        # Stylize buttons to match the image
        Button(self.ui_frame, text="Exit", width=10, command=self.back_btn).place(relx=0.3, y=340, anchor="center")
        #Button(self.ui_frame, text="New", width=10, command=self.add_new_user_btn).place(relx=0.5, y=340, anchor="center")
        #Button(self.ui_frame, text="Submit", width=10, command=self.submit_btn).place(relx=0.7, y=340, anchor="center")
                                                                                                            
    def get_user_input(self):
        """ 
        Function Name: get_user_input
        Function Purpose: This function gets and sets the user input.
        """   
        # This function would actually get input from GUI fields or console input
        username = self.username_entry.get()
        first_password = self.first_password_entry.get()
        second_password = self.second_password_entry.get()
        email = self.email_entry.get()
        
        # Call the function to validate the user input

        # If valid, create a User object with the input
        self.user_input_list = [username, first_password, second_password, email]
            
    def submit_button_click(self):
        """ 
        Function Name: submit_button_click
        Function Purpose: This function is executed once the user enters their user name and password
        """
        # Get the valid user input
        

        try:
            # Attempt to create a User object with the provided credentials
            print("User object created")
            # At this point, the input is valid as per our setters
            
            # Now you would proceed with a database check here for getting the primary key ID's
            
            # Set the user content and prep for db dump
            
            # Delete the username and password entry fields so the data does not persist in some address in RAM
            
            # Destroy the window and open the main dashboard
            
            
        except ValueError as e:
            # If setters raise a ValueError, inform the user
            messagebox.showwarning("Input Error", str(e))
            # Here, clear the entries or highlight them to indicate an error
            self.set_bg_to_white(self.entry_widget_list)                     
            
    def clear_entry(self):
        """ 
        Function Name: clear_entry
        Function Purpose: This function is executed if the user clicks clear. The fields should be deleted
        """
        # Delete the content of the entry widgets
        self.clear_entry_widget(self.entry_widget_list)
        self.set_bg_to_white(self.entry_widget_list)
        
        # Return focus to first input
        self.entry_widget_list[0].focus()

    def add_new_user(self):
        """ 
        Function Name: add_new_user
        Function Purpose: This function executes when the user clicks on 'New' button to add a new user
        """
        # Destroy the UI Frame and its children widgets
        self.destroy_child_frame()
        
        # Create the new user frame
        
    def back_btn(self):
        """ 
        Function Name: back_btn
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Back', the widow is destroyed and the user is sent back to the previous page 
        """       
        # Hide the existing components inside the main container
        for widget in self.winfo_children():
            widget.pack_forget()
            
            # Load the frame that was previously displayed
            login_screen = UserLogin_UiComposable()            