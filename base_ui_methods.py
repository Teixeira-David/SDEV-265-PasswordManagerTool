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
from tool_tip import CreateToolTip
from view_account_ui_composable import View_All_Accounts_UiComposable, View_SocialMedia_Accounts_UiComposable
from view_account_ui_composable import View_WebService_Accounts_UiComposable, View_Fiance_Accounts_UiComposable, View_Personal_Accounts_UiComposable
from crud_ui_composable import Add_Accounts_UiComposable, Edit_Accounts_UiComposable
from user_object_class import User
from password_object_class import PasswordWithPolicy
from user_login_ui import UserLogin_UiComposable, AddNewUser_UiComposable
from generate_password_ui import CustomPasswordGen_UiComposable
from dashboard_ui import MainDashboard_UiComposable


#######################################################################################################
# Custom Password Generator Class
#######################################################################################################
 
class Init_UiFrames(tk.Frame):
    """
    Class Name: Init_UiFrames
    Class Description: This class sets all the initial UI frames for the program.
    """
    def __init__(self, *args, **kwargs):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """   
        # Create the root tkinter variable
        super().__init__(*args, **kwargs)
        self.frames = {}
        
    def init_frames(self, main_container):
        """
        Function Name: init_frames
        Description: This function creates the frame container stack for the main UI
        """
        # Create the frames for the main UI
        for FrameClass in [
            UserLogin_UiComposable, 
            AddNewUser_UiComposable, 
            CustomPasswordGen_UiComposable,
            MainDashboard_UiComposable,
            ]:
            # Create the frame and add it to the stack
            frame = FrameClass(parent=main_container, controller=self)
            # Add the frame to the stack
            self.frames[FrameClass.__name__] = frame
            # Ensure all frames are in the same grid cell and can expand/fill.
            frame.grid(row=0, column=0, sticky="nsew")
            frame.grid_remove()
        main_container.grid_rowconfigure(0, weight=1)
        main_container.grid_columnconfigure(0, weight=1)
        
        # Show initial frame
        self.show_frame("MainDashboard_UiComposable")
        #self.show_frame("UserLogin_UiComposable")
        
#######################################################################################################
# Base Ui Composable Class
#######################################################################################################

class Base_UiComposable(tk.Tk):
    """
    Class Name: Base_UiComposable
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
        self.parent_container()    
        
        # Create the class attributes
        self.init_attributes()
        
        # Create the main frame directory
        init_fr = Init_UiFrames()
        init_fr.init_frames(self.main_container)
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()    
        
        # Exit the program if the user closes the window
        sys.exit()      

    def init_attributes(self):
        """
        Function Name: init_attributes
        Description: This function creates the class attributes for the main UI
        """
        # Initialize frames
        self.frames = {}
        # Initialize the paned_window_hidden to True so it starts hidden
        self.paned_window_hidden = True
        self.last_action = None
        self.currently_selected_icon = None
        self.current_frame = None
        self.is_favorites_clicked = False
        
        # Initialize the sub frames stack
        self.dashboard_frames = {}
        
        # Initialize the shared data
        self.shared_data = {}
        
    def parent_container(self):
        """
        Function Name: parent_container
        Description: This function creates the main container for the main UI
        """
        # Main container for the main UI
        self.main_container = Frame(self)
        self.main_container.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
    def sub_parent_ui_frame(self, parent_container, frame_width, frame_height, bg_color='white'):
        """
        Function Name: sub_parent_ui_frame
        Description: Creates a fixed-size frame for UI elements.
        """
        # Adjust the size as needed
        self.sub_parent_frame = Frame(parent_container, width=frame_width, height=frame_height, bg=bg_color)  
        self.sub_parent_frame.pack_propagate(False)  # Prevents the frame from resizing to fit its contents
        self.sub_parent_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame within the main_container
        
    def file_menu_composable(self):
        """
        Function Name: file_menu_composable
        Description: This function creates the file menu for the main Ui Dashboard fragment
        """
        # Create a menu bar
        menu_bar = tk.Menu(self)  # 'self' should be the instance of Base_UiComposable which is a tk.Tk

        # Add 'File' menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_menu_btn)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Add 'Edit' menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # Add 'View' menu
        view_menu = tk.Menu(menu_bar, tearoff=0)
        view_menu.add_command(label="Zoom In", command=self.edit_menu_btn)
        menu_bar.add_cascade(label="View", menu=view_menu)

        # Add 'Help' menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # Set the menu bar on the window
        self.config(menu=menu_bar)
        
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

    def primary_sidebar_composable(self, parent_container):
        """
        Function Name: primary_sidebar_composable
        Description: This function creates the sidebar for the main UI
        """
        # Create a sidebar frame
        self.sidebar = tk.Frame(parent_container, bg='#dddddd')
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

    def create_dynamic_column(self, parent_container):
        """
        Function Name: create_dynamic_column
        Description: This function creates the dynamic column for the main UI
        """
        # Create the paned_window widget
        self.paned_window = ttk.Panedwindow(parent_container, orient=tk.HORIZONTAL)
        
        # Create the dynamic column as a Frame
        self.dynamic_column = tk.Frame(self.paned_window, bg='#dddddd', width=60, highlightbackground='lightgrey', highlightthickness=0.5)
        self.paned_window.add(self.dynamic_column, weight=1)
        
        # Create a handle for resizing
        self.handle = ttk.Separator(self.paned_window, orient=tk.VERTICAL)
        self.paned_window.add(self.handle, weight=0)  # Add handle with no weight to ensure it doesn't expand

        # Bind the handle to a method that resizes the pane
        self.handle.bind('<B1-Motion>', self.resize_pane)
        
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
                self.show_frame(action)

        self.last_action = action  
        
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
            
    def create_med_center_image_canvas(self, image_path, canvas_width, canvas_height, image_width, image_height, padding=20, tag=None):
        """
        Function Name: create_image_canvas
        Description: Sets up the frame containing the application's logo in the center of the parent frame.
        """
        # Create a canvas for the shield logo at the top of the sub_parent_frame
        self.canvas = Canvas(self.sub_parent_frame, width=canvas_width, height=canvas_height, bg='white', highlightthickness=0)
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
        # Create a canvas for the image at the top of the sub_parent_frame
        self.canvas = Canvas(self.sub_parent_frame, width=canvas_width, height=canvas_height, bg='white', highlightthickness=0)
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
        self.bg_canvas = tk.Canvas(self.sub_parent_frame, width=width_size, height=height_size)
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

    def resize_Icon(self, icon_path, size=(32, 32)):
        """
        Function Name: resize_Icon
        Description: This function resizes the icon to the specified width and height
        """        
        image = Image.open(icon_path)
        resized_image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(resized_image)
    
    def position_sub_parent_frame(self):
        """
        Function Name: position_sub_parent_frame
        Description: Creates a fixed-size frame for UI elements.
        """
        # Center sub_parent_frame every time the window resizes
        self.sub_parent_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Optionally, rebind the resize event to a new method that re-centers sub_parent_frame
        self.bind("<Configure>", self.on_window_resize)

    def on_window_resize(self, event=None):
        """
        Function Name: on_window_resize
        Description: This function creates the background image window for the main UI
        """
        # Check if the canvas still exists before trying to modify it
        self.position_sub_parent_frame()

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

    def switch_composable(self, frame_class, data=None, *args, **kwargs):
        """
        Destroys the current frame and replaces it with a new one from the given frame class.
        """
        if self.current_frame is not None:
            # Properly destroy the current frame
            self.current_frame.destroy_base_composable()
            print(f"Destroyed current frame: {type(self.current_frame).__name__}")
            self.current_frame = None  # Ensure reference is cleared

        # Create the new frame and pack it into the same parent
        self.current_frame = frame_class(self.parent, self.controller, data=data, *args, **kwargs)
        self.current_frame.pack(fill='both', expand=True)
        print(f"Loaded new frame: {frame_class.__name__}")

    def destroy_base_composable(self):
        """ 
        Function Name: destroy_base_composable
        Function Purpose: This function executes when the user clicks away from the current composable
        """
        print("Destroying composable:", self.__class__.__name__)

        # Destroy the label
        if hasattr(self, 'header_label'):
            self.header_label.destroy()
            print("Header label destroyed.")
            
        # Iterate over all child widgets and destroy them
        for child in self.winfo_children():
            child.destroy()
        
        # Destroy the treeview
        self.tree.destroy()
        
        # Finally, destroy this frame itself
        self.main_container.destroy()
        print("Composable destroyed successfully")
        
    def show_frame(self, frame_name, tag=None):
        """
        Function Name: show_frame
        Description: This function shows the frame inside the main container
        """
        print(f"Attempting to show frame: {frame_name} with tag: {tag}")
        # Hide all frames first
        for fname, frame in self.frames.items():
            if getattr(frame, 'layout_manager', 'grid') == 'pack':
                frame.pack_forget()
            else:
                frame.grid_remove()

        # Show the requested frame
        frame = self.frames.get(frame_name)
        if frame:
            print(f"Showing frame: {frame_name}")
            # Use tag to determine layout manager
            if tag == 'pack':
                frame.pack(fill='both', expand=True)
            elif tag == 'grid':
                frame.grid(row=0, column=0, sticky='nsew')
            else:
                # Default to grid if no tag is specified
                frame.grid(row=0, column=0, sticky='nsew')
            
            frame.tkraise()  # Bring the frame to the top
            if hasattr(frame, 'show'):
                frame.show()  # If the frame has a show method, call it
        else:
            print(f"No frame with name {frame_name} found.")

    def hide_frame(self, frame_name):
        """
        Function Name: hide_frame
        Description: This function hides the specified frame.
        """
        frame = self.frames.get(frame_name)
        if frame:
            frame.grid_remove()
        else:
            print(f"No frame with name {frame_name} found.")
            
    def destroy_child_frame(self):
        """ 
        Function Name: add_new_user
        Function Purpose: This function executes when the frame inside the main container will be destroyed.
        """
        # Destroy the UI Frame and its children widgets
        if hasattr(self, 'frames') and self.frames is not None:
            self.frames.destroy()
            self.frames = None # Set to None to prevent memory leaks
            
    def exit_app_btn(self):
        """ 
        Function Name: exit_app_btn
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """       
        # Display the user ask question to see if the user would like to exit the program
        if messagebox.askyesno(message="CAUTION! \n\n Would you like to exit the program?", icon='question'):          
            sys.exit()
            
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
        
    def load_all_accounts_composable(self):
        """ 
        Function Name: load_all_accounts_composable
        Function Purpose: This function executes when the user clicks on 'All Accounts' button to display the UI composable
        """
        # Debugging
        print("load_all_accounts_composable triggered")
        # Show the 'social media' composable
        self.switch_composable(View_All_Accounts_UiComposable)

    def load_social_media_composable(self):
        """ 
        Function Name: load_social_media_composable
        Function Purpose: This function executes when the user clicks on 'Social Media' button to display the UI composable
        """
        # Debugging
        print("load_social_media_composable triggered")
        # Show the 'social media' composable
        self.switch_composable(View_SocialMedia_Accounts_UiComposable)
        
    def load_web_services_composable(self):
        """ 
        Function Name: load_web_services_composable
        Function Purpose: This function executes when the user clicks on 'Web Services' button to display the UI composable
        """
        # Debugging
        print("load_web_services_composable triggered")
        # Show the 'social media' composable
        self.switch_composable(View_WebService_Accounts_UiComposable)
        
    def load_finance_composable(self):
        """ 
        Function Name: load_finance_composable
        Function Purpose: This function executes when the user clicks on 'Finance' button to display the UI composable
        """
        # Debugging
        print("load_finance_composable triggered")
        # Show the 'social media' composable
        self.switch_composable(View_Fiance_Accounts_UiComposable)
        
    def load_personal_composable(self):
        """ 
        Function Name: load_personal_composable
        Function Purpose: This function executes when the user clicks on 'Personal' button to display the UI composable
        """
        # Debugging
        print("load_personal_composable triggered")               
        # Show the 'social media' composable
        self.switch_composable(View_Personal_Accounts_UiComposable)

