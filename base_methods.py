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


#######################################################################################################
# Base Method Class
#######################################################################################################

class Base_Ui_Methods():
    """
    Class Name: Base_Ui_Methods
    Class Description: This is the base class for all the methods that are used in the application.
    """
    crud_frame = {}
    standard_frame = {}
    
    def __init__(self, *args, **kwargs):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes.
        """ 
        self.frame_instances = {}
        super().__init__(*args, **kwargs)

    def parent_ui_frame(self, frame_width, frame_height, tag=None, bg_color='white'):
        """
        Function Name: parent_ui_frame
        Description: Creates a fixed-size frame for UI elements.
        """
        if tag != None:
            # Create a frame with the specified tag
            parent_frame = self.controller
        else:
            # Create a frame with the specified tag
            parent_frame = self
            
        # Adjust the size as needed
        self.ui_frame = Frame(parent_frame, width=frame_width, height=frame_height, bg=bg_color)  
        self.ui_frame.pack_propagate(False)  # Prevents the frame from resizing to fit its contents
        self.ui_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame within the main_container
        
    def create_med_center_image_canvas(self, image_path, canvas_width, canvas_height, image_width, image_height, padding=20, tag=None):
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
            # Change all white (also shades of whites) pixels to transparent
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
            sys.exit()

    def show_grid_frame(self, frame_name, frame_type='standard'):
        """
        Function Name: show_grid_frame
        Description: This function shows the frame inside the main container
        """
        # Select the correct frame dictionary based on frame_type
        frames_dict = self.get_crud_frame() if frame_type == 'crud' else self.get_frames()
        
        # Hide all frames first
        for i in frames_dict.values():
            # Hide all frames
            i.grid_remove()

        # Show the requested frame
        frame = frames_dict.get(frame_name)
        if frame:
            frame.grid()
            frame.tkraise()  # Bring the frame to the top
            if hasattr(frame, 'show'):
                frame.show()  # If the frame has a show method, call it
        else:
            print(f"No frame with name {frame_name} found.")
            
    def show_pack_frame(self, frame_name, frame_type='standard'):
        """
        Function Name: show_pack_frame
        Description: This function shows the frame inside the main container
        """
        # Select the correct frame dictionary based on frame_type
        frames_dict = self.get_crud_frame() if frame_type == 'crud' else self.get_frames()
        
        # Attempt to retrieve the frame from the appropriate dictionary
        frame = frames_dict.get(frame_name)
        
        # Hide all frames first
        for i in frames_dict.values():
            # Hide all frames
            i.pack_forget()

        # Show the requested frame
        if frame:
            frame.pack(fill='both', expand=True)
            frame.tkraise()  # Bring the frame to the top
            if hasattr(frame, 'show'):
                frame.show()  # If the frame has a show method, call it
            print(f"Showing frame: {frame_name} using pack.")
        else:
            print(f"No frame with name {frame_name} found.")

    def hide_grid_frame(self, frame_name, frame_type='frame'):
        """
        Function Name: hide_grid_frame
        Description: This function hides the specified frame.
        """
        # Select the correct frame dictionary based on frame_type
        frames_dict = self.get_crud_frame() if frame_type == 'crud' else self.get_frames()
        
        # Attempt to retrieve the frame from the appropriate dictionary
        for frame in frames_dict.values():
            if frame:
                print(f"Attempting to hide frame: {frame}")
                frame.grid_remove()
                print(f"Frame {frame} hidden.")
            else:
                print(f"No frame found with name {frame}")

    def hide_pack_frame(self, frame_name, frame_type='frame'):
        """
        Function Name: hide_pack_frame
        Description: This function hides the specified frame.
        """
        # Select the correct frame dictionary based on frame_type
        frames_dict = self.get_crud_frame() if frame_type == 'crud' else self.get_frames()
        
        # Attempt to retrieve the frame from the appropriate dictionary
        for frame in frames_dict.values():
            print(f"Attempting to hide frame: {frame_name}")
            frame.pack_forget()
            print(f"Frame {frame_name} hidden.")
        else:
            print(f"No frame with name {frame_name} found.")

    def show_child_frame(self, frame_name):
        """ 
        Function Name: show_child_frame
        Function Purpose: This function shows a specific frame by name that was previously hidden or needs to be brought to the foreground.
        
        Args:
        frame_name (str): The name of the frame to show.
        """
        # Attempt to retrieve the frame from the dictionary
        frame = self.crud_frame.get(frame_name)
        
        if frame:
            if hasattr(frame, 'ui_frame'):
                # Check if ui_frame exists and is not None
                if frame.ui_frame:
                    # Place the frame at the predefined location and configuration
                    frame.ui_frame.place(relx=0.5, rely=0.5, anchor="center")
                    frame.ui_frame.tkraise()  # Bring the ui_frame to the top
                    if hasattr(frame, 'show'):
                        frame.show()  # If the frame has a 'show' method, call it to update any necessary data or UI elements
                else:
                    print(f"ui_frame is initialized but None in {frame_name}.")
            else:
                print(f"{frame_name} exists but lacks an 'ui_frame' attribute.")
        else:
            print(f"No frame found with name {frame_name} in the standard_frame dictionary.")

    def destroy_child_frame(self):
        """ 
        Function Name: add_new_user
        Function Purpose: This function executes when the frame inside the main container will be destroyed.
        """
        # Destroy the UI Frame and its children widgets
        if hasattr(self, 'ui_frame') and self.ui_frame is not None:
            self.ui_frame.destroy()
            self.ui_frame = None # Set to None to prevent memory leaks

    def hide_child_frame(self):
        """ 
        Function Name: hide_child_frame
        Function Purpose: This function executes when the frame inside the main container will be hidden.
        """
        # Hide the UI Frame and retain its state
        if hasattr(self, 'ui_frame') and self.ui_frame is not None:
            self.ui_frame.place_forget()

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

    def set_frames(self, frame_name, frame_object):
        """
        Function Name: set_frames
        Description: This function sets the standard frames for the main UI.
        """
        self.standard_frame[frame_name] = frame_object
        print(f"Appended {frame_name} to STANDARD frames.")

    def get_frames(self):
        """
        Function Name: get_frames
        Description: This function sets the standard frames for the main UI.
        """
        return self.standard_frame
    
    def set_crud_frame(self, frame_name, frame_object):
        """
        Function Name: set_crud_frame
        Description: This function sets the CRUD frames for the main UI.
        """
        self.crud_frame[frame_name] = frame_object
        print(f"Appended {frame_name} to CRUD frames.")

    def get_crud_frame(self):
        """
        Function Name: set_crud_frame
        Description: This function sets the CRUD frames for the main UI.
        """
        return self.crud_frame
    
    def update_frame_data(self, frame_name, data):
        """
        Function Name: update_frame_data
        Description: This function updates the data in the specified frame.
        """
        if frame_name in self.crud_frame:
            self.crud_frame[frame_name].set_data(data)
        else:
            print(f"Frame {frame_name} not found.")
            
    def switch_composable(self, frame_class, frame_type='standard', data=None, *args, **kwargs):
        """
        Function Name: switch_composable
        Description: Hides the current frame and replaces it with a new one from the given frame class.
        If the frame already exists, it reuses it instead of creating a new one, making the
        transition more efficient.
        """
        # Select the correct frame dictionary based on frame_type
        frames_dict = self.get_crud_frame() if frame_type == 'crud' else self.get_frames()

        # Make sure frame_class is a callable class reference
        if not callable(frame_class):
            print(f"Invalid frame class: {frame_class}")
            return
        
        # Determine parameters based on frame type
        if frame_type == 'crud':
            class_params = (self.parent, self.controller, data) + args
        else:
            class_params = (self.parent, self.controller) + args

        # Hide and potentially destroy the current frame if it exists and is visible
        if hasattr(self, 'current_frame') and self.current_frame is not None:
            if frame_type == 'crud':
                #self.current_frame.pack_forget()
                self.destroy_child_frame()
            else:
                #self.current_frame.grid_remove()
                self.destroy_child_frame()
            print(f"Hid current frame: {type(self.current_frame).__name__}")

        # Check if the frame already exists in the dictionary; if not, create and store it
        if frame_class.__ne__ not in frames_dict:
            # Create and store the frame in the correct dictionary
            frame_instance = frame_class(*class_params, **kwargs)
            frames_dict[frame_class.__name__] = frame_instance
            print(f"Created new frame: {frame_class.__name__}")

        # Update the current_frame to the new one from the correct dictionary
        self.current_frame = frames_dict[frame_class.__name__]

        # Show the new frame
        if frame_type == 'crud':
            self.current_frame.pack(fill='both', expand=True)
        else:
            self.current_frame.grid(row=0, column=0, sticky="nsew")
        print(f"Loaded frame: {frame_class.__name__}")

    def destroy_all_composable(self):
        """ 
        Function Name: destroy_all_composable
        Purpose: Destroys all frame instances that were created during the program's execution. 
        """
        # Iterate over a copy of the list since to destroy it
        for key, frame in list(self.frame_instances.items()):
            frame.destroy()  # Assuming each instance has a destroy method
            print(f"Destroyed frame: {key}")
        self.frame_instances.clear()
        
    def register_frame_instance(self, frame_instance):
        """ 
        Function Name: register_frame_instance
        Purpose: Registers a frame instance to be managed for destruction. 
        """
        frame_key = frame_instance.__class__.__name__
        if frame_key not in self.frame_instances:
            self.frame_instances[frame_key] = frame_instance
            print(f"Frame registered: {frame_key}")
        else:
            print(f"Frame already registered: {frame_key}")

    def unregister_frame_instance(self, frame_instance):
        """ 
        Function Name: unregister_frame_instance
        Purpose: Unregisters a frame instance, typically called before manual destruction. 
        """
        frame_key = frame_instance.__class__.__name__
        if frame_key in self.frame_instances:
            del self.frame_instances[frame_key]
            print(f"Frame unregistered: {frame_key}")
        else:
            print(f"Frame not found: {frame_key}")