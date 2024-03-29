"""
.______    _______ .___________.    ___         .______   .______       _______     ___       __  ___ 
|   _  \  |   ____||           |   /   \        |   _  \  |   _  \     |   ____|   /   \     |  |/  / 
|  |_)  | |  |__   `---|  |----`  /  ^  \       |  |_)  | |  |_)  |    |  |__     /  ^  \    |  '  /  
|   _  <  |   __|      |  |      /  /_\  \      |   _  <  |      /     |   __|   /  /_\  \   |    <   
|  |_)  | |  |____     |  |     /  _____  \     |  |_)  | |  |\  \----.|  |____ /  _____  \  |  .  \  
|______/  |_______|    |__|    /__/     \__\    |______/  | _| `._____||_______/__/     \__\ |__|\__\                                                                                                       
"""
"""
Project Name: Beta Break 0.0.02
Developer: David Teixeira
Date: 02/23/2023
Abstract: This project is vol 0.0.2 to store and retrieve data for PPE Inspections
"""

# Import Python Libraries
from functools import partial
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk, Listbox
from PIL import Image, ImageTk
from FragmentUiComposable import ItemType_NewInspection_Action, Ui_Default_ItemSelection


# Import project modules
from ToolTip import CreateToolTip
from UiDataTypeModel import ItemType


#######################################################################################################
# Main Ui Composable Class
#######################################################################################################        

class Main_UiComposable(tk.Tk):
    """
    Class Name: Main_UiComposable
    Class Description: This class is for the main UI of the program. It will be the first page the user sees when they open the program. 
    """
    def __init__(self, *args, **kwargs):
        # Create the root tkinter variable
        super().__init__(*args, **kwargs)

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Set the window to open with the full screen width and height
        self.geometry(f"{self.widthSize}x{self.heightSize}")
        
        # Set the maximized state of the window
        self.state('zoomed')
        
        # Set window title
        self.title("Beta Break 0.0.02")
        self.resizable(True, True)

        # Load the file menu Ui Composable
        self.fileMenu_UiComposable()

        # Load the sidebar Ui Composable
        self.sideBar_UiComposable()
        
        # Create the main container
        self.createMainContainer()

        # Load and set the background image
        self.load_SetBackgroundImg()       
                
        # Create the dynamic column
        self.createDynamicColumn()     
                
        # Initialize the panedWindowHidden to True so it starts hidden
        self.panedWindowHidden = True
        self.lastAction = None
        self.currently_selected_icon = None   
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()  

    def on_window_resize(self, event):
        """
        Function Name: on_window_resize
        Description: This function creates the background image window for the main UI
        """
        # Check if the canvas still exists before trying to modify it
        if self.bg_canvas.winfo_exists():
            # Recalculate the center position based on the current window size
            center_x = self.winfo_width() // 2 - self.bg_image.width() // 2
            center_y = self.winfo_height() // 2 - self.bg_image.height() // 2

            # Move the background image to the new center position
            self.bg_canvas.coords(self.bg_image_id, center_x, center_y)
        
    def load_SetBackgroundImg(self):
        """
        Function Name: load_SetBackgroundImg
        Description: This function creates the background image for the main UI
        """
        # Set the flag to indicate the background image is not hidden
        self.blnBackgroundImg_Hidden = False
        
        # Bind the resize event
        self.bind("<Configure>", self.on_window_resize) 
        
        # Load the image
        image_path = "ic_bb_background.png"
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

        image.putdata(newData)

        # Convert processed image for Tkinter
        self.bg_image = ImageTk.PhotoImage(image)

        # Create a Canvas for the background image
        self.bg_canvas = tk.Canvas(self.main_container, width=self.widthSize, height=self.heightSize)
        self.bg_canvas.pack(fill="both", expand=True)

        # Calculate the center position and place the image
        center_x = self.widthSize // 2 - self.bg_image.width() // 2
        center_y = self.heightSize // 2 - self.bg_image.height() // 2
        self.bg_image_id = self.bg_canvas.create_image(center_x, center_y, anchor="nw", image=self.bg_image)

    def remove_background_image(self):
        """
        Function Name: remove_background_image
        Description: This function removes the background image from the main UI.
        """
        # Set the flag to indicate the background image is hidden
        self.blnBackgroundImg_Hidden = True
        
        # Unbind the resize event
        self.bg_canvas.delete(self.bg_image_id)
        self.bg_canvas.destroy()
                
    def createMainContainer(self):
        """
        Function Name: createMainContainer
        Description: This function creates the main container for the main UI
        """
        # Main container for dynamic columns
        self.main_container = ttk.PanedWindow(self, orient="horizontal")
        self.main_container.pack(fill="both", expand=True)
        
        # Create the dynamic column dictionary
        self.additional_DynamicColumns = []
            
    def fileMenu_UiComposable(self):
        """
        Function Name: fileMenu_UiComposable
        Description: This function creates the file menu for the main UI
        """
        # Create a menu bar
        self.menuBar = tk.Menu(self)
        self.config(menu=self.menuBar)
        
        # Add 'File' menu
        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="New", command=self.newFile)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.quit)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)

        # Add 'Edit' menu
        self.editMenu = tk.Menu(self.menuBar, tearoff=0)
        self.editMenu.add_command(label="Undo", command=self.undoAction)
        self.menuBar.add_cascade(label="Edit", menu=self.editMenu)

        # Add 'Go' menu
        self.goMenu = tk.Menu(self.menuBar, tearoff=0)
        self.goMenu.add_command(label="Home", command=self.goHome)
        self.menuBar.add_cascade(label="Go", menu=self.goMenu)

        # Add 'View' menu
        self.viewMenu = tk.Menu(self.menuBar, tearoff=0)
        self.viewMenu.add_command(label="Zoom In", command=self.zoomIn)
        self.viewMenu.add_command(label="Zoom Out", command=self.zoomOut)
        self.menuBar.add_cascade(label="View", menu=self.viewMenu)

        # Add 'Help' menu
        self.helpMenu = tk.Menu(self.menuBar, tearoff=0)
        self.helpMenu.add_command(label="About", command=self.showAbout)
        self.menuBar.add_cascade(label="Help", menu=self.helpMenu)

    # Define the command functions
    def newFile(self):
        # Functionality to create a new file
        messagebox.showinfo("New", "Create a new file...")

    def undoAction(self):
        # Undo functionality
        messagebox.showinfo("Undo", "Undo action...")

    def goHome(self):
        # Navigate to the home screen
        messagebox.showinfo("Go", "Going home...")

    def zoomIn(self):
        # Zoom in functionality
        messagebox.showinfo("Zoom In", "Zooming in...")

    def zoomOut(self):
        # Zoom out functionality
        messagebox.showinfo("Zoom Out", "Zooming out...")

    def showAbout(self):
        # Display the 'About' dialog
        messagebox.showinfo("About", "Beta Break 0.0.02\n© 2024")   
                
    def sideBar_UiComposable(self):
        """
        Function Name: sideBar_UiComposable
        Description: This function creates the sidebar for the main UI
        """
        # Create a sidebar frame
        self.sidebar = tk.Frame(self, width=200, bg='#dddddd')
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=0, pady=0)

        # Define icon paths and corresponding tooltips, excluding the settings icon for now
        icon_info = [
            ('ic_auto_belay.png', "Auto Belays", self.populateAutoBelay_Sub_Menu_Options),
            ('ic_belay_device.png', "Belay Devices", self.populateBelayDevice_Sub_Menu_Options),
            ('ic_carabiner.png', "Connectors", self.populateConnectors_Sub_Menu_Options),
            ('ic_harness.png', "Harnesses", self.populateHarness_Sub_Menu_Options),
            ('ic_rope.png', "Ropes", self.populateRope_Sub_Menu_Options),
            ('ic_drill.png', "Route Setting Equipment", self.populateRouteSet_Sub_Menu_Options),
        ]

        # Load, resize icons, and create buttons with tooltips
        for icon_path, tooltip_text, action in icon_info:
            self.createIconButton(icon_path, tooltip_text, action)

        # Separately handle the settings icon to place it at the bottom
        self.createIconButton('ic_settings.png', "Settings", self.load_Settings_UiComposable, place_bottom=True)

    def createIconButton(self, icon_path, tooltip_text, action, place_bottom=False):
        """
        Function Name: createIconButton
        Description: Helper function to create an icon button with a tooltip.
        """
        icon = self.resize_Icon(icon_path)
        button_canvas = tk.Canvas(self.sidebar, width=50, height=50, bg='#dddddd', highlightthickness=0, bd=0)
        if place_bottom:
            button_canvas.pack(side='bottom', pady=10)
        else:
            button_canvas.pack(pady=10)
        button_canvas.create_image(25, 25, image=icon)
        button_canvas.bind("<Button-1>", lambda event, a=action, btn=button_canvas: self.onIconClick(event, a, btn))  # Bind to onIconClick
        CreateToolTip(button_canvas, tooltip_text)
        button_canvas.image = icon  # Keep a reference to avoid garbage collection

    def resize_Icon(self, icon_path, size=(32, 32)):
        """
        Function Name: resize_Icon
        Description: This function resizes the icon to the specified width and height
        """
        image = Image.open(icon_path)
        resized_image = image.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(resized_image)

    def createDynamicColumn(self):
        """
        Function Name: createDynamicColumn
        Description: This function creates the dynamic column for the main UI
        """
        # Create the Panedwindow widget
        self.panedWindow = ttk.Panedwindow(self, orient=tk.HORIZONTAL)
        
        # Create the dynamic column as a Frame
        self.dynamicColumn = tk.Frame(self.panedWindow, bg='lightgrey', width=200)
        
        # Add the dynamic column to the Panedwindow but don't pack it yet
        self.panedWindow.add(self.dynamicColumn, weight=1)

        # Keep commented out to ensure there is no re-sizeable handle
        # Create a handle for resizing
        self.handle = ttk.Separator(self.panedWindow, orient=tk.VERTICAL)
        self.panedWindow.add(self.handle, weight=0)

        # Bind the handle to a method that resizes the paned window
        self.handle.bind('<B1-Motion>', self.resize_Pane)

    def add_paned_window(self, action=None):
        """
        Function Name: add_paned_window
        Description: This function adds a new paned window to the main paned window
        """
        if self.blnBackgroundImg_Hidden == False:
            # Call to hide the background image
            self.remove_background_image()
        
        # First check the count of the additional dynamic frames created, if exceeding 3, then return a message
        if len(self.additional_DynamicColumns) >= 3:
            messagebox.showinfo("Error", "You can only display up to 3 additional frames. Please remove a frame to add another.")
            return
        
        self.new_column = ttk.Frame(self.main_container, relief="sunken", width=200)
        self.new_column.pack_propagate(False)  # Prevent the frame from shrinking to fit its contents
        self.new_column.grid_columnconfigure(0, weight=1)  # Center the content horizontally
        self.new_column.grid_rowconfigure(0, weight=1)  # Center the content vertically

        close_btn = ttk.Button(self.new_column, text="X", command=lambda col=self.new_column: self.remove_paned_window(col))
        close_btn.pack(anchor="ne")
        self.main_container.add(self.new_column, weight=1)
        self.additional_DynamicColumns.append(self.new_column) 
            
        # Execute the action with the new column as its argument
        if action:
            action(self.new_column)
        
    def remove_paned_window(self, column):
        """
        Function Name: remove_paned_window
        Description: This function removes the specified paned window from the main paned window
        """
        # Remove the column from the Panedwindow
        self.main_container.forget(column)
        # Destroy the column's widget
        column.destroy()
        # Remove the column from our list of dynamic columns
        self.additional_DynamicColumns.remove(column)
        
        # Check if the additional dynamic columns list is empty
        if len(self.additional_DynamicColumns) == 0:
            self.load_SetBackgroundImg()
                    
    def showOrHidePane(self):
        """
        Function Name: showOrHidePane
        Description: Shows or hides the panedWindow containing the dynamic column.
        """
        if self.panedWindowHidden:
            # If hidden, show the paned window
            self.panedWindow.place(x=50, rely=0.0, relheight=1.0)
            self.panedWindowHidden = False
        else:
            # If shown, hide the paned window
            self.panedWindow.place_forget()
            self.panedWindowHidden = True
                
    def resize_Pane(self, event):
        """
        Function Name: resize_Pane
        Description: This function resizes the pane based on the event
        """
        # Calculate the new width for the dynamic column
        new_width = event.x
        
        # Set minimum width to prevent the pane from becoming too small
        min_width = 100  # Minimum width in pixels
        if new_width < min_width:
            new_width = min_width
        
        # Adjust the width of the dynamic column
        self.dynamicColumn.config(width=new_width)
        
        # Update the Panedwindow sash position
        self.panedWindow.sash_place(0, new_width, 0)

    def populateAutoBelay_Sub_Menu_Options(self):
        """
        Function Name: populateAutoBelay_Sub_Menu_Options
        Description: This function populates the sub menu options in the dynamic column
        """
        # Clear previous content if any
        self.remove_Widget_Options()

        # Define the main options and their corresponding detailed options
        main_options = self.sideBar_SubMenuOptions_List().get("AutoBelays")
        
        # Set the ITemType to AutoBelays
        self.itemType = ItemType.AUTOBELAYS
        
        # Set the main options and their corresponding detailed options
        self.create_SubOption_Container(main_options)

    def populateBelayDevice_Sub_Menu_Options(self):
        """
        Function Name: populateBelayDevice_Sub_Menu_Options
        Description: This function populates the sub menu options in the dynamic column
        """
        # Clear previous content if any
        self.remove_Widget_Options()

        # Define the main options and their corresponding detailed options
        main_options = self.sideBar_SubMenuOptions_List().get("BelayDevices")
        
        # Set the ITemType to BelayDevices
        self.itemType = ItemType.BELAYDEVICES
        
        # Set the main options and their corresponding detailed options
        self.create_SubOption_Container(main_options)
        
    def populateConnectors_Sub_Menu_Options(self):
        """
        Function Name: populateConnectors_Sub_Menu_Options
        Description: This function populates the sub menu options in the dynamic column
        """
        # Clear previous content if any
        self.remove_Widget_Options()

        # Define the main options and their corresponding detailed options
        main_options = self.sideBar_SubMenuOptions_List().get("Connectors")

        # Get the itemType for "Connectors"
        self.itemType = self.map_main_option_to_ItemType("Connectors")

        # Pass both main options and action mappings to create_SubOption_Container
        action_mappings = self.sideBar_SubMenu_Button_Options_List(self.itemType)
        self.create_SubOption_Container(main_options, action_mappings)
    
    def populateHarness_Sub_Menu_Options(self):
        """
        Function Name: populateHarness_Sub_Menu_Options
        Description: This function populates the sub menu options in the dynamic column
        """
        # Clear previous content if any
        self.remove_Widget_Options()

        # Define the main options and their corresponding detailed options
        main_options = self.sideBar_SubMenuOptions_List().get("Harnesses")
        
        # Set the ITemType to Harnesses
        self.itemType = ItemType.HARNESS
        
        # Set the main options and their corresponding detailed options
        self.create_SubOption_Container(main_options)
        
    def populateRope_Sub_Menu_Options(self):
        """
        Function Name: populateRope_Sub_Menu_Options
        Description: This function populates the sub menu options in the dynamic column
        """
        # Clear previous content if any
        self.remove_Widget_Options()

        # Define the main options and their corresponding detailed options
        main_options = self.sideBar_SubMenuOptions_List().get("Ropes")
        
        # Set the ITemType to Ropes
        self.itemType = ItemType.ROPES
        
        # Set the main options and their corresponding detailed options
        self.create_SubOption_Container(main_options)

    def populateRouteSet_Sub_Menu_Options(self):
        """
        Function Name: populateRouteSet_Sub_Menu_Options
        Description: This function populates the sub menu options in the dynamic column
        """
        # Clear previous content if any
        self.remove_Widget_Options()

        # Define the main options and their corresponding detailed options
        main_options = self.sideBar_SubMenuOptions_List().get("RouteSettingEquipment")
        
        # Set the ITemType to RouteSettingEquip
        self.itemType = ItemType.ROUTESETTINGEQUIP
        
        # Set the main options and their corresponding detailed options
        self.create_SubOption_Container(main_options)
                            
    def remove_Widget_Options(self):
        """
        Function Name: remove_Widget_Options
        Description: This function removes all the widgets from the pane window.
        """
        # Clear previous content if any
        for widget in self.dynamicColumn.winfo_children():
            widget.destroy()

    def create_SubOption_Container(self, main_option_dict, action_mappings):
        """
        Function Name: create_SubOption_Container
        Description: This function creates the sub option container for the main UI
        """
        # Declare Local Variables
        aActionList = []
        self.main_options = main_option_dict
        itemType = self.itemType.type_name
        self.option_panes = {}  # Dictionary to keep track of the option panes
        self.option_labels = {}  # Dictionary to keep track of the main option labels

        # For loop to create the sub options
        for main_option, sub_options in self.main_options.items():
            # Create a container frame for each main option
            container_frame = tk.Frame(self.dynamicColumn)
            container_frame.pack(fill='x', padx=5, pady=2)

            # Create a label for the main option and pack it to the left
            label = tk.Label(container_frame, text=main_option, font=("Arial", 10, "bold"), cursor="hand2")
            label.pack(side='top', fill='x', anchor='w')
            label.bind("<Button-1>", lambda event, mo=main_option: self.toggle_option_pane(mo))
            self.option_labels[main_option] = label  # Store the label

            # Create a frame for sub-options inside the container_frame but don't pack it yet
            option_pane = tk.Frame(container_frame, bg='lightgrey')
            self.option_panes[main_option] = option_pane

            # Calculate the width based on the longest option text
            max_option_length = max(len(option) for option in sub_options)
            button_width = max(25, max_option_length * 8)  # Adjust the factor (8) according to your font size and style

            # Extract action functions from the action_mappings
            for option, action_func in action_mappings.get(itemType, {}).items():
                aActionList.append((option, action_func))
                
            for a, option in enumerate(sub_options):
                # Retrieve the action for the current option
                action = aActionList[a]
                # print(f"Option: {option}, Action: {action}")  # Debug print
                if action:
                    # If action exists for the option, create a button with it
                    sub_btn = tk.Button(option_pane, text=option, command=lambda action_func=action_func: self.add_paned_window(action_func), width=button_width, height=1, font=("Arial", 10))
                    sub_btn.pack(expand=True, fill='x')
                else:
                    # Handle the case where no action is defined for the option
                    print(f"No action defined for {option} in {main_option}")

    def map_main_option_to_ItemType(self, main_option):
        """
        Maps the main option string to an ItemType enum value.
        Adjust this mapping based on your application's structure and enum definitions.
        """
        option_map = {
            "Connectors": ItemType.CONNECTORS,
            # Add other mappings as necessary
        }
        return option_map.get(main_option)
        
    def toggle_option_pane(self, main_option):
        """
        Toggle the visibility of the sub-options pane for a main option.
        """
        option_pane = self.option_panes[main_option]

        # Check if the pane is currently visible
        if option_pane.winfo_ismapped():
            option_pane.pack_forget()  # Hide the pane
        else:
            # Hide all other panes first
            for pane in self.option_panes.values():
                pane.pack_forget()
            # Now show the current pane directly under the label within the same container
            option_pane.pack()
                            
    def onIconClick(self, event, action, button_canvas):
        """ 
        Function Name: onIconClick
        Description: This function toggles the paned window column and executes the action
        """
        # Reset background of previously selected icon if exists
        if self.currently_selected_icon:
            self.currently_selected_icon.configure(bg='#dddddd')  # Reset background to default
        # Highlight the currently selected icon
        button_canvas.configure(bg='lightblue')  # Highlight selection
        self.currently_selected_icon = button_canvas  # Update the reference to the currently selected icon
        
        # The rest of the logic remains the same
        if action == self.lastAction and not self.panedWindowHidden:
            # Hide the paned window if the same action is triggered and it's currently visible
            self.showOrHidePane()
        else:
            # Show the paned window and populate options for any other cases
            if self.panedWindowHidden:
                self.showOrHidePane()
            action()  # Execute the corresponding action
        self.lastAction = action  # Update the last action
                
    def onOptionSelected(self, option):
        print(f"{option} selected")

    def sideBar_SubMenuOptions_List(self):
        """
        Function Name: sideBar_SubMenuOptions_List
        Description: This function creates the sidebar sub main UI options. Be sure to add more features for 
        reviewing the reports later on.
        """
        # Create the dictionaries for the sub options
        return {
            'AutoBelays': {            
                "Conduct Inspection": ["New"],
                "Review Reports": [
                    "View Unit Info", 
                    "View Future Inspection Dates", 
                    "View Future Service Dates", 
                    "View Unit Wall Locations", 
                    "View Units Out For Reservice", 
                    ],
            "Open Reports": ["Open"],
            "Download Reports": ["Download"]
            },
            'BelayDevices': {
                "Conduct Inspection": ["New"],
                "Review Reports": [
                    "View Belay Device Info", 
                    "View Future Inspection Dates", 
                    "View Belay Device Wall Locations", 
                    ],
            "Open Reports": ["Open"],
            "Download Reports": ["Download"]                
            },
            'Connectors': {
                "Conduct Inspection": ["New"],
                "Review Reports": [
                    "View Connector Info", 
                    "View Future Inspection Dates", 
                    "View Connector Wall Locations", 
                    ],
            "Open Reports": ["Open"],
            "Download Reports": ["Download"]                
            },
            'Harnesses': {
                "Conduct Inspection": ["New"],
                "Review Reports": [
                    "View Harness Info", 
                    "View Future Inspection Dates", 
                    ],
            "Open Reports": ["Open"],
            "Download Reports": ["Download"]                
            },
            'Ropes': {
                "Conduct Inspection": ["New"],
                "Rope System Setup": ["Open"],
                "Review Reports": [
                    "View Rope Info", 
                    "View Rope System Info", 
                    "View Future Inspection Dates", 
                    "View Rope Wall Locations", 
                    ],
            "Open Reports": ["Open"],
            "Download Reports": ["Download"]                
            },
            'RouteSettingEquipment': {
                "Conduct Inspection": ["New"],
                "Review Reports": [
                    "View Route Setting Info", 
                    ],
            "Open Reports": ["Open"],
            "Download Reports": ["Download"]                
            }
        }

    def sideBar_SubMenu_Button_Options_List(self, itemType):
        """
        Function Name: sideBar_SubMenu_Button_Options_List
        Description: This function generates the sub menu button options for the main UI and contains the executable methods
        required for each button.
        """
        # Map each option to a function that creates the necessary UI within the parent frame.
        return {
            'Connectors': {
                "New": lambda frame: self.load_Connector_UiComposable(frame, itemType),
                "View Connector Info": lambda frame: self.load_Connector_UiComposable(frame, itemType),
                "View Future Inspection Dates": lambda frame: self.load_Connector_UiComposable(frame, itemType),
                "View Connector Wall Locations": lambda frame: self.load_Connector_UiComposable(frame, itemType),
                "Open": lambda frame: self.load_Connector_UiComposable(frame, itemType),
                "Download": lambda frame: self.load_Connector_UiComposable(frame, itemType)              
            },
        }
        
    def load_AutoBelay_UiComposable(self, frame):
        """
        Function Name: load_AutoBelay_UiComposable
        Description: This function loads the Auto Belay UI Composable
        """
        print("load_AutoBelay_UiComposable triggered")

    def load_BelayDevice_UiComposable(self, frame):
        """
        Function Name: load_BelayDevice_UiComposable
        Description: This function loads the Belay Device UI Composable
        """
        print("load_BelayDevice_UiComposable triggered")
        
    def load_Connector_UiComposable(self, frame, itemType):
        """
        Function Name: load_Connector_UiComposable
        Description: This function loads the Connector UI Composable
        """
        # Optionally, give the frame a name for identification
        setattr(frame, 'frame_name', 'new_column_frame')

        # Debug: Print the frame name
        print(f"Loading UI in frame named: {getattr(frame, 'frame_name', 'Unknown')}")

        # Instantiate the Ui_Default_ItemSelection class within the given frame
        Ui_Default_ItemSelection(frame, itemType)
                
    def load_Harness_UiComposable(self, frame):
        """
        Function Name: load_Harness_UiComposable
        Description: This function loads the Harness UI Composable
        """
        print("load_Harness_UiComposable triggered")
        
    def load_Rope_UiComposable(self, frame):
        """
        Function Name: load_Rope_UiComposable
        Description: This function loads the Rope UI Composable
        """
        print("load_Rope_UiComposable triggered")

    def load_RouteSetting_UiComposable(self, frame):
        """
        Function Name: load_RouteSetting_UiComposable
        Description: This function loads the Route Setting UI Composable
        """
        print("load_RouteSetting_UiComposable triggered")
                
    def load_Settings_UiComposable(self, frame):
        """
        Function Name: load_AutoBelay_UiComposable
        Description: This function loads the Auto Belay UI Composable
        """
        print("load_AutoBelay_UiComposable triggered")                                                



######################################################################################################
# Main Start of Program
#######################################################################################################         

def Main():
    """ 
    Function Name: Main Start Program
    Function Description: This function begins the program. Open the GUI Login Page
    """

    # Display the Main Ui Composable
    app = Main_UiComposable()
    
# This is the start of main program
if __name__ == '__main__':
    Main()