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
from base_methods import Base_Ui_Methods
from account_object_class import Account
from tool_tip import CreateToolTip

#######################################################################################################
# View Account Information Class
#######################################################################################################  

class View_AccountInfo_UiComposable(tk.Frame, Base_Ui_Methods):
    """
    Class Name: View_AccountInfo_UiComposable
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
        # Set the last action to None
        self.currently_selected_icon = None
        self.last_action = None
        
        # Create the main Ui Frame
        self.create_ui_frame()   

    def create_ui_frame(self):
        """
        Function Name: create_ui_frame
        Description: Creates a fixed-size frame for UI elements.
        """ 
        # Call the methods to set labels, entry fields, and buttons within this ui_frame 
        self.create_general_labels()
        self.create_tree_view_frame()
        self.create_buttons()   
        
    def create_general_labels(self):
        """
        Function Name: create_general_labels
        Description: This function creates the labels for the account UI
        """
        # Set the font style for the header
        header_font = Font(family="Helvetica", size=16, weight="bold")

        # Header label
        tk.Label(self.parent, text="Accounts", font=header_font).place(relx=0.15, rely=0.05, anchor="center")

    def create_tree_view_frame(self):
        """
        Function Name: create_tree_view_frame
        Description: This function creates the scrollable tree view frame for the account UI
        """
        # Define the font for the column headers
        col_header_font = Font(family="Helvetica", size=10, weight="bold")

        # Configure the style of the Treeview heading to use the col_header_font
        style = ttk.Style(self.parent)
        style.configure("Treeview.Heading", font=col_header_font)

        # Define styles for alternating rows
        style.configure("evenrow.Treeview", background="lightblue")
        style.configure("oddrow.Treeview", background="white")
        
        # Scrollable Frame for Data
        scroll_frame = tk.Frame(self.parent, bg='white')
        scroll_frame.place(relx=0.54, rely=0.1, anchor="n", relwidth=0.91, relheight=0.9)

        # Treeview widget with headers
        self.tree = ttk.Treeview(scroll_frame, columns=('application_name', 'user_name', 'email', 'password', 'last_update', 'category'), show='headings', selectmode='extended')
        self.tree.pack(side='left', fill='both', expand=True)

        # Define column headings and properties
        self.tree.heading('application_name', text='Application Name')
        self.tree.column('application_name', anchor=tk.CENTER, width=120)
        self.tree.heading('user_name', text='User Name')
        self.tree.column('user_name', anchor=tk.CENTER, width=120)
        self.tree.heading('email', text='Email')
        self.tree.column('email', anchor=tk.CENTER, width=180)
        self.tree.heading('password', text='Password')
        self.tree.column('password', anchor=tk.CENTER, width=120)
        self.tree.heading('last_update', text='Last Update')
        self.tree.column('last_update', anchor=tk.CENTER, width=120)
        self.tree.heading('category', text='Category')
        self.tree.column('category', anchor=tk.CENTER, width=120)

        # Style configuration for selected items (Optional)
        style.map('Treeview', background=[('selected', '#007cb9')])

        # Scrollbar for the treeview
        scrollbar = ttk.Scrollbar(scroll_frame, orient='vertical', command=self.tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Populate the treeview with sample data
        self.get_db_data()  

    def get_db_data(self):
        """
        Function Name: get_db_data
        Description: This function will fetch data from the database and populate the treeview.
        """
        # Get the data from the db
        result = Account.get_all_account_info()
        
        # Clear existing treeview
        for i in self.tree.get_children():
            self.tree.delete(i)

        if result:
            # Define styles for alternating rows
            self.tree.tag_configure('oddrow', background='white')
            self.tree.tag_configure('evenrow', background='lightgrey')

            # Add new data to the treeview
            for index, row in enumerate(result):
                # Choose the tag based on the row index
                tag = 'evenrow' if index % 2 == 0 else 'oddrow'
                self.tree.insert("", "end", values=row, tags=(tag,))
        else:
            pass

    def on_treeview_click(self, event):
        """
        Function Name: on_treeview_click
        Description: This function sets and aligns the check box icons for the account UI
        """
        # Get the clicked item
        rowid = self.tree.identify_row(event.y)
        column = self.tree.identify_column(event.x)

        # Check if the click is on the first column (where the check buttons are)
        if self.tree.heading(column, "text") == '' and rowid:
            # Toggle the checked state
            item = self.tree.item(rowid)
            if self.tree.item(rowid, 'image') == self.checked_image:  # If already checked
                self.tree.item(rowid, image=self.unchecked_image)
            else:  # If not checked
                self.tree.item(rowid, image=self.checked_image)

    def create_buttons(self):
        """
        Function Name: create_buttons
        Description: This function will create all the buttons for the account UI
        """
        # Separately handle the settings icon to place it at top right corner
        self.create_icon_button('ic_add.png', "Add New Account", self.add_new_account_composable, x=0.90, y=0.035)
        self.create_icon_button('ic_edit.png', "Edit Account", self.edit_account_composable, x=0.93, y=0.035)
        self.create_icon_button('ic_delete.png', "Delete Account", self.delete_account_composable, x=0.96, y=0.035)
        
    def resize_Icon(self, icon_path, size=(20, 20)):
        """
        Function Name: resize_Icon
        Description: This function resizes the icon to the specified width and height
        """        
        image = Image.open(icon_path)
        resized_image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(resized_image)
    
    def create_icon_button(self, icon_path, tooltip_text, action, x=0.90, y=0.05):
        """
        Function Name: create_icon_button
        Description: Helper function to create an icon button with a tooltip.
        """
        # Resize the icon
        icon = self.resize_Icon(icon_path)

        # Create the button canvas
        button_canvas = tk.Canvas(self.parent, width=30, height=30, highlightthickness=0, bd=0)
        button_canvas.place(relx=x, rely=y, anchor="ne")
        button_canvas.create_image(15, 15, image=icon)
        button_canvas.bind("<Button-1>", lambda event, a=action, btn=button_canvas: self.on_icon_click(event, a, btn))  # Bind to on_icon_click
        CreateToolTip(button_canvas, tooltip_text)
        button_canvas.image = icon

    def show_frame(self, frame_name):
        """
        Function Name: show_frame
        Description: This function shows the frame inside the main container
        """
        # Check if the frame to be shown is a sub-frame and handle accordingly
        if frame_name in self.sub_frames:
            # Hide all sub-frames first
            for f in self.sub_frames.values():
                f.pack_forget()
            # Show the requested sub-frame
            self.sub_frames[frame_name].pack(fill='both', expand=True)
            # Optionally, call a 'show' method if the sub-frame has one
            if hasattr(self.sub_frames[frame_name], 'show'):
                self.sub_frames[frame_name].show()
        else:
            # Handle main frames: Get the frame from the frame stack
            frame = self.frames.get(frame_name)
            if frame:
                frame.tkraise()  # Ensuring that the frame is brought to the top
                # Call show method explicitly if defined in the frame
                if hasattr(frame, 'show'):
                    frame.show()
            else:
                print(f"No frame with name {frame_name} found.")
                
    def on_icon_click(self, event, action, button_canvas):
        """ 
        Function Name: on_icon_click
        Description: This function toggles the paned window column and executes the action
        """
        # Reset background of previously selected icon if exists
        if self.currently_selected_icon:
            self.currently_selected_icon.configure(bg='SystemButtonFace')  # Reset background to default
        # Highlight the currently selected icon
        button_canvas.configure(bg='lightblue')  # Highlight selection
        self.currently_selected_icon = button_canvas  # Update the reference to the currently selected icon
        # Update the last action
        self.last_action = action  
        
    def on_item_selection(self, event):
        """
        Function Name: on_item_selection
        Description: Called when an item in the Treeview is selected.
        """
        self.selected_items = self.tree.selection()

    def edit_selected_items(self):
        """
        Function Name: edit_selected_items
        Description: Called when the edit button is clicked.
        """
        selected_items = self.tree.selection()
        # Add your logic to edit the selected items
        print("Editing items:", selected_items)

    def delete_selected_items(self):
        """
        Function Name: delete_selected_items
        Description: Called when the delete button is clicked.
        """
        selected_items = self.tree.selection()
        # Add your logic to delete the selected items
        for item in selected_items:
            self.tree.delete(item)
        print("Deleted items:", selected_items)
        
    def add_new_account_composable(self):
        """ 
        Function Name: add_new_account_composable
        Function Purpose: This function executes when the user clicks on 'Add' button to display the add new account
        UI composable
        """
        print("add_new_account_composable triggered")
        # Call the composable

    def edit_account_composable(self):
        """ 
        Function Name: edit_account_composable
        Function Purpose: This function executes when the user clicks on 'Edit' button to display the edit an account
        UI composable
        """
        print("edit_account_composable triggered")
        # Call the composable
        
    def delete_account_composable(self):
        """ 
        Function Name: delete_account_composable
        Function Purpose: This function executes when the user clicks on 'Delete' button to display the delete an account
        UI composable
        """
        print("delete_account_composable triggered")
        # Call the composable