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
from tkinter import *
from tkinter import messagebox, ttk, Listbox
import tkinter as tk

# Import project modules
from UiDataTypeModel import ItemType, ItemType_BoolMap, ItemType_DropMap, ItemType_Serial_BumperNum_CacheMap, ItemType_SetSerial_InUse_Selection
from ObjectClass import Connectors, Bool_Flag, WallLocation

class ItemType_NewInspection_Action():
    """
    Class Name: ItemType_NewInspection_Action
    Class Description: This class executes the new inspection action for the items
    """ 
    # Define a mapping of ItemType to their corresponding actions
    actionMap = {
        ItemType.CONNECTORS: lambda parent: Ui_Default_ItemSelection(parent, ItemType.CONNECTORS),

    }
            
    @staticmethod
    def execute_new_inspection_action(item_type, parent):
        """
        Method Name: execute_new_inspection_action
        Description: Executes the new inspection action for the given item type.
        
        :param item_type: ItemType enum member indicating the type of item.
        :param parent: The parent widget for the new Ui_Default_ItemSelection instance.
        """
        action = ItemType_NewInspection_Action.actionMap.get(item_type)
        if action:
            action(parent)  # Call the action with the parent widget
        else:
            print(f"No action defined for {item_type}.")
            
#######################################################################################################
# Default Ui Composable Item Selection Class
#######################################################################################################             
class Ui_Default_ItemSelection(tk.Frame):
    """
    Class Name: ItemSelection
    Class Description: This class is for conducting item selections.
    """
    def __init__(self, parent, itemType):
        """
        Function Name: __init__
        Function Purpose: Initialize the window for new item selection.
        Parameters:
        - itemType: The type of item being selected.
        - itemData: The data associated with the item type.
        """
        # Initialize the parent class.
        super().__init__(parent) 
        
        # Set the item type and access the mapped data for the given item type.
        self.itemType = itemType
        # Access the mapped data for the given item type.
        self.itemData = ItemType_DropMap.itemData.get(self.itemType, {})

        # Container Frame for centered alignment
        self.setupWindow()
        self.loadSelectionWidget()
        self.createAdditionalInfoFrame()
        self.setupLabels()
        self.setupDropdownMenus()
        self.checkPreviousSelections()
        self.createButtons()
        self.mainloop()

    def setupWindow(self):
        """
        Function Name: setupWindow
        Description: Set up the main window's attributes.
        """
        # Adjust the frame size if necessary
        self.pack(fill="both", expand=True)
        # Apply sunken relief to the main frame if desired
        #self.config(relief="sunken", borderwidth=2)
        
        # Intermediate frame to help with centering
        #centerFrame = ttk.Frame(self)
        #centerFrame.pack(side="top", expand=True)


        # Example of setting up a title label inside the frame if needed:
        #titleLabel = ttk.Label(centerFrame, text=f"{self.itemType} Selection", font=("Arial", 14, "bold"))
        #titleLabel.pack(side="top", pady=10)  # This will center titleLabel within centerFrame        
        # # Adjust the frame size if necessary
        # self.pack(fill="both", expand=True)
        
        # # Example of setting up a title label inside the frame if needed:
        # titleLabel = ttk.Label(self, text=f"{self.itemType} Selection", font=("Arial", 14, "bold"))
        # titleLabel.pack(side="top", pady=10)  # Adjust packing options as necessary.

    def loadSelectionWidget(self):
        """
        Function Name: loadSelectionWidget
        Description: Load the widget for item selection.
        """
        self.Selection_Widget()

    def Selection_Widget(self):
        """ 
        Function Name: Selection_Widget
        Function Purpose: This function populates the search by widget for Serial or Bumper Num search.
        """       
        # Call the mapping method to get serial/bumper number cached list data based on itemType
        itemType = self.itemType
        serialNumCacheList, bumperNumCacheList = self.getCachedItems_FromItemType(itemType)
            
        # Create the first frame to hold the input fields using f-string for concatenation
        self.selectInput = LabelFrame(self, text=f"Select {self.itemType}")
        self.selectInput.place(x=100, y=35, width=450, height=100)

        # Create the labels using f-strings
        self.lblSearchBy_ItemID = Label(self.selectInput, text=f"Query by {self.itemType} ID:")
        self.lblItemID_Selection = Label(self.selectInput, text=f"{self.itemType} ID Selection:")

        # Create the label locations
        self.lblSearchBy_ItemID.place(x=19, y=5)
        self.lblItemID_Selection.place(x=18, y=40)

        # Create variables to hold the value of the selected radio button
        self.objRadioValue = tk.StringVar(value='serial')
        self.objComboValue = tk.StringVar()

        # List objects of serial and bumper values
        self.astrSerialNumList = serialNumCacheList
        self.astrBumperNumList = bumperNumCacheList

        # Create the radio buttons
        self.rbSerial = tk.Radiobutton(self.selectInput, text="Serial Number", variable=self.objRadioValue, value="serial", command=self.Populate_Dropdown)
        self.rbBumper = tk.Radiobutton(self.selectInput, text="Bumper Number", variable=self.objRadioValue, value="bumper", command=self.Populate_Dropdown)

        # Place the radio buttons next to each other using .place()
        self.rbSerial.place(x=190, y=5)
        self.rbBumper.place(x=300, y=5)
                    
        # Create the entry input box
        self.dropItemSelection = ttk.Combobox(self.selectInput, values=self.astrSerialNumList, state='readonly')
        self.dropItemSelection.configure(width=25)

        # Populate the dropdown based on the default radio button selection
        self.Populate_Dropdown()

        # Create the grid for all of the entry input fields
        self.dropItemSelection.place(x=190, y=40)     

    def Populate_Dropdown(self):
        """ 
        Function Name: Populate_Dropdown
        Function Purpose: This function populates the dropdown based on the radio button selection.
        """           
        if self.objRadioValue.get() == "serial":
            self.dropItemSelection["values"] = self.astrSerialNumList
        else:
            self.dropItemSelection["values"] = self.astrBumperNumList
        self.dropItemSelection.set("")           

    def Update_Dropdown_Values(self):
        """ 
        Function Name: Update_Dropdown_Values
        Function Purpose: This function is executed once the user clicks on AddConnector or AddLocation button and updates the drop down
        object list with the new values.
        """           
        # Call the mapping method to get serial/bumper number cached list data based on itemType
        itemType = self.itemType
        serialNumCacheList, bumperNumCacheList = self.getCachedItems_FromItemType(itemType)
        
        # Ensure the dropdowns are Comboboxes and clear their current selections
        if isinstance(self.dropItemSelection, ttk.Combobox):
            self.dropItemSelection.set("") 
        if isinstance(self.dropItemLocation, ttk.Combobox):
            self.dropItemLocation.set("")

        # Update the values for connector selection dropdown
        self.astrSerialNumList = serialNumCacheList
        self.astrBumperNumList = bumperNumCacheList
        if isinstance(self.dropItemSelection, ttk.Combobox):
            self.dropItemSelection['values'] = self.astrSerialNumList

        # Update the values for connector location dropdown
        if isinstance(self.dropItemLocation, ttk.Combobox):
            self.dropItemLocation['values'] = WallLocation.astrWallLocationDesc

        if Bool_Flag.blnComplexWithConnectorFlag is True:
            # Disable the drop location if this class is called from ropes inspection
            self.dropItemLocation.set(WallLocation.strWallLocationDesc)
            self.dropItemLocation.configure(state='disabled')
            
    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)   
        
    def createAdditionalInfoFrame(self):
        """
        Function Name: createAdditionalInfoFrame
        Description: Create the frame for additional information.
        """
        # Create the frame fields
        self.typeFrame = tk.LabelFrame(self, text="Additional Info")
        self.typeFrame.place(x=100, y=140, width=450, height=200)

    def setupLabels(self):
        """
        Function Name: setupLabels
        Description: Set up labels for the form.
        """
        # Directly use the enum's label attribute if self.itemType is an enum member
        self.strInUseLabel = self.itemType.label if isinstance(self.itemType, ItemType) else "Device"
        
        # Create the label for the checkboxes
        self.lblItemLocation = tk.Label(self.typeFrame, text=f"{self.itemType} Location:")
        self.lblInUse = tk.Label(self.typeFrame, text=f"{self.strInUseLabel} In Use:")
        self.lblQuestion = tk.Label(self.typeFrame, text="Can't find what you're looking for?")
                        
        # Create the label locations
        self.lblItemLocation.place(x=35, y=15)
        self.lblInUse.place(x=70, y=55)
        self.lblQuestion.place(x=125, y=95)

    def setupDropdownMenus(self):
        """
        Function Name: setupDropdownMenus
        Description: Set up dropdown menus for the form.
        """
        self.astrWallLocationList = WallLocation.astrWallLocationDesc if WallLocation.astrWallLocationDesc else ""
            
        # Create the drop down menu list for each attribute
        self.dropItemLocation = ttk.Combobox(self.typeFrame, values=self.astrWallLocationList, state='readonly')
        self.dropInUse = ttk.Combobox(self.typeFrame, values=['Yes', 'No'], state='readonly')
        
        # Create the drop down menu size for each attribute
        self.dropItemLocation.configure(width=25)
        self.dropInUse.configure(width=25)
        
        # Create the grid for the drop down menu list objects
        self.dropItemLocation.place(x=190, y=15)  
        self.dropInUse.place(x=190, y=55)  

    def checkPreviousSelections(self):
        """
        Function Name: checkPreviousSelections
        Description: Check and set previous selections if any based on the item type.
        """
        # Assuming self.itemType is set to an ItemType enum member
        itemType = self.itemType
        strWallLocation = WallLocation.strWallLocationDesc if WallLocation.strWallLocationDesc else ""

        # Call the mapping method to get serial/bumper number and in use data based on itemType
        serialNum, bumperNum, equipInUse = self.getDropItems_FromItemType(itemType)
        
        # Call the bool mapping method to get the boolean flags based on itemType
        complexWithConnectorFlag, itemPersistFlag, serialNumRadioSelect = self.getBoolFlags_FromItemType(itemType)
        
        # Disable the drop location if this class is called from ropes inspection
        if complexWithConnectorFlag:
            self.dropItemLocation.set(strWallLocation)
            self.dropItemLocation.configure(state='disabled')
            self.dropInUse.set("Yes")
            self.dropInUse.configure(state='disabled')

        # Check if the cache values for any drop menus have been previously selected and set the values
        if itemPersistFlag:
            if serialNumRadioSelect:
                self.Set_Previous_Drop_List(serialNum, self.dropItemSelection)
                self.dropItemSelection["values"] = serialNum
            else:
                self.objRadioValue.set("bumper")
                self.dropItemSelection["values"] = bumperNum
                self.Set_Previous_Drop_List(bumperNum, self.dropItemSelection)
            self.Set_Previous_Drop_List(equipInUse, self.dropInUse)
            self.Set_Previous_Drop_List(strWallLocation, self.dropItemLocation)

    def getDropItems_FromItemType(self, itemType):
        """
        Function Name: getDropItems_FromItemType
        Description: Method to return serial, bumper number, and device in use items based on the item type.
        """
        # Initialize with default values in case the item type is not found in the data source
        serialNum = ""
        bumperNum = ""
        equipInUse = ""

        # Retrieve data from the ItemType_DropMap based on itemType
        if itemType in ItemType_DropMap.itemData:
            data = ItemType_DropMap.itemData[itemType]
            # Assign values directly from the map
            serialNum = data.get('serialNum', "")
            bumperNum = data.get('bumperNum', "")
            equipInUse = data.get('equipInUse', "")

        return serialNum, bumperNum, equipInUse

    def getBoolFlags_FromItemType(self, itemType):
        """
        Method to return boolean flags based on the item type.
        """
        # Initialize with default values in case the item type is not found in the data source
        complexWithConnectorFlag = False
        itemPersistFlag = False
        serialNumRadioSelect = False

        # Retrieve boolean flags from the ItemType_BoolMap based on itemType
        if itemType in ItemType_BoolMap.itemData:
            data = ItemType_BoolMap.itemData[itemType]
            # Assign boolean values directly from the map
            complexWithConnectorFlag = data.get('complexWithConnectorFlag', False)
            itemPersistFlag = data.get('itemPersistFlag', False)
            serialNumRadioSelect = data.get('serialNumRadioSelect', False)

        return complexWithConnectorFlag, itemPersistFlag, serialNumRadioSelect

    def createButtons(self):
        """
        Function Name: createButtons
        Description: Create action buttons for the form.
        """
        # Create the buttons
        self.btnUpdateItemInfo = Button(self.typeFrame, width=12, text=f"Update {self.strInUseLabel}", command=self.Update_Item_Info)
        self.btnAddItem = Button(self.typeFrame, width=12, text=f"Add {self.itemType}", command=self.Add_Item)
        self.btnAddLocation = Button(self.typeFrame, width=12, text="Add Location", command=self.Add_Location)
        self.btnExit = Button(self, width=10, text="Back", command=self.Back)
        self.btnReset = Button(self, width=10, text="Reset",command=self.Reset)
        self.btnNext = Button(self, width=10, text="Next", command=self.Next)
            
        # Create the position of the button
        self.btnUpdateItemInfo.place(x=40, y=140)
        self.btnAddItem.place(x=175, y=140) 
        self.btnAddLocation.place(x=310, y=140)
        self.btnExit.place(x=170, y=360) 
        self.btnNext.place(x=400, y=360) 
        self.btnReset.place(x=285, y=360)

    def Next(self):
        """ 
        Function Name: Next
        Function Purpose: This function is executed once the user clicks on the "Next" button. Once the inputs 
        are validated, the inspection results loads the user selected data and is retained at the object class locations 
        before committing to the database. If all inputs are valid and confirmed by the user, the next stage of inspections is executed.
        """
        # First check if the input is empty, if so, notify the user the input needs attention 
        blnValidate = self.Validate_InputFields()
        
        # If status is true then proceed to update the result field, else, reset the fields
        if blnValidate is True:
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to next inspection page?', icon='question') is True:     
                # Load the user data and prep the data for db dump
                self.Pull_UserInput()     
                
                # Go to the next inspection page
                self.Next_Inspection()
            else:
                # Check if the user would like to reset the fields
                if messagebox.askyesno(message='ATTENTION! \n\n Would you like to reset the fields?', icon='question') is True:
                    # Clear the input fields and after data is submitted to the database
                    self.Reset()
                    
    def checkInput(self, drop_arg):
        """
        Function Name: checkInput
        Description: Check if the input field is not empty.
        """
        if drop_arg:
            return True
        messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.', icon='warning')
        return False

    def validate_InputFields(self):
        """
        Function Name: validate_InputFields
        Description: Validate all user inputs.
        """
        # Validate each field sequentially and focus on the first invalid field
        for field in [self.dropItemSelection, self.dropItemLocation, self.dropInUse]:
            if not self.checkInput(field.get()):
                field.focus()
                return False  # Stop at the first failure
        return True  # All fields are valid
    
    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        """   
        # Initialize the local variable
        strSerialNum = ""
        
        # Call the mapping method to get serial/bumper number cached list data based on itemType
        itemType = self.itemType
        serialNumCacheList, bumperNumCacheList = self.getCachedItems_FromItemType(itemType)
        
        # Get the selected values from the drop menus
        if self.dropItemSelection.get() in serialNumCacheList:
            strSerialNum = self.dropItemSelection.get()
            Bool_Flag.Set_SerialRadio_Bool_Value_True(Bool_Flag)
        else:
            intPrimID = bumperNumCacheList.index(self.dropItemSelection.get()) + 1
            strSerialNum = serialNumCacheList[intPrimID]
            Bool_Flag.Set_BumperRadio_Bool_Value_True(Bool_Flag)
            
        # Get the selected values from the drop menus    
        itemLocation = self.dropItemLocation.get()
        itemInUseStatus = self.dropInUse.get()

        # Update the Connectors class objects with the new selected values
        ItemType_SetSerial_InUse_Selection.update_ItemData(item_type=itemType, serial_num=strSerialNum, equip_in_use=itemInUseStatus)

        # Commit the data to load the WallLocation class objects with the data from the db
        WallLocation.strWallLocationDesc = itemLocation
        WallLocation.Get_WallLocation_Selection(WallLocation)
        
    def getCachedItems_FromItemType(self, itemType):
        """
        Function Name: getCachedItems_FromItemType
        Description: Method to return serial and bumper number cached lists items based on the item type.
        """
        # Initialize with default values in case the item type is not found in the data source
        serialNumList = []
        bumperNumList = []

        # Retrieve data from the ItemType_Serial_BumperNum_CacheMap based on itemType
        if itemType in ItemType_Serial_BumperNum_CacheMap.itemData:
            data = ItemType_Serial_BumperNum_CacheMap.itemData[itemType]
            # Assign values directly from the map
            serialNumList = data.get('serialNumCacheList', [])
            bumperNumList = data.get('bumperNumCacheList', [])

        return serialNumList, bumperNumList
    
    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This function is executed once the user clicks on the reset button inside the root
        frame. If the user clicks 'Reset', all data is set back to default.
        """     
        # Set the list objects first element to the drop click object
        self.dropItemSelection.set("")
        self.dropItemLocation.set("")
        self.dropInUse.set("")

        # Reset the radio button to its default value
        self.objRadioValue.set("serial")

        # Populate the dropdown based on default radio button selection
        self.Populate_Dropdown()

        # Re-Populate the dropdown menus 
        self.dropItemSelection["values"] = self.astrSerialNumList
        
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """   
        # Hide the current window
        self.Exit()  
         
                    
    def Add_Item(self):
        """ 
        Function Name: Add_Item
        Function Purpose: This function is executed once the user clicks on Add button and updates the drop down
        object list with the new values.
        """           

        # Update the drop-down menu values
        self.Update_Dropdown_Values()

    def Update_Item_Info(self):
        """ 
        Function Name: Update_Item_Info
        Function Purpose: This function is executed if the user clicks Update Item Information button. 
        """

        # Update the drop-down menu values
        self.Update_Dropdown_Values()
        
    def Add_Location(self):
        """ 
        Function Name: Add_Location
        Function Purpose: This function is executed once the user clicks on AddLocation button and updates the drop down
        object list with the new values.
        """           

        # Update the drop-down menu values
        self.Update_Dropdown_Values()        