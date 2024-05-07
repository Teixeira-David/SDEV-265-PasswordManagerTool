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
from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
from tkinter.font import Font
from PIL import Image, ImageTk

# Import project modules
from base_methods import Base_Ui_Methods
from account_object_class import Account
from password_object_class import PasswordWithPolicy
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
    def __init__(self, parent, controller, tag, **kwargs):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """   
        # Super class instantiation
        super().__init__(parent)
        self.controller = controller 
        self.parent = parent
        self.tag = tag # Set the tag for the type of info to populate
        self.selected_items = [] # Initialize the selected items list

        # Debugging output to print all passed keyword arguments
        print("Received kwargs:", kwargs)
        
        # Retrieve sidebar control methods from kwargs
        self.hide_sidebar = kwargs.get('hide_sidebar')
        self.show_sidebar = kwargs.get('show_sidebar')
        
        # Set the last action to None
        self.currently_selected_icon = None
        self.last_action = None 
        self.current_frame = None
        self.icon_buttons = [] 
        self.controller.shared_data = {'selected_data': None}
        self.selected_data = []
        
    def create_ui_frame(self):
        """
        Function Name: create_ui_frame
        Description: Creates a fixed-size frame for UI elements.
        """ 
        # Destroy the current frame if it exists
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
        column_headers, columns = self.get_columns_by_tag(self.tag)
        
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
        base_columns = ['application_name', 'user_name', 'email', 'password', 'last_update', 'category', 'notes']
        # Base header columns
        base_header = ['Application Name', 'User Name', 'Email', 'Password', 'Last Update', 'Category', 'Notes']
        
        # Define different column setups for different tags
        if tag == "Account_Info":
            # Pop the 'notes' column
            base_columns.pop(6)
            base_header.pop(6)
            return (base_header, base_columns)
        else:
            # Pop the 'category' column
            base_columns.pop(5)
            base_header.pop(5)
            return (base_header, base_columns)
        
    def get_db_data(self):
        """
        Function Name: get_db_data
        Description: This function will fetch data from the database and populate the treeview.
        """
        # Get the key for decryption
        key = PasswordWithPolicy.get_key()
        
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
                # Change the row tuple to a list
                row = list(row)
                # Choose the tag based on the row index
                tag = 'evenrow' if index % 2 == 0 else 'oddrow'
                # Decrypt the password stored in the database
                row[3] = PasswordWithPolicy.decrypt_password(row[3], key=key)
                self.tree.insert("", "end", values=row, tags=(tag,))
        else:
            pass

    def create_buttons(self):
        """
        Function Name: create_buttons
        Description: This function will create all the buttons for the account UI
        """
        # Set the icon path
        add_img = 'ic_add.png'
        edit_img = 'ic_edit.png'
        delete_img = 'ic_delete.png'
        
        # Add the images to the resource path
        self.resource_path(add_img)
        self.resource_path(edit_img)
        self.resource_path(delete_img)
        
        # Separately handle the settings icon to place it at top right corner
        self.create_icon_button(add_img, "Add New Account", self.add_new_account_composable, x=0.90, y=0.03)
        self.create_icon_button(edit_img, "Edit Account", self.edit_account_composable, x=0.93, y=0.03)
        self.create_icon_button(delete_img, "Delete Account", self.delete_account_composable, x=0.96, y=0.03)
        
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
        # Get the item IDs of the selected items
        self.selected_items = self.tree.selection()
        # Clear previous selections
        self.selected_indices = []
        self.all_selected_data = []
        
        # Store index of each selected item
        for i, item in enumerate(self.selected_items):
            item_data = self.tree.item(item, 'values')
            self.all_selected_data.append(item_data)
            self.selected_indices.append(self.tree.index(item))
            self.selected_indices[i] += 1
            # Debug: Print selected indices to verify
            print("Data for item {}: {}".format(item, item_data))  # Debug to view the data selected
            print("Selected indices:", self.selected_indices)
        
        return self.all_selected_data

    def destroy_all_composable(self):
        """ 
        Function Name: destroy_all_composable
        Function Purpose: This function executes when the user clicks away from the current composable
        """
        from view_account_ui_composable import View_All_Accounts_UiComposable, View_SocialMedia_Accounts_UiComposable, View_WebService_Accounts_UiComposable, View_Fiance_Accounts_UiComposable, View_Personal_Accounts_UiComposable
        # List of all frame types that might be currently displayed
        frame_types = [
            Base_AccountInfo_UiComposable,
            View_All_Accounts_UiComposable,
            View_SocialMedia_Accounts_UiComposable,
            View_WebService_Accounts_UiComposable,
            View_Fiance_Accounts_UiComposable,
            View_Personal_Accounts_UiComposable,
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
        # Hide the sidebar elements
        if self.hide_sidebar:
            self.hide_sidebar()

        print("Received kwargs:", self.hide_sidebar)
        print("Received kwargs:", self.show_sidebar)
        
        # Initialize and show only the Add_Accounts_UiComposable frame
        self.destroy_all_composable()
        self.switch_composable(
            frame_class=Add_Accounts_UiComposable, 
            show_sidebar=self.show_sidebar
            )
        
        # Refresh the treeview or the display to show the updated state
        self.get_db_data()
        
    def edit_account_composable(self):
        """ 
        Function Name: edit_account_composable
        Function Purpose: This function executes when the user clicks on 'Edit' button to display the edit an account
        UI composable
        """
        # Get the data from the selected list
        data = self.get_selected_items_data()
        print(data) # Debugging purposes
        
        # If not data items are selected, warn the user to select an item
        if not data:
            messagebox.showwarning("No Selection", "Please select an item to edit.")
            return
        
        # Get the user selected data before opening the custom password generator
        #self.controller.shared_data = {'selected_data': data}
        
        # Hide the sidebar elements
        if self.hide_sidebar:
            self.hide_sidebar()
        print("Received kwargs:", self.hide_sidebar)
        print("Received kwargs:", self.show_sidebar)
        
        # Call the composable
        self.destroy_all_composable()
        self.switch_composable(
            frame_class=Edit_Accounts_UiComposable,
            data=data, 
            selected_index=self.selected_indices, 
            show_sidebar=self.show_sidebar
            )

        # Refresh the treeview or the display to show the updated state
        self.get_db_data() 
        
    def convert_selected_data(self, data):
        """ 
        Function Name: convert_selected_data
        Function Purpose: This function is converts the data passed to only represent the user name and app name
        """      
        if data is not None and len(data) > 0:
            for d in data:
                self.selected_data.append(d[0] + " - " + d[1])
                
    def delete_account_composable(self):
        """ 
        Function Name: delete_account_composable
        Function Purpose: This function executes when the user clicks on 'Delete' button to display the delete an account
        UI composable
        """
        print("delete_account_composable triggered") # Debugging purposes

        # Retrieve the data from the selected list
        data = self.get_selected_items_data()
        print(data)  # Debugging purposes
        
        # If not data items are selected, warn the user to select an item
        if not data:
            messagebox.showwarning("No Selection", "Please select an item to edit.")
            return
        
        # Convert the data for processing
        self.convert_selected_data(data)
        
        # Create a formatted string of account names for the confirmation message
        account_names = ", \n".join(self.selected_data)
        account_list_text = f"{account_names}"

        # Display an explicit and informative warning message to the user
        confirmation_message = (
            f"WARNING: You are about to permanently delete the following account(s): \n\n{account_list_text}\n\n"
            "This action CANNOT be undone. All associated data will be irretrievably lost. Please confirm that you wish to "
            "proceed with deleting these accounts. It is recommended to backup any important data before proceeding."
        )
        
        if messagebox.askokcancel("Confirm Permanent Delete", confirmation_message):
            # If the user confirms, call the delete method
            Account.delete_account(Account, data)
            # Refresh the treeview or the display to show the updated state
            self.get_db_data()
        
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