#######################################################################################################
# User Login Class
#######################################################################################################

class UserLogin_UiComposable(tk.Frame, Base_UiComposable):
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
        self.parent = parent
        self.controller = controller # Set the controller object for direction flow
        
        # Create the main Ui Frame
        self.create_ui_frame()    

    def create_ui_frame(self):
        """
        Function Name: create_ui_frame
        Description: Creates a fixed-size frame for UI elements.
        """
        # Adjust the size as needed
        self.sub_parent_ui_frame(self.parent, 600, 400)
        
        # Call this method to set up the header frame
        self.create_logo_image()
        
        # Call the methods to set labels, entry fields, and buttons within this sub_parent_frame 
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
        Label(self.sub_parent_frame, text="Username:", bg='white').place(relx=0.4, y=240, anchor="e")
        Label(self.sub_parent_frame, text="Password:", bg='white').place(relx=0.4, y=280, anchor="e")

    def create_entry_fields(self):
        """
        Function Name: create_entry_fields
        Description: This function creates the entry fields for the main UI
        """
        # Create and place entry fields to match the image, centered
        self.username_entry = Entry(self.sub_parent_frame, width=30)
        self.password_entry = Entry(self.sub_parent_frame, width=30, show='*')
        
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
        Button(self.sub_parent_frame, text="Exit", width=10, command=self.exit_app_btn).place(relx=0.3, y=340, anchor="center")
        Button(self.sub_parent_frame, text="New", width=10, command=self.add_new_user_btn).place(relx=0.5, y=340, anchor="center")
        Button(self.sub_parent_frame, text="Submit", width=10, command=self.submit_btn).place(relx=0.7, y=340, anchor="center")
                                                                                                            
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
                self.controller.show_frame("MainDashboard_UiComposable")
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
        self.controller.show_frame("AddNewUser_UiComposable")
            
            
#######################################################################################################
# Add New User Class
#######################################################################################################

class AddNewUser_UiComposable(tk.Frame, PasswordWithPolicy, Base_UiComposable):
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
        self.parent = parent
        self.controller = controller # Set the controller object for direction flow
        
        # Create the main Ui Frame
        self.create_sub_parent_frame()    

    def create_sub_parent_frame(self):
        """
        Function Name: create_sub_parent_frame
        Description: Creates a fixed-size frame for UI elements.
        """
        # Adjust the size as needed
        self.sub_parent_ui_frame(self.parent, 600, 400)
        
        # Call this method to set up the header frame
        self.create_logo_image()
        
        # Call the methods to set labels, entry fields, and buttons within this sub_parent_frame 
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
        Description: This function creates the labels for the main UI
        """
        # Stylize labels to match the image
        Label(self.sub_parent_frame, text="New User Credentials:", bg='white').place(relx=0.32, y=110, anchor="e")
        Label(self.sub_parent_frame, text="Username:", bg='white').place(relx=0.37, y=140, anchor="e")
        Label(self.sub_parent_frame, text="Password:", bg='white').place(relx=0.37, y=180, anchor="e")
        Label(self.sub_parent_frame, text="Password:", bg='white').place(relx=0.37, y=220, anchor="e")
        Label(self.sub_parent_frame, text="Email:", bg='white').place(relx=0.37, y=260, anchor="e")

    def create_entry_fields(self):
        """
        Function Name: create_entry_fields
        Description: This function creates the entry fields for the main UI
        """
        # Create and place entry fields to match the image, centered
        self.username_entry = Entry(self.sub_parent_frame, width=30)
        self.first_password_entry = Entry(self.sub_parent_frame, width=30, show='*')
        self.second_password_entry = Entry(self.sub_parent_frame, width=30, show='*')
        self.email_entry = Entry(self.sub_parent_frame, width=30)
        
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
        
    def create_buttons(self):
        """
        Function Name: create_buttons
        Description: This function creates the buttons for the main UI
        """
        # Button(self.sub_parent_frame, text="Show", command=self.toggle_password(pswrd_widgets)).place(relx=0.20, y=180, anchor="center")
        Button(self.sub_parent_frame, text="Show", command=self.show_password_btn).place(relx=0.8, y=180, anchor="center")
        
        # Stylize buttons to match the image
        # Button(self.sub_parent_frame, text="Generate", width=10, command=self.generate_btn).place(relx=0.9, y=180, anchor="e")
        Button(self.sub_parent_frame, text="Generate", width=10, command=self.generate_btn).place(relx=0.25, y=180, anchor="e")
        Button(self.sub_parent_frame, text="Back", width=10, command=self.back_btn).place(relx=0.3, y=340, anchor="center")
        Button(self.sub_parent_frame, text="Reset", width=10, command=self.clear_entry).place(relx=0.5, y=340, anchor="center")
        Button(self.sub_parent_frame, text="Submit", width=10, command=self.submit_btn).place(relx=0.7, y=340, anchor="center")
        
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
        self.controller.show_frame("CustomPasswordGen_UiComposable")
        
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
        self.controller.show_frame("UserLogin_UiComposable")       
    

#######################################################################################################
# Custom Password Generator Class
#######################################################################################################

class CustomPasswordGen_UiComposable(tk.Frame, Base_UiComposable):
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
        self.parent = parent
        self.controller = controller # Set the controller object for direction flow
        self.controller.shared_data = {'generated_password': None}  # Initializing shared data

        # Create the main Ui Frame
        self.create_ui_frame()    

    def create_ui_frame(self):
        """
        Function Name: create_ui_frame
        Description: Creates a fixed-size frame for UI elements.
        """
        # Adjust the size as needed
        self.sub_parent_ui_frame(self.parent, 600, 400)
        
        # Call this method to set up the header frame
        self.create_logo_image()
        
        # Call the methods to set labels, entry fields, and buttons within this sub_parent_frame 
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
        Label(self.sub_parent_frame, text="Generate Custom Password", bg='white').place(relx=0.34, y=110, anchor="e")
        Label(self.sub_parent_frame, text="Character Length:", bg='white').place(relx=0.33, y=160, anchor="e")
        Label(self.sub_parent_frame, text="Character Set:", bg='white').place(relx=0.33, y=220, anchor="e")
        Label(self.sub_parent_frame, text="Expiry Period:", bg='white').place(relx=0.33, y=280, anchor="e")

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
                self.sub_parent_frame, 
                text=str(option),
                bg=bg_color
                ).place(relx=base_relx + (i*char_len_spacing+0.003), y=y_pos_char_len - 20)
            tk.Radiobutton(
                self.sub_parent_frame,
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
                self.sub_parent_frame, 
                text=option,
                bg=bg_color
                ).place(relx=base_relx + i*char_set_spacing, y=y_pos_char_set - 20)
            tk.Checkbutton(
                self.sub_parent_frame,
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
                self.sub_parent_frame, 
                text=f"{option} Days",
                bg=bg_color
                ).place(relx=base_relx + i*expiry_spacing, y=y_pos_expiry_period - 20)
            tk.Radiobutton(
                self.sub_parent_frame,
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
        Button(self.sub_parent_frame, text="Back", width=10, command=self.back_btn).place(relx=0.3, y=340, anchor="center")
        Button(self.sub_parent_frame, text="Reset", width=10, command=self.clear_entry).place(relx=0.5, y=340, anchor="center")
        Button(self.sub_parent_frame, text="Generate", width=10, command=self.generate_btn).place(relx=0.7, y=340, anchor="center")
                                                                                                            
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
            # Attempt to create a newly custom password with the provided credentials
            generated_password = self.generate_new_custom_password()
            
            # Ask the user if they want to use the generated password
            if messagebox.askyesno("Password Generation", f"The newly generated password is: \n\n{generated_password}\n\nDo you want to use this password?"):
                # Save the password in shared_data
                self.controller.shared_data['generated_password'] = generated_password
                # Optionally switch back to the Add New User frame
                self.controller.show_frame("AddNewUser_UiComposable")
            else:
                print("User declined the new password")
                self.clear_entry()
            
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
        return pwp.password

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


#######################################################################################################
# Main Dashboard Ui Composable Class
#######################################################################################################

class MainDashboard_UiComposable(tk.Frame, Base_UiComposable):
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
        self.create_ui_frame()    

    def create_ui_frame(self):
        """
        Function Name: create_ui_frame
        Description: Creates a fixed-size frame for UI elements.
        """ 
        # Get the screen width and height 
        self.width_size = self.winfo_screenwidth() 
        self.height_size = self.winfo_screenheight()
        
        # Adjust the size as needed
        self.sub_parent_ui_frame(self.parent, self.width_size, self.height_size)

        # Call this method to set up the header frame
        self.set_dashboard_bg_img(self.width_size, self.height_size)
        
        # Create the file menu
        self.file_menu_composable()
        
        # Create the main container for dynamic columns
        self.primary_sidebar_composable(self.parent)
        
        # Create the dynamic column 
        self.create_dynamic_column(self.parent)
        
        
