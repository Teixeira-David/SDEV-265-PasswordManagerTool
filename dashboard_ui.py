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
from tool_tip import CreateToolTip



#######################################################################################################
# Main Dashboard Ui Composable Class
#######################################################################################################

class MainDashboard_UiComposable(tk.Frame, Base_Ui_Methods):
    """
    Class Name: MainDashboard_UiComposable
    Class Description: This class is the main dashboard page of the program where the user 
    can choose to navigate through the various password detail pages and CRUD settings.
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
        # Initialize the paned_window_hidden to True so it starts hidden
        self.paned_window_hidden = True
        self.last_action = None
        self.currently_selected_icon = None
        self.is_favorites_clicked = False
        
        # Get the screen width and height 
        self.width_size = self.winfo_screenwidth() 
        self.height_size = self.winfo_screenheight()
        
        # Adjust the size as needed
        self.parent_ui_frame(self.width_size, self.height_size)
        
        # Call this method to set up the header frame
        self.set_dashboard_bg_img(self.width_size, self.height_size)
        
        # Create the file menu
        self.file_menu_composable()
        
        # Create the main container for dynamic columns
        self.primary_sidebar_composable()
        
        # Create the dynamic column 
        self.create_dynamic_column()

    def file_menu_composable(self):
        """
        Function Name: file_menu_composable
        Description: This function creates the file menu for the main Ui Dashboard fragment
        """
        # Create a menu bar
        self.menu_bar = tk.Menu(self.controller)
        
        # Add 'File' menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_menu_btn)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Add 'Edit' menu
        self.edit_menu_btn = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu_btn)

        # Add 'View' menu
        self.view_menu_btn = tk.Menu(self.menu_bar, tearoff=0)
        self.view_menu_btn.add_command(label="Zoom In", command=self.edit_menu_btn)
        self.menu_bar.add_cascade(label="View", menu=self.view_menu_btn)

        # Add 'Help' menu
        self.help_menu_btn = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu_btn)
        
        # Set the menu bar on the controller (root window)
        self.controller.config(menu=self.menu_bar)
        
    def new_menu_btn(self):
        """
        Function Name: new_menu_btn
        Description: This function is executed when the user clicks on the 'New' option in the file menu.
        """
        # Functionality to menu item
        messagebox.showinfo("New", "Create a new file...")

    def edit_menu_btn(self):
        """
        Function Name: edit_menu_btn
        Description: This function is executed when the user clicks on the 'Edit' option in the file menu.
        """
        # Functionality to menu item
        messagebox.showinfo("Edit", "Edit an account...")
        
    def view_menu_btn(self):
        """
        Function Name: view_menu_btn
        Description: This function is executed when the user clicks on the 'View' option in the file menu.
        """
        # Functionality to menu item
        messagebox.showinfo("View", "View and account...")
        
    def help_menu_btn(self):
        """
        Function Name: help_menu_btn
        Description: This function is executed when the user clicks on the 'Help' option in the file menu.
        """
        # Functionality to menu item
        messagebox.showinfo("Help", "Help needed with application...")

    def primary_sidebar_composable(self):
        """
        Function Name: primary_sidebar_composable
        Description: This function creates the sidebar for the main UI
        """
        # Create a sidebar frame
        self.sidebar = tk.Frame(self, width=200, bg='#dddddd')
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=0, pady=0)

        # Separately handle the settings icon to place it at the bottom
        self.create_icon_button('ic_favorite.png', "Favorites", self.load_favorites_composable)

        # Separately handle the settings icon to place it at the bottom
        self.create_icon_button('ic_setting.png', "Settings", self.load_settings_composable, place_bottom=True)

    def sub_sidebar_composable(self):
        """
        Function Name: sub_sidebar_composable
        Description: This function creates the sidebar for the main UI
        """
        # Define icon paths and corresponding tooltips, excluding the settings icon for now
        icon_info = [
            ('ic_all_accounts.png', "All Accounts", self.load_all_accounts_composable),
            ('ic_social_media.png', "Social Media", self.load_social_media_composable),
            ('ic_webservice.png', "Web Services", self.load_web_services_composable),
            ('ic_finance.png', "Finance", self.load_finance_composable),
            ('ic_personal.png', "Personal", self.load_personal_composable),
        ]

        # Load, resize icons, and create buttons with tooltips
        for icon_path, tooltip_text, action in icon_info:
            self.create_icon_button(icon_path, tooltip_text, action, sidebar='sub')

    def create_dynamic_column(self):
        """
        Function Name: create_dynamic_column
        Description: This function creates the dynamic column for the main UI
        """
        # Create the paned_window widget
        self.paned_window = ttk.Panedwindow(self, orient=tk.HORIZONTAL)
        
        # Create the dynamic column as a Frame
        self.dynamic_column = tk.Frame(self.paned_window, bg='#dddddd', width=60, highlightbackground='lightgrey', highlightthickness=0.5)
        
        # Add the dynamic column to the paned_window but don't pack it yet
        self.paned_window.add(self.dynamic_column, weight=1)

        # Keep commented out to ensure there is no re-sizeable handle
        # Create a handle for resizing
        self.handle = ttk.Separator(self.paned_window, orient=tk.VERTICAL)
        self.paned_window.add(self.handle, weight=0)

        # Bind the handle to a method that resizes the paned window
        self.handle.bind('<B1-Motion>', self.resize_pane)

    def resize_pane(self, event):
        """
        Function Name: resize_pane
        Description: This function resizes the pane based on the event
        """
        # Calculate the new width for the dynamic column
        new_width = event.x
        
        # Set minimum width to prevent the pane from becoming too small
        min_width = 200  # Minimum width in pixels
        if new_width < min_width:
            new_width = min_width
        
        # Adjust the width of the dynamic column
        self.dynamic_column.config(width=new_width)
        
        # Update the paned_window sash position
        self.paned_window.sash_place(0, new_width, 0)
        
    def create_icon_button(self, icon_path, tooltip_text, action, sidebar='primary', place_bottom=False):
        """
        Function Name: create_icon_button
        Description: Helper function to create an icon button with a tooltip.
        """
        icon = self.resize_Icon(icon_path)
        if sidebar == 'sub':
            button_canvas = tk.Canvas(self.dynamic_column, width=50, height=50, bg='#dddddd', highlightthickness=0, bd=0)
        else:
            button_canvas = tk.Canvas(self.sidebar, width=50, height=50, bg='#dddddd', highlightthickness=0, bd=0)
        if place_bottom:
            button_canvas.pack(side='bottom', pady=10)
        else:
            button_canvas.pack(pady=10)
        button_canvas.create_image(25, 25, image=icon)
        button_canvas.bind("<Button-1>", lambda event, a=action, btn=button_canvas: self.on_icon_click(event, a, btn))  # Bind to on_icon_click
        CreateToolTip(button_canvas, tooltip_text)
        button_canvas.image = icon  # Keep a reference to avoid garbage collection

    def on_icon_click(self, event, action, button_canvas):
        """ 
        Function Name: on_icon_click
        Description: This function toggles the paned window column and executes the action
        """
        # Reset background of previously selected icon if exists
        if self.currently_selected_icon:
            self.currently_selected_icon.configure(bg='#dddddd')  # Reset background to default
        # Highlight the currently selected icon
        button_canvas.configure(bg='lightblue')  # Highlight selection
        self.currently_selected_icon = button_canvas  # Update the reference to the currently selected icon
        
        # The rest of the logic remains the same
        if action == self.last_action and not self.paned_window_hidden:
            # Hide the paned window if the same action is triggered and it's currently visible
            self.show_or_hide_pane()
        else:
            # Show the paned window and populate options for any other cases
            if self.paned_window_hidden:
                self.show_or_hide_pane()
            action()  # Execute the corresponding action
        self.last_action = action  # Update the last action
        
    def show_or_hide_pane(self):
        """
        Function Name: show_or_hide_pane
        Description: Shows or hides the paned_window containing the dynamic column.
        """
        if self.paned_window_hidden:
            # If hidden, show the paned window
            self.paned_window.place(x=50, rely=0.0, relheight=1.0)
            self.paned_window_hidden = False
        else:
            # If shown, hide the paned window
            self.paned_window.place_forget()
            self.paned_window_hidden = True
            
    def resize_Icon(self, icon_path, size=(32, 32)):
        """
        Function Name: resize_Icon
        Description: This function resizes the icon to the specified width and height
        """        
        image = Image.open(icon_path)
        resized_image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(resized_image)

    def load_favorites_composable(self):
        """ 
        Function Name: load_favorites_composable
        Function Purpose: This function executes when the user clicks on 'settings' button to display the UI composable
        """
        # Get the bool status of the favorites btn clicked
        if self.is_favorites_clicked is False:
            print("load_favorites_composable triggered")   
            self.is_favorites_clicked = True
            self.sub_sidebar_composable()
        
    def load_settings_composable(self):
        """ 
        Function Name: load_settings_composable
        Function Purpose: This function executes when the user clicks on 'settings' button to display the UI composable
        """
        print("load_settings_composable triggered")   
        
    def load_all_accounts_composable(self):
        """ 
        Function Name: load_all_accounts_composable
        Function Purpose: This function executes when the user clicks on 'All Accounts' button to display the UI composable
        """
        print("load_all_accounts_composable triggered")

    def load_social_media_composable(self):
        """ 
        Function Name: load_social_media_composable
        Function Purpose: This function executes when the user clicks on 'Social Media' button to display the UI composable
        """
        print("load_social_media_composable triggered")
        
    def load_web_services_composable(self):
        """ 
        Function Name: load_web_services_composable
        Function Purpose: This function executes when the user clicks on 'Web Services' button to display the UI composable
        """
        print("load_web_services_composable triggered")
        
    def load_finance_composable(self):
        """ 
        Function Name: load_finance_composable
        Function Purpose: This function executes when the user clicks on 'Finance' button to display the UI composable
        """
        print("load_finance_composable triggered")
        
    def load_personal_composable(self):
        """ 
        Function Name: load_personal_composable
        Function Purpose: This function executes when the user clicks on 'Personal' button to display the UI composable
        """
        print("load_personal_composable triggered")               
            
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
            self.controller.show_frame("UserLogin_UiComposable")  
        
 