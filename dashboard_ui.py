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
from base_methods import Base_Ui_Methods
from tool_tip import CreateToolTip
from view_account_ui_composable import View_All_Accounts_UiComposable, View_SocialMedia_Accounts_UiComposable
from view_account_ui_composable import View_WebService_Accounts_UiComposable, View_Fiance_Accounts_UiComposable, View_Personal_Accounts_UiComposable

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
        self.parent = parent
        # Create the main Ui Frame
        #self.create_ui_frame()    

    def create_ui_frame(self):
        """
        Function Name: create_ui_frame
        Description: Creates a fixed-size frame for UI elements.
        """ 
        # Initialize the paned_window_hidden to True so it starts hidden
        self.paned_window_hidden = True
        self.last_action = None
        self.currently_selected_icon = None
        self.current_frame = None
        self.is_favorites_clicked = False
        
        # Initialize the sub frames stack
        self.dashboard_frames = {}
        
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
        
    def switch_dashboard_composable(self, frame_class, **kwargs):
        """
        Function Name: switch_dashboard_composable
        Description: Destroys the current frame and replaces it with a new one from the given frame class.
        """
        if self.current_frame is not None:
            self.current_frame.destroy_ui_composable()  # Destroy the current composable
            print(f"Destroyed current frame: {type(self.current_frame).__name__}")

        # Create the new frame and pack it into the same parent
        self.current_frame = frame_class(self.controller, self.controller, **kwargs)
        #self.current_frame.pack(fill='both', expand=True)
        print(f"Loaded new frame: {frame_class.__name__}")
        
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
        self.sidebar = tk.Frame(self, bg='#dddddd')
        self.sidebar.pack(side='left', fill='y')
        
        # Separately handle the favorites and settings icon to place it at top and the bottom
        self.create_icon_button('ic_favorite.png', "Favorites", self.load_favorites_composable)
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
            ('ic_web_service.png', "Web Services", self.load_web_services_composable),
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
        self.paned_window = ttk.Panedwindow(self.controller, orient=tk.HORIZONTAL)
        
        # Create the dynamic column as a Frame
        self.dynamic_column = tk.Frame(self.paned_window, bg='#dddddd', width=60, highlightbackground='lightgrey', highlightthickness=0.5)
        self.paned_window.add(self.dynamic_column, weight=1)
        
        # Create a handle for resizing
        self.handle = ttk.Separator(self.paned_window, orient=tk.VERTICAL)
        self.paned_window.add(self.handle, weight=0)  # Add handle with no weight to ensure it doesn't expand

        # Bind the handle to a method that resizes the pane
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
        # Resize the icon
        icon = self.resize_Icon(icon_path)
        
        # Create a canvas for the icon
        button_canvas = tk.Canvas(self.sidebar if sidebar == 'primary' else self.dynamic_column, 
                                width=50, height=50, bg='#dddddd', highlightthickness=0)
        # Pack at the bottom if place_bottom is True
        if place_bottom:
            button_canvas.pack(side='bottom', pady=10)
        else:
            button_canvas.pack(pady=10)  # Regular packing for other icons
        
        # Create the icon image
        button_canvas.pack(pady=10)
        button_canvas.create_image(25, 25, image=icon)
        button_canvas.bind("<Button-1>", lambda event, a=action, btn=button_canvas: self.on_icon_click(event, a, btn))
        CreateToolTip(button_canvas, tooltip_text)
        button_canvas.image = icon # Keep a reference to avoid garbage collection

    def on_icon_click(self, event, action, button_canvas):
        """ 
        Function Name: on_icon_click
        Description: This function toggles the paned window column and executes the action
        """
        # Reset background of previously selected icon if exists
        if self.currently_selected_icon:
            self.currently_selected_icon.configure(bg='#dddddd')  # Reset background to default
        # Highlight the currently selected icon
        button_canvas.configure(bg='lightblue')
        self.currently_selected_icon = button_canvas

        # Check if same action is triggered and pane is visible
        if action == self.last_action and not self.paned_window_hidden:
            self.show_or_hide_pane()
        else:
            if self.paned_window_hidden:
                self.show_or_hide_pane()
            if callable(action):
                action()
            elif isinstance(action, str):
                # Delegate frame management to the controller
                self.show_dashboard_frame(action)

        self.last_action = action       
        
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
            
    def show_dashboard_frame(self, frame_name):
        """
        Function Name: show_dashboard_frame
        Description: Show a specific frame by name, hiding others.
        """
        frame = self.dashboard_frames.get(frame_name)
        if frame:
            for f in self.dashboard_frames.values():
                f.pack_forget()  # Hide all frames
            #frame.pack(fill='both', expand=True)  # Make the frame visible using pack
        else:
            print(f"Frame {frame_name} not found")

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
            # Debugging
            print("load_favorites_composable triggered")   
            self.is_favorites_clicked = True
            self.sub_sidebar_composable()
        
    def load_settings_composable(self):
        """ 
        Function Name: load_settings_composable
        Function Purpose: This function executes when the user clicks on 'settings' button to display the UI composable
        """
        # Debugging
        print("load_settings_composable triggered")   
        # Show warning message about this page is not fully implemented yet and if the user wants to exit, they must enter 'yes'
        if messagebox.askyesno("Warning", "This page is not fully implemented yet. Do you want to exit the program?"):
            self.exit_app_btn()
        
    def load_all_accounts_composable(self):
        """ 
        Function Name: load_all_accounts_composable
        Function Purpose: This function executes when the user clicks on 'All Accounts' button to display the UI composable
        """
        # Debugging
        print("load_all_accounts_composable triggered")
        self.destroy_child_frame()
        # Pass hide and show sidebar methods through kwargs
        self.switch_dashboard_composable(
            View_All_Accounts_UiComposable,
            hide_sidebar=self.hide_sidebar_elements,
            show_sidebar=self.show_sidebar_elements
        )

    def load_social_media_composable(self):
        """ 
        Function Name: load_social_media_composable
        Function Purpose: This function executes when the user clicks on 'Social Media' button to display the UI composable
        """
        # Debugging
        print("load_social_media_composable triggered")
        self.destroy_child_frame()
        # Show the 'social media' composable
        self.switch_dashboard_composable(
            View_SocialMedia_Accounts_UiComposable,
            hide_sidebar=self.hide_sidebar_elements,
            show_sidebar=self.show_sidebar_elements
        )
        
    def load_web_services_composable(self):
        """ 
        Function Name: load_web_services_composable
        Function Purpose: This function executes when the user clicks on 'Web Services' button to display the UI composable
        """
        # Debugging
        print("load_web_services_composable triggered")
        self.destroy_child_frame()
        # Show the 'social media' composable
        self.switch_dashboard_composable(
            View_WebService_Accounts_UiComposable,
            hide_sidebar=self.hide_sidebar_elements,
            show_sidebar=self.show_sidebar_elements
        )
        
    def load_finance_composable(self):
        """ 
        Function Name: load_finance_composable
        Function Purpose: This function executes when the user clicks on 'Finance' button to display the UI composable
        """
        # Debugging
        print("load_finance_composable triggered")
        self.destroy_child_frame()
        # Show the 'social media' composable
        self.switch_dashboard_composable(
            View_Fiance_Accounts_UiComposable,
            hide_sidebar=self.hide_sidebar_elements,
            show_sidebar=self.show_sidebar_elements
        )
        
    def load_personal_composable(self):
        """ 
        Function Name: load_personal_composable
        Function Purpose: This function executes when the user clicks on 'Personal' button to display the UI composable
        """
        # Debugging
        print("load_personal_composable triggered")     
        self.destroy_child_frame()
        # Show the 'social media' composable
        self.switch_dashboard_composable(
            View_Personal_Accounts_UiComposable,
            hide_sidebar=self.hide_sidebar_elements,
            show_sidebar=self.show_sidebar_elements
        )

    def hide_sidebar_elements(self):
        """
        Function Name: hide_ui_elements
        Description: This function hides the sidebar and dynamic column.
        """
        # Check if the sidebar exists and then hide it
        if hasattr(self, 'sidebar') and self.sidebar.winfo_exists():
            self.sidebar.pack_forget()
            self.sidebar.destroy()

        # Check if the paned_window exists and then hide it
        self.show_or_hide_pane()
        
    def show_sidebar_elements(self):
        """
        Function Name: show_ui_elements
        Description: This function reveals the sidebar and dynamic column.
        """
        # Check if the paned_window exists and then hide it
        self.primary_sidebar_composable()
        print(self.paned_window_hidden)
        if self.paned_window_hidden:
            self.load_all_accounts_composable()
            self.show_or_hide_pane()
        
        # # Debugging: Highlight areas to visually confirm layout behavior
        # self.sidebar.config(bg='red')  # Temporarily set to red to see its actual area
        # self.config(bg='blue')  # Temporarily set the parent's background to blue
        