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
from base_methods import Base_Ui_Methods
from account_object_class import Account
from generate_password_ui import CustomPasswordGen_UiComposable
from user_object_class import User

#######################################################################################################
# Add or Edit Account Info Class
#######################################################################################################

class Add_Edit_Account_UiComposable(tk.Frame, Base_Ui_Methods):
    """
    Class Name: Add_Edit_Account_UiComposable
    Class Description: This class is the to add a new user to the application.
    """
    stored_selected_data = []
    selected_index = 0
    
    def __init__(self, parent, controller, tag, data=None, frame=None, *args, **kwargs):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """            
        # Create the root tkinter variable
        super().__init__(parent, *args, **kwargs)
        self.controller = controller 
        self.parent = parent
        self.tag = tag
        self.data = data if data is not None else []
        self.frame = frame 
        self.selected_data = []

    def create_ui_frame(self):
        """
        Function Name: create_ui_frame
        Description: Creates a fixed-size frame for UI elements.
        """
        # Set the dimension params
        #print(self.tag)
        if self.tag == "Add":
            self.parent_ui_frame(600, 500, self.tag)
        else:
            self.parent_ui_frame(600, 550, self.tag)
        
        # Call the method to set up the UI elements
        #self.init_crud_frames()
        
        # Call this method to set up the header frame
        self.create_logo_image()
        
        # Call the methods to set labels, entry fields, and buttons within this ui_frame 
        self.create_labels()
        self.convert_data()
        self.create_entry_fields()
        self.create_buttons()
        self.config_entry_fields()
        
        # Get the generated password
        self.load_generated_password()

    def init_crud_frames(self, frame_to_init='CustomPasswordGen_UiComposable', data=None):
        """
        Function Name: init_crud_frames
        Description: This function creates the frame container stack for the crude UI icons
        'Add', 'Edit', and 'Delete'.
        """
        # Initialize frames dictionary
        if not hasattr(self, 'crud_frame'):
            self.crud_frame = {}
    
        # Create the frames for the CRUD UI
        crud_class_frames = {
            'CustomPasswordGen_UiComposable': CustomPasswordGen_UiComposable
        }

        # Create only the requested frame for the main UI
        if frame_to_init and frame_to_init in crud_class_frames:
            if frame_to_init not in self.crud_frame:  # Check if frame already exists
                CrudClass = crud_class_frames[frame_to_init]
                # Instantiate the frame with the provided data or default to None if data isn't provided
                crud_frame = CrudClass(parent=self.parent, controller=self.controller, data=data or None)
                self.crud_frame[frame_to_init] = crud_frame
                self.set_crud_frame(frame_to_init, crud_frame)
            else:
                print(f"{frame_to_init} is already initialized.")
        else:
            print(f"{frame_to_init} is not a valid frame.")
            
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
            padding=(95,10)
            ) # Call the method to create the image frame
        
    def create_labels(self):
        """
        Function Name: create_labels
        Description: This function creates the labels for the main UI
        """
        # Determine label text based on the action type
        action_text = "Add New Account" if self.tag == "Add" else "Edit Account"
        x_value = 0.32 if self.tag == "Add" else 0.30
        Label(self.ui_frame, text=action_text, bg='white').place(relx=x_value, y=110, anchor="e")

        labels = [
            "Items Selected:", "Category:", "Platform/App Name:", "User Name:", "Password:",
            "Confirm Password:", "Email:", "Hint/Note:"
        ]
        # Remove the first label if the tag is "Add"
        if self.tag == "Add":
            labels.pop(0)
            
        # Determine the y-axis starting point and spacing between widgets
        y_start = 140
        y_increment = 40
        for i, text in enumerate(labels):
            Label(self.ui_frame, text=text, bg='white').place(relx=0.37, y=y_start + i * y_increment, anchor="e")        

    def create_entry_fields(self):
        """
        Function Name: create_entry_fields
        Description: This function creates the entry fields for the main UI
        """
        # Drop values
        category_values = ["Social Media", "Web Services", "Finance", "Personal"]
        entry_labels = ['AppName', 'Username', 'First Password', 'Second Password', 'Email', 'Hint']
        entry_widths = [30, 30, 30, 30, 30, (45, 3)]  # Ensure there's an entry width for each label

        # Entry widgets configuration
        entries = []
        for i, label in enumerate(entry_labels):
            if "Password" in label:
                entry = Entry(self.ui_frame, width=entry_widths[i], show='*')
                if label == "First Password":
                    self.first_password_entry = entry  # Assign to class attribute
                elif label == "Second Password":
                    self.second_password_entry = entry  # Assign to class attribute
            elif label == "Hint":
                # Treat the 'Hint' as a Text widget, which uses a tuple for width and height
                entry = Text(self.ui_frame, width=entry_widths[i][0], height=entry_widths[i][1])
                self.hint_entry = entry 
            else:
                entry = Entry(self.ui_frame, width=entry_widths[i])
                if label == "AppName":
                    self.appname_entry = entry
                elif label == "Username":
                    self.username_entry = entry
                elif label == "Email":
                    self.email_entry = entry
            entries.append(entry)

        # Determine the y-axis starting point and spacing between widgets
        if self.tag == "Add":
            y_start = 180
            # Special placement for the Hint entry
            entries[-1].place(relx=0.49, y=420, anchor="center")  # 'Hint' has its special placement
        else:
            y_start = 220
            # Special placement for the Hint entry
            entries[-1].place(relx=0.49, y=460, anchor="center")  # 'Hint' has its special placement
        y_increment = 40
        y_positions = [y_start + i * y_increment for i in range(len(entries)-1)]  # -1 because Hint will be placed separately

        # Place each widget
        for entry, y in zip(entries[:-1], y_positions):  # Skip the last entry (Hint)
            entry.place(relx=0.57, y=y, anchor="center")

        # Manage Combobox for categories based on the tag
        if self.tag == "Add":
            self.category_drop = ttk.Combobox(self.ui_frame, values=category_values, width=27, state='readonly')
            self.category_drop.place(relx=0.57, y=y_start - y_increment, anchor="center")
        else:
            self.items_selected_drop = ttk.Combobox(self.ui_frame, values=self.selected_data, width=27, state='readonly')
            self.category_drop = ttk.Combobox(self.ui_frame, values=category_values, width=27, state='readonly')
            self.items_selected_drop.place(relx=0.57, y=y_start - 2 * y_increment, anchor="center")
            self.category_drop.place(relx=0.57, y=y_start - y_increment, anchor="center")
            # Bind the selection of an item to populate the fields
            self.items_selected_drop.bind("<<ComboboxSelected>>", lambda e: self.populate_fields())

        # Store all widgets in a list for easy access or modification later
        self.entry_widget_list = [self.category_drop] + entries if self.tag == "Add" else [self.category_drop, self.items_selected_drop] + entries

    def config_entry_fields(self):
        """
        Function Name: config_entry_fields
        Description: This function configures the entry fields for the main UI
        """
        # Set the entry fields to be disabled if the tag is 'Edit'
        if self.tag == "Edit":
            if self.controller.shared_data.get('generated_password'):
                self.populate_fields()
            else:
                for entry in self.entry_widget_list:
                    entry.config(state='disabled')
                # Disable the 'Generate' button and the 'Items Selected' drop-down
                self.show_btn.config(state='disabled')
                self.gen_btn.config(state='disabled')
                self.items_selected_drop.config(state='readonly')
        else:
            # Set the placeholder text for the entry fields
            placeholders = {
                self.appname_entry: "e.g. Facebook, Twitter, etc.",
                self.username_entry: "e.g. johndoe123",
                self.email_entry: "e.g. youremail@gmail.com",
            }
            # Ensure the placeholder text is displayed in the entry fields
            for entry, placeholder in placeholders.items():
                entry.insert(0, placeholder)
                entry.config(fg='grey')
                entry.bind("<FocusIn>", lambda event, e=entry, ph=placeholder: self.on_entry_click(event, e, ph))
                entry.bind("<FocusOut>", lambda event, e=entry, ph=placeholder: self.on_focus_out(event, e, ph))

            # Special handling for the Text widget for hint
            self.hint_entry.insert("1.0", "Add any additional notes or hints here...")
            self.hint_entry.config(fg='grey')
            self.hint_entry.bind("<FocusIn>", lambda event, e=self.hint_entry, ph="Add any additional notes or hints here...": self.on_entry_click(event, e, ph))
            self.hint_entry.bind("<FocusOut>", lambda event, e=self.hint_entry, ph="Add any additional notes or hints here...": self.on_focus_out(event, e, ph))

    def create_buttons(self):
        """
        Function Name: create_buttons
        Description: This function creates the buttons for the main UI
        """
        if self.tag == "Add":
            y_values = [260, 470]
        else:
            y_values = [300, 520]
        
        # Stylize buttons to match the ui elements
        self.show_btn = Button(self.ui_frame, text="Show", command=self.show_password_btn)
        self.show_btn.place(relx=0.8, y=y_values[0], anchor="center")
        self.gen_btn = Button(self.ui_frame, text="Generate", width=10, command=self.generate_btn)
        self.gen_btn.place(relx=0.25, y=y_values[0], anchor="e")
        Button(self.ui_frame, text="Back", width=10, command=self.back_btn).place(relx=0.3, y=y_values[1], anchor="center")
        Button(self.ui_frame, text="Reset", width=10, command=self.clear_entry).place(relx=0.5, y=y_values[1], anchor="center")
        Button(self.ui_frame, text="Submit", width=10, command=self.submit_btn).place(relx=0.7, y=y_values[1], anchor="center")
        
    def get_user_input(self):
        """ 
        Function Name: get_user_input
        Function Purpose: This function gets and sets the user input.
        """   
        # This function would actually get input from GUI fields or console input
        item_selected = self.items_selected_drop.get() if self.tag != "Add" else None
        category = self.category_drop.get()
        appname = self.appname_entry.get()
        username = self.username_entry.get()
        first_password = self.first_password_entry.get()
        second_password = self.second_password_entry.get()
        email = self.email_entry.get()
        
        # Get the text input from the hint entry
        hint = self.hint_entry.get("1.0", "end-1c")

        # Create a user object entry list of the input values
        return [item_selected, category, appname, username, first_password, second_password, email, hint]

    def validate_drop_inputs(self):
        """
        Function Name: validate_drop_inputs
        Function Purpose: This function validates the drop menu user inputs.
        """
        # Get the user input and set the error dictionary
        input_list = self.get_user_input()
        errors = {}
        
        # Always check for category selection regardless of the tag
        if not self.category_drop.get().strip():
            errors['category_drop'] = "Please select a category"

        # Check for item selection if the tag is not 'Add'
        if self.tag != "Add":
            if not self.items_selected_drop.get().strip():
                all_other_fields_filled = all(entry.get().strip() for entry in self.entry_widget_list[:-1] if entry != self.items_selected_drop)
                if not all_other_fields_filled:
                    errors['items_selected_drop'] = "Please select an item from the list"

        return input_list, errors
    
    def submit_btn(self):
        """ 
        Function Name: submit_btn
        Function Purpose: This function is executed once the user enters their user name and password
        """
        # Set all the backgrounds to white
        self.set_bg_to_white(self.entry_widget_list)
        
        # Get the user input
        input_list, errors = self.validate_drop_inputs()
        if errors:
            for field, error in errors.items():
                self.set_invalid(getattr(self, field), error)
            return
        
        # Set the index based off the tag
        if self.tag == "Add":
            input_list.pop(0)
            category_idx = 0
            account_name_idx = 1
            username_idx = 2
            first_pswrd_idx = 3
            second_pswrd_idx = 4
            email_idx = 5
            note_idx = 6
        else:
            category_idx = 1
            account_name_idx = 2
            username_idx = 3
            first_pswrd_idx = 4
            second_pswrd_idx = 5
            email_idx = 6
            note_idx = 7
            
        # First check if the two user passwords are the same and if not, to return warning the user didn't 
        # enter the same password
        if input_list[first_pswrd_idx] != input_list[second_pswrd_idx]:
            self.set_invalid([self.first_password_entry, self.second_password_entry], invalid_pswrd_msg)
            return

        # Declare the Error Message
        invalid_pswrd_msg = "Passwords do not match. Please try again."
        confirmation_message = (
            f"You are about to add a new account named '{input_list[1]}' under the category '{input_list[0]}'.\n\n"
            "Adding this account will allow you to manage its details through this tool. \n\n"
            "Do you want to proceed?"
        )
        edit_message = (
            f"You are about to edit an existing account named '{input_list[3]}' under the category '{input_list[1]}'.\n\n"
            "Editing this account will update its information within this tool. It is recommended to carefully review "
            "and confirm all changes, especially if they affect crucial details like username or password.\n\n"
            "Proceeding with this update can help ensure that the account details remain accurate and relevant to the "
            "category it's associated with. \n\n"
            "Do you want to proceed with these changes?"
            )

        # Debug, make sure to comment this out after testing
        User.user_id = 1
        
        try:
            # Attempt to create a Account object with the provided credentials
            acc_obj = Account(
                account_id=Add_Edit_Account_UiComposable.selected_index + 1,
                user_id=User.user_id,
                account_name=input_list[account_name_idx], 
                account_username=input_list[username_idx], 
                account_password=input_list[first_pswrd_idx], 
                account_email=input_list[email_idx],
                category=input_list[category_idx],
                notes=input_list[note_idx]
            )
            
            if self.tag == "Add":
                # Make sure to get the user acceptance to add the new account
                response = messagebox.askyesno("Confirm New Account", confirmation_message)
                if response:
                    acc_obj.add_new_account()
                    self.clear_entry_widget(self.entry_widget_list)
                    acc_obj.delete_account_data()
                    self.back_btn()
            else:
                # Make sure to get the user acceptance to edit the selected account
                response = messagebox.askyesno("Confirm Edit Account", edit_message)
                if response:
                    acc_obj.edit_account()
                    self.clear_entry_widget(self.entry_widget_list)
                    acc_obj.delete_account_data()
                    self.back_btn()
                    
        except ValueError as e:
            # Handle specific field errors based on message content
            if 'category' in str(e).lower():
                self.set_invalid(self.category_drop, str(e))
            elif 'items selected' in str(e).lower():
                self.set_invalid(self.items_selected_drop, str(e))
            elif 'acount name' in str(e).lower():
                self.set_invalid(self.appname_entry, str(e))
            elif 'username' in str(e).lower():
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
            self.first_password_entry.delete(0, END)
            self.first_password_entry.insert(0, generated_password)
            self.first_password_entry.config(show='*')
            self.second_password_entry.delete(0, END)
            self.second_password_entry.insert(0, generated_password)
            self.second_password_entry.config(show='*')

    def convert_data(self):
        """ 
        Function Name: convert_data
        Function Purpose: This function is converts the data passed to only represent the user name and app name
        """      
        if self.data is not None and len(self.data) > 0:
            for data in self.data:
                self.selected_data.append(data[0] + " - " + data[1])
        else:
            self.data = Add_Edit_Account_UiComposable.stored_selected_data
            for data in self.data:
                self.selected_data.append(data[0] + " - " + data[1])

    def populate_fields(self):
        """
        Function Name: populate_fields
        Description: Populate the entry fields based on the selected item in the dropdown.
        """
        # Get the index of the selected item
        if self.items_selected_drop.get() is not None and len(self.items_selected_drop.get()) > 0:
            Add_Edit_Account_UiComposable.selected_index = self.items_selected_drop.current()
        else: 
            self.convert_data()

        # Check if an item is selected
        if Add_Edit_Account_UiComposable.selected_index >= 0:
            # Get the data tuple for the selected index
            selected_item = self.data[Add_Edit_Account_UiComposable.selected_index]

            # Set the config state to normal
            for entry in self.entry_widget_list:
                entry.config(state='normal')
                
            # Set the buttons to normal
            self.show_btn.config(state='normal')
            self.gen_btn.config(state='normal')
            
            # Clear existing entries
            self.appname_entry.delete(0, END)
            self.username_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.hint_entry.delete("1.0", END)
            
            # Insert the data into the fields
            if self.controller.shared_data.get('generated_password'):
                self.load_generated_password()
                self.appname_entry.insert(0, selected_item[0])
                self.username_entry.insert(0, selected_item[1])
                self.email_entry.insert(0, selected_item[2])
            else:
                self.appname_entry.insert(0, selected_item[0])
                self.username_entry.insert(0, selected_item[1])
                self.first_password_entry.insert(0, selected_item[3])
                self.second_password_entry.insert(0, selected_item[3])
                self.email_entry.insert(0, selected_item[2])
            
            # Replace the underscore with a space
            category = selected_item[5].replace("_", " ")
            self.category_drop.set(category)

        else:
            messagebox.showerror("Selection Error", "No item selected or available for editing.")

    def clear_entry(self):
        """ 
        Function Name: clear_entry
        Function Purpose: This function is executed if the user clicks clear. The fields should be deleted
        """
        # Delete the content of the entry widgets
        self.clear_entry_widget(self.entry_widget_list)
        self.set_bg_to_white(self.entry_widget_list)
        
        # Return focus to first input
        if self.tag == "Add":
            self.category_drop.focus()
        else:
            self.config_entry_fields()
            self.items_selected_drop.focus()
    
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
        # Hide the current frame    
        #self.hide_child_frame()
        self.destroy_child_frame()
        
        Add_Edit_Account_UiComposable.stored_selected_data = self.controller.shared_data.get('selected_data')
        print(Add_Edit_Account_UiComposable.stored_selected_data)
        
        # Load the generate custom frame Ui
        self.cust_pswrd_gen = CustomPasswordGen_UiComposable(self.parent, self.controller, tag=self.tag, crud_frames=self.frame)
        
    def back_btn(self):
        """ 
        Function Name: back_btn
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Back', the widow is destroyed and the user is sent back to the previous page 
        """   
        # Import the view_account_ui_composable module 
        from view_account_ui_composable import View_All_Accounts_UiComposable
        
        # Destroy the widgets
        self.destroy_child_frame()
        
        # Load the main dashboard frame
        self.switch_composable(View_All_Accounts_UiComposable, frame_type='crud')
        
            
#######################################################################################################
# Add Account Information Class
#######################################################################################################  

class Add_Accounts_UiComposable(tk.Frame):
    """
    Class Name: Add_Accounts_UiComposable
    Class Description: This class adds an account and composes the base add or edit composable.
    """
    def __init__(self, parent, controller, data=None, crud_frame=None, *args, **kwargs):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """   
        # Create the root tkinter variable
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.controller = controller 
        self.data = data
        self.crud_frame = crud_frame
        self.current_frame = None

        # Set the tag name that controls what to load
        self.tag = "Add"
        
        # Delay the UI setup to after the frame is fully initialized
        self.after(100, self.post_init)
        
    def post_init(self):
        """
        Function Name: post_init
        Description: This function creates the add account UI composable.
        """
        # Attempt to instantiate the base add/edit ui composable
        self.add_obj = Add_Edit_Account_UiComposable(self.parent, self.controller, self.tag, self.data, self.crud_frame)
        self.add_obj.create_ui_frame()  
        
    def is_add_obj_created(self):
        """
        Function Name: is_add_obj_created
        Function Purpose: Checks if the 'add_obj' attribute has been instantiated and still exists.
        Returns:
            bool: True if 'add_obj' is instantiated and not destroyed, False otherwise.
        """
        return self.is_existing

    def destroy_add_ui(self):
        """ 
        Function Name: destroy_add_ui
        Function Purpose: This function destroys the add account UI composable. 
        """    
        # Destroy the widgets
        self.add_obj.destroy_child_frame()
        
#######################################################################################################
# Edit Account Information Class
#######################################################################################################  

class Edit_Accounts_UiComposable(tk.Frame):
    """
    Class Name: Edit_Accounts_UiComposable
    Class Description: This class edits an account and composes the base add or edit composable.
    """
    def __init__(self, parent, controller, data=None, crud_frame=None,*args, **kwargs):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """   
        # Create the root tkinter variable
        super().__init__(parent, *args, **kwargs)
        self.controller = controller 
        self.parent = parent
        self.data = data
        self.crud_frame = crud_frame

        # Set the tag name that controls what to load
        self.tag = "Edit"
        
        # Delay the UI setup to after the frame is fully initialized
        self.after(100, self.post_init)
        
    def post_init(self):
        """
        Function Name: post_init
        Description: This function creates the edit account UI composable.
        """
        # Instantiate the base add/edit ui composable
        self.edit_obj = Add_Edit_Account_UiComposable(self.parent, self.controller, self.tag, self.data, self.crud_frame)
        self.edit_obj.create_ui_frame()        

    def destroy_edit_ui(self):
        """ 
        Function Name: destroy_edit_ui
        Function Purpose: This function destroys the edit account UI composable.  
        """    
        # Destroy the widgets
        self.edit_obj.destroy_child_frame()