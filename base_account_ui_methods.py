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
from crud_ui_composable import Edit_Accounts_UiComposable, Add_Accounts_UiComposable

#######################################################################################################
# Base Account Information Class
#######################################################################################################  

class Base_AccountInfo_UiComposable(tk.Frame, Base_Ui_Methods):
    """
    Class Name: Base_AccountInfo_UiComposable
    Class Description: This class is the primary Ui class for all of the user's account information Ui Composable.
    """
    def __init__(self, parent, controller, tag, *args, **kwargs):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """   
        # Super class instantiation
        super().__init__(parent, *args, **kwargs)
        self.controller = controller 
        self.parent = parent
        
        self.tag = tag # Set the tag for the type of info to populate
        self.selected_items = [] # Initialize the selected items list

        # Set the last action to None
        self.currently_selected_icon = None
        self.last_action = None 
        self.current_frame = None
        self.icon_buttons = [] 
        
    def create_ui_frame(self):
        """
        Function Name: create_ui_frame
        Description: Creates a fixed-size frame for UI elements.
        """ 
        self.destroy_base_composable()
        # Call the methods to set labels, entry fields, and buttons within this ui_frame 
        self.create_general_labels()
        self.create_tree_view_frame()
        self.create_buttons()   
        
    def create_general_labels(self):
        """
        Function Name: create_general_labels
        Description: This function creates the labels for the account UI
        """
        # Declare Primary Header Label
        head_label = "Accounts"
        
        # Set the font style for the header
        header_font = Font(family="Helvetica", size=16, weight="bold")
        
        # Set the header text based off the tag name
        formatted_tag = self.tag.replace('_', ' ')
        if formatted_tag != "Account Info":
            header_text = formatted_tag + " " + head_label
        else:
            header_text = formatted_tag
            
        # Header label
        self.header_label = tk.Label(self.parent, text=header_text, font=header_font)
        self.header_label.place(relx=0.2, rely=0.05, anchor="center")

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
        
        # Dynamic column definitions based on the tag
        column_headers, columns = self.get_columns_by_tag(self.tag)  # Assuming this method returns two lists
        
        # Scrollable Frame for Data
        self.scroll_frame = tk.Frame(self.parent, bg='white')
        self.scroll_frame.place(relx=0.54, rely=0.1, anchor="n", relwidth=0.91, relheight=0.9)

        # Treeview widget with headers
        self.tree = ttk.Treeview(self.scroll_frame, columns=columns, show='headings', selectmode='extended')
        self.tree.pack(side='left', fill='both', expand=True)
        self.tree.bind("<ButtonRelease-1>", self.on_item_selection)  # Bind to on_item_selection

        # Set column properties dynamically
        for header, col in zip(column_headers, columns):
            self.tree.heading(col, text=header)  # Use header text from column_headers list
            self.tree.column(col, anchor=tk.CENTER, width=120)

        # Style configuration for selected items (Optional)
        style.map('Treeview', background=[('selected', '#007cb9')])

        # Scrollbar for the treeview
        self.scrollbar = ttk.Scrollbar(self.scroll_frame, orient='vertical', command=self.tree.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Populate the treeview with sample data
        self.get_db_data() 

    def get_columns_by_tag(self, tag):
        """
        Function Name: get_columns_by_tag
        Description: This function returns the column names based on the tag.
        """
        # Base column setup
        base_columns = ['application_name', 'user_name', 'email', 'password', 'category', 'notes']
        # Base header columns
        base_header = ['Application Name', 'User Name', 'Email', 'Password', 'Category', 'Notes']
        
        # Define different column setups for different tags
        if tag == "Account_Info":
            # Pop the 'notes' column
            base_columns.pop(5)
            base_header.pop(5)
            return (base_header, base_columns)
        else:
            # Pop the 'category' column
            base_columns.pop(4)
            base_header.pop(4)
            return (base_header, base_columns)
        
    def get_db_data(self):
        """
        Function Name: get_db_data
        Description: This function will fetch data from the database and populate the treeview.
        """
        # Get the data from the db
        if self.tag == "Account_Info":
            result = Account.get_all_account_info()
        elif self.tag == "Social_Media":
            result = Account.get_all_social_media_info()
        elif self.tag == "Web_Service":
            result = Account.get_all_web_service_info()
        elif self.tag == "Finance":
            result = Account.get_all_finance_info()
        else:
            result = Account.get_all_personal_info()
        
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

    def create_buttons(self):
        """
        Function Name: create_buttons
        Description: This function will create all the buttons for the account UI
        """
        # Separately handle the settings icon to place it at top right corner
        self.create_icon_button('ic_add.png', "Add New Account", self.add_new_account_composable, x=0.90, y=0.03)
        self.create_icon_button('ic_edit.png', "Edit Account", self.edit_account_composable, x=0.93, y=0.03)
        self.create_icon_button('ic_delete.png', "Delete Account", self.delete_account_composable, x=0.96, y=0.03)
        
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
        
        # Keep reference to image
        button_canvas.image = icon
        button_canvas.bind("<Button-1>", lambda event, a=action, btn=button_canvas: self.on_icon_click(event, a, btn))
        CreateToolTip(button_canvas, tooltip_text)
        
        # Track the button canvas
        self.icon_buttons.append(button_canvas)

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

        # Execute the action
        action()  # Directly call the action here
        
    def on_item_selection(self, event):
        """
        Function Name: on_item_selection
        Description: Called when an item in the Treeview is selected.
        """
        self.selected_items = self.tree.selection()
        #print("Selected items:", self.selected_items)

    def get_selected_items_data(self):
        """
        Function Name: get_selected_items_data
        Description: Retrieves data for all items selected in the Treeview.
        """
        # Get all selected item IDs
        selected_items = self.selected_items  
        # List to store data of all selected items
        all_selected_data = []  

        # Loop through each selected item and fetch its data
        for item_id in selected_items:
            item_data = self.tree.item(item_id, 'values')  
            all_selected_data.append(item_data)
            print("Data for item {}: {}".format(item_id, item_data))  # Debug to view the data selected

        return all_selected_data

    def edit_selected_items(self):
        """
        Function Name: edit_selected_items
        Description: Called when the edit button is clicked.
        """
        selected_items = self.selected_items
        # Add your logic to edit the selected items
        print("Editing items:", selected_items)

    def delete_selected_items(self):
        """
        Function Name: delete_selected_items
        Description: Called when the delete button is clicked.
        """
        selected_items = self.selected_items
        # Add your logic to delete the selected items
        for item in selected_items:
            self.tree.delete(item)
        print("Deleted items:", selected_items)
        
    def destroy_all_composable(self):
        """ 
        Function Name: destroy_all_composable
        Function Purpose: This function executes when the user clicks away from the current composable
        """
        # List of all frame types that might be currently displayed
        frame_types = [
            Base_AccountInfo_UiComposable,
        ]

        # Destroy the current frames
        for frame_type in frame_types:
            # Append the frame type to the list of frame instances
            self.destroy_base_composable()
            print(f"Destroyed composable for {frame_type.__name__}")
        
    def add_new_account_composable(self):
        """ 
        Function Name: add_new_account_composable
        Function Purpose: This function executes when the user clicks on 'Add' button to display the add new account
        UI composable
        """
        # Initialize and show only the Add_Accounts_UiComposable frame
        self.destroy_all_composable()
        self.switch_composable(Add_Accounts_UiComposable, frame_type='crud')
        
    def edit_account_composable(self):
        """ 
        Function Name: edit_account_composable
        Function Purpose: This function executes when the user clicks on 'Edit' button to display the edit an account
        UI composable
        """
        # Get the data from the selected list
        data = self.get_selected_items_data()
        print(data) # Debugging purposes
        
        # Call the composable
        self.destroy_all_composable()
        self.switch_composable(Edit_Accounts_UiComposable, frame_type='crud', data=data)
        
    def delete_account_composable(self):
        """ 
        Function Name: delete_account_composable
        Function Purpose: This function executes when the user clicks on 'Delete' button to display the delete an account
        UI composable
        """
        print("delete_account_composable triggered") # Debugging purposes

        # Get the data from the selected list
        data = self.get_selected_items_data()
        print(data) # Debugging purposes
        
        # Call the composable
            
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

        if hasattr(self, 'tree') and self.tree.winfo_exists():
            self.tree.unbind("<ButtonRelease-1>")  # Unbind any events tied to the treeview
            self.tree.destroy()
            print("Treeview destroyed.")
        
        if hasattr(self, 'scrollbar') and self.scrollbar.winfo_exists():
            self.scrollbar.destroy()
            print("Scrollbar destroyed.")
        
        # Destroy the scroll frame
        if hasattr(self, 'scroll_frame') and self.scroll_frame.winfo_exists():
            self.scroll_frame.destroy()
            print("Scroll frame destroyed.")

        # Destroy the icon buttons
        if hasattr(self, 'icon_buttons'):
            for button_canvas in self.icon_buttons:
                if button_canvas.winfo_exists():
                    button_canvas.unbind("<Button-1>")  # Unbind the event before destroying
                    button_canvas.destroy()  # Destroy the canvas
                    print("Button canvas destroyed.")
            self.icon_buttons.clear()  # Clear the list after destroying
