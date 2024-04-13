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

# Import project modules
from user_object_class import User
from password_object_class import PasswordWithPolicy
from base_methods import Base_Ui_Methods



#######################################################################################################
# Custom Password Generator Class
#######################################################################################################

class CustomPasswordGen_UiComposable(tk.Frame, Base_Ui_Methods, PasswordWithPolicy):
    """
    Class Name: CustomPasswordGen_UiComposable
    Class Description: This class is the custom password generator page of the program where the user 
    can create a custom password based of provided parameters.
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
        Description: This function creates the labels for the  UI
        """
        # Stylize labels to match the image
        Label(self.ui_frame, text="Generate Custom Password", bg='white').place(relx=0.34, y=110, anchor="e")
        Label(self.ui_frame, text="Character Length:", bg='white').place(relx=0.33, y=160, anchor="e")
        Label(self.ui_frame, text="Character Set:", bg='white').place(relx=0.33, y=220, anchor="e")
        Label(self.ui_frame, text="Expiry Period:", bg='white').place(relx=0.33, y=280, anchor="e")

    def create_entry_fields(self):
        """
        Function Name: create_entry_fields
        Description: This function creates the entry fields (radio and combo box) for the UI
        """
        # Create labels and radio buttons for Character Length
        self.set_char_len_rb_buttons()

        # Create labels and checkboxes for Character Set
        self.set_char_set_chk_buttons()

        # Create labels and radio buttons for Expiry Period
        self.set_expiry_period_rb_buttons()
            
    def set_char_len_rb_buttons(self, base_relx=0.35, bg_color='white'):
        """
        Function Name: set_char_len_rb_buttons
        Description: This function creates the radio buttons for the character length
        """
        # Create and place entry fields to match 
        rb_char_len_list = (8,10,12,16,32)
        # Variables to hold the selected options
        self.rb_char_len_var = tk.IntVar(value=8)
        # Set the spacing for the buttons
        char_len_spacing = 0.125
        # Y-positions for the buttons
        y_pos_char_len = 160

        # Create labels and radio buttons for Character Length
        for i, option in enumerate(rb_char_len_list):
            tk.Label(
                self.ui_frame, 
                text=str(option),
                bg=bg_color
                ).place(relx=base_relx + (i*char_len_spacing+0.003), y=y_pos_char_len - 20)
            tk.Radiobutton(
                self.ui_frame,
                variable=self.rb_char_len_var,
                value=option,
                bg=bg_color
            ).place(relx=base_relx + i*char_len_spacing, y=y_pos_char_len)
            
    def set_char_set_chk_buttons(self, base_relx=0.35, bg_color='white'):
        """
        Function Name: set_char_set_chk_buttons
        Description: This function creates the check buttons for the character set
        """
        # Create and place entry fields to match 
        rb_char_set_list = ("Uppercase", "Lowercase", "Numerics", "Special Symbols")
        # Variables to hold the selected options
        self.rb_char_set_vars = {option: tk.BooleanVar(value=True) for option in rb_char_set_list}
        # Set the spacing for the buttons
        char_set_spacing = 0.130
        # Y-positions for the buttons
        y_pos_char_set = 220
 
         # Create labels and checkboxes for Character Set
        for i, option in enumerate(rb_char_set_list):
            tk.Label(
                self.ui_frame, 
                text=option,
                bg=bg_color
                ).place(relx=base_relx + i*char_set_spacing, y=y_pos_char_set - 20)
            tk.Checkbutton(
                self.ui_frame,
                variable=self.rb_char_set_vars[option],
                bg=bg_color
            ).place(relx=base_relx + i*char_set_spacing, y=y_pos_char_set)
            
    def set_expiry_period_rb_buttons(self, base_relx=0.35, bg_color='white'):
        """
        Function Name: set_expiry_period_rb_buttons
        Description: This function creates the radio buttons for the expiry period
        """
        # Create and place entry fields to match 
        rb_expiry_period_list = (30,90,180,365)
        # Variables to hold the selected options
        self.rb_expiry_period_var = tk.IntVar(value=30)
        # Set the spacing for the buttons
        expiry_spacing = 0.125
        # Y-positions for the buttons
        y_pos_expiry_period = 280

        # Create labels and radio buttons for Expiry Period
        for i, option in enumerate(rb_expiry_period_list):
            tk.Label(
                self.ui_frame, 
                text=f"{option} Days",
                bg=bg_color
                ).place(relx=base_relx + i*expiry_spacing, y=y_pos_expiry_period - 20)
            tk.Radiobutton(
                self.ui_frame,
                variable=self.rb_expiry_period_var,
                value=option,
                bg=bg_color
            ).place(relx=base_relx + i*expiry_spacing, y=y_pos_expiry_period)
        
    def create_buttons(self):
        """
        Function Name: create_buttons
        Description: This function creates the buttons for the UI
        """
        # Stylize buttons to match the image
        Button(self.ui_frame, text="Back", width=10, command=self.back_btn).place(relx=0.3, y=340, anchor="center")
        Button(self.ui_frame, text="Reset", width=10, command=self.clear_entry).place(relx=0.5, y=340, anchor="center")
        Button(self.ui_frame, text="Generate", width=10, command=self.generate_btn).place(relx=0.7, y=340, anchor="center")
                                                                                                            
    def get_user_input(self):
        """ 
        Function Name: get_user_input
        Function Purpose: This function gets and sets the user input.
        """   
        # Get the radio button selection
        char_len = self.rb_char_len_var.get()
        char_set = [option for option in self.rb_char_set_vars if self.rb_char_set_vars[option].get()]
        
        # Get the combo box selection
        expiry_period = self.rb_expiry_period_var.get()
        
        return char_len, char_set, expiry_period
            
    def generate_btn(self):
        """ 
        Function Name: generate_btn
        Function Purpose: This function is executed once the user selects the password parameters
        """
        try:
            # Attempt to create a newly custom password with the provided credentials and 
            # request user acceptance and prep for db dump
            self.generate_new_custom_password()
            
            # Delete the newly generated password so the data does not persist in some address in RAM
            
            
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
        # Set the entry radio and check boxes to default values
        self.rb_char_len_var.set(8) # Set the default value for the radio button or character length
        for option in self.rb_char_set_vars: # Set the default value for the character set
            self.rb_char_set_vars[option].set(True)
        self.rb_expiry_period_var.set(30) # Set the default value for the radio button or expiry period

    def generate_new_custom_password(self):
        """ 
        Function Name: generate_new_custom_password
        Function Purpose: This function executes when the user clicks on 'Generate' button to create a new custom password
        """
        # Initialize the character set boolean list
        char_bool_list = [False, False, False, False]
        
        # Define a mapping from character set names to their respective indices
        char_set_to_index = {
            "Uppercase": 0,
            "Lowercase": 1,
            "Numerics": 2,
            "Special Symbols": 3
        }
        
        # Get the user input
        self.usr_input_results = self.get_user_input()
        
        # Set the character length
        char_len = self.usr_input_results[0]
        
        # Set the character set booleans based on the user selected character sets
        for item in self.usr_input_results[1]:
            if item in char_set_to_index:
                char_bool_list[char_set_to_index[item]] = True
        
        # Set the expiry period
        expiry_period = self.usr_input_results[2]
        
        # Create the PasswordWithPolicy object with the specified parameters
        pwp = PasswordWithPolicy(0, char_min_length=char_len, include_uppercase=char_bool_list[0], 
                                include_lowercase=char_bool_list[1], include_digits=char_bool_list[2], 
                                include_special=char_bool_list[3], expiry_period_length=expiry_period)
        
        # Generate the password
        pwp.generate_password()
        
        # Display the newly generated password and gain user acceptance
        if messagebox.askyesno(message=f'ATTENTION! \n\n The newly generated password is: \n\n {pwp.password} \n\n Do you want to use this password?'):
            print("User accepted the new password")
            # Destroy the window and return to last page
            self.back_btn()
        else:
            print("User declined the new password")
            # Rest the entry fields
            self.clear_entry()

    def add_new_custom_password_btn(self):
        """ 
        Function Name: add_new_custom_password_btn
        Function Purpose: This function executes when the user accepts the newly created password.
        """
        print("Add new custom password")
        
    def back_btn(self, back_stack_frame=None):
        """ 
        Function Name: back_btn
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Back', the widow is destroyed and the user is sent back to the previous page 
        """       
        # Check if the back_stack_frame is not empty and if not direct controller to the back stack item behind 
        # the what is currently showing
        if back_stack_frame:
            self.controller.show_frame(back_stack_frame)
        else:
            self.controller.show_frame("AddNewUser_UiComposable")  
        
 