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
from PIL import Image, ImageTk
from pyisemail import is_email

# Import project modules
from user_object_class import User
from base_methods import Base_Ui_Methods
from password_object_class import PasswordWithPolicy



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
        self.controller = controller # Set the controller object for direction flow
        
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
            padding=20
            ) # Call the method to create the image frame
        
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
        return [username, password]
            
    def submit_btn(self):
        """ 
        Function Name: submit_btn
        Function Purpose: This function is executed once the user enters their user name and password
        """
        # First change the backgrounds to white
        self.set_bg_to_white(self.entry_widget_list)
        
        # Declare the Error Message
        error_msg = "Invalid Username or Password. Please try again."
        
        # Get the user input
        input_list = self.get_user_input()

        try:
            # Attempt to create a User object with the provided credentials
            usr_obj = User(username=input_list[0], user_password=input_list[1])
            
            # At this point, the input is valid as per our setters and need to check with the db if the values exist
            bln_flag = usr_obj.validate_user_login_cred()
            
            # Now check if the flag is true or false to proceed
            if bln_flag:
                # Delete the username and password entry fields so the data does not persist in some address in RAM
                self.clear_entry_widget(self.entry_widget_list)
                usr_obj.delete_user_data()
                
                # User input is valid and the user is authenticated proceed to the main dashboard
                self.controller.show_grid_frame("MainDashboard_UiComposable")
            else:
                # User input is invalid and the user is not authenticated
                self.set_invalid(self.entry_widget_list, error_msg)
                # Delete the username and password entry fields so the data does not persist in some address in RAM
                usr_obj.delete_user_data()
                return
        
        except ValueError as e:
            # Handle specific field errors based on message content
            if 'username' in str(e).lower():
                self.set_invalid(self.username_entry, str(e))
            elif 'password' in str(e).lower():
                self.set_invalid(self.password_entry, str(e))
            else:
                messagebox.showwarning("Input Error", str(e))                     
            
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
        self.controller.show_grid_frame("AddNewUser_UiComposable")
            
            
#######################################################################################################
# Add New User Class
#######################################################################################################

class AddNewUser_UiComposable(tk.Frame, Base_Ui_Methods, PasswordWithPolicy):
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
        self.controller = controller # Set the controller object for direction flow
        
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
        self.config_entry_fields()
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
            image_width=90, 
            image_height=90, 
            padding=(80,10)
            ) # Call the method to create the image frame
        
    def create_labels(self):
        """
        Function Name: create_labels
        Description: This function creates the labels for the main UI
        """
        # Stylize labels to match the image
        Label(self.ui_frame, text="New User Credentials:", bg='white').place(relx=0.32, y=110, anchor="e")
        Label(self.ui_frame, text="Username:", bg='white').place(relx=0.37, y=140, anchor="e")
        Label(self.ui_frame, text="Password:", bg='white').place(relx=0.37, y=180, anchor="e")
        Label(self.ui_frame, text="Password:", bg='white').place(relx=0.37, y=220, anchor="e")
        Label(self.ui_frame, text="Email:", bg='white').place(relx=0.37, y=260, anchor="e")

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
        self.username_entry.place(relx=0.57, y=140, anchor="center")
        self.first_password_entry.place(relx=0.57, y=180, anchor="center")
        self.second_password_entry.place(relx=0.57, y=220, anchor="center")
        self.email_entry.place(relx=0.57, y=260, anchor="center")
        
        # Create the entry widget list
        self.entry_widget_list = [
            self.username_entry, 
            self.first_password_entry, 
            self.second_password_entry, 
            self.email_entry
            ]

    def config_entry_fields(self):
        """
        Function Name: config_entry_fields
        Description: This function configures the entry fields for the main UI
        """
        # Set the placeholder text for the entry fields
        placeholders = {
            self.username_entry: "e.g. janedoe123",
            self.email_entry: "e.g. your_email@gmail.com",
        }
        # Ensure the placeholder text is displayed in the entry fields
        for entry, placeholder in placeholders.items():
            entry.insert(0, placeholder)
            entry.config(fg='grey')
            entry.bind("<FocusIn>", lambda event, e=entry, ph=placeholder: self.on_entry_click(event, e, ph))
            entry.bind("<FocusOut>", lambda event, e=entry, ph=placeholder: self.on_focus_out(event, e, ph))

    def create_buttons(self):
        """
        Function Name: create_buttons
        Description: This function creates the buttons for the main UI
        """
        # Button(self.ui_frame, text="Show", command=self.toggle_password(pswrd_widgets)).place(relx=0.20, y=180, anchor="center")
        Button(self.ui_frame, text="Show", command=self.show_password_btn).place(relx=0.8, y=180, anchor="center")
        
        # Stylize buttons to match the image
        # Button(self.ui_frame, text="Generate", width=10, command=self.generate_btn).place(relx=0.9, y=180, anchor="e")
        Button(self.ui_frame, text="Generate", width=10, command=self.generate_btn).place(relx=0.25, y=180, anchor="e")
        Button(self.ui_frame, text="Back", width=10, command=self.back_btn).place(relx=0.3, y=340, anchor="center")
        Button(self.ui_frame, text="Reset", width=10, command=self.clear_entry).place(relx=0.5, y=340, anchor="center")
        Button(self.ui_frame, text="Submit", width=10, command=self.submit_btn).place(relx=0.7, y=340, anchor="center")
        
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

        # Create a user object entry list of the input values
        return [username, first_password, second_password, email]
            
    def submit_btn(self):
        """ 
        Function Name: submit_btn
        Function Purpose: This function is executed once the user enters their user name and password
        """
        # Set all the backgrounds to white
        self.set_bg_to_white(self.entry_widget_list)
        
        # Declare the Error Message
        invalid_pswrd_msg = "Passwords do not match. Please try again."
        invalid_user_msg = "Username already exists. Please create a unique username and try again."
        
        # Get the user input
        input_list = self.get_user_input()

        # First check if the two user passwords are the same and if not, to return warning the user didn't 
        # enter the same password
        if input_list[1] != input_list[2]:
            self.set_invalid([self.first_password_entry, self.second_password_entry], invalid_pswrd_msg)
            return

        try:
            # Attempt to create a User object with the provided credentials
            usr_obj = User(username=input_list[0], user_password=input_list[1], user_email=input_list[3])
            
            # Validate unique username and email in the database
            if usr_obj.validate_unique_user_login_cred():
                response = messagebox.askyesno("Confirm New User", f"Proceed to add new user account '{input_list[0]}'?")
                if response:
                    usr_obj.add_new_user()
                    self.clear_entry_widget(self.entry_widget_list)
                    usr_obj.delete_user_data()
                    self.back_btn()
                else:
                    self.set_invalid([self.username_entry], invalid_user_msg)
            else:
                self.set_invalid([self.username_entry], invalid_user_msg)
            
        except ValueError as e:
            # Handle specific field errors based on message content
            if 'username' in str(e).lower():
                self.set_invalid(self.username_entry, str(e))
            elif 'password' in str(e).lower():
                self.set_invalid([self.first_password_entry, self.second_password_entry], str(e))
            elif 'email' in str(e).lower():
                self.set_invalid(self.email_entry, str(e))
            else:
                messagebox.showwarning("Input Error", str(e))                   
        
    def show(self):
        """
        Function Name: show
        Description: This method is called whenever this frame is raised to the top.
        It will check for a new password and fill the entry fields if available.
        """
        self.tkraise()  # Make sure the frame comes to the top
        self.load_generated_password()  # Load password into entry fields if available

    def load_generated_password(self):
        """
        Function Name: load_generated_password
        Function Purpose: This function loads the generated password into the entry fields
        """
        # This method can be called right after the frame is shown
        generated_password = self.controller.shared_data.get('generated_password')
        if generated_password:
            self.first_password_entry.delete(0, tk.END)
            self.first_password_entry.insert(0, generated_password)
            self.first_password_entry.config(show='*')
            self.second_password_entry.delete(0, tk.END)
            self.second_password_entry.insert(0, generated_password)
            self.second_password_entry.config(show='*')
                            
    def clear_entry(self):
        """ 
        Function Name: clear_entry
        Function Purpose: This function is executed if the user clicks clear. The fields should be deleted
        """
        # Delete the content of the entry widgets
        self.clear_entry_widget(self.entry_widget_list)
        self.set_bg_to_white(self.entry_widget_list)
        self.config_entry_fields()
        # Return focus to first input
        self.entry_widget_list[0].focus()
    
    def show_password_btn(self):
        """ 
        Function Name: show_password_btn
        Function Purpose: This function is executed once the user clicks on the 'show' button to reveal the password
        """       
        # Set the widget list
        pswrd_widgets = [self.first_password_entry, self.second_password_entry]

        # Call the method to toggle the password
        self.toggle_password(pswrd_widgets)
        
    def generate_btn(self):
        """ 
        Function Name: back_btn
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Back', the widow is destroyed and the user is sent back to the previous page 
        """       
        # Load the generate custom frame Ui
        self.controller.show_grid_frame("CustomPasswordGen_UiComposable")
        
    def back_btn(self):
        """ 
        Function Name: back_btn
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Back', the widow is destroyed and the user is sent back to the previous page 
        """    
        # Clear all entry fields
        self.clear_entry()
        
        # Optionally, clear any shared data related to this frame
        if 'generated_password' in self.controller.shared_data:
            del self.controller.shared_data['generated_password']
        
        # Navigate back to the login frame
        self.controller.show_grid_frame("UserLogin_UiComposable")       