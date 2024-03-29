import re
import sys
from tkinter import *
from tkinter import messagebox, ttk, Listbox
import tkinter as tk
from datetime import date, datetime, timedelta
import random
import string
from PIL import Image, ImageTk

# Import project modules
from user_object_class import User
from password_object_class import PasswordWithPolicy


#######################################################################################################
# User Login Class
#######################################################################################################

class UserLogin_UiComposable(tk.Tk):
    """
    Class Name: UserLogin_UiComposable
    Class Description: This class is the main start up page of the program where the user logs into the program.
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
        self.create_main_container()    

        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()           
        sys.exit() # Exit the program if the user closes the window
        
    def create_main_container(self):
        """
        Function Name: create_main_container
        Description: This function creates the main container for the main UI
        """
        # Main container for the main UI
        self.main_container = Frame(self)
        self.main_container.pack(fill="both", expand=True)
        
        # Create the main Ui Frame
        self.create_ui_frame()

    def create_ui_frame(self):
        """
        Function Name: create_ui_frame
        Description: Creates a fixed-size frame for UI elements.
        """
        # Adjust the size as needed
        self.ui_frame = Frame(self.main_container, width=600, height=400, bg='white')  
        self.ui_frame.pack_propagate(False)  # Prevents the frame from resizing to fit its contents
        self.ui_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame within the main_container

        # Call this method to set up the header frame
        self.create_header_frame()
        
        # Call the methods to set labels, entry fields, and buttons within this ui_frame 
        self.create_labels()
        self.create_entry_fields()
        self.create_buttons()

    def create_header_frame(self):
        """
        Function Name: create_header_frame
        Description: Sets up the frame containing the application's header/logo.
        """
        # Create a canvas for the shield logo at the top of the ui_frame
        self.canvas = Canvas(self.ui_frame, width=200, height=200, bg='white', highlightthickness=0)
        self.canvas.pack(pady=20)
        
        # Load the logo image
        logo_path = "ic_logo_small_medium.png" 
        self.shield_logo = Image.open(logo_path)
        self.shield_logo = self.shield_logo.resize((200, 200), Image.Resampling.LANCZOS)
        self.shield_photoimage = ImageTk.PhotoImage(self.shield_logo)
        self.canvas.create_image(100, 100, image=self.shield_photoimage)

        # Call the methods to set labels, entry fields, and buttons within this ui_frame
        self.create_labels()
        self.create_entry_fields()
        self.create_buttons()
        
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
        
    def create_labels(self):
        """
        Function Name: create_labels
        Description: This function creates the labels for the main UI
        """
        # Stylize labels to match the image
        Label(self.ui_frame, text="Username:", bg='white').place(relx=0.4, y=240, anchor="e")
        Label(self.ui_frame, text="Password:", bg='white').place(relx=0.4, y=280, anchor="e")

    def create_entry_fields(self):
        """
        Function Name: create_entry_fields
        Description: This function creates the entry fields for the main UI
        """
        # Create and place entry fields to match the image, centered
        username_entry = Entry(self.ui_frame, width=30)
        password_entry = Entry(self.ui_frame, width=30, show='*')
        
        # Position the entry fields at the center
        username_entry.place(relx=0.6, y=240, anchor="center")
        password_entry.place(relx=0.6, y=280, anchor="center")
        
    def create_buttons(self):
        """
        Function Name: create_buttons
        Description: This function creates the buttons for the main UI
        """
        # Stylize buttons to match the image
        Button(self.ui_frame, text="Exit", width=10).place(relx=0.3, y=340, anchor="center")
        Button(self.ui_frame, text="New", width=10).place(relx=0.5, y=340, anchor="center")
        Button(self.ui_frame, text="Submit", width=10).place(relx=0.7, y=340, anchor="center")
                                                                                                            
    def get_user_input(self):
        """ 
        Function Name: get_user_input
        Function Purpose: This function gets and sets the user input.
        """   
        # This function would actually get input from GUI fields or console input
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Call the function to validate the user input
        self.validate_and_set_user_info(username, password)
            
    def submit_button_click(self):
        """ 
        Function Name: submit_button_click
        Function Purpose: This function is executed once the user enters their user name and password
        """
        # Get the user input
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            # Attempt to create a User object with the provided credentials
            user = User(username=username, user_password=password)
            
            # At this point, the input is valid as per our setters
            
            # Now you would proceed with a database check here for getting the primary key ID's
            
            # Set the user content and prep for db dump
            
            # Delete the username and password entry fields so the data does not persist in some address in RAM
            
            # Destroy the window and open the main dashboard
            
            
        except ValueError as e:
            # If setters raise a ValueError, inform the user
            messagebox.showwarning("Input Error", str(e))
            # Here, clear the entries or highlight them to indicate an error
            self.clear_entry_bg_color()                     

    def check_input(args):
        """ 
        Function Name: check_input
        Function Purpose: This function executes when the user clicks the 'Submit' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        try:
            if args != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.', icon='warning')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        # Return the blnValidate status
        return blnValidate 
            
    def clear_button_click(self):
        """ 
        Function Name: clear_button_click
        Function Purpose: This function is executed if the user clicks clear. The fields should be deleted
        """
        # Delete the login name and login password to reset the text box
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        
        # Clear out the background colors and set to default as 'white'
        self.clear_entry_bg_color()
        
        # Return focus to first input
        self.username_entry.focus()
            
    def clear_entry_bg_color(self):
        """ 
        Function Name: clear_entry_bg_color
        Function Purpose: This function executes when the user submits their entries and clears the background
        color before any validation checks.
        """
        # Delete the button after submission
        self.username_entry.configure(background='White')
        self.password_entry.configure(background='White')

    def exit_button(self):
        """ 
        Function Name: exit_button
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """       
        # Display the user ask question to see if the user would like to exit the program
        if messagebox.askyesno(message="EXIT APPLICATION \n\n Would you like to exit the program?", icon='question'):        
            self.destroy()   
            sys.exit()
            

def Main():
    """ 
    Function Name: Main Start Program
    Function Description: This function begins the program. Open the GUI launch Page
    """
    try:
        # Start the main GUI window  
        userLoginObj = UserLogin_UiComposable()
        
    # Display error message if the entry is invalid
    except Exception as err:
        print("Exception occurred because", err)

# This is the start of main program
if __name__ == '__main__':
    Main()            