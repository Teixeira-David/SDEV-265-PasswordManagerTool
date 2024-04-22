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
from database_script import Database_File_Handler


#######################################################################################################
# Base Method Class
#######################################################################################################

class Base_Ui_Methods():
    """
    Class Name: Base_Ui_Methods
    Class Description: This is the base class for all the methods that are used in the application.
    """
    def __init__(self, *args, **kwargs):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes.
        """   
        self.frames = {}
        super().__init__(*args, **kwargs)
        
    def parent_ui_frame(self, frame_width, frame_height, bg_color='white'):
        """
        Function Name: parent_ui_frame
        Description: Creates a fixed-size frame for UI elements.
        """
        # Adjust the size as needed
        self.ui_frame = Frame(self, width=frame_width, height=frame_height, bg=bg_color)  
        self.ui_frame.pack_propagate(False)  # Prevents the frame from resizing to fit its contents
        self.ui_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame within the main_container
        
    def create_med_center_image_canvas(self, image_path, canvas_width, canvas_height, image_width, image_height, padding=20):
        """
        Function Name: create_image_canvas
        Description: Sets up the frame containing the application's logo in the center of the parent frame.
        """
        # Create a canvas for the shield logo at the top of the ui_frame
        self.canvas = Canvas(self.ui_frame, width=canvas_width, height=canvas_height, bg='white', highlightthickness=0)
        self.canvas.pack(pady=padding)
        
        # Load the logo image
        logo_path = image_path 
        self.shield_logo = Image.open(logo_path)
        self.shield_logo = self.shield_logo.resize((image_width, image_height), Image.Resampling.LANCZOS)
        self.shield_photoimage = ImageTk.PhotoImage(self.shield_logo)
        self.canvas.create_image(100, 100, image=self.shield_photoimage)
        
    def create_sml_ul_image_canvas(self, image_path, canvas_width, canvas_height, image_width, image_height, padding=20):
        """
        Function Name: create_sml_ul_image_canvas
        Description: Sets up the frame containing the application's logo in the upper left corner of the parent frame.
        """
        # Create a canvas for the image at the top of the ui_frame
        self.canvas = Canvas(self.ui_frame, width=canvas_width, height=canvas_height, bg='white', highlightthickness=0)
        self.canvas.place(x=padding[0], y=padding[1])
        
        # Load the logo image
        logo_path = image_path 
        self.shield_logo = Image.open(logo_path)
        self.shield_logo = self.shield_logo.resize((image_width, image_height), Image.Resampling.LANCZOS)
        self.shield_photoimage = ImageTk.PhotoImage(self.shield_logo)
        
        # Create the image on the canvas with the northwest (upper left) anchor
        self.canvas.create_image(0, 0, anchor="nw", image=self.shield_photoimage)
        
    def set_dashboard_bg_img(self, width_size, height_size):
        """
        Function Name: set_dashboard_bg_img
        Description: This function creates the background image for the main UI
        """
        # Set the flag to indicate the background image is hidden
        self.is_bg_img_hidden = False
        
        # Bind the resize event
        self.bind("<Configure>", self.on_window_resize) 
        
        # Load the image
        image_path = "ic_logo_med_bg_low_opacity.png"
        image = Image.open(image_path)

        # Convert the image to RGBA (if not already in this mode)
        image = image.convert("RGBA")

        # Process the image to remove white background
        datas = image.getdata()
        newData = []
        for item in datas:
            # Change all white (also shades of whites)
            # pixels to transparent
            if item[0] > 200 and item[1] > 200 and item[2] > 200:  # Adjust the RGB values as needed
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        # Update image with processed data
        image.putdata(newData)

        # Convert processed image for Tkinter
        self.bg_image = ImageTk.PhotoImage(image)

        # Create a Canvas for the background image
        self.bg_canvas = tk.Canvas(self.ui_frame, width=width_size, height=height_size)
        self.bg_canvas.pack(fill="both", expand=True)

        # Calculate the center position and place the image
        center_x = width_size // 2 - self.bg_image.width() // 2
        center_y = height_size // 2 - self.bg_image.height() // 2
        self.bg_image_id = self.bg_canvas.create_image(center_x, center_y, anchor="nw", image=self.bg_image)

    def remove_background_image(self):
        """
        Function Name: remove_background_image
        Description: This function removes the background image from the main UI.
        """
        # Set the flag to indicate the background image is hidden
        self.is_bg_img_hidden = True
        
        # Unbind the resize event
        self.bg_canvas.delete(self.bg_image_id)
        self.bg_canvas.destroy()
        
    def position_ui_frame(self):
        """
        Function Name: position_ui_frame
        Description: Creates a fixed-size frame for UI elements.
        """
        # Center ui_frame every time the window resizes
        self.ui_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Optionally, rebind the resize event to a new method that re-centers ui_frame
        self.bind("<Configure>", self.on_window_resize)

    def on_window_resize(self, event=None):
        """
        Function Name: on_window_resize
        Description: This function creates the background image window for the main UI
        """
        # Check if the canvas still exists before trying to modify it
        self.position_ui_frame()
        
    def destroy_child_frame(self):
        """ 
        Function Name: add_new_user
        Function Purpose: This function executes when the frame inside the main container will be destroyed.
        """
        # Destroy the UI Frame and its children widgets
        if hasattr(self, 'ui_frame') and self.ui_frame is not None:
            self.ui_frame.destroy()
            self.ui_frame = None # Set to None to prevent memory leaks

    def clear_entry_widget(self, entry_widgets, widget_index=0):
        """ 
        Function Name: clear_entry_widget
        Function Purpose: This function is executed if the user clicks 'clear' or 'reset'. The fields 
        should be deleted and their background color should be set to white. Always set the entry widget of 
        of the first element to have focus.
        """
        # Delete the content of the entry widgets
        for i, widget in enumerate(entry_widgets):
            widget.delete(0, END)
            # Set focus to the first widget in the list
            if i == widget_index:
                widget.focus()
                
    def set_bg_to_white(self, entry_widgets):
        """ 
        Function Name: set_bg_to_white
        Function Purpose: This function is executed if the user clicks 'clear' or 'reset'. The fields 
        should have their background color should be set to white.
        """
        # Clear out the background colors and set to default as 'white'
        for e in entry_widgets:
            e.configure(background='White')
        
    def set_bg_to_yellow(self, entry_widgets):
        """ 
        Function Name: set_bg_to_yellow
        Function Purpose: This function is executed if the user input is invalid. The fields 
        should have their background color should be set to yellow to indicate the invalid fields.
        """
        # Clear out the background colors and set to default as 'white'
        for e in entry_widgets:
            e.configure(background='Yellow')
            
    def set_invalid(self, widgets, msg=""):
        """
        Method Name: set_invalid
        Description: Highlights the input field to indicate invalid data and sets focus.
        """
        if isinstance(widgets, list):
            # If a list of widgets is provided
            self.clear_entry_widget(widgets)
            # Set the background color to yellow for all widgets
            self.set_bg_to_yellow(widgets)
        else:
            # Single widget provided
            widgets.delete(0, END)
            widgets.configure(background='Yellow')
            widgets.focus()

        # Display the error message
        if msg:
            messagebox.showwarning("Input Error", msg)
            
    def exit_app_btn(self):
        """ 
        Function Name: exit_app_btn
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """       
        # Display the user ask question to see if the user would like to exit the program
        if messagebox.askyesno(message="CAUTION! \n\n Would you like to exit the program?", icon='question'):          
            # Backup the database if the user closes the window
            Database_File_Handler.backup_volume(Database_File_Handler)
            sys.exit()

    def show_frame(self, frame_name):
        """
        Function Name: show_frame
        Description: This function shows the frame inside the main container
        """
        # Get the frame from the frame stack
        frame = self.frames.get(frame_name)
        if frame:
            frame.tkraise()  # Ensuring that the show method is called when the frame is raised
            if hasattr(frame, 'show'):
                frame.show()  # Call show method explicitly if defined in the frame
        else:
            print(f"No frame with name {frame_name} found.")
            
    def toggle_password(self, entry):
        """
        Function Name: toggle_password
        Description: This function toggles the visibility of the password in the entry widget.
        """
        if isinstance(entry, list):
            # Toggle the show attribute of the entry widget
            for e in entry:
                if e.cget('show') == '':
                    e.config(show='*')
                else:
                    e.config(show='')
        else:
            if entry.cget('show') == '':
                entry.config(show='*')
            else:
                entry.config(show='')

            
        