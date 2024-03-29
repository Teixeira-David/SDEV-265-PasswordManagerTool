"""
.______    _______ .___________.    ___         .______   .______       _______     ___       __  ___ 
|   _  \  |   ____||           |   /   \        |   _  \  |   _  \     |   ____|   /   \     |  |/  / 
|  |_)  | |  |__   `---|  |----`  /  ^  \       |  |_)  | |  |_)  |    |  |__     /  ^  \    |  '  /  
|   _  <  |   __|      |  |      /  /_\  \      |   _  <  |      /     |   __|   /  /_\  \   |    <   
|  |_)  | |  |____     |  |     /  _____  \     |  |_)  | |  |\  \----.|  |____ /  _____  \  |  .  \  
|______/  |_______|    |__|    /__/     \__\    |______/  | _| `._____||_______/__/     \__\ |__|\__\                                                                                                       
"""
"""
Project Name: Auto Belay Inspection User Interface
Developer: David Teixeira
Date: 11/02/2023
Abstract: This project is vol 0.0.2 to store and retrieve data for PPE Inspections
"""

# Import Python Libraries
from tkinter import *
from tkinter import messagebox, ttk, Listbox
import tkinter as tk
from datetime import date, datetime, timedelta
import os
import sys
import subprocess
import platform
import getpass
import shutil
import sqlite3 
import configparser
import glob
# os.environ['TK_SILENCE_DEPRECATION'] = '1'

# Import project modules
from ObjectClass import AutoBelay, AutoBelayInspect
from ObjectClass import BrakeHousing, BrakePhysicalInspect, BrakeVisualInspect, StandardBrakeInspect, BrakeCompSelection
from ObjectClass import Carabiner, CarabinerFunctionInspect, CarabinerPhysicalInspect, CarabinerVisualInspect, StandardCarabinerInspect
from ObjectClass import CaseHousing, CasePhysicalInspect, CaseVisualInspect, StandardCaseInspect
from ObjectClass import CaseVisSelection, CasePhysSelection, CaseCompSelection
from ObjectClass import States, WallLocation, GymFacility, CarabinerFunction, AdminUsers
from ObjectClass import InspectionStatus, InspectionType, Metallic, Textile, Plastic, StandardInspect
from ObjectClass import Lanyard, LanyardFunctionInspect, LanyardPhysicalInspect, LanyardVisualInspect, StandardLanyardInspect
from ObjectClass import RetractorFunct, LoginName, UserLogins, Inspector, Reports
from ObjectClass import DeviceHandle, HandlePhysicalInspect, HandleVisualInspect, StandardHandelInspect
from ObjectClass import HandleVisSelection, HandlePhysSelection
from ObjectClass import CarabVisSelection, CarabPhysSelection, CarabFunctSelection, LanyardVisSelection
from ObjectClass import LanyardPhysSelection, RetractFunctSelection, Bool_Flag, BrakeVisSelection, BrakePhysSelection
from ObjectClass import Location, AutoBelayReserviceReport, Ropes, RopeVisSelection, RopeVisualInspect, RopePhysSelection, RopePhysicalInspect
from ObjectClass import StandardRopeInspect, RopeInspect, Connectors, ConnectorFunction, ConnectorVisSelection
from ObjectClass import ConnectorVisualInspect, ConnectorPhysSelection, ConnectorPhysicalInspect, ConnectorFunctSelection
from ObjectClass import ConnectorFunctionInspect, StandardConnectorInspect, ConnectorInspect, BelayDevices, BelayDeviceFunction
from ObjectClass import BelayDeviceVisSelection, BelayDeviceVisualInspect, BelayDevicePhysSelection, BelayDevicePhysicalInspect
from ObjectClass import BelayDeviceFunctSelection, BelayDeviceFunctionInspect, StandardBelayDeviceInspect, BelayDeviceInspect
from ObjectClass import BelayDevicePlasticVisSelection, BelayDevicePlasticPhysSelection, BelayDevicePlasticFunctSelection
from ObjectClass import CustomRopeSystem, ConnectorsRetiredReport, BelayDevicesRetiredReport, RopesRetiredReport
from BaseFunctionClass import BaseFunctions
from DatabaseScript import Database, Queries, Records
from SendEmail import Send_Email
# from RopesUI import Build_Rope_Sys_Setup


#######################################################################################################
# User Login Class
#######################################################################################################

class UserLogin_Main(tk.Tk, LoginName):
    """
    Class Name: UserLogin_Main
    Class Description: This class is the main start up page of the program where the user logs into the program.
    """
    def __init__(self):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """               
        # Create the root tkinter variable
        super().__init__()
        
        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight() 

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (600/2)     
        self.y = (self.heightSize/2) - (200/2)    
                
        # Create the Window attributes
        self.WindowTitle = self.title("User Login")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (600, 200, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Create the frame for the login credentials
        self.lblFrame = LabelFrame(self, width=590, height=590)
        self.lblFrame.place(x=5, y=5, width=590, height=190)
        
        # Create the Label attributes
        self.lblLoginLabel = Label(self.lblFrame, text="Username:")
        self.lblPasswordLabel = Label(self.lblFrame, text="Password:")
        self.lblLoginLabel.place(x=126, y=58)
        self.lblPasswordLabel.place(x=128, y=85)
        
        # Create the Login Credential attributes
        self.LoginNameEntry = StringVar()
        self.LoginPasswordEntry = StringVar()
        self.LoginNameEntry = Entry(self.lblFrame, width=35)
        self.LoginPasswordEntry =  Entry(self.lblFrame, width=35, show='*') 
        self.LoginNameEntry.place(x=220, y=55)
        self.LoginPasswordEntry.place(x=220, y=83)
        self.LoginNameEntry.focus()

        # Create the Button attributes
        self.btnExit = Button(self.lblFrame, text = "Exit", width=10,  command=lambda:UserLogin_Main.Exit(self))
        self.btnClearButton = Button(self.lblFrame, text = "Clear", width=10,  command=lambda:UserLogin_Main.ClearButton_Click(self))
        self.btnSubmitButton = Button(self.lblFrame, text = "Submit", width=10, command=lambda:UserLogin_Main.SubmitButton_Click(self))
        self.btnExit.place(x=160, y=120)
        self.btnClearButton.place(x=260, y=120)
        self.btnSubmitButton.place(x=360, y=120)

        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()           
        sys.exit() 
                                    
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                blnValidate = False
        except ValueError:
            messagebox.showwarning(message='ERROR \n\n Whoops! Something unexpected happened. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate

    def Validate_Credential_InputFields(self):
        """ 
        Function Name: Validate_Credential_InputFields
        Function Purpose: This function validates the user inputs.
        """
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)
        
        # Check the user input
        blnValidate = UserLogin_Main.Check_Input(self.LoginNameEntry.get())
        
        # Check if the input is valid
        if (blnValidate is True):
            # Validate the user inputs
            LogNameResultTup = LoginName.Check_Login_Name(self.LoginNameEntry.get())     

            # Check if the input is valid
            if (LogNameResultTup[0] is True):  
                self.strLoginName = LogNameResultTup[1]                 
                # Check the user input
                blnValidate = UserLogin_Main.Check_Input(self.LoginPasswordEntry.get())
            
                # Check if the input is valid
                if (blnValidate is True):
                    # Check the user input
                    LogPswrdResultTup = LoginName.Validate_Login_Password(self.LoginPasswordEntry.get())
                    
                    # Check if the input is valid
                    if (LogPswrdResultTup[0] is True):                                                                                                                                                         
                        blnValidate = True
                        self.strLoginPassword = LogPswrdResultTup[1]
                        return [blnValidate, LogNameResultTup, LogPswrdResultTup]       
                    else:
                        # Return blnValidate as False
                        blnValidate = False
                        messagebox.showwarning(message='ERROR \n\n The password was incorrect. \n Please try again.', icon='warning')   
                        self.LoginPasswordEntry.focus()
                        self.LoginPasswordEntry.delete(0, END)
                        self.LoginPasswordEntry.configure(background='Yellow')                   
                else:
                    # Return blnValidate as False
                    messagebox.showwarning(message='ERROR \n\n Password should not be empty. Please Try again.', icon='warning')
                    blnValidate = False
                    self.LoginPasswordEntry.focus()
                    self.LoginPasswordEntry.delete(0, END)
                    self.LoginPasswordEntry.configure(background='Yellow')                       
            else:
                # Return blnValidate as False
                messagebox.showwarning(message='ERROR \nUser name does not exist. Please Try again.', icon='warning')
                blnValidate = False  
                self.LoginNameEntry.focus()      
                self.LoginNameEntry.delete(0, END)
                self.LoginPasswordEntry.delete(0, END)
                self.LoginPasswordEntry.configure(background='Yellow')     
                self.LoginNameEntry.configure(background='Yellow')                       
        else:
            # Return blnValidate as False
            messagebox.showwarning(message='ERROR \n\n User name should not be empty. Please Try again.', icon='warning')
            blnValidate = False
            self.LoginNameEntry.focus()   
            self.LoginNameEntry.delete(0, END)
            self.LoginNameEntry.configure(background='Yellow')               
                
        return [blnValidate]

    # def ShowWarningMessage(self, message):
    #     """ 
    #     Function Name: ShowWarningMessage
    #     Function Purpose: This function is executed once the user clicks on AddUnit button and updates the drop down
    #     object list with the new values.
    #     """           
    #     # Build the child instance 
    #     msgBox = MessageBox(self)
    #     msgBox.Warning_Messagebox(message)
            
    def SubmitButton_Click(self):
        """ 
        Function Name: SubmitButton_Click
        Function Purpose: This function is executed once the user enters their user name and password
        """
        # Check if all of the inputs are valid
        global blnValidate 
        blnValidate = bool(False)

        # Clear out the background colors and set to default as 'white'        
        UserLogin_Main.Clear_BG_Color(self)
        
        # Get the blnValidate status
        aResultList = UserLogin_Main.Validate_Credential_InputFields(self)

        # Check if the input is valid
        if (aResultList[0] is True):
            # Validate that the elements in the list are equal
            if (self.strLoginPassword == aResultList[2][1]):
                # Assign the class attributes to the valid inputs
                l = LoginName(aResultList[1][2], aResultList[1][1], aResultList[2][1]) 
                
                # Get the InspectorID 
                Inspector.intInspectorID = l.intLoginID
                LoginName.intLoginID = l.intLoginID
                
                # Set the current user
                UserLogins.aintUserLoginID = []
                UserLogins.Get_UserLogin_Data(UserLogins)
                for i, value in enumerate(UserLogins.aintUserLoginID):
                    if l.intLoginID == value:      
                        UserLogins.Append_CurrentUserLoginList(UserLogins, value)
                        UserLogins.Append_CurrentUserLoginList(UserLogins, l.intLoginID)
                        UserLogins.Append_CurrentUserLoginList(UserLogins, self.strLoginName)
                
                # Delete the login name and login password to reset the text box
                LoginName.Delete_Login_Data(self)
                UserLogins.Delete_UserLogin_Data(UserLogins)
                
                # Destroy the window and proceed to the main menu
                self.destroy()               
                Start_Menu()    

    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the root
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Hide the current window
        self.deiconify()        
        
    def ClearButton_Click(self):
        """ 
        Function Name: ClearButton_Click
        Function Purpose: This function is executed if the user clicks clear. The fields should be deleted
        """
        # Delete the login name and login password to reset the text box
        self.LoginNameEntry.delete(0, END)
        self.LoginPasswordEntry.delete(0, END)
        
        # Clear out the background colors and set to default as 'white'
        UserLogin_Main.Clear_BG_Color(self)
        
        # Return focus to first input
        self.LoginNameEntry.focus()
            
    def Clear_BG_Color(self):
        """ 
        Function Name: Clear_BG_Color
        Function Purpose: This button executes when the user submits their entries and clears the background
        color before any validation checks.
        """
        # Delete the button after submission
        self.LoginNameEntry.configure(background='White')
        self.LoginPasswordEntry.configure(background='White')

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """       
        # Display the user ask question to see if the user would like to exit the program
        if messagebox.askyesno(message="EXIT APPLICATION \n\n Would you like to exit the program?", icon='question'):        
            self.destroy()   
            sys.exit()      
            

#######################################################################################################
# Start Menu Class
#######################################################################################################        

class Start_Menu(tk.Tk, Inspector):
    """
    Class Name: Start_Menu
    Class Description: This class is for the main menu after the user validates their login credentials. 
    """
    def __init__(self, ):
        # Load the data from the database
        Start_Menu.Load_Obj_Lists(self)
        
        # Create the root tkinter variable
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (560/2)     
        self.y = (self.heightSize/2) - (330/2)    
                        
        # Create the Window attributes
        self.WindowTitle = self.title("Main Menu")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (560, 330, self.x, self.y))
        self.WindowSize = self.resizable(False, False)
        
        # Create the frame for the buttons
        self.btnFrame = LabelFrame(self, text='Menu Selection')
        self.btnFrame.place(x=160, y=15, width=250, height=285)

        # Create the sql query string to check if the user who logged in is admin or not
        AdminUsers.Get_AdminUser_Data(AdminUsers)

        # Make sure to comment this out after testing 
        self.intInspectorID = 1
        
        # Check if the user is permitted to access the system admin interface
        if self.intInspectorID in AdminUsers.aintAdminInspectorID:
            # User is permitted to access the system admin interface
            # Create the Buttons
            self.btnAutoBelayMenu = Button(self.btnFrame, width=25, text = "Auto Belays", command=lambda:Start_Menu.Open_AutoBelay_Menu(self))        
            self.btnBelayDeviceMenu = Button(self.btnFrame, width=25, text = "Belay Devices", command=lambda:Start_Menu.Open_BelayDevice_Menu(self))
            self.btnConnectorsMenu = Button(self.btnFrame, width=25, text = "Connectors", command=lambda:Start_Menu.Open_ConnectorsMenu(self))
            self.btnRopesMenu = Button(self.btnFrame, width=25, text = "Ropes", command=lambda:Start_Menu.Open_RopesMenu(self))        
            self.btnAddNewUser = Button(self.btnFrame, width=25, text = "Add User", command=lambda:Start_Menu.Open_AddUser(self))
            self.btnEditUser = Button(self.btnFrame,  width=25, text="Edit User", command=lambda:Start_Menu.Open_EditUser(self))        
            self.btnOpenReport = Button(self.btnFrame, width=25, text = "Open Reports", command=lambda:Start_Menu.Open_Records_Dir(self))
            self.btnExit = Button(self.btnFrame, width=25, text = "Log Out", command=lambda:Start_Menu.Exit(self))
        else:
            # Create the Buttons
            self.btnAutoBelayMenu = Button(self.btnFrame, width=25, text = "Auto Belays", command=lambda:Start_Menu.Open_AutoBelay_Menu(self))        
            self.btnBelayDeviceMenu = Button(self.btnFrame, width=25, text = "Belay Devices", command=lambda:Start_Menu.Open_BelayDevice_Menu(self), state='disabled')      
            self.btnConnectorsMenu = Button(self.btnFrame, width=25, text = "Connectors", command=lambda:Start_Menu.Open_ConnectorsMenu(self), state='disabled')
            self.btnRopesMenu = Button(self.btnFrame, width=25, text = "Ropes", command=lambda:Start_Menu.Open_RopesMenu(self), state='disabled')   
            self.btnAddNewUser = Button(self.btnFrame, width=25, text = "Add User", command=lambda:Start_Menu.Open_AddUser(self), state='disabled')
            self.btnEditUser = Button(self.btnFrame,  width=25, text="Edit User", command=lambda:Start_Menu.Open_EditUser(self), state='disabled')        
            self.btnOpenReport = Button(self.btnFrame, width=25, text = "Open Reports", command=lambda:Start_Menu.Open_Records_Dir(self))
            self.btnExit = Button(self.btnFrame, width=25, text = "Log Out", command=lambda:Start_Menu.Exit(self))
        
        # Destroy the admin user array list
        AdminUsers.Delete_Admin_Data(AdminUsers)

        # Create the button grid
        self.btnAutoBelayMenu.grid(row=0, column=1, padx=29, pady=3)
        self.btnBelayDeviceMenu.grid(row=1, column=1, pady=3)
        self.btnConnectorsMenu.grid(row=2, column=1, pady=3)
        self.btnRopesMenu.grid(row=3, column=1, pady=3)
        self.btnAddNewUser.grid(row=4, column=1, pady=3)
        self.btnEditUser.grid(row=5, column=1, pady=3)
        self.btnOpenReport.grid(row=6, column=1, pady=3)
        self.btnExit.grid(row=7, column=1, pady=3)
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()  
        
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)   
        
        # Create the back database file and check to send out failed email notification
        # Send_Email.HH_Fail_SendEmail() 
        # Send_Email.HH_Updated_Unit_Reserviced_SendEmail()
        Database.dbBackup_Volume(Database.db_path)            
        UserLogin_Main()
        
    def Open_AutoBelay_Menu(self):
        """ 
        Function Name: Open_AutoBelay_Menu
        Function Purpose: This function is executed if the user clicks Auto Belays button.
        """
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)
        
        # Set the stored lists
        Start_Menu.Delete_Obj_Lists(self) 
    
        # Delete the root window
        self.destroy()
        
        # Open the Auto Belays Menu Window
        AutoBelay_Menu()

    def Open_BelayDevice_Menu(self):
        """ 
        Function Name: Open_BelayDevice_Menu
        Function Purpose: This function is executed if the user clicks Belay Devices button.
        """
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)
        
        # Set the stored lists
        Start_Menu.Delete_Obj_Lists(self) 
    
        # Delete the root window
        self.destroy()
        
        # Open the Belay Devices Menu Window
        BelayDevices_Menu()

    def Open_ConnectorsMenu(self):
        """ 
        Function Name: Open_ConnectorsMenu
        Function Purpose: This function is executed if the user clicks Connectors Menu button.
        """
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)
        
        # Set the stored lists
        Start_Menu.Delete_Obj_Lists(self) 
    
        # Delete the root window
        self.destroy()
        
        # Open the Connectors Menu Window
        Connectors_Menu()
                
    def Open_RopesMenu(self):
        """ 
        Function Name: Open_RopesMenu
        Function Purpose: This function is executed if the user clicks Ropes Menu button.
        """
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)
        
        # Set the stored lists
        Start_Menu.Delete_Obj_Lists(self) 
    
        # Delete the root window
        self.destroy()
        
        # Open the Ropes Menu Window
        Ropes_Menu()
        
    def Open_AddUser(self):
        """ 
        Function Name: Open_AddUser
        Function Purpose: This function is executed if the user clicks add new user button. 
        """
        # Delete the root window
        self.destroy()
        
        # Open the Add Inspector Window
        AddInspector()        

    def Open_EditUser(self):
        """ 
        Function Name: Open_EditUser
        Function Purpose: This function is executed if the user clicks Edit User button. This functions allows
        the user to specify the which credentials need to be edited.
        """
        # Delete the root window
        self.destroy()
        
        # Open the Send Reports window
        EditUser()

    def Open_Records_Dir(self):
        """ 
        Function Name: Open_Records_Dir
        Function Purpose: This function is executed if the user clicks Open Report Information button. 
        """
        # Open the send reports window
        Records.Open_Records_Dir()   
        
    def Load_Obj_Lists(self):
        """ 
        Function Name: Load_Obj_Lists
        Function Purpose: This function is executed once the start menu page is loaded. Either upon first log in or 
        after the user exits a sub window executed from the start menu.
        """
        # Set the database attributes    
        AutoBelay.Get_AutoBelay_Data(AutoBelay)
        BrakeHousing.Get_BrakeHousing_Data(BrakeHousing)
        States.Get_State_Data(States)
        WallLocation.Get_WallLocation_Data(WallLocation)
        Location.Get_Location_Data(Location)
        GymFacility.Get_Gym_Data(GymFacility)
        Carabiner.Get_Carabiner_Data(Carabiner)
        CarabinerFunction.Get_CarabinerFunct_Data(CarabinerFunction)
        CaseHousing.Get_CaseHousing_Data(CaseHousing)
        InspectionStatus.Get_InspectionStatus_Data(InspectionStatus)
        InspectionType.Get_InspectionType_Data(InspectionType)
        Metallic.Get_MetallicInspectionType_Data(Metallic)
        Textile.Get_TextileInspectionType_Data(Textile)
        Plastic.Get_PlasticInspectionType_Data(Plastic)
        DeviceHandle.Get_Handel_Data(DeviceHandle)
        Lanyard.Get_Lanyard_Data(Lanyard)
        RetractorFunct.Get_RetractFunct_Data(RetractorFunct)
        Ropes.Get_Ropes_Data(Ropes)
        CustomRopeSystem.Get_CustomRopeSystem_Data(CustomRopeSystem)
        Connectors.Get_Connectors_Data(Connectors)
        BelayDevices.Get_BelayDevices_Data(BelayDevices)
            
    def Delete_Obj_Lists(self):
        """ 
        Function Name: Delete_Obj_Lists
        Function Purpose: This function is executed if the user clicks submit button. The list objects in each 
        class will be deleted to be reupdated by the call to the db if there is any new inspections or added data
        to the db
        """
        AutoBelay.Delete_AutoBelay_Data(AutoBelay)
        BrakeHousing.Delete_BrakeHousing_Data(BrakeHousing)
        States.Delete_State_Data(States)
        WallLocation.Delete_WallLocation_Data(WallLocation)
        Location.Delete_Location_Data(Location)
        GymFacility.Delete_Facility_Data(GymFacility)
        Carabiner.Delete_Carabiner_Data(Carabiner)
        CarabinerFunction.Delete_CarabinerFunct_Data(CarabinerFunction)
        CaseHousing.Delete_Case_Data(CaseHousing)
        InspectionStatus.Delete_InspectionStatus_Data(InspectionStatus)
        InspectionType.Delete_InspectionStatus_Data(InspectionType)
        Metallic.Delete_MetallicInspection_Data(Metallic)
        Textile.Delete_TextileInspection_Data(Textile)
        Plastic.Delete_PlasticInspection_Data(Plastic)
        DeviceHandle.Delete_Handle_Data(DeviceHandle)
        Lanyard.Delete_Lanyard_Data(Lanyard)
        RetractorFunct.Delete_RetractFunct_Data(RetractorFunct)
        Inspector.Delete_Inspector_Data(Inspector)
        LoginName.Delete_Login_Data(LoginName)
        UserLogins.Delete_UserLogin_Data(UserLogins)
        AdminUsers.Delete_Admin_Data(AdminUsers)
        Ropes.Delete_Ropes_Data(Ropes)
        CustomRopeSystem.Delete_CustomRopeSystem_Data(CustomRopeSystem)
        StandardRopeInspect.Delete_Rope_Data(StandardRopeInspect)
        Connectors.Delete_Connectors_Data(Connectors)
        StandardConnectorInspect.Delete_Connector_Data(StandardConnectorInspect)
        BelayDevices.Delete_BelayDevices_Data(BelayDevices)
        StandardBelayDeviceInspect.Delete_BelayDevice_Data(StandardBelayDeviceInspect)
        
    def Set_Default_Bool_Values(self):
        """ 
        Function Name: Set_Default_Bool_Values
        Function Purpose: This function is at the start of the program to set the bool persist values to False
        """
        # Set the bool class object value back to false before opening the window
        Bool_Flag.Set_AutoBelay_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_Handle_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_Case_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_Brake_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_Lanyard_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_Carab_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_OutForService_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_SerialRadio_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_BumperRadio_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_RopeSystem_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_Rope_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_Connector_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_BelayDevice_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_ComplexWithConnector_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_ComplexWithBelayDevice_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_ComplexWithTwo_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_SimpleRope_Bool_Value_False(Bool_Flag)

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed if the user clicks exit button. The main menu will
        exit once this button is clicked and will return the user to the login page.
        """
        # Delete the root window
        self.destroy()
        
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)  
        
        # Create the back database file and check to send out failed email notification
        # Send_Email.HH_Fail_SendEmail() 
        # Send_Email.HH_Updated_Unit_Reserviced_SendEmail()
        Database.dbBackup_Volume(Database.db_path)            
        UserLogin_Main()

#######################################################################################################
# AutoBelay Menu Class
#######################################################################################################        

class AutoBelay_Menu(tk.Tk):
    """
    Class Name: AutoBelay_Menu
    Class Description: This class is for the auto belay main menu. 
    """
    def __init__(self, ):
        # Load the data from the database
        Start_Menu.Load_Obj_Lists(self)
        
        # Create the root tkinter variable
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (560/2)     
        self.y = (self.heightSize/2) - (390/2)    
                        
        # Create the Window attributes
        self.WindowTitle = self.title("Auto Belay Menu")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (560, 390, self.x, self.y))
        self.WindowSize = self.resizable(False, False)
        
        # Create the frame for the buttons
        self.btnFrame = LabelFrame(self, text='Menu Selection')
        self.btnFrame.place(x=160, y=15, width=250, height=345)

        # Create the Buttons
        self.btnNewInspect = Button(self.btnFrame, width=25, text = "New Inspection", command=lambda:AutoBelay_Menu.Open_NewInspection(self))        
        self.btnViewFutureInspectDate = Button(self.btnFrame, width=25, text = "View Future Inspection Dates", command=lambda:AutoBelay_Menu.Open_ViewLastNext_InspectionDates(self))
        self.btnViewFutureServiceDate = Button(self.btnFrame, width=25, text = "View Future Service Dates", command=lambda:AutoBelay_Menu.Open_ViewService_InspectionDates(self))
        self.btnViewUnitDates = Button(self.btnFrame, width=25, text = "View Unit Dates", command=lambda:AutoBelay_Menu.Open_AutoBelayDates(self))
        self.btnViewUnitInfo = Button(self.btnFrame, width=25, text = "View Unit Info", command=lambda:AutoBelay_Menu.Open_AutoBelayInfo(self))
        self.btnViewWallLocation = Button(self.btnFrame, width=25, text = "View Unit Wall Locations", command=lambda:AutoBelay_Menu.Open_AutoBelay_WallLocations(self))
        self.btnViewOutForReservice = Button(self.btnFrame, width=25, text = "View Units Out For Reservice", command=lambda:AutoBelay_Menu.Open_AutoBelay_OutForReservice(self))
        self.btnDownloadReport = Button(self.btnFrame, width=25, text = "Download Reports", command=lambda:AutoBelay_Menu.Open_DownloadReports(self))
        self.btnOpenReport = Button(self.btnFrame, width=25, text = "Open Reports", command=lambda:AutoBelay_Menu.Open_Records_Dir(self))
        self.btnExit = Button(self.btnFrame, width=25, text = "Home", command=lambda:AutoBelay_Menu.Exit(self))

        # Create the button grid
        self.btnNewInspect.grid(row=0, column=1, padx=29, pady=3)
        self.btnViewFutureInspectDate.grid(row=2, column=1, pady=3)
        self.btnViewFutureServiceDate.grid(row=3, column=1, pady=3)
        self.btnViewUnitDates.grid(row=4, column=1, pady=3)
        self.btnViewUnitInfo.grid(row=5, column=1, pady=3)
        self.btnViewWallLocation.grid(row=6, column=1, pady=3)
        self.btnViewOutForReservice.grid(row=7, column=1, pady=3)
        self.btnDownloadReport.grid(row=8, column=1, pady=3)
        self.btnOpenReport.grid(row=9, column=1, pady=3)
        self.btnExit.grid(row=10, column=1, pady=3)
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()  
        
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)   
        
        # Send the user back to the main menu        
        Start_Menu()
        
    def Open_NewInspection(self):
        """ 
        Function Name: Open_NewInspection
        Function Purpose: This function is executed if the user clicks new inspection button. The 
        call is to the inspection class and will execute and add a new inspection to the database.
        """
        # Delete the root window
        self.destroy()
        
        # Open the New Inspection Window
        AutoBelaySelection()

    def Open_ViewLastNext_InspectionDates(self):
        """ 
        Function Name: Open_ViewLastNext_InspectionDates
        Function Purpose: This function is executed if the user clicks view AutoBelay Next/Last inspection dates button. 
        """
        # Delete the root window
        self.destroy()
        
        # Determine the Caller_ID based on the class
        Caller_ID = "AutoBelay"
        
        # Open the add new location window
        View_LastNext_InspectDate(Class_CallerID=Caller_ID)

    def Open_ViewService_InspectionDates(self):
        """ 
        Function Name: Open_ViewService_InspectionDates
        Function Purpose: This function is executed if the user clicks view AutoBelay Service/Reservice inspection dates button. 
        """
        # Delete the root window
        self.destroy()
        
        # Open the add new location window
        View_Service_InspectDate()
        
    def Open_AutoBelayDates(self):
        """ 
        Function Name: Open_AutoBelayDates
        Function Purpose: This function is executed if the user clicks View AutoBelay Dates button. 
        """
        # Delete the root window
        self.destroy()
        
        # Open the add new location window
        View_AutoBelayDates()

    def Open_AutoBelayInfo(self):
        """ 
        Function Name: Open_AutoBelayInfo
        Function Purpose: This function is executed if the user clicks View AutoBelay Info button. 
        """
        # Delete the root window
        self.destroy()
        
        # Open the add new location window
        View_AutoBelay_Info()
        
    def Open_AutoBelay_WallLocations(self):
        """ 
        Function Name: Open_AutoBelay_WallLocations
        Function Purpose: This function is executed if the user clicks View AutoBelay Locations button. 
        """
        # Delete the root window
        self.destroy()
        
        # Determine the Caller_ID based on the class
        Caller_ID = "AutoBelay"
        
        # Open the view location window
        View_Item_WallLocations(Class_CallerID=Caller_ID)  

    def Open_AutoBelay_OutForReservice(self):
        """ 
        Function Name: Open_AutoBelay_OutForReservice
        Function Purpose: This function is executed if the user clicks View AutoBelay Out For Reservice button. 
        """
        # Delete the root window
        self.destroy()
        
        # Open the view location window
        View_OutForReservice() 
        
    def Open_Records_Dir(self):
        """ 
        Function Name: Open_Records_Dir
        Function Purpose: This function is executed if the user clicks Open Report Information button. 
        """
        # Open the send reports window
        Records.Open_Records_Dir()   
        
    def Open_DownloadReports(self):
        """ 
        Function Name: Open_DownloadReports
        Function Purpose: This function executes whenever the user clicks the 'Download Reports' button. This function
        pulls from the db specific views and downloads the views to a desired directory. Each file is saved as an excel
        file. 
        """
        Queries.Download_Files(Queries, user_triggered=True)       
        messagebox.showwarning(message='SUCCESSFUL DOWNLOAD \n\n All files have been downloaded to the Records Directory.', icon='warning')

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed if the user clicks exit button. The main menu will
        exit once this button is clicked and will return the user to the login page.
        """
        # Delete the root window
        self.destroy()
        
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)  
        
        # Send the user back to the main menu   
        Start_Menu()


#######################################################################################################
# Auto Belay Selection Class
#######################################################################################################   

class AutoBelaySelection(tk.Tk, AutoBelay):
    """
    Class Name: AutoBelaySelection
    Class Description: This class is to conduct Auto Belay Selection.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new Auto Belay Selection. User must click
        'Next' Button in order to progress to the next inspection type.
        """
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (650/2)     
        self.y = (self.heightSize/2) - (410/2)          
        
        # Create the Window attributes                
        self.title("Auto Belay Selection")
        self.geometry('%dx%d+%d+%d' % (650, 410, self.x, self.y))
        self.resizable(False, False)

        # Load the query selection widget
        self.Selection_Widget()
        
        # Create the frame fields
        self.typeFrame = tk.LabelFrame(self, text="Additional Info")
        self.typeFrame.place(x=100, y=140, width=450, height=200)
                
        # Create the label for the checkboxes
        self.lblUnitLocation = tk.Label(self.typeFrame, text="Unit Location:")
        self.lblInUse = tk.Label(self.typeFrame, text="Device In Use:")
        self.lblQuestion = tk.Label(self.typeFrame, text="Can't find what you're looking for?")
                        
        # Create the label locations
        self.lblUnitLocation.place(x=70, y=15)
        self.lblInUse.place(x=70, y=55)
        self.lblQuestion.place(x=125, y=95)

        # Create the drop down menu list for each attribute
        self.dropUnitLocation = ttk.Combobox(self.typeFrame, values=WallLocation.astrWallLocationDesc, state='readonly')
        self.dropInUse = ttk.Combobox(self.typeFrame, values=['Yes', 'No'], state='readonly')
        
        # Create the drop down menu size for each attribute
        self.dropUnitLocation.configure(width=25)
        self.dropInUse.configure(width=25)
        
        # Create the grid for the drop down menu list objects
        self.dropUnitLocation.place(x=190, y=15)  
        self.dropInUse.place(x=190, y=55)  

        # Check if the cache values for any drop menus have been previously selected and set the values
        if Bool_Flag.blnAutoBelayPersistFlag == True:
            if (Bool_Flag.blnSerialNumRadioSelect == True):
                self.Set_Previous_Drop_List(AutoBelay.strSerialNum, self.dropUnitSelection)
            else:
                self.objRadioValue.set("bumper")
                self.dropUnitSelection["values"] = self.astrBumperNumList
                self.Set_Previous_Drop_List(AutoBelay.strBumperNum, self.dropUnitSelection)
            self.Set_Previous_Drop_List(AutoBelay.blnDeviceInUse, self.dropInUse)
            self.Set_Previous_Drop_List(WallLocation.strWallLocationDesc, self.dropUnitLocation)
            
        # Create the buttons
        self.btnUpdateUnitInfo = Button(self.typeFrame, width=12, text = "Update Unit Info", command=self.Update_AutoBelay_Info)
        self.btnAddUnit = Button(self.typeFrame, width=12, text="Add Unit", command=self.Add_Unit)
        self.btnAddLocation = Button(self.typeFrame, width=12, text = "Add Location", command=self.Add_Location)
        self.btnExit = Button(self, width=10, text="Back", command=self.Back)
        self.btnReset = Button(self, width=10, text="Reset",command=self.Reset)
        self.btnNext = Button(self, width=10, text="Next", command=self.Next)
            
        # Create the position of the button
        self.btnUpdateUnitInfo.place(x=40, y=140)
        self.btnAddUnit.place(x=175, y=140) 
        self.btnAddLocation.place(x=310, y=140)
        self.btnExit.place(x=170, y=360) 
        self.btnNext.place(x=400, y=360) 
        self.btnReset.place(x=285, y=360)
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()

        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)
        AutoBelay_Menu()         

    def Selection_Widget(self):
        """ 
        Function Name: Selection_Widget
        Function Purpose: This function populates the search by widget for Serial or Bumper Num search.
        """           
        # Create the first frame to hold the input fields
        self.selectInput = LabelFrame(self, text="Select Unit")
        self.selectInput.place(x=100, y=35, width=450, height=100)

        # Create the labels 
        self.lblSearchByUnitID = Label(self.selectInput, text="Query by Unit ID:")
        self.lblUnitSelection = Label(self.selectInput, text="Unit ID Selection:")

        # Create the label locations
        self.lblSearchByUnitID.place(x=55, y=5)
        self.lblUnitSelection.place(x=55, y=40)

        # Create variables to hold the value of the selected radio button
        self.objRadioValue = tk.StringVar(value='serial')
        self.objComboValue = tk.StringVar()

        # List objects of serial and bumper values
        self.astrSerialNumList = self.astrSerialNum
        self.astrBumperNumList = self.astrBumperNum

        # Create the radio buttons
        self.rbSerial = tk.Radiobutton(self.selectInput, text="Serial Number", variable=self.objRadioValue, value="serial", command=self.Populate_Dropdown)
        self.rbBumper = tk.Radiobutton(self.selectInput, text="Bumper Number", variable=self.objRadioValue, value="bumper", command=self.Populate_Dropdown)

        # Place the radio buttons next to each other using .place()
        self.rbSerial.place(x=190, y=5)
        self.rbBumper.place(x=300, y=5)
                    
        # Create the entry input box
        self.dropUnitSelection = ttk.Combobox(self.selectInput, values=self.astrSerialNumList, state='readonly')
        self.dropUnitSelection.configure(width=25,)

        # Populate the dropdown based on the default radio button selection
        self.Populate_Dropdown()

        # Create the grid for all of the entry input fields
        self.dropUnitSelection.place(x=190, y=40) 

    def Populate_Dropdown(self):
        """ 
        Function Name: Populate_Dropdown
        Function Purpose: This function populates the dropdown based on the radio button selection.
        """           
        if self.objRadioValue.get() == "serial":
            self.dropUnitSelection["values"] = self.astrSerialNumList
        else:
            self.dropUnitSelection["values"] = self.astrBumperNumList
        self.dropUnitSelection.set("")  # Clear the combobox's current value                                    
        
    def Change_Date_To_Format(dtmObject, aResultTup):
        """ 
        Function Name: Change_Date_To_Format
        Function Purpose: This function is executed every call of the validation check to ensure the dates are all
        changed to the same format no matter if the character is valid.
        """ 
        dtmObject.delete(0, END)
        dtmObject.insert(0, aResultTup[1])
        dtmObject = aResultTup[1]

        return dtmObject

    def Convert_Date_Format(date_str):
        """ 
        Function Name: SubmitSelect
        Function Purpose: This button Convert date from "YYYY-MM-DD" to "MM/DD/YYYY"
        """
        year, month, day = date_str.split('-')
        return f"{month}/{day}/{year}"
        
    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)
        
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.', icon='warning')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate
    
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)  

        # Check the user input
        blnValidate = AutoBelaySelection.Check_Input(self.dropUnitSelection.get())

        # Check if the input is valid
        if (blnValidate is True):
            # Check the user input
            blnValidate = AutoBelaySelection.Check_Input(self.dropUnitLocation.get())         
            
            # Check if the input is valid
            if (blnValidate is True):
                # Check the user input
                blnValidate = AutoBelaySelection.Check_Input(self.dropInUse.get())         
                
                # Check if the input is valid
                if (blnValidate is True):
                    blnValidate = True
                else:
                    # Return blnValidate as False
                    blnValidate = False
                    self.dropInUse.focus()
            else:
                # Return blnValidate as False
                blnValidate = False
                self.dropUnitLocation.focus()                                                
        else:
            # Return blnValidate as False
            blnValidate = False
            self.dropUnitSelection.focus()

        return blnValidate            

    def Next_Inspection(self):
        """ 
        Function Name: Next_Inspection
        Function Purpose: This function is executed once the user clicks on Next button to move to the nex inspection
        type window. Withdraw the parent window and load the new window.
        """           
        # Hide the main window
        self.Exit()  

        # Open the new window
        CarabinerInspection()

    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the root
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Hide the current window
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """     
        # Hide the current window
        self.Exit()  
        
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)

        # Show the main window after the new window is closed
        AutoBelay_Menu()

    def Update_Dropdown_Values(self):
        """ 
        Function Name: Update_Dropdown_Values
        Function Purpose: This function is executed once the user clicks on AddUnit or AddLocation button and updates the drop down
        object list with the new values.
        """             
        # Ensure the dropdowns are Comboboxes and clear their current selections
        if isinstance(self.dropUnitSelection, ttk.Combobox):
            self.dropUnitSelection.set("") 
        if isinstance(self.dropUnitLocation, ttk.Combobox):
            self.dropUnitLocation.set("")

        # Update the values for connector selection dropdown
        self.astrSerialNumList = AutoBelay.astrSerialNum
        self.astrBumperNumList = AutoBelay.astrBumperNum
        if isinstance(self.dropUnitSelection, ttk.Combobox):
            self.dropUnitSelection['values'] = self.astrSerialNumList

        # Update the values for connector location dropdown
        if isinstance(self.dropUnitLocation, ttk.Combobox):
            self.dropUnitLocation['values'] = WallLocation.astrWallLocationDesc
            
        # # Populate the dropdown menus
        # self.dropUnitSelection.set("") 
        # self.astrSerialNumList = AutoBelay.astrSerialNum
        # self.astrBumperNumList = AutoBelay.astrBumperNum
        # #self.dropUnitSelection['values'] = self.astrSerialNumList
        # self.dropUnitLocation['values'] = WallLocation.astrWallLocationDesc

    def Add_Unit(self):
        """ 
        Function Name: Add_Unit
        Function Purpose: This function is executed once the user clicks on AddUnit button and updates the drop down
        object list with the new values.
        """           
        # Hide the main window
        self.Withdraw()  

        # Call your AddUnit function here
        newWindow = AddUnit(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Show the main window after the new window is closed
        self.Deiconify()  

        # Update the drop-down menu values
        self.Update_Dropdown_Values()

    def Update_AutoBelay_Info(self):
        """ 
        Function Name: Update_AutoBelay_Info
        Function Purpose: This function is executed if the user clicks Update AutoBelay Information button. 
        """
        # Hide the main window
        self.Withdraw()  

        # Call your AddUnit function here
        newWindow = UpdateUnitInfo(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Show the main window after the new window is closed
        self.Deiconify()  

        # Update the drop-down menu values
        self.Update_Dropdown_Values()
        
    def Add_Location(self):
        """ 
        Function Name: Add_Location
        Function Purpose: This function is executed once the user clicks on AddLocation button and updates the drop down
        object list with the new values.
        """           
        # Hide the main window
        self.Withdraw()  

        # Call your AddLocation function here
        newWindow = AddLocation(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Show the main window after the new window is closed
        self.Deiconify()  

        # Update the drop-down menu values
        self.Update_Dropdown_Values()

    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        """   
        # Get the selected values from the drop menus
        if self.dropUnitSelection.get() in AutoBelay.astrSerialNum:
            SerialNum = self.dropUnitSelection.get()
            Bool_Flag.Set_SerialRadio_Bool_Value_True(Bool_Flag)
        else:
            intPrimID = AutoBelay.astrBumperNum.index(self.dropUnitSelection.get()) + 1
            SerialNum = AutoBelay.astrSerialNum[intPrimID]
            Bool_Flag.Set_BumperRadio_Bool_Value_True(Bool_Flag)
            
        UnitLocation = self.dropUnitLocation.get()
        InUseStatus = self.dropInUse.get()

        # Commit the data to load the AutoBelay class objects with the data from the db
        AutoBelay.strSerialNum = SerialNum
        AutoBelay.blnDeviceInUse = InUseStatus
        AutoBelay.Set_AutoBelay_Selection(AutoBelay)

        # Commit the data to load the WallLocation class objects with the data from the db
        WallLocation.strWallLocationDesc = UnitLocation
        WallLocation.Get_WallLocation_Selection(WallLocation)

    def Next(self):
        """ 
        Function Name: Next
        Function Purpose: This function is executed once the user clicks on the "Next" button. Once the inputs 
        are validated, the inspection results loads the user selected data and is retained at the object class locations 
        before committing to the database. If all inputs are valid and confirmed by the user, the next stage of inspections is executed.
        """
        global blnValidate
        blnValidate = bool(False)             
        
        # First check if the input is empty, if so, notify the user the input needs attention 
        blnValidate = self.Validate_InputFields()
        
        # If status is true then proceed to update the result field, else, reset the fields
        if blnValidate is True:
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to next inspection component?', icon='question') is True:     
                # Load the user data and prep the data for db dump
                self.Pull_UserInput()     

                # Go to the next inspection component
                self.Next_Inspection()
            else:
                # Check if the user would like to reset the fields
                if messagebox.askyesno(message='ATTENTION! \n\n Would you like to reset the fields?', icon='question') is True:
                    # Clear the input fields and after data is submitted to the database
                    self.Reset()                

    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This function is executed once the user clicks on the reset button inside the root
        frame. If the user clicks 'Reset', all data is set back to default.
        """     
        # Set the list objects first element to the drop click object
        self.dropUnitSelection.set("")
        self.dropUnitLocation.set("")
        self.dropInUse.set("")

        # Reset the radio button to its default value
        self.objRadioValue.set("serial")

        # Populate the dropdown based on default radio button selection
        self.Populate_Dropdown()

        # Re-Populate the dropdown menus 
        self.dropUnitSelection["values"] = self.astrSerialNumList
        
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        

# #######################################################################################################
# # Add New Unit Class
# ####################################################################################################### 

class AddUnit(tk.Toplevel, AutoBelay):
    """
    Class Name: AddUnit
    Class Description: This class adds a unit to the database.
    """
    def __init__(self, parent):
        # Initialize the Toplevel window
        super().__init__(parent)

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (580/2)     
        self.y = (self.heightSize/2) - (340/2)    
                                        
        # Create the Window attributes
        self.title("Add New AutoBelay")
        self.geometry('%dx%d+%d+%d' % (580, 340, self.x, self.y))
        self.resizable(False, False)

        # Create the second frame to hold the input fields
        self.frameInput = tk.LabelFrame(self, text="Unit Credentials")
        self.frameInput.place(x=90, y=10, width=405, height=260)

        # Create the labels 
        self.lblDeviceName = tk.Label(self.frameInput, text="Manufacture Name:")
        self.lblSerialNum = tk.Label(self.frameInput, text="Serial Number:")
        self.lblBumperNum = tk.Label(self.frameInput, text="Bumper Number:")
        self.lblManuDate = tk.Label(self.frameInput, text="Manufacture Date:")
        self.lblServiceDate = tk.Label(self.frameInput, text="Service Date:")
        self.lblReserviceDate = tk.Label(self.frameInput, text="Re-service Date:")
        self.lblInstallDate = tk.Label(self.frameInput, text="Install Date:")
        self.lblDeviceInUse = tk.Label(self.frameInput, text="Device In Use:")

        # Create the label locations
        self.lblDeviceName.grid(row=0, column=0, sticky='W', padx=5)
        self.lblSerialNum.grid(row=1, column=0, sticky='W', padx=5)
        self.lblBumperNum.grid(row=2, column=0, sticky='W', padx=5)
        self.lblManuDate.grid(row=3, column=0, sticky='W', padx=5)
        self.lblServiceDate.grid(row=4, column=0, sticky='W', padx=5)
        self.lblReserviceDate.grid(row=5, column=0, sticky='W', padx=5)
        self.lblInstallDate.grid(row=6, column=0, sticky='W', padx=5)
        self.lblDeviceInUse.grid(row=7, column=0, sticky='W', padx=5)

        # Create the entry input box
        self.DeviceNameInput = Entry(self.frameInput, width=40)
        self.SerialNumInput = Entry(self.frameInput, width=40)
        self.BumperNumInput = Entry(self.frameInput, width=40)
        self.ManuDateInput = Entry(self.frameInput, width=40)
        self.ServiceDateInput = Entry(self.frameInput, width=40)
        self.ReserviceDateInput = Entry(self.frameInput, width=40, state='readonly')
        self.InstallDateInput = Entry(self.frameInput, width=40)

        # Create the drop down menu list objects
        self.dropInUse = ttk.Combobox(self.frameInput, values=['Yes', 'No'], state='readonly')

        # Create the drop down menu size for each attribute
        self.dropInUse.configure(width=37)
        
        # Create the grid for the drop down menu
        self.dropInUse.grid(row=7, column=1, padx=5, pady=5)

        # Create a list of all the entry objects
        aEntryList = (self.ManuDateInput, self.ServiceDateInput, self.InstallDateInput, self.BumperNumInput) 
        astrPlaceHolder = ("MM/DD/YYYY", "MM/DD/YYYY", "MM/DD/YYYY", "Optional")

        # Insert the placeholders at the desired entry points
        for i, entry in enumerate(aEntryList):
            entry.insert(0, astrPlaceHolder[i])
            entry.config(fg='grey')
            entry.bind('<FocusIn>', lambda event, entry=entry, placeholder=astrPlaceHolder[i]: self.On_Entry_Click(event, entry, placeholder))
            entry.bind('<FocusOut>', lambda event, entry=entry, placeholder=astrPlaceHolder[i]: self.On_FocusOut(event, entry, placeholder))
            
        # Create the grid for all of the entry input fields
        self.DeviceNameInput.grid(row=0, column=1, padx=25, pady=5)
        self.SerialNumInput.grid(row=1, column=1, pady=5)
        self.BumperNumInput.grid(row=2, column=1, pady=5)
        self.ManuDateInput.grid(row=3, column=1, pady=5)
        self.ServiceDateInput.grid(row=4, column=1, pady=5)
        self.ReserviceDateInput.grid(row=5, column=1, pady=5)
        self.InstallDateInput.grid(row=6, column=1, pady=5)

        # Create the buttons
        self.btnExit = Button(self, text="Back", width=10, command=lambda:AddUnit.Exit(self))
        self.btnReset = Button(self, text="Reset", width=10, command=lambda:AddUnit.Reset(self))
        self.btnSubmit = Button(self, text="Submit", width=10, command=lambda:AddUnit.Submit(self))

        # Create the button grid
        self.btnExit.place(x=120, y=290)
        self.btnReset.place(x=250, y=290)
        self.btnSubmit.place(x=380, y=290)

    def On_Entry_Click(self, event, entry, strPlaceHolder):
        """ 
        Function Name: On_Entry_Click
        Function Purpose: This function gets called whenever entry is clicked by a user to start a new entry.
        """    
        if entry.get() == strPlaceHolder:
            entry.delete(0, "end") 
            entry.insert(0, '') 
            entry.config(fg='black')
            
    def On_FocusOut(self, event, entry, strPlaceHolder):
        """ 
        Function Name: On_FocusOut
        Function Purpose: This function gets called whenever the entry loses focus.
        """            
        if entry.get() == '':
            entry.insert(0, strPlaceHolder)
            entry.config(fg='grey') 
                                            
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate
        
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        def set_invalid(input_field, msg=""):
            """
            Highlights the input field to indicate invalid data and sets focus.
            """
            input_field.delete(0, tk.END)
            input_field.configure(background='Yellow')
            input_field.focus()
            if msg == "":
                pass 
            else:
                messagebox.showwarning("Input Error", msg)

        def Validate_Service_Reservice_Dates():
            """ 
            Function Name: Change_Date_To_Format
            Function Purpose: This function validates Service and Reservice Dates.
            """ 
            # Validate Service Date
            if not AddUnit.Check_Input(self.ServiceDateInput.get()):
                set_invalid(self.ServiceDateInput)
                return False

            result_tup = BaseFunctions.Validate_Date_Input(self.ServiceDateInput.get())
            if not result_tup[0]:
                set_invalid(self.ServiceDateInput)
                return False

            self.ServiceDateResult = AddUnit.Change_Date_To_Format(self.ServiceDateInput, result_tup)

            # Automatically calculate and set Reservice Date
            aDateResult = BaseFunctions.Update_Service_InspectionDate(result_tup[1])
            if self.ReserviceDateInput.get() == "":
                self.ReserviceDateInput.configure(state='normal')
                self.ReserviceDateInput.insert(0, datetime.strftime(aDateResult[1], '%m/%d/%Y'))
                self.ReserviceDateInput.configure(state='readonly')

            return True
        
        # Validate Manufacturer Name
        if not (AddUnit.Check_Input(self.DeviceNameInput.get()) and
                BaseFunctions.Validate_String_Input(self.DeviceNameInput.get())):
            set_invalid(self.DeviceNameInput, "Invalid Manufacturer Name. Please try again.")
            return False
        
        # Validate Serial Number
        serial_num = self.SerialNumInput.get()
        if serial_num == "" or not BaseFunctions.Validate_Serial_Input(serial_num):
            set_invalid(self.SerialNumInput, "Invalid serial number. Please try again.")
            return False
        elif serial_num in AutoBelay.astrSerialNum:
            set_invalid(self.SerialNumInput, "Duplicate serial number detected. Please try again.")
            return False

        # Get the Primary Key ID
        sqlPrimKey = ("TAutoBelays", "intAutoBelayID")  
        self.AutoBelayID = self.Get_Or_Create_ID(self.SerialNumInput.get(), sqlPrimKey)
                
        # Validate Bumper Number if it exists
        bumper_num = self.BumperNumInput.get()
        if bumper_num != "" and not BaseFunctions.Validate_Serial_Input(bumper_num):
            set_invalid(self.BumperNumInput, "Invalid bumper number. Please try again.")
            return False
        elif bumper_num == 'Optional':
            pass
        elif bumper_num in AutoBelay.astrBumperNum:
            set_invalid(self.BumperNumInput, "Duplicate bumper number detected. Please try again.")
            return False

        self.BumperNumInput.delete(0, tk.END)
        new_bumper_num_value = bumper_num if bumper_num != "" else 'Optional'
        self.BumperNumInput.insert(0, new_bumper_num_value)
        
        # Validate Manufacturing Date
        if not AddUnit.Check_Input(self.ManuDateInput.get()):
            set_invalid(self.ManuDateInput, "Invalid manufacturing date. Please try again.")
            return False

        result_tup = BaseFunctions.Validate_Date_Input(self.ManuDateInput.get())
        if not result_tup[0]:
            set_invalid(self.ManuDateInput, "Invalid manufacturing date. Please try again.")
            return False

        self.ManuDateInputResult = AddUnit.Change_Date_To_Format(self.ManuDateInput, result_tup)

        # Validate Service and Reservice Dates
        if not Validate_Service_Reservice_Dates():
            return False
        
        # Validate Installation Date
        if not AddUnit.Check_Input(self.InstallDateInput.get()):
            set_invalid(self.InstallDateInput, "Invalid entry. Entry cannot be empty. Please try again.")
            return False

        result_tup = BaseFunctions.Validate_Date_Input(self.InstallDateInput.get())
        if not result_tup[0]:
            set_invalid(self.InstallDateInput, "Invalid installation date. Please try again.")
            return False

        self.InstallDateResult = AddUnit.Change_Date_To_Format(self.InstallDateInput, result_tup)

        # Validate 'In Use' Selection
        if not AddUnit.Check_Input(self.dropInUse.get()):
            set_invalid(self.dropInUse, "Invalid entry. Entry cannot be empty. Please try again.")
            return False
        
        return True

    def Change_Date_To_Format(dtmObject, aResultTup):
        """ 
        Function Name: Change_Date_To_Format
        Function Purpose: This function is executed every call of the validation check to ensure the dates are all
        changed to the same format no matter if the character is valid.
        """ 
        dtmObject.delete(0, END)
        dtmObject.insert(0, aResultTup[1])
        dtmObject = aResultTup[1]

        return dtmObject

    def Restore_ReserviceDate(self):
        """ 
        Function Name: Restore_ReserviceDate
        Function Purpose: This function is executed every call of the validation check to ensure the reservice date persists
        throughout the validation function.
        """              
        # First delete the Reservice object and set it back to the return tuple
        if self.ServiceDateInput.get() != "":
            self.ReserviceDateInput.configure(state='normal')
            self.ReserviceDateInput.delete(0, END)
            aDateResult = BaseFunctions.Update_Service_InspectionDate(self.strServiceDateResult)                                                    
            self.ReserviceDateInput.insert(0, datetime.strftime(aDateResult[1], '%m/%d/%Y'))
            self.ReserviceDateInput.configure(state='readonly')

    def Get_UserInput(self):
        """ 
        Function Name: Get_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        Then the data will be sent to the db.
        """       
        # Get the current date for last and next inspection
        aDateResult = BaseFunctions.Update_Inspection_Date()
        lastDate = datetime.strftime(aDateResult[0], '%m/%d/%Y')
        nextDate =  datetime.strftime(aDateResult[1], '%m/%d/%Y')
        
        # Assign value to the objects
        AutoBelayID = self.AutoBelayID
        SerialNum = self.SerialNumInput.get()
        BumperNum = self.BumperNumInput.get()
        ManufactureDate = self.ManuDateInputResult
        ServiceDate = self.ServiceDateResult
        ReserviceDate = self.ReserviceDateInput.get()
        InstallationDate = self.InstallDateResult
        LastInspectionDate = lastDate
        NextInspectionDate = nextDate
        DeviceInUse = self.dropInUse.get()

        # If BumperNum = "Optional" place a 'None' string
        if BumperNum == "Optional":
            BumperNum = "None"
            
        # Capitalize the first letter of each word and append a space after splitting the user input into a list
        resultList = self.DeviceNameInput.get().split()
        self.Cap_DeviceName = [result.capitalize() for result in resultList]
        DeviceName = ' '.join(self.Cap_DeviceName)                
        
        # Assign the local objects to the class objects
        self.intAutoBelayID = AutoBelayID
        self.strDeviceName = DeviceName
        self.strSerialNum = SerialNum
        self.strBumperNum = BumperNum
        self.dtmManufactureDate = ManufactureDate
        self.dtmServiceDate = ServiceDate
        self.dtmReserviceDate = ReserviceDate
        self.dtmInstallationDate = InstallationDate
        self.dtmLastInspectionDate = LastInspectionDate
        self.dtmNextInspectionDate = NextInspectionDate
        self.blnDeviceInUse = DeviceInUse

    def Get_Combined_Selection(self, persisted_array, default_value):
        """
        Function Name: Get_Combined_Selection
        Function Purpose: This function combines the array elements into a comma-separated string,
        and handles the case when the persisted array is empty by setting a default value.
        """
        if len(persisted_array) == 0:
            return default_value
        else:
            return ",".join(persisted_array)
        
    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
                        
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlStatement[0], sqlStatement[1]))    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
    
    def Clear_BG_Color(self):
        """ 
        Function Name: Clear_BG_Color
        Function Purpose: This button executes when the user submits their entries and clears the background
        color before any validation checks.
        """
        # Delete the button after submission
        self.DeviceNameInput.configure(background='White')
        self.SerialNumInput.configure(background='White')
        self.BumperNumInput.configure(background='White')
        self.ManuDateInput.configure(background='White')
        self.ServiceDateInput.configure(background='White')
        self.ReserviceDateInput.configure(background='White')
        self.InstallDateInput.configure(background='White')
        
    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This button executes when the user wants to reset the values.
        """
        # Delete the button after submission
        self.DeviceNameInput.delete(0, END)
        self.SerialNumInput.delete(0, END)
        self.BumperNumInput.delete(0, END)
        self.ManuDateInput.delete(0, END)
        self.ReserviceDateInput.configure(state='normal')
        self.ReserviceDateInput.delete(0, END)
        self.ReserviceDateInput.configure(state='readonly')
        self.ServiceDateInput.delete(0, END)
        self.ReserviceDateInput.delete(0, END)
        self.InstallDateInput.delete(0, END)
        
        # Reset the drop menus
        self.dropInUse.set("")
        
        # Clear out the background colors and set to default as 'white'
        AddUnit.Clear_BG_Color(self)

        # Create a list of all the entry objects
        aEntryList = (self.ManuDateInput, self.ServiceDateInput, self.InstallDateInput, self.BumperNumInput) 
        astrPlaceHolder = ("MM/DD/YYYY", "MM/DD/YYYY", "MM/DD/YYYY", "Optional")

        # Insert the placeholders at the desired entry points
        for i, entry in enumerate(aEntryList):
            entry.insert(0, astrPlaceHolder[i])
            entry.config(fg='grey')
            entry.bind('<FocusIn>', lambda event, entry=entry, placeholder=astrPlaceHolder[i]: self.On_Entry_Click(event, entry, placeholder))
            entry.bind('<FocusOut>', lambda event, entry=entry, placeholder=astrPlaceHolder[i]: self.On_FocusOut(event, entry, placeholder))
        

    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the new AutoBelay unit to the db. Else, reset
        """
        # Check if all of the inputs are valid
        global blnValidate 
        blnValidate = bool(False)
        
        # Clear out the background colors and set to default as 'white'
        AddUnit.Clear_BG_Color(self)
        
        # Get the blnValidate status
        blnValidate = AddUnit.Validate_InputFields(self)
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to add new unit?') is True:     
                # Load the user data and prep the data for db dump
                AddUnit.Get_UserInput(self)
                AutoBelay.Add_NewAutoBelay_Query(self)                     

                # Check if the user would like to add another unit
                if messagebox.askyesno(message='SUCCESSFUL UPLOAD! \n\n Would you like to add another unit?') is True:
                    # Clear the input fields and after data is submitted to the database
                    AddUnit.Reset(self)
                else:
                    AddUnit.Exit(self)
            
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        
                
#######################################################################################################
# Update AutoBelay Info
#######################################################################################################

class UpdateUnitInfo(tk.Toplevel, AutoBelay):
    """
    Class Name: UpdateUnitInfo
    Class Description: This class updates manufacture, service, re-service, and installation dates for any AutoBelay unit to the database.
    """
    def __init__(self, parent):
        # Initialize the Toplevel window
        super().__init__(parent)

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (560/2)     
        self.y = (self.heightSize/2) - (430/2)  
                                        
        # Create the Window attributes
        self.WindowTitle = self.title("Update Auto Belay Information")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (560, 430, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Load the query selection widget
        self.Selection_Widget()
                
        # Create the second frame to hold the input fields
        self.frameInput = LabelFrame(self, text="Unit Credentials")
        self.frameInput.place(x=75, y=170, width=405, height=200)

        # Create the labels 
        self.lblSerialNum = tk.Label(self.frameInput, text="Serial Number:")
        self.lblBumperNum = tk.Label(self.frameInput, text="Bumper Number:")
        self.lblManuDate = tk.Label(self.frameInput, text="Manufacture Date:")
        self.lblServiceDate = tk.Label(self.frameInput, text="Service Date:")
        self.lblInstallDate = tk.Label(self.frameInput, text="Install Date:")
        self.lblDeviceInUse = tk.Label(self.frameInput, text="Device In Use:")

        # Create the label locations
        self.lblSerialNum.grid(row=1, column=0, sticky='W', padx=5)
        self.lblBumperNum.grid(row=2, column=0, sticky='W', padx=5)
        self.lblManuDate.grid(row=3, column=0, sticky='W', padx=5)
        self.lblServiceDate.grid(row=4, column=0, sticky='W', padx=5)
        self.lblInstallDate.grid(row=5, column=0, sticky='W', padx=5)
        self.lblDeviceInUse.grid(row=6, column=0, sticky='W', padx=5)
        
        # Create the entry input box
        self.SerialNumInput = Entry(self.frameInput, width=39, state='disabled')
        self.BumperNumInput = Entry(self.frameInput, width=39, state='disabled')
        self.ManuDateInput = Entry(self.frameInput, width=39, state='disabled')
        self.ServiceDateInput = Entry(self.frameInput, width=39, state='disabled')
        self.InstallDateInput = Entry(self.frameInput, width=39, state='disabled')

        # Create the combo box
        self.aInUseSelectionList = ("Yes", "No", "Out For Reservice")
        self.dropInUseSelection = ttk.Combobox(self.frameInput, values=self.aInUseSelectionList, state='disabled')
        self.dropInUseSelection.configure(width=36,)

        # Create the grid for all of the entry input fields
        self.SerialNumInput.grid(row=1, column=1, padx=25, pady=5)
        self.BumperNumInput.grid(row=2, column=1, pady=5)
        self.ManuDateInput.grid(row=3, column=1, pady=5)
        self.ServiceDateInput.grid(row=4, column=1, pady=5)
        self.InstallDateInput.grid(row=5, column=1, pady=5)
        self.dropInUseSelection.grid(row=6, column=1, pady=5)

        # Create the buttons
        self.btnExit = Button(self, text="Back", width=10, command=lambda:UpdateUnitInfo.Exit(self))
        self.btnReset = Button(self, text="Reset", width=10, command=lambda:UpdateUnitInfo.Reset(self))
        self.btnSubmit = Button(self, text="Submit", width=10, command=lambda:UpdateUnitInfo.Submit(self))

        # Create the button grid
        self.btnExit.place(x=105, y=385)
        self.btnReset.place(x=235, y=385)
        self.btnSubmit.place(x=365, y=385)

    def Selection_Widget(self):
        """ 
        Function Name: Selection_Widget
        Function Purpose: This function populates the search by widget for Serial or Bumper Num search.
        """           
        # Create the first frame to hold the input fields
        self.selectInput = LabelFrame(self, text="Select Unit")
        self.selectInput.place(x=75, y=35, width=405, height=130)

        # Create the labels 
        self.lblSearchByUnitID = Label(self.selectInput, text="Query by Unit ID:")
        self.lblUnitSelection = Label(self.selectInput, text="Unit ID Selection:")

        # Create the label locations
        self.lblSearchByUnitID.place(x=10, y=5)
        self.lblUnitSelection.place(x=10, y=35)

        # Create variables to hold the value of the selected radio button
        self.objRadioValue = tk.StringVar(value='serial')
        self.objComboValue = tk.StringVar()

        # List objects of serial and bumper values
        self.astrSerialNumList = self.astrSerialNum
        self.astrBumperNumList = self.astrBumperNum

        # Create the radio buttons
        self.rbSerial = tk.Radiobutton(self.selectInput, text="Serial Number", variable=self.objRadioValue, value="serial", command=self.Populate_Dropdown)
        self.rbBumper = tk.Radiobutton(self.selectInput, text="Bumper Number", variable=self.objRadioValue, value="bumper", command=self.Populate_Dropdown)

        # Place the radio buttons next to each other using .place()
        self.rbSerial.place(x=135, y=5)
        self.rbBumper.place(x=265, y=5)
                    
        # Create the combo box
        self.dropUnitSelection = ttk.Combobox(self.selectInput, values=self.astrSerialNumList, state='readonly')
        self.dropUnitSelection.configure(width=36,)

        # Populate the dropdown based on the default radio button selection
        self.Populate_Dropdown()

        # Create the grid for all of the entry input fields
        self.dropUnitSelection.place(x=140, y=35)

        # Create the buttons
        self.btnSelectSubmit = Button(self.selectInput, text="Submit", width=10, command=lambda:UpdateUnitInfo.SubmitSelect(self))

        # Create the button grid
        self.btnSelectSubmit.place(x=165, y=70)  

    def Populate_Dropdown(self):
        """ 
        Function Name: Populate_Dropdown
        Function Purpose: This function populates the dropdown based on the radio button selection.
        """           
        if self.objRadioValue.get() == "serial":
            self.dropUnitSelection["values"] = self.astrSerialNumList
        else:
            self.dropUnitSelection["values"] = self.astrBumperNumList
        self.dropUnitSelection.set("")  # Clear the combobox's current value                                    
        
    def Change_Date_To_Format(dtmObject, aResultTup):
        """ 
        Function Name: Change_Date_To_Format
        Function Purpose: This function is executed every call of the validation check to ensure the dates are all
        changed to the same format no matter if the character is valid.
        """ 
        dtmObject.delete(0, END)
        dtmObject.insert(0, aResultTup[1])
        dtmObject = aResultTup[1]

        return dtmObject

    def Convert_Date_Format(date_str):
        """ 
        Function Name: SubmitSelect
        Function Purpose: This button Convert date from "YYYY-MM-DD" to "MM/DD/YYYY"
        """
        year, month, day = date_str.split('-')
        return f"{month}/{day}/{year}"

    def Disable_After_Submit(self):
        """ 
        Function Name: Disable_After_Submit
        Function Purpose: This function disables certain controls after submission.
        """   
        # Disable the submit button
        self.btnSubmit.configure(state='disabled')
        
        # Reset the value of the dropdown
        self.dropUnitSelection.set("")

    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)
        
    def Check_Serial_Or_Bumper(self):
        """ 
        Function Name: Check_Serial_Or_Bumper
        Function Purpose: This function is executed once the user clicks on the option of query search by serial
        number or bumper number. 
        """        
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Get the primary key ID from the dropdown
        strSelectionID = self.dropUnitSelection.get()
        
        # Determine the primary key for the query
        if strSelectionID in AutoBelay.astrSerialNum:
            primary_key = AutoBelay.astrSerialNum.index(strSelectionID) + 1
            blnFlag = True
        elif strSelectionID in AutoBelay.astrBumperNum:
            primary_key =  AutoBelay.astrBumperNum.index(strSelectionID) + 1
            blnFlag = False
            
        # Return the primary key
        return (blnFlag, primary_key)
                
    def SubmitSelect(self):
        """ 
        Function Name: SubmitSelect
        Function Purpose: This button executes when the user selects the user login names.
        """
        # Set the state of the inputs
        for entry in [self.SerialNumInput, self.BumperNumInput, self.ManuDateInput, self.ServiceDateInput, self.InstallDateInput]:
            entry.configure(state='normal')

        # Configure the drop menu for in use
        self.dropInUseSelection.configure(state='readonly')

        # Determine the primary key for the query
        resultTup =  self.Check_Serial_Or_Bumper()
        primary_key =  resultTup[1]

        # Execute the query
        aParams = ('TAutoBelays', 'intAutoBelayID', primary_key)
        QueryResult = Queries.Get_All_DB_Values_OnePrimKey(Queries, aParams)
        
        if QueryResult:
            self.SerialNumInput.insert(0, QueryResult[2])
            self.BumperNumInput.insert(0, QueryResult[3])
            self.ManuDateInput.insert(0, UpdateUnitInfo.Convert_Date_Format(QueryResult[4]))
            self.ServiceDateInput.insert(0, UpdateUnitInfo.Convert_Date_Format(QueryResult[5]))
            self.InstallDateInput.insert(0, UpdateUnitInfo.Convert_Date_Format(QueryResult[7]))
            self.Set_Previous_Drop_List(QueryResult[10], self.dropInUseSelection)
        
        # Disable the select submit button
        self.btnSelectSubmit.configure(state='disabled')
        
        # Enable the submit and reset buttons
        self.btnSubmit.configure(state='normal')
        self.btnReset.configure(state='normal')
                
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate
        
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        def set_invalid(input_field, msg):
            """
            Highlights the input field to indicate invalid data and sets focus.
            """
            input_field.delete(0, tk.END)
            input_field.configure(background='Yellow')
            input_field.focus()
            messagebox.showwarning("Input Error", msg)

        def Validate_Service_Reservice_Dates():
            """ 
            Function Name: Validate_Service_Reservice_Dates
            Function Purpose: This function validates Service and Reservice Dates.
            """ 
            # Validate Service Date
            if not UpdateUnitInfo.Check_Input(self.ServiceDateInput.get()):
                set_invalid(self.ServiceDateInput, "Service Date should not be empty. Please try again.")
                return False

            result_tup = BaseFunctions.Validate_Date_Input(self.ServiceDateInput.get())
            if not result_tup[0]:
                set_invalid(self.ServiceDateInput, "Invalid Service Date. Please try again.")
                return False

            self.ServiceDateResult = UpdateUnitInfo.Change_Date_To_Format(self.ServiceDateInput, result_tup)

            return True

        # Validate Serial Number
        serial_num = self.SerialNumInput.get()
        if not (UpdateUnitInfo.Check_Input(serial_num) and BaseFunctions.Validate_Serial_Input(serial_num)):
            set_invalid(self.SerialNumInput, "Invalid serial number. Please try again.")
            return False
        
        # Validate Bumper Number if it exists
        bumper_num = self.BumperNumInput.get()
        if bumper_num != "" and not BaseFunctions.Validate_Serial_Input(bumper_num):
            set_invalid(self.BumperNumInput, "Invalid bumper number. Please try again.")
            return False

        self.BumperNumInput.delete(0, tk.END)
        new_bumper_num_value = bumper_num if bumper_num != "" else 'Optional'
        self.BumperNumInput.insert(0, new_bumper_num_value)
                
        # Validate Manufacturing Date
        if not UpdateUnitInfo.Check_Input(self.ManuDateInput.get()):
            set_invalid(self.ManuDateInput, "Manufacture Date should not be empty. Please try again.")
            return False

        result_tup = BaseFunctions.Validate_Date_Input(self.ManuDateInput.get())
        if not result_tup[0]:
            set_invalid(self.ManuDateInput, "Invalid Manufacture Date. Please try again.")
            return False

        self.ManuDateInputResult = UpdateUnitInfo.Change_Date_To_Format(self.ManuDateInput, result_tup)

        # Validate Service and Reservice Dates
        if not Validate_Service_Reservice_Dates():
            return False
        
        # Validate Installation Date
        if not UpdateUnitInfo.Check_Input(self.InstallDateInput.get()):
            set_invalid(self.InstallDateInput, "Installation Date should not be empty. Please try again.")
            return False

        result_tup = BaseFunctions.Validate_Date_Input(self.InstallDateInput.get())
        if not result_tup[0]:
            set_invalid(self.InstallDateInput, "Invalid Installation Date. Please try again.")
            return False

        self.InstallDateResult = UpdateUnitInfo.Change_Date_To_Format(self.InstallDateInput, result_tup)

        # Validate 'In Use' Selection
        if not AddUnit.Check_Input(self.dropInUseSelection.get()):
            set_invalid(self.dropInUseSelection, "Device In Use should not be empty. Please try again.")
            return False
        
        return True

    def Get_UserInput(self):
        """ 
        Function Name: Get_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        Then the data will be sent to the db.
        """                
        # Assign value to the objects
        SerialNum = self.SerialNumInput.get()
        BumperNum = self.BumperNumInput.get()
        ManuDate = datetime.strptime(self.ManuDateInputResult, '%m/%d/%Y').date()
        ServiceDate = datetime.strptime(self.ServiceDateResult, '%m/%d/%Y').date()
        aServiceDateList = BaseFunctions.Update_Service_InspectionDate(self.ServiceDateResult)
        ReserviceDate = datetime.strftime(aServiceDateList[1], '%m/%d/%Y')
        InstallationDate = datetime.strptime(self.InstallDateResult, '%m/%d/%Y').date()
        ManuDate = str(ManuDate)
        ServiceDate = str(ServiceDate)
        ReserviceDate = str(ReserviceDate)
        InstallationDate = str(InstallationDate)
        DeviceInUse = self.dropInUseSelection.get()
        
        # First check if the serial or bumper number was selected 
        resultTup =  self.Check_Serial_Or_Bumper()
        intPrimKey = resultTup[1] - 1

        # Commit the data to load the AutoBelay class objects with the data from the db
        AutoBelay.strSerialNum = AutoBelay.astrSerialNum[intPrimKey]
        AutoBelay.Set_AutoBelay_Data(AutoBelay)
            
        # Finish by updating the AutoBelay class objects before the database dump
        a = AutoBelay(self.intAutoBelayID, self.strDeviceName, SerialNum, BumperNum, ManuDate, ServiceDate, 
                    ReserviceDate, InstallationDate, self.dtmLastInspectionDate, self.dtmNextInspectionDate, 
                    DeviceInUse)
        AutoBelay.intAutoBelayID = a.intAutoBelayID
        AutoBelay.strDeviceName = a.strDeviceName
        AutoBelay.strSerialNum = a.strSerialNum
        AutoBelay.strBumperNum = a.strBumperNum
        AutoBelay.dtmManufactureDate = a.dtmManufactureDate
        AutoBelay.dtmServiceDate = a.dtmServiceDate
        AutoBelay.dtmReserviceDate = a.dtmReserviceDate
        AutoBelay.dtmInstallationDate = a.dtmInstallationDate
        AutoBelay.dtmLastInspectionDate = a.dtmLastInspectionDate
        AutoBelay.dtmNextInspectionDate = a.dtmNextInspectionDate
        AutoBelay.blnDeviceInUse = a.blnDeviceInUse
        
    def Clear_BG_Color(self):
        """ 
        Function Name: Clear_BG_Color
        Function Purpose: This button executes when the user submits their entries and clears the background
        color before any validation checks.
        """
        # Delete the button after submission
        self.SerialNumInput.configure(background='White')
        self.BumperNumInput.configure(background='White')
        self.ManuDateInput.configure(background='White')
        self.ServiceDateInput.configure(background='White')
        self.InstallDateInput.configure(background='White')
        
    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This button executes when the user wants to reset the values.
        """
        # Delete the entries
        self.dropUnitSelection.set("")
        self.SerialNumInput.delete(0, END)
        self.BumperNumInput.delete(0, END)
        self.ManuDateInput.delete(0, END)
        self.ServiceDateInput.delete(0, END)
        self.InstallDateInput.delete(0, END)
        self.dropInUseSelection.set("")
        
        # Re-configure input entries to be disabled
        self.SerialNumInput.configure(state='disabled')
        self.BumperNumInput.configure(state='disabled')
        self.ManuDateInput.configure(state='disabled')
        self.ServiceDateInput.configure(state='disabled')
        self.InstallDateInput.configure(state='disabled')       
        self.dropInUseSelection.configure(state='disabled') 

        # Disable/enable the select, submit, and reset submit button
        self.btnSelectSubmit.configure(state='normal')
        self.btnReset.configure(state='disabled')
        self.btnSubmit.configure(state='disabled') 

        # Reset the radio button to its default value
        self.objRadioValue.set("serial")
        
        # Populate the dropdown based on default radio button selection
        self.Populate_Dropdown()

        # Re-Populate the dropdown menus 
        self.dropUnitSelection["values"] = self.astrSerialNumList
        self.dropInUseSelection["values"] = self.aInUseSelectionList
        
        # Clear out the background colors and set to default as 'white'
        UpdateUnitInfo.Clear_BG_Color(self)

        # Call the function to disable controls after submission
        self.Disable_After_Submit()
        
    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the updated AutoBelay unit information to the db. 
        Else, reset
        """
        # Check if all of the inputs are valid
        global blnValidate 
        blnValidate = bool(False)
        
        # Clear out the background colors and set to default as 'white'
        UpdateUnitInfo.Clear_BG_Color(self)
        
        # Get the blnValidate status
        blnValidate = UpdateUnitInfo.Validate_InputFields(self)
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to update the unit information?') is True:     
                # Load the user data and prep the data for db dump
                UpdateUnitInfo.Get_UserInput(self)             
                AutoBelay.Update_NewAutoBelay_Query(self)
                AutoBelayReserviceReport.Update_AutoBelay_ReserviceReport_Query(self)

                # Check if the user would like to update another unit
                if messagebox.askyesno(message='SUCCESSFUL UPDATE! \n\n Would you like to update another unit?') is True:
                    # Clear the input fields and after data is submitted to the database
                    UpdateUnitInfo.Reset(self)
                else:
                    UpdateUnitInfo.Exit(self)
            else:
                pass

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        
        
# #######################################################################################################
# # Add New Location Class
# ####################################################################################################### 

class AddLocation(tk.Toplevel, WallLocation):
    """
    Class Name: AddLocation
    Class Description: This class adds a New Wall Location to the database.
    """
    def __init__(self, parent):
        # Initialize the Toplevel window
        super().__init__(parent)

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (805/2)     
        self.y = (self.heightSize/2) - (220/2)   
                
        # Create the Window attributes
        self.title("Add New Wall Location")
        self.geometry('%dx%d+%d+%d' % (805, 220, self.x, self.y))
        self.resizable(False, False)

        # Create the second frame to hold the input fields
        self.typeFrame = tk.LabelFrame(self, text="Add Location")
        self.typeFrame.place(x=100, y=10, width=600, height=150)      

        # Create the labels 
        self.lblMyLocation = tk.Label(self.typeFrame, text="Wall Locations:")
        self.lblLineNumber = tk.Label(self.typeFrame, text="Line Number:")
        self.lblFindMsg = tk.Label(self.typeFrame, text="Can't find what your're looking for?")
        self.lblWallName = tk.Label(self.typeFrame, text="Add New Location Name:")

        # Create the label locations    
        self.lblMyLocation.place(x=20, y=10)         
        self.lblLineNumber.place(x=355, y=10)
        self.lblFindMsg.place(x=195, y=60)
        self.lblWallName.place(x=35, y=90)

        # Add some items to the listBox in alphabetical order
        self.aDropSelectItems = ttk.Combobox(self.typeFrame, values=Location.astrLocationName, state='readonly')

        # Create the drop down menu size for each attribute
        self.aDropSelectItems.configure(width=30)

        # Create the grid for the drop down menu list objects
        self.aDropSelectItems.place(x=115, y=10)  
        
        # Create the entry input box
        self.LineNumberInput = Entry(self.typeFrame, width=20)
        self.WallNameInput = Entry(self.typeFrame, width=35)

        # Create the grid for all of the entry input fields
        self.LineNumberInput.place(x=445, y=10)
        self.WallNameInput.place(x=185, y=90)
        
        # Create the buttons
        self.btnAdd = Button(self.typeFrame, text="Add", width=10, command=lambda:AddLocation.Add(self))
        self.btnExit = Button(self, text="Back", width=10, command=lambda:AddLocation.Exit(self))
        self.btnReset = Button(self, text="Reset", width=10, command=lambda:AddLocation.Reset(self))
        self.btnSubmit = Button(self, text="Submit", width=10, command=lambda:AddLocation.Submit(self))

        # Create the button grid
        self.btnAdd.place(x=420, y=87)
        self.btnExit.place(x=220, y=175)
        self.btnReset.place(x=355, y=175)
        self.btnSubmit.place(x=490, y=175)
            
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate

    def Validate_Drop_Plus_LineInput(self):
        """ 
        Function Name: Validate_Drop_Plus_LineInput
        Function Purpose: This function validates the user selection from the drop menu and the line number entry.
        """
        # Check the user input
        blnValidate = AddLocation.Check_Input(self.aDropSelectItems.get())            
    
        # Check if the input is valid
        if (blnValidate is True):
            # Check the user input
            blnValidate = AddLocation.Check_Input(self.LineNumberInput.get())

            # Check if the input is valid
            if (blnValidate is True):
                # Check the user input
                blnValidate = BaseFunctions.Validate_StringNumeric_Input(self.LineNumberInput.get())
                
                # Check if the input is valid
                if (blnValidate is True):
                    # Configure the Wall location name
                    self.WallLocationDesc = BaseFunctions.Config_Wall_Location_Name(self.aDropSelectItems.get(), self.LineNumberInput.get())
                    # Check if the input is valid
                    if (blnValidate is True):
                        # Get the Primary Key ID
                        if self.WallLocationDesc not in WallLocation.astrWallLocationDesc:
                            # Get the Primary Key ID
                            sqlWallLocationPrimKey = ("TWallLocations", "intWallLocationID")   
                            self.WallLocationID = self.Get_Or_Create_ID(self.WallLocationDesc, sqlWallLocationPrimKey)
                            blnValidate = True
                        else:
                            messagebox.showwarning(message='ERROR \n\n Wall location (%s  %s) already exists. Please try again.'%(self.WallNameInput.get(), self.LineNumberInput.get()))
                            # Return blnValidate as False
                            blnValidate = False
                            self.Reset()         
                else:
                    # Return blnValidate as False
                    blnValidate = False         
                    self.LineNumberInput.delete(0, END)
                    self.LineNumberInput.configure(background='Yellow')
                    self.LineNumberInput.focus()                
            else:
                # Return blnValidate as False
                blnValidate = False         
                self.LineNumberInput.delete(0, END)
                self.LineNumberInput.configure(background='Yellow')
                self.LineNumberInput.focus()                                                                               
        else:
            # Return blnValidate as False
            blnValidate = False
            self.aDropSelectItems.focus()
            
        return blnValidate            
    
    def Validate_New_Location_Name_Input(self):
        """ 
        Function Name: Validate_New_Location_Name_Input
        Function Purpose: This function validates the user input for a new location to the drop menu list.
        """
        # Check the user input
        blnValidate = AddLocation.Check_Input(self.WallNameInput.get())            
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check the user input
            blnValidate = BaseFunctions.Validate_String_Input(self.WallNameInput.get())

            # Check if the new location name already exists
            if (blnValidate is True):
                # Change the word to capitalize the first letter of each word
                self.LocationDesc = self.WallNameInput.get().title()
                
                # Get the Primary Key ID
                if self.LocationDesc not in Location.astrLocationName:
                    # Get the Primary Key ID
                    sqlLocationPrimKey = ("TLocations", "intLocationID")   
                    self.LocationID = self.Get_Or_Create_ID(self.LocationDesc, sqlLocationPrimKey)
                    blnValidate = True
                else:
                    messagebox.showwarning(message='ERROR \n\n Wall location (%s  %s) already exists. Please try again.'%(self.WallNameInput.get(), self.LineNumberInput.get()))
                    # Return blnValidate as False
                    blnValidate = False
                    self.Reset()          
            else:
                # Return blnValidate as False
                blnValidate = False         
                self.WallNameInput.delete(0, END)
                self.WallNameInput.configure(background='Yellow')
                self.WallNameInput.focus()                                                                        
        else:
            # Return blnValidate as False
            blnValidate = False
            self.WallNameInput.delete(0, END)
            self.WallNameInput.configure(background='Yellow')
            self.WallNameInput.focus()           

        return blnValidate                                                

    def Get_Combined_Selection(self, persisted_array, default_value):
        """
        Function Name: Get_Combined_Selection
        Function Purpose: This function combines the array elements into a comma-separated string,
        and handles the case when the persisted array is empty by setting a default value.
        """
        if len(persisted_array) == 0:
            return default_value
        else:
            return ",".join(persisted_array)
        
    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
                        
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlStatement[0], sqlStatement[1]))    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
    
    def Get_UserInput(self):
        """ 
        Function Name: Get_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        Then the data will be sent to the db.
        """       
        # # Get the Primary Key ID
        # sqlWallLocationPrimKey = ("TWallLocations", "intWallLocationID")   
        # WallLocationID = Queries.Get_MaxPrimaryKeys(Queries, sqlWallLocationPrimKey[0], sqlWallLocationPrimKey[1])

        # Assign the local objects to the class objects
        wl = WallLocation(self.WallLocationID, self.WallLocationDesc)
        WallLocation.intWallLocationID = wl.intWallLocationID
        WallLocation.strWallLocationDesc = wl.strWallLocationDesc
        
    def Get_UserInput_Add(self):
        """ 
        Function Name: Get_UserInput_Add
        Function Purpose: This function is executed once the user clicks on the add button inside the result
        frame. If the user clicks 'Add', all data is pulled and dumped into the corresponding class objects. 
        Then the data will be sent to the db.
        """       
        # Assign the local objects to the class objects
        l = Location(self.LocationID, self.LocationDesc)
        Location.intLocationID = l.intLocationID
        Location.strLocationName = l.strLocationName
                
    def Clear_BG_Color(self):
        """ 
        Function Name: Clear_BG_Color
        Function Purpose: This button executes when the user submits their entries and clears the background
        color before any validation checks.
        """
        # Delete the button after submission
        self.WallNameInput.configure(background='White')
        self.LineNumberInput.configure(background='White')

    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This button executes when the user wants to Resets the values.
        """
        # Set the list objects first element to the drop click object
        self.aDropSelectItems.set("")
                
        # Delete the button after submission
        self.WallNameInput.delete(0, END)    
        self.LineNumberInput.delete(0, END)    
        
        # Clear out the background colors and set to default as 'white'
        AddLocation.Clear_BG_Color(self)

    def Add(self):
        """ 
        Function Name: Add
        Function Purpose: This button executes when the user wants to add the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the new location name to the db. Else, reset
        """
        # Check if all of the inputs are valid
        global blnValidate 
        blnValidate = bool(False)
        
        # Clear out the background colors and set to default as 'white'
        AddLocation.Clear_BG_Color(self)
                
        # Get the blnValidate status
        blnValidate = AddLocation.Validate_New_Location_Name_Input(self)
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check first with the user if the entry's are correct before dumping to DB                 
            if messagebox.askyesno(message='CAUTION! \n\nDo you want to proceed with adding this new wall location name? \n\n "%s"'%(self.LocationDesc)) is True:
                # Load the user data and prep the data for db dump
                AddLocation.Get_UserInput_Add(self)
                Location.Add_NewLocation_Query(Location)
                AddLocation.Reset(self)
                AddLocation.Update_Dropdown_Values(self)
            else:
                pass  

    def Update_Dropdown_Values(self):
        """ 
        Function Name: Update_Dropdown_Values
        Function Purpose: This function is executed once the user clicks on Location button and updates the drop down
        object list with the new values.
        """             
        self.aDropSelectItems['values'] = Location.astrLocationName
        
    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the new location to the db. Else, reset
        """
        # Check if all of the inputs are valid
        global blnValidate 
        blnValidate = bool(False)
        
        # Clear out the background colors and set to default as 'white'
        AddLocation.Clear_BG_Color(self)
                
        # Get the blnValidate status
        blnValidate = AddLocation.Validate_Drop_Plus_LineInput(self)
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\nYour abbreviated wall location is: %s \n\nDo you want to proceed with adding this new wall location?'%(self.WallLocationDesc)) is True:     
                # Load the user data and prep the data for db dump
                AddLocation.Get_UserInput(self)
                WallLocation.Add_NewWallLocation_Query(WallLocation)

                # Check if the user would like to add another wall location
                if messagebox.askyesno(message='SUCCESSFUL UPLOAD! \n\n Would you like to add another wall location?') is True:
                    # Clear the input fields and after data is submitted to the database
                    AddLocation.Reset(self)
                else:
                    AddLocation.Exit(self)
            else:
                pass  

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        
        
#######################################################################################################
# Carabiner Inspection Class
#######################################################################################################

class  CarabinerInspection(tk.Tk): 
    """
    Class Name: CarabinerInspection
    Class Description: This class is to conduct carabiner inspections.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new carabiner inspection. User must click
        'Next' Button in order to progress to the next inspection type. A Visual, Physical, and Functional inspection
        must be performed to complete the inspection.
        """
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk window 
        self.x = (self.widthSize/2) - (805/2)     
        self.y = (self.heightSize/2) - (600/2)          
        
        # Create the Window attributes        
        strUnitSelected = "Auto Belay Selected: %s"%(AutoBelay.strSerialNum)      
        self.title("Carabiner Inspection - " + strUnitSelected)
        self.geometry('%dx%d+%d+%d' % (805, 600, self.x, self.y))
        self.resizable(False, False)

        # Create the frame fields
        self.typeFrame = tk.LabelFrame(self, text="CarabinerSelection")
        self.typeFrame.place(x=95, y=10, width=610, height=80)
        self.visCheckListFrame = tk.LabelFrame(self, text="Visual Inspection Results")
        self.visCheckListFrame.place(x=95, y=100, width=300, height=200)
        self.physCheckListFrame = tk.LabelFrame(self, text="Physical Inspection Results")
        self.physCheckListFrame.place(x=405, y=100, width=300, height=200)
        self.functCheckListFrame = tk.LabelFrame(self, text="Functional Inspection Results")
        self.functCheckListFrame.place(x=95, y=310, width=610, height=125)
        self.commFrame = tk.LabelFrame(self, text="Inspection Comment")
        self.commFrame.place(x=95, y=440, width=610, height=100)
                
        # Create the label for the checkboxes
        self.lblCarabType = tk.Label(self.typeFrame, text="Carabiner Type:")
        self.lblCarabVisualStatus = tk.Label(self.visCheckListFrame, text="Visual Status:")
        self.lblCarabPhysicalStatus = tk.Label(self.physCheckListFrame, text="Physical Status:")
        self.lblCarabFunctStatus = tk.Label(self.functCheckListFrame, text="Function Status:")
                        
        # Create the label locations
        self.lblCarabType.place(x=155, y=18)
        self.lblCarabVisualStatus.place(x=5, y=140)
        self.lblCarabPhysicalStatus.place(x=5, y=140)
        self.lblCarabFunctStatus.place(x=155, y=65)

        # Create the drop down menu list for each attribute
        self.dropCarabType = ttk.Combobox(self.typeFrame, values=Carabiner.astrCarabinerType, state='readonly')
        self.dropCarabVisStatus = ttk.Combobox(self.visCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropCarabPhysStatus = ttk.Combobox(self.physCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropCarabFunctStatus = ttk.Combobox(self.functCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        
        # Create the drop down menu size for each attribute
        self.dropCarabType.configure(width=20)
        self.dropCarabVisStatus.configure(width=20)
        self.dropCarabPhysStatus.configure(width=20)
        self.dropCarabFunctStatus.configure(width=20)
        
        # Create the grid for the drop down menu list objects
        self.dropCarabType.place(x=290, y=20)   
        self.dropCarabVisStatus.place(x=125, y=140)  
        self.dropCarabPhysStatus.place(x=125, y=140)  
        self.dropCarabFunctStatus.place(x=290, y=65)  

        # Create the master list for the metallic and functional inspection types
        self.selectItems = Metallic.astrMetallicInspectionDesc 
        self.functItems = CarabinerFunction.astrCarabinerFunctionDesc
        
        # Create the checkbox lists for visual, physical, and functional
        self.visCheckList = [] 
        self.physCheckList = []
        self.functCheckList = []
        
        # Create an empty list to store selected items
        self.checkboxVisStates = {}
        self.checkboxPhysStates = {}
        self.checkboxFuncStates = {}

        # Create the checkbox list
        self.Create_Check_Buttons(self.selectItems, self.visCheckListFrame, CarabVisSelection.astrCarabVisMetSelect, self.visCheckList, self.checkboxVisStates, self.Get_VisCheckbox_List, "visual")
        self.Create_Check_Buttons(self.selectItems, self.physCheckListFrame, CarabPhysSelection.astrCarabPhysMetSelect, self.physCheckList, self.checkboxPhysStates, self.Get_PhysCheckbox_List, "physical")
        self.Create_Check_Buttons(self.functItems, self.functCheckListFrame, CarabFunctSelection.astrCarabFunctSelect, self.functCheckList, self.checkboxFuncStates, self.Get_FuncCheckbox_List, "functional")

        # First check if the selection values have been assigned
        self.Set_Previous_Checkbox_List(CarabVisSelection.astrCarabVisMetSelect, self.visCheckList, self.selectItems)
        self.Set_Previous_Checkbox_List(CarabPhysSelection.astrCarabPhysMetSelect, self.physCheckList, self.selectItems)
        self.Set_Previous_Checkbox_List(CarabFunctSelection.astrCarabFunctSelect, self.functCheckList, self.functItems)
                
        # Check if the cache values for any drop menus have been previously selected and set the values
        if Bool_Flag.blnCarabPersistFlag == True:
            self.Set_Previous_Drop_List(Carabiner.strCarabinerType, self.dropCarabType)
            self.Set_Previous_Drop_List(CarabVisSelection.strCarabVisStatus, self.dropCarabVisStatus)
            self.Set_Previous_Drop_List(CarabPhysSelection.strCarabPhysStatus, self.dropCarabPhysStatus)
            self.Set_Previous_Drop_List(CarabFunctSelection.strCarabFunctStatus, self.dropCarabFunctStatus)

        # Create the comment fieldConnectorInspection
        self.commInput = tk.Text(self.commFrame, state='normal')
        self.commInput.grid(row=0, column=0, padx=5, pady=4)
        self.commInput.configure(width=74, height=4, padx=0)
        
        # Create the buttons
        self.btnBack = Button(self, text="Back", width=10, command=self.Back)
        self.btnClear = Button(self, text="Clear", width=10, command=self.Clear)
        self.btnExit = Button(self, text="Exit", width=10, command=self.Exit)
        self.btnNext = Button(self, text="Next", width=10, command=self.Next)
            
        # Create the position of the button
        self.btnBack.place(x=160, y=555)
        self.btnClear.place(x=420, y=555)
        self.btnNext.place(x=550, y=555) 
        self.btnExit.place(x=290, y=555) 
        
        # Keep the window open while the user is interacting with the widgets
        self.mainloop()

        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the stored data in the class attributes
        StandardCarabinerInspect.Delete_Carabiner_Data(self)
                        
        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)
        AutoBelay_Menu()           

    def Create_Check_Buttons(self, selectItems, checkListFrame, arrayObject, checkList, checkboxStates, callback, strInsType):
        """ 
        Function Name: Create_Check_Buttons
        Function Description: This helper method to create the checkbox buttons
        """
        if strInsType == "visual" or strInsType == "physical":
            maxColPerRow = 2
        else:
            maxColPerRow = 4

        for index, item in enumerate(selectItems):
            # Check if the item was previously selected (exists in arrayObject)
            is_selected = item in arrayObject
            var = tk.StringVar(value='1' if is_selected else '0')
            checkList.append(var)

            # Use a lambda function to capture the current item in the loop
            checkBox = tk.Checkbutton(checkListFrame, text=item, variable=var, onvalue='1', offvalue='0', 
                                    command=lambda item=item, var=var: callback(item, var))
            
            # Store the variable in the checkboxStates dictionary
            checkboxStates[item] = var

            # Calculate the row and column position of checkbutton based on index and max columns 
            rowPosition = index // maxColPerRow
            colPosition = index % maxColPerRow
            checkBox.grid(row=rowPosition, column=colPosition, sticky="w", padx=10)
            
    def Set_Previous_Checkbox_List(self, selectList, checkboxList, paramsList):
        """
        Function Name: Set_Vis_Previous_Checkbox_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the checkboxes from the cache array list for all checkboxes.
        """   
        # First check if the cache values have been assigned
        if len(selectList) == 0:
            # Check the first item of the list    
            checkboxList[0].set('1')
        else:
            # Set the Selection data to the objects in the window
            for i, item in enumerate(paramsList):
                if item in selectList:
                    checkboxList[i].set('1')

    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)

    def Get_VisCheckbox_List(self, item, var):
        """
        Function Name: Get_VisCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':            
            self.Update_Checkbox_List(self.visCheckList, item, self.checkboxVisStates, "visual", CarabVisSelection.astrCarabVisMetSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.visCheckList, item, self.checkboxVisStates, "visual", CarabVisSelection.astrCarabVisMetSelect)
            
    def Get_PhysCheckbox_List(self, item, var):
        """
        Function Name: Get_PhysCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':          
            self.Update_Checkbox_List(self.physCheckList, item, self.checkboxPhysStates, "physical", CarabPhysSelection.astrCarabPhysMetSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.physCheckList, item, self.checkboxPhysStates, "physical", CarabPhysSelection.astrCarabPhysMetSelect)

    def Get_FuncCheckbox_List(self, item, var):
        """
        Function Name: Get_FuncCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':          
            self.Update_Checkbox_List(self.functCheckList, item, self.checkboxFuncStates, "functional", CarabFunctSelection.astrCarabFunctSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.functCheckList, item, self.checkboxFuncStates, "functional", CarabFunctSelection.astrCarabFunctSelect)

    def Update_Checkbox_List(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Update_Checkbox_List
        Function Purpose: This function is a generalized method to update checkbox states and persistent data.
        """
        # Check if the first item is selected and deselect all remaining items
        if item == self.selectItems[0]:
            for selectedItem in checkboxList[1:]:
                selectedItem.set('0')
        # Check if any other item is selected and deselect the first item
        else:
            if checkboxList[0].get() == '1':
                checkboxList[0].set('0')

        # Check if the window section is functional
        if selectionKey == 'functional':
            # Update the checkbox states dictionary
            checkboxStates[item] = '1' if checkboxList[self.functItems.index(item)].get() == '1' else '0'
        else:
            # Update the checkbox states dictionary
            checkboxStates[item] = '1' if checkboxList[self.selectItems.index(item)].get() == '1' else '0'

        # Update the persistent data based on the updated checkbox states
        selectedItemsList = [item for item, state in checkboxStates.items() if state == '1']
        
        # Update the arrayObject with selectedItemsList        
        self.Update_Persistent_Array(arrayObject, selectedItemsList)

    def Handle_Deselection(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Handle_Deselection
        Function Purpose: This function is called when a checkbox is deselected.
        """
        # # For now, I'm just printing a message. You can modify this to implement the desired behavior.
        # print(f"Checkbox {item} was deselected!")

        # If you want to remove an item from a persisted list or dictionary upon deselection, you can do so here:
        checkboxStates.pop(item, None)
        arrayObject.remove(item)
        
    def Update_Persistent_Array(self, arrayObject, selectedItemsList):
        """
        Function Name: Update_Persistent_Array
        Function Description: This function updates the arrayObject with the selected items list, while keeping existing persisted data.
        """
        # print("Selected Items:", selectedItemsList)
        # print("Before update:", arrayObject)

        selectedSet = set(selectedItemsList)
        arraySet = set(arrayObject)

        # Find items to add and remove
        toAdd = selectedSet - arraySet
        toRemove = arraySet - selectedSet

        for item in toAdd:
            arrayObject.append(item)
        for item in toRemove:
            arrayObject.remove(item)

        # print("After update:", arrayObject) 

    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.', icon='warning')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate

    def Check_Checkbox_Input(lstCheckBox, strFieldDesc):
        """
        Function Name: Check_Checkbox_Input
        Function Purpose: This function is called whenever a checkbox is present and needs to check if any of the entries are empty. If so,
        warn the user.
        """    
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)
            
        try:
            for i in range(0, len(lstCheckBox)):
                if lstCheckBox[i].get() == '1':
                    # Set blnValidated to True
                    blnValidate = True

            # Check if the blnValidated flag is true or false and warn the user if the entire field is empty
            if blnValidate is True:
                pass
            else:
                messagebox.showwarning(title='ERROR', message='%s field should not be empty. Please verify your selection.'%(strFieldDesc), icon='warning')
                blnValidate = False
                # Select the first checkbox
                lstCheckBox[0].set('1')

        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate  

    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)  
        strVisField = str("Visual Result")
        strPhysField = str("Physical Result")
        strFunctField = str("Functional Result")

        # Check the user input
        blnValidate = CarabinerInspection.Check_Input(self.dropCarabType.get())

        # Check if the input is valid
        if (blnValidate is True):
            # Check the user input
            blnValidate = CarabinerInspection.Check_Input(self.dropCarabVisStatus.get())         
            
            # Check if the input is valid
            if (blnValidate is True):
                # Check the user input
                blnValidate = CarabinerInspection.Check_Input(self.dropCarabPhysStatus.get())         
                
                # Check if the input is valid
                if (blnValidate is True):
                    # Check the user input
                    blnValidate = CarabinerInspection.Check_Input(self.dropCarabFunctStatus.get())   

                    # Check if the input is valid
                    if (blnValidate is True):
                        # Check the user input
                        blnValidate = CarabinerInspection.Check_Checkbox_Input(self.visCheckList, strVisField)                                                                                                   
                        
                        # Check if the input is valid
                        if (blnValidate is True):
                            # Check the user input
                            blnValidate = CarabinerInspection.Check_Checkbox_Input(self.physCheckList, strPhysField)                                                                                                   
                            
                            # Check if the input is valid
                            if (blnValidate is True):
                                # Check the user input
                                blnValidate = CarabinerInspection.Check_Checkbox_Input(self.functCheckList, strFunctField)                                                                                                   
                                
                                # Check if the input is valid
                                if (blnValidate is True):
                                    blnValidate = True
                                else:
                                    # Return blnValidate as False
                                    blnValidate = False                                    
                            else:
                                # Return blnValidate as False
                                blnValidate = False                                
                        else:
                            # Return blnValidate as False
                            blnValidate = False
                    else:
                        # Return blnValidate as False
                        blnValidate = False
                        self.dropCarabFunctStatus.focus()
                else:
                    # Return blnValidate as False
                    blnValidate = False
                    self.dropCarabPhysStatus.focus()
            else:
                # Return blnValidate as False
                blnValidate = False
                self.dropCarabVisStatus.focus()                                                
        else:
            # Return blnValidate as False
            blnValidate = False
            self.dropCarabType.focus()

        return blnValidate 

    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        """       
        # Declare Local Variables
        sqlCarabVisSel = ("TCarabVisMetalSelects", "intCarabVisMetalSelectID", "strCarabVisMetSelect")
        sqlCarabPhysSel = ("TCarabPhysMetalSelects", "intCarabPhysMetalSelectID", "strCarabPhysMetSelect")
        sqlCarabFunctSel = ("TCarabFunctSelects", "intCarabFunctSelectID", "strCarabFunctSelect")
        sqlCarabVisIns = ("TCarabinerVisualInspections", "intCarabinerVisualID")
        sqlCarabPhysIns = ("TCarabinerPhysicalInspections", "intCarabinerPhysicalID") 
        sqlCarabFunctIns = ("TCarabinerFunctionInspections", "intCarabinerFunctionInspectID")
        sqlCarabStandIns = ("TStandardCarabinerInspections", "intStandardCarabinerInspectionID")

        # Check if the comment is empty. If not, pass in the values. If empty, pass in 'None'
        if self.commInput.get("1.0", "end-1c") != "":
            self.strComment = str(self.commInput.get("1.0", "end-1c"))
            self.strComment += "; "
            # Add the comment to the AutoBelay Comment object
            AutoBelayInspect.strComment = ''.join(self.strComment)
        else:
            self.strComment = 'None'
            AutoBelayInspect.strComment = self.strComment
        
        # Get the selection strings
        CarabinerType = self.dropCarabType.get()
        CarabVisMetSelect = self.Get_Combined_Selection(CarabVisSelection.astrCarabVisMetSelect, self.selectItems[0])
        CarabPhysMetSelect = self.Get_Combined_Selection(CarabPhysSelection.astrCarabPhysMetSelect, self.selectItems[0])
        CarabFunctSelect = self.Get_Combined_Selection(CarabPhysSelection.astrCarabPhysMetSelect, self.functItems[0])

        # # Display the string representation
        # print(CarabinerType)
        # print(CarabVisMetSelect) 
        # print(CarabPhysMetSelect)
        # print(CarabFunctSelect)
                
        # Get the status for the visual, physical, and functional selection 
        CarabVisStatus = self.dropCarabVisStatus.get()
        CarabPhysStatus = self.dropCarabPhysStatus.get()
        CarabFunctStatus = self.dropCarabFunctStatus.get()

        # Get the ID of the selected status item
        CarabVisStatusID = InspectionStatus.astrInspectionStatusDesc.index(CarabVisStatus) + 1
        CarabPhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(CarabPhysStatus) + 1
        CarabFunctStatusID = InspectionStatus.astrInspectionStatusDesc.index(CarabFunctStatus) + 1
        
        # Get the type of selection, either physical, functional, or visual
        VisInsTypeDesc = InspectionType.astrInspectionTypeDesc[0]
        PhysInsTypeDesc = InspectionType.astrInspectionTypeDesc[1]
        FunctInsTypeDesc = InspectionType.astrInspectionTypeDesc[2]

        # Get the ID of the selected Type item
        VisInsTypeID = InspectionType.astrInspectionTypeDesc.index(VisInsTypeDesc) + 1
        PhysInsTypeID = InspectionType.astrInspectionTypeDesc.index(PhysInsTypeDesc) + 1
        FunctInsTypeID = InspectionType.astrInspectionTypeDesc.index(FunctInsTypeDesc) + 1

        # Get the list of items selected and attach them to the selection object for Visual, Functional,and Physical Selection
        CarabVisMetalSelectID = self.Get_Or_Create_ID(CarabVisMetSelect, sqlCarabVisSel)              
        CarabPhysMetalSelectID = self.Get_Or_Create_ID(CarabPhysMetSelect, sqlCarabPhysSel)
        CarabFunctSelectID = self.Get_Or_Create_ID(CarabFunctSelect, sqlCarabFunctSel)

        # Get the ID's for the base objects in each class
        CarabinerID = Carabiner.astrCarabinerType.index(CarabinerType) + 1
        CarabinerVisualInspectID = self.Get_Max_Primary_Key(sqlCarabVisIns[0], sqlCarabVisIns[1])
        CarabinerPhysicalInspectID = self.Get_Max_Primary_Key(sqlCarabPhysIns[0], sqlCarabPhysIns[1])
        CarabinerFunctionInspectID = self.Get_Max_Primary_Key(sqlCarabFunctIns[0], sqlCarabFunctIns[1])
        StandardCarabinerInspectionID = self.Get_Max_Primary_Key(sqlCarabStandIns[0], sqlCarabStandIns[1])
        
        # Assign the local object to the class objects
        c = Carabiner(CarabinerID, CarabinerType)
        cvs = CarabVisSelection(CarabVisMetalSelectID, CarabVisMetSelect, CarabVisStatus)
        cps = CarabPhysSelection(CarabPhysMetalSelectID, CarabPhysMetSelect, CarabPhysStatus)
        cfs = CarabFunctSelection(CarabFunctSelectID, CarabFunctSelect, CarabFunctStatus)

        # Commit the data to the visual inspection
        Carabiner.strCarabinerType = c.strCarabinerType
        CarabVisSelection.intCarabVisMetalSelectID = cvs.intCarabVisMetalSelectID
        CarabVisSelection.strCarabVisMetSelect = cvs.strCarabVisMetSelect
        CarabVisSelection.strCarabVisStatus = cvs.strCarabVisStatus
        CarabinerVisualInspect.aCarabVisualCache = (CarabinerVisualInspectID, c.intCarabinerID, VisInsTypeID, cvs.intCarabVisMetalSelectID, CarabVisStatusID)

        # Commit the data to the physical inspection
        CarabPhysSelection.intCarabPhysMetalSelectID = cps.intCarabPhysMetalSelectID
        CarabPhysSelection.strCarabPhysMetSelect = cps.strCarabPhysMetSelect
        CarabPhysSelection.strCarabPhysStatus = cps.strCarabPhysStatus
        CarabinerPhysicalInspect.aCarabPhysicalCache = (CarabinerPhysicalInspectID, c.intCarabinerID, PhysInsTypeID, cps.intCarabPhysMetalSelectID, CarabPhysStatusID)    

        # Commit the data to the function inspection
        CarabFunctSelection.intCarabFunctSelectID = cfs.intCarabFunctSelectID
        CarabFunctSelection.strCarabFunctSelect = cfs.strCarabFunctSelect
        CarabFunctSelection.strCarabFunctStatus = cfs.strCarabFunctStatus
        CarabinerFunctionInspect.aCarabFunctCache = (CarabinerFunctionInspectID, c.intCarabinerID, FunctInsTypeID, cfs.intCarabFunctSelectID, CarabFunctStatusID)  

        # Commit the data to the standard inspection
        StandardCarabinerInspect.aStandardCarabInsCache = (StandardCarabinerInspectionID, CarabinerVisualInspectID, CarabinerPhysicalInspectID, CarabinerFunctionInspectID)

    def Get_Combined_Selection(self, persisted_array, default_value):
        """
        Function Name: Get_Combined_Selection
        Function Purpose: This function combines the array elements into a comma-separated string,
        and handles the case when the persisted array is empty by setting a default value.
        """
        if len(persisted_array) == 0:
            return default_value
        else:
            return ",".join(persisted_array)
        
    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
                        
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlStatement[0], sqlStatement[1]))    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
                    
    def Next(self):
        """ 
        Function Name: Next
        Function Purpose: This function is executed once the user clicks on the "Next" button. Once the inputs 
        are validated, the inspection results loads the user selected data and is retained at the object class locations 
        before committing to the database. If all inputs are valid and confirmed by the user, the next stage of inspections is executed.
        """
        global blnValidate
        blnValidate = bool(False)             
        
        # First check if the input is empty, if so, notify the user the input needs attention 
        blnValidate = self.Validate_InputFields()
        
        # If status is true then proceed to update the result field, else, reset the fields
        if blnValidate is True:
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to next inspection component?', icon='question') is True:
                # print(CarabVisSelection.astrCarabVisMetSelect)
                # print(CarabPhysSelection.astrCarabPhysMetSelect) 
                # print(CarabFunctSelection.astrCarabFunctSelect)
                # Load the user data and prep the data for db dump
                self.Pull_UserInput()     

                # Go to the next inspection component
                self.Next_Inspection()
            else:
                # Check if the user would like to reset the fields
                if messagebox.askyesno(message='ATTENTION! \n\n Would you like to reset the fields?', icon='question') is True:
                    # Clear the input fields and after data is submitted to the database
                    self.Clear()                

    def Clear(self):
        """ 
        Function Name: Clear
        Function Purpose: This function is executed once the user clicks on the Clear button inside the
        frame. If the user clicks 'Clear', all data is set back to default.
        """     
        # Set the list objects first element to the drop click object
        self.dropCarabType.set("")
        self.dropCarabVisStatus.set("")
        self.dropCarabPhysStatus.set("")
        self.dropCarabFunctStatus.set("")
        
        # Reset the checkboxes to empty selections
        BaseFunctions.Deselect_All_Checkbox(self.visCheckList)
        BaseFunctions.Deselect_All_Checkbox(self.physCheckList)
        BaseFunctions.Deselect_All_Checkbox(self.functCheckList)

        # Set the first item in the list to the first checkbox item displayed
        self.visCheckList[0].set('1')
        self.physCheckList[0].set('1')
        self.functCheckList[0].set('1')

        # Clear the class objects
        StandardCarabinerInspect.Reset_Carabiner_Data(self)
        StandardCarabinerInspect.Delete_Carabiner_Data(self)
        
        # Delete the comment field 
        self.commInput.delete("1.0", "end-1c") 

    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Expose the window widget to the user
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """     
        # Hide the current window
        self.Exit()  

        # Show the main window after the new window is closed
        AutoBelaySelection()

    def Next_Inspection(self):
        """ 
        Function Name: Next_Inspection
        Function Purpose: This function is executed once the user clicks on Next button to move to the nex inspection
        type window. Withdraw the parent window and load the new window.
        """           
        # Hide the main window
        self.Exit()  

        # Open the new window
        LanyardInspection()

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        
        
#######################################################################################################
# Lanyard Inspection Class
####################################################################################################### 

class LanyardInspection(tk.Tk):
    """
    Class Name: LanyardInspection
    Class Description: This class is to conduct lanyard inspections.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new lanyard inspection. User must click
        'Next' Button in order to progress to the next inspection type. A Visual, Physical, and Functional inspection
        must be performed to complete the inspection.
        """                
        # Load the data from the database
        # Start_Menu.Load_Obj_Lists(self) # Make sure to comment this out after testing
                
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (805/2)     
        self.y = (self.heightSize/2) - (600/2)          
        
        # Create the Window attributes  
        strUnitSelected = "Auto Belay Selected: %s"%(AutoBelay.strSerialNum)                 
        self.title("Lanyard Inspection - " + strUnitSelected)
        self.geometry('%dx%d+%d+%d' % (805, 600, self.x, self.y))
        self.resizable(False, False)

        # Create the frame fields
        self.typeFrame = tk.LabelFrame(self, text="Lanyard/Retractor Selection")
        self.typeFrame.place(x=95, y=10, width=620, height=80)
        self.visCheckListFrame = tk.LabelFrame(self, text="Visual Inspection Results")
        self.visCheckListFrame.place(x=95, y=100, width=310, height=200)
        self.physCheckListFrame = tk.LabelFrame(self, text="Physical Inspection Results")
        self.physCheckListFrame.place(x=405, y=100, width=310, height=200)
        self.functCheckListFrame = tk.LabelFrame(self, text="Functional Inspection Results")
        self.functCheckListFrame.place(x=95, y=310, width=620, height=125)
        self.commFrame = tk.LabelFrame(self, text="Inspection Comment")
        self.commFrame.place(x=95, y=440, width=620, height=100)
                
        # Create the label for the checkboxes
        self.lblLanyardLen = tk.Label(self.typeFrame, text="Lanyard Length:")
        self.lblLanyardVisualStatus = tk.Label(self.visCheckListFrame, text="Visual Status:")
        self.lblLanyardPhysicalStatus = tk.Label(self.physCheckListFrame, text="Physical Status:")
        self.lblRetractFunctStatus = tk.Label(self.functCheckListFrame, text="Function Status:")
                        
        # Create the label locations
        self.lblLanyardLen.place(x=120, y=20)
        self.lblLanyardVisualStatus.place(x=15, y=155)
        self.lblLanyardPhysicalStatus.place(x=15, y=155)
        self.lblRetractFunctStatus.place(x=155, y=65)

        # Create the drop down menu list for each attribute
        self.dropLanyardLen = ttk.Combobox(self.typeFrame, values=Lanyard.astrLanyardLength, state='readonly')
        self.dropLanyardVisStatus = ttk.Combobox(self.visCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropLanyardPhysStatus = ttk.Combobox(self.physCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropRetractFunctStatus = ttk.Combobox(self.functCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        
        # Create the drop down menu size for each attribute
        self.dropLanyardLen.configure(width=20)
        self.dropLanyardVisStatus.configure(width=20)
        self.dropLanyardPhysStatus.configure(width=20)
        self.dropRetractFunctStatus.configure(width=20)
        
        # Create the grid for the drop down menu list objects
        self.dropLanyardLen.place(x=240, y=20)   
        self.dropLanyardVisStatus.place(x=135, y=155)  
        self.dropLanyardPhysStatus.place(x=135, y=155)  
        self.dropRetractFunctStatus.place(x=290, y=65)  

        # Create the master list for the Textile and functional inspection types
        self.selectItems = Textile.astrTextileInspectionDesc        
        self.functItems = RetractorFunct.astrRetractFunctionDesc                                                                        
        
        # Create the checkbox lists for visual, physical, and functional
        self.visCheckList = [] 
        self.physCheckList = []
        self.functCheckList = []
        
        # Create an empty list to store selected items
        self.checkboxVisStates = {}
        self.checkboxPhysStates = {}
        self.checkboxFuncStates = {}

        # Create the checkbox list
        self.Create_Check_Buttons(self.selectItems, self.visCheckListFrame, LanyardVisSelection.astrLanVisTextSelect, self.visCheckList, self.checkboxVisStates, self.Get_VisCheckbox_List, "visual")
        self.Create_Check_Buttons(self.selectItems, self.physCheckListFrame, LanyardPhysSelection.astrLanPhysTextSelect, self.physCheckList, self.checkboxPhysStates, self.Get_PhysCheckbox_List, "physical")
        self.Create_Check_Buttons(self.functItems, self.functCheckListFrame, RetractFunctSelection.astrRetractFunctSelect, self.functCheckList, self.checkboxFuncStates, self.Get_FuncCheckbox_List, "functional")

        # First check if the selection values have been assigned
        self.Set_Previous_Checkbox_List(LanyardVisSelection.astrLanVisTextSelect, self.visCheckList, self.selectItems)
        self.Set_Previous_Checkbox_List(LanyardPhysSelection.astrLanPhysTextSelect, self.physCheckList, self.selectItems)
        self.Set_Previous_Checkbox_List(RetractFunctSelection.astrRetractFunctSelect, self.functCheckList, self.functItems)        
        
        # Check if the cache values for any drop menus have been previously selected and set the values
        if Bool_Flag.blnLanyardPersistFlag == True:
            self.Set_Previous_Drop_List(Lanyard.strLanyardLength, self.dropLanyardLen)
            self.Set_Previous_Drop_List(LanyardVisSelection.strLanVisStatus, self.dropLanyardVisStatus)
            self.Set_Previous_Drop_List(LanyardPhysSelection.strLanPhysStatus, self.dropLanyardPhysStatus)
            self.Set_Previous_Drop_List(RetractFunctSelection.strRetractStatus, self.dropRetractFunctStatus)

        # Create the comment field
        self.commInput = tk.Text(self.commFrame, state='normal')
        self.commInput.grid(row=0, column=0, padx=5, pady=4)
        self.commInput.configure(width=75, height=4, padx=1)
        
        # Create the buttons
        self.btnBack = tk.Button(self, text="Back", width=10, command=self.Back)
        self.btnClear = tk.Button(self, text="Clear", width=10, command=self.Clear)
        self.btnExit = tk.Button(self, text="Exit", width=10, command=self.Exit)
        self.btnNext = tk.Button(self, text="Next", width=10, command=self.Next)
        self.btnAddLanLen = tk.Button(self.typeFrame, text="Add New Length", width=5, command=self.Add_Lanyard_Length)
            
        # Create the position of the button
        self.btnBack.place(x=170, y=555)
        self.btnExit.place(x=300, y=555)
        self.btnClear.place(x=430, y=555)
        self.btnNext.place(x=560, y=555) 
        self.btnAddLanLen.place(x=420, y=17, width=150) 
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()
        
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the stored data in the class attributes
        StandardCarabinerInspect.Delete_Carabiner_Data(self)
        StandardLanyardInspect.Delete_Lanyard_Data(self)

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)
        AutoBelay_Menu()    
        
    def Create_Check_Buttons(self, selectItems, checkListFrame, arrayObject, checkList, checkboxStates, callback, strInsType):
        """ 
        Function Name: Create_Check_Buttons
        Function Description: This helper method to create the checkbox buttons
        """
        if strInsType == "visual" or strInsType == "physical":
            maxColPerRow = 2
        else:
            maxColPerRow = 4

        for index, item in enumerate(selectItems):
            # Check if the item was previously selected (exists in arrayObject)
            is_selected = item in arrayObject
            var = tk.StringVar(value='1' if is_selected else '0')
            checkList.append(var)

            # Use a lambda function to capture the current item in the loop
            checkBox = tk.Checkbutton(checkListFrame, text=item, variable=var, onvalue='1', offvalue='0', 
                                    command=lambda item=item, var=var: callback(item, var))
            
            # Store the variable in the checkboxStates dictionary
            checkboxStates[item] = var

            # Calculate the row and column position of checkbutton based on index and max columns 
            rowPosition = index // maxColPerRow
            colPosition = index % maxColPerRow
            checkBox.grid(row=rowPosition, column=colPosition, sticky="w", padx=12)
            
    def Set_Previous_Checkbox_List(self, selectList, checkboxList, paramsList):
        """
        Function Name: Set_Vis_Previous_Checkbox_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the checkboxes from the cache array list for all checkboxes.
        """   
        # First check if the cache values have been assigned
        if len(selectList) == 0:
            # Check the first item of the list    
            checkboxList[0].set('1')
        else:
            # Set the Selection data to the objects in the window
            for i, item in enumerate(paramsList):
                if item in selectList:
                    checkboxList[i].set('1')

    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)

    def Get_VisCheckbox_List(self, item, var):
        """
        Function Name: Get_VisCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':            
            self.Update_Checkbox_List(self.visCheckList, item, self.checkboxVisStates, "visual", LanyardVisSelection.astrLanVisTextSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.visCheckList, item, self.checkboxVisStates, "visual", LanyardVisSelection.astrLanVisTextSelect)
            
    def Get_PhysCheckbox_List(self, item, var):
        """
        Function Name: Get_PhysCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':          
            self.Update_Checkbox_List(self.physCheckList, item, self.checkboxPhysStates, "physical", LanyardPhysSelection.astrLanPhysTextSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.physCheckList, item, self.checkboxPhysStates, "physical", LanyardPhysSelection.astrLanPhysTextSelect)

    def Get_FuncCheckbox_List(self, item, var):
        """
        Function Name: Get_FuncCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':          
            self.Update_Checkbox_List(self.functCheckList, item, self.checkboxFuncStates, "functional", RetractFunctSelection.astrRetractFunctSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.functCheckList, item, self.checkboxFuncStates, "functional", RetractFunctSelection.astrRetractFunctSelect)

    def Update_Checkbox_List(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Update_Checkbox_List
        Function Purpose: This function is a generalized method to update checkbox states and persistent data.
        """
        # Check if the first item is selected and deselect all remaining items
        if item == self.selectItems[0]:
            for selectedItem in checkboxList[1:]:
                selectedItem.set('0')
        # Check if any other item is selected and deselect the first item
        else:
            if checkboxList[0].get() == '1':
                checkboxList[0].set('0')

        # Check if the window section is functional
        if selectionKey == 'functional':
            # Update the checkbox states dictionary
            checkboxStates[item] = '1' if checkboxList[self.functItems.index(item)].get() == '1' else '0'
        else:
            # Update the checkbox states dictionary
            checkboxStates[item] = '1' if checkboxList[self.selectItems.index(item)].get() == '1' else '0'

        # Update the persistent data based on the updated checkbox states
        selectedItemsList = [item for item, state in checkboxStates.items() if state == '1']
        
        # Update the arrayObject with selectedItemsList        
        self.Update_Persistent_Array(arrayObject, selectedItemsList)

    def Handle_Deselection(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Handle_Deselection
        Function Purpose: This function is called when a checkbox is deselected.
        """
        # # For now, I'm just printing a message. You can modify this to implement the desired behavior.
        # print(f"Checkbox {item} was deselected!")

        # If you want to remove an item from a persisted list or dictionary upon deselection, you can do so here:
        checkboxStates.pop(item, None)
        arrayObject.remove(item)
        
    def Update_Persistent_Array(self, arrayObject, selectedItemsList):
        """
        Function Name: Update_Persistent_Array
        Function Description: This function updates the arrayObject with the selected items list, while keeping existing persisted data.
        """
        # print("Selected Items:", selectedItemsList)
        # print("Before update:", arrayObject)

        selectedSet = set(selectedItemsList)
        arraySet = set(arrayObject)

        # Find items to add and remove
        toAdd = selectedSet - arraySet
        toRemove = arraySet - selectedSet

        for item in toAdd:
            arrayObject.append(item)
        for item in toRemove:
            arrayObject.remove(item)

        # print("After update:", arrayObject) 
        
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(message='ERROR \n\n Input should not be empty. Please Try again.', icon='warning')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(message='ERROR \n\n Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate

    def Check_Checkbox_Input(lstCheckBox, strFieldDesc):
        """
        Function Name: Check_Checkbox_Input
        Function Purpose: This function is called whenever a checkbox is present and needs to check if any of the entries are empty. If so,
        warn the user.
        """    
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)
            
        try:
            for i in range(0, len(lstCheckBox)):
                if lstCheckBox[i].get() == '1':
                    # Set blnValidated to True
                    blnValidate = True

            # Check if the blnValidated flag is true or false and warn the user if the entire field is empty
            if blnValidate is True:
                pass
            else:
                messagebox.showwarning(message='ERROR \n\n %s field should not be empty. Please verify your selection.'%(strFieldDesc), icon='warning')
                blnValidate = False
                # Select the first checkbox
                lstCheckBox[0].set('1')

        except ValueError:
            messagebox.showwarning(message='ERROR \n\n Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate

    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)  
        strVisField = str("Visual Result")
        strPhysField = str("Physical Result")
        strFunctField = str("Functional Result")

        # Check the user input
        blnValidate = LanyardInspection.Check_Input(self.dropLanyardLen.get())

        # Check if the input is valid
        if (blnValidate is True):
            # Check the user input
            blnValidate = LanyardInspection.Check_Input(self.dropLanyardVisStatus.get())

            # Check if the input is valid
            if (blnValidate is True):
                # Check the user input
                blnValidate = LanyardInspection.Check_Input(self.dropLanyardPhysStatus.get())                             

                # Check if the input is valid
                if (blnValidate is True):
                    # Check the user input
                    blnValidate = LanyardInspection.Check_Input(self.dropRetractFunctStatus.get())  

                    # Check if the input is valid
                    if (blnValidate is True):
                        # Check the user input
                        blnValidate = LanyardInspection.Check_Checkbox_Input(self.visCheckList, strVisField)                                                                                                   
                        
                        # Check if the input is valid
                        if (blnValidate is True):
                            # Check the user input
                            blnValidate = LanyardInspection.Check_Checkbox_Input(self.physCheckList, strPhysField)                                                                                                   
                            
                            # Check if the input is valid
                            if (blnValidate is True):
                                # Check the user input
                                blnValidate = LanyardInspection.Check_Checkbox_Input(self.functCheckList, strFunctField)                                                                                                   
                                
                                # Check if the input is valid
                                if (blnValidate is True):
                                    blnValidate = True
                                else:
                                    # Return blnValidate as False
                                    blnValidate = False                                    
                            else:
                                # Return blnValidate as False
                                blnValidate = False                                
                        else:
                            # Return blnValidate as False
                            blnValidate = False
                    else:
                        # Return blnValidate as False
                        blnValidate = False
                        self.dropRetractFunctStatus.focus()
                else:
                    # Return blnValidate as False
                    blnValidate = False
                    self.dropLanyardPhysStatus.focus()
            else:
                # Return blnValidate as False
                blnValidate = False
                self.dropLanyardVisStatus.focus()                                                
        else:
            # Return blnValidate as False
            blnValidate = False
            self.dropLanyardLen.focus()

        return blnValidate 

    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        """   
        # Declare Local Variables
        sqlLanVisSel = ("TLanVisTextSelects", "intLanVisTextSelectID", "strLanVisTextSelect")
        sqlLanPhysSel = ("TLanPhysTextSelects", "intLanPhysTextSelectID", "strLanPhysTextSelect")
        sqlLanFunctSel = ("TRetractFunctSelects", "intRetractFunctSelectID", "strRetractFunctSelect")
        sqlLanVisIns = ("TLanyardVisualInspections", "intLanyardVisualInspectionID")
        sqlLanPhysIns = ("TLanyardPhysicalInspections", "intLanyardPhysicalInspectionID") 
        sqlLanFunctIns = ("TLanyardRetractFunctionInspections", "intLanyardRetractFunctionInspectionID")
        sqlLanStandIns = ("TStandardLanyardInspections", "intStandardLanyardInspectionID")

        # Check if the comment is empty. If not, pass in the values. IF empty, pass in 'None'
        if self.commInput.get("1.0", "end-1c") != "":
            self.strComment = str(self.commInput.get("1.0", "end-1c"))
            self.strComment += "; "
            # Add the comment to the AutoBelay Comment object
            AutoBelayInspect.strComment = ''.join(self.strComment)
        else:
            self.commInput = 'None' 
            AutoBelayInspect.strComment = self.commInput
        
        # Get the selection strings
        LanyardLength = self.dropLanyardLen.get()
        LanVisTextSelect = self.Get_Combined_Selection(LanyardVisSelection.astrLanVisTextSelect, self.selectItems[0])
        LanPhysTextSelect = self.Get_Combined_Selection(LanyardPhysSelection.astrLanPhysTextSelect, self.selectItems[0])
        RetractFunctSelect = self.Get_Combined_Selection(RetractFunctSelection.astrRetractFunctSelect, self.functItems[0])

        # # Display the string representation
        # print(LanyardLength)
        # print(LanVisTextSelect) 
        # print(LanPhysTextSelect)
        # print(RetractFunctSelect)

        # Get the status for the visual, physical, and functional selection                
        LanyardVisStatus = self.dropLanyardVisStatus.get()
        LanyardPhysStatus = self.dropLanyardPhysStatus.get()
        LanyardFunctStatus = self.dropRetractFunctStatus.get()

        # Get the ID of the selected status item
        LanyardVisStatusID = InspectionStatus.astrInspectionStatusDesc.index(LanyardVisStatus) + 1
        LanyardPhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(LanyardPhysStatus) + 1
        LanyardFunctStatusID = InspectionStatus.astrInspectionStatusDesc.index(LanyardFunctStatus) + 1
        
        # Get the type of selection, either physical, functional, or visual
        VisInsTypeDesc = InspectionType.astrInspectionTypeDesc[0]
        PhysInsTypeDesc = InspectionType.astrInspectionTypeDesc[1]
        FunctInsTypeDesc = InspectionType.astrInspectionTypeDesc[2]

        # Get the ID of the selected Type item
        VisInsTypeID = InspectionType.astrInspectionTypeDesc.index(VisInsTypeDesc) + 1
        PhysInsTypeID = InspectionType.astrInspectionTypeDesc.index(PhysInsTypeDesc) + 1
        FunctInsTypeID = InspectionType.astrInspectionTypeDesc.index(FunctInsTypeDesc) + 1

        # Get the list of items selected and attach them to the selection object for Visual and Physical Selection
        LanVisTextSelectID = self.Get_Or_Create_ID(LanVisTextSelect, sqlLanVisSel)              
        LanPhysTextSelectID = self.Get_Or_Create_ID(LanPhysTextSelect, sqlLanPhysSel)
        RetractFunctSelectID = self.Get_Or_Create_ID(RetractFunctSelect, sqlLanFunctSel)
        
        # Get the ID's for the base objects in each class
        LanyardID = Lanyard.astrLanyardLength.index(LanyardLength) + 1
        LanyardVisualInspectionID = self.Get_Max_Primary_Key(sqlLanVisIns[0], sqlLanVisIns[1])
        LanyardPhysicalInspectionID = self.Get_Max_Primary_Key(sqlLanPhysIns[0], sqlLanPhysIns[1])
        LanyardRetractFunctionInspectionID = self.Get_Max_Primary_Key(sqlLanFunctIns[0], sqlLanFunctIns[1])
        StandardLanyardInspectionID = self.Get_Max_Primary_Key(sqlLanStandIns[0], sqlLanStandIns[1])
                
        # Assign the local object to the class objects        
        l = Lanyard(LanyardID, LanyardLength)
        lvs = LanyardVisSelection(LanVisTextSelectID, LanVisTextSelect, LanyardVisStatus)
        lps = LanyardPhysSelection(LanPhysTextSelectID, LanPhysTextSelect, LanyardPhysStatus)
        rfs = RetractFunctSelection(RetractFunctSelectID, RetractFunctSelect, LanyardFunctStatus)

        # Commit the data to the visual inspection
        Lanyard.intLanyardID = l.intLanyardID
        Lanyard.strLanyardLength = l.strLanyardLength      
        LanyardVisSelection.intLanVisTextSelectID = lvs.intLanVisTextSelectID
        LanyardVisSelection.strLanVisTextSelect = lvs.strLanVisTextSelect 
        LanyardVisSelection.strLanVisStatus = lvs.strLanVisStatus
        LanyardVisualInspect.aLanyardVisualCache = (LanyardVisualInspectionID, l.intLanyardID, VisInsTypeID, lvs.intLanVisTextSelectID, LanyardVisStatusID)

        # Commit the data to the physical inspection
        LanyardPhysSelection.intLanPhysTextSelectID = lps.intLanPhysTextSelectID
        LanyardPhysSelection.strLanPhysTextSelect = lps.strLanPhysTextSelect 
        LanyardPhysSelection.strLanPhysStatus = lps.strLanPhysStatus
        LanyardPhysicalInspect.aLanyardPhysicalCache = (LanyardPhysicalInspectionID, l.intLanyardID, PhysInsTypeID, lps.intLanPhysTextSelectID, LanyardPhysStatusID)    

        # Commit the data to the function inspection
        RetractFunctSelection.intRetractFunctSelectID = rfs.intRetractFunctSelectID
        RetractFunctSelection.strRetractFunctSelect = rfs.strRetractFunctSelect         
        RetractFunctSelection.strRetractStatus = rfs.strRetractStatus
        LanyardFunctionInspect.aLanyardFunctCache = (LanyardRetractFunctionInspectionID, l.intLanyardID, FunctInsTypeID, rfs.intRetractFunctSelectID, LanyardFunctStatusID)  

        # Commit the data to the standard inspection
        StandardLanyardInspect.aStandardLanyardInsCache = (StandardLanyardInspectionID, LanyardVisualInspectionID, LanyardPhysicalInspectionID, LanyardRetractFunctionInspectionID)

    def Get_Combined_Selection(self, persisted_array, default_value):
        """
        Function Name: Get_Combined_Selection
        Function Purpose: This function combines the array elements into a comma-separated string,
        and handles the case when the persisted array is empty by setting a default value.
        """
        if len(persisted_array) == 0:
            return default_value
        else:
            return ",".join(persisted_array)
        
    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
                        
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlStatement[0], sqlStatement[1]))    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
                                    
    def Next(self):
        """ 
        Function Name: Next
        Function Purpose: This function is executed once the user clicks on the "Next" button. Once the inputs 
        are validated, the inspection results loads the user selected data and is retained at the object class locations 
        before committing to the database. If all inputs are valid and confirmed by the user, the next stage of inspections is executed.
        """
        global blnValidate
        blnValidate = bool(False)             
        
        # First check if the input is empty, if so, notify the user the input needs attention 
        blnValidate = self.Validate_InputFields()
        
        # If status is true then proceed to update the result field, else, reset the fields
        if (blnValidate is True):
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to next inspection component?', icon='question') is True:  
                # print(LanyardVisSelection.astrLanVisTextSelect)
                # print(LanyardPhysSelection.astrLanPhysTextSelect) 
                # print(RetractFunctSelection.astrRetractFunctSelect)                   
                # Load the user data and prep the data for db dump
                self.Pull_UserInput()      

                # Go to the next inspection component
                self.Next_Inspection()

            else:
                # Check if the user would like to reset the fields
                if messagebox.askyesno(message='ATTENTION! \n\n Would you like to reset the fields?', icon='question') is True:
                    # Clear the input fields and after data is submitted to the database
                    self.Clear(self)                

    def Clear(self):
        """ 
        Function Name: Clear
        Function Purpose: This function is executed once the user clicks on the Clear button inside the root
        frame. If the user clicks 'Clear', all data is set back to default.
        """     
        # Set the list objects first element to the drop click object
        self.dropLanyardLen.set("")
        self.dropLanyardVisStatus.set("")
        self.dropLanyardPhysStatus.set("")
        self.dropRetractFunctStatus.set("")

        # Reset the checkboxes to empty selections
        BaseFunctions.Deselect_All_Checkbox(self.visCheckList)  
        BaseFunctions.Deselect_All_Checkbox(self.physCheckList) 
        BaseFunctions.Deselect_All_Checkbox(self.functCheckList)

        # Set the first item in the list to the first checkbox item displayed
        self.visCheckList[0].set('1')
        self.physCheckList[0].set('1')
        self.functCheckList[0].set('1')

        # Clear the class objects
        StandardLanyardInspect.Reset_Lanyard_Data(self)
        StandardLanyardInspect.Delete_Lanyard_Data(self)
        
        # Delete the comment field 
        self.commInput.delete("1.0", "end-1c") 

    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the root
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Hide the current window
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """     
        # Hide the current window
        self.Exit()  

        # Show the main window after the new window is closed
        CarabinerInspection()

    def Update_Dropdown_Values(self):
        """ 
        Function Name: Update_Dropdown_Values
        Function Purpose: This function is executed once the user clicks on AddLanyard button and updates the drop down
        object list with the new values.
        """             
        self.dropLanyardLen['values'] = Lanyard.astrLanyardLength

    def Add_Lanyard_Length(self):
        """ 
        Function Name: Add_Lanyard_Length
        Function Purpose: This function is executed once the user clicks on AddLanyard button and updates the drop down
        object list with the new values.
        """           
        # Hide the main window
        self.Withdraw()  

        # Call your AddLanyardLen function here
        newWindow = AddLanyardLen(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Show the main window after the new window is closed
        self.Deiconify()  

        # Update the drop-down menu values
        self.Update_Dropdown_Values()

    def Next_Inspection(self):
        """ 
        Function Name: Next_Inspection
        Function Purpose: This function is executed once the user clicks on Next button to move to the nex inspection
        type window. Withdraw the parent window and load the new window.
        """           
        # Hide the main window
        self.Exit()  

        # Open the new window
        CaseInspection()

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the window is destroyed, and the user is sent back to the main menu 
        """         
        self.destroy()
        

#######################################################################################################
# Lanyard Length Class
####################################################################################################### 
        
class AddLanyardLen(tk.Toplevel, Lanyard):
    """
    Class Name: AddLanyardLen
    Class Description: This class adds a New Lanyard Length to the database.
    """
    def __init__(self, parent):    
        # Initialize the Toplevel window
        super().__init__(parent)

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk window 
        self.x = (self.widthSize/2) - (400/2)     
        self.y = (self.heightSize/2) - (120/2)          
        
        # Set the window attributes
        self.title("Add New Lanyard Length")
        self.geometry('%dx%d+%d+%d' % (400, 120, self.x, self.y))
        self.resizable(False, False)

        # Create the frame to hold the input fields
        self.frameInput = tk.LabelFrame(self, text="Lanyard Credentials")
        self.frameInput.place(x=35, y=10, width=330, height=90)

        # Create the labels 
        self.lblLanyardLen = tk.Label(self.frameInput, text="Lanyard Length (ft):")
        self.lblLanyardLen.grid(row=0, column=0, padx=15, pady=2, sticky='W')

        # Create the entry input box
        self.LanyardLenInput = tk.Entry(self.frameInput, width=25)
        self.LanyardLenInput.grid(row=0, column=1, padx=10, pady=2)
        
        # Create the buttons
        self.btnExit = tk.Button(self.frameInput, text="Back", width=10, command=self.Exit)
        self.btnReset = tk.Button(self.frameInput, text="Reset", width=10, command=self.Reset)
        self.btnSubmit = tk.Button(self.frameInput, text="Submit", width=10, command=self.Submit)

        # Position the buttons
        self.btnExit.place(x=20, y=35)
        self.btnReset.place(x=120, y=35)
        self.btnSubmit.place(x=220, y=35)

    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate

    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        # Check the user input
        blnValidate = AddLanyardLen.Check_Input(self.LanyardLenInput.get())            
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check the user input
            blnValidate = BaseFunctions.Validate_StringNumeric_Input(self.LanyardLenInput.get())

            # Check if the input is valid
            if (blnValidate is True):
                # Configure the lanyard length
                self.strLanyardLength = str(self.LanyardLenInput.get()) + str("ft")
                
                # Check if the input is valid
                if self.strLanyardLength not in Lanyard.astrLanyardLength:
                    # Get the next primary key ID for the new lanyard length
                    Lanyard.intLanyardID = Queries.Get_MaxPrimaryKeys(Queries, "TLanyards", "intLanyardID")                                                            
                    blnValidate = True      
                else:      
                    # Return blnValidate as False
                    messagebox.showwarning(title='INVALID INPUT', message='%s already exists. Please enter another input.'%(self.strLanyardLength))
                    blnValidate = False         
                    self.LanyardLenInput.delete(0, END)
                    self.LanyardLenInput.configure(background='Yellow')
                    self.LanyardLenInput.focus()             
            else:
                # Return blnValidate as False
                blnValidate = False         
                self.LanyardLenInput.delete(0, END)
                self.LanyardLenInput.configure(background='Yellow')
                self.LanyardLenInput.focus()                                                                    
        else:
            # Return blnValidate as False
            blnValidate = False
            self.LanyardLenInput.delete(0, END)
            self.LanyardLenInput.configure(background='Yellow')
            self.LanyardLenInput.focus()           

        return blnValidate                                                

    def Clear_BG_Color(self):
        """ 
        Function Name: Clear_BG_Color
        Function Purpose: This button executes when the user submits their entries and clears the background
        color before any validation checks.
        """
        # Delete the button after submission
        self.LanyardLenInput.configure(background='White')
        
    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This button executes when the user wants to reset the values.
        """
        # Delete the button after submission
        self.LanyardLenInput.delete(0, END)     
        
        # Clear out the background colors and set to default as 'white'
        AddLanyardLen.Clear_BG_Color(self)

        # Reload the data after user submits entry
        Lanyard.Delete_Lanyard_Data(Lanyard)
        Lanyard.Get_Lanyard_Data(Lanyard)
        
    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the new location to the db. Else, reset
        """
        # Check if all of the inputs are valid
        global blnValidate 
        blnValidate = bool(False)
        
        # Clear out the background colors and set to default as 'white'
        AddLanyardLen.Clear_BG_Color(self)
                
        # Get the blnValidate status
        blnValidate = AddLanyardLen.Validate_InputFields(self)
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message=('CAUTION! \n\n Proceed to add new lanyard length: %s?')%(self.strLanyardLength)) is True:     
                # Load the user data and prep the data for db dump
                Lanyard.Add_LanyardLen_Query(self)                     
                
                # Check if the user would like to add another lanyard length
                if messagebox.askyesno(message='SUCCESSFUL UPLOAD! \n\n Would you like to add another lanyard length?') is True:
                    # Clear the input fields and after data is submitted to the database
                    AddLanyardLen.Reset(self)
                else:
                    AddLanyardLen.Exit(self)
            else:
                pass  

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        # Load the data from the database
        Lanyard.Delete_Lanyard_Data(Lanyard)
        Lanyard.Get_Lanyard_Data(Lanyard)        
        self.destroy()
        

#######################################################################################################
# Brake Housing Inspection Class
#######################################################################################################

class BrakeInspection(tk.Tk):
    """
    Class Name: BrakeInspection
    Class Description: This class is to conduct Brake inspections.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new Brake inspection. User must click
        'Next' Button in order to progress to the next inspection type. A Visual and Physical inspection
        must be performed to complete the inspection.
        """
        # Create the root tkinter variable
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (805/2)     
        self.y = (self.heightSize/2) - (600/2)          
        
        # Create the Window attributes          
        strUnitSelected = "Auto Belay Selected: %s"%(AutoBelay.strSerialNum)                                
        self.title("Brake Housing Inspection - " + strUnitSelected)      
        self.geometry('%dx%d+%d+%d' % (805, 600, self.x, self.y))
        self.resizable(False, False)

        # Create the frame fields
        self.typeFrame = tk.LabelFrame(self, text="Component Selection")
        self.typeFrame.place(x=95, y=10, width=610, height=210)
        self.visCheckListFrame = tk.LabelFrame(self, text="Visual Inspection Results")
        self.visCheckListFrame.place(x=95, y=230, width=300, height=200)
        self.physCheckListFrame = tk.LabelFrame(self, text="Physical Inspection Results")
        self.physCheckListFrame.place(x=405, y=230, width=300, height=200)
        self.commFrame = tk.LabelFrame(self, text="Inspection Comment")
        self.commFrame.place(x=95, y=440, width=610, height=100)

        # Create the listBox
        self.listBox = tk.Listbox(self.typeFrame)
        self.listBox.place(x=35, y=25, width=220, height=160)

        # Add some items to the listBox in alphabetical order
        self.comSelectItems = BrakeHousing.astrBrakeComponentDesc
        for item in self.comSelectItems[1:]:
            self.listBox.insert(tk.END, item)
            
        # Create a second listBox to hold removed items
        self.removeListBox = tk.Listbox(self.typeFrame)
        self.removeListBox.place(x=350, y=25, width=220, height=160)

        # Replace list with the first object in the primary list
        self.removeListBox.insert(tk.END, self.comSelectItems[0])
        
        # Create the list array for the remove Listbox
        self.removeListItems = []
        self.removeListItems = [self.removeListBox.get(i) for i in range(self.removeListBox.size())]      

        # Bind double-click event to listBox
        self.listBox.bind("<Double-Button-1>", self.on_double_click)
                        
        # Bind double-click event to the removed items listBox
        self.removeListBox.bind("<Double-Button-1>", self.on_removed_double_click)                        
                        
        # Create the label for the checkboxes
        self.lblDefaultComp = tk.Label(self.typeFrame, text="Affected Items")
        self.lblFinalComp = tk.Label(self.typeFrame, text="Selected Items")
        self.lblBrakeVisualStatus = tk.Label(self.visCheckListFrame, text="Visual Status:")
        self.lblBrakePhysicalStatus = tk.Label(self.physCheckListFrame, text="Physical Status:")
                        
        # Create the label locations
        self.lblDefaultComp.place(x=110, y=1)
        self.lblFinalComp.place(x=430, y=1)
        self.lblBrakeVisualStatus.place(x=5, y=140)
        self.lblBrakePhysicalStatus.place(x=5, y=140)

        # Create the drop down menu list for each attribute
        self.dropBrakeVisStatus = ttk.Combobox(self.visCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropBrakePhysStatus = ttk.Combobox(self.physCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly') 
        
        # Create the drop down menu size for each attribute
        self.dropBrakeVisStatus.configure(width=20)
        self.dropBrakePhysStatus.configure(width=20)
        
        # Create the grid for the drop down menu list objects
        self.dropBrakeVisStatus.place(x=130, y=140)  
        self.dropBrakePhysStatus.place(x=130, y=140)  

        # Create the master list for the metallic and functional inspection types
        self.selectItems = Metallic.astrMetallicInspectionDesc

        # Create the checkbox lists for visual, physical, and functional
        self.visCheckList = [] 
        self.physCheckList = []

        # Create a dictionary to track checkbox states
        self.checkboxVisStates = {}
        self.checkboxPhysStates = {}

        # Create the checkbox list
        self.Create_Check_Buttons(self.selectItems, self.visCheckListFrame, BrakeVisSelection.astrBrakeVisMetSelect, self.visCheckList, self.checkboxVisStates, self.Get_VisCheckbox_List)
        self.Create_Check_Buttons(self.selectItems, self.physCheckListFrame, BrakePhysSelection.astrBrakePhysMetSelect, self.physCheckList, self.checkboxPhysStates, self.Get_PhysCheckbox_List)

        # First check if the selection values have been assigned
        self.Set_Previous_Checkbox_List(BrakeVisSelection.astrBrakeVisMetSelect, self.visCheckList, self.selectItems)                
        self.Set_Previous_Checkbox_List(BrakePhysSelection.astrBrakePhysMetSelect, self.physCheckList, self.selectItems)                                        
                                
       # Check if the cache values for any drop menus have been previously selected and set the values
        if Bool_Flag.blnBrakePersistFlag == True:
            self.Set_Previous_ListBox(BrakeCompSelection.strBrakeCompSelect)
            self.Set_Previous_Drop_List(BrakeVisSelection.strBrakeVisStatus, self.dropBrakeVisStatus)
            self.Set_Previous_Drop_List(BrakePhysSelection.strBrakePhysStatus, self.dropBrakePhysStatus)            
        
        # Create the comment field
        self.commInput = Text(self.commFrame, state='normal')
        self.commInput.grid(row=0, column=0, padx=5, pady=4)
        self.commInput.configure(width=74, height=4, padx=0)
        
        # Create the buttons
        self.btnBack = Button(self, text="Back", width=10, command=self.Back)
        self.btnClear = Button(self, text="Clear", width=10, command=self.Clear)
        self.btnExit = Button(self, text="Exit", width=10, command=self.Exit)
        self.btnNext = Button(self, text="Next", width=10, command=self.Next)
        self.btnReset = Button(self.typeFrame, text="Reset", width=10, command=self.Reset)
            
        # Create the position of the button
        self.btnBack.place(x=160, y=555)
        self.btnClear.place(x=420, y=555)
        self.btnNext.place(x=550, y=555) 
        self.btnExit.place(x=290, y=555) 
        self.btnReset.place(x=263, y=90) 

        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()

        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the stored data in the class attributes
        StandardCarabinerInspect.Delete_Carabiner_Data(self)
        StandardLanyardInspect.Delete_Lanyard_Data(self)
        StandardCaseInspect.Delete_Case_Data(self)
        StandardBrakeInspect.Delete_Brake_Data(self)

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)
        AutoBelay_Menu()    
        
    def Create_Check_Buttons(self, selectItems, checkListFrame, arrayObject, checkList, checkboxStates, callback):
        """ 
        Function Name: Create_Check_Buttons
        Function Description: This helper method to create the checkbox buttons
        """
        maxColPerRow = 2

        for index, item in enumerate(selectItems):
            # Check if the item was previously selected (exists in arrayObject)
            is_selected = item in arrayObject
            var = tk.StringVar(value='1' if is_selected else '0')
            checkList.append(var)

            # Use a lambda function to capture the current item in the loop
            checkBox = tk.Checkbutton(checkListFrame, text=item, variable=var, onvalue='1', offvalue='0', 
                                    command=lambda item=item, var=var: callback(item, var))
            
            # Store the variable in the checkboxStates dictionary
            checkboxStates[item] = var

            # Calculate the row and column position of checkbutton based on index and max columns 
            rowPosition = index // maxColPerRow
            colPosition = index % maxColPerRow
            checkBox.grid(row=rowPosition, column=colPosition, sticky="w")
            
    def on_double_click(self, event):
        """
        Function Name: on_double_click
        Function Purpose: This function Set event trigger function for double-click actions for the removed items listBox
        """   
        # Get selected item from listBox
        widget = event.widget
        selection = widget.curselection()
        selected_item = widget.get(selection[0])

        # Always remove the selected item from the listBox
        widget.delete(selection[0])

        if selected_item != self.comSelectItems[0]:  # Check if selected item is not the first item
            # If the first item of comSelectItems is present in removeListItems, then move it to listBox
            if self.comSelectItems[0] in self.removeListItems:
                self.removeListBox.delete(0)
                self.listBox.insert(0, self.comSelectItems[0])
            
            # Add the removed item to removeListBox
            self.removeListBox.insert(tk.END, selected_item)
        else:
            # If the selected item is the first item, reset the listBox
            self.Reset()
        
        # Always update the removeListItems and persistent data after making changes
        self.removeListItems = [self.removeListBox.get(i) for i in range(self.removeListBox.size())]
        self.Update_Persistent_Array(BrakeCompSelection.astrBrakeCompSelect, self.removeListItems)     
                    
    def on_removed_double_click(self, event):
        """
        Function Name: on_removed_double_click
        Function Purpose: This function Set event trigger function for double-click actions for the removed items listBox
        """           
        # Get selected item from removed items listBox
        widget = event.widget
        selection = widget.curselection()
        item = widget.get(selection[0])

        # Remove selected item from removed items listBox
        widget.delete(selection[0])

        # Add removed item back to the first listBox
        self.listBox.insert(tk.END, item)
        
        # Get the list of the items in the removed listBox
        self.removeList = [self.removeListBox.get(i) for i in range(self.removeListBox.size())]
        self.Update_Persistent_Array(BrakeCompSelection.astrBrakeCompSelect, self.removeList)
        
    def Set_Previous_Checkbox_List(self, selectList, checkboxList, paramsList):
        """
        Function Name: Set_Vis_Previous_Checkbox_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the checkboxes from the cache array list for all checkboxes.
        """   
        # First check if the cache values have been assigned
        if len(selectList) == 0:
            # Check the first item of the list    
            checkboxList[0].set('1')
        else:
            # Set the Selection data to the objects in the window
            for i, item in enumerate(paramsList):
                if item in selectList:
                    checkboxList[i].set('1')

    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)

    def Set_Previous_ListBox(self, selectString):
        """
        Function Name: Set_Previous_ListBox
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the list box menu item from the cache array list for all list box menus.
        """
        # Split the comma-separated string into a list of items
        anewList = str(selectString).split(',')

        # Check if the list box menu has the first element in the list
        listBoxItems = [self.listBox.get(i) for i in range(self.listBox.size())]
        removedBoxItems = [self.removeListBox.get(i) for i in range(self.removeListBox.size())]

        # Check if the removed list box items are comSelectItems[0]
        if self.comSelectItems[0] not in anewList:
            # First delete all items in the removed list box and the original list box
            self.removeListBox.delete(0, tk.END)
            self.listBox.delete(0, tk.END)
            self.removeListItems.clear()
            removedBoxItems.clear()
            
            for item in anewList:
                # Remove the item from the listBox
                if item in listBoxItems:
                    listBoxItems.remove(item)
                # Add removed item to the removeListBox if it's not already present
                if item not in [self.removeListBox.get(i) for i in range(self.removeListBox.size())]:
                    self.removeListBox.insert(tk.END, item)  
                    
            # Set the first element in the listBox to the comSelectItem[0]
            self.listBox.insert(tk.END, self.comSelectItems[0])
                                
            # Add the new list to the listBox columns
            for i in listBoxItems:
                self.listBox.insert(tk.END, i)

        # Set the removed list items to the selected list items
        self.removeListItems = [self.removeListBox.get(i) for i in range(self.removeListBox.size())]

        # Update the arrayObject based on deselection
        self.Update_Persistent_Array(BrakeCompSelection.astrBrakeCompSelect, self.removeListItems)
        
    def Get_VisCheckbox_List(self, item, var):
        """
        Function Name: Get_VisCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':            
            self.Update_Checkbox_List(self.visCheckList, item, self.checkboxVisStates, "visual", BrakeVisSelection.astrBrakeVisMetSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.visCheckList, item, self.checkboxVisStates, "visual", BrakeVisSelection.astrBrakeVisMetSelect)

    def Get_PhysCheckbox_List(self, item, var):
        """
        Function Name: Get_PhysCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':          
            self.Update_Checkbox_List(self.physCheckList, item, self.checkboxPhysStates, "physical", BrakePhysSelection.astrBrakePhysMetSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.physCheckList, item, self.checkboxPhysStates, "physical", BrakePhysSelection.astrBrakePhysMetSelect)

    def Update_Checkbox_List(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Update_Checkbox_List
        Function Purpose: This function is a generalized method to update checkbox states and persistent data.
        """
        # Check if the first item is selected and deselect all remaining items
        if item == self.selectItems[0]:
            for selectedItem in checkboxList[1:]:
                selectedItem.set('0')
        # Check if any other item is selected and deselect the first item
        else:
            if checkboxList[0].get() == '1':
                checkboxList[0].set('0')

        # Update the checkbox states dictionary
        checkboxStates[item] = '1' if checkboxList[self.selectItems.index(item)].get() == '1' else '0'

        # Update the persistent data based on the updated checkbox states
        selectedItemsList = [item for item, state in checkboxStates.items() if state == '1']
        
        # Update the arrayObject with selectedItemsList        
        self.Update_Persistent_Array(arrayObject, selectedItemsList)

    def Handle_Deselection(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Handle_Deselection
        Function Purpose: This function is called when a checkbox is deselected.
        """
        # # For now, I'm just printing a message. You can modify this to implement the desired behavior.
        # print(f"Checkbox {item} was deselected!")

        # If you want to remove an item from a persisted list or dictionary upon deselection, you can do so here:
        checkboxStates.pop(item, None)
        arrayObject.remove(item)
                
    def Update_Persistent_Array(self, arrayObject, selectedItemsList):
        """
        Function Name: Update_Persistent_Array
        Function Description: This function updates the arrayObject with the selected items list, while keeping existing persisted data.
        """
        # print("Selected Items:", selectedItemsList)
        # print("Before update:", arrayObject)

        selectedSet = set(selectedItemsList)
        arraySet = set(arrayObject)

        # Find items to add and remove
        toAdd = selectedSet - arraySet
        toRemove = arraySet - selectedSet

        for item in toAdd:
            arrayObject.append(item)
        for item in toRemove:
            arrayObject.remove(item)

        # print("After update:", arrayObject)

    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate

    def Check_Checkbox_Input(lstCheckBox, strFieldDesc):
        """
        Function Name: Check_Checkbox_Input
        Function Purpose: This function is called whenever a checkbox is present and needs to check if any of the entries are empty. If so,
        warn the user.
        """    
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)
            
        try:
            for i in range(0, len(lstCheckBox)):
                if lstCheckBox[i].get() == '1':
                    # Set blnValidated to True
                    blnValidate = True

            # Check if the blnValidated flag is true or false and warn the user if the entire field is empty
            if blnValidate is True:
                pass
            else:
                messagebox.showwarning(title='ERROR', message='%s field should not be empty. Please verify your selection.'%(strFieldDesc))
                blnValidate = False
                # Select the first checkbox
                lstCheckBox[0].set('1')

        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate

    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)  
        strVisField = str("Visual Result")
        strPhysField = str("Physical Result")

        # Check the user input
        blnValidate = BrakeInspection.Check_Input(self.dropBrakeVisStatus.get())

        # Check if the input is valid
        if (blnValidate is True):
            # Check the user input
            blnValidate = BrakeInspection.Check_Input(self.dropBrakePhysStatus.get())

            # Check if the input is valid
            if (blnValidate is True):
                # Check the user input
                blnValidate = BrakeInspection.Check_Checkbox_Input(self.visCheckList, strVisField)                                                                                                   
                
                # Check if the input is valid
                if (blnValidate is True):
                    # Check the user input
                    blnValidate = BrakeInspection.Check_Checkbox_Input(self.physCheckList, strPhysField)                                                                                                   
                    
                    # Check if the input is valid
                    if (blnValidate is True):
                        blnValidate = True
                    else:
                        # Return blnValidate as False
                        blnValidate = False                                    
                else:
                    # Return blnValidate as False
                    blnValidate = False                                
            else:
                # Return blnValidate as False
                blnValidate = False
                self.dropBrakePhysStatus.focus()
        else:
            # Return blnValidate as False
            blnValidate = False
            self.dropBrakeVisStatus.focus()

        return blnValidate 

    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        """   
        # Declare Local Variables
        sqlBrakeComSel = ("TBrakeCompSelects", "intBrakeCompSelectID", "strBrakeCompSelect")
        sqlBrakeVisSel = ("TBrakeVisMetalSelects", "intBrakeVisMetalSelectID", "strBrakeVisMetSelect")
        sqlBrakePhysSel = ("TBrakePhysMetalSelects", "intBrakePhysMetalSelectID", "strBrakePhysMetSelect")
        sqlBrakeVisIns = ("TBrakeHousingVisualInspections", "intBrakeHousingVisualInspectionID")
        sqlBrakePhysIns = ("TBrakeHousingPhysicalInspections", "intBrakeHousingPhysicalInspectionID")         
        sqlBrakeStandIns = ("TStandardBrakeHousingInspections", "intStandardBrakeHousingInspectionID")

        # Check if the comment is empty. If not, pass in the values. IF empty, pass in 'None'
        if self.commInput.get("1.0", "end-1c") != "":
            self.strComment = str(self.commInput.get("1.0", "end-1c"))
            self.strComment += "; "
            # Add the comment to the AutoBelay Comment object
            AutoBelayInspect.strComment = ''.join(self.strComment)
        else:
            self.commInput = 'None' 
            AutoBelayInspect.strComment = self.commInput
        
        # Combine the array elements into comma-separated strings
        BrakeCompSelect = self.Get_Combined_Selection(BrakeCompSelection.astrBrakeCompSelect, self.comSelectItems[0])
        BrakeVisMetSelect = self.Get_Combined_Selection(BrakeVisSelection.astrBrakeVisMetSelect, self.selectItems[0])
        BrakePhysMetSelect = self.Get_Combined_Selection(BrakePhysSelection.astrBrakePhysMetSelect, self.selectItems[0])

        # # Display the string representation
        # print(BrakeCompSelect)
        # print(BrakeVisMetSelect) 
        # print(BrakePhysMetSelect)
        
        # Get the status for the visual, and physical selection         
        BrakeVisStatus = self.dropBrakeVisStatus.get()                
        BrakePhysStatus = self.dropBrakePhysStatus.get() 
        
        # Get the type of selection, either physical or visual            
        VisInsTypeDesc = InspectionType.astrInspectionTypeDesc[0]   
        PhysInsTypeDesc = InspectionType.astrInspectionTypeDesc[1]  

        # First check if there is a duplicate in the db for the brake comp selection
        BrakeCompSelectID = self.Get_Or_Create_ID(BrakeCompSelect, sqlBrakeComSel)

        # Get the ID of the selected status item
        BrakeVisStatusID = InspectionStatus.astrInspectionStatusDesc.index(BrakeVisStatus) + 1
        BrakePhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(BrakePhysStatus) + 1

        # Get the ID of the selected Type item
        VisInsTypeID = InspectionType.astrInspectionTypeDesc.index(VisInsTypeDesc) + 1
        PhysInsTypeID = InspectionType.astrInspectionTypeDesc.index(PhysInsTypeDesc) + 1        
        
        # Get the list of items selected and attach them to the selection object for Visual and Physical Selection
        BrakeVisMetalSelectID = self.Get_Or_Create_ID(BrakeVisMetSelect, sqlBrakeVisSel)
        BrakePhysMetalSelectID = self.Get_Or_Create_ID(BrakePhysMetSelect, sqlBrakePhysSel)
        
        # Get the ID's for the base objects in each class
        BrakeHousingVisualInspectionID = self.Get_Max_Primary_Key(sqlBrakeVisIns[0], sqlBrakeVisIns[1])
        BrakeHousingPhysicalInspectionID = self.Get_Max_Primary_Key(sqlBrakePhysIns[0], sqlBrakePhysIns[1])
        StandardBrakeHousingInspectionID = self.Get_Max_Primary_Key(sqlBrakeStandIns[0], sqlBrakeStandIns[1])

        # Assign the local object to the class objects           
        b = BrakeCompSelection(BrakeCompSelectID, BrakeCompSelect)
        bvs = BrakeVisSelection(BrakeVisMetalSelectID, BrakeVisMetSelect, BrakeVisStatus)
        bps = BrakePhysSelection(BrakePhysMetalSelectID, BrakePhysMetSelect, BrakePhysStatus)

        # Commit the data to the visual inspection
        BrakeCompSelection.intBrakeCompSelectID = b.intBrakeCompSelectID 
        BrakeCompSelection.strBrakeCompSelect = b.strBrakeCompSelect        
        BrakeVisSelection.intBrakeVisMetalSelectID = bvs.intBrakeVisMetalSelectID
        BrakeVisSelection.strBrakeVisMetSelect = bvs.strBrakeVisMetSelect 
        BrakeVisSelection.strBrakeVisStatus = bvs.strBrakeVisStatus
        BrakeVisualInspect.aBrakeVisInsCache = (BrakeHousingVisualInspectionID, b.intBrakeCompSelectID, VisInsTypeID, bvs.intBrakeVisMetalSelectID, BrakeVisStatusID)

        # Commit the data to the physical inspection
        BrakePhysSelection.intBrakePhysMetalSelectID = bps.intBrakePhysMetalSelectID 
        BrakePhysSelection.strBrakePhysMetSelect = bps.strBrakePhysMetSelect
        BrakePhysSelection.strBrakePhysStatus = bps.strBrakePhysStatus
        BrakePhysicalInspect.aBrakePhysInsCache = (BrakeHousingPhysicalInspectionID, b.intBrakeCompSelectID, PhysInsTypeID, bps.intBrakePhysMetalSelectID, BrakePhysStatusID)    

        # Commit the data to the standard inspection
        StandardBrakeInspect.aStandardBrakeInsCache = (StandardBrakeHousingInspectionID, BrakeHousingVisualInspectionID, BrakeHousingPhysicalInspectionID)

    def Get_Combined_Selection(self, persisted_array, default_value):
        """
        Function Name: Get_Combined_Selection
        Function Purpose: This function combines the array elements into a comma-separated string,
        and handles the case when the persisted array is empty by setting a default value.
        """
        if len(persisted_array) == 0:
            return default_value
        else:
            return ",".join(persisted_array)
        
    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
            
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlStatement[0], sqlStatement[1]))    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
    
    def Next(self):
        """ 
        Function Name: Next
        Function Purpose: This function is executed once the user clicks on the "Next" button. Once the inputs 
        are validated, the inspection results loads the user selected data and is retained at the object class locations 
        before committing to the database. If all inputs are valid and confirmed by the user, the next stage of inspections is executed.
        """
        global blnValidate
        blnValidate = bool(False)             
        
        # First check if the input is empty, if so, notify the user the input needs attention 
        blnValidate = self.Validate_InputFields()
        
        # If status is true then proceed to update the result field, else, reset the fields
        if (blnValidate is True):
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to next inspection component?') is True:
                # print(BrakeCompSelection.astrBrakeCompSelect)
                # print(BrakeVisSelection.astrBrakeVisMetSelect)
                # print(BrakePhysSelection.astrBrakePhysMetSelect)
                # Load the user data and prep the data for db dump
                self.Pull_UserInput()      

                # Go to the next inspection component
                self.Next_Inspection()

            else:
                # Check if the user would like to reset the fields
                if messagebox.askyesno(message='ATTENTION! \n\n Would you like to reset the fields?') is True:
                    # Clear the input fields and after data is submitted to the database
                    self.Clear(self)  

    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This function is executed once the user clicks on the Reset button inside the root
        frame. If the user clicks 'Reset', all data is set back to default.
        """     
        # Clear the fields before inserting the primary list
        self.removeListBox.delete(0, tk.END)
        self.listBox.delete(0, tk.END)

        # Remove all the objects in the remove list
        for i in self.removeListItems:
            self.removeListItems.clear()
        
        # Replace list with the first object in the primary list
        self.removeListBox.insert(tk.END, self.comSelectItems[0])
        self.removeListItems = [self.removeListBox.get(i) for i in range(self.removeListBox.size())]    
                
        # Set the list objects first element to the drop click object
        for i in self.comSelectItems[1:]:
            self.listBox.insert(tk.END, i)

    def Clear(self):
        """ 
        Function Name: Clear
        Function Purpose: This function is executed once the user clicks on the Clear button inside the root
        frame. If the user clicks 'Clear', all data is set back to default.
        """     
        # Set the list objects first element to the drop click object
        self.dropBrakeVisStatus.set("")
        self.dropBrakePhysStatus.set("")
        
        # Clear the checkboxes to empty selections
        self.visCheckBox = BaseFunctions.Deselect_All_Checkbox(self.visCheckList)
        self.physCheckBox = BaseFunctions.Deselect_All_Checkbox(self.physCheckList)

        # Set the first item in the list to the first checkbox item displayed
        self.visCheckList[0].set('1')
        self.physCheckList[0].set('1')

        # Clear the class objects
        StandardBrakeInspect.Reset_Brake_Data(self)
        StandardBrakeInspect.Delete_Brake_Data(self)
        
        # Delete the comment field 
        self.commInput.delete("1.0", "end-1c") 
        
        # Reset the listbox fields
        self.Reset()

    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the root
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Hide the current window
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """     
        # Hide the current window
        self.Exit()  

        # Show the main window after the new window is closed
        CaseInspection()

    def Next_Inspection(self):
        """ 
        Function Name: Next_Inspection
        Function Purpose: This function is executed once the user clicks on Next button to move to the nex inspection
        type window. Withdraw the parent window and load the new window.
        """           
        # Hide the main window
        self.Exit()  

        # Open the new window
        HandleInspection()

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()       
        

#######################################################################################################
# Case Housing Inspection Class
#######################################################################################################   
class CaseInspection(tk.Tk):
    """
    Class Name: CaseInspection
    Class Description: This class is to conduct Case inspections.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new lanyard inspection. User must click
        'Next' Button in order to progress to the next inspection type. A Visual and Physical inspection
        must be performed to complete the inspection.
        """
        # Create the root tkinter variable
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (805/2)     
        self.y = (self.heightSize/2) - (600/2)          
        
        # Create the Window attributes    
        strUnitSelected = "Auto Belay Selected: %s"%(AutoBelay.strSerialNum)                                
        self.title("Case Housing Inspection - " + strUnitSelected)
        self.geometry('%dx%d+%d+%d' % (805, 600, self.x, self.y))
        self.resizable(False, False)

        # Create the frame fields
        self.typeFrame = tk.LabelFrame(self, text="Component Selection")
        self.typeFrame.place(x=95, y=10, width=610, height=210)
        self.visCheckListFrame = tk.LabelFrame(self, text="Visual Inspection Results")
        self.visCheckListFrame.place(x=95, y=230, width=300, height=200)
        self.physCheckListFrame = tk.LabelFrame(self, text="Physical Inspection Results")
        self.physCheckListFrame.place(x=405, y=230, width=300, height=200)
        self.commFrame = tk.LabelFrame(self, text="Inspection Comment")
        self.commFrame.place(x=95, y=440, width=610, height=100)

        # Create the listBox
        self.listBox = tk.Listbox(self.typeFrame)
        self.listBox.place(x=35, y=25, width=220, height=160)

        # Add some items to the listBox in alphabetical order
        self.comSelectItems = CaseHousing.astrCaseComponentDescs
        for item in self.comSelectItems[1:]:
            self.listBox.insert(tk.END, item)
            
        # Create a second listBox to hold removed items
        self.removeListBox = tk.Listbox(self.typeFrame)
        self.removeListBox.place(x=350, y=25, width=220, height=160)

        # Replace list with the first object in the primary list
        self.removeListBox.insert(tk.END, self.comSelectItems[0])
        
        # Create the list array for the remove Listbox
        self.removeListItems = []
        self.removeListItems = [self.removeListBox.get(i) for i in range(self.removeListBox.size())]      
            
        # Bind double-click event to listBox
        self.listBox.bind("<Double-Button-1>", self.on_double_click)
                        
        # Bind double-click event to the removed items listBox
        self.removeListBox.bind("<Double-Button-1>", self.on_removed_double_click)
                        
        # Create the label for the checkboxes
        self.lblDefaultComp = tk.Label(self.typeFrame, text="Affected Items")
        self.lblFinalComp = tk.Label(self.typeFrame, text="Selected Items")
        self.lblCaseVisualStatus = tk.Label(self.visCheckListFrame, text="Visual Status:")
        self.lblCasePhysicalStatus = tk.Label(self.physCheckListFrame, text="Physical Status:")
                        
        # Create the label locations
        self.lblDefaultComp.place(x=100, y=1)
        self.lblFinalComp.place(x=420, y=1)
        self.lblCaseVisualStatus.place(x=5, y=140)
        self.lblCasePhysicalStatus.place(x=5, y=140)

        # Create the drop down menu list for each attribute
        self.dropCaseVisStatus = ttk.Combobox(self.visCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropCasePhysStatus = ttk.Combobox(self.physCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        
        # Create the drop down menu size for each attribute
        self.dropCaseVisStatus.configure(width=20)
        self.dropCasePhysStatus.configure(width=20)
        
        # Create the grid for the drop down menu list objects
        self.dropCaseVisStatus.place(x=130, y=140)  
        self.dropCasePhysStatus.place(x=130, y=140)  

        # Create the master list for the metallic types
        self.selectItems = Metallic.astrMetallicInspectionDesc 

        # Create the checkbox lists for visual, and physical
        self.visCheckList = [] 
        self.physCheckList = []
        
        # Create a dictionary to track checkbox states
        self.checkboxVisStates = {}
        self.checkboxPhysStates = {}
        
        # Create the checkbox list
        self.Create_Check_Buttons(self.selectItems, self.visCheckListFrame, CaseVisSelection.astrCaseVisMetSelect, self.visCheckList, self.checkboxVisStates, self.Get_VisCheckbox_List)
        self.Create_Check_Buttons(self.selectItems, self.physCheckListFrame, CasePhysSelection.astrCasePhysMetSelect, self.physCheckList, self.checkboxPhysStates, self.Get_PhysCheckbox_List)

        # First check if the selection values have been assigned
        self.Set_Previous_Checkbox_List(CaseVisSelection.astrCaseVisMetSelect, self.visCheckList, self.selectItems) 
        self.Set_Previous_Checkbox_List(CasePhysSelection.astrCasePhysMetSelect, self.physCheckList, self.selectItems)                

        # Check if the cache values for any drop menus have been previously selected and set the values
        if Bool_Flag.blnCasePersistFlag == True:
            self.Set_Previous_ListBox(CaseCompSelection.strCaseCompSelect)
            self.Set_Previous_Drop_List(CaseVisSelection.strCaseVisStatus, self.dropCaseVisStatus)
            self.Set_Previous_Drop_List(CasePhysSelection.strCasePhysStatus, self.dropCasePhysStatus)            

        # Create the comment field
        self.commInput = tk.Text(self.commFrame, state='normal')
        self.commInput.grid(row=0, column=0, padx=5, pady=4)
        self.commInput.configure(width=74, height=4, padx=0)
        
        # Create the buttons
        self.btnBack = Button(self, text="Back", width=10, command=self.Back)
        self.btnClear = Button(self, text="Clear", width=10, command=self.Clear)
        self.btnExit = Button(self, text="Exit", width=10, command=self.Exit)
        self.btnNext = Button(self, text="Next", width=10, command=self.Next)
        self.btnReset = Button(self.typeFrame, text="Reset", width=10, command=self.Reset)
            
        # Create the position of the button
        self.btnBack.place(x=160, y=555)
        self.btnClear.place(x=420, y=555)
        self.btnNext.place(x=550, y=555) 
        self.btnExit.place(x=290, y=555) 
        self.btnReset.place(x=263, y=90) 

        # Keep the window open while the user is interacting with the widgets
        self.mainloop()       

        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the stored data in the class attributes
        StandardCarabinerInspect.Delete_Carabiner_Data(self)
        StandardLanyardInspect.Delete_Lanyard_Data(self)
        StandardCaseInspect.Delete_Case_Data(self)

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)
        AutoBelay_Menu()    
        
    def Create_Check_Buttons(self, selectItems, checkListFrame, arrayObject, checkList, checkboxStates, callback):
        """ 
        Function Name: Create_Check_Buttons
        Function Description: This helper method to create the checkbox buttons
        """
        maxColPerRow = 2

        for index, item in enumerate(selectItems):
            # Check if the item was previously selected (exists in arrayObject)
            is_selected = item in arrayObject
            var = tk.StringVar(value='1' if is_selected else '0')
            checkList.append(var)

            # Use a lambda function to capture the current item in the loop
            checkBox = tk.Checkbutton(checkListFrame, text=item, variable=var, onvalue='1', offvalue='0', 
                                    command=lambda item=item, var=var: callback(item, var))
            
            # Store the variable in the checkboxStates dictionary
            checkboxStates[item] = var

            # Calculate the row and column position of checkbutton based on index and max columns 
            rowPosition = index // maxColPerRow
            colPosition = index % maxColPerRow
            checkBox.grid(row=rowPosition, column=colPosition, sticky="w")
            
    def on_double_click(self, event):
        """
        Function Name: on_double_click
        Function Purpose: This function Set event trigger function for double-click actions for the removed items listBox
        """   
        # Get selected item from listBox
        widget = event.widget
        selection = widget.curselection()
        selected_item = widget.get(selection[0])

        # Always remove the selected item from the listBox
        widget.delete(selection[0])

        if selected_item != self.comSelectItems[0]:  # Check if selected item is not the first item
            # If the first item of comSelectItems is present in removeListItems, then move it to listBox
            if self.comSelectItems[0] in self.removeListItems:
                self.removeListBox.delete(0)
                self.listBox.insert(0, self.comSelectItems[0])
            
            # Add the removed item to removeListBox
            self.removeListBox.insert(tk.END, selected_item)
        else:
            # If the selected item is the first item, reset the listBox
            self.Reset()
        
        # Always update the removeListItems and persistent data after making changes
        self.removeListItems = [self.removeListBox.get(i) for i in range(self.removeListBox.size())]
        self.Update_Persistent_Array(CaseCompSelection.astrCaseCompSelect, self.removeListItems)       
            
    def on_removed_double_click(self, event):
        """
        Function Name: on_removed_double_click
        Function Purpose: This function Set event trigger function for double-click actions for the removed items listBox
        """           
        # Get selected item from removed items listBox
        widget = event.widget
        selection = widget.curselection()
        item = widget.get(selection[0])

        # Remove selected item from removed items listBox
        widget.delete(selection[0])

        # Add removed item back to the first listBox
        self.listBox.insert(tk.END, item)
        
        # Get the list of the items in the removed listBox
        self.removeList = [self.removeListBox.get(i) for i in range(self.removeListBox.size())]
        self.Update_Persistent_Array(CaseCompSelection.astrCaseCompSelect, self.removeList)
                
    def Set_Previous_Checkbox_List(self, selectList, checkboxList, paramsList):
        """
        Function Name: Set_Vis_Previous_Checkbox_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the checkboxes from the cache array list for all checkboxes.
        """   
        # First check if the cache values have been assigned
        if len(selectList) == 0:
            # Check the first item of the list    
            checkboxList[0].set('1')
        else:
            # Set the Selection data to the objects in the window
            for i, item in enumerate(paramsList):
                if item in selectList:
                    checkboxList[i].set('1')

    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)

    def Set_Previous_ListBox(self, selectString):
        """
        Function Name: Set_Previous_ListBox
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the list box menu item from the cache array list for all list box menus.
        """
        # Split the comma-separated string into a list of items
        anewList = str(selectString).split(',')

        # Check if the list box menu has the first element in the list
        listBoxItems = [self.listBox.get(i) for i in range(self.listBox.size())]
        removedBoxItems = [self.removeListBox.get(i) for i in range(self.removeListBox.size())]

        # Check if the removed list box items are comSelectItems[0]
        if self.comSelectItems[0] not in anewList:
            # First delete all items in the removed list box and the original list box
            self.removeListBox.delete(0, tk.END)
            self.listBox.delete(0, tk.END)
            self.removeListItems.clear()
            removedBoxItems.clear()
            
            for item in anewList:
                # Remove the item from the listBox
                if item in listBoxItems:
                    listBoxItems.remove(item)
                # Add removed item to the removeListBox if it's not already present
                if item not in [self.removeListBox.get(i) for i in range(self.removeListBox.size())]:
                    self.removeListBox.insert(tk.END, item)  
                    
            # Set the first element in the listBox to the comSelectItem[0]
            self.listBox.insert(tk.END, self.comSelectItems[0])
                                
            # Add the new list to the listBox columns
            for i in listBoxItems:
                self.listBox.insert(tk.END, i)

        # Set the removed list items to the selected list items
        self.removeListItems = [self.removeListBox.get(i) for i in range(self.removeListBox.size())]

        # Update the arrayObject based on deselection
        self.Update_Persistent_Array(CaseCompSelection.astrCaseCompSelect, self.removeListItems)

    def Get_VisCheckbox_List(self, item, var):
        """
        Function Name: Get_VisCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':            
            self.Update_Checkbox_List(self.visCheckList, item, self.checkboxVisStates, "visual", CaseVisSelection.astrCaseVisMetSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.visCheckList, item, self.checkboxVisStates, "visual", CaseVisSelection.astrCaseVisMetSelect)
            
    def Get_PhysCheckbox_List(self, item, var):
        """
        Function Name: Get_PhysCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':          
            self.Update_Checkbox_List(self.physCheckList, item, self.checkboxPhysStates, "physical", CasePhysSelection.astrCasePhysMetSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.physCheckList, item, self.checkboxPhysStates, "physical", CasePhysSelection.astrCasePhysMetSelect)
            
    def Update_Checkbox_List(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Update_Checkbox_List
        Function Purpose: This function is a generalized method to update checkbox states and persistent data.
        """
        # Check if the first item is selected and deselect all remaining items
        if item == self.selectItems[0]:
            for selectedItem in checkboxList[1:]:
                selectedItem.set('0')
        # Check if any other item is selected and deselect the first item
        else:
            if checkboxList[0].get() == '1':
                checkboxList[0].set('0')

        # Update the checkbox states dictionary
        checkboxStates[item] = '1' if checkboxList[self.selectItems.index(item)].get() == '1' else '0'

        # Update the persistent data based on the updated checkbox states
        selectedItemsList = [item for item, state in checkboxStates.items() if state == '1']
        
        # Update the arrayObject with selectedItemsList        
        self.Update_Persistent_Array(arrayObject, selectedItemsList)

    def Handle_Deselection(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Handle_Deselection
        Function Purpose: This function is called when a checkbox is deselected.
        """
        # # For now, I'm just printing a message. You can modify this to implement the desired behavior.
        # print(f"Checkbox {item} was deselected!")

        # If you want to remove an item from a persisted list or dictionary upon deselection, you can do so here:
        checkboxStates.pop(item, None)
        arrayObject.remove(item)
        
    def Update_Persistent_Array(self, arrayObject, selectedItemsList):
        """
        Function Name: Update_Persistent_Array
        Function Description: This function updates the arrayObject with the selected items list, while keeping existing persisted data.
        """
        # print("Selected Items:", selectedItemsList)
        # print("Before update:", arrayObject)

        selectedSet = set(selectedItemsList)
        arraySet = set(arrayObject)

        # Find items to add and remove
        toAdd = selectedSet - arraySet
        toRemove = arraySet - selectedSet

        for item in toAdd:
            arrayObject.append(item)
        for item in toRemove:
            arrayObject.remove(item)

        # print("After update:", arrayObject)                                

    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate
    
    def Check_Checkbox_Input(lstCheckBox, strFieldDesc):
        """
        Function Name: Check_Checkbox_Input
        Function Purpose: This function is called whenever a checkbox is present and needs to check if any of the entries are empty. If so,
        warn the user.
        """    
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)
            
        try:
            for i in range(0, len(lstCheckBox)):
                if lstCheckBox[i].get() == '1':
                    # Set blnValidated to True
                    blnValidate = True

            # Check if the blnValidated flag is true or false and warn the user if the entire field is empty
            if blnValidate is True:
                pass
            else:
                messagebox.showwarning(title='ERROR', message='%s field should not be empty. Please verify your selection.'%(strFieldDesc))
                blnValidate = False
                # Select the first checkbox
                lstCheckBox[0].set('1')

        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate

    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)  
        strVisField = str("Visual Result")
        strPhysField = str("Physical Result")

        # Check the user input
        blnValidate = CaseInspection.Check_Input(self.dropCaseVisStatus.get())

        # Check if the input is valid
        if (blnValidate is True):
            # Check the user input
            blnValidate = CaseInspection.Check_Input(self.dropCasePhysStatus.get())

            # Check if the input is valid
            if (blnValidate is True):
                # Check the user input
                blnValidate = CaseInspection.Check_Checkbox_Input(self.visCheckList, strVisField)                                                                                                   
                
                # Check if the input is valid
                if (blnValidate is True):
                    # Check the user input
                    blnValidate = CaseInspection.Check_Checkbox_Input(self.physCheckList, strPhysField)                                                                                                   
                    
                    # Check if the input is valid
                    if (blnValidate is True):
                        blnValidate = True
                    else:
                        # Return blnValidate as False
                        blnValidate = False                                    
                else:
                    # Return blnValidate as False
                    blnValidate = False                                
            else:
                # Return blnValidate as False
                blnValidate = False
                self.dropCasePhysStatus.focus()
        else:
            # Return blnValidate as False
            blnValidate = False
            self.dropCaseVisStatus.focus()

        return blnValidate 

    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        """    
        # Declare Local Variables
        sqlCaseComSel = ("TCaseCompSelects", "intCaseCompSelectID", "strCaseCompSelect")
        sqlCaseVisSel = ("TCaseVisMetalSelects", "intCaseVisMetalSelectID", "strCaseVisMetSelect")
        sqlCasePhysSel = ("TCasePhysMetalSelects", "intCasePhysMetalSelectID", "strCasePhysMetSelect")
        sqlCaseVisIns = ("TCaseHousingVisualInspections", "intCaseHousingVisualInspectionID")
        sqlCasePhysIns = ("TCaseHousingPhysicalInspections", "intCaseHousingPhysicalInspectionID")         
        sqlCaseStandIns = ("TStandardCaseHousingInspections", "intStandardCaseHousingInspectionID")

        # Check if the comment is empty. If not, pass in the values. IF empty, pass in 'None'
        CaseCompSelect = self.Get_Combined_Selection(CaseCompSelection.astrCaseCompSelect, self.comSelectItems[0])
        CaseVisMetSelect = self.Get_Combined_Selection(CaseVisSelection.astrCaseVisMetSelect, self.selectItems[0])
        CasePhysMetSelect = self.Get_Combined_Selection(CasePhysSelection.astrCasePhysMetSelect, self.selectItems[0])

        # # Display the string representation
        # print(CaseCompSelect)
        # print(CaseVisMetSelect) 
        # print(CasePhysMetSelect)

        # Get the status for the visual, and physical selection                                                
        CaseVisStatus = self.dropCaseVisStatus.get()                
        CasePhysStatus = self.dropCasePhysStatus.get()      
        
        # Get the type of selection, either physical or visual        
        VisInsTypeDesc = InspectionType.astrInspectionTypeDesc[0]   
        PhysInsTypeDesc = InspectionType.astrInspectionTypeDesc[1]  

        # First check if there is a duplicate in the db for the case comp selection
        CaseCompSelectID = self.Get_Or_Create_ID(CaseCompSelect, sqlCaseComSel)

        # Get the ID of the selected status item
        CaseVisStatusID = InspectionStatus.astrInspectionStatusDesc.index(CaseVisStatus) + 1
        CasePhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(CasePhysStatus) + 1

        # Get the ID of the selected Inspection Type item
        VisInsTypeID = InspectionType.astrInspectionTypeDesc.index(VisInsTypeDesc) + 1
        PhysInsTypeID = InspectionType.astrInspectionTypeDesc.index(PhysInsTypeDesc) + 1        

        # Get the list of items selected and attach them to the selection object for Visual and Physical Selection
        CaseVisMetalSelectID = self.Get_Or_Create_ID(CaseVisMetSelect, sqlCaseVisSel)              
        CasePhysMetalSelectID = self.Get_Or_Create_ID(CasePhysMetSelect, sqlCasePhysSel)

        # Get the ID's for the base objects in each class
        CaseHousingVisualInspectionID = self.Get_Max_Primary_Key(sqlCaseVisIns[0], sqlCaseVisIns[1])
        CaseHousingPhysicalInspectionID = self.Get_Max_Primary_Key(sqlCasePhysIns[0], sqlCasePhysIns[1])
        StandardCaseHousingInspectionID = self.Get_Max_Primary_Key(sqlCaseStandIns[0], sqlCaseStandIns[1])
        
        # Assign the local object to the class objects   
        c = CaseCompSelection(CaseCompSelectID, CaseCompSelect)
        cvs = CaseVisSelection(CaseVisMetalSelectID, CaseVisMetSelect, CaseVisStatus)
        cps = CasePhysSelection(CasePhysMetalSelectID, CasePhysMetSelect, CasePhysStatus)

        # Commit the data to the visual inspection
        CaseCompSelection.intCaseCompSelectID = c.intCaseCompSelectID
        CaseCompSelection.strCaseCompSelect = c.strCaseCompSelect    
        CaseVisSelection.intCaseVisMetalSelectID = cvs.intCaseVisMetalSelectID  
        CaseVisSelection.strCaseVisMetSelect = cvs.strCaseVisMetSelect
        CaseVisSelection.strCaseVisStatus = cvs.strCaseVisStatus
        CaseVisualInspect.aCaseVisInsCache = (CaseHousingVisualInspectionID, c.intCaseCompSelectID, VisInsTypeID, cvs.intCaseVisMetalSelectID, CaseVisStatusID)

        # Commit the data to the physical inspection
        CasePhysSelection.intCasePhysMetalSelectID = cps.intCasePhysMetalSelectID
        CasePhysSelection.strCasePhysMetSelect = cps.strCasePhysMetSelect
        CasePhysSelection.strCasePhysStatus = cps.strCasePhysStatus
        CasePhysicalInspect.aCasePhysInsCache = (CaseHousingPhysicalInspectionID, c.intCaseCompSelectID, PhysInsTypeID, cps.intCasePhysMetalSelectID, CasePhysStatusID)    

        # Commit the data to the standard inspection
        StandardCaseInspect.aStandardCaseInsCache = (StandardCaseHousingInspectionID, CaseHousingVisualInspectionID, CaseHousingPhysicalInspectionID)

    def Get_Combined_Selection(self, persisted_array, default_value):
        """
        Function Name: Get_Combined_Selection
        Function Purpose: This function combines the array elements into a comma-separated string,
        and handles the case when the persisted array is empty by setting a default value.
        """
        if len(persisted_array) == 0:
            return default_value
        else:
            return ",".join(persisted_array)
        
    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
                            
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlStatement[0], sqlStatement[1]))    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
    
    def Next(self):
        """ 
        Function Name: Next
        Function Purpose: This function is executed once the user clicks on the "Next" button. Once the inputs 
        are validated, the inspection results loads the user selected data and is retained at the object class locations 
        before committing to the database. If all inputs are valid and confirmed by the user, the next stage of inspections is executed.
        """
        global blnValidate
        blnValidate = bool(False)             
        
        # First check if the input is empty, if so, notify the user the input needs attention 
        blnValidate = self.Validate_InputFields()
        
        # If status is true then proceed to update the result field, else, reset the fields
        if (blnValidate is True):
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to next inspection component?') is True:                    
                # print(CaseCompSelection.astrCaseCompSelect)
                # print(CaseVisSelection.astrCaseVisMetSelect) 
                # print(CasePhysSelection.astrCasePhysMetSelect)
                # Load the user data and prep the data for db dump               
                self.Pull_UserInput()      

                # Go to the next inspection component
                self.Next_Inspection()

            else:
                # Check if the user would like to reset the fields
                if messagebox.askyesno(message='ATTENTION! \n\n Would you like to reset the fields?') is True:
                    # Clear the input fields and after data is submitted to the database
                    self.Clear(self)  

    def Clear(self):
        """ 
        Function Name: Clear
        Function Purpose: This function is executed once the user clicks on the Clear button inside the root
        frame. If the user clicks 'Clear', all data is set back to default.
        """     
        # Set the list objects first element to the drop click object
        self.dropCaseVisStatus.set("")
        self.dropCasePhysStatus.set("")
        
        # Clear the checkboxes to empty selections
        self.visCheckBox = BaseFunctions.Deselect_All_Checkbox(self.visCheckList)
        self.physCheckBox = BaseFunctions.Deselect_All_Checkbox(self.physCheckList)

        # Set the first item in the list to the first checkbox item displayed
        self.visCheckList[0].set('1')
        self.physCheckList[0].set('1')

        # Delete the comment field 
        self.commInput.delete("1.0", "end-1c") 

        # Clear the class objects 
        StandardCaseInspect.Reset_Case_Data(self)
        StandardCaseInspect.Delete_Case_Data(self)
                
        # Reset the listbox fields
        self.Reset()

    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This function is executed once the user clicks on the Reset button inside the root
        frame. If the user clicks 'Reset', all data is set back to default.
        """     
        # Clear the fields before inserting the primary list
        self.removeListBox.delete(0, tk.END)
        self.listBox.delete(0, tk.END)

        # Remove all the objects in the remove list
        for i in self.removeListItems:
            self.removeListItems.clear()
        
        # Replace list with the first object in the primary list
        self.removeListBox.insert(tk.END, self.comSelectItems[0])
        self.removeListItems = [self.removeListBox.get(i) for i in range(self.removeListBox.size())]    
                
        # Set the list objects first element to the drop click object
        for i in self.comSelectItems[1:]:
            self.listBox.insert(tk.END, i)
            
    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the root
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Hide the current window
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """     
        # Hide the current window
        self.Exit()  

        # Show the main window after the new window is closed
        LanyardInspection()

    def Next_Inspection(self):
        """ 
        Function Name: Next_Inspection
        Function Purpose: This function is executed once the user clicks on Next button to move to the nex inspection
        type window. Withdraw the parent window and load the new window.
        """           
        # Hide the main window
        self.Exit()  

        # Open the new window
        BrakeInspection()

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        

#######################################################################################################
# Device Handle Inspection Class
#######################################################################################################   
class HandleInspection(tk.Tk):
    """
    Class Name: HandleInspection
    Class Description: This class is to conduct Device Handle inspections.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new Device Handle inspection. User must click
        'Next' Button in order to progress to the next inspection type. A Visual and Physical inspection
        must be performed to complete the inspection.
        """
        # Create the root tkinter variable
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (805/2)     
        self.y = (self.heightSize/2) - (470/2)          
        
        # Create the Window attributes                
        strUnitSelected = "Auto Belay Selected: %s"%(AutoBelay.strSerialNum)                                
        self.title("Device Handle Inspection - " + strUnitSelected)            
        self.geometry('%dx%d+%d+%d' % (805, 470, self.x, self.y))
        self.resizable(False, False)

        # Create the frame fields
        self.typeFrame = tk.LabelFrame(self, text="Handle Selection")
        self.typeFrame.place(x=90, y=10, width=610, height=80)
        self.visCheckListFrame = tk.LabelFrame(self, text="Visual Inspection Results")
        self.visCheckListFrame.place(x=90, y=100, width=300, height=200)
        self.physCheckListFrame = tk.LabelFrame(self, text="Physical Inspection Results")
        self.physCheckListFrame.place(x=400, y=100, width=300, height=200)
        self.commFrame = tk.LabelFrame(self, text="Inspection Comment")
        self.commFrame.place(x=90, y=310, width=610, height=100)
                
        # Create the label for the checkboxes
        self.lblHandleType = tk.Label(self.typeFrame, text="Handle Type:")
        self.lblHandleVisualStatus = tk.Label(self.visCheckListFrame, text="Visual Status:")
        self.lblHandlePhysicalStatus = tk.Label(self.physCheckListFrame, text="Physical Status:")
                        
        # Create the label locations
        self.lblHandleType.place(x=180, y=18)
        self.lblHandleVisualStatus.place(x=5, y=140)
        self.lblHandlePhysicalStatus.place(x=5, y=140)

        # Create the drop down menu list for each attribute
        self.dropHandleType = ttk.Combobox(self.typeFrame, values=DeviceHandle.astrHandleType, state='readonly')
        self.dropHandleVisStatus = ttk.Combobox(self.visCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropHandlePhysStatus = ttk.Combobox(self.physCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        
        # Create the drop down menu size for each attribute
        self.dropHandleType.configure(width=25)
        self.dropHandleVisStatus.configure(width=20)
        self.dropHandlePhysStatus.configure(width=20)
        
        # Create the grid for the drop down menu list objects
        self.dropHandleType.place(x=290, y=18)   
        self.dropHandleVisStatus.place(x=125, y=140)  
        self.dropHandlePhysStatus.place(x=125, y=140)  

        # Create the master list for the metallic and functional inspection types
        self.selectItems = Metallic.astrMetallicInspectionDesc
        
        # Create the checkbox lists for visual, physical, and functional
        self.visCheckList = [] 
        self.physCheckList = []
        
        # Create an empty list to store selected items
        self.checkboxVisStates = {}
        self.checkboxPhysStates = {}

        # Create the checkbox list
        self.Create_Check_Buttons(self.selectItems, self.visCheckListFrame, HandleVisSelection.astrHandVisMetSelect, self.visCheckList, self.checkboxVisStates, self.Get_VisCheckbox_List, "visual")
        self.Create_Check_Buttons(self.selectItems, self.physCheckListFrame, HandlePhysSelection.astrHandPhysMetSelect, self.physCheckList, self.checkboxPhysStates, self.Get_PhysCheckbox_List, "physical")

        # First check if the selection values have been assigned
        self.Set_Previous_Checkbox_List(HandleVisSelection.astrHandVisMetSelect, self.visCheckList, self.selectItems)        
        self.Set_Previous_Checkbox_List(HandlePhysSelection.astrHandPhysMetSelect, self.physCheckList, self.selectItems)
        
        # Check if the cache values for any drop menus have been previously selected and set the values
        if Bool_Flag.blnHandlePersistFlag == True:
            self.Set_Previous_Drop_List(DeviceHandle.strHandleType, self.dropHandleType)
            self.Set_Previous_Drop_List(HandleVisSelection.strHandleVisStatus, self.dropHandleVisStatus)
            self.Set_Previous_Drop_List(HandlePhysSelection.strHandlePhysStatus, self.dropHandlePhysStatus)            

        # Create the comment field
        self.commInput = tk.Text(self.commFrame, state='normal')
        self.commInput.grid(row=0, column=0, padx=5, pady=4)
        self.commInput.configure(width=74, height=4, padx=0)
        
        # Create the buttons
        self.btnBack = Button(self, text="Back", width=10, command=self.Back)
        self.btnClear = Button(self, text="Clear", width=10, command=self.Reset)
        self.btnExit = Button(self, text="Exit", width=10, command=self.Exit)
        self.btnNext = Button(self, text="Next", width=10, command=self.Next)
            
        # Create the position of the button
        self.btnBack.place(x=160, y=425)
        self.btnClear.place(x=420, y=425)
        self.btnNext.place(x=550, y=425) 
        self.btnExit.place(x=290, y=425) 
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()

        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the stored data in the class attributes
        StandardCarabinerInspect.Delete_Carabiner_Data(self)
        StandardLanyardInspect.Delete_Lanyard_Data(self)
        StandardCaseInspect.Delete_Case_Data(self)
        StandardBrakeInspect.Delete_Brake_Data(self)
        StandardHandelInspect.Delete_Handle_Data(self)

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)
        AutoBelay_Menu()            

    def Create_Check_Buttons(self, selectItems, checkListFrame, arrayObject, checkList, checkboxStates, callback, strInsType):
        """ 
        Function Name: Create_Check_Buttons
        Function Description: This helper method to create the checkbox buttons
        """
        if strInsType == "visual" or strInsType == "physical":
            maxColPerRow = 2
        else:
            maxColPerRow = 4

        for index, item in enumerate(selectItems):
            # Check if the item was previously selected (exists in arrayObject)
            is_selected = item in arrayObject
            var = tk.StringVar(value='1' if is_selected else '0')
            checkList.append(var)

            # Use a lambda function to capture the current item in the loop
            checkBox = tk.Checkbutton(checkListFrame, text=item, variable=var, onvalue='1', offvalue='0', 
                                    command=lambda item=item, var=var: callback(item, var))
            
            # Store the variable in the checkboxStates dictionary
            checkboxStates[item] = var

            # Calculate the row and column position of checkbutton based on index and max columns 
            rowPosition = index // maxColPerRow
            colPosition = index % maxColPerRow
            checkBox.grid(row=rowPosition, column=colPosition, sticky="w", padx=10)
            
    def Set_Previous_Checkbox_List(self, selectList, checkboxList, paramsList):
        """
        Function Name: Set_Vis_Previous_Checkbox_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the checkboxes from the cache array list for all checkboxes.
        """   
        # First check if the cache values have been assigned
        if len(selectList) == 0:
            # Check the first item of the list    
            checkboxList[0].set('1')
        else:
            # Set the Selection data to the objects in the window
            for i, item in enumerate(paramsList):
                if item in selectList:
                    checkboxList[i].set('1')

    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)

    def Get_VisCheckbox_List(self, item, var):
        """
        Function Name: Get_VisCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':            
            self.Update_Checkbox_List(self.visCheckList, item, self.checkboxVisStates, "visual", HandleVisSelection.astrHandVisMetSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.visCheckList, item, self.checkboxVisStates, "visual", HandleVisSelection.astrHandVisMetSelect)
            
    def Get_PhysCheckbox_List(self, item, var):
        """
        Function Name: Get_PhysCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':          
            self.Update_Checkbox_List(self.physCheckList, item, self.checkboxPhysStates, "physical", HandlePhysSelection.astrHandPhysMetSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.physCheckList, item, self.checkboxPhysStates, "physical", HandlePhysSelection.astrHandPhysMetSelect)

    def Update_Checkbox_List(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Update_Checkbox_List
        Function Purpose: This function is a generalized method to update checkbox states and persistent data.
        """
        # Check if the first item is selected and deselect all remaining items
        if item == self.selectItems[0]:
            for selectedItem in checkboxList[1:]:
                selectedItem.set('0')
        # Check if any other item is selected and deselect the first item
        else:
            if checkboxList[0].get() == '1':
                checkboxList[0].set('0')

        # Check if the window section is functional
        if selectionKey == 'functional':
            # Update the checkbox states dictionary
            checkboxStates[item] = '1' if checkboxList[self.functItems.index(item)].get() == '1' else '0'
        else:
            # Update the checkbox states dictionary
            checkboxStates[item] = '1' if checkboxList[self.selectItems.index(item)].get() == '1' else '0'

        # Update the persistent data based on the updated checkbox states
        selectedItemsList = [item for item, state in checkboxStates.items() if state == '1']
        
        # Update the arrayObject with selectedItemsList        
        self.Update_Persistent_Array(arrayObject, selectedItemsList)

    def Handle_Deselection(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Handle_Deselection
        Function Purpose: This function is called when a checkbox is deselected.
        """
        # For now, I'm just printing a message. You can modify this to implement the desired behavior.
        # print(f"Checkbox {item} was deselected!")

        # If you want to remove an item from a persisted list or dictionary upon deselection, you can do so here:
        checkboxStates.pop(item, None)
        arrayObject.remove(item)
        
    def Update_Persistent_Array(self, arrayObject, selectedItemsList):
        """
        Function Name: Update_Persistent_Array
        Function Description: This function updates the arrayObject with the selected items list, while keeping existing persisted data.
        """
        # print("Selected Items:", selectedItemsList)
        # print("Before update:", arrayObject)

        selectedSet = set(selectedItemsList)
        arraySet = set(arrayObject)

        # Find items to add and remove
        toAdd = selectedSet - arraySet
        toRemove = arraySet - selectedSet

        for item in toAdd:
            arrayObject.append(item)
        for item in toRemove:
            arrayObject.remove(item)

        # print("After update:", arrayObject) 
        
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate

    def Check_Checkbox_Input(lstCheckBox, strFieldDesc):
        """
        Function Name: Check_Checkbox_Input
        Function Purpose: This function is called whenever a checkbox is present and needs to check if any of the entries are empty. If so,
        warn the user.
        """    
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)
            
        try:
            for i in range(0, len(lstCheckBox)):
                if lstCheckBox[i].get() == '1':
                    # Set blnValidated to True
                    blnValidate = True

            # Check if the blnValidated flag is true or false and warn the user if the entire field is empty
            if blnValidate is True:
                pass
            else:
                messagebox.showwarning(title='ERROR', message='%s field should not be empty. Please verify your selection.'%(strFieldDesc))
                blnValidate = False
                # Select the first checkbox
                lstCheckBox[0].set('1')

        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate  

    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)  
        strVisField = str("Visual Result")
        strPhysField = str("Physical Result")

        # Check the user input
        blnValidate = HandleInspection.Check_Input(self.dropHandleType.get())

        # Check if the input is valid
        if (blnValidate is True):
            # Check the user input
            blnValidate = HandleInspection.Check_Input(self.dropHandleVisStatus.get())         
            
            # Check if the input is valid
            if (blnValidate is True):
                # Check the user input
                blnValidate = HandleInspection.Check_Input(self.dropHandlePhysStatus.get())         
                
                # Check if the input is valid
                if (blnValidate is True):
                    # Check the user input
                    blnValidate = HandleInspection.Check_Checkbox_Input(self.visCheckList, strVisField)                                                                                                   
                    
                    # Check if the input is valid
                    if (blnValidate is True):
                        # Check the user input
                        blnValidate = HandleInspection.Check_Checkbox_Input(self.physCheckList, strPhysField)                                                                                                   
                        
                        # Check if the input is valid
                        if (blnValidate is True):
                            blnValidate = True
                        else:
                            # Return blnValidate as False
                            blnValidate = False                                                                  
                    else:
                        # Return blnValidate as False
                        blnValidate = False
                else:
                    # Return blnValidate as False
                    blnValidate = False
                    self.dropHandlePhysStatus.focus()
            else:
                # Return blnValidate as False
                blnValidate = False
                self.dropHandleVisStatus.focus()                                                
        else:
            # Return blnValidate as False
            blnValidate = False
            self.dropHandleType.focus()

        return blnValidate 

    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        """       
        # Declare Local Variables
        sqlHandleVisSel = ("THandleVisMetalSelects", "intHandVisMetalSelectID", "strHandVisMetSelect")
        sqlHandlePhysSel = ("THandlePhysMetalSelects", "intHandPhysMetalSelectID", "strHandPhysMetSelect")
        sqlHandleVisIns = ("THandleVisualInspections", "intHandleVisualID")
        sqlHandlePhysIns = ("THandlePhysicalInspections", "intHandlePhysicalID") 
        sqlHandleStandIns = ("TStandardHandleInspections", "intStandardHandleInspectionID")

        # Check if the comment is empty. If not, pass in the values. If empty, pass in 'None'
        if self.commInput.get("1.0", "end-1c") != "":
            self.strComment = str(self.commInput.get("1.0", "end-1c"))
            self.strComment += "; "
            # Add the comment to the AutoBelay Comment object
            AutoBelayInspect.strComment = ''.join(self.strComment)
        else:
            self.strComment = 'None'
            AutoBelayInspect.strComment = self.strComment
        
        # Get the selected values
        HandleType = self.dropHandleType.get()
        HandleVisMetSelect = self.Get_Combined_Selection(HandleVisSelection.astrHandVisMetSelect, self.selectItems[0])
        HandlePhysMetSelect = self.Get_Combined_Selection(HandlePhysSelection.astrHandPhysMetSelect, self.selectItems[0])

        # # Display the string representation
        # print(HandleType)
        # print(HandleVisMetSelect) 
        # print(HandlePhysMetSelect)
        
        # Get the status for the visual, physical selection
        HandleVisStatus = self.dropHandleVisStatus.get()
        HandlePhysStatus = self.dropHandlePhysStatus.get()
        
        # Get the ID of the selected status item
        HandleVisStatusID = InspectionStatus.astrInspectionStatusDesc.index(HandleVisStatus) + 1
        HandlePhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(HandlePhysStatus) + 1
        
        # Get the type of selection, either physical, visual 
        VisInsTypeDesc = InspectionType.astrInspectionTypeDesc[0]
        PhysInsTypeDesc = InspectionType.astrInspectionTypeDesc[1]

        # Get the ID of the selected Type item
        VisInsTypeID = InspectionType.astrInspectionTypeDesc.index(VisInsTypeDesc) + 1
        PhysInsTypeID = InspectionType.astrInspectionTypeDesc.index(PhysInsTypeDesc) + 1

        # Get the list of items selected and attach them to the selection object for Visual and Physical Selection
        HandleVisMetalSelectID = self.Get_Or_Create_ID(HandleVisMetSelect, sqlHandleVisSel)              
        HandlePhysMetalSelectID = self.Get_Or_Create_ID(HandleVisMetSelect, sqlHandlePhysSel)
                            
        # Get the ID's for the base objects in each class
        HandleID = DeviceHandle.astrHandleType.index(HandleType) + 1
        HandleVisualInsID = self.Get_Max_Primary_Key(sqlHandleVisIns[0], sqlHandleVisIns[1])
        HandlePhysicalInsID = self.Get_Max_Primary_Key(sqlHandlePhysIns[0], sqlHandlePhysIns[1])        
        StandardHandleInspectionID = self.Get_Max_Primary_Key(sqlHandleStandIns[0], sqlHandleStandIns[1])

        # Assign the local object to the class objects
        h = DeviceHandle(HandleID, HandleType)
        hvs = HandleVisSelection(HandleVisMetalSelectID, HandleVisMetSelect, HandleVisStatus)
        hps = HandlePhysSelection(HandlePhysMetalSelectID, HandlePhysMetSelect, HandlePhysStatus)        

        # Commit the data to the visual inspection
        DeviceHandle.strHandleType = h.strHandleType
        HandleVisSelection.intHandVisMetalSelectID = hvs.intHandVisMetalSelectID
        HandleVisSelection.strHandVisMetSelect = hvs.strHandVisMetSelect
        HandleVisSelection.strHandleVisStatus = hvs.strHandleVisStatus
        HandleVisualInspect.aHandleVisCache = (HandleVisualInsID, h.intDeviceHandleID, VisInsTypeID, hvs.intHandVisMetalSelectID, HandleVisStatusID)

        # Commit the data to the physical inspection
        HandlePhysSelection.intHandPhysMetalSelectID = hps.intHandPhysMetalSelectID
        HandlePhysSelection.strHandPhysMetSelect = hps.strHandPhysMetSelect
        HandlePhysSelection.strHandlePhysStatus = hps.strHandlePhysStatus
        HandlePhysicalInspect.aHandlePhysCache = (HandlePhysicalInsID, h.intDeviceHandleID, PhysInsTypeID, hps.intHandPhysMetalSelectID, HandlePhysStatusID)    

        # Commit the data to the standard inspection
        StandardHandelInspect.aStandardHandleInsCache = (StandardHandleInspectionID, HandleVisualInsID, HandlePhysicalInsID)

    def Get_Combined_Selection(self, persisted_array, default_value):
        """
        Function Name: Get_Combined_Selection
        Function Purpose: This function combines the array elements into a comma-separated string,
        and handles the case when the persisted array is empty by setting a default value.
        """
        if len(persisted_array) == 0:
            return default_value
        else:
            return ",".join(persisted_array)
        
    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
    
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlStatement[0], sqlStatement[1]))    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
                    
    def Next(self):
        """ 
        Function Name: Next
        Function Purpose: This function is executed once the user clicks on the "Next" button. Once the inputs 
        are validated, the inspection results loads the user selected data and is retained at the object class locations 
        before committing to the database. If all inputs are valid and confirmed by the user, the next stage of inspections is executed.
        """
        global blnValidate
        blnValidate = bool(False)             
        
        # First check if the input is empty, if so, notify the user the input needs attention 
        blnValidate = self.Validate_InputFields()
        
        # If status is true then proceed to update the result field, else, reset the fields
        if blnValidate is True:
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to next inspection component?') is True:
                # print(HandleVisSelection.astrHandVisMetSelect)
                # print(HandlePhysSelection.astrHandPhysMetSelect) 
                # Load the user data and prep the data for db dump
                self.Pull_UserInput()     

                # Go to the next inspection component
                self.Next_Inspection()
            else:
                # Check if the user would like to reset the fields
                if messagebox.askyesno(message='ATTENTION! \n\n Would you like to reset the fields?') is True:
                    # Clear the input fields and after data is submitted to the database
                    self.Reset(self)                

    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This function is executed once the user clicks on the reset button inside the root
        frame. If the user clicks 'Reset', all data is set back to default.
        """     
        # Set the list objects first element to the drop click object
        self.dropHandleType.set("")
        self.dropHandleVisStatus.set("")
        self.dropHandlePhysStatus.set("")
        
        # Reset the checkboxes to empty selections
        self.visCheckBox = BaseFunctions.Deselect_All_Checkbox(self.visCheckList)
        self.physCheckBox = BaseFunctions.Deselect_All_Checkbox(self.physCheckList)
        self.functCheckBox = BaseFunctions.Deselect_All_Checkbox(self.functCheckList)

        # Set the first item in the list to the first checkbox item displayed
        self.visCheckList[0].set('1')
        self.physCheckList[0].set('1')
        self.functCheckList[0].set('1')

        # Clear the class objects
        StandardHandelInspect.Reset_Handle_Data(self)
        StandardHandelInspect.Delete_Handle_Data(self)
        
        # Delete the comment field 
        self.commInput.delete("1.0", "end-1c") 

    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Expose the window widget to the user
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """     
        # Open the frame and set the inputs to the class objects
        self.Exit()

        # Show the main window after the new window is closed
        BrakeInspection()        

    def Next_Inspection(self):
        """ 
        Function Name: Next_Inspection
        Function Purpose: This function is executed once the user clicks on Next button to move to the nex inspection
        type window. Withdraw the parent window and load the new window.
        """           
        # Hide the main window
        self.Exit()  

        # Display the overall selections before dumping data to db
        InspectionResults()

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        
                        
#######################################################################################################
# Inspection Results Class
#######################################################################################################   

class InspectionResults(tk.Tk):
    """
    Class Name: InspectionResults
    Class Description: This class is to display the selected inspection components to the user before the 
    data is dumped to the db. User must complete all previous inspection selection modules in order to submit
    data to the database for a standard inspection.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new unit inspection. Display a message
        to the user regarding the protocol for each inspection. User must click 'Check' Button in order to submit
        the data to the db.
        """
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (610/2)     
        self.y = (self.heightSize/2) - (280/2)    
                        
        # Create the Window attributes                
        self.title("Inspection Results")
        self.geometry('%dx%d+%d+%d' % (610, 280, self.x, self.y))
        self.resizable(False, False)

        # Create the scrollbar frame
        self.scrollFrame = LabelFrame(self, text='Results')
        self.scrollFrame.place(x=5, width=600, height=230)  # Adjusted the y-coordinate
        self.resultCanvas = Canvas(self.scrollFrame)
        self.resultCanvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.resultScrollBar = Scrollbar(self.scrollFrame, orient=VERTICAL, command=self.resultCanvas.yview)
        self.resultScrollBar.pack(side=RIGHT, fill=Y)
        self.resultCanvas.configure(yscrollcommand=self.resultScrollBar.set)
        self.resultCanvas.bind('<Configure>', lambda event: self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all")))

        # Create the third frame to hold the result fields
        self.resultFrame = Frame(self.resultCanvas)
        self.resultCanvas.create_window((0,0), window=self.resultFrame, anchor='nw')
        
        # Bind mousewheel scrolling
        self.resultCanvas.bind_all("<MouseWheel>", self.on_vertical_scroll)
        
        # Create the label for the drop down menu lists
        self.lblDeviceName = Label(self.resultFrame, text="Manufacture Name:")
        self.lblSerialNum = Label(self.resultFrame, text="Serial Number:")
        self.lblBumperNum = Label(self.resultFrame, text="Bumper Number:")
        self.lblManDate = Label(self.resultFrame, text="Manufacture Date:")
        self.lblServiceDate = Label(self.resultFrame, text="Service Date:")
        self.lblReserviceDate = Label(self.resultFrame, text="Reservice Date:")
        self.lblInstallDate= Label(self.resultFrame, text="Install Date:")
        self.lblLastInsDate = Label(self.resultFrame, text="Last Inspection Date:")
        self.lblNextInsDate = Label(self.resultFrame, text="Next Inspection Date:")
        self.lblUnitLocation = Label(self.resultFrame, text="Unit Location:")
        self.lblInUse = Label(self.resultFrame, text="Device In Use:")
        self.lblCarabLine = Label(self.resultFrame, text="----------------------------------")
        self.lblCarabType = Label(self.resultFrame, text="Carabiner Type:")
        self.lblCarabVisual = Label(self.resultFrame, text="Visual Component:")
        self.lblCarabPhysical = Label(self.resultFrame, text="Physical Component:")        
        self.lblCarabFunct = Label(self.resultFrame, text="Function Component:")
        self.lblCarabVisualStatus = Label(self.resultFrame, text="Visual Status:")
        self.lblCarabPhysicalStatus = Label(self.resultFrame, text="Physical Status:")
        self.lblCarabFunctStatus = Label(self.resultFrame, text="Function Status:")
        self.lblHandLine = Label(self.resultFrame, text="----------------------------------")
        self.lblHandleType = Label(self.resultFrame, text="Handle Type:")
        self.lblHandleVisual = Label(self.resultFrame, text="Visual Component:")
        self.lblHandlePhysical = Label(self.resultFrame, text="Physical Component:")
        self.lblHandleVisualStatus = Label(self.resultFrame, text="Visual Status:")
        self.lblHandlePhysicalStatus = Label(self.resultFrame, text="Physical Status:")
        self.lblCaseLine = Label(self.resultFrame, text="----------------------------------")
        self.lblCaseComp = Label(self.resultFrame, text="Case Component:")
        self.lblCaseVisual = Label(self.resultFrame, text="Visual Component:")
        self.lblCasePhysical = Label(self.resultFrame, text="Physical Component:")
        self.lblCaseVisualStatus = Label(self.resultFrame, text="Visual Status:")
        self.lblCasePhysicalStatus = Label(self.resultFrame, text="Physical Status:")
        self.lblBrakeLine = Label(self.resultFrame, text="----------------------------------")
        self.lblBrakeComp = Label(self.resultFrame, text="Brake Component:")
        self.lblBrakeVisual = Label(self.resultFrame, text="Visual Component:")
        self.lblBrakePhysical = Label(self.resultFrame, text="Physical Component:")
        self.lblBrakeVisualStatus = Label(self.resultFrame, text="Visual Status:")
        self.lblBrakePhysicalStatus = Label(self.resultFrame, text="Physical Status:")
        self.lblLanyardLine = Label(self.resultFrame, text="----------------------------------")
        self.lblLanyardLen = Label(self.resultFrame, text="Lanyard Length:")
        self.lblLanyardVisual = Label(self.resultFrame, text="Visual Component:")
        self.lblLanyardPhysical = Label(self.resultFrame, text="Physical Component:")
        self.lblRetractFunct = Label(self.resultFrame, text="Function Component:")
        self.lblLanyardVisualStatus = Label(self.resultFrame, text="Visual Status:")
        self.lblLanyardPhysicalStatus = Label(self.resultFrame, text="Physical Status:")
        self.lblRetractFunctStatus = Label(self.resultFrame, text="Function Status:")
        
        # Create the label locations
        self.lblDeviceName.grid(row=0, padx=50, column=0, sticky='W')
        self.lblSerialNum.grid(row=1, padx=50,  column=0, sticky='W')
        self.lblBumperNum.grid(row=2, padx=50,  column=0, sticky='W')
        self.lblManDate.grid(row=3, padx=50,  column=0, sticky='W')
        self.lblServiceDate.grid(row=4, padx=50,  column=0, sticky='W')
        self.lblReserviceDate.grid(row=5, padx=50,  column=0, sticky='W')
        self.lblInstallDate.grid(row=6, padx=50,  column=0, sticky='W')
        self.lblLastInsDate.grid(row=7, padx=50,  column=0, sticky='W')
        self.lblNextInsDate.grid(row=8, padx=50,  column=0, sticky='W')        
        self.lblUnitLocation.grid(row=9, padx=50,  column=0, sticky='W') 
        self.lblInUse.grid(row=10, padx=50,  column=0, sticky='W') 
        self.lblCarabLine.grid(row=11, padx=50,  column=0, sticky='W') 
        self.lblCarabType.grid(row=12, padx=50,  column=0, sticky='W') 
        self.lblCarabVisual.grid(row=13, padx=50,  column=0, sticky='W') 
        self.lblCarabPhysical.grid(row=14, padx=50,  column=0, sticky='W') 
        self.lblCarabFunct.grid(row=15, padx=50,  column=0, sticky='W') 
        self.lblCarabVisualStatus.grid(row=16, padx=50,  column=0, sticky='W') 
        self.lblCarabPhysicalStatus.grid(row=17, padx=50,  column=0, sticky='W') 
        self.lblCarabFunctStatus.grid(row=18, padx=50,  column=0, sticky='W') 
        self.lblHandLine.grid(row=19, padx=50,  column=0, sticky='W') 
        self.lblHandleType.grid(row=20, padx=50,  column=0, sticky='W') 
        self.lblHandleVisual.grid(row=21, padx=50,  column=0, sticky='W') 
        self.lblHandlePhysical.grid(row=22, padx=50,  column=0, sticky='W') 
        self.lblHandleVisualStatus.grid(row=23, padx=50,  column=0, sticky='W') 
        self.lblHandlePhysicalStatus.grid(row=24, padx=50,  column=0, sticky='W') 
        self.lblCaseLine.grid(row=25, padx=50,  column=0, sticky='W')        
        self.lblCaseComp.grid(row=26, padx=50,  column=0, sticky='W') 
        self.lblCaseVisual.grid(row=27, padx=50,  column=0, sticky='W') 
        self.lblCasePhysical.grid(row=28, padx=50,  column=0, sticky='W') 
        self.lblCaseVisualStatus.grid(row=29, padx=50,  column=0, sticky='W') 
        self.lblCasePhysicalStatus.grid(row=30, padx=50,  column=0, sticky='W')          
        self.lblBrakeLine.grid(row=31, padx=50,  column=0, sticky='W') 
        self.lblBrakeComp.grid(row=32, padx=50,  column=0, sticky='W')
        self.lblBrakeVisual.grid(row=33, padx=50,  column=0, sticky='W')
        self.lblBrakePhysical.grid(row=34, padx=50,  column=0, sticky='W') 
        self.lblBrakeVisualStatus.grid(row=35, padx=50,  column=0, sticky='W') 
        self.lblBrakePhysicalStatus.grid(row=36, padx=50,  column=0, sticky='W')
        self.lblLanyardLine.grid(row=37, padx=50,  column=0, sticky='W')              
        self.lblLanyardLen.grid(row=38, padx=50,  column=0, sticky='W')
        self.lblLanyardVisual.grid(row=39, padx=50,  column=0, sticky='W')
        self.lblLanyardPhysical.grid(row=40, padx=50,  column=0, sticky='W')
        self.lblRetractFunct.grid(row=41, padx=50,  column=0, sticky='W')
        self.lblLanyardVisualStatus.grid(row=42, padx=50,  column=0, sticky='W') 
        self.lblLanyardPhysicalStatus.grid(row=43, padx=50,  column=0, sticky='W') 
        self.lblRetractFunctStatus.grid(row=44, padx=50,  column=0, sticky='W')        

        # Create the output boxes to display the results as normal
        self.DeviceNameOutput = Entry(self.resultFrame, width=40, state='normal')
        self.SerialNumOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BumperNumOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ManDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ServiceDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ReserviceOutput = Entry(self.resultFrame, width=40, state='normal')
        self.InstallDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.LastInsDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.NextInsDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.UnitLocationOutput = Entry(self.resultFrame, width=40, state='normal')
        self.InUseOutput = Entry(self.resultFrame, width=40, state='normal')
        self.CarabTypeOutput = Entry(self.resultFrame, width=40, state='normal')
        self.CarabVisualOutput = Entry(self.resultFrame, width=40, state='normal')
        self.CarabPhysicalOutput = Entry(self.resultFrame, width=40, state='normal')
        self.CarabFunctOutput = Entry(self.resultFrame, width=40, state='normal')
        self.CarabVisStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.CarabPhysStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.CarabFunctStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.HandleTypeOutput = Entry(self.resultFrame, width=40, state='normal')
        self.HandleVisualOutput = Entry(self.resultFrame, width=40, state='normal')
        self.HandlePhysicalOutput = Entry(self.resultFrame, width=40, state='normal')
        self.HandleVisStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.HandlePhysStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.CaseCompOutput = Entry(self.resultFrame, width=40, state='normal')
        self.CaseVisualOutput = Entry(self.resultFrame, width=40, state='normal')
        self.CasePhysicalOutput = Entry(self.resultFrame, width=40, state='normal')
        self.CaseVisStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.CasePhysStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BrakeCompOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BrakeVisualOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BrakePhysicalOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BrakeVisStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BrakePhysStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.LanyardLenOutput = Entry(self.resultFrame, width=40, state='normal')
        self.LanyardVisualOutput = Entry(self.resultFrame, width=40, state='normal')
        self.LanyardPhysicalOutput = Entry(self.resultFrame, width=40, state='normal')
        self.RetractFunctOutput = Entry(self.resultFrame, width=40, state='normal')
        self.LanyardVisStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.LanyardPhysStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.RetractFunctStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        
        # Set the last and next inspection date based off of the current date
        aDateResult = BaseFunctions.Update_Inspection_Date()
        LastInspectionDate = datetime.strftime(aDateResult[0], '%Y-%m-%d')
        NextInspectionDate = datetime.strftime(aDateResult[1], '%Y-%m-%d')
                
        # Set the values to the output boxes 
        self.DeviceNameOutput.insert(0, AutoBelay.strDeviceName)
        self.SerialNumOutput.insert(0, AutoBelay.strSerialNum)
        self.BumperNumOutput.insert(0, AutoBelay.strBumperNum)
        self.ManDateOutput.insert(0, AutoBelay.dtmManufactureDate)
        self.ServiceDateOutput.insert(0, AutoBelay.dtmServiceDate)
        self.ReserviceOutput.insert(0, AutoBelay.dtmReserviceDate)
        self.InstallDateOutput.insert(0, AutoBelay.dtmInstallationDate)
        self.LastInsDateOutput.insert(0, LastInspectionDate)
        self.NextInsDateOutput.insert(0, NextInspectionDate)
        self.UnitLocationOutput.insert(0, WallLocation.strWallLocationDesc)
        self.InUseOutput.insert(0, AutoBelay.blnDeviceInUse)
        self.CarabTypeOutput.insert(0, Carabiner.strCarabinerType)
        self.CarabVisualOutput.insert(0, CarabVisSelection.strCarabVisMetSelect)
        self.CarabPhysicalOutput.insert(0, CarabPhysSelection.strCarabPhysMetSelect)
        self.CarabFunctOutput.insert(0, CarabFunctSelection.strCarabFunctSelect)
        self.CarabVisStatusOutput.insert(0, CarabVisSelection.strCarabVisStatus)
        self.CarabPhysStatusOutput.insert(0, CarabPhysSelection.strCarabPhysStatus)
        self.CarabFunctStatusOutput.insert(0, CarabFunctSelection.strCarabFunctStatus)
        self.HandleTypeOutput.insert(0, DeviceHandle.strHandleType)
        self.HandleVisualOutput.insert(0, HandleVisSelection.strHandVisMetSelect)
        self.HandlePhysicalOutput.insert(0, HandlePhysSelection.strHandPhysMetSelect)
        self.HandleVisStatusOutput.insert(0, HandleVisSelection.strHandleVisStatus)
        self.HandlePhysStatusOutput.insert(0, HandlePhysSelection.strHandlePhysStatus)
        self.CaseCompOutput.insert(0, CaseCompSelection.strCaseCompSelect)
        self.CaseVisualOutput.insert(0, CaseVisSelection.strCaseVisMetSelect)
        self.CasePhysicalOutput.insert(0, CasePhysSelection.strCasePhysMetSelect)
        self.CaseVisStatusOutput.insert(0, CaseVisSelection.strCaseVisStatus)
        self.CasePhysStatusOutput.insert(0, CasePhysSelection.strCasePhysStatus)
        self.BrakeCompOutput.insert(0, BrakeCompSelection.strBrakeCompSelect)
        self.BrakeVisualOutput.insert(0, BrakeVisSelection.strBrakeVisMetSelect)
        self.BrakePhysicalOutput.insert(0, BrakePhysSelection.strBrakePhysMetSelect)
        self.BrakeVisStatusOutput.insert(0, BrakeVisSelection.strBrakeVisStatus)
        self.BrakePhysStatusOutput.insert(0, BrakePhysSelection.strBrakePhysStatus)
        self.LanyardLenOutput.insert(0, Lanyard.strLanyardLength)
        self.LanyardVisualOutput.insert(0, LanyardVisSelection.strLanVisTextSelect)
        self.LanyardPhysicalOutput.insert(0, LanyardPhysSelection.strLanPhysTextSelect)
        self.RetractFunctOutput.insert(0, RetractFunctSelection.strRetractFunctSelect)
        self.LanyardVisStatusOutput.insert(0, LanyardVisSelection.strLanVisStatus)
        self.LanyardPhysStatusOutput.insert(0, LanyardPhysSelection.strLanPhysStatus)
        self.RetractFunctStatusOutput.insert(0, RetractFunctSelection.strRetractStatus)

        # Create the output boxes to display the results as readonly after the inputs have been placed
        self.DeviceNameOutput.configure(state='readonly')
        self.SerialNumOutput.configure(state='readonly')
        self.BumperNumOutput.configure(state='readonly')
        self.ManDateOutput.configure(state='readonly')
        self.ServiceDateOutput.configure(state='readonly')
        self.ReserviceOutput.configure(state='readonly')
        self.InstallDateOutput.configure(state='readonly')
        self.LastInsDateOutput.configure(state='readonly')
        self.NextInsDateOutput.configure(state='readonly')
        self.UnitLocationOutput.configure(state='readonly')
        self.InUseOutput.configure(state='readonly')
        self.CarabTypeOutput.configure(state='readonly')
        self.CarabVisualOutput.configure(state='readonly')
        self.CarabPhysicalOutput.configure(state='readonly')
        self.CarabFunctOutput.configure(state='readonly')
        self.CarabVisStatusOutput.configure(state='readonly')
        self.CarabPhysStatusOutput.configure(state='readonly')
        self.CarabFunctStatusOutput.configure(state='readonly')
        self.HandleTypeOutput.configure(state='readonly')
        self.HandleVisualOutput.configure(state='readonly')
        self.HandlePhysicalOutput.configure(state='readonly')
        self.HandleVisStatusOutput.configure(state='readonly')
        self.HandlePhysStatusOutput.configure(state='readonly')
        self.CaseCompOutput.configure(state='readonly')
        self.CaseVisualOutput.configure(state='readonly')
        self.CasePhysicalOutput.configure(state='readonly')
        self.CaseVisStatusOutput.configure(state='readonly')
        self.CasePhysStatusOutput.configure(state='readonly')
        self.BrakeCompOutput.configure(state='readonly')
        self.BrakeVisualOutput.configure(state='readonly')
        self.BrakePhysicalOutput.configure(state='readonly')
        self.BrakeVisStatusOutput.configure(state='readonly')
        self.BrakePhysStatusOutput.configure(state='readonly')
        self.LanyardLenOutput.configure(state='readonly')
        self.LanyardVisualOutput.configure(state='readonly')
        self.LanyardPhysicalOutput.configure(state='readonly')
        self.RetractFunctOutput.configure(state='readonly')
        self.LanyardVisStatusOutput.configure(state='readonly')
        self.LanyardPhysStatusOutput.configure(state='readonly')
        self.RetractFunctStatusOutput.configure(state='readonly')
        
        # Create the grid for the drop down menu list objects
        self.DeviceNameOutput.grid(row=0, column=1)  
        self.SerialNumOutput.grid(row=1, column=1)   
        self.BumperNumOutput.grid(row=2, column=1) 
        self.ManDateOutput.grid(row=3, column=1) 
        self.ServiceDateOutput.grid(row=4, column=1) 
        self.ReserviceOutput.grid(row=5, column=1) 
        self.InstallDateOutput.grid(row=6, column=1)
        self.LastInsDateOutput.grid(row=7, column=1) 
        self.NextInsDateOutput.grid(row=8, column=1)   
        self.UnitLocationOutput.grid(row=9, column=1)
        self.InUseOutput.grid(row=10, column=1)
        self.CarabTypeOutput.grid(row=12, column=1)
        self.CarabVisualOutput.grid(row=13, column=1)
        self.CarabPhysicalOutput.grid(row=14, column=1)
        self.CarabFunctOutput.grid(row=15, column=1)
        self.CarabVisStatusOutput.grid(row=16, column=1)
        self.CarabPhysStatusOutput.grid(row=17, column=1)
        self.CarabFunctStatusOutput.grid(row=18, column=1)
        self.HandleTypeOutput.grid(row=20, column=1)
        self.HandleVisualOutput.grid(row=21, column=1)
        self.HandlePhysicalOutput.grid(row=22, column=1)
        self.HandleVisStatusOutput.grid(row=23, column=1)
        self.HandlePhysStatusOutput.grid(row=24, column=1)        
        self.CaseCompOutput.grid(row=26, column=1)
        self.CaseVisualOutput.grid(row=27, column=1)
        self.CasePhysicalOutput.grid(row=28, column=1)
        self.CaseVisStatusOutput.grid(row=29, column=1)
        self.CasePhysStatusOutput.grid(row=30, column=1)           
        self.BrakeCompOutput.grid(row=32, column=1)
        self.BrakeVisualOutput.grid(row=33, column=1)
        self.BrakePhysicalOutput.grid(row=34, column=1)
        self.BrakeVisStatusOutput.grid(row=35, column=1)
        self.BrakePhysStatusOutput.grid(row=36, column=1)           
        self.LanyardLenOutput.grid(row=38, column=1)
        self.LanyardVisualOutput.grid(row=39, column=1)
        self.LanyardPhysicalOutput.grid(row=40, column=1)
        self.RetractFunctOutput.grid(row=41, column=1)
        self.LanyardVisStatusOutput.grid(row=42, column=1)
        self.LanyardPhysStatusOutput.grid(row=43, column=1)           
        self.RetractFunctStatusOutput.grid(row=44, column=1)
        
        # Create the buttons
        self.btnExit = Button(self, text="Exit", width=10, command=self.Exit)
        self.btnSubmit = Button(self, text="Submit", width=10, command=self.Submit)
        self.btnBack = Button(self, text="Back", width=10, command=self.Back)
            
        # Create the position of the button
        self.btnBack.place(x=140, y=240)
        self.btnSubmit.place(x=270, y=240)
        self.btnExit.place(x=400, y=240)

        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()    

        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the stored data in the class attributes
        StandardCarabinerInspect.Delete_Carabiner_Data(self)
        StandardLanyardInspect.Delete_Lanyard_Data(self)
        StandardCaseInspect.Delete_Case_Data(self)
        StandardBrakeInspect.Delete_Brake_Data(self)
        StandardHandelInspect.Delete_Handle_Data(self)
                
        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)
        AutoBelay_Menu()         

    def on_vertical_scroll(self, event):
        """Scroll the canvas vertically using the mouse wheel."""
        self.resultCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        
    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the new location to the db. Else, reset
        """
        # Check first with the user if the entry's are correct before dumping to DB
        if messagebox.askyesno(message='CAUTION! \n\n Proceed to submit Auto Belay inspection?') is True:     
            # Load the user data and prep the data for db dump
            InspectionResults.Submit_Standard_Inspection(self)
            
            # Check if the user would like to add another inspection
            if messagebox.askyesno(message='SUCCESSFUL UPLOAD! \n\n Would you like to complete another inspection?') is True:
                # Clear the input fields and after data is submitted to the database
                InspectionResults.Exit(self)
                AutoBelaySelection()
            else:
                InspectionResults.Exit(self)
                AutoBelay_Menu()
        else:
            pass  

    def Submit_Standard_Inspection(self):
        """ 
        Function Name: Submit_Standard_Inspection
        Function Purpose: This function is executed once the user clicks on the submit button and all the standard
        inspection data cached arrays will be pulled and dumped into the the database
        """    
        # Set the global AutoBelay Attributes
        AutoBelay.Update_AutoBelay_Inspect_Dates(AutoBelay)        
        
        # Commit the Carabiner Inspection data to the database
        CarabVisSelection.Add_CarabVisSelection_Query(self)
        CarabPhysSelection.Add_CarabPhysSelection_Query(self)
        CarabFunctSelection.Add_CarabFunctSelection_Query(self)
        CarabinerVisualInspect.Add_CarabinerVisualInspect_Query(self)
        CarabinerPhysicalInspect.Add_CarabinerPhysicalInspect_Query(self)
        CarabinerFunctionInspect.Add_CarabinerFunctInspect_Query(self)
        StandardCarabinerInspect.Add_StandCarabinerInspect_Query(self)
        
        # Commit the Lanyard Inspection data to the database
        LanyardVisSelection.Add_LanyardVisSelectList_Query(self)
        LanyardPhysSelection.Add_LanyardPhysSelectList_Query(self)
        RetractFunctSelection.Add_RetractFunctSelection_Query(self)
        LanyardVisualInspect.Add_LanyardVisualInspect_Query(self)
        LanyardPhysicalInspect.Add_LanyardPhysicalInspect_Query(self)
        LanyardFunctionInspect.Add_LanyardFunctInspect_Query(self)
        StandardLanyardInspect.Add_StandLanyardInspect_Query(self)
                
        # Commit the Handle Inspection data to the database
        HandleVisSelection.Add_HandVisSelection_Query(self)
        HandlePhysSelection.Add_HandPhysSelection_Query(self)
        HandleVisualInspect.Add_HandelVisInspect_Query(self)
        HandlePhysicalInspect.Add_HandelPhysInspect_Query(self)
        StandardHandelInspect.Add_StandHandleInspect_Query(self)
        
        # Commit the Brake Inspection data to the database
        BrakeCompSelection.Add_BrakeCompSelection_Query(self)
        BrakeVisSelection.Add_BrakeVisSelectList_Query(self)
        BrakePhysSelection.Add_BrakePhysSelectList_Query(self)
        BrakeVisualInspect.Add_BrakeVisualInspect_Query(self)
        BrakePhysicalInspect.Add_BrakePhysicalInspect_Query(self)
        StandardBrakeInspect.Add_StandBrakeInspect_Query(self)
        
        # Commit the Case Inspection data to the database
        CaseCompSelection.Add_CaseCompSelection_Query(self)
        CaseVisSelection.Add_CaseVisSelection_Query(self)
        CasePhysSelection.Add_CasePhysSelection_Query(self)
        CaseVisualInspect.Add_CaseVisualInspect_Query(self)
        CasePhysicalInspect.Add_CasePhysicalInspect_Query(self)
        StandardCaseInspect.Add_StandCaseInspect_Query(self)
        
        # Commit the Standard Inspection data to the database
        StandardInspect.Add_StandInspect_Query(self)

        # Get the AutoBelay overall status and update the units in use status 
        AutoBelay.Update_AutoBelay_InUse_Status(AutoBelay)
        
        # Commit the AutoBelayInspection data to the database
        AutoBelayInspect.Add_AutoBelayInspection_Query(self)
        AutoBelayInspect.Add_AutoBelayInspector_Query(self)
        AutoBelayInspect.Add_AutoBelayLocation_Query(self)
        
        # First check if the unit has been packaged for reservice to add report to db
        if Bool_Flag.Get_OutForService_Bool_Value(Bool_Flag) is True:
            AutoBelayReserviceReport.Add_AutoBelay_ReserviceReport_Query(self)
            
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)
        
        # Delete the stored data in the class attributes
        StandardCarabinerInspect.Delete_Carabiner_Data(self)
        StandardLanyardInspect.Delete_Lanyard_Data(self)
        StandardCaseInspect.Delete_Case_Data(self)
        StandardBrakeInspect.Delete_Brake_Data(self)
        StandardHandelInspect.Delete_Handle_Data(self)
        AutoBelayInspect.Delete_AutoBelayInspect_Data(self)        
        AutoBelayReserviceReport.Delete_AutoBelay_ReserviceReport_Data(self)
        Start_Menu.Delete_Obj_Lists(self)        

        # Reload the object lists
        Start_Menu.Load_Obj_Lists(Start_Menu)
                
    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Expose the window widget to the user
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """     
        # Hide the current window
        self.Exit()  

        # Show the main window after the new window is closed
        HandleInspection()

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        
        
#######################################################################################################
# View Last/Next Inspection Dates Class
#######################################################################################################  

class View_LastNext_InspectDate(tk.Tk):
    """
    Class Name: View_LastNext_InspectDate
    Class Description: This class views all of the last and next inspection dates and highlights the dates due for
    immediate or upcoming inspection dates based off the parameters of less than 7 days and or less than 14 days.
    """
    def __init__(self, Class_CallerID=""):
        self.Class_CallerID = Class_CallerID
        
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (620/2)     
        self.y = (self.heightSize/2) - (360/2)    
                
        # Create the Window attributes
        self.WindowTitle = self.title("Future Inspections")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (620, 360, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Create the multi line text field
        self.frameMSG = LabelFrame(self, text="Inspection Message")
        self.frameMSG.place(x=5, y=0, width=610, height=100)

        # Create the display message for the new inspection
        self.DisplayMessage = str(
        """
        Items highlighted in 'Yellow' indicate an upcoming inspection within the next 4 days or more. 
        Those highlighted in 'Red' signal an inspection that is either overdue or due within the next 3 days. 
        Items without highlights are currently not in need of immediate inspection.
        """)
                
        # Create the label for the display message
        self.InstructMessage = Label(self.frameMSG, text=self.DisplayMessage)
        self.InstructMessage.grid(row=0, column=0, padx=15)

        # Create the main frame for headers and data
        self.mainFrame = Frame(self)
        self.mainFrame.place(x=5, y=105, width=610, height=215)

        # Header Frame
        self.headerFrame = Frame(self.mainFrame)
        self.headerFrame.pack(side=TOP, fill=X, padx=2)

        # Scrollable Frame for Data
        self.scrollFrame = Frame(self.mainFrame)
        self.scrollFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

        # Canvas and Scrollbar for the scrollable Frame
        self.resultCanvas = Canvas(self.scrollFrame)
        self.resultCanvas.pack(side=LEFT, fill=BOTH, expand=True, padx=0)
        self.resultScrollBar = Scrollbar(self.scrollFrame, orient=VERTICAL, command=self.resultCanvas.yview)
        self.resultScrollBar.pack(side=RIGHT, fill=Y)
        self.resultCanvas.configure(yscrollcommand=self.resultScrollBar.set)

        # Frame for Data inside Canvas
        self.resultFrame = Frame(self.resultCanvas)
        self.resultCanvas.create_window((0,0), window=self.resultFrame, anchor='nw')

        # Configure the scroll region dynamically
        self.resultFrame.bind('<Configure>', self.onFrameConfigure)
                
        # Bind mousewheel scrolling
        self.resultCanvas.bind_all("<MouseWheel>", self.on_vertical_scroll)

        # Create the columns 
        self.columns = ["Serial Number", "Bumper Number", "Last Inspection", "Next Inspection"]
        
        # Get the data from the database for the view 
        sqlViewList = ("vAutoBelayLastNextInspectDates", "vRopeLastNextInspectDates", "vConnectorLastNextInspectDates",
                    "vBelayDeviceLastNextInspectDates")
        
        # Determine the caller ID to execute the view
        if self.Class_CallerID == "AutoBelay":
            sqlView = sqlViewList[0]
        elif self.Class_CallerID == "Rope":
            sqlView = sqlViewList[1]
        elif self.Class_CallerID == "Connector":
            sqlView = sqlViewList[2]
        elif self.Class_CallerID == "BelayDevice":
            sqlView = sqlViewList[3]
            
        # Call the query function
        self.sqlResultQuery = Queries.Get_All_DB_Values(self, sqlView)
        
        # Create timedelta variables to calculate the days remaining
        self.dtmWARNING_MIN = timedelta(days=3)
        self.dtmWARNING_MAX = timedelta(days=7)
        self.dtmMONTH_COUNT = timedelta(days=30)
        self.dtmToday = date.today()
        self.dtmToday = datetime.strptime(str(self.dtmToday), '%Y-%m-%d')

        # Create the header for the rows for the grid
        for col_index, col in enumerate(self.columns):
            Label(self.headerFrame, text=col, relief=RIDGE, width=20).grid(row=0, column=col_index)

        # Populate the grid with data
        for row_index, row_data in enumerate(self.sqlResultQuery):
            # First check if row_data entries are already datetime.date, if not, convert them.
            self.lastDate = row_data[2] if isinstance(row_data[2], date) else datetime.strptime(row_data[2], '%Y-%m-%d')
            self.nextDate = row_data[3] if isinstance(row_data[3], date) else datetime.strptime(row_data[3], '%Y-%m-%d')
            
            for col_index, cell_value in enumerate(row_data):
                # Create the data labels
                self.DataLabel = Label(self.resultFrame, text=cell_value, relief=RIDGE, width=20)
                
                if self.columns[col_index] == "Next Inspection":
                    if self.nextDate > self.dtmToday:
                        # Calculate the days remaining 
                        self.daysRemain = (self.nextDate - self.dtmToday)
                        
                        # Conditional determining the type of warning 
                        if self.daysRemain <= self.dtmWARNING_MIN:
                            self.DataLabel.configure(bg='#ff4e01')                   
                        elif self.daysRemain > self.dtmWARNING_MIN and self.daysRemain <= self.dtmWARNING_MAX:
                            self.DataLabel.configure(bg='#fefe00')         
                    else:
                        # Calculate the days overdue 
                        self.daysOverdue = (self.nextDate - self.dtmToday)
                        
                        # Conditional determining the type of warning
                        if self.daysOverdue <= self.dtmWARNING_MIN:
                            self.DataLabel.configure(background='#ff4e01')                      
                        elif self.daysOverdue > self.dtmWARNING_MIN and self.daysOverdue <= self.dtmWARNING_MAX:
                            self.DataLabel.configure(background='#fefe00')       
            
                # Increment the grid
                self.DataLabel.grid(row=row_index+1, column=col_index)

        # Add the exit button
        self.btnBack = Button(self, text="Back", width=10, command=self.Exit)                
        self.btnBack.place(x=265, y=325)
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()

        # Open the Main Menu
        self.Identify_Class_Return()

    def onFrameConfigure(self, event):
        """ 
        Function Name: onFrameConfigure
        Function Purpose: This function resets the scroll region to encompass the inner frame
        """           
        self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all"))

    def on_vertical_scroll(self, event):
        """Scroll the canvas vertically using the mouse wheel."""
        self.resultCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
                                
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        self.Identify_Class_Return()

    def Identify_Class_Return(self):
        """ 
        Function Name: Identify_Class_Return
        Function Purpose: This function is executed when the calls caller ID is identified and returns control
        back to the desired menu
        """      
        Start_Menu.Delete_Obj_Lists(Start_Menu)
        
        # Determine which class menu control needs to return to 
        if self.Class_CallerID == "AutoBelay":
            AutoBelay_Menu()
        elif self.Class_CallerID == "Rope":
            Ropes_Menu()
        elif self.Class_CallerID == "Connector":
            Connectors_Menu()
        elif self.Class_CallerID == "BelayDevice":
            BelayDevices_Menu()
            
        
#######################################################################################################
# View Service/Reservice Dates Class
#######################################################################################################

class View_Service_InspectDate(tk.Tk):
    """
    Class Name: View_Service_InspectDate
    Class Description: This class views all of the service and reservice inspection dates and highlights the dates due for
    immediate or upcoming inspection dates based off the parameters of less than 75 days and or less than 45 days.
    """
    def __init__(self):
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (620/2)     
        self.y = (self.heightSize/2) - (380/2) 
                
        # Create the Window attributes
        self.WindowTitle = self.title("Service/Re-service Inspections")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (620, 380, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Create the multi line text field
        self.frameMSG = LabelFrame(self, text="Inspection Message")
        self.frameMSG.place(x=5, y=0, width=610, height=115)

        # Create the display message for the new inspection
        self.DisplayMessage = str(
        """
        Please note that units marked with a 'Yellow' highlight are scheduled for re-servicing within the next
        75 days. Units that are highlighted in 'Red' may either be past due for their scheduled re-servicing
        or are approaching the due date within 45 days or fewer. Units without highlights are currently not
        in need of immediate re-servicing.
        """)
                
        # Create the label for the display message
        self.InstructMessage = Label(self.frameMSG, text=self.DisplayMessage)
        self.InstructMessage.grid(row=0, column=0, padx=10)

        # Create the main frame for headers and data
        self.mainFrame = Frame(self)
        self.mainFrame.place(x=5, y=120, width=610, height=215)

        # Header Frame
        self.headerFrame = Frame(self.mainFrame)
        self.headerFrame.pack(side=TOP, fill=X, padx=2)

        # Scrollable Frame for Data
        self.scrollFrame = Frame(self.mainFrame)
        self.scrollFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

        # Canvas and Scrollbar for the scrollable Frame
        self.resultCanvas = Canvas(self.scrollFrame)
        self.resultCanvas.pack(side=LEFT, fill=BOTH, expand=True, padx=0)
        self.resultScrollBar = Scrollbar(self.scrollFrame, orient=VERTICAL, command=self.resultCanvas.yview)
        self.resultScrollBar.pack(side=RIGHT, fill=Y)
        self.resultCanvas.configure(yscrollcommand=self.resultScrollBar.set)

        # Frame for Data inside Canvas
        self.resultFrame = Frame(self.resultCanvas)
        self.resultCanvas.create_window((0,0), window=self.resultFrame, anchor='nw')

        # Configure the scroll region dynamically
        self.resultFrame.bind('<Configure>', self.onFrameConfigure)
                
        # Bind mousewheel scrolling
        self.resultCanvas.bind_all("<MouseWheel>", self.on_vertical_scroll)

        # Create the columns 
        self.columns = ["Serial Number", "Bumper Number", "Service Date", "Re-service Date"]
        
        # Get the data from the database for the view vABServiceDates
        sqlView = "vABServiceDates"
        
        # Call the query function
        self.sqlResultQuery = Queries.Get_All_DB_Values(self, sqlView)
        
        # Create timedelta variables to calculate the days remaining
        self.dtmWARNING_MIN = timedelta(days=45)
        self.dtmWARNING_MAX = timedelta(days=75)
        self.dtmMONTH_COUNT = timedelta(days=30)
        self.dtmToday = date.today()
        self.dtmToday = datetime.strptime(str(self.dtmToday), '%Y-%m-%d')

        # Create the header for the rows for the grid
        for col_index, col in enumerate(self.columns):
            Label(self.headerFrame, text=col, relief=RIDGE, width=20).grid(row=0, column=col_index)
            
        # Populate the grid with data
        for row_index, row_data in enumerate(self.sqlResultQuery):
            # Create a new list holding the values at rowIndex
            self.serviceDate = datetime.strptime(row_data[2], '%Y-%m-%d')
            self.reserviceDate = datetime.strptime(row_data[3], '%Y-%m-%d')

            for col_index, cell_value in enumerate(row_data):
                # Create the data labels
                self.DataLabel = Label(self.resultFrame, text=cell_value, relief=RIDGE, width=20)

                if self.columns[col_index] == "Re-service Date":
                    if self.reserviceDate > self.dtmToday:
                        # Calculate the days remaining 
                        self.daysRemain = (self.reserviceDate - self.dtmToday)

                        # Conditional determining the type of warning 
                        if self.daysRemain <= self.dtmWARNING_MIN:
                            self.DataLabel.configure(bg='#ff4e01')                   
                        elif self.daysRemain > self.dtmWARNING_MIN and self.daysRemain <= self.dtmWARNING_MAX:
                            self.DataLabel.configure(bg='#fefe00')         
                    else:
                        # Calculate the days overdue 
                        self.daysOverdue = (self.reserviceDate - self.dtmToday)
                        
                        # Conditional determining the type of warning
                        if self.daysOverdue <= self.dtmWARNING_MIN:
                            self.DataLabel.configure(background='#ff4e01')                      
                        elif self.daysOverdue > self.dtmWARNING_MIN and self.daysOverdue <= self.dtmWARNING_MAX:
                            self.DataLabel.configure(background='#fefe00')     

                # Increment the grid
                self.DataLabel.grid(row=row_index+1, column=col_index)
                
        # Add the exit button
        self.btnBack = Button(self, text="Back", width=10, command=self.Exit)                
        self.btnBack.place(x=265, y=343)
                                
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)
        AutoBelay_Menu() 

    def onFrameConfigure(self, event):
        """ 
        Function Name: onFrameConfigure
        Function Purpose: This function resets the scroll region to encompass the inner frame
        """           
        self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all"))

    def on_vertical_scroll(self, event):
        """Scroll the canvas vertically using the mouse wheel."""
        self.resultCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
                    
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        Start_Menu.Delete_Obj_Lists(Start_Menu)
        AutoBelay_Menu()        


#######################################################################################################
# View AutoBelay Dates Class
#######################################################################################################    
    
class View_AutoBelayDates(tk.Tk):
    """
    Class Name: View_AutoBelayDates
    Class Description:  This class views all of the AutoBelay Dates
    """
    def __init__(self):
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (905/2)     
        self.y = (self.heightSize/2) - (340/2)    
                
        # Create the Window attributes
        self.WindowTitle = self.title("Auto Belay Date Information")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (905, 340, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Main Frame for Header and Data
        self.mainFrame = Frame(self)
        self.mainFrame.place(x=5, y=5, width=895, height=265)

        # Header Frame and Canvas
        self.headerCanvas = Canvas(self.mainFrame, height=25, highlightthickness=0, bg='gray')
        self.headerCanvas.pack(side=TOP, fill=X)
        self.headerFrame = Frame(self.headerCanvas)
        self.headerCanvas.create_window((0, 0), window=self.headerFrame, anchor='nw')

        # Scrollable Frame for Data
        self.scrollFrame = Frame(self.mainFrame)
        self.scrollFrame.place(x=0, y=25, width=895, height=240)

        # Canvas for Scrollable Content
        self.resultCanvas = Canvas(self.scrollFrame, highlightthickness=0)
        self.resultCanvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Vertical Scrollbar
        self.resultScrollBarV = Scrollbar(self.scrollFrame, orient=VERTICAL, command=self.resultCanvas.yview)

        # Horizontal Scrollbar at the bottom of the main frame, not the scroll frame
        self.resultScrollBarH = Scrollbar(self, orient=HORIZONTAL, command=self.resultCanvas.xview)
        self.resultScrollBarH.place(x=0, y=270, width=895, height=20)

        # Configure Canvas Scrollbars
        self.resultCanvas.configure(yscrollcommand=self.resultScrollBarV.set, xscrollcommand=self.resultScrollBarH.set)
        self.headerCanvas.configure(xscrollcommand=self.resultScrollBarH.set)

        # Frame for Data inside Canvas
        self.resultFrame = Frame(self.resultCanvas)
        self.resultCanvas.create_window((0, 0), window=self.resultFrame, anchor='nw')

        # Configure Scroll Region
        self.resultFrame.bind("<Configure>", self.onFrameConfigure)
        self.headerCanvas.bind("<Configure>", lambda e: self.headerCanvas.configure(scrollregion=self.headerCanvas.bbox("all")))

        # Bind mousewheel scrolling
        self.resultCanvas.bind_all("<MouseWheel>", self.on_vertical_scroll)
        
        # Create the columns 
        self.columns = ["Serial Number",  "Bumper Number", "Manufacture Date", "Service Date",  "Reservice Date",  "Installation Date", "Last Inspection", "Next Inspection"]
        
        # Get the data from the database for the view vAutoBelayDates
        sqlView = "vAutoBelayDates"
        
        # Call the query function
        self.sqlResultQuery = Queries.Get_All_DB_Values(self, sqlView)
        
        # Create the header for the rows for the grid
        for col_index, col in enumerate(self.columns):
            Label(self.headerFrame, text=col, relief=RIDGE, width=20).grid(row=0, column=col_index)
            
        # Populate the grid with data
        for row_index, row_data in enumerate(self.sqlResultQuery):
            for col_index, cell_value in enumerate(row_data):
                # Create the data labels
                self.DataLabel = Label(self.resultFrame, text=cell_value, relief=RIDGE, width=20).grid(row=row_index+1, column=col_index)

        # Add the exit button
        self.btnBack = Button(self, text="Back", width=10, command=self.Exit)                
        self.btnBack.place(x=405, y=295)
                    
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)
        AutoBelay_Menu() 

    def on_horizontal_scroll(self, *args):
        """Synchronize horizontal scrolling between header and data canvases."""
        # Update the xview (horizontal view) of the result canvas based on the scrollbar's action
        self.resultCanvas.xview(*args)
        
        # Get the current horizontal scroll position of the result canvas
        scroll_pos = self.resultCanvas.xview()
        
        # Apply the same horizontal scroll position to the header canvas
        self.headerCanvas.xview_moveto(scroll_pos[0])

    def on_vertical_scroll(self, event):
        """Scroll the canvas vertically using the mouse wheel."""
        self.resultCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
            
    def onFrameConfigure(self, event):
        """This function resets the scroll region to encompass the inner frame and hides/shows the scrollbar as needed."""
        self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all"))
        # Set the header canvas to the same horizontal position as the result canvas
        self.headerCanvas.xview_moveto(self.resultCanvas.xview()[0])
                
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        Start_Menu.Delete_Obj_Lists(Start_Menu)
        AutoBelay_Menu()
        

#######################################################################################################
# View Item Dates Class
#######################################################################################################    
    
class View_ItemDates(tk.Tk):
    """
    Class Name: View_ItemDates
    Class Description:  This class views all of the Items Dates
    """
    def __init__(self, Class_CallerID=""):
        self.Class_CallerID = Class_CallerID
        
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (910/2)     
        self.y = (self.heightSize/2) - (270/2)    
        
        # Create the title for the window
        astrTitleList = ("Rope Date Information", "Connector Date Information", "Belay Device Date Information")
        
        # Determine the caller ID to execute the title
        if self.Class_CallerID == "Rope":
            strTitle = astrTitleList[0]
        elif self.Class_CallerID == "Connector":
            strTitle = astrTitleList[1]
        elif self.Class_CallerID == "BelayDevice":
            strTitle = astrTitleList[2]
        
        # Create the Window attributes
        self.WindowTitle = self.title(strTitle)
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (910, 270, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Create the main frame for headers and data
        self.mainFrame = Frame(self)
        self.mainFrame.place(x=5, y=5, width=900, height=225)

        # Header Frame
        self.headerFrame = Frame(self.mainFrame)
        self.headerFrame.pack(side=TOP, fill=X, padx=2)

        # Scrollable Frame for Data
        self.scrollFrame = Frame(self.mainFrame)
        self.scrollFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

        # Canvas and Scrollbar for the scrollable Frame
        self.resultCanvas = Canvas(self.scrollFrame)
        self.resultCanvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.resultScrollBar = Scrollbar(self.scrollFrame, orient=VERTICAL, command=self.resultCanvas.yview)
        self.resultScrollBar.pack(side=RIGHT, fill=Y)
        self.resultCanvas.configure(yscrollcommand=self.resultScrollBar.set)

        # Frame for Data inside Canvas
        self.resultFrame = Frame(self.resultCanvas)
        self.resultCanvas.create_window((0,0), window=self.resultFrame, anchor='nw')

        # Configure the scroll region dynamically
        self.resultFrame.bind('<Configure>', self.onFrameConfigure)
        
        # Bind the canvas to the mouse wheel
        self.resultCanvas.bind_all("<MouseWheel>", lambda event: self.resultCanvas.yview_scroll(-1*(event.delta//1), "units"))
        self.resultCanvas.bind_all("<MouseWheel>", lambda event: self.resultCanvas.yview_scroll(-1*(event.delta*1), "units"))

        # Get the data from the database for the view 
        sqlViewList = ("vRopeDates", "vConnectorDates", "vBelayDeviceDates")
        
        # Determine the caller ID to execute the view
        if self.Class_CallerID == "Rope":
            sqlView = sqlViewList[0]
        elif self.Class_CallerID == "Connector":
            sqlView = sqlViewList[1]
        elif self.Class_CallerID == "BelayDevice":
            sqlView = sqlViewList[2]
        
        # Call the query function
        self.sqlResultQuery = Queries.Get_All_DB_Values(self, sqlView)
        
        # Create the column headers in the headerFrame
        self.columns = ["Serial Number",  "Bumper Number", "Manufacture Date", "Installation Date", "Last Inspection", "Next Inspection"]
        for col_index, col in enumerate(self.columns):
            Label(self.headerFrame, text=col, relief=RIDGE, width=20).grid(row=0, column=col_index)

        # Populate the grid with data in the resultFrame
        for row_index, row_data in enumerate(self.sqlResultQuery):
            for col_index, cell_value in enumerate(row_data):
                Label(self.resultFrame, text=cell_value, relief=RIDGE, width=20).grid(row=row_index, column=col_index)

        # Add the exit button
        self.btnBack = Button(self, text="Back", width=10, command=self.Exit)                
        self.btnBack.place(x=405, y=237)
                    
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()
        
        # Open the Main Menu
        self.Identify_Class_Return()

    def onFrameConfigure(self, event):
        """ 
        Function Name: onFrameConfigure
        Function Purpose: This function resets the scroll region to encompass the inner frame
        """           
        self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all"))
                
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        self.Identify_Class_Return()

    def Identify_Class_Return(self):
        """ 
        Function Name: Identify_Class_Return
        Function Purpose: This function is executed when the calls caller ID is identified and returns control
        back to the desired menu
        """      
        Start_Menu.Delete_Obj_Lists(Start_Menu)
        
        # Determine which class menu control needs to return to 
        if self.Class_CallerID == "Rope":
            Ropes_Menu()
        elif self.Class_CallerID == "Connector":
            Connectors_Menu()
        elif self.Class_CallerID == "BelayDevice":
            BelayDevices_Menu()

                
#######################################################################################################
# View Items Wall Locations Class
####################################################################################################### 

class View_Item_WallLocations(tk.Tk):
    """
    Class Name: View_Item_WallLocations
    Class Description:  This class views all of the Items Wall Locations
    """
    def __init__(self, Class_CallerID=""):
        self.Class_CallerID = Class_CallerID
        
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (470/2)     
        self.y = (self.heightSize/2) - (245/2)    

        # Create the title for the window
        astrTitleList = ("Auto Belay Wall Locations", "Rope Wall Locations", "Connector Wall Locations", "Belay Device Wall Locations")
        
        # Determine the caller ID to execute the title
        if self.Class_CallerID == "AutoBelay":
            strTitle = astrTitleList[0]
        elif self.Class_CallerID == "Rope":
            strTitle = astrTitleList[1]
        elif self.Class_CallerID == "Connector":
            strTitle = astrTitleList[2]
        elif self.Class_CallerID == "BelayDevice":
            strTitle = astrTitleList[3]
                            
        # Create the Window attributes
        self.WindowTitle = self.title(strTitle)
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (470, 245, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Create the main frame for headers and data
        self.mainFrame = Frame(self)
        self.mainFrame.place(x=5, y=5, width=460, height=190)

        # Header Frame
        self.headerFrame = Frame(self.mainFrame)
        self.headerFrame.pack(side=TOP, fill=X, padx=2)

        # Scrollable Frame for Data
        self.scrollFrame = Frame(self.mainFrame)
        self.scrollFrame.pack(side=BOTTOM, fill=BOTH, expand=True)
        self.resultCanvas = Canvas(self.scrollFrame)
        self.resultCanvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.resultScrollBar = Scrollbar(self.scrollFrame, orient=VERTICAL, command=self.resultCanvas.yview)
        self.resultScrollBar.pack(side=RIGHT, fill=Y)
        self.resultCanvas.configure(yscrollcommand=self.resultScrollBar.set)
        self.resultCanvas.bind('<Configure>', lambda event: self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all")))
        
        # Create the third frame to hold the result fields
        self.resultFrame = Frame(self.resultCanvas)
        self.resultCanvas.create_window((0,0), window=self.resultFrame, anchor='nw')
        
        # Bind mousewheel scrolling
        self.resultCanvas.bind_all("<MouseWheel>", self.on_vertical_scroll)

        # Get the data from the database for the view 
        sqlViewList = ("vAutoBelayWallLocations", "vRopeWallLocations", "vConnectorWallLocations", "vBelayDeviceWallLocations")
        
        # Determine the caller ID to execute the view
        if self.Class_CallerID == "AutoBelay":
            sqlView = sqlViewList[0]
        elif self.Class_CallerID == "Rope":
            sqlView = sqlViewList[1]
        elif self.Class_CallerID == "Connector":
            sqlView = sqlViewList[2]
        elif self.Class_CallerID == "BelayDevice":
            sqlView = sqlViewList[3]
            
        # Call the query function
        self.sqlResultQuery = Queries.Get_All_DB_Values(self, sqlView)
        
        # Create the column headers in the headerFrame
        self.columns = ["Serial Number", "Bumper Number", "Wall Location"]
        for col_index, col in enumerate(self.columns):
            Label(self.headerFrame, text=col, relief=RIDGE, width=20).grid(row=0, column=col_index)
            
        # Populate the grid with data
        for row_index, row_data in enumerate(self.sqlResultQuery):
            for col_index, cell_value in enumerate(row_data):
                # Create the data labels
                self.DataLabel = Label(self.resultFrame, text=cell_value, relief=RIDGE, width=20).grid(row=row_index+1, column=col_index)

        # Add the exit button
        self.btnBack = Button(self, text="Back", width=10, command=self.Exit)                
        self.btnBack.place(x=190, y=205)
                    
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()
                                
        # Open the Main Menu
        self.Identify_Class_Return()

    def onFrameConfigure(self, event):
        """ 
        Function Name: onFrameConfigure
        Function Purpose: This function resets the scroll region to encompass the inner frame
        """           
        self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all"))

    def on_vertical_scroll(self, event):
            """Scroll the canvas vertically using the mouse wheel."""
            self.resultCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
                            
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        self.Identify_Class_Return()

    def Identify_Class_Return(self):
        """ 
        Function Name: Identify_Class_Return
        Function Purpose: This function is executed when the calls caller ID is identified and returns control
        back to the desired menu
        """      
        Start_Menu.Delete_Obj_Lists(Start_Menu)
        
        # Determine which class menu control needs to return to 
        if self.Class_CallerID == "AutoBelay":
            AutoBelay_Menu()
        elif self.Class_CallerID == "Rope":
            Ropes_Menu()
        elif self.Class_CallerID == "Connector":
            Connectors_Menu()
        elif self.Class_CallerID == "BelayDevice":
            BelayDevices_Menu()      
        
        
#######################################################################################################
# View Rope Information Class
####################################################################################################### 

class View_Rope_Info(tk.Tk):
    """
    Class Name: View_Rope_Info
    Class Description:  This class views all of the Rope Information
    """
    def __init__(self):
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (905/2)     
        self.y = (self.heightSize/2) - (280/2)    

        # Create the Window attributes
        self.WindowTitle = self.title("Rope Information")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (905, 280, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Main Frame for Header and Data
        self.mainFrame = Frame(self)
        self.mainFrame.place(x=5, y=5, width=895, height=225)

        # Header Frame and Canvas
        self.headerCanvas = Canvas(self.mainFrame, height=25, highlightthickness=0, bg='gray')
        self.headerCanvas.pack(side=TOP, fill=X)
        self.headerFrame = Frame(self.headerCanvas)
        self.headerCanvas.create_window((0, 0), window=self.headerFrame, anchor='nw')

        # Scrollable Frame for Data
        self.scrollFrame = Frame(self.mainFrame)
        self.scrollFrame.place(x=0, y=25, width=895, height=200)

        # Canvas for Scrollable Content
        self.resultCanvas = Canvas(self.scrollFrame, highlightthickness=0)
        self.resultCanvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Vertical Scrollbar
        self.resultScrollBarV = Scrollbar(self.scrollFrame, orient=VERTICAL, command=self.resultCanvas.yview)

        # Horizontal Scrollbar at the bottom of the main frame, not the scroll frame
        self.resultScrollBarH = Scrollbar(self.mainFrame, orient=HORIZONTAL, command=self.resultCanvas.xview)
        self.resultScrollBarH.place(x=0, y=205, width=895, height=20)

        # Configure Canvas Scrollbars
        self.resultCanvas.configure(yscrollcommand=self.resultScrollBarV.set, xscrollcommand=self.resultScrollBarH.set)
        self.headerCanvas.configure(xscrollcommand=self.resultScrollBarH.set)

        # Frame for Data inside Canvas
        self.resultFrame = Frame(self.resultCanvas)
        self.resultCanvas.create_window((0, 0), window=self.resultFrame, anchor='nw')

        # Configure Scroll Region
        self.resultFrame.bind("<Configure>", self.onFrameConfigure)
        self.headerCanvas.bind("<Configure>", lambda e: self.headerCanvas.configure(scrollregion=self.headerCanvas.bbox("all")))

        # Bind mousewheel scrolling
        self.resultCanvas.bind_all("<MouseWheel>", self.on_vertical_scroll)

        # Get the data from the database for the view 
        sqlView = "vRopes"
            
        # Call the query function
        self.sqlResultQuery = Queries.Get_All_DB_Values(self, sqlView)
        
        # Create the column headers in the headerFrame
        self.columns = ["Serial Number", "Bumper Number", "Rope Length", "Diameter", "Elasticity", "Manufacture Name", "Manufacture Date",
                        "Install Date", "Last Inspection", "Next Inspection", "In Use Status"]
        for col_index, col in enumerate(self.columns):
            Label(self.headerFrame, text=col, relief=RIDGE, width=20).grid(row=0, column=col_index)
            
        # Populate the grid with data
        for row_index, row_data in enumerate(self.sqlResultQuery):
            for col_index, cell_value in enumerate(row_data):
                # Create the data labels
                self.DataLabel = Label(self.resultFrame, text=cell_value, relief=RIDGE, width=20).grid(row=row_index+1, column=col_index)

        # Add the exit button
        self.btnBack = Button(self, text="Back", width=10, command=self.Exit)                
        self.btnBack.place(x=405, y=240)
                    
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()
                                
        # Open the Main Menu
        self.Identify_Class_Return()

    def on_horizontal_scroll(self, *args):
        """Synchronize horizontal scrolling between header and data canvases."""
        # Update the xview (horizontal view) of the result canvas based on the scrollbar's action
        self.resultCanvas.xview(*args)
        
        # Get the current horizontal scroll position of the result canvas
        scroll_pos = self.resultCanvas.xview()
        
        # Apply the same horizontal scroll position to the header canvas
        self.headerCanvas.xview_moveto(scroll_pos[0])

    def on_vertical_scroll(self, event):
        """Scroll the canvas vertically using the mouse wheel."""
        self.resultCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
            
    def onFrameConfigure(self, event):
        """This function resets the scroll region to encompass the inner frame and hides/shows the scrollbar as needed."""
        self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all"))
        # Set the header canvas to the same horizontal position as the result canvas
        self.headerCanvas.xview_moveto(self.resultCanvas.xview()[0])
                
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        self.Identify_Class_Return()

    def Identify_Class_Return(self):
        """ 
        Function Name: Identify_Class_Return
        Function Purpose: This function is executed when the calls caller ID is identified and returns control
        back to the desired menu
        """      
        Start_Menu.Delete_Obj_Lists(Start_Menu)
        Ropes_Menu()   


#######################################################################################################
# View Custom Rope System Information Class
####################################################################################################### 

class View_Custom_Rope_System_Info(tk.Tk):
    """
    Class Name: View_Custom_Rope_System_Info
    Class Description:  This class views all of the Custom Rope System Information
    """
    def __init__(self):
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (905/2)     
        self.y = (self.heightSize/2) - (280/2)    

        # Create the Window attributes
        self.WindowTitle = self.title("Custom Rope System Information")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (905, 280, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Main Frame for Header and Data
        self.mainFrame = Frame(self)
        self.mainFrame.place(x=5, y=5, width=895, height=225)

        # Header Frame and Canvas
        self.headerCanvas = Canvas(self.mainFrame, height=25, highlightthickness=0, bg='gray')
        self.headerCanvas.pack(side=TOP, fill=X)
        self.headerFrame = Frame(self.headerCanvas)
        self.headerCanvas.create_window((0, 0), window=self.headerFrame, anchor='nw')

        # Scrollable Frame for Data
        self.scrollFrame = Frame(self.mainFrame)
        self.scrollFrame.place(x=0, y=25, width=895, height=200)

        # Canvas for Scrollable Content
        self.resultCanvas = Canvas(self.scrollFrame, highlightthickness=0)
        self.resultCanvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Vertical Scrollbar
        self.resultScrollBarV = Scrollbar(self.scrollFrame, orient=VERTICAL, command=self.resultCanvas.yview)

        # Horizontal Scrollbar at the bottom of the main frame, not the scroll frame
        self.resultScrollBarH = Scrollbar(self.mainFrame, orient=HORIZONTAL, command=self.resultCanvas.xview)
        self.resultScrollBarH.place(x=0, y=205, width=895, height=20)

        # Configure Canvas Scrollbars
        self.resultCanvas.configure(yscrollcommand=self.resultScrollBarV.set, xscrollcommand=self.resultScrollBarH.set)
        self.headerCanvas.configure(xscrollcommand=self.resultScrollBarH.set)

        # Frame for Data inside Canvas
        self.resultFrame = Frame(self.resultCanvas)
        self.resultCanvas.create_window((0, 0), window=self.resultFrame, anchor='nw')

        # Configure Scroll Region
        self.resultFrame.bind("<Configure>", self.onFrameConfigure)
        self.headerCanvas.bind("<Configure>", lambda e: self.headerCanvas.configure(scrollregion=self.headerCanvas.bbox("all")))

        # Bind mousewheel scrolling
        self.resultCanvas.bind_all("<MouseWheel>", self.on_vertical_scroll)

        # Get the data from the database for the view 
        sqlView = "TCustomRopeSystems"
            
        # Call the query function
        self.sqlResultQuery = Queries.Get_All_DB_Values(self, sqlView)
        
        # Modify each sublist to remove the first element
        self.queryResult = [sublist[1:-1] for sublist in self.sqlResultQuery]

        # Debugging: Print the modified result to check the structure
        # print("Modified Query Result:", self.queryResult)
                
        # Create the column headers in the headerFrame
        self.columns = ["System Name", "Complexity", "Pre-Tied Knots", "Connector Count", "First Connector Type", 
                        "Second Connector Type", "Belay Device Type"]
        for col_index, col in enumerate(self.columns):
            Label(self.headerFrame, text=col, relief=RIDGE, width=20).grid(row=0, column=col_index)
            
        # Populate the grid with data
        for row_index, row_data in enumerate(self.queryResult):
            for col_index, cell_value in enumerate(row_data):
                # Create the data labels
                self.DataLabel = Label(self.resultFrame, text=cell_value, relief=RIDGE, width=20).grid(row=row_index+1, column=col_index)

        # Add the exit button
        self.btnBack = Button(self, text="Back", width=10, command=self.Exit)                
        self.btnBack.place(x=405, y=240)
                    
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()
                                
        # Open the Main Menu
        self.Identify_Class_Return()
        
    def on_horizontal_scroll(self, *args):
        """Synchronize horizontal scrolling between header and data canvases."""
        # Update the xview (horizontal view) of the result canvas based on the scrollbar's action
        self.resultCanvas.xview(*args)
        
        # Get the current horizontal scroll position of the result canvas
        scroll_pos = self.resultCanvas.xview()
        
        # Apply the same horizontal scroll position to the header canvas
        self.headerCanvas.xview_moveto(scroll_pos[0])

    def on_vertical_scroll(self, event):
        """Scroll the canvas vertically using the mouse wheel."""
        self.resultCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
            
    def onFrameConfigure(self, event):
        """This function resets the scroll region to encompass the inner frame and hides/shows the scrollbar as needed."""
        self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all"))
        # Set the header canvas to the same horizontal position as the result canvas
        self.headerCanvas.xview_moveto(self.resultCanvas.xview()[0])
                
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        self.Identify_Class_Return()

    def Identify_Class_Return(self):
        """ 
        Function Name: Identify_Class_Return
        Function Purpose: This function is executed when the calls caller ID is identified and returns control
        back to the desired menu
        """      
        Start_Menu.Delete_Obj_Lists(Start_Menu)
        Ropes_Menu()
        

#######################################################################################################
# View Device Information Class
####################################################################################################### 

class View_Device_Info(tk.Tk):
    """
    Class Name: View_Device_Info
    Class Description:  This class views all of the Device Information
    """
    def __init__(self, Class_CallerID=""):
        self.Class_CallerID = Class_CallerID
        
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (905/2)     
        self.y = (self.heightSize/2) - (280/2)    

        # Create the title for the window
        astrTitleList = ("Connector Information", "Belay Device Information")
        
        # Determine the caller ID to execute the title
        if self.Class_CallerID == "Connector":
            strTitle = astrTitleList[0]
        elif self.Class_CallerID == "BelayDevice":
            strTitle = astrTitleList[1]
            
        # Create the Window attributes
        self.WindowTitle = self.title(strTitle)
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (905, 280, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Main Frame for Header and Data
        self.mainFrame = Frame(self)
        self.mainFrame.place(x=5, y=5, width=895, height=225)

        # Header Frame and Canvas
        self.headerCanvas = Canvas(self.mainFrame, height=25, highlightthickness=0, bg='gray')
        self.headerCanvas.pack(side=TOP, fill=X)
        self.headerFrame = Frame(self.headerCanvas)
        self.headerCanvas.create_window((0, 0), window=self.headerFrame, anchor='nw')

        # Scrollable Frame for Data
        self.scrollFrame = Frame(self.mainFrame)
        self.scrollFrame.place(x=0, y=25, width=895, height=200)

        # Canvas for Scrollable Content
        self.resultCanvas = Canvas(self.scrollFrame, highlightthickness=0)
        self.resultCanvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Vertical Scrollbar
        self.resultScrollBarV = Scrollbar(self.scrollFrame, orient=VERTICAL, command=self.resultCanvas.yview)

        # Horizontal Scrollbar at the bottom of the main frame, not the scroll frame
        self.resultScrollBarH = Scrollbar(self.mainFrame, orient=HORIZONTAL, command=self.resultCanvas.xview)
        self.resultScrollBarH.place(x=0, y=205, width=895, height=20)

        # Configure Canvas Scrollbars
        self.resultCanvas.configure(yscrollcommand=self.resultScrollBarV.set, xscrollcommand=self.resultScrollBarH.set)
        self.headerCanvas.configure(xscrollcommand=self.resultScrollBarH.set)

        # Frame for Data inside Canvas
        self.resultFrame = Frame(self.resultCanvas)
        self.resultCanvas.create_window((0, 0), window=self.resultFrame, anchor='nw')

        # Configure Scroll Region
        self.resultFrame.bind("<Configure>", self.onFrameConfigure)
        self.headerCanvas.bind("<Configure>", lambda e: self.headerCanvas.configure(scrollregion=self.headerCanvas.bbox("all")))

        # Bind mousewheel scrolling
        self.resultCanvas.bind_all("<MouseWheel>", self.on_vertical_scroll)

        # Create the column headers in the headerFrame
        self.columns = ["Serial Number", "Bumper Number", "Manufacture Name", "Manufacture Date", "Install Date", 
                        "Last Inspection", "Next Inspection", "Device Type", "In Use Status"]
        
        # Get the data from the database for the view 
        sqlViewList = ("vConnectors", "vBelayDevices")
        
        # Determine the caller ID to execute the view
        if self.Class_CallerID == "Connector":
            sqlView = sqlViewList[0]
        elif self.Class_CallerID == "BelayDevice":
            sqlView = sqlViewList[1]
            self.columns.insert(0, "Device Name")
            
        # Call the query function
        self.sqlResultQuery = Queries.Get_All_DB_Values(self, sqlView)

        for col_index, col in enumerate(self.columns):
            Label(self.headerFrame, text=col, relief=RIDGE, width=20).grid(row=0, column=col_index)
            
        # Populate the grid with data
        for row_index, row_data in enumerate(self.sqlResultQuery):
            for col_index, cell_value in enumerate(row_data):
                # Create the data labels
                self.DataLabel = Label(self.resultFrame, text=cell_value, relief=RIDGE, width=20).grid(row=row_index+1, column=col_index)

        # Add the exit button
        self.btnBack = Button(self, text="Back", width=10, command=self.Exit)                
        self.btnBack.place(x=405, y=240)
                    
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()
                                
        # Open the Main Menu
        self.Identify_Class_Return()

    def on_horizontal_scroll(self, *args):
        """Synchronize horizontal scrolling between header and data canvases."""
        # Update the xview (horizontal view) of the result canvas based on the scrollbar's action
        self.resultCanvas.xview(*args)
        
        # Get the current horizontal scroll position of the result canvas
        scroll_pos = self.resultCanvas.xview()
        
        # Apply the same horizontal scroll position to the header canvas
        self.headerCanvas.xview_moveto(scroll_pos[0])

    def on_vertical_scroll(self, event):
        """Scroll the canvas vertically using the mouse wheel."""
        self.resultCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
            
    def onFrameConfigure(self, event):
        """This function resets the scroll region to encompass the inner frame and hides/shows the scrollbar as needed."""
        self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all"))
        # Set the header canvas to the same horizontal position as the result canvas
        self.headerCanvas.xview_moveto(self.resultCanvas.xview()[0])
                
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        self.Identify_Class_Return()

    def Identify_Class_Return(self):
        """ 
        Function Name: Identify_Class_Return
        Function Purpose: This function is executed when the calls caller ID is identified and returns control
        back to the desired menu
        """      
        Start_Menu.Delete_Obj_Lists(Start_Menu)
        
        # Determine which class menu control needs to return to 
        if self.Class_CallerID == "Connector":
            Connectors_Menu()
        elif self.Class_CallerID == "BelayDevice":
            BelayDevices_Menu()      
        
                
#######################################################################################################
# View AutoBelay Information Class
####################################################################################################### 

class View_AutoBelay_Info(tk.Tk):
    """
    Class Name: View_AutoBelay_Info
    Class Description:  This class views all of the AutoBelay Information
    """
    def __init__(self):
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (905/2)     
        self.y = (self.heightSize/2) - (340/2)    

        # Create the Window attributes
        self.WindowTitle = self.title("Auto Belay Information")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (905, 340, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Main Frame for Header and Data
        self.mainFrame = Frame(self)
        self.mainFrame.place(x=5, y=5, width=895, height=265)

        # Header Frame and Canvas
        self.headerCanvas = Canvas(self.mainFrame, height=25, highlightthickness=0, bg='gray')
        self.headerCanvas.pack(side=TOP, fill=X)
        self.headerFrame = Frame(self.headerCanvas)
        self.headerCanvas.create_window((0, 0), window=self.headerFrame, anchor='nw')

        # Scrollable Frame for Data
        self.scrollFrame = Frame(self.mainFrame)
        self.scrollFrame.place(x=0, y=25, width=895, height=240)

        # Canvas for Scrollable Content
        self.resultCanvas = Canvas(self.scrollFrame, highlightthickness=0)
        self.resultCanvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Vertical Scrollbar
        self.resultScrollBarV = Scrollbar(self.scrollFrame, orient=VERTICAL, command=self.resultCanvas.yview)

        # Horizontal Scrollbar at the bottom of the main frame, not the scroll frame
        self.resultScrollBarH = Scrollbar(self, orient=HORIZONTAL, command=self.resultCanvas.xview)
        self.resultScrollBarH.place(x=0, y=270, width=895, height=20)

        # Configure Canvas Scrollbars
        self.resultCanvas.configure(yscrollcommand=self.resultScrollBarV.set, xscrollcommand=self.resultScrollBarH.set)
        self.headerCanvas.configure(xscrollcommand=self.resultScrollBarH.set)

        # Frame for Data inside Canvas
        self.resultFrame = Frame(self.resultCanvas)
        self.resultCanvas.create_window((0, 0), window=self.resultFrame, anchor='nw')

        # Configure Scroll Region
        self.resultFrame.bind("<Configure>", self.onFrameConfigure)
        self.headerCanvas.bind("<Configure>", lambda e: self.headerCanvas.configure(scrollregion=self.headerCanvas.bbox("all")))

        # Bind mousewheel scrolling
        self.resultCanvas.bind_all("<MouseWheel>", self.on_vertical_scroll)

        # Get the data from the database for the view 
        sqlView = "vAutoBelays"
            
        # Call the query function
        self.sqlResultQuery = Queries.Get_All_DB_Values(self, sqlView)
        
        # Create the column headers in the headerFrame
        self.columns = ["Manufacture Name", "Serial Number", "Bumper Number", "Manufacture Date", "Service Date", "Re-Service Date", 
                        "Install Date", "Last Inspection", "Next Inspection", "In Use Status"]
        for col_index, col in enumerate(self.columns):
            Label(self.headerFrame, text=col, relief=RIDGE, width=20).grid(row=0, column=col_index)
            
        # Populate the grid with data
        for row_index, row_data in enumerate(self.sqlResultQuery):
            for col_index, cell_value in enumerate(row_data):
                # Create the data labels
                self.DataLabel = Label(self.resultFrame, text=cell_value, relief=RIDGE, width=20).grid(row=row_index+1, column=col_index)

        # Add the exit button
        self.btnBack = Button(self, text="Back", width=10, command=self.Exit)                
        self.btnBack.place(x=405, y=295)
                    
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()
                                
        # Open the Main Menu
        self.Identify_Class_Return()

    def on_horizontal_scroll(self, *args):
        """Synchronize horizontal scrolling between header and data canvases."""
        # Update the xview (horizontal view) of the result canvas based on the scrollbar's action
        self.resultCanvas.xview(*args)
        
        # Get the current horizontal scroll position of the result canvas
        scroll_pos = self.resultCanvas.xview()
        
        # Apply the same horizontal scroll position to the header canvas
        self.headerCanvas.xview_moveto(scroll_pos[0])

    def on_vertical_scroll(self, event):
        """Scroll the canvas vertically using the mouse wheel."""
        self.resultCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
            
    def onFrameConfigure(self, event):
        """This function resets the scroll region to encompass the inner frame and hides/shows the scrollbar as needed."""
        self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all"))
        # Set the header canvas to the same horizontal position as the result canvas
        self.headerCanvas.xview_moveto(self.resultCanvas.xview()[0])
                
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        self.Identify_Class_Return()

    def Identify_Class_Return(self):
        """ 
        Function Name: Identify_Class_Return
        Function Purpose: This function is executed when the calls caller ID is identified and returns control
        back to the desired menu
        """      
        Start_Menu.Delete_Obj_Lists(Start_Menu)
        AutoBelay_Menu()   
                    
#######################################################################################################
# View Out for Reservice Class
#######################################################################################################

class View_OutForReservice(tk.Tk):
    """
    Class Name: View_OutForReservice
    Class Description: This class views all of the Out for Reservice devices.
    """
    def __init__(self):
        # Initialize the Toplevel window 
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (765/2)     
        self.y = (self.heightSize/2) - (280/2) 
                
        # Create the Window attributes
        self.WindowTitle = self.title("Units Out For Reservice")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (765, 280, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Create the main frame for headers and data
        self.mainFrame = Frame(self)
        self.mainFrame.place(x=5, y=5, width=755, height=225)

        # Header Frame
        self.headerFrame = Frame(self.mainFrame)
        self.headerFrame.pack(side=TOP, fill=X, padx=2)

        # Scrollable Frame for Data
        self.scrollFrame = Frame(self.mainFrame)
        self.scrollFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

        # Canvas and Scrollbar for the scrollable Frame
        self.resultCanvas = Canvas(self.scrollFrame)
        self.resultCanvas.pack(side=LEFT, fill=BOTH, expand=True, padx=0)
        self.resultScrollBar = Scrollbar(self.scrollFrame, orient=VERTICAL, command=self.resultCanvas.yview)
        self.resultScrollBar.pack(side=RIGHT, fill=Y)
        self.resultCanvas.configure(yscrollcommand=self.resultScrollBar.set)

        # Frame for Data inside Canvas
        self.resultFrame = Frame(self.resultCanvas)
        self.resultCanvas.create_window((0,0), window=self.resultFrame, anchor='nw')

        # Configure the scroll region dynamically
        self.resultFrame.bind('<Configure>', self.onFrameConfigure)
                
        # Bind mousewheel scrolling
        self.resultCanvas.bind_all("<MouseWheel>", self.on_vertical_scroll)

        # Create the columns 
        self.columns = ["Serial Number", "Bumper Number", "Last Inspection Date", "Service Date", "Re-service Date"]
        
        # Get the data from the database for the view 
        sqlView = "vAutoBelayReserviceReports"
        
        # Call the query function
        self.sqlResultQuery = Queries.Get_All_DB_Values(self, sqlView)
        
        # Create the header for the rows for the grid
        for col_index, col in enumerate(self.columns):
            Label(self.resultFrame, text=col, relief=RIDGE, width=20).grid(row=0, column=col_index)
            
        # Populate the grid with data
        for row_index, row_data in enumerate(self.sqlResultQuery[:]):
            for col_index, cell_value in enumerate(row_data):
                # Create the data labels
                self.DataLabel = Label(self.resultFrame, text=cell_value, relief=RIDGE, width=20).grid(row=row_index+1, column=col_index)

        # Add the exit button
        self.btnBack = Button(self, text="Back", width=10, command=self.Exit)                
        self.btnBack.place(x=325, y=240)
                                
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)
        AutoBelay_Menu() 

    def onFrameConfigure(self, event):
        """ 
        Function Name: onFrameConfigure
        Function Purpose: This function resets the scroll region to encompass the inner frame
        """           
        self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all"))

    def on_vertical_scroll(self, event):
        """Scroll the canvas vertically using the mouse wheel."""
        self.resultCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
                
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        Start_Menu.Delete_Obj_Lists(Start_Menu)
        AutoBelay_Menu()            
                

#######################################################################################################
# Add Inspector Class
####################################################################################################### 
class AddInspector(tk.Tk, Inspector, UserLogins, LoginName):
    """
    Class Name: AddInspector
    Class Description: This class adds a Inspector to the database.
    """
    def __init__(self):
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()  

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (580/2)     
        self.y = (self.heightSize/2) - (310/2)    
                        
        # Create the Window attributes
        self.WindowTitle = self.title("Add New Inspector")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (580, 310, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Create the second frame to hold the input fields
        self.frameInput = LabelFrame(self, text="User Credentials")
        self.frameInput.place(x=85, y=40, width=405, height=220)

        # Create the labels 
        self.lblFName = Label(self.frameInput, text="First Name:")
        self.lblLName = Label(self.frameInput, text="Last Name:")
        self.lblEmail = Label(self.frameInput, text="Email:")
        self.lblPassword = Label(self.frameInput, text="Password:")
        self.lblPasswordReEnter = Label(self.frameInput, text="Re-enter Password:")

        # Create the label locations
        self.lblFName.grid(row=0, column=0, sticky='W', padx=35)
        self.lblLName.grid(row=1, column=0, sticky='W', padx=35)
        self.lblEmail.grid(row=2, column=0, sticky='W', padx=35)
        self.lblPassword.grid(row=3, column=0, sticky='W', padx=35)
        self.lblPasswordReEnter.grid(row=4, column=0, sticky='W', padx=35)        

        # Create the entry input box
        self.FNameInput = Entry(self.frameInput, width=30)
        self.LNameInput = Entry(self.frameInput, width=30)
        self.EmailInput = Entry(self.frameInput, width=30)
        self.PasswordInput = Entry(self.frameInput, width=30, show='*')
        self.PasswordReEnterInput = Entry(self.frameInput, width=30, show='*')

        # Create the grid for all of the entry input fields
        self.FNameInput.grid(row=0, column=1, padx=0, pady=5)
        self.LNameInput.grid(row=1, column=1, pady=5)
        self.EmailInput.grid(row=2, column=1, pady=5)
        self.PasswordInput.grid(row=3, column=1, pady=5)
        self.PasswordReEnterInput.grid(row=4, column=1, pady=5)

        # Create the buttons
        self.btnSubmit = Button(self.frameInput, text="Submit", width=10, command=lambda:AddInspector.Submit(self))
        self.btnExit = Button(self.frameInput, text="Back", width=10, command=lambda:AddInspector.Exit(self))
        self.btnReset = Button(self.frameInput, text="Reset", width=10, command=lambda:AddInspector.Reset(self))

        # Create the button grid
        self.btnExit.place(x=40, y=160) 
        self.btnSubmit.place(x=280, y=160) 
        self.btnReset.place(x=160, y=160)
                
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()            

        # Call the start menu sub
        Start_Menu.Delete_Obj_Lists(self)
        Start_Menu()        
        
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate
            
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        # Check the user input
        blnValidate = AddInspector.Check_Input(self.FNameInput.get())
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check the user input
            blnValidate = BaseFunctions.Validate_String_Input(self.FNameInput.get())     
                
            # Check if the input is valid
            if (blnValidate is True):
                # Check the user input
                blnValidate = AddInspector.Check_Input(self.LNameInput.get())

                # Check if the input is valid
                if (blnValidate is True):
                    # Check the user input
                    blnValidate = BaseFunctions.Validate_String_Input(self.LNameInput.get())     
                                        
                    # Check if the input is valid
                    if (blnValidate is True):
                        # Check the user input
                        blnValidate = AddInspector.Check_Input(self.EmailInput.get())

                        # Check if the input is valid
                        if (blnValidate is True):
                            # Check the user input
                            blnValidate = BaseFunctions.Validate_Email_Input(self.EmailInput.get())     
                                                
                            # Check if the input is valid
                            if (blnValidate is True):
                                # Check the user input
                                blnValidate = AddInspector.Check_Input(self.PasswordInput.get())
                                
                                # Check if the input is valid
                                if (blnValidate is True):
                                    # Check the user input
                                    blnValidate = AddInspector.Check_Input(self.PasswordReEnterInput.get())

                                    # Check if the input is valid
                                    if (blnValidate is True):
                                        # Check if the first password input is the same as the second password input
                                        if (self.PasswordInput.get() == self.PasswordReEnterInput.get()):
                                            # Check if the password input is valid and if so add 
                                            ReturnTup = BaseFunctions.Validate_NewLogin_Password(self.PasswordReEnterInput.get())
                                            
                                            # Check if the return tuple contains a valid status of True and a filled hash password result
                                            if (ReturnTup[0] is True):
                                                # Set the class object password equal to the hashed password
                                                self.strLoginPassword = ReturnTup[1]
                                                
                                                # Load the login credentials into the class object for each user prior to check for duplicates
                                                LoginName.Get_Login_Data(LoginName)
                                                
                                                # Set the user name prior to checking to duplicate in the db
                                                FirstName = self.FNameInput.get()
                                                LastName = self.LNameInput.get()
                                                strLoginName = str(FirstName+ "." + LastName)
                                                
                                                # Check if there are any users with this same user name in the database
                                                if strLoginName not in LoginName.astrLoginName:
                                                    sqlLoginQuery = ("TLogins", "intLoginID", "strLoginName")
                                                    self.InspectorID = self.Get_Or_Create_ID(strLoginName, sqlLoginQuery)
                                                    blnValidate = True
                                                    LoginName.Delete_Login_Data(LoginName)
                                                    
                                                else:
                                                    messagebox.showwarning(message='ERROR \n\n User name already exists. Please try again.')
                                                    # Return blnValidate as False
                                                    blnValidate = False
                                                    LoginName.Delete_Login_Data(LoginName)
                                                    self.Reset()                                                       
                                            else:
                                                # Return blnValidate as False
                                                blnValidate = False  
                                                self.PasswordInput.delete(0, END)
                                                self.PasswordReEnterInput.delete(0, END)
                                                self.PasswordInput.configure(background='Yellow')
                                                self.PasswordReEnterInput.configure(background='Yellow')
                                                self.PasswordInput.focus()                                                                                                       
                                        else:
                                            # Return blnValidate as False
                                            messagebox.showwarning(title='ERROR', message='The passwords entered do not match. Please try again.')
                                            blnValidate = False  
                                            self.PasswordInput.delete(0, END)
                                            self.PasswordReEnterInput.delete(0, END)
                                            self.PasswordInput.configure(background='Yellow')
                                            self.PasswordReEnterInput.configure(background='Yellow')
                                            self.PasswordInput.focus()                                                                                       
                                    else:
                                        # Return blnValidate as False
                                        blnValidate = False
                                        self.PasswordReEnterInput.delete(0, END)
                                        self.PasswordReEnterInput.configure(background='Yellow')
                                        self.PasswordReEnterInput.focus()                                          
                                else:
                                    # Return blnValidate as False
                                    blnValidate = False
                                    self.PasswordInput.delete(0, END)
                                    self.PasswordInput.configure(background='Yellow')
                                    self.PasswordInput.focus()                                      
                            else:
                                # Return blnValidate as False
                                blnValidate = False  
                                self.EmailInput.delete(0, END)
                                self.EmailInput.configure(background='Yellow')
                                self.EmailInput.focus()                                            
                        else:
                            # Return blnValidate as False
                            blnValidate = False  
                            self.EmailInput.delete(0, END)
                            self.EmailInput.configure(background='Yellow')
                            self.EmailInput.focus()                                                     
                    else:
                        # Return blnValidate as False
                        blnValidate = False  
                        self.LNameInput.delete(0, END)
                        self.LNameInput.configure(background='Yellow')
                        self.LNameInput.focus()                                                 
                else:
                    # Return blnValidate as False
                    blnValidate = False                         
                    self.LNameInput.delete(0, END)
                    self.LNameInput.configure(background='Yellow')
                    self.LNameInput.focus()                      
            else:
                # Return blnValidate as False
                blnValidate = False         
                self.FNameInput.delete(0, END)
                self.FNameInput.configure(background='Yellow')
                self.FNameInput.focus()                                                                        
        else:
            # Return blnValidate as False
            blnValidate = False
            self.FNameInput.delete(0, END)
            self.FNameInput.configure(background='Yellow')
            self.FNameInput.focus()            
            
        return blnValidate

    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
                        
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, sqlStatement)    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
    
    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed when the user has entered all fields and the inputs are valid. The inputs 
        will then be passed into the Inspector, Logins classes filling each object.
        """       
        self.strFirstName = self.FNameInput.get()
        self.strLastName = self.LNameInput.get()
        self.strLoginName = str(self.strFirstName + "." + self.strLastName)
        self.strEmail = self.EmailInput.get()
        self.intInspectorID = self.InspectorID

        # Add the new inspector and the new login parameters
        Inspector.Add_NewInspector_Query(self)
        LoginName.Add_NewLoginName_Query(self)
        UserLogins.Add_NewUserLogin_Query(self)
        
    def Clear_BG_Color(self):
        """ 
        Function Name: Clear_BG_Color
        Function Purpose: This button executes when the user submits their entries and clears the background
        color before any validation checks.
        """
        # Delete the button after submission
        self.FNameInput.configure(background='White')
        self.LNameInput.configure(background='White')
        self.EmailInput.configure(background='White')
        self.PasswordInput.configure(background='White')
        self.PasswordReEnterInput.configure(background='White')
        
    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This button executes when the user wants to reset the values.
        """
        # Delete the button after submission
        self.FNameInput.delete(0, END)
        self.LNameInput.delete(0, END)
        self.EmailInput.delete(0, END)
        self.PasswordInput.delete(0, END)
        self.PasswordReEnterInput.delete(0, END)
        self.FNameInput.focus()
        
        # Clear out the background colors and set to default as 'white'
        AddInspector.Clear_BG_Color(self)

    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the new inspector to the db. Else, reset
        """
        # Check if all of the inputs are valid
        global blnValidate 
        blnValidate = bool(False)
        
        # Clear out the background colors and set to default as 'white'
        AddInspector.Clear_BG_Color(self)
        
        # Get the blnValidate status
        blnValidate = AddInspector.Validate_InputFields(self)
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to add new inspector?') is True:     
                # Load the user data and prep the data for db dump
                AddInspector.Pull_UserInput(self)             
                
                # Display to the user the new user name
                messagebox.showwarning(message='ATTENTION! \n\n Your new user name is: \n\n %s'%(self.strLoginName))                  
                
                # Request to add this user to have admin permission                
                if messagebox.askyesno(message='ATTENTION! \n\n Would you like to grant user %s with admin permission?'%(self.strLoginName)):
                    AdminUsers.Add_AdminUser_Query(self)
                    
                # Check if the user would like to add another Inspector
                if messagebox.askyesno(message='SUCCESSFUL UPLOAD! \n\n Would you like to add another Inspector?') is True:
                    # Clear the input fields and after data is submitted to the database
                    AddInspector.Reset(self)
                else:
                    AddInspector.Exit(self)
            else:
                pass

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        Start_Menu.Delete_Obj_Lists(Start_Menu)
        Start_Menu()


#######################################################################################################
# Edit User Class
####################################################################################################### 
class EditUser(tk.Tk, Inspector, AdminUsers):
    """
    Class Name: EditUser
    Class Description: This class edits an Inspector and updates the database.
    """
    def __init__(self):
        # Preload the data set 
        LoginName.Get_Login_Data(self)
        
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()  

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (580/2)     
        self.y = (self.heightSize/2) - (390/2)    
                        
        # Create the Window attributes
        self.WindowTitle = self.title("Edit User")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (580, 390, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Create the second frame to hold the input fields
        self.selectInput = LabelFrame(self, text="Select User Login Name")
        self.selectInput.place(x=90, y=35, width=405, height=90)

        # Create the labels 
        self.lblLoginName = Label(self.selectInput, text="Login Name:")

        # Create the label locations
        self.lblLoginName.grid(row=0, column=0, sticky='W', padx=37)

        # Create the entry input box
        self.dropLoginName = ttk.Combobox(self.selectInput, values=self.astrLoginName[1:], state='readonly')
        self.dropLoginName.configure(width=30)

        # Create the grid for all of the entry input fields
        self.dropLoginName.grid(row=0, column=1)

        # Create the buttons
        self.btnSelectSubmit = Button(self.selectInput, text="Submit", width=10, command=lambda:EditUser.SubmitSelect(self))

        # Create the button grid
        self.btnSelectSubmit.place(x=160, y=35)

        # Create the second frame to hold the input fields
        self.frameInput = LabelFrame(self, text="User Credentials")
        self.frameInput.place(x=90, y=130, width=405, height=220)

        # Create the labels 
        self.lblFName = Label(self.frameInput, text="First Name:")
        self.lblLName = Label(self.frameInput, text="Last Name:")
        self.lblEmail = Label(self.frameInput, text="Email:")
        self.lblPassword = Label(self.frameInput, text="Password:")
        self.lblPasswordReEnter = Label(self.frameInput, text="Re-enter Password:")

        # Create the label locations
        self.lblFName.grid(row=0, column=0, sticky='W', padx=25)
        self.lblLName.grid(row=1, column=0, sticky='W', padx=25)
        self.lblEmail.grid(row=2, column=0, sticky='W', padx=25)
        self.lblPassword.grid(row=3, column=0, sticky='W', padx=25)
        self.lblPasswordReEnter.grid(row=4, column=0, sticky='W', padx=25)        

        # Create the entry input box
        self.FNameInput = Entry(self.frameInput, width=35, state='disabled')
        self.LNameInput = Entry(self.frameInput, width=35, state='disabled')
        self.EmailInput = Entry(self.frameInput, width=35, state='disabled')
        self.PasswordInput = Entry(self.frameInput, width=35, state='disabled')
        self.PasswordReEnterInput = Entry(self.frameInput, width=35, state='disabled')
        
        # Create the grid for all of the entry input fields
        self.FNameInput.grid(row=0, column=1, pady=5)
        self.LNameInput.grid(row=1, column=1, pady=5)
        self.EmailInput.grid(row=2, column=1, pady=5)

        # Create the buttons
        self.btnSubmit = Button(self.frameInput, text="Submit", width=10, command=lambda:EditUser.Submit(self), state='disabled')
        self.btnExit = Button(self.frameInput, text="Back", width=10, command=lambda:EditUser.Exit(self))
        self.btnReset = Button(self.frameInput, text="Reset", width=10, command=lambda:EditUser.Reset(self), state='disabled')

        # Create the button grid
        self.btnExit.place(x=40, y=160) 
        self.btnSubmit.place(x=280, y=160) 
        self.btnReset.place(x=160, y=160)
                        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()            

        # Call the start menu sub
        Start_Menu.Delete_Obj_Lists(self)
        Start_Menu()        
            
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate
            
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        # Check the user input
        blnValidate = EditUser.Check_Input(self.FNameInput.get())
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check the user input
            blnValidate = BaseFunctions.Validate_String_Input(self.FNameInput.get())     
                
            # Check if the input is valid
            if (blnValidate is True):
                # Check the user input
                blnValidate = EditUser.Check_Input(self.LNameInput.get())

                # Check if the input is valid
                if (blnValidate is True):
                    # Check the user input
                    blnValidate = BaseFunctions.Validate_String_Input(self.LNameInput.get())     
                                        
                    # Check if the input is valid
                    if (blnValidate is True):
                        # Check the user input
                        blnValidate = EditUser.Check_Input(self.EmailInput.get())

                        # Check if the input is valid
                        if (blnValidate is True):
                            # Check the user input
                            blnValidate = BaseFunctions.Validate_Email_Input(self.EmailInput.get())     
                                                
                            # Check if the input is valid
                            if (blnValidate is True):
                                # Check the user input
                                blnValidate = EditUser.Check_Input(self.PasswordInput.get())
                                
                                # Check if the input is valid
                                if (blnValidate is True):
                                    # Check the user input
                                    blnValidate = EditUser.Check_Input(self.PasswordReEnterInput.get())

                                    # Check if the input is valid
                                    if (blnValidate is True):
                                        # Check if the first password input is the same as the second password input
                                        if (self.PasswordInput.get() == self.PasswordReEnterInput.get()):
                                            # Check if the password input is valid and if so add 
                                            ReturnTup = BaseFunctions.Validate_NewLogin_Password(self.PasswordReEnterInput.get())
                                            
                                            # Check if the return tuple contains a valid status of True and a filled hash password result
                                            if (ReturnTup[0] is True):
                                                # Set the class object password equal to the hashed password
                                                self.strLoginPassword = ReturnTup[1]
                                                
                                                # Load the login credentials into the class object for each user prior to check for duplicates
                                                LoginName.Get_Login_Data(LoginName)
                                                
                                                # Set the user name prior to checking to duplicate in the db
                                                FirstName = self.FNameInput.get()
                                                LastName = self.LNameInput.get()
                                                strLoginName = str(FirstName+ "." + LastName)
                                                
                                                # Check if there are any users with this same user name in the database
                                                if strLoginName in LoginName.astrLoginName:
                                                    sqlLoginQuery = ("TLogins", "intLoginID", "strLoginName")
                                                    self.InspectorID = self.Get_Or_Create_ID(strLoginName, sqlLoginQuery)
                                                    blnValidate = True
                                                    LoginName.Delete_Login_Data(LoginName)                                                    
                                                else:
                                                    messagebox.showwarning(message='ERROR \n\n User name already exists. Please try again.')
                                                    # Return blnValidate as False
                                                    blnValidate = False
                                                    LoginName.Delete_Login_Data(LoginName)
                                                    self.Reset() 
                                            else:
                                                # Return blnValidate as False
                                                blnValidate = False  
                                                self.PasswordInput.delete(0, END)
                                                self.PasswordReEnterInput.delete(0, END)
                                                self.PasswordInput.configure(background='Yellow')
                                                self.PasswordReEnterInput.configure(background='Yellow')
                                                self.PasswordInput.focus()                                                                                                       
                                        else:
                                            # Return blnValidate as False
                                            messagebox.showwarning(title='ERROR', message='The passwords entered do not match. Please try again.')
                                            blnValidate = False  
                                            self.PasswordInput.delete(0, END)
                                            self.PasswordReEnterInput.delete(0, END)
                                            self.PasswordInput.configure(background='Yellow')
                                            self.PasswordReEnterInput.configure(background='Yellow')
                                            self.PasswordInput.focus()                                                                                       
                                    else:
                                        # Return blnValidate as False
                                        blnValidate = False
                                        self.PasswordReEnterInput.delete(0, END)
                                        self.PasswordReEnterInput.configure(background='Yellow')
                                        self.PasswordReEnterInput.focus()                                          
                                else:
                                    # Return blnValidate as False
                                    blnValidate = False
                                    self.PasswordInput.delete(0, END)
                                    self.PasswordInput.configure(background='Yellow')
                                    self.PasswordInput.focus()                                      
                            else:
                                # Return blnValidate as False
                                blnValidate = False  
                                self.EmailInput.delete(0, END)
                                self.EmailInput.configure(background='Yellow')
                                self.EmailInput.focus()                                            
                        else:
                            # Return blnValidate as False
                            blnValidate = False  
                            self.EmailInput.delete(0, END)
                            self.EmailInput.configure(background='Yellow')
                            self.EmailInput.focus()                                                     
                    else:
                        # Return blnValidate as False
                        blnValidate = False  
                        self.LNameInput.delete(0, END)
                        self.LNameInput.configure(background='Yellow')
                        self.LNameInput.focus()                                                 
                else:
                    # Return blnValidate as False
                    blnValidate = False                         
                    self.LNameInput.delete(0, END)
                    self.LNameInput.configure(background='Yellow')
                    self.LNameInput.focus()                      
            else:
                # Return blnValidate as False
                blnValidate = False         
                self.FNameInput.delete(0, END)
                self.FNameInput.configure(background='Yellow')
                self.FNameInput.focus()                                                                        
        else:
            # Return blnValidate as False
            blnValidate = False
            self.FNameInput.delete(0, END)
            self.FNameInput.configure(background='Yellow')
            self.FNameInput.focus()            
            
        return blnValidate

    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
                        
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, sqlStatement)    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
    
    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed when the user has entered all fields and the inputs are valid. The inputs 
        will then be passed into the Inspector, Logins classes filling each object.
        """       
        self.strFirstName = self.FNameInput.get()
        self.strLastName = self.LNameInput.get()
        self.strEmail = self.EmailInput.get()
        self.strLoginName = str(self.strFirstName + "." + self.strLastName)
        self.intInspectorID = self.InspectorID

        # Add the new inspector and the new login parameters
        Inspector.Update_InspectorCred_Query(self)
        LoginName.Update_LoginCred_Query(self)

    def Clear_BG_Color(self):
        """ 
        Function Name: Clear_BG_Color
        Function Purpose: This button executes when the user submits their entries and clears the background
        color before any validation checks.
        """
        # Delete the button after submission
        self.FNameInput.configure(background='White')
        self.LNameInput.configure(background='White')
        self.EmailInput.configure(background='White')
        self.PasswordInput.configure(background='White')
        self.PasswordReEnterInput.configure(background='White')
        
    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This button executes when the user wants to reset the values.
        """
        # Delete the button after submission
        self.dropLoginName.set("")
        self.FNameInput.delete(0, END)
        self.LNameInput.delete(0, END)
        self.EmailInput.delete(0, END)
        self.PasswordInput.delete(0, END)
        self.PasswordReEnterInput.delete(0, END)
        self.dropLoginName.focus()
        
        # Re-configure password input to be disabled
        self.FNameInput.configure(state='disabled')
        self.LNameInput.configure(state='disabled')
        self.EmailInput.configure(state='disabled')
        self.PasswordInput.configure(state='disabled')
        self.PasswordReEnterInput.configure(state='disabled')       

        # Disable/enable the select, submit, and reset submit button
        self.btnSelectSubmit.configure(state='normal')
        self.btnReset.configure(state='disabled')
        self.btnSubmit.configure(state='disabled') 
                        
        # Clear out the background colors and set to default as 'white'
        EditUser.Clear_BG_Color(self)

    def SubmitSelect(self):
        """ 
        Function Name: SubmitSelect
        Function Purpose: This button executes when the user selects the user login names.
        """
        # Input the data inside the entry input box
        self.FNameInput.configure(state='normal')
        self.LNameInput.configure(state='normal')
        self.EmailInput.configure(state='normal')
        self.PasswordInput.configure(state='normal')
        self.PasswordReEnterInput.configure(state='normal')

        # Break apart the user login name to the first and last name
        self.LoginName = self.dropLoginName.get()
        self.FNameInput.insert(0, self.LoginName.split('.')[0])
        self.LNameInput.insert(0, self.LoginName.split('.')[1])
        
        # Create the sql query string
        sqlQuery = """SELECT intInspectorID, strEmail FROM TInspectors WHERE strFirstName = '%s' AND strLastName = '%s'""" % (self.LoginName.split('.')[0], self.LoginName.split('.')[1])
        
        # Get the query results
        QueryResult = Database.dbExeQuery(Database, sqlQuery)
        self.InspectorID = QueryResult[0][0]
        self.EmailInput.insert(0, QueryResult[0][1])
            
        # Get the password input
        self.PasswordInput = Entry(self.frameInput, width=35, show='*')
        self.PasswordReEnterInput = Entry(self.frameInput, width=35, show='*')
        
        # Create the grid for the password input 
        self.PasswordInput.grid(row=3, column=1, pady=5)
        self.PasswordReEnterInput.grid(row=4, column=1, pady=5)        
        
        # Disable the select submit button
        self.btnSelectSubmit.configure(state='disabled')
        
        # Enable the submit, and reset button
        self.btnSubmit.configure(state='normal')
        self.btnReset.configure(state='normal')

    def Remove_AdminRequest(self):
        """ 
        Function Name: Remove_AdminRequest
        Function Purpose: This function only checks if the updated user has admin permissions and requests the user to either 
        remove the updated user or not. 
        """
        # Check if the user is in the admin group
        AdminUsers.Get_AdminUser_Data(self)
                
        if self.InspectorID in AdminUsers.aintAdminInspectorID: 
            # Check if the admin user would like to remove this new user to the database as admin
            if messagebox.askyesno(message='ATTENTION! \n\n Would you like to remove user %s of admin permissions?'%(self.LoginName)) is True:
                # Call the admin user class and upload the new user to the AdminUser table in the db
                sqlTableName = "TAdminUsers"
                intPrimID = "intAdminUserID"
                intInspectorID = "intInspectorID"
                params = (sqlTableName, intInspectorID, self.InspectorID)
                
                # Set the keyID to the admin ID
                intKeyID = Queries.Get_DB_Value(Queries, intPrimID, params)                    
                Queries.Remove_Attribute_Query(Queries, sqlTableName, intPrimID, intKeyID)
        else:
            # Request to add this user to have admin permission                
            if messagebox.askyesno(message='ATTENTION! \n\n Would you like to grant user %s with admin permission?'%(self.LoginName)):
                # Set the query attributes
                sqlTableName = "TLogins"
                intPrimID = "intLoginID"
                AdminUsers.intInspectorID = self.InspectorID
                params = (sqlTableName, intPrimID, AdminUsers.intInspectorID)
                
                # Set the keyID to the login ID
                LoginName.intLoginID = Queries.Get_DB_Value(Queries, intPrimID, params)
                AdminUsers.Add_AdminUser_Query(AdminUsers)

        # Delete the array lists
        Start_Menu.Delete_Obj_Lists(Start_Menu)
                                
    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the new inspector to the db. Else, reset
        """
        # Check if all of the inputs are valid
        global blnValidate 
        blnValidate = bool(False)
        
        # Clear out the background colors and set to default as 'white'
        EditUser.Clear_BG_Color(self)
        
        # Get the blnValidate status
        blnValidate = EditUser.Validate_InputFields(self)
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to update inspector credentials?') is True:     
                # Load the user data and prep the data for db dump
                EditUser.Pull_UserInput(self)             
                
                # Check if the user is in the admin group
                EditUser.Remove_AdminRequest(self)
                
                # Display to the user the new user name
                messagebox.showwarning(message='ATTENTION! \n\n Updated user %s'%(self.LoginName))                  
                
                # Check if the user would like to add another Inspector
                if messagebox.askyesno(message='SUCCESSFUL UPLOAD! \n\n Would you like to update another Inspector?') is True:
                    # Clear the input fields and after data is submitted to the database
                    EditUser.Reset(self)
                else:
                    EditUser.Exit(self)
            else:
                pass

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        Start_Menu.Delete_Obj_Lists(Start_Menu)
        Start_Menu()


#######################################################################################################
# Ropes Menu Class
#######################################################################################################        

class Ropes_Menu(tk.Tk):
    """
    Class Name: Ropes_Menu
    Class Description: This class is for the Ropes main menu. 
    """
    def __init__(self, ):
        # Load the data from the database
        Start_Menu.Load_Obj_Lists(self)
        
        # Create the root tkinter variable
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (560/2)     
        self.y = (self.heightSize/2) - (390/2)    
                        
        # Create the Window attributes
        self.WindowTitle = self.title("Rope Menu")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (560, 390, self.x, self.y))
        self.WindowSize = self.resizable(False, False)
        
        # Create the frame for the buttons
        self.btnFrame = LabelFrame(self, text='Menu Selection')
        self.btnFrame.place(x=160, y=15, width=250, height=345)

        # Create the Buttons
        self.btnRigSetup = Button(self.btnFrame, width=25, text = "Rope System Setup", command=lambda:Ropes_Menu.Open_RopeSystem_Setup(self))
        self.btnNewInspect = Button(self.btnFrame, width=25, text = "New Inspection", command=lambda:Ropes_Menu.Open_NewInspection(self))        
        self.btnViewFutureInspectDate = Button(self.btnFrame, width=25, text = "View Future Inspection Dates", command=lambda:Ropes_Menu.Open_ViewLastNext_InspectionDates(self))
        self.btnViewRopeDates = Button(self.btnFrame, width=25, text = "View Rope Dates", command=lambda:Ropes_Menu.Open_RopeDates(self))
        self.btnViewRopeInfo = Button(self.btnFrame, width=25, text = "View Rope Info", command=lambda:Ropes_Menu.Open_Rope_Info(self))
        self.btnViewRopeSystemInfo = Button(self.btnFrame, width=25, text = "View Rope System Info", command=lambda:Ropes_Menu.Open_RopeSys_Info(self))
        self.btnViewRopeWallLocation = Button(self.btnFrame, width=25, text = "View Rope Wall Locations", command=lambda:Ropes_Menu.Open_Rope_WallLocations(self))
        self.btnDownloadReport = Button(self.btnFrame, width=25, text = "Download Reports", command=lambda:Ropes_Menu.Open_DownloadReports(self))
        self.btnOpenReport = Button(self.btnFrame, width=25, text = "Open Reports", command=lambda:Ropes_Menu.Open_Records_Dir(self))
        self.btnExit = Button(self.btnFrame, width=25, text = "Home", command=lambda:Ropes_Menu.Exit(self))

        # Create the button grid
        self.btnRigSetup.grid(row=0, column=1, padx=29, pady=3)
        self.btnNewInspect.grid(row=1, column=1, padx=29, pady=3)
        self.btnViewFutureInspectDate.grid(row=2, column=1, pady=3)
        self.btnViewRopeDates.grid(row=3, column=1, pady=3)
        self.btnViewRopeInfo.grid(row=4, column=1, pady=3)
        self.btnViewRopeSystemInfo.grid(row=5, column=1, pady=3)
        self.btnViewRopeWallLocation.grid(row=6, column=1, pady=3)
        self.btnDownloadReport.grid(row=7, column=1, pady=3)
        self.btnOpenReport.grid(row=8, column=1, pady=3)
        self.btnExit.grid(row=9, column=1, pady=3)
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()  
        
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)   
        
        # Send the user back to the main menu        
        Start_Menu()

    def Open_RopeSystem_Setup(self):
        """ 
        Function Name: Open_RopeSystem_Setup
        Function Purpose: This function is executed if the user clicks Rope System Setup.
        """
        # Delete the root window
        self.destroy()
        
        # Open the New Inspection Window
        Build_Rope_Sys_Setup()

    def Open_NewInspection(self):
        """ 
        Function Name: Open_NewInspection
        Function Purpose: This function is executed if the user clicks new inspection button. The 
        call is to the inspection class and will execute and add a new inspection to the database.
        """
        # Delete the root window
        self.destroy()
        
        # Open the New Inspection Window
        GymRopeSelection()

    def Open_ViewLastNext_InspectionDates(self):
        """ 
        Function Name: Open_ViewLastNext_InspectionDates
        Function Purpose: This function is executed if the user clicks view Ropes Next/Last inspection dates button. 
        """
        # Delete the root window
        self.destroy()
        
        # Determine the Caller_ID based on the class
        Caller_ID = "Rope"
        
        # Open the add new location window
        View_LastNext_InspectDate(Class_CallerID=Caller_ID)
        
    def Open_RopeDates(self):
        """ 
        Function Name: Open_RopeDates
        Function Purpose: This function is executed if the user clicks View Ropes Dates button. 
        """
        # Delete the root window
        self.destroy()

        # Determine the Caller_ID based on the class
        Caller_ID = "Rope"
                
        # Open the add new location window
        View_ItemDates(Class_CallerID=Caller_ID)

    def Open_Rope_WallLocations(self):
        """ 
        Function Name: Open_Rope_WallLocations
        Function Purpose: This function is executed if the user clicks View Ropes Locations button. 
        """
        # Delete the root window
        self.destroy()

        # Determine the Caller_ID based on the class
        Caller_ID = "Rope"
                        
        # Open the view location window
        View_Item_WallLocations(Class_CallerID=Caller_ID)  

    def Open_Rope_Info(self):
        """ 
        Function Name: Open_Rope_Info
        Function Purpose: This function is executed if the user clicks View Ropes Info button. 
        """
        # Delete the root window
        self.destroy()
        
        # Open the view location window
        View_Rope_Info()
        
    def Open_RopeSys_Info(self):
        """ 
        Function Name: Open_RopeSys_Info
        Function Purpose: This function is executed if the user clicks View Rope System Info button. 
        """
        # Delete the root window
        self.destroy()
        
        # Open the view location window
        View_Custom_Rope_System_Info()
        
    def Open_Rope_OutOfService(self):
        """ 
        Function Name: Open_Rope_OutOfService
        Function Purpose: This function is executed if the user clicks View Ropes Out For Reservice button. 
        """
        # Delete the root window
        self.destroy()
        
        # Open the view location window

        
    def Open_Records_Dir(self):
        """ 
        Function Name: Open_Records_Dir
        Function Purpose: This function is executed if the user clicks Open Report Information button. 
        """
        # Open the send reports window
        Records.Open_Records_Dir()   
        
    def Open_DownloadReports(self):
        """ 
        Function Name: Open_DownloadReports
        Function Purpose: This function executes whenever the user clicks the 'Download Reports' button. This function
        pulls from the db specific views and downloads the views to a desired directory. Each file is saved as an excel
        file. 
        """
        Queries.Download_Files(Queries, user_triggered=True)       
        messagebox.showwarning(message='SUCCESSFUL DOWNLOAD \n\n All files have been downloaded to the Records Directory.', icon='warning')
        
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed if the user clicks exit button. The main menu will
        exit once this button is clicked and will return the user to the login page.
        """
        # Delete the root window
        self.destroy()
        
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)  
        
        # Send the user back to the main menu   
        Start_Menu()


#######################################################################################################
# Build Rope System Setup
#######################################################################################################

class Build_Rope_Sys_Setup(tk.Tk, CustomRopeSystem):
    """
    Class Name: Build_Rope_Sys_Setup
    Class Description: This class provides the user with a build for rope systems and to store the setup options in db.
    """
    def __init__(self):
        # Load the data from the database
        # Start_Menu.Load_Obj_Lists(self) # Make sure to comment this out after testing
                
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (560/2)     
        self.y = (self.heightSize/2) - (470/2)  
                                        
        # Create the Window attributes
        self.WindowTitle = self.title("Build Rope System")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (560, 470, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Load the query selection widget
        self.Selection_Widget()
                
        # Create the second frame to hold the input fields
        self.frameInput = LabelFrame(self, text="Additional Components")
        self.frameInput.place(x=75, y=230, width=405, height=180)

        # Create the labels 
        self.lblPreTiedKnots = tk.Label(self.frameInput, text="Pre-tied Knots:")
        self.lblConnectCount = tk.Label(self.frameInput, text="Connector Count:")
        self.lblFirstConnectType = tk.Label(self.frameInput, text="First Connector Type:")
        self.lblSecondConnectType = tk.Label(self.frameInput, text="Second Connector Type:")
        self.lblBelayDevice = tk.Label(self.frameInput, text="Belay Device:")

        # Create the label locations
        self.lblPreTiedKnots.grid(row=1, column=0, sticky='W', padx=10)
        self.lblConnectCount.grid(row=2, column=0, sticky='W', padx=10)
        self.lblFirstConnectType.grid(row=3, column=0, sticky='W', padx=10)
        self.lblSecondConnectType.grid(row=4, column=0, sticky='W', padx=10)
        self.lblBelayDevice.grid(row=5, column=0, sticky='W', padx=10)

        # Create the combo box lists
        self.aKnotList = ("None", "Yes")
        self.aConnectorCountList = ("0", "1", "2")
        self.aConnectorTypeList = Carabiner.astrCarabinerType
        self.aConnectorTypeList.insert(0, "None")
        self.aBelayDeviceTypeList = ("None", "Assisted-Braking", "Manual")
        
        # Create the combo box
        self.dropKnot = ttk.Combobox(self.frameInput, values=self.aKnotList, state='disabled')
        self.dropConCount = ttk.Combobox(self.frameInput, values=self.aConnectorCountList, state='disabled')
        self.dropFirstConType = ttk.Combobox(self.frameInput, values=self.aConnectorTypeList, state='disabled')
        self.dropSecondConType = ttk.Combobox(self.frameInput, values=self.aConnectorTypeList, state='disabled')
        self.dropDeviceType = ttk.Combobox(self.frameInput, values=self.aBelayDeviceTypeList, state='disabled')
        
        # Bind the second connector type drop menu to enable once the connector count equals 2
        self.dropConCount.bind("<<ComboboxSelected>>", self.On_Connector_Count_Change)
        self.On_Connector_Count_Change()  # Call the function to set the initial state
        
        # Configure the drop menu lists
        self.dropKnot.configure(width=30,)
        self.dropConCount.configure(width=30,)
        self.dropFirstConType.configure(width=30,)
        self.dropSecondConType.configure(width=30,)
        self.dropDeviceType.configure(width=30,)

        # Create the grid for all of the entry input fields
        self.dropKnot.grid(row=1, column=1, padx=25, pady=5)
        self.dropConCount.grid(row=2, column=1, pady=5)
        self.dropFirstConType.grid(row=3, column=1, pady=5)
        self.dropSecondConType.grid(row=4, column=1, pady=5)
        self.dropDeviceType.grid(row=5, column=1, pady=5)

        # Create the buttons
        self.btnExit = Button(self, text="Back", width=10, command=lambda:Build_Rope_Sys_Setup.Exit(self))
        self.btnReset = Button(self, text="Reset", width=10, command=lambda:Build_Rope_Sys_Setup.Reset(self))
        self.btnSubmit = Button(self, text="Submit", width=10, command=lambda:Build_Rope_Sys_Setup.Submit(self))

        # Create the button grid
        self.btnExit.place(x=105, y=425)
        self.btnReset.place(x=235, y=425)
        self.btnSubmit.place(x=365, y=425)

        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()  
        
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the object lists
        Start_Menu.Delete_Obj_Lists(self)   
        
        # Send the user back to the ropes main menu        
        Ropes_Menu()
        
    def Selection_Widget(self):
        """ 
        Function Name: Selection_Widget
        Function Purpose: This function populates the search by widget for Serial or Bumper Num search.
        """           
        # Create the first frame to hold the input fields
        self.selectInput = LabelFrame(self, text="Select Rope System Setup")
        self.selectInput.place(x=75, y=35, width=405, height=190)

        # Create the display message for the new inspection
        self.simpleDisplayMessage = str(
        """
        Simple System: This setup includes a standalone rope with no 
        additional components. It's straightforward, easier to manage, 
        and suitable for standard operations.""")
        
        self.complexDisplayMessage = str(
        """Complex System: Opt for this setup if you require a more 
        intricate arrangement. It involves multiple types of additional
        components, providing versatility and advanced functionality.""")  

        # Create the label for the display message
        self.simpleInstructMessage = Label(self.selectInput, text=self.simpleDisplayMessage)
        self.complexInstructMessage = Label(self.selectInput, text=self.complexDisplayMessage)
        self.simpleInstructMessage.grid(row=0, column=0, sticky="W", padx=5)
        self.complexInstructMessage.grid(row=1, column=0, sticky="W", padx=5)
        
        # Create the labels 
        self.lblRopeSys = Label(self.selectInput, text="Rope System:")

        # Create the label locations
        self.lblRopeSys.place(x=80, y=130)

        # Create variables to hold the value of the selected radio button
        self.objRadioValue = tk.StringVar(value='simple')

        # List objects of serial and bumper values
        self.astrComplexityList = ("Simple", "Complex")

        # Create the radio buttons
        self.rbSimple = tk.Radiobutton(self.selectInput, text="Simple", variable=self.objRadioValue, value="simple")
        self.rbComplex = tk.Radiobutton(self.selectInput, text="Complex", variable=self.objRadioValue, value="complex")
        
        # Place the radio buttons next to each other using .place()
        self.rbSimple.place(x=170, y=130)
        self.rbComplex.place(x=240, y=130)
        self.Setup_Radio_Command()

    def Setup_Radio_Command(self):
        """ 
        Function Name: Setup_Radio_Command
        Function Purpose: This function populates the dropdown based on the radio button selection.
        """          
        self.rbSimple.configure(command=self.Populate_Dropdown)
        self.rbComplex.configure(command=self.Populate_Dropdown)
        
    def Populate_Dropdown(self):
        """ 
        Function Name: Populate_Dropdown
        Function Purpose: This function populates the dropdown based on the radio button selection.
        """           
        if self.objRadioValue.get() == "simple":
            # Disable the dropdowns
            for entry in [self.dropKnot, self.dropConCount, self.dropFirstConType, self.dropSecondConType, self.dropDeviceType]:
                # Delete the entries
                entry.set("")
                entry.configure(state='disabled')
        else:
            # Enable the dropdowns
            for entry in [self.dropKnot, self.dropConCount, self.dropDeviceType]:
                entry.configure(state='readonly')

    def On_Connector_Count_Change(self, event=None):
        """ 
        Function Name: On_Connector_Count_Change
        Function Purpose: This function holds the even handler for when the connector count equals 2 and allows
        the second connector type to display as readonly. 
        """  
        connector_count = self.dropConCount.get()

        # Create a copy of the connector type list for modification
        astrModifiedConnectorList = self.aConnectorTypeList.copy()
                    
        if connector_count == "":
            self.dropFirstConType.set("")
            self.dropSecondConType.set("")
            self.dropFirstConType.configure(state='disabled')
            self.dropSecondConType.configure(state='disabled')
        elif connector_count == "1":
            self.dropSecondConType.set("")
            self.dropFirstConType.configure(state='readonly')
            astrModifiedConnectorList.pop(0)
            self.dropFirstConType['values'] = astrModifiedConnectorList
            self.dropSecondConType.configure(state='disabled')
        elif connector_count == "2":
            astrModifiedConnectorList.pop(0)
            self.dropFirstConType['values'] = astrModifiedConnectorList
            self.dropSecondConType['values'] = astrModifiedConnectorList
            self.dropFirstConType.configure(state='readonly')
            self.dropSecondConType.configure(state='readonly')
        elif connector_count == "0":
            self.dropFirstConType.set("")
            self.dropSecondConType.set("")
            self.dropFirstConType.configure(state='disabled')
            self.dropSecondConType.configure(state='disabled')

    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.', icon='warning')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate
    
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        # Check if the radio obj is simple or not. If simple, pass and if Complex, reset values
        if self.objRadioValue.get() == "simple":
            pass
        else:
            # Check the user input for dropKnot
            if not Build_Rope_Sys_Setup.Check_Input(self.dropKnot.get()):
                self.dropKnot.focus()
                return False

            # Check the user input for dropConCount
            if not Build_Rope_Sys_Setup.Check_Input(self.dropConCount.get()):
                self.dropConCount.focus()
                return False

            # Validate based on the dropConCount value
            if self.dropConCount.get() == "1":
                # Check the user input for dropFirstConType
                if not Build_Rope_Sys_Setup.Check_Input(self.dropFirstConType.get()):
                    self.dropFirstConType.focus()
                    return False

                # Check the user input for dropDeviceType
                if not Build_Rope_Sys_Setup.Check_Input(self.dropDeviceType.get()):
                    self.dropDeviceType.focus()
                    return False

            elif self.dropConCount.get() == "2":
                # Check the user input for dropFirstConType
                if not Build_Rope_Sys_Setup.Check_Input(self.dropFirstConType.get()):
                    self.dropFirstConType.focus()
                    return False

                # Check the user input for dropSecondConType
                if not Build_Rope_Sys_Setup.Check_Input(self.dropSecondConType.get()):
                    self.dropSecondConType.focus()
                    return False

                # Check the user input for dropDeviceType
                if not Build_Rope_Sys_Setup.Check_Input(self.dropDeviceType.get()):
                    self.dropDeviceType.focus()
                    return False

            elif self.dropConCount.get() == "0" and self.dropDeviceType.get() == "None":
                # Display warning message
                messagebox.showwarning("Invalid Selection", "Each belay device requires at least one connector. Please adjust your selections.")
                self.Reset()
                self.dropKnot.focus()
                return False

        # If all checks pass, return True
        return True
                            
    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This function is executed once the user clicks on the "Submit" button. Once the inputs 
        are validated, the inspection results loads the user selected data and is retained at the object class locations 
        before committing to the database. If all inputs are valid and confirmed by the user, the next stage of inspections is executed.
        """
        global blnValidate
        blnValidate = bool(False)             
        
        # First check if the input is empty, if so, notify the user the input needs attention 
        blnValidate = self.Validate_InputFields()
        
        # If status is true then proceed to update the result field, else, reset the fields
        if blnValidate is True:
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to upload the new custom rope system?', icon='question') is True:
                # print(CustomRopeSystem.aintRopeSystemIDCache)
                # print(CustomRopeSystem.astrRopeSystemNameCache) 
                # print(CustomRopeSystem.astrComplexityCacheCache)
                # print(CustomRopeSystem.aintConnectorCountCacheCache)
                # print(CustomRopeSystem.astrFirstConnectorTypeCache)
                # print(CustomRopeSystem.astrSecondConnectorTypeCache)
                # print(CustomRopeSystem.astrDeviceTypeCache)
                # Load the user data and prep the data for db dump
                blnValidate = self.Pull_UserInput()    
                
                if blnValidate is True:
                    # Check if the user would like to update another unit
                    if messagebox.askyesno(message='SUCCESSFUL UPDATE! \n\n Would you like to add another rope system?') is True:
                        # Clear the input fields and after data is submitted to the database
                        self.Reset()
                    else:
                        self.Exit()
            else:
                # Check if the user would like to reset the fields
                if messagebox.askyesno(message='ATTENTION! \n\n Would you like to reset the fields?', icon='question') is True:
                    # Clear the input fields and after data is submitted to the database
                    self.Clear()   
                        
    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        """       
        # Declare Local Variables
        sqlRopeSysSel = ("TCustomRopeSystems", "intRopeSystemID", "strRopeSystemName", "strComplexity", "intConnectorCount", 
                        "strFirstConnectorType", "strSecondConnectorType", "strDeviceType")

        # Get the selection strings
        strSelectionOption = self.Check_Simple_Or_Complex()
        if strSelectionOption == "simple":
            RopeSystemName = "Simple Rope System"
            strComplexity = "Simple"
            strKnot = "None"
            intConnectorCount = 0
            strFirstConnectorType = "None"
            strSecondConnectorType = "None"
            strDeviceType = "None"
        else:
            # First get the user defined name for the complex rope system then the rest of the inputs
            resultTuple = self.Add_Complex_RopeSys_Name()
            RopeSystemName = resultTuple[0]
            strComplexity = "Complex"
            strKnot = self.dropKnot.get()
            
            # Try to set the connector count
            try:
                intConnectorCount = int(self.dropConCount.get())
            except ValueError:
                # Handle invalid integer input for connector count
                intConnectorCount = 0  # or other default/error handling
                
            strFirstConnectorType = self.dropFirstConType.get().strip() or "None"
            strSecondConnectorType = self.dropSecondConType.get().strip() or "None"
            strDeviceType = self.dropDeviceType.get().strip()

        # # Display the string representation
        # print(CustomRopeSystem)
        
        if RopeSystemName != None:
            # Get the ID of the selected type item 
            intCustomRopeSystemID = self.Get_Or_Create_ID(RopeSystemName, sqlRopeSysSel) 
                
            # Assign the local object to the class objects
            crs = CustomRopeSystem(intCustomRopeSystemID, RopeSystemName, strComplexity, strKnot, 
                                    intConnectorCount, strFirstConnectorType, strSecondConnectorType, strDeviceType)
            
            # Commit the data for the inspection
            CustomRopeSystem.intRopeSystemID = crs.intRopeSystemID
            CustomRopeSystem.strRopeSystemName = crs.strRopeSystemName
            CustomRopeSystem.strComplexity = crs.strComplexity
            CustomRopeSystem.strPreTiedKnot = crs.strPreTiedKnot
            CustomRopeSystem.intConnectorCount = crs.intConnectorCount
            CustomRopeSystem.strFirstConnectorType = crs.strFirstConnectorType
            CustomRopeSystem.strSecondConnectorType = crs.strSecondConnectorType
            CustomRopeSystem.strDeviceType = crs.strDeviceType
            
            # Add the new custom rope system 
            CustomRopeSystem.Add_CustomRopeSystem_Query(CustomRopeSystem) 
            return True
        else:
            return False

    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
                        
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlStatement[0], sqlStatement[1]))    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
    
    def Check_Simple_Or_Complex(self):
        """ 
        Function Name: Check_Simple_Or_Complex
        Function Purpose: This function is executed once the user clicks on the option of simple or complex rope system.
        """        
        # Get the selected option from the radio button
        strSelectionOption = self.objRadioValue.get()
            
        # Return the selected option
        return strSelectionOption
        
    def Add_Complex_RopeSys_Name(self):
        """ 
        Function Name: Add_Complex_RopeSys_Name
        Function Purpose: This function is executed once the user selects a complex rope system. This gets the user defined system name. 
        """           
        # Hide the main window
        self.Withdraw()  

        # Call your AddComplexRopeSysName function here
        newWindow = AddComplexRopeSysName(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Retrieve RopeSystemName and RopeSystemID from newWindow
        # This assumes newWindow has these attributes set
        RopeSystemName = getattr(newWindow, 'RopeSystemName', None)
        RopeSystemID = getattr(newWindow, 'RopeSystemID', None)

        # Show the main window after the new window is closed
        self.Deiconify()  

        return (RopeSystemName, RopeSystemID)  

    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Expose the window widget to the user
        self.deiconify()
                                                            
    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This button executes when the user wants to reset the values.
        """
        # Check if the radio obj is simple or not. If simple, pass and if Complex, reset values
        if self.objRadioValue.get() == "simple":
            pass
        else:
            # Delete the entries
            self.dropKnot.set("")
            self.dropConCount.set("")
            self.dropFirstConType.set("")
            self.dropSecondConType.set("")
            self.dropDeviceType.set("")

            # Disable the drop menus for first and second connector 
            self.dropFirstConType.configure(state='disabled')
            self.dropSecondConType.configure(state='disabled')
            
            # Populate the dropdown based on default radio button selection
            self.Populate_Dropdown()
        
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()


#######################################################################################################
# Add Complex Rope System Name Class
#######################################################################################################         
class AddComplexRopeSysName(tk.Toplevel):
    """
    Class Name: AddComplexRopeSysName
    Class Description: This class adds a New Complex Rope System Name to the database.
    """
    def __init__(self, parent):    
        # Initialize the Toplevel window
        super().__init__(parent)

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk window 
        self.x = (self.widthSize/2) - (600/2)     
        self.y = (self.heightSize/2) - (150/2)          
        
        # Set the window attributes
        self.title("Add New Complex Rope System Name")
        self.geometry('%dx%d+%d+%d' % (600, 150, self.x, self.y))
        self.resizable(False, False)

        # Create the frame to hold the input fields
        self.frameInput = tk.LabelFrame(self, text="Rope System Name")
        self.frameInput.place(x=30, y=5, width=540, height=90)

        # Create the labels 
        self.lblRopeSysName = tk.Label(self.frameInput, text="Complex Rope System Name:")
        self.lblRopeSysName.place(x=60, y=20)

        # Create the entry input box
        self.RopeSysNameInput = tk.Entry(self, width=35)
        self.RopeSysNameInput.place(x=280, y=45)
        # self.RopeSysNameInput.focus()
        
        # Create the buttons
        self.btnExit = tk.Button(self, text="Back", width=10, command=self.Exit)
        self.btnReset = tk.Button(self, text="Reset", width=10, command=self.Reset)
        self.btnSubmit = tk.Button(self, text="Submit", width=10, command=self.Submit)

        # Position the buttons
        self.btnExit.place(x=130, y=110)
        self.btnReset.place(x=260, y=110)
        self.btnSubmit.place(x=390, y=110)

    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(message='ERROR \n\n Input should not be empty. Please Try again.', icon='warning')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(message='ERROR \n\n Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate

    def Validate_InputFields(self):
        """
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        # Retrieve user input
        userInput = self.RopeSysNameInput.get().strip()
        
        # First, check if the input is not empty using Check_Input
        if not AddComplexRopeSysName.Check_Input(userInput):
            self.RopeSysNameInput.configure(background='Yellow')
            self.RopeSysNameInput.focus()
            return False
        
        # Validate user input for basic check and string content
        if not BaseFunctions.Validate_String_Input(userInput):
            messagebox.showwarning("INVALID INPUT", "Please enter a valid input.", icon='warning')
            self.RopeSysNameInput.configure(background='Yellow')
            self.RopeSysNameInput.focus()
            return False

        # Capitalize the first letter of each word
        formattedInput = ' '.join(word.capitalize() for word in userInput.split())
        
        # Check for uniqueness in the system
        if formattedInput in CustomRopeSystem.astrRopeSystemNameCache:
            messagebox.showwarning("INVALID INPUT", f"{formattedInput} already exists. Please enter another input.", icon='warning')
            self.RopeSysNameInput.delete(0, 'end')
            self.RopeSysNameInput.configure(background='Yellow')
            self.RopeSysNameInput.focus()
            return False

        # Input passed all checks, proceed to set validated and formatted input
        self.RopeSystemName = formattedInput
        self.RopeSystemID = Queries.Get_MaxPrimaryKeys(Queries, "TCustomRopeSystems", "intRopeSystemID")
        return True                                    

    def Clear_BG_Color(self):
        """ 
        Function Name: Clear_BG_Color
        Function Purpose: This button executes when the user submits their entries and clears the background
        color before any validation checks.
        """
        # Delete the button after submission
        self.RopeSysNameInput.configure(background='White')
        
    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This button executes when the user wants to reset the values.
        """
        # Delete the button after submission
        self.RopeSysNameInput.delete(0, END)     
        
        # Clear out the background colors and set to default as 'white'
        AddComplexRopeSysName.Clear_BG_Color(self)

        # Reload the data after user submits entry
        # CustomRopeSystem.Delete_CustomRopeSystem_Data(CustomRopeSystem)
        # CustomRopeSystem.Get_CustomRopeSystem_Data(CustomRopeSystem)
        
    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the new location to the db. Else, reset
        """
        # Check if all of the inputs are valid
        global blnValidate 
        blnValidate = bool(False)
        
        # Clear out the background colors and set to default as 'white'
        AddComplexRopeSysName.Clear_BG_Color(self)
                
        # Get the blnValidate status
        blnValidate = AddComplexRopeSysName.Validate_InputFields(self)
        
        # Check if the input is valid
        if blnValidate:
            # Check first with the user if the entries are correct before dumping to DB
            if messagebox.askyesno(message=f'CAUTION! \n\n Proceed to add new complex rope system name: {self.RopeSystemName}?'):
                self.Exit()
            else:
                self.Reset()

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        # Load the data from the database
        CustomRopeSystem.Delete_CustomRopeSystem_Data(CustomRopeSystem)
        CustomRopeSystem.Get_CustomRopeSystem_Data(CustomRopeSystem)        
        self.destroy()


#######################################################################################################
# Rope Selection Class
#######################################################################################################   

class GymRopeSelection(tk.Tk):
    """
    Class Name: GymRopeSelection
    Class Description: This class is to conduct Gym Rope Selection.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new Gym Rope Selection. User must click
        'Next' Button in order to progress to the next inspection type.
        """
        # Load the data from the database
        # Start_Menu.Load_Obj_Lists(self) # Make sure to comment this out after testing
        
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (650/2)     
        self.y = (self.heightSize/2) - (585/2)          
        
        # Create the Window attributes                
        self.title("Rope System Selection")
        self.geometry('%dx%d+%d+%d' % (650, 585, self.x, self.y))
        self.resizable(False, False)

        # Load the query selection widget for rope system selection
        self.RopeSystem_Selection_Widget()
        
        # Load the query selection widget for Search by serial or bumper num
        self.Selection_Widget()
        
        # Create the frame fields
        self.typeFrame = tk.LabelFrame(self, text="Additional Info")
        self.typeFrame.place(x=100, y=325, width=450, height=200)
                
        # Create the label for the checkboxes
        self.lblRopeLocation = tk.Label(self.typeFrame, text="Rope Location:")
        self.lblInUse = tk.Label(self.typeFrame, text="Rope In Use:")
        self.lblQuestion = tk.Label(self.typeFrame, text="Can't find what you're looking for?")
                        
        # Create the label locations
        self.lblRopeLocation.place(x=65, y=15)
        self.lblInUse.place(x=78, y=55)
        self.lblQuestion.place(x=125, y=95)

        # Create the drop down menu list for each attribute
        self.dropRopeLocation = ttk.Combobox(self.typeFrame, values=WallLocation.astrWallLocationDesc, state='readonly')
        self.dropInUse = ttk.Combobox(self.typeFrame, values=['Yes', 'No'], state='readonly')
        
        # Create the drop down menu size for each attribute
        self.dropRopeLocation.configure(width=25)
        self.dropInUse.configure(width=25)
        
        # Create the grid for the drop down menu list objects
        self.dropRopeLocation.place(x=190, y=15)  
        self.dropInUse.place(x=190, y=55)  

        # Check if the cache values for any drop menus have been previously selected and set the values
        if (Bool_Flag.blnRopePersistFlag == True) or (Bool_Flag.blnComplexWithBelayDeviceFlag is True) or (Bool_Flag.blnComplexWithConnectorFlag is True) or (Bool_Flag.blnSimpleRopeFlag is True):
            self.Set_Previous_Drop_List(CustomRopeSystem.strRopeSystemName, self.dropRopSysSelection)
            self.Set_Previous_Drop_List(Ropes.strSerialNum, self.dropRopeSelection)
            self.Set_Previous_Drop_List(Ropes.strEquipInUse, self.dropInUse)
            self.Set_Previous_Drop_List(WallLocation.strWallLocationDesc, self.dropRopeLocation)

            # Manually trigger the selection logic without an event
            self.On_Rope_System_Selected(None)

        # Create the buttons
        self.btnUpdateRopeInfo = Button(self.typeFrame, width=12, text = "Update Rope Info", command=self.Update_Rope_Info)
        self.btnAddRope = Button(self.typeFrame, width=12, text="Add Rope", command=self.Add_Rope)
        self.btnAddLocation = Button(self.typeFrame, width=12, text = "Add Location", command=self.Add_Location)
        self.btnExit = Button(self, width=10, text="Back", command=self.Back)
        self.btnReset = Button(self, width=10, text="Reset",command=self.Reset)
        self.btnNext = Button(self, width=10, text="Next", command=self.Next)
            
        # Create the position of the button
        self.btnUpdateRopeInfo.place(x=40, y=140)
        self.btnAddRope.place(x=175, y=140) 
        self.btnAddLocation.place(x=310, y=140)
        self.btnExit.place(x=168, y=540) 
        self.btnNext.place(x=400, y=540) 
        self.btnReset.place(x=285, y=540)
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()  
        
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the object lists
        Start_Menu.Delete_Obj_Lists(self)   
        
        # Send the user back to the main menu        
        Ropes_Menu()
        
    def Selection_Widget(self):
        """ 
        Function Name: Selection_Widget
        Function Purpose: This function populates the search by widget for Serial or Bumper Num search.
        """           
        # Create the first frame to hold the input fields
        self.selectInput = LabelFrame(self, text="Select Rope")
        self.selectInput.place(x=100, y=220, width=450, height=100)

        # Create the labels 
        self.lblSearchByRopeID = Label(self.selectInput, text="Query by Rope ID:")
        self.lblRopeSelection = Label(self.selectInput, text="Rope ID Selection:")

        # Create the label locations
        self.lblSearchByRopeID.place(x=50, y=5)
        self.lblRopeSelection.place(x=50, y=40)

        # Create variables to hold the value of the selected radio button
        self.objRadioValue = tk.StringVar(value='serial')

        # List objects of serial and bumper values
        self.astrSerialNumList = Ropes.astrSerialNumCache
        self.astrBumperNumList = Ropes.astrBumperNumCache

        # Create the radio buttons
        self.rbSerial = tk.Radiobutton(self.selectInput, text="Serial Number", variable=self.objRadioValue, value="serial", command=self.Populate_Dropdown)
        self.rbBumper = tk.Radiobutton(self.selectInput, text="Bumper Number", variable=self.objRadioValue, value="bumper", command=self.Populate_Dropdown)

        # Place the radio buttons next to each other using .place()
        self.rbSerial.place(x=180, y=5)
        self.rbBumper.place(x=290, y=5)
                    
        # Create the entry input box
        self.dropRopeSelection = ttk.Combobox(self.selectInput, values=self.astrSerialNumList, state='readonly')
        self.dropRopeSelection.configure(width=25,)

        # Populate the dropdown based on the default radio button selection
        self.Populate_Dropdown()

        # Create the grid for all of the entry input fields
        self.dropRopeSelection.place(x=190, y=40) 

    def RopeSystem_Selection_Widget(self):
        """ 
        Function Name: RopeSystem_Selection_Widget
        Function Purpose: This function populates the search by widget for Rope System Setup search.
        """           
        # Create the first frame to hold the input fields
        self.selectRopeSysSelect = LabelFrame(self, text="System Selection")
        self.selectRopeSysSelect.place(x=100, y=35, width=450, height=180)

        # Create the labels 
        self.lblRopeSysDrop = Label(self.selectRopeSysSelect, text="Choose Rope System:")
        self.lblSysComplex = Label(self.selectRopeSysSelect, text="System Complexity:")
        self.lblPretiedKnots = Label(self.selectRopeSysSelect, text="Pre-tied Knots:")
        self.lblConnectorCount = Label(self.selectRopeSysSelect, text="Connector Count:")
        self.lblBelayDevice = Label(self.selectRopeSysSelect, text="Belay Device:")
        
        # Create the label locations
        self.lblRopeSysDrop.place(x=32, y=5)
        self.lblSysComplex.place(x=40, y=35)
        self.lblPretiedKnots.place(x=68, y=65)
        self.lblConnectorCount.place(x=50, y=95)
        self.lblBelayDevice.place(x=75, y=125)

        # List objects of serial and bumper values
        self.astrSetUpSelection = CustomRopeSystem.astrRopeSystemNameCache
        self.astrSetupList = self.astrSetUpSelection

        # Create the entry input box
        self.dropRopSysSelection = ttk.Combobox(self.selectRopeSysSelect, values=self.astrSetupList, state='readonly')
        self.dropRopSysSelection.configure(width=25,)

        # Create the grid for all of the entry input fields
        self.dropRopSysSelection.place(x=190, y=5) 

        # Bind the selection event after the Combobox is created
        self.dropRopSysSelection.bind("<<ComboboxSelected>>", self.On_Rope_System_Selected)

        # Create the entry input box
        self.SysComplexInput = Entry(self.selectRopeSysSelect, width=28, state='disabled')
        self.PretiedKnotInput = Entry(self.selectRopeSysSelect, width=28, state='disabled')
        self.ConnectorCountInput = Entry(self.selectRopeSysSelect, width=28, state='disabled')
        self.BelayDeviceInput = Entry(self.selectRopeSysSelect, width=28, state='disabled')
                
        # Create the placements for the entry inputs
        self.SysComplexInput.place(x=190, y=35)
        self.PretiedKnotInput.place(x=190, y=65)
        self.ConnectorCountInput.place(x=190, y=95)
        self.BelayDeviceInput.place(x=190, y=125)

    def On_Rope_System_Selected(self, event):
        """
        Function Name: on_rope_system_selected
        Function Purpose: Called when a new rope system is selected from the dropdown.
        """
        # Declare Local Variables
        default_index = -1
        
        # Get the current index of the selected item
        selected_index = self.dropRopSysSelection.current()
        
        if selected_index != default_index:
            # Fetch data from CustomRopeSystem class arrays using the selected index
            sys_complexity = CustomRopeSystem.astrComplexityCache[selected_index]
            pretied_knots = CustomRopeSystem.astrPreTiedKnotCache[selected_index]
            connector_count = str(CustomRopeSystem.aintConnectorCountCache[selected_index])
            belay_device = CustomRopeSystem.astrDeviceTypeCache[selected_index]

            # Fill the input fields with the retrieved data
            self.Update_Entry_Field(self.SysComplexInput, sys_complexity)
            self.Update_Entry_Field(self.PretiedKnotInput, pretied_knots)
            self.Update_Entry_Field(self.ConnectorCountInput, connector_count)
            self.Update_Entry_Field(self.BelayDeviceInput, belay_device)
        else:
            # Clear the fields if no selection is made
            for entry in [self.SysComplexInput, self.PretiedKnotInput, self.ConnectorCountInput, self.BelayDeviceInput]:
                self.Update_Entry_Field(entry, "")

    def Update_Entry_Field(self, entry_field, value):
        """
        Function Name: Update_Entry_Field
        Function Purpose: Update an entry field with a given value.
        """
        entry_field.configure(state='normal')
        entry_field.delete(0, tk.END)
        entry_field.insert(0, value)
        entry_field.configure(state='disabled')
                    
    def Populate_Dropdown(self):
        """ 
        Function Name: Populate_Dropdown
        Function Purpose: This function populates the dropdown based on the radio button selection.
        """           
        if self.objRadioValue.get() == "serial":
            self.dropRopeSelection["values"] = self.astrSerialNumList
        else:
            self.dropRopeSelection["values"] = self.astrBumperNumList
        self.dropRopeSelection.set("")                             
        
    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)
        
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.', icon='warning')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate
    
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)  

        # Check the user input
        blnValidate = GymRopeSelection.Check_Input(self.dropRopSysSelection.get())

        # Check if the input is valid
        if (blnValidate is True):
            # Check the user input
            blnValidate = GymRopeSelection.Check_Input(self.dropRopeSelection.get())         
                
            # Check if the input is valid
            if (blnValidate is True):
                # Check the user input
                blnValidate = GymRopeSelection.Check_Input(self.dropRopeLocation.get())         
                
                # Check if the input is valid
                if (blnValidate is True):
                    # Check the user input
                    blnValidate = GymRopeSelection.Check_Input(self.dropInUse.get())         
                    
                    # Check if the input is valid
                    if (blnValidate is True):
                        blnValidate = True
                    else:
                        # Return blnValidate as False
                        blnValidate = False
                        self.dropInUse.focus()
                else:
                    # Return blnValidate as False
                    blnValidate = False
                    self.dropRopeLocation.focus()                
            else:
                # Return blnValidate as False
                blnValidate = False
                self.dropRopeSelection.focus()                                                     
        else:
            # Return blnValidate as False
            blnValidate = False
            self.dropRopSysSelection.focus()

        return blnValidate            

    def Next_Inspection(self):
        """ 
        Function Name: Next_Inspection
        Function Purpose: This function is executed once the user clicks on Next button to move to the nex inspection
        type window. Withdraw the parent window and load the new window.
        """      
        # Hide the main window
        self.Exit()  

        # Set the default bool values before moving to the next inspection
        Bool_Flag.Set_ComplexWithConnector_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_ComplexWithBelayDevice_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_ComplexWithTwo_Bool_Value_False(Bool_Flag)
        Bool_Flag.Set_SimpleRope_Bool_Value_False(Bool_Flag)
        
        # Determine the rope system complexity to determine the path the user takes
        if CustomRopeSystem.strComplexity == "Simple":
            # set the Simple Rope System Bool to true
            Bool_Flag.Set_SimpleRope_Bool_Value_True(Bool_Flag)
            
            # Open the window for simple rope inspection
            RopeInspection() 
        else:
            # Complex Rope Systems
            if CustomRopeSystem.strPreTiedKnot == "None" and CustomRopeSystem.intConnectorCount == 0 and CustomRopeSystem.strDeviceType != "None":
                # Path for complex system with no knots, no connectors but a device type
                self.ComplexRopeInspection_NoKnots_NoConnectors_YesDevice(Ropes.strEquipInUse)  

            elif CustomRopeSystem.strPreTiedKnot == "None" and CustomRopeSystem.intConnectorCount != 0 and CustomRopeSystem.strDeviceType != "None":
                # Path for complex system with no knots, some connectors and a device type
                self.ComplexRopeInspection_NoKnots_YesConnectors_YesDevice(Ropes.strEquipInUse)  

            elif CustomRopeSystem.strPreTiedKnot == "None" and CustomRopeSystem.intConnectorCount != 0 and CustomRopeSystem.strDeviceType == "None":
                # Path for system with connectors but no knots and no device
                self.ComplexRopeInspection_NoKnots_YesConnectors_NoDevice(Ropes.strEquipInUse)

            elif CustomRopeSystem.strPreTiedKnot != "None" and CustomRopeSystem.intConnectorCount != 0 and CustomRopeSystem.strDeviceType != "None": 
                # Path for complex system with knots, connectors and a device type
                self.ComplexRopeInspection_YesKnots_YesConnectors_YesDevice(Ropes.strEquipInUse) 

            elif CustomRopeSystem.strPreTiedKnot != "None" and CustomRopeSystem.intConnectorCount == 0 and CustomRopeSystem.strDeviceType != "None":
                # Path for system with knots, no connectors, and with device type
                self.ComplexRopeInspection_YesKnots_NoConnectors_YesDevice(Ropes.strEquipInUse)

            elif CustomRopeSystem.strPreTiedKnot != "None" and CustomRopeSystem.intConnectorCount != 0 and CustomRopeSystem.strDeviceType == "None":
                # Path for system with connectors but no device
                self.ComplexRopeInspection_YesKnots_YesConnectors_NoDevice(Ropes.strEquipInUse)
                
            elif CustomRopeSystem.strPreTiedKnot != "None" and CustomRopeSystem.intConnectorCount == 0 and CustomRopeSystem.strDeviceType == "None":
                # Path for system with knots but no connectors and no device
                self.ComplexRopeInspection_YesKnots_NoConnectors_NoDevice()
                                
            else:
                # Handle cases that don't fit any of the above criteria
                messagebox.showwarning("Invalid Selection", "The selected rope system configuration is not valid for inspection.")

    def ComplexRopeInspection_NoKnots_NoConnectors_YesDevice(self, strInUseFlag):
        """ 
        Function Name: ComplexRopeInspection_NoKnots_NoConnectors_YesDevice
        Function Purpose: This function when the user selects a complex rope system with knots, connectors and a device type.
        """     
        # Check if the item is in use, if not, return  
        if strInUseFlag == "No":
            if not messagebox.askyesno(message='CAUTION!\n\nPlease confirm: You have chosen a rope marked as out of use, which is part of a system that includes belay devices. Have these devices been detached from the rope system?'):
                messagebox.showwarning(message='TAKE ACTION!\n\nPlease remove the belay devices from the rope system before proceeding.', icon='warning')
                return

        # Set the bool flags
        Bool_Flag.Set_ComplexWithBelayDevice_Bool_Value_True(Bool_Flag)
        
        # Proceed with the inspections
        BelayDeviceSelection()

    def ComplexRopeInspection_NoKnots_YesConnectors_YesDevice(self, strInUseFlag):
        """ 
        Function Name: ComplexRopeInspection_NoKnots_YesConnectors_YesDevice
        Function Purpose: This function when the user selects a complex rope system with knots, connectors and a device type.
        """     
        # Check if the item is in use, if not, return  
        if strInUseFlag == "No":
            if not messagebox.askyesno(message='CAUTION!\n\nPlease confirm: You have chosen a rope marked as out of use, which is part of a system that includes connectors and belay devices. Have these connectors and devices been detached from the rope system?'):
                messagebox.showwarning(message='TAKE ACTION!\n\nPlease remove the connectors and belay devices from the rope system before proceeding.', icon='warning')
                return

        # Set the bool flags
        Bool_Flag.Set_ComplexWithConnector_Bool_Value_True(Bool_Flag)
        Bool_Flag.Set_ComplexWithBelayDevice_Bool_Value_True(Bool_Flag)
        
        # Proceed with the inspections
        if CustomRopeSystem.intConnectorCount > 1:
            Bool_Flag.Set_ComplexWithTwo_Bool_Value_True(Bool_Flag)
            TwoConnectorSelection()
        else:
            ConnectorSelection()

    def ComplexRopeInspection_NoKnots_YesConnectors_NoDevice(self, strInUseFlag):
        """ 
        Function Name: ComplexRopeInspection_NoKnots_YesConnectors_NoDevice
        Function Purpose: This function when the user selects a complex rope system with knots, connectors and a device type.
        """     
        # Check if the item is in use, if not, return  
        if strInUseFlag == "No":
            if not messagebox.askyesno(message='CAUTION!\n\nPlease confirm: You have chosen a rope marked as out of use, which is part of a system that includes connectors. Have these connectors been detached from the rope system?'):
                messagebox.showwarning(message='TAKE ACTION!\n\nPlease remove the connectors from the rope system before proceeding.', icon='warning')
                return

        # Set the bool flags
        Bool_Flag.Set_ComplexWithConnector_Bool_Value_True(Bool_Flag)
        
        # Proceed with the inspections
        if CustomRopeSystem.intConnectorCount > 1:
            Bool_Flag.Set_ComplexWithTwo_Bool_Value_True(Bool_Flag)
            TwoConnectorSelection()
        else:
            ConnectorSelection()
        
    def ComplexRopeInspection_YesKnots_YesConnectors_YesDevice(self, strInUseFlag):
        """ 
        Function Name: ComplexRopeInspection_YesKnots_YesConnectors_YesDevice
        Function Purpose: This function when the user selects a complex rope system with knots, connectors and a device type.
        """   
        # Check if the item is in use, if not, return  
        if strInUseFlag == "No":
            if not messagebox.askyesno(message='CAUTION!\n\nPlease confirm: You have chosen a rope marked as out of use, which is part of a system that includes connectors and belay devices. Have these connectors and devices been detached from the rope system?'):
                messagebox.showwarning(message='TAKE ACTION!\n\nPlease remove the connectors and belay devices from the rope system before proceeding.', icon='warning')
                return

        if not messagebox.askyesno(message='CAUTION!\n\nWere the knotted areas of the rope untied?'):
            messagebox.showwarning(message='CAUTION!\n\nPlease untie each knot before proceeding.', icon='warning')
            return

        # Set the bool flags
        Bool_Flag.Set_ComplexWithConnector_Bool_Value_True(Bool_Flag)
        Bool_Flag.Set_ComplexWithBelayDevice_Bool_Value_True(Bool_Flag)
        
        # Proceed with the inspections
        if CustomRopeSystem.intConnectorCount > 1:
            Bool_Flag.Set_ComplexWithTwo_Bool_Value_True(Bool_Flag)
            TwoConnectorSelection()
        else:
            ConnectorSelection()
                    
    def ComplexRopeInspection_YesKnots_NoConnectors_YesDevice(self, strInUseFlag):
        """ 
        Function Name: ComplexRopeInspection_YesKnots_NoConnectors_YesDevice
        Function Purpose: This function when the user selects a complex rope system with knots, no connectors and a device type.
        """     
        # Check if the item is in use, if not, return  
        if strInUseFlag == "No":
            if not messagebox.askyesno(message='CAUTION!\n\nPlease confirm: You have chosen a rope marked as out of use, which is part of a system that includes belay devices. Have these devices been detached from the rope system?'):
                messagebox.showwarning(message='TAKE ACTION!\n\nPlease remove the belay devices from the rope system before proceeding.', icon='warning')
                return

        if not messagebox.askyesno(message='CAUTION!\n\nWere the knotted areas of the rope untied?'):
            messagebox.showwarning(message='CAUTION!\n\nPlease untie each knot before proceeding.', icon='warning')
            return

        # Set the bool flags
        Bool_Flag.Set_ComplexWithBelayDevice_Bool_Value_True(Bool_Flag)
        
        # Proceed with the inspections
        BelayDeviceSelection()

    def ComplexRopeInspection_YesKnots_YesConnectors_NoDevice(self, strInUseFlag):
        """ 
        Function Name: ComplexRopeInspection_YesKnots_YesConnectors_NoDevice
        Function Purpose: This function when the user selects a complex rope system with knots, connectors but no device type.
        """     
        # Check if the item is in use, if not, return  
        if strInUseFlag == "No":
            if not messagebox.askyesno(message='CAUTION!\n\nPlease confirm: You have chosen a rope marked as out of use, which is part of a system that includes connectors. Have these connectors been detached from the rope system?'):
                messagebox.showwarning(message='TAKE ACTION!\n\nPlease remove the connectors from the rope system before proceeding.', icon='warning')
                return

        if not messagebox.askyesno(message='CAUTION!\n\nWere the knotted areas of the rope untied?'):
            messagebox.showwarning(message='CAUTION!\n\nPlease untie each knot before proceeding.', icon='warning')
            return

        # Set the bool flags
        Bool_Flag.Set_ComplexWithConnector_Bool_Value_True(Bool_Flag)
        
        # Proceed with the inspections
        if  CustomRopeSystem.intConnectorCount > 1:
            Bool_Flag.Set_ComplexWithTwo_Bool_Value_True(Bool_Flag)
            TwoConnectorSelection()
        else:
            ConnectorSelection()

    def ComplexRopeInspection_YesKnots_NoConnectors_NoDevice(self):
        """ 
        Function Name: ComplexRopeInspection_YesKnots_NoConnectors_NoDevice
        Function Purpose: This function when the user selects a complex rope system with knots, no connectors and no device type.
        """     
        if not messagebox.askyesno(message='CAUTION!\n\nWere the knotted areas of the rope untied?'):
            messagebox.showwarning(message='CAUTION!\n\nPlease untie each knot before proceeding.', icon='warning')
            return

        # Proceed with the inspections
        RopeInspection()
                                
    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the root
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Hide the current window
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """     
        # Hide the current window
        self.Exit()  
        
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)
        
        # Set the stored lists
        Start_Menu.Delete_Obj_Lists(self) 

        # Show the main window after the new window is closed
        Ropes_Menu()

    def Update_Dropdown_Values(self):
        """ 
        Function Name: Update_Dropdown_Values
        Function Purpose: This function is executed once the user clicks on add and update buttons the drop down
        object list with the new values.
        """             
        # Ensure the dropdowns are Comboboxes and clear their current selections
        if isinstance(self.dropRopeSelection, ttk.Combobox):
            self.dropRopeSelection.set("") 
        if isinstance(self.dropRopeLocation, ttk.Combobox):
            self.dropRopeLocation.set("")

        # Update the values for connector selection dropdown
        self.astrSerialNumList = Ropes.astrSerialNumCache
        self.astrBumperNumList = Ropes.astrBumperNumCache
        if isinstance(self.dropRopeSelection, ttk.Combobox):
            self.dropRopeSelection['values'] = self.astrSerialNumList

        # Update the values for connector location dropdown
        if isinstance(self.dropRopeLocation, ttk.Combobox):
            self.dropRopeLocation['values'] = WallLocation.astrWallLocationDesc
            
        # # Populate the dropdown menus
        # self.dropRopeSelection.set("") 
        # self.astrSerialNumList = Ropes.astrSerialNumCache
        # self.astrBumperNumList = Ropes.astrBumperNumCache
        # self.dropRopeSelection['values'] = self.astrSerialNumList
        # self.dropRopeLocation['values'] = WallLocation.astrWallLocationDesc

    def Add_Rope(self):
        """ 
        Function Name: Add_Rope
        Function Purpose: This function is executed once the user clicks on AddRope button and updates the drop down
        object list with the new values.
        """
        # Reset the fields
        self.Reset()
        
        # Hide the main window
        self.Withdraw()  

        # Call your AddRope function here
        newWindow = AddRope(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Show the main window after the new window is closed
        self.Deiconify()  

        # Update the drop-down menu values
        self.Update_Dropdown_Values()

    def Update_Rope_Info(self):
        """ 
        Function Name: Update_Rope_Info
        Function Purpose: This function is executed if the user clicks Update Rope Information button. 
        """
        # Reset the fields
        self.Reset()
        
        # Hide the main window
        self.Withdraw()  

        # Call your AddRope function here
        newWindow = UpdateRopeInfo(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Show the main window after the new window is closed
        self.Deiconify()  

        # Update the drop-down menu values
        self.Update_Dropdown_Values()
        
    def Add_Location(self):
        """ 
        Function Name: Add_Location
        Function Purpose: This function is executed once the user clicks on AddLocation button and updates the drop down
        object list with the new values.
        """           
        # Hide the main window
        self.Withdraw()  

        # Call your AddLocation function here
        newWindow = AddLocation(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Show the main window after the new window is closed
        self.Deiconify()  

        # Update the drop-down menu values
        self.Update_Dropdown_Values()

    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        """   
        # Get the selected values from the drop menus
        if self.dropRopeSelection.get() in Ropes.astrSerialNumCache:
            SerialNum = self.dropRopeSelection.get()
        else:
            intPrimID = Ropes.astrBumperNumCache.index(self.dropRopeSelection.get()) + 1
            SerialNum = Ropes.astrSerialNumCache[intPrimID]
        
        # Get the location and in use status
        RopeSysSelection = self.dropRopSysSelection.get()
        UnitLocation = self.dropRopeLocation.get()
        InUseStatus = self.dropInUse.get()

        # Commit the data to load the rope system class objects with the data from the db
        CustomRopeSystem.strRopeSystemName = RopeSysSelection
        CustomRopeSystem.Set_CustomRopeSystem_Selection(CustomRopeSystem)

        # Commit the data to load the Rope class objects with the data from the db
        Ropes.strSerialNum = SerialNum
        Ropes.strEquipInUse = InUseStatus
        Ropes.Set_Ropes_Selection(Ropes)

        # Commit the data to load the WallLocation class objects with the data from the db
        WallLocation.strWallLocationDesc = UnitLocation
        WallLocation.Get_WallLocation_Selection(WallLocation)

    def Next(self):
        """ 
        Function Name: Next
        Function Purpose: This function is executed once the user clicks on the "Next" button. Once the inputs 
        are validated, the inspection results loads the user selected data and is retained at the object class locations 
        before committing to the database. If all inputs are valid and confirmed by the user, the next stage of inspections is executed.
        """
        global blnValidate
        blnValidate = bool(False)             
        
        # First check if the input is empty, if so, notify the user the input needs attention 
        blnValidate = self.Validate_InputFields()
        
        # If status is true then proceed to update the result field, else, reset the fields
        if blnValidate is True:
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to next inspection component?', icon='question') is True:     
                # Load the user data and prep the data for db dump
                self.Pull_UserInput()     

                # Go to the next inspection component
                self.Next_Inspection()
            else:
                # Check if the user would like to reset the fields
                if messagebox.askyesno(message='ATTENTION! \n\n Would you like to reset the fields?', icon='question') is True:
                    # Clear the input fields and after data is submitted to the database
                    self.Reset()                

    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This function is executed once the user clicks on the reset button inside the root
        frame. If the user clicks 'Reset', all data is set back to default.
        """     
        # Set the list objects first element to the drop click object
        self.dropRopSysSelection.set("")
        self.dropRopeSelection.set("")
        self.dropRopeLocation.set("")
        self.dropInUse.set("")

        # Re-configure input entries to be active
        self.SysComplexInput.configure(state='normal')
        self.PretiedKnotInput.configure(state='normal')
        self.ConnectorCountInput.configure(state='normal')
        self.BelayDeviceInput.configure(state='normal')
        
        # Delete what is in the entry input fields
        self.SysComplexInput.delete(0, END)
        self.PretiedKnotInput.delete(0, END)
        self.ConnectorCountInput.delete(0, END)
        self.BelayDeviceInput.delete(0, END)

        # Re-configure input entries to be disabled
        self.SysComplexInput.configure(state='disabled')
        self.PretiedKnotInput.configure(state='disabled')
        self.ConnectorCountInput.configure(state='disabled')
        self.BelayDeviceInput.configure(state='disabled')
        
        # Reset the radio button to its default value
        self.objRadioValue.set("serial")

        # Populate the dropdown based on default radio button selection
        self.Populate_Dropdown()

        # Re-Populate the dropdown menus 
        self.dropRopeSelection["values"] = self.astrSerialNumList
        
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()


#######################################################################################################
# Rope Inspection Class
#######################################################################################################   
class RopeInspection(tk.Tk):
    """
    Class Name: RopeInspection
    Class Description: This class is to conduct Rope inspections.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new Rope inspection. User must click
        'Next' Button in order to progress to the next inspection type. A Visual and Physical inspection
        must be performed to complete the inspection.
        """
        # Load the data from the database
        # Start_Menu.Load_Obj_Lists(self) # Make sure to comment this out after testing
        
        # Create the root tkinter variable
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (805/2)     
        self.y = (self.heightSize/2) - (520/2)          
        
        # Create the Window attributes                
        self.title("Rope Inspection")
        self.geometry('%dx%d+%d+%d' % (805, 520, self.x, self.y))
        self.resizable(False, False)

        # Load the query selection widget for Search by serial or bumper num
        self.Selection_Widget()
        
        # Create the frame fields
        self.visCheckListFrame = tk.LabelFrame(self, text="Visual Inspection Results")
        self.visCheckListFrame.place(x=95, y=165, width=310, height=200)
        self.physCheckListFrame = tk.LabelFrame(self, text="Physical Inspection Results")
        self.physCheckListFrame.place(x=405, y=165, width=310, height=200)
        self.commFrame = tk.LabelFrame(self, text="Inspection Comment")
        self.commFrame.place(x=95, y=370, width=620, height=100)
                
        # Create the label for the checkboxes
        self.lblRopeVisualStatus = tk.Label(self.visCheckListFrame, text="Visual Status:")
        self.lblRopePhysicalStatus = tk.Label(self.physCheckListFrame, text="Physical Status:")
                        
        # Create the label locations
        self.lblRopeVisualStatus.place(x=15, y=155)
        self.lblRopePhysicalStatus.place(x=15, y=155)

        # Create the drop down menu list for each attribute
        self.dropRopeVisStatus = ttk.Combobox(self.visCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropRopePhysStatus = ttk.Combobox(self.physCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        
        # Create the drop down menu size for each attribute
        self.dropRopeVisStatus.configure(width=20)
        self.dropRopePhysStatus.configure(width=20)
        
        # Create the grid for the drop down menu list objects  
        self.dropRopeVisStatus.place(x=135, y=155)  
        self.dropRopePhysStatus.place(x=135, y=155)  

        # Create the master list for the textile and functional inspection types
        self.selectItems = Textile.astrTextileInspectionDesc
        
        # Create the checkbox lists for visual, physical
        self.visCheckList = [] 
        self.physCheckList = []
        
        # Create an empty list to store selected items
        self.checkboxVisStates = {}
        self.checkboxPhysStates = {}

        # Create the checkbox list
        self.Create_Check_Buttons(self.selectItems, self.visCheckListFrame, RopeVisSelection.astrRopeVisTextSelect, self.visCheckList, self.checkboxVisStates, self.Get_VisCheckbox_List, "visual")
        self.Create_Check_Buttons(self.selectItems, self.physCheckListFrame, RopePhysSelection.astrRopePhysTextSelect, self.physCheckList, self.checkboxPhysStates, self.Get_PhysCheckbox_List, "physical")

        # First check if the selection values have been assigned
        self.Set_Previous_Checkbox_List(RopeVisSelection.astrRopeVisTextSelect, self.visCheckList, self.selectItems)        
        self.Set_Previous_Checkbox_List(RopePhysSelection.astrRopePhysTextSelect, self.physCheckList, self.selectItems)
        
        # Check if the cache values for any drop menus have been previously selected and set the values
        if (Bool_Flag.blnRopePersistFlag == True):
            self.Set_Previous_Drop_List(RopeVisSelection.strRopeVisStatus, self.dropRopeVisStatus)
            self.Set_Previous_Drop_List(RopePhysSelection.strRopePhysStatus, self.dropRopePhysStatus)            

        # Create the comment field
        self.commInput = tk.Text(self.commFrame, state='normal')
        self.commInput.grid(row=0, column=0, padx=5, pady=4)
        self.commInput.configure(width=75, height=4, padx=1)
        
        # Create the buttons
        self.btnBack = Button(self, text="Back", width=10, command=self.Back)
        self.btnClear = Button(self, text="Clear", width=10, command=self.Reset)
        self.btnExit = Button(self, text="Exit", width=10, command=self.Exit)
        self.btnNext = Button(self, text="Next", width=10, command=self.Next)
            
        # Create the position of the button
        self.btnBack.place(x=170, y=480)
        self.btnExit.place(x=300, y=480) 
        self.btnClear.place(x=430, y=480)
        self.btnNext.place(x=560, y=480) 
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()

        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the stored data in the class attributes
        Start_Menu.Delete_Obj_Lists(self)

        # Open the Main Menu
        GymRopeSelection()            

    def Selection_Widget(self):
        """ 
        Function Name: Selection_Widget
        Function Purpose: This function populates the search by widget for Serial or Bumper Num search.
        """           
        # Create the first frame to hold the input fields
        self.typeFrame = tk.LabelFrame(self, text="Selected Rope")
        self.typeFrame.place(x=95, y=10, width=620, height=150)

        # Create the labels 
        self.lblRopeSerial = Label(self.typeFrame, text="Serial ID:")
        self.lblRopeBumper = Label(self.typeFrame, text="Bumper ID:")
        self.lblRopeType = tk.Label(self.typeFrame, text="Rope Type:")
        self.lblRopeLength = tk.Label(self.typeFrame, text="Rope Length:")

        # Create the label locations
        self.lblRopeSerial.place(x=197, y=5)
        self.lblRopeBumper.place(x=183, y=35)
        self.lblRopeType.place(x=183, y=65)
        self.lblRopeLength.place(x=170, y=95)

        # Create the entry input box
        self.SerialNumOut = Entry(self.typeFrame, width=30, state='normal')
        self.BumperNumOut = Entry(self.typeFrame, width=30, state='normal')
        self.RopeType = Entry(self.typeFrame, width=30, state='normal')
        self.RopeLength = Entry(self.typeFrame, width=30, state='normal')

        # Set the values selected from the user
        self.SerialNumOut.insert(0, Ropes.strSerialNum)
        self.BumperNumOut.insert(0, Ropes.strBumperNum)
        self.RopeType.insert(0, Ropes.strElasticity)
        self.RopeLength.insert(0, Ropes.strRopeLength)
        
        # Configure the state to disabled
        self.SerialNumOut.configure(state='disabled')
        self.BumperNumOut.configure(state='disabled')
        self.RopeType.configure(state='disabled')
        self.RopeLength.configure(state='disabled')
                
        # Create the grid for all of the entry input fields
        self.SerialNumOut.place(x=275, y=5)
        self.BumperNumOut.place(x=275, y=35)
        self.RopeType.place(x=275, y=65) 
        self.RopeLength.place(x=275, y=95) 
        
    def Create_Check_Buttons(self, selectItems, checkListFrame, arrayObject, checkList, checkboxStates, callback, strInsType):
        """ 
        Function Name: Create_Check_Buttons
        Function Description: This helper method to create the checkbox buttons
        """
        if strInsType == "visual" or strInsType == "physical":
            maxColPerRow = 2
        else:
            maxColPerRow = 4

        for index, item in enumerate(selectItems):
            # Check if the item was previously selected (exists in arrayObject)
            is_selected = item in arrayObject
            var = tk.StringVar(value='1' if is_selected else '0')
            checkList.append(var)

            # Use a lambda function to capture the current item in the loop
            checkBox = tk.Checkbutton(checkListFrame, text=item, variable=var, onvalue='1', offvalue='0', 
                                    command=lambda item=item, var=var: callback(item, var))
            
            # Store the variable in the checkboxStates dictionary
            checkboxStates[item] = var

            # Calculate the row and column position of checkbutton based on index and max columns 
            rowPosition = index // maxColPerRow
            colPosition = index % maxColPerRow
            checkBox.grid(row=rowPosition, column=colPosition, sticky="w", padx=10)
            
    def Set_Previous_Checkbox_List(self, selectList, checkboxList, paramsList):
        """
        Function Name: Set_Vis_Previous_Checkbox_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the checkboxes from the cache array list for all checkboxes.
        """   
        # First check if the cache values have been assigned
        if len(selectList) == 0:
            # Check the first item of the list    
            checkboxList[0].set('1')
        else:
            # Set the Selection data to the objects in the window
            for i, item in enumerate(paramsList):
                if item in selectList:
                    checkboxList[i].set('1')

    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)

    def Get_VisCheckbox_List(self, item, var):
        """
        Function Name: Get_VisCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':            
            self.Update_Checkbox_List(self.visCheckList, item, self.checkboxVisStates, "visual", RopeVisSelection.astrRopeVisTextSelect)
        # Checkbox was deselected
        else:
            self.Rope_Deselection(self.visCheckList, item, self.checkboxVisStates, "visual", RopeVisSelection.astrRopeVisTextSelect)
            
    def Get_PhysCheckbox_List(self, item, var):
        """
        Function Name: Get_PhysCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':          
            self.Update_Checkbox_List(self.physCheckList, item, self.checkboxPhysStates, "physical", RopePhysSelection.astrRopePhysTextSelect)
        # Checkbox was deselected
        else:
            self.Rope_Deselection(self.physCheckList, item, self.checkboxPhysStates, "physical", RopePhysSelection.astrRopePhysTextSelect)

    def Update_Checkbox_List(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Update_Checkbox_List
        Function Purpose: This function is a generalized method to update checkbox states and persistent data.
        """
        # Check if the first item is selected and deselect all remaining items
        if item == self.selectItems[0]:
            for selectedItem in checkboxList[1:]:
                selectedItem.set('0')
        # Check if any other item is selected and deselect the first item
        else:
            if checkboxList[0].get() == '1':
                checkboxList[0].set('0')

        # Check if the window section is functional
        if selectionKey == 'functional':
            # Update the checkbox states dictionary
            checkboxStates[item] = '1' if checkboxList[self.functItems.index(item)].get() == '1' else '0'
        else:
            # Update the checkbox states dictionary
            checkboxStates[item] = '1' if checkboxList[self.selectItems.index(item)].get() == '1' else '0'

        # Update the persistent data based on the updated checkbox states
        selectedItemsList = [item for item, state in checkboxStates.items() if state == '1']
        
        # Update the arrayObject with selectedItemsList        
        self.Update_Persistent_Array(arrayObject, selectedItemsList)

    def Rope_Deselection(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Rope_Deselection
        Function Purpose: This function is called when a checkbox is deselected.
        """
        # For now, I'm just printing a message. You can modify this to implement the desired behavior.
        # print(f"Checkbox {item} was deselected!")

        # If you want to remove an item from a persisted list or dictionary upon deselection, you can do so here:
        checkboxStates.pop(item, None)
        arrayObject.remove(item)
        
    def Update_Persistent_Array(self, arrayObject, selectedItemsList):
        """
        Function Name: Update_Persistent_Array
        Function Description: This function updates the arrayObject with the selected items list, while keeping existing persisted data.
        """
        # print("Selected Items:", selectedItemsList)
        # print("Before update:", arrayObject)

        selectedSet = set(selectedItemsList)
        arraySet = set(arrayObject)

        # Find items to add and remove
        toAdd = selectedSet - arraySet
        toRemove = arraySet - selectedSet

        for item in toAdd:
            arrayObject.append(item)
        for item in toRemove:
            arrayObject.remove(item)

        # print("After update:", arrayObject) 
        
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate

    def Check_Checkbox_Input(lstCheckBox, strFieldDesc):
        """
        Function Name: Check_Checkbox_Input
        Function Purpose: This function is called whenever a checkbox is present and needs to check if any of the entries are empty. If so,
        warn the user.
        """    
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)
            
        try:
            for i in range(0, len(lstCheckBox)):
                if lstCheckBox[i].get() == '1':
                    # Set blnValidated to True
                    blnValidate = True

            # Check if the blnValidated flag is true or false and warn the user if the entire field is empty
            if blnValidate is True:
                pass
            else:
                messagebox.showwarning(title='ERROR', message='%s field should not be empty. Please verify your selection.'%(strFieldDesc))
                blnValidate = False
                # Select the first checkbox
                lstCheckBox[0].set('1')

        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate  

    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)  
        strVisField = str("Visual Result")
        strPhysField = str("Physical Result")

        # Check the user input
        blnValidate = RopeInspection.Check_Input(self.dropRopeVisStatus.get())         
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check the user input
            blnValidate = RopeInspection.Check_Input(self.dropRopePhysStatus.get())         
            
            # Check if the input is valid
            if (blnValidate is True):
                # Check the user input
                blnValidate = RopeInspection.Check_Checkbox_Input(self.visCheckList, strVisField)                                                                                                   
                
                # Check if the input is valid
                if (blnValidate is True):
                    # Check the user input
                    blnValidate = RopeInspection.Check_Checkbox_Input(self.physCheckList, strPhysField)                                                                                                   
                    
                    # Check if the input is valid
                    if (blnValidate is True):
                        blnValidate = True
                    else:
                        # Return blnValidate as False
                        blnValidate = False                                                                  
                else:
                    # Return blnValidate as False
                    blnValidate = False
            else:
                # Return blnValidate as False
                blnValidate = False
                self.dropRopePhysStatus.focus()
        else:
            # Return blnValidate as False
            blnValidate = False
            self.dropRopeVisStatus.focus()                                                

        return blnValidate 

    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        """       
        # Declare Local Variables
        sqlRopeVisSel = ("TRopeVisTextSelects", "intRopeVisTextSelectID", "strRopeVisTextSelect")
        sqlRopePhysSel = ("TRopePhysTextSelects", "intRopePhysTextSelectID", "strRopePhysTextSelect")
        sqlRopeVisIns = ("TRopeVisualInspections", "intRopeVisualInspectionID")
        sqlRopePhysIns = ("TRopePhysicalInspections", "intRopePhysicalInspectionID") 
        sqlRopeStandIns = ("TStandardRopeInspections", "intStandardRopeInspectionID")

        # Check if the comment is empty. If not, pass in the values. If empty, pass in 'None'
        if self.commInput.get("1.0", "end-1c") != "":
            self.strComment = str(self.commInput.get("1.0", "end-1c"))
            self.strComment += "; "
            # Add the comment to the AutoBelay Comment object
            RopeInspect.strComment = ''.join(self.strComment)
        else:
            self.strComment = 'None'
            RopeInspect.strComment = self.strComment
        
        # Get the selected values
        RopeVisMetSelect = self.Get_Combined_Selection(RopeVisSelection.astrRopeVisTextSelect, self.selectItems[0])
        RopePhysMetSelect = self.Get_Combined_Selection(RopePhysSelection.astrRopePhysTextSelect, self.selectItems[0])

        # # Display the string representation
        # print(RopeVisMetSelect) 
        # print(RopePhysMetSelect)
        
        # Get the status for the visual, physical selection
        RopeVisStatus = self.dropRopeVisStatus.get()
        RopePhysStatus = self.dropRopePhysStatus.get()
        
        # Get the ID of the selected status item
        RopeVisStatusID = InspectionStatus.astrInspectionStatusDesc.index(RopeVisStatus) + 1
        RopePhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(RopePhysStatus) + 1
        
        # Get the type of selection, either physical, visual 
        VisInsTypeDesc = InspectionType.astrInspectionTypeDesc[0]
        PhysInsTypeDesc = InspectionType.astrInspectionTypeDesc[1]

        # Get the ID of the selected Type item
        VisInsTypeID = InspectionType.astrInspectionTypeDesc.index(VisInsTypeDesc) + 1
        PhysInsTypeID = InspectionType.astrInspectionTypeDesc.index(PhysInsTypeDesc) + 1

        # Get the list of items selected and attach them to the selection object for Visual and Physical Selection
        RopeVisMetalSelectID = self.Get_Or_Create_ID(RopeVisMetSelect, sqlRopeVisSel)              
        RopePhysMetalSelectID = self.Get_Or_Create_ID(RopeVisMetSelect, sqlRopePhysSel)
                            
        # Get the ID's for the base objects in each class
        RopeVisualInsID = self.Get_Max_Primary_Key(sqlRopeVisIns[0], sqlRopeVisIns[1])
        RopePhysicalInsID = self.Get_Max_Primary_Key(sqlRopePhysIns[0], sqlRopePhysIns[1])        
        StandardRopeInspectionID = self.Get_Max_Primary_Key(sqlRopeStandIns[0], sqlRopeStandIns[1])

        # Assign the local object to the class objects
        rvs = RopeVisSelection(RopeVisMetalSelectID, RopeVisMetSelect, RopeVisStatus)
        rps = RopePhysSelection(RopePhysMetalSelectID, RopePhysMetSelect, RopePhysStatus)        

        # Commit the data to the visual inspection
        RopeVisSelection.intRopeVisTextSelectID = rvs.intRopeVisTextSelectID
        RopeVisSelection.strRopeVisTextSelect = rvs.strRopeVisTextSelect
        RopeVisSelection.strRopeVisStatus = rvs.strRopeVisStatus
        RopeVisualInspect.aRopeVisualCache = (RopeVisualInsID, Ropes.intRopeID, VisInsTypeID, rvs.intRopeVisTextSelectID, RopeVisStatusID)

        # Commit the data to the physical inspection
        RopePhysSelection.intRopePhysTextSelectID = rps.intRopePhysTextSelectID
        RopePhysSelection.strRopePhysTextSelect = rps.strRopePhysTextSelect
        RopePhysSelection.strRopePhysStatus = rps.strRopePhysStatus
        RopePhysicalInspect.aRopePhysicalCache = (RopePhysicalInsID, Ropes.intRopeID, PhysInsTypeID, rps.intRopePhysTextSelectID, RopePhysStatusID)    

        # Commit the data to the standard inspection
        StandardRopeInspect.aStandardRopeInsCache = (StandardRopeInspectionID, RopeVisualInsID, RopePhysicalInsID)

    def Get_Combined_Selection(self, persisted_array, default_value):
        """
        Function Name: Get_Combined_Selection
        Function Purpose: This function combines the array elements into a comma-separated string,
        and Ropes the case when the persisted array is empty by setting a default value.
        """
        if len(persisted_array) == 0:
            return default_value
        else:
            return ",".join(persisted_array)
        
    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
    
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlStatement[0], sqlStatement[1]))    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
                    
    def Next(self):
        """ 
        Function Name: Next
        Function Purpose: This function is executed once the user clicks on the "Next" button. Once the inputs 
        are validated, the inspection results loads the user selected data and is retained at the object class locations 
        before committing to the database. If all inputs are valid and confirmed by the user, the next stage of inspections is executed.
        """
        global blnValidate
        blnValidate = bool(False)             
        
        # First check if the input is empty, if so, notify the user the input needs attention 
        blnValidate = self.Validate_InputFields()
        
        # If status is true then proceed to update the result field, else, reset the fields
        if blnValidate is True:
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to next inspection component?') is True:
                # print(RopeVisSelection.astrRopeVisTextSelect)
                # print(RopePhysSelection.astrRopePhysTextSelect) 
                # Load the user data and prep the data for db dump
                self.Pull_UserInput()     

                # Set the global class bool to true
                Bool_Flag.Set_Rope_Bool_Value_True(Bool_Flag)
                
                # Go to the next inspection component
                self.Next_Inspection()
            else:
                # Check if the user would like to reset the fields
                if messagebox.askyesno(message='ATTENTION! \n\n Would you like to reset the fields?') is True:
                    # Clear the input fields and after data is submitted to the database
                    self.Reset(self)                

    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This function is executed once the user clicks on the reset button inside the root
        frame. If the user clicks 'Reset', all data is set back to default.
        """     
        # Set the list objects first element to the drop click object
        self.dropRopeType.set("")
        self.dropRopeVisStatus.set("")
        self.dropRopePhysStatus.set("")
        
        # Reset the checkboxes to empty selections
        self.visCheckBox = BaseFunctions.Deselect_All_Checkbox(self.visCheckList)
        self.physCheckBox = BaseFunctions.Deselect_All_Checkbox(self.physCheckList)
        self.functCheckBox = BaseFunctions.Deselect_All_Checkbox(self.functCheckList)

        # Set the first item in the list to the first checkbox item displayed
        self.visCheckList[0].set('1')
        self.physCheckList[0].set('1')
        self.functCheckList[0].set('1')

        # Clear the class objects
        StandardRopeInspect.Reset_Rope_Data(self)
        StandardRopeInspect.Delete_Rope_Data(self)
        
        # Delete the comment field 
        self.commInput.delete("1.0", "end-1c") 

    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Expose the window widget to the user
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """     
        # Open the frame and set the inputs to the class objects
        self.Exit()
        
        # Show the main window after the new window is closed
        if (Bool_Flag.blnComplexWithBelayDeviceFlag is True):
            BelayDeviceInspection()
        elif (Bool_Flag.blnComplexWith_Two_ConnectorFlag is True):
            TwoConnectorInspection()
        elif (Bool_Flag.blnComplexWithConnectorFlag is True):
            ConnectorInspection()
        else:
            # Show the main window after the new window is closed
            GymRopeSelection()        

    def Next_Inspection(self):
        """ 
        Function Name: Next_Inspection
        Function Purpose: This function is executed once the user clicks on Next button to move to the nex inspection
        type window. Withdraw the parent window and load the new window.
        """           
        # Hide the main window
        self.Exit()  

        # Load the next inspection window
        Complex_Rope_InspectionResults()
        
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()


# #######################################################################################################
# # Add New Rope Class
# ####################################################################################################### 

class AddRope(tk.Toplevel, Ropes):
    """
    Class Name: AddRope
    Class Description: This class adds a new rope to the database.
    """
    def __init__(self, parent):
        # Load the data from the database
        # Start_Menu.Load_Obj_Lists(self) # Make sure to comment this out after testing
                
        # Initialize the Toplevel window
        super().__init__(parent)

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (580/2)     
        self.y = (self.heightSize/2) - (370/2)    
                                        
        # Create the Window attributes
        self.title("Add New Rope")
        self.geometry('%dx%d+%d+%d' % (580, 370, self.x, self.y))
        self.resizable(False, False)

        # Create the second frame to hold the input fields
        self.frameInput = tk.LabelFrame(self, text="Rope Credentials")
        self.frameInput.place(x=90, y=10, width=405, height=290)

        # Create the labels 
        self.lblManuName = tk.Label(self.frameInput, text="Manufacture Name:")
        self.lblSerialNum = tk.Label(self.frameInput, text="Serial Number:")
        self.lblBumperNum = tk.Label(self.frameInput, text="Bumper Number:")
        self.lblRopeLength = tk.Label(self.frameInput, text="Rope Length:")
        self.lblDiameter = tk.Label(self.frameInput, text="Diameter:")
        self.lblElasticity = tk.Label(self.frameInput, text="Elasticity:")        
        self.lblManuDate = tk.Label(self.frameInput, text="Manufacture Date:")
        self.lblInstallDate = tk.Label(self.frameInput, text="Install Date:")
        self.lblRopeInUse = tk.Label(self.frameInput, text="Rope In Use:")

        # Create the label locations
        self.lblManuName.grid(row=0, column=0, sticky='W', padx=5)
        self.lblSerialNum.grid(row=1, column=0, sticky='W', padx=5)
        self.lblBumperNum.grid(row=2, column=0, sticky='W', padx=5)
        self.lblRopeLength.grid(row=3, column=0, sticky='W', padx=5)
        self.lblDiameter.grid(row=4, column=0, sticky='W', padx=5)
        self.lblElasticity.grid(row=5, column=0, sticky='W', padx=5)
        self.lblManuDate.grid(row=6, column=0, sticky='W', padx=5)
        self.lblInstallDate.grid(row=7, column=0, sticky='W', padx=5)
        self.lblRopeInUse.grid(row=8, column=0, sticky='W', padx=5)

        # Create the entry input box
        self.ManuNameInput = Entry(self.frameInput, width=40)
        self.SerialNumInput = Entry(self.frameInput, width=40)
        self.BumperNumInput = Entry(self.frameInput, width=40)
        self.RopeLengthInput = Entry(self.frameInput, width=40)
        self.DiameterInput = Entry(self.frameInput, width=40)

        # Create the drop down menu list objects
        self.dropElasticity = ttk.Combobox(self.frameInput, values=['Static', 'Semi-Static', 'Dynamic'], state='readonly')
        # Create the entry input box
        self.ManuDateInput = Entry(self.frameInput, width=40)
        self.InstallDateInput = Entry(self.frameInput, width=40)
        
        # Create the drop down menu list objects
        self.dropInUse = ttk.Combobox(self.frameInput, values=['Yes', 'No'], state='readonly')

        # Create the drop down menu size for each attribute
        self.dropElasticity.configure(width=37)
        self.dropInUse.configure(width=37)
        
        # Create the grid for the drop down menu
        self.dropElasticity.grid(row=5, column=1, padx=5, pady=5)
        self.dropInUse.grid(row=8, column=1, padx=5, pady=5)

        # Create a list of all the entry objects
        aEntryList = (self.RopeLengthInput, self.DiameterInput, self.ManuDateInput, self.InstallDateInput, self.BumperNumInput) 
        astrPlaceHolder = ("Meters", "Millimeters", "MM/DD/YYYY", "MM/DD/YYYY", "Optional")

        # Insert the placeholders at the desired entry points
        for i, entry in enumerate(aEntryList):
            entry.insert(0, astrPlaceHolder[i])
            entry.config(fg='grey')
            entry.bind('<FocusIn>', lambda event, entry=entry, placeholder=astrPlaceHolder[i]: self.On_Entry_Click(event, entry, placeholder))
            entry.bind('<FocusOut>', lambda event, entry=entry, placeholder=astrPlaceHolder[i]: self.On_FocusOut(event, entry, placeholder))
            
        # Create the grid for all of the entry input fields
        self.ManuNameInput.grid(row=0, column=1, padx=25, pady=5)
        self.SerialNumInput.grid(row=1, column=1, pady=5)
        self.BumperNumInput.grid(row=2, column=1, pady=5)
        self.RopeLengthInput.grid(row=3, column=1, pady=5)
        self.DiameterInput.grid(row=4, column=1, pady=5)
        self.ManuDateInput.grid(row=6, column=1, pady=5)
        self.InstallDateInput.grid(row=7, column=1, pady=5)

        # Create the buttons
        self.btnExit = Button(self, text="Back", width=10, command=lambda:AddRope.Exit(self))
        self.btnReset = Button(self, text="Reset", width=10, command=lambda:AddRope.Reset(self))
        self.btnSubmit = Button(self, text="Submit", width=10, command=lambda:AddRope.Submit(self))

        # Create the button grid
        self.btnExit.place(x=120, y=320)
        self.btnReset.place(x=250, y=320)
        self.btnSubmit.place(x=380, y=320)

    def On_Entry_Click(self, event, entry, strPlaceHolder):
        """ 
        Function Name: On_Entry_Click
        Function Purpose: This function gets called whenever entry is clicked by a user to start a new entry.
        """    
        if entry.get() == strPlaceHolder:
            entry.delete(0, "end") 
            entry.insert(0, '') 
            entry.config(fg='black')
            
    def On_FocusOut(self, event, entry, strPlaceHolder):
        """ 
        Function Name: On_FocusOut
        Function Purpose: This function gets called whenever the entry loses focus.
        """            
        if entry.get() == '':
            entry.insert(0, strPlaceHolder)
            entry.config(fg='grey') 
                                            
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate
        
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        def set_invalid(input_field, msg):
            """
            Highlights the input field to indicate invalid data and sets focus.
            """
            input_field.delete(0, tk.END)
            input_field.configure(background='Yellow')
            input_field.focus()
            messagebox.showwarning("Input Error", msg)

        # Validate Manufacturer Name
        if not (AddRope.Check_Input(self.ManuNameInput.get()) and
                BaseFunctions.Validate_String_Input(self.ManuNameInput.get())):
            set_invalid(self.ManuNameInput, "Invalid manufacturer name. Please try again.")
            return False

        # Validate Serial Number
        serial_num = self.SerialNumInput.get()
        if not (AddRope.Check_Input(serial_num) and BaseFunctions.Validate_Serial_Input(serial_num)):
            set_invalid(self.SerialNumInput, "Invalid serial number. Please try again.")
            return False
        elif serial_num in Ropes.astrSerialNumCache:
            set_invalid(self.SerialNumInput, "Duplicate serial number detected. Please try again.")
            return False
        
        # Get the Primary Key ID
        sqlPrimKey = ("TRopes", "intRopeID")   
        self.RopeIDResult = self.Get_Or_Create_ID(self.SerialNumInput.get(), sqlPrimKey)
        
        # Validate Bumper Number if it exists
        bumper_num = self.BumperNumInput.get()
        if bumper_num != "" and not BaseFunctions.Validate_Serial_Input(bumper_num):
            set_invalid(self.BumperNumInput, "Invalid bumper number. Please try again.")
            return False
        elif bumper_num in Ropes.astrBumperNumCache:
            set_invalid(self.BumperNumInput, "Duplicate bumper number detected. Please try again.")
            return False

        self.BumperNumInput.delete(0, tk.END)
        new_bumper_num_value = bumper_num if bumper_num != "" else 'Optional'
        self.BumperNumInput.insert(0, new_bumper_num_value)

        # Validate Rope Length
        rope_length = self.RopeLengthInput.get()
        rope_length_result = rope_length[:-1] if rope_length.endswith('m') else rope_length
        if not BaseFunctions.Validate_StringNumeric_Input(rope_length_result):
            set_invalid(self.RopeLengthInput, "Invalid rope length. Please try again.")
            return False

        self.RopeLengthResult = rope_length_result + 'm'

        # Validate Diameter
        diameter = self.DiameterInput.get()
        diameter_result = diameter[:-2] if diameter.endswith('mm') else diameter
        if not BaseFunctions.Validate_StringFloat_Input(diameter_result):
            set_invalid(self.DiameterInput, "Invalid diameter. Please try again.")
            return False

        self.DiameterResult = diameter_result + 'mm'

        # Validate Elasticity Selection
        if not AddRope.Check_Input(self.dropElasticity.get()):
            set_invalid(self.dropElasticity, "Invalid elasticity. Please try again.")
            return False
                                
        # Validate Manufacturing Date
        if not AddRope.Check_Input(self.ManuDateInput.get()):
            set_invalid(self.ManuDateInput, "Invalid manufacturing date. Please try again.")
            return False

        result_tup = BaseFunctions.Validate_Date_Input(self.ManuDateInput.get())
        if not result_tup[0]:
            set_invalid(self.ManuDateInput, "Invalid manufacturing date. Please try again.")
            return False

        self.ManuDateResult = AddRope.Change_Date_To_Format(self.ManuDateInput, result_tup)

        # Validate Installation Date
        if not AddRope.Check_Input(self.InstallDateInput.get()):
            set_invalid(self.InstallDateInput, "Invalid installation date. Please try again.")
            return False

        result_tup = BaseFunctions.Validate_Date_Input(self.InstallDateInput.get())
        if not result_tup[0]:
            set_invalid(self.InstallDateInput, "Invalid installation date. Please try again.")
            return False

        self.InstallDateResult = AddRope.Change_Date_To_Format(self.InstallDateInput, result_tup)

        # Validate 'In Use' Selection
        if not UpdateRopeInfo.Check_Input(self.dropInUse.get()):
            set_invalid(self.dropInUse, "Invalid 'In Use' selection. Please try again.")
            return False
                
        return True

    def Change_Date_To_Format(dtmObject, aResultTup):
        """ 
        Function Name: Change_Date_To_Format
        Function Purpose: This function is executed every call of the validation check to ensure the dates are all
        changed to the same format no matter if the character is valid.
        """ 
        dtmObject.delete(0, END)
        dtmObject.insert(0, aResultTup[1])
        dtmObject = aResultTup[1]

        return dtmObject

    def Get_UserInput(self):
        """ 
        Function Name: Get_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        Then the data will be sent to the db.
        """       
        # Get the current date for last and next inspection
        aDateResult = BaseFunctions.Update_Inspection_Date()
        lastDate = datetime.strftime(aDateResult[0], '%m/%d/%Y')
        nextDate =  datetime.strftime(aDateResult[1], '%m/%d/%Y')
        
        # Assign value to the objects
        RopeID = self.RopeIDResult
        SerialNum = self.SerialNumInput.get()
        BumperNum = self.BumperNumInput.get()
        RopeLength = self.RopeLengthResult
        RopeDiameter = self.DiameterResult
        RopeElasticity = self.dropElasticity.get()
        ManufactureDate = self.ManuDateResult
        InstallationDate = self.InstallDateResult
        LastInspectionDate = lastDate
        NextInspectionDate = nextDate
        RopeInUse = self.dropInUse.get()

        # If BumperNum = "Optional" place a 'None' string
        if BumperNum == "Optional":
            BumperNum = "None"
            
        # Capitalize the first letter of each word and append a space after splitting the user input into a list
        resultList = self.ManuNameInput.get().split()
        self.Cap_ManuName = [result.capitalize() for result in resultList]
        ManuName = ' '.join(self.Cap_ManuName)                
        
        # Assign the local objects to the class objects
        self.intRopeID = RopeID
        self.strSerialNum = SerialNum
        self.strBumperNum = BumperNum
        self.strRopeLength = RopeLength
        self.strDiameter = RopeDiameter
        self.strElasticity = RopeElasticity
        self.strManufactureName = ManuName
        self.dtmManufactureDate = ManufactureDate
        self.dtmInstallationDate = InstallationDate
        self.dtmLastInspectionDate = LastInspectionDate
        self.dtmNextInspectionDate = NextInspectionDate
        self.strEquipInUse = RopeInUse

    def Get_Combined_Selection(self, persisted_array, default_value):
        """
        Function Name: Get_Combined_Selection
        Function Purpose: This function combines the array elements into a comma-separated string,
        and handles the case when the persisted array is empty by setting a default value.
        """
        if len(persisted_array) == 0:
            return default_value
        else:
            return ",".join(persisted_array)
        
    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
                        
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlStatement[0], sqlStatement[1]))    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
    
    def Clear_BG_Color(self):
        """ 
        Function Name: Clear_BG_Color
        Function Purpose: This button executes when the user submits their entries and clears the background
        color before any validation checks.
        """
        # Delete the button after submission
        self.ManuNameInput.configure(background='White')
        self.SerialNumInput.configure(background='White')
        self.BumperNumInput.configure(background='White')
        self.RopeLengthInput.configure(background='White')
        self.DiameterInput.configure(background='White')
        self.ManuDateInput.configure(background='White')
        self.InstallDateInput.configure(background='White')
        
    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This button executes when the user wants to reset the values.
        """
        # Delete the button after submission
        self.ManuNameInput.delete(0, END)
        self.SerialNumInput.delete(0, END)
        self.BumperNumInput.delete(0, END)
        self.RopeLengthInput.delete(0, END)
        self.DiameterInput.delete(0, END)
        self.ManuDateInput.delete(0, END)
        self.InstallDateInput.delete(0, END)
        
        # Reset the drop menus
        self.dropElasticity.set("")
        self.dropInUse.set("")
        
        # Clear out the background colors and set to default as 'white'
        AddRope.Clear_BG_Color(self)
        
        # Create a list of all the entry objects
        aEntryList = (self.RopeLengthInput, self.DiameterInput, self.ManuDateInput, self.InstallDateInput, self.BumperNumInput) 
        astrPlaceHolder = ("Meters", "Millimeters", "MM/DD/YYYY", "MM/DD/YYYY", "Optional")

        # Insert the placeholders at the desired entry points
        for i, entry in enumerate(aEntryList):
            entry.insert(0, astrPlaceHolder[i])
            entry.config(fg='grey')
            entry.bind('<FocusIn>', lambda event, entry=entry, placeholder=astrPlaceHolder[i]: self.On_Entry_Click(event, entry, placeholder))
            entry.bind('<FocusOut>', lambda event, entry=entry, placeholder=astrPlaceHolder[i]: self.On_FocusOut(event, entry, placeholder))
            
    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the new Rope Rope to the db. Else, reset
        """
        # Check if all of the inputs are valid
        global blnValidate 
        blnValidate = bool(False)
        
        # Clear out the background colors and set to default as 'white'
        AddRope.Clear_BG_Color(self)
        
        # Get the blnValidate status
        blnValidate = AddRope.Validate_InputFields(self)
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to add new Rope?') is True:     
                # Load the user data and prep the data for db dump
                AddRope.Get_UserInput(self)
                Ropes.Add_Ropes_Query(self)                     

                # Check if the user would like to add another Rope
                if messagebox.askyesno(message='SUCCESSFUL UPLOAD! \n\n Would you like to add another Rope?') is True:
                    # Clear the input fields and after data is submitted to the database
                    AddRope.Reset(self)
                else:
                    AddRope.Exit(self)
            
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        

#######################################################################################################
# Update Ropes Info
#######################################################################################################

class UpdateRopeInfo(tk.Toplevel, Ropes):
    """
    Class Name: UpdateRopeInfo
    Class Description: This class updates any Rope to the database.
    """
    def __init__(self, parent):
        # Load the data from the database
        # Start_Menu.Load_Obj_Lists(self) # Make sure to comment this out after testing
        
        # Initialize the Toplevel window
        super().__init__(parent)

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (560/2)     
        self.y = (self.heightSize/2) - (481/2)  
                                        
        # Create the Window attributes
        self.WindowTitle = self.title("Update Rope Information")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (560, 481, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Load the query selection widget
        self.Selection_Widget()
                
        # Create the second frame to hold the input fields
        self.frameInput = LabelFrame(self, text="Rope Credentials")
        self.frameInput.place(x=75, y=170, width=405, height=260)

        # Create the labels 
        self.lblSerialNum = tk.Label(self.frameInput, text="Serial Number:")
        self.lblBumperNum = tk.Label(self.frameInput, text="Bumper Number:")
        self.lblRopeLength = tk.Label(self.frameInput, text="Rope Length:")
        self.lblDiameter = tk.Label(self.frameInput, text="Diameter:")
        self.lblElasticity = tk.Label(self.frameInput, text="Elasticity:")        
        self.lblManuDate = tk.Label(self.frameInput, text="Manufacture Date:")
        self.lblInstallDate = tk.Label(self.frameInput, text="Install Date:")
        self.lblRopeInUse = tk.Label(self.frameInput, text="Rope In Use:")

        # Create the label locations
        self.lblSerialNum.grid(row=1, column=0, sticky='W', padx=5)
        self.lblBumperNum.grid(row=2, column=0, sticky='W', padx=5)
        self.lblRopeLength.grid(row=3, column=0, sticky='W', padx=5)
        self.lblDiameter.grid(row=4, column=0, sticky='W', padx=5)
        self.lblElasticity.grid(row=5, column=0, sticky='W', padx=5)
        self.lblManuDate.grid(row=6, column=0, sticky='W', padx=5)
        self.lblInstallDate.grid(row=7, column=0, sticky='W', padx=5)
        self.lblRopeInUse.grid(row=8, column=0, sticky='W', padx=5)
        
        # Create the entry input box
        self.SerialNumInput = Entry(self.frameInput, width=39, state='disabled')
        self.BumperNumInput = Entry(self.frameInput, width=39, state='disabled')
        self.RopeLengthInput = Entry(self.frameInput, width=39, state='disabled')
        self.DiameterInput = Entry(self.frameInput, width=39, state='disabled')
        # Create the combo box
        self.dropElasticity = ttk.Combobox(self.frameInput, values=['Static', 'Semi-Static', 'Dynamic'], state='disabled')
        # Create the entry input box
        self.ManuDateInput = Entry(self.frameInput, width=39, state='disabled')
        self.InstallDateInput = Entry(self.frameInput, width=39, state='disabled')
        
        # Create the combo box
        self.aInUseSelectionList = ('Yes', 'No', 'Retired')
        self.dropInUseSelection = ttk.Combobox(self.frameInput, values=self.aInUseSelectionList, state='disabled')
        self.dropElasticity.configure(width=36,)
        self.dropInUseSelection.configure(width=36,)

        # Create the grid for all of the entry input fields
        self.SerialNumInput.grid(row=1, column=1, padx=25, pady=5)
        self.BumperNumInput.grid(row=2, column=1, pady=5)
        self.RopeLengthInput.grid(row=3, column=1, pady=5)
        self.DiameterInput.grid(row=4, column=1, pady=5)
        self.dropElasticity.grid(row=5, column=1, pady=5)
        self.ManuDateInput.grid(row=6, column=1, pady=5)
        self.InstallDateInput.grid(row=7, column=1, pady=5)
        self.dropInUseSelection.grid(row=8, column=1, pady=5)

        # Create the buttons
        self.btnExit = Button(self, text="Back", width=10, command=lambda:UpdateRopeInfo.Exit(self))
        self.btnReset = Button(self, text="Reset", width=10, command=lambda:UpdateRopeInfo.Reset(self))
        self.btnSubmit = Button(self, text="Submit", width=10, command=lambda:UpdateRopeInfo.Submit(self))

        # Create the button grid
        self.btnExit.place(x=105, y=440)
        self.btnReset.place(x=235, y=440)
        self.btnSubmit.place(x=365, y=440)

    def Selection_Widget(self):
        """ 
        Function Name: Selection_Widget
        Function Purpose: This function populates the search by widget for Serial or Bumper Num search.
        """           
        # Create the first frame to hold the input fields
        self.selectInput = LabelFrame(self, text="Select Rope")
        self.selectInput.place(x=75, y=35, width=405, height=130)

        # Create the labels 
        self.lblSearchByRopeID = Label(self.selectInput, text="Query by Rope ID:")
        self.lblRopeSelection = Label(self.selectInput, text="Rope ID Selection:")

        # Create the label locations
        self.lblSearchByRopeID.place(x=10, y=5)
        self.lblRopeSelection.place(x=10, y=35)

        # Create variables to hold the value of the selected radio button
        self.objRadioValue = tk.StringVar(value='serial')
        self.objComboValue = tk.StringVar()

        # List objects of serial and bumper values
        self.astrSerialNumList = self.astrSerialNumCache
        self.astrBumperNumList = self.astrBumperNumCache

        # Create the radio buttons
        self.rbSerial = tk.Radiobutton(self.selectInput, text="Serial Number", variable=self.objRadioValue, value="serial", command=self.Populate_Dropdown)
        self.rbBumper = tk.Radiobutton(self.selectInput, text="Bumper Number", variable=self.objRadioValue, value="bumper", command=self.Populate_Dropdown)

        # Place the radio buttons next to each other using .place()
        self.rbSerial.place(x=135, y=5)
        self.rbBumper.place(x=265, y=5)
                    
        # Create the combo box
        self.dropRopeSelection = ttk.Combobox(self.selectInput, values=self.astrSerialNumList, state='readonly')
        self.dropRopeSelection.configure(width=36,)

        # Populate the dropdown based on the default radio button selection
        self.Populate_Dropdown()

        # Create the grid for all of the entry input fields
        self.dropRopeSelection.place(x=140, y=35)

        # Create the buttons
        self.btnSelectSubmit = Button(self.selectInput, text="Submit", width=10, command=lambda:UpdateRopeInfo.SubmitSelect(self))

        # Create the button grid
        self.btnSelectSubmit.place(x=165, y=70)  

    def Populate_Dropdown(self):
        """ 
        Function Name: Populate_Dropdown
        Function Purpose: This function populates the dropdown based on the radio button selection.
        """           
        if self.objRadioValue.get() == "serial":
            self.dropRopeSelection["values"] = self.astrSerialNumList
        else:
            self.dropRopeSelection["values"] = self.astrBumperNumList
        self.dropRopeSelection.set("")  # Clear the combobox's current value                                    
        
    def Change_Date_To_Format(dtmObject, aResultTup):
        """ 
        Function Name: Change_Date_To_Format
        Function Purpose: This function is executed every call of the validation check to ensure the dates are all
        changed to the same format no matter if the character is valid.
        """ 
        dtmObject.delete(0, END)
        dtmObject.insert(0, aResultTup[1])
        dtmObject = aResultTup[1]

        return dtmObject

    def Convert_Date_Format(date_str):
        """ 
        Function Name: SubmitSelect
        Function Purpose: This button Convert date from "YYYY-MM-DD" to "MM/DD/YYYY"
        """
        year, month, day = date_str.split('-')
        return f"{month}/{day}/{year}"

    def Disable_After_Submit(self):
        """ 
        Function Name: Disable_After_Submit
        Function Purpose: This function disables certain controls after submission.
        """   
        # Disable the submit button
        self.btnSubmit.configure(state='disabled')
        
        # Reset the value of the dropdown
        self.dropRopeSelection.set("")

    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)
        
    def Check_Serial_Or_Bumper(self):
        """ 
        Function Name: Check_Serial_Or_Bumper
        Function Purpose: This function is executed once the user clicks on the option of query search by serial
        number or bumper number. 
        """        
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Get the primary key ID from the dropdown
        strSelectionID = self.dropRopeSelection.get()
        
        # Determine the primary key for the query
        if strSelectionID in Ropes.astrSerialNumCache:
            primary_key = Ropes.astrSerialNumCache.index(strSelectionID) + 1
            blnFlag = True
        elif strSelectionID in Ropes.astrBumperNumCache:
            primary_key =  Ropes.astrBumperNumCache.index(strSelectionID) + 1
            blnFlag = False
            
        # Return the primary key
        return (blnFlag, primary_key)
                
    def SubmitSelect(self):
        """ 
        Function Name: SubmitSelect
        Function Purpose: This button executes when the user selects the rope.
        """
        # Set the state of the inputs
        for entry in [self.SerialNumInput, self.BumperNumInput, self.RopeLengthInput, self.DiameterInput, self.ManuDateInput, self.InstallDateInput]:
            entry.configure(state='normal')

        # Configure the drop menu for in use
        self.dropElasticity.configure(state='readonly')
        self.dropInUseSelection.configure(state='readonly')

        # Determine the primary key for the query
        resultTup =  self.Check_Serial_Or_Bumper()
        primary_key =  resultTup[1]

        # Execute the query
        aParams = ('TRopes', 'intRopeID', primary_key)
        QueryResult = Queries.Get_All_DB_Values_OnePrimKey(Queries, aParams)
        
        if QueryResult:
            self.SerialNumInput.insert(0, QueryResult[1])
            self.BumperNumInput.insert(0, QueryResult[2])
            self.RopeLengthInput.insert(0, QueryResult[3])
            self.DiameterInput.insert(0, QueryResult[4])
            self.Set_Previous_Drop_List(QueryResult[5], self.dropElasticity)
            self.ManuDateInput.insert(0, UpdateRopeInfo.Convert_Date_Format(QueryResult[7]))
            self.InstallDateInput.insert(0, UpdateRopeInfo.Convert_Date_Format(QueryResult[8]))
            self.Set_Previous_Drop_List(QueryResult[11], self.dropInUseSelection)
        
        # Disable the select submit button
        self.btnSelectSubmit.configure(state='disabled')
        
        # Enable the submit and reset buttons
        self.btnSubmit.configure(state='normal')
        self.btnReset.configure(state='normal')
                
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate
        
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        def set_invalid(input_field):
            """
            Set the input field to show invalid data.
            """
            input_field.delete(0, tk.END)
            input_field.configure(background='Yellow')
            input_field.focus()

        # Validate Serial Number
        if not (UpdateRopeInfo.Check_Input(self.SerialNumInput.get()) and
                BaseFunctions.Validate_Serial_Input(self.SerialNumInput.get())):
            set_invalid(self.SerialNumInput)
            return False

        # Validate Bumper Number
        bumper_num = self.BumperNumInput.get()
        if bumper_num != "" and not BaseFunctions.Validate_Serial_Input(bumper_num):
            set_invalid(self.BumperNumInput)
            return False

        self.BumperNumInput.delete(0, tk.END)
        new_bumper_num_value = bumper_num if bumper_num != "" else 'None'
        self.BumperNumInput.insert(0, new_bumper_num_value)

        # Validate Rope Length
        rope_length = self.RopeLengthInput.get()
        rope_length_result = rope_length[:-1] if rope_length.endswith('m') else rope_length
        if not BaseFunctions.Validate_StringNumeric_Input(rope_length_result):
            set_invalid(self.RopeLengthInput)
            return False

        self.RopeLengthResult = rope_length_result + 'm'

        # Validate Diameter
        diameter = self.DiameterInput.get()
        diameter_result = diameter[:-2] if diameter.endswith('mm') else diameter
        if not BaseFunctions.Validate_StringFloat_Input(diameter_result):
            set_invalid(self.DiameterInput)
            return False

        self.DiameterResult = diameter_result + 'mm'

        # Validate Elasticity
        if not UpdateRopeInfo.Check_Input(self.dropElasticity.get()):
            set_invalid(self.dropElasticity)
            return False
                                
        # Validate Manufacturing Date
        if not UpdateRopeInfo.Check_Input(self.ManuDateInput.get()):
            set_invalid(self.ManuDateInput)
            return False

        result_tup = BaseFunctions.Validate_Date_Input(self.ManuDateInput.get())
        if not result_tup[0]:
            set_invalid(self.ManuDateInput)
            return False

        self.ManuDateInputResult = UpdateRopeInfo.Change_Date_To_Format(self.ManuDateInput, result_tup)

        # Validate Installation Date
        if not UpdateRopeInfo.Check_Input(self.InstallDateInput.get()):
            set_invalid(self.InstallDateInput)
            return False

        result_tup = BaseFunctions.Validate_Date_Input(self.InstallDateInput.get())
        if not result_tup[0]:
            set_invalid(self.InstallDateInput)
            return False

        self.InstallDateResult = UpdateRopeInfo.Change_Date_To_Format(self.InstallDateInput, result_tup)

        # Validate 'In Use' Selection
        if not UpdateRopeInfo.Check_Input(self.dropInUseSelection.get()):
            set_invalid(self.dropInUseSelection)
            return False

        return True

    def Get_UserInput(self):
        """ 
        Function Name: Get_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        Then the data will be sent to the db.
        """                
        # Assign value to the objects
        SerialNum = self.SerialNumInput.get()
        BumperNum = self.BumperNumInput.get()
        ManuDate = datetime.strptime(self.ManuDateInputResult, '%m/%d/%Y').date()
        InstallationDate = datetime.strptime(self.InstallDateResult, '%m/%d/%Y').date()
        ropeLength = self.RopeLengthResult
        ropeDiameter = self.DiameterResult
        ropeElasticity = self.dropElasticity.get()
        ManuDate = str(ManuDate)
        InstallationDate = str(InstallationDate)
        RopeInUse = self.dropInUseSelection.get()
        
        # First check if the serial or bumper number was selected 
        resultTup =  self.Check_Serial_Or_Bumper()
        intPrimKey = resultTup[1] - 1

        # Commit the data to load the Ropes class objects with the data from the db
        Ropes.strSerialNum = Ropes.astrSerialNumCache[intPrimKey]
        Ropes.Set_Ropes_Data(Ropes)
            
        # Finish by updating the Ropes class objects before the database dump
        r = Ropes(self.intRopeID, SerialNum, BumperNum, ropeLength, ropeDiameter, ropeElasticity, 
                    self.strManufactureName, ManuDate, InstallationDate, self.dtmLastInspectionDate, 
                    self.dtmNextInspectionDate, RopeInUse)
        
        Ropes.intRopeID = r.intRopeID
        Ropes.strSerialNum = r.strSerialNum
        Ropes.strBumperNum = r.strBumperNum
        Ropes.strRopeLength = r.strRopeLength
        Ropes.strDiameter = r.strDiameter
        Ropes.strElasticity = r.strElasticity
        Ropes.strManufactureName = r.strManufactureName
        Ropes.dtmManufactureDate = r.dtmManufactureDate
        Ropes.dtmInstallationDate = r.dtmInstallationDate
        Ropes.dtmLastInspectionDate = r.dtmLastInspectionDate
        Ropes.dtmNextInspectionDate = r.dtmNextInspectionDate
        Ropes.strEquipInUse = r.strEquipInUse
        
    def Clear_BG_Color(self):
        """ 
        Function Name: Clear_BG_Color
        Function Purpose: This button executes when the user submits their entries and clears the background
        color before any validation checks.
        """
        # Delete the button after submission
        self.SerialNumInput.configure(background='White')
        self.BumperNumInput.configure(background='White')
        self.RopeLengthInput.configure(background='White')
        self.DiameterInput.configure(background='White')
        self.ManuDateInput.configure(background='White')
        self.InstallDateInput.configure(background='White')
        
    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This button executes when the user wants to reset the values.
        """
        # Delete the entries
        self.dropRopeSelection.set("")
        self.dropElasticity.set("")
        self.SerialNumInput.delete(0, END)
        self.BumperNumInput.delete(0, END)
        self.RopeLengthInput.delete(0, END)
        self.DiameterInput.delete(0, END)
        self.ManuDateInput.delete(0, END)
        self.InstallDateInput.delete(0, END)
        self.dropInUseSelection.set("")
        
        # Re-configure input entries to be disabled
        self.dropElasticity.configure(state='disabled')
        self.SerialNumInput.configure(state='disabled')
        self.BumperNumInput.configure(state='disabled')
        self.RopeLengthInput.configure(state='disabled')
        self.DiameterInput.configure(state='disabled')
        self.ManuDateInput.configure(state='disabled')
        self.InstallDateInput.configure(state='disabled')       
        self.dropInUseSelection.configure(state='disabled') 

        # Disable/enable the select, submit, and reset submit button
        self.btnSelectSubmit.configure(state='normal')
        self.btnReset.configure(state='disabled')
        self.btnSubmit.configure(state='disabled') 

        # Reset the radio button to its default value
        self.objRadioValue.set("serial")
        
        # Populate the dropdown based on default radio button selection
        self.Populate_Dropdown()

        # Re-Populate the dropdown menus 
        self.dropRopeSelection["values"] = self.astrSerialNumList
        self.dropInUseSelection["values"] = self.aInUseSelectionList
        
        # Clear out the background colors and set to default as 'white'
        UpdateRopeInfo.Clear_BG_Color(self)

        # Call the function to disable controls after submission
        self.Disable_After_Submit()
        
    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the updated Ropes Rope information to the db. 
        Else, reset
        """
        # Check if all of the inputs are valid
        global blnValidate 
        blnValidate = bool(False)
        
        # Clear out the background colors and set to default as 'white'
        UpdateRopeInfo.Clear_BG_Color(self)
        
        # Get the blnValidate status
        blnValidate = UpdateRopeInfo.Validate_InputFields(self)
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to update the Rope information?') is True:     
                # Load the user data and prep the data for db dump
                UpdateRopeInfo.Get_UserInput(self)             
                Ropes.Update_NewRopes_Query(self)
                
                # Check if the user would like to update another Rope
                if messagebox.askyesno(message='SUCCESSFUL UPDATE! \n\n Would you like to update another Rope?') is True:
                    # Clear the input fields and after data is submitted to the database
                    UpdateRopeInfo.Reset(self)
                else:
                    UpdateRopeInfo.Exit(self)

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()


#######################################################################################################
# Complex Rope Inspection Results Class
#######################################################################################################   

class Complex_Rope_InspectionResults(tk.Tk):
    """
    Class Name: Complex_Rope_InspectionResults
    Class Description: This class is to display the selected inspection components to the user before the 
    data is dumped to the db. User must complete all previous inspection selection modules in order to submit
    data to the database for a standard inspection.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new unit inspection. Display a message
        to the user regarding the protocol for each inspection. User must click 'Check' Button in order to submit
        the data to the db.
        """
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (610/2)     
        self.y = (self.heightSize/2) - (280/2)    
                        
        # Create the Window attributes                
        self.title("Inspection Results")
        self.geometry('%dx%d+%d+%d' % (610, 280, self.x, self.y))
        self.resizable(False, False)

        # Create the scrollbar frame
        self.scrollFrame = LabelFrame(self, text='Results')
        self.scrollFrame.place(x=5, width=600, height=230)
        self.resultCanvas = Canvas(self.scrollFrame)
        self.resultCanvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.resultScrollBar = Scrollbar(self.scrollFrame, orient=VERTICAL, command=self.resultCanvas.yview)
        self.resultScrollBar.pack(side=RIGHT, fill=Y)
        self.resultCanvas.configure(yscrollcommand=self.resultScrollBar.set)
        self.resultCanvas.bind('<Configure>', lambda event: self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all")))

        # Create the third frame to hold the result fields
        self.resultFrame = Frame(self.resultCanvas)
        self.resultCanvas.create_window((0,0), window=self.resultFrame, anchor='nw')
        
        # Bind mousewheel scrolling
        self.resultCanvas.bind_all("<MouseWheel>", self.on_vertical_scroll)

        # Set the last and next inspection date based off of the current date
        aDateResult = BaseFunctions.Update_Inspection_Date()
        self.LastInspectionDate = datetime.strftime(aDateResult[0], '%Y-%m-%d')
        self.NextInspectionDate = datetime.strftime(aDateResult[1], '%Y-%m-%d')

        # Determine which display to show based off of the inspection components selected
        if (Bool_Flag.blnComplexWith_Two_ConnectorFlag is True) and (Bool_Flag.blnComplexWithBelayDeviceFlag is True):
            # Create the labels for the drop down menu lists
            self.Two_ConnectorComposable()
            self.BelayDeviceComposable()
            self.RopeComposable()
                    
            # Set the values in the entry fields
            self.Two_ConnectorEntryComposable()
            self.BelayDeviceEntryComposable()
            self.RopeEntryComposable()
        elif (Bool_Flag.blnComplexWith_Two_ConnectorFlag is True):
            # Create the labels for the drop down menu lists
            self.Two_ConnectorComposable()
            self.RopeComposable()
                    
            # Set the values in the entry fields
            self.Two_ConnectorEntryComposable()
            self.RopeEntryComposable()                
        elif (Bool_Flag.blnComplexWithBelayDeviceFlag is True) and (Bool_Flag.blnComplexWithConnectorFlag is True):
            # Create the labels for the drop down menu lists
            self.ConnectorComposable()
            self.BelayDeviceComposable()
            self.RopeComposable()
                    
            # Set the values in the entry fields
            self.ConnectorEntryComposable()
            self.BelayDeviceEntryComposable()
            self.RopeEntryComposable()                 
        elif (Bool_Flag.blnComplexWithConnectorFlag is True):
            # Create the labels for the drop down menu lists
            self.ConnectorComposable()
            self.RopeComposable()
                    
            # Set the values in the entry fields
            self.ConnectorEntryComposable()
            self.RopeEntryComposable() 
        elif (Bool_Flag.blnComplexWithBelayDeviceFlag is True):
            # Create the labels for the drop down menu lists
            self.BelayDeviceComposable()
            self.RopeComposable()
                    
            # Set the values in the entry fields
            self.BelayDeviceEntryComposable()
            self.RopeEntryComposable()     
        else:
            self.RopeComposable()
            self.RopeEntryComposable()  

        # Create the buttons
        self.btnExit = Button(self, text="Exit", width=10, command=self.Exit)
        self.btnSubmit = Button(self, text="Submit", width=10, command=self.Submit)
        self.btnBack = Button(self, text="Back", width=10, command=self.Back)
            
        # Create the position of the button
        self.btnBack.place(x=140, y=240)
        self.btnSubmit.place(x=270, y=240)
        self.btnExit.place(x=400, y=240)

        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()    

        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the stored data in the class attributes
        StandardConnectorInspect.Delete_Connector_Data(self)
        StandardBelayDeviceInspect.Delete_BelayDevice_Data(self)
        StandardRopeInspect.Delete_Rope_Data(self)
        
        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)
        Ropes_Menu()         

    def on_vertical_scroll(self, event):
        """Scroll the canvas vertically using the mouse wheel."""
        self.resultCanvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def ConnectorComposable(self):
        """ 
        Function Name: ConnectorComposable
        Function Purpose: This function is the complete the inspection for the Connector
        """
        # Create the label for the drop down menu lists for the first connector
        self.lblConnectorOneHeaderInfo = Label(self.resultFrame, text="Connector Information")
        self.lblConnectorOneType = Label(self.resultFrame, text="Connector Type:")
        self.lblConnectorOneSerialNum = Label(self.resultFrame, text="Serial Number:")
        self.lblConnectorOneBumperNum = Label(self.resultFrame, text="Bumper Number:")
        self.lblConnectorOneManuName = Label(self.resultFrame, text="Manufacture Name:")
        self.lblConnectorOneManDate = Label(self.resultFrame, text="Manufacture Date:")
        self.lblConnectorOneInstallDate= Label(self.resultFrame, text="Install Date:")
        self.lblConnectorOneLastInsDate = Label(self.resultFrame, text="Last Inspection Date:")
        self.lblConnectorOneNextInsDate = Label(self.resultFrame, text="Next Inspection Date:")
        self.lblConnectorOneInUse = Label(self.resultFrame, text="Device In Use:")
        self.lblConnectorOneLocation = Label(self.resultFrame, text="Connector Location:")
        self.lblConnectorOneSpacerOne = Label(self.resultFrame, text="")
        self.lblConnectorOneHeaderResults = Label(self.resultFrame, text="First Connector Results")
        self.lblConnectorOneVisual = Label(self.resultFrame, text="Visual Component:")
        self.lblConnectorOnePhysical = Label(self.resultFrame, text="Physical Component:")        
        self.lblConnectorOneFunct = Label(self.resultFrame, text="Function Component:")
        self.lblConnectorOneVisualStatus = Label(self.resultFrame, text="Visual Status:")
        self.lblConnectorOnePhysicalStatus = Label(self.resultFrame, text="Physical Status:")
        self.lblConnectorOneFunctStatus = Label(self.resultFrame, text="Function Status:")
        
        # Create the label locations
        self.lblConnectorOneHeaderInfo.grid(row=0, padx=220, column=0, columnspan=2, sticky='EW') 
        self.lblConnectorOneType.grid(row=1, padx=50, column=0, sticky='W')
        self.lblConnectorOneSerialNum.grid(row=2, padx=50, column=0, sticky='W')
        self.lblConnectorOneBumperNum.grid(row=3, padx=50, column=0, sticky='W')
        self.lblConnectorOneManuName.grid(row=4, padx=50, column=0, sticky='W')
        self.lblConnectorOneManDate.grid(row=5, padx=50, column=0, sticky='W')
        self.lblConnectorOneInstallDate.grid(row=6, padx=50, column=0, sticky='W')        
        self.lblConnectorOneLastInsDate.grid(row=7, padx=50, column=0, sticky='W') 
        self.lblConnectorOneNextInsDate.grid(row=8, padx=50, column=0, sticky='W') 
        self.lblConnectorOneInUse.grid(row=9, padx=50, column=0, sticky='W') 
        self.lblConnectorOneLocation.grid(row=10, padx=50, column=0, sticky='W') 
        self.lblConnectorOneSpacerOne.grid(row=11, padx=50, column=0, sticky='W') 
        self.lblConnectorOneHeaderResults.grid(row=12, padx=50, column=0, columnspan=2, sticky='EW') 
        self.lblConnectorOneVisual.grid(row=13, padx=50, column=0, sticky='W') 
        self.lblConnectorOnePhysical.grid(row=14, padx=50, column=0, sticky='W') 
        self.lblConnectorOneFunct.grid(row=15, padx=50, column=0, sticky='W') 
        self.lblConnectorOneVisualStatus.grid(row=16, padx=50, column=0, sticky='W')
        self.lblConnectorOnePhysicalStatus.grid(row=17, padx=50, column=0, sticky='W')
        self.lblConnectorOneFunctStatus.grid(row=18, padx=50, column=0, sticky='W')

        # Create the output boxes to display the results as normal
        self.ConnectorOneTypeOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneSerialNumOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneBumperNumOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneManuNameOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneManDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneInstallDateOutput = Entry(self.resultFrame, width=40, state='normal')       
        self.ConnectorOneLastInsDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneNextInsDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneInUseOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneLocationOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneVisualOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOnePhysicalOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneFunctOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneVisualStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOnePhysicalStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneFunctStatusOutput = Entry(self.resultFrame, width=40, state='normal')

    def ConnectorEntryComposable(self):
        """ 
        Function Name: ConnectorEntryComposable
        Function Purpose: This function is the complete the inspection for the Connectors 
        """
        # Set the values to the output boxes 
        self.ConnectorOneTypeOutput.insert(0, Connectors.strDeviceType)
        self.ConnectorOneSerialNumOutput.insert(0, Connectors.strSerialNum)
        self.ConnectorOneBumperNumOutput.insert(0, Connectors.strBumperNum)
        self.ConnectorOneManuNameOutput.insert(0, Connectors.strManufactureName)
        self.ConnectorOneManDateOutput.insert(0, Connectors.dtmManufactureDate)
        self.ConnectorOneInstallDateOutput.insert(0, Connectors.dtmInstallationDate)
        self.ConnectorOneLastInsDateOutput.insert(0, self.LastInspectionDate)
        self.ConnectorOneNextInsDateOutput.insert(0, self.NextInspectionDate)
        self.ConnectorOneInUseOutput.insert(0, Connectors.strEquipInUse)
        self.ConnectorOneLocationOutput.insert(0, WallLocation.strWallLocationDesc)
        self.ConnectorOneVisualOutput.insert(0, ConnectorVisSelection.strConnectorVisMetalSelect)
        self.ConnectorOnePhysicalOutput.insert(0, ConnectorPhysSelection.strConnectorPhysMetalSelect)
        self.ConnectorOneFunctOutput.insert(0, ConnectorFunctSelection.strConnectorFunctSelect)
        self.ConnectorOneVisualStatusOutput.insert(0, ConnectorVisSelection.strConnectorVisStatus)
        self.ConnectorOnePhysicalStatusOutput.insert(0, ConnectorPhysSelection.strConnectorPhysStatus)
        self.ConnectorOneFunctStatusOutput.insert(0, ConnectorFunctSelection.strConnectorFunctStatus)

        # Create the output boxes to display the results as readonly after the inputs have been placed for connector one
        self.ConnectorOneTypeOutput.configure(state='readonly')
        self.ConnectorOneSerialNumOutput.configure(state='readonly')
        self.ConnectorOneBumperNumOutput.configure(state='readonly')
        self.ConnectorOneManuNameOutput.configure(state='readonly')
        self.ConnectorOneManDateOutput.configure(state='readonly')
        self.ConnectorOneInstallDateOutput.configure(state='readonly')       
        self.ConnectorOneLastInsDateOutput.configure(state='readonly')
        self.ConnectorOneNextInsDateOutput.configure(state='readonly')
        self.ConnectorOneInUseOutput.configure(state='readonly')
        self.ConnectorOneLocationOutput.configure(state='readonly')
        self.ConnectorOneVisualOutput.configure(state='readonly')
        self.ConnectorOnePhysicalOutput.configure(state='readonly')
        self.ConnectorOneFunctOutput.configure(state='readonly')
        self.ConnectorOneVisualStatusOutput.configure(state='readonly')
        self.ConnectorOnePhysicalStatusOutput.configure(state='readonly')
        self.ConnectorOneFunctStatusOutput.configure(state='readonly')

        # Create the grid for the entry field objects
        self.ConnectorOneTypeOutput.grid(row=1, column=1, padx=(0, 20))
        self.ConnectorOneSerialNumOutput.grid(row=2, column=1, padx=(0, 20))
        self.ConnectorOneBumperNumOutput.grid(row=3, column=1, padx=(0, 20))
        self.ConnectorOneManuNameOutput.grid(row=4, column=1, padx=(0, 20))
        self.ConnectorOneManDateOutput.grid(row=5, column=1, padx=(0, 20))
        self.ConnectorOneInstallDateOutput.grid(row=6, column=1, padx=(0, 20))
        self.ConnectorOneLastInsDateOutput.grid(row=7, column=1, padx=(0, 20))
        self.ConnectorOneNextInsDateOutput.grid(row=8, column=1, padx=(0, 20))
        self.ConnectorOneInUseOutput.grid(row=9, column=1, padx=(0, 20))
        self.ConnectorOneLocationOutput.grid(row=10, column=1, padx=(0, 20))
        self.ConnectorOneVisualOutput.grid(row=13, column=1, padx=(0, 20))
        self.ConnectorOnePhysicalOutput.grid(row=14, column=1, padx=(0, 20))
        self.ConnectorOneFunctOutput.grid(row=15, column=1, padx=(0, 20))
        self.ConnectorOneVisualStatusOutput.grid(row=16, column=1, padx=(0, 20))
        self.ConnectorOnePhysicalStatusOutput.grid(row=17, column=1, padx=(0, 20))
        self.ConnectorOneFunctStatusOutput.grid(row=18, column=1, padx=(0, 20))

    def Two_ConnectorComposable(self):
        """ 
        Function Name: Two_ConnectorComposable
        Function Purpose: This function is the complete the inspection for the Two Connectors
        """
        # Create the label for the drop down menu lists for the first connector
        self.lblConnectorOneHeaderInfo = Label(self.resultFrame, text="First Connector Information")
        self.lblConnectorOneType = Label(self.resultFrame, text="Connector Type:")
        self.lblConnectorOneSerialNum = Label(self.resultFrame, text="Serial Number:")
        self.lblConnectorOneBumperNum = Label(self.resultFrame, text="Bumper Number:")
        self.lblConnectorOneManuName = Label(self.resultFrame, text="Manufacture Name:")
        self.lblConnectorOneManDate = Label(self.resultFrame, text="Manufacture Date:")
        self.lblConnectorOneInstallDate= Label(self.resultFrame, text="Install Date:")
        self.lblConnectorOneLastInsDate = Label(self.resultFrame, text="Last Inspection Date:")
        self.lblConnectorOneNextInsDate = Label(self.resultFrame, text="Next Inspection Date:")
        self.lblConnectorOneInUse = Label(self.resultFrame, text="Device In Use:")
        self.lblConnectorOneLocation = Label(self.resultFrame, text="Connector Location:")
        self.lblConnectorOneSpacerOne = Label(self.resultFrame, text="")
        self.lblConnectorOneHeaderResults = Label(self.resultFrame, text="First Connector Results")
        self.lblConnectorOneVisual = Label(self.resultFrame, text="Visual Component:")
        self.lblConnectorOnePhysical = Label(self.resultFrame, text="Physical Component:")        
        self.lblConnectorOneFunct = Label(self.resultFrame, text="Function Component:")
        self.lblConnectorOneVisualStatus = Label(self.resultFrame, text="Visual Status:")
        self.lblConnectorOnePhysicalStatus = Label(self.resultFrame, text="Physical Status:")
        self.lblConnectorOneFunctStatus = Label(self.resultFrame, text="Function Status:")

        # Create the label for the drop down menu lists for the second connector
        self.lblConnectorTwoSpacerOne = Label(self.resultFrame, text="")
        self.lblConnectorTwoHeaderInfo = Label(self.resultFrame, text="Second Connector Information")
        self.lblConnectorTwoType = Label(self.resultFrame, text="Connector Type:")
        self.lblConnectorTwoSerialNum = Label(self.resultFrame, text="Serial Number:")
        self.lblConnectorTwoBumperNum = Label(self.resultFrame, text="Bumper Number:")
        self.lblConnectorTwoManuName = Label(self.resultFrame, text="Manufacture Name:")
        self.lblConnectorTwoManDate = Label(self.resultFrame, text="Manufacture Date:")
        self.lblConnectorTwoInstallDate= Label(self.resultFrame, text="Install Date:")
        self.lblConnectorTwoLastInsDate = Label(self.resultFrame, text="Last Inspection Date:")
        self.lblConnectorTwoNextInsDate = Label(self.resultFrame, text="Next Inspection Date:")
        self.lblConnectorTwoInUse = Label(self.resultFrame, text="Device In Use:")
        self.lblConnectorTwoLocation = Label(self.resultFrame, text="Connector Location:")
        self.lblConnectorTwoSpacerTwo = Label(self.resultFrame, text="")
        self.lblConnectorTwoHeaderResults = Label(self.resultFrame, text="Second Connector Results")
        self.lblConnectorTwoVisual = Label(self.resultFrame, text="Visual Component:")
        self.lblConnectorTwoPhysical = Label(self.resultFrame, text="Physical Component:")        
        self.lblConnectorTwoFunct = Label(self.resultFrame, text="Function Component:")
        self.lblConnectorTwoVisualStatus = Label(self.resultFrame, text="Visual Status:")
        self.lblConnectorTwoPhysicalStatus = Label(self.resultFrame, text="Physical Status:")
        self.lblConnectorTwoFunctStatus = Label(self.resultFrame, text="Function Status:")
        
        # Create the label locations
        self.lblConnectorOneHeaderInfo.grid(row=0, padx=220, column=0, columnspan=2, sticky='EW') 
        self.lblConnectorOneType.grid(row=1, padx=50, column=0, sticky='W')
        self.lblConnectorOneSerialNum.grid(row=2, padx=50, column=0, sticky='W')
        self.lblConnectorOneBumperNum.grid(row=3, padx=50, column=0, sticky='W')
        self.lblConnectorOneManuName.grid(row=4, padx=50, column=0, sticky='W')
        self.lblConnectorOneManDate.grid(row=5, padx=50, column=0, sticky='W')
        self.lblConnectorOneInstallDate.grid(row=6, padx=50, column=0, sticky='W')        
        self.lblConnectorOneLastInsDate.grid(row=7, padx=50, column=0, sticky='W') 
        self.lblConnectorOneNextInsDate.grid(row=8, padx=50, column=0, sticky='W') 
        self.lblConnectorOneInUse.grid(row=9, padx=50, column=0, sticky='W') 
        self.lblConnectorOneLocation.grid(row=10, padx=50, column=0, sticky='W') 
        self.lblConnectorOneSpacerOne.grid(row=11, padx=50, column=0, sticky='W') 
        self.lblConnectorOneHeaderResults.grid(row=12, padx=50, column=0, columnspan=2, sticky='EW') 
        self.lblConnectorOneVisual.grid(row=13, padx=50, column=0, sticky='W') 
        self.lblConnectorOnePhysical.grid(row=14, padx=50, column=0, sticky='W') 
        self.lblConnectorOneFunct.grid(row=15, padx=50, column=0, sticky='W') 
        self.lblConnectorOneVisualStatus.grid(row=16, padx=50, column=0, sticky='W')
        self.lblConnectorOnePhysicalStatus.grid(row=17, padx=50, column=0, sticky='W')
        self.lblConnectorOneFunctStatus.grid(row=18, padx=50, column=0, sticky='W')

        # Create the label locations 
        self.lblConnectorTwoSpacerOne.grid(row=19, padx=50, column=0, sticky='W')
        self.lblConnectorTwoHeaderInfo.grid(row=20, padx=50, column=0, columnspan=2, sticky='EW')
        self.lblConnectorTwoType.grid(row=21, padx=50, column=0, sticky='W')
        self.lblConnectorTwoSerialNum.grid(row=22, padx=50, column=0, sticky='W')
        self.lblConnectorTwoBumperNum.grid(row=23, padx=50, column=0, sticky='W')
        self.lblConnectorTwoManuName.grid(row=24, padx=50, column=0, sticky='W')
        self.lblConnectorTwoManDate.grid(row=25, padx=50, column=0, sticky='W')
        self.lblConnectorTwoInstallDate.grid(row=26, padx=50, column=0, sticky='W')        
        self.lblConnectorTwoLastInsDate.grid(row=27, padx=50, column=0, sticky='W') 
        self.lblConnectorTwoNextInsDate.grid(row=28, padx=50, column=0, sticky='W') 
        self.lblConnectorTwoInUse.grid(row=29, padx=50, column=0, sticky='W') 
        self.lblConnectorTwoLocation.grid(row=30, padx=50, column=0, sticky='W')
        self.lblConnectorTwoSpacerTwo.grid(row=31, padx=50, column=0, sticky='W') 
        self.lblConnectorTwoHeaderResults.grid(row=32, padx=50, column=0, columnspan=2, sticky='EW') 
        self.lblConnectorTwoVisual.grid(row=33, padx=50, column=0, sticky='W') 
        self.lblConnectorTwoPhysical.grid(row=34, padx=50, column=0, sticky='W') 
        self.lblConnectorTwoFunct.grid(row=35, padx=50, column=0, sticky='W') 
        self.lblConnectorTwoVisualStatus.grid(row=36, padx=50, column=0, sticky='W')
        self.lblConnectorTwoPhysicalStatus.grid(row=37, padx=50, column=0, sticky='W')
        self.lblConnectorTwoFunctStatus.grid(row=38, padx=50, column=0, sticky='W')

        # Create the output boxes to display the results as normal
        self.ConnectorOneTypeOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneSerialNumOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneBumperNumOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneManuNameOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneManDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneInstallDateOutput = Entry(self.resultFrame, width=40, state='normal')       
        self.ConnectorOneLastInsDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneNextInsDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneInUseOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneLocationOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneVisualOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOnePhysicalOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneFunctOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneVisualStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOnePhysicalStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorOneFunctStatusOutput = Entry(self.resultFrame, width=40, state='normal')

        # Create the output boxes to display the results as normal
        self.ConnectorTwoTypeOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorTwoSerialNumOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorTwoBumperNumOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorTwoManuNameOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorTwoManDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorTwoInstallDateOutput = Entry(self.resultFrame, width=40, state='normal')     
        self.ConnectorTwoLastInsDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorTwoNextInsDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorTwoInUseOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorTwoLocationOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorTwoVisualOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorTwoPhysicalOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorTwoFunctOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorTwoVisualStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorTwoPhysicalStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorTwoFunctStatusOutput = Entry(self.resultFrame, width=40, state='normal')

    def Two_ConnectorEntryComposable(self):
        """ 
        Function Name: Two_ConnectorEntryComposable
        Function Purpose: This function is the complete the inspection for the Two Connectors 
        """
        # Get the two selected connectors
        amultiConnectorList = Connectors.Get_TwoConnector_StageList_Obj(Connectors)

        # Set the values to the output boxes 
        self.ConnectorOneTypeOutput.insert(0, amultiConnectorList[0][8])
        self.ConnectorOneSerialNumOutput.insert(0, amultiConnectorList[0][1])
        self.ConnectorOneBumperNumOutput.insert(0, amultiConnectorList[0][2])
        self.ConnectorOneManuNameOutput.insert(0, amultiConnectorList[0][3])
        self.ConnectorOneManDateOutput.insert(0, amultiConnectorList[0][4])
        self.ConnectorOneInstallDateOutput.insert(0, amultiConnectorList[0][5])
        self.ConnectorOneLastInsDateOutput.insert(0, self.LastInspectionDate)
        self.ConnectorOneNextInsDateOutput.insert(0, self.NextInspectionDate)
        self.ConnectorOneInUseOutput.insert(0, amultiConnectorList[0][9])
        self.ConnectorOneLocationOutput.insert(0, WallLocation.strWallLocationDesc)
        self.ConnectorOneVisualOutput.insert(0, ConnectorVisSelection.aTwoConnectorVisSelectCache[0][1])
        self.ConnectorOnePhysicalOutput.insert(0, ConnectorPhysSelection.aTwoConnectorPhysSelectCache[0][1])
        self.ConnectorOneFunctOutput.insert(0, ConnectorFunctSelection.aTwoConnectorFunctSelectCache[0][1])
        self.ConnectorOneVisualStatusOutput.insert(0, ConnectorVisSelection.aTwoConnectorVisSelectCache[0][2])
        self.ConnectorOnePhysicalStatusOutput.insert(0, ConnectorPhysSelection.aTwoConnectorPhysSelectCache[0][2])
        self.ConnectorOneFunctStatusOutput.insert(0, ConnectorFunctSelection.aTwoConnectorFunctSelectCache[0][2])

        # Set the values to the output boxes 
        self.ConnectorTwoTypeOutput.insert(0, amultiConnectorList[1][8])
        self.ConnectorTwoSerialNumOutput.insert(0, amultiConnectorList[1][1])
        self.ConnectorTwoBumperNumOutput.insert(0, amultiConnectorList[1][2])
        self.ConnectorTwoManuNameOutput.insert(0, amultiConnectorList[1][3])
        self.ConnectorTwoManDateOutput.insert(0, amultiConnectorList[1][4])
        self.ConnectorTwoInstallDateOutput.insert(0, amultiConnectorList[1][5])
        self.ConnectorTwoLastInsDateOutput.insert(0, self.LastInspectionDate)
        self.ConnectorTwoNextInsDateOutput.insert(0, self.NextInspectionDate)
        self.ConnectorTwoInUseOutput.insert(0, amultiConnectorList[1][9])
        self.ConnectorTwoLocationOutput.insert(0, WallLocation.strWallLocationDesc)
        self.ConnectorTwoVisualOutput.insert(0, ConnectorVisSelection.aTwoConnectorVisSelectCache[1][1])
        self.ConnectorTwoPhysicalOutput.insert(0, ConnectorPhysSelection.aTwoConnectorPhysSelectCache[1][1])
        self.ConnectorTwoFunctOutput.insert(0, ConnectorFunctSelection.aTwoConnectorFunctSelectCache[1][1])
        self.ConnectorTwoVisualStatusOutput.insert(0, ConnectorVisSelection.aTwoConnectorVisSelectCache[1][2])
        self.ConnectorTwoPhysicalStatusOutput.insert(0, ConnectorPhysSelection.aTwoConnectorPhysSelectCache[1][2])
        self.ConnectorTwoFunctStatusOutput.insert(0, ConnectorFunctSelection.aTwoConnectorFunctSelectCache[1][2])

        # Create the output boxes to display the results as readonly after the inputs have been placed for connector one
        self.ConnectorOneTypeOutput.configure(state='readonly')
        self.ConnectorOneSerialNumOutput.configure(state='readonly')
        self.ConnectorOneBumperNumOutput.configure(state='readonly')
        self.ConnectorOneManuNameOutput.configure(state='readonly')
        self.ConnectorOneManDateOutput.configure(state='readonly')
        self.ConnectorOneInstallDateOutput.configure(state='readonly')       
        self.ConnectorOneLastInsDateOutput.configure(state='readonly')
        self.ConnectorOneNextInsDateOutput.configure(state='readonly')
        self.ConnectorOneInUseOutput.configure(state='readonly')
        self.ConnectorOneLocationOutput.configure(state='readonly')
        self.ConnectorOneVisualOutput.configure(state='readonly')
        self.ConnectorOnePhysicalOutput.configure(state='readonly')
        self.ConnectorOneFunctOutput.configure(state='readonly')
        self.ConnectorOneVisualStatusOutput.configure(state='readonly')
        self.ConnectorOnePhysicalStatusOutput.configure(state='readonly')
        self.ConnectorOneFunctStatusOutput.configure(state='readonly')

        # Create the output boxes to display the results as readonly after the inputs have been placed for connector two
        self.ConnectorTwoTypeOutput.configure(state='readonly')
        self.ConnectorTwoSerialNumOutput.configure(state='readonly')
        self.ConnectorTwoBumperNumOutput.configure(state='readonly')
        self.ConnectorTwoManuNameOutput.configure(state='readonly')
        self.ConnectorTwoManDateOutput.configure(state='readonly')
        self.ConnectorTwoInstallDateOutput.configure(state='readonly')    
        self.ConnectorTwoLastInsDateOutput.configure(state='readonly')
        self.ConnectorTwoNextInsDateOutput.configure(state='readonly')
        self.ConnectorTwoInUseOutput.configure(state='readonly')
        self.ConnectorTwoLocationOutput.configure(state='readonly')
        self.ConnectorTwoVisualOutput.configure(state='readonly')
        self.ConnectorTwoPhysicalOutput.configure(state='readonly')
        self.ConnectorTwoFunctOutput.configure(state='readonly')
        self.ConnectorTwoVisualStatusOutput.configure(state='readonly')
        self.ConnectorTwoPhysicalStatusOutput.configure(state='readonly')
        self.ConnectorTwoFunctStatusOutput.configure(state='readonly')

        # Create the grid for the entry field objects
        self.ConnectorOneTypeOutput.grid(row=1, column=1, padx=(0, 20))
        self.ConnectorOneSerialNumOutput.grid(row=2, column=1, padx=(0, 20))
        self.ConnectorOneBumperNumOutput.grid(row=3, column=1, padx=(0, 20))
        self.ConnectorOneManuNameOutput.grid(row=4, column=1, padx=(0, 20))
        self.ConnectorOneManDateOutput.grid(row=5, column=1, padx=(0, 20))
        self.ConnectorOneInstallDateOutput.grid(row=6, column=1, padx=(0, 20))
        self.ConnectorOneLastInsDateOutput.grid(row=7, column=1, padx=(0, 20))
        self.ConnectorOneNextInsDateOutput.grid(row=8, column=1, padx=(0, 20))
        self.ConnectorOneInUseOutput.grid(row=9, column=1, padx=(0, 20))
        self.ConnectorOneLocationOutput.grid(row=10, column=1, padx=(0, 20))
        self.ConnectorOneVisualOutput.grid(row=13, column=1, padx=(0, 20))
        self.ConnectorOnePhysicalOutput.grid(row=14, column=1, padx=(0, 20))
        self.ConnectorOneFunctOutput.grid(row=15, column=1, padx=(0, 20))
        self.ConnectorOneVisualStatusOutput.grid(row=16, column=1, padx=(0, 20))
        self.ConnectorOnePhysicalStatusOutput.grid(row=17, column=1, padx=(0, 20))
        self.ConnectorOneFunctStatusOutput.grid(row=18, column=1, padx=(0, 20))

        # Create the grid for the entry field objects
        self.ConnectorTwoTypeOutput.grid(row=21, column=1, padx=(0, 20))
        self.ConnectorTwoSerialNumOutput.grid(row=22, column=1, padx=(0, 20))
        self.ConnectorTwoBumperNumOutput.grid(row=23, column=1, padx=(0, 20))
        self.ConnectorTwoManuNameOutput.grid(row=24, column=1, padx=(0, 20))
        self.ConnectorTwoManDateOutput.grid(row=25, column=1, padx=(0, 20))
        self.ConnectorTwoInstallDateOutput.grid(row=26, column=1, padx=(0, 20))
        self.ConnectorTwoLastInsDateOutput.grid(row=27, column=1, padx=(0, 20))
        self.ConnectorTwoNextInsDateOutput.grid(row=28, column=1, padx=(0, 20))
        self.ConnectorTwoInUseOutput.grid(row=29, column=1, padx=(0, 20))
        self.ConnectorTwoLocationOutput.grid(row=30, column=1, padx=(0, 20))
        self.ConnectorTwoVisualOutput.grid(row=33, column=1, padx=(0, 20))
        self.ConnectorTwoPhysicalOutput.grid(row=34, column=1, padx=(0, 20))
        self.ConnectorTwoFunctOutput.grid(row=35, column=1, padx=(0, 20))
        self.ConnectorTwoVisualStatusOutput.grid(row=36, column=1, padx=(0, 20))
        self.ConnectorTwoPhysicalStatusOutput.grid(row=37, column=1, padx=(0, 20))
        self.ConnectorTwoFunctStatusOutput.grid(row=38, column=1, padx=(0, 20))
                                        
    def BelayDeviceComposable(self):
        """ 
        Function Name: BelayDeviceComposable
        Function Purpose: This function is the complete the inspection for the Belay Device
        """
        # Create the label for the drop down menu lists
        self.lblBelayDeviceSpacerOne = Label(self.resultFrame, text="")
        self.lblBelayDeviceHeaderInfo = Label(self.resultFrame, text="Belay Device Information")
        self.lblBelayDeviceName = Label(self.resultFrame, text="Belay Device Name:")
        self.lblBelayDeviceType = Label(self.resultFrame, text="Belay Device Type:")
        self.lblBelayDeviceSerialNum = Label(self.resultFrame, text="Serial Number:")
        self.lblBelayDeviceBumperNum = Label(self.resultFrame, text="Bumper Number:")
        self.lblBelayDeviceManuName = Label(self.resultFrame, text="Manufacture Name:")
        self.lblBelayDeviceManDate = Label(self.resultFrame, text="Manufacture Date:")
        self.lblBelayDeviceInstallDate= Label(self.resultFrame, text="Install Date:")
        self.lblBelayDeviceLastInsDate = Label(self.resultFrame, text="Last Inspection Date:")
        self.lblBelayDeviceNextInsDate = Label(self.resultFrame, text="Next Inspection Date:")
        self.lblBelayDeviceInUse = Label(self.resultFrame, text="Device In Use:")
        self.lblBelayDeviceLocation = Label(self.resultFrame, text="Belay Device Location:")
        self.lblBelayDeviceSpacerTwo = Label(self.resultFrame, text="")
        self.lblBelayDeviceMetalHeaderResults = Label(self.resultFrame, text="Belay Device Metal Results")
        self.lblMetBelayDeviceVisual = Label(self.resultFrame, text="Visual Metal Component:")
        self.lblMetBelayDevicePhysical = Label(self.resultFrame, text="Physical Metal Component:")        
        self.lblMetBelayDeviceFunct = Label(self.resultFrame, text="Function Metal Component:")
        self.lblMetBelayDeviceVisualStatus = Label(self.resultFrame, text="Visual Metal Status:")
        self.lblMetBelayDevicePhysicalStatus = Label(self.resultFrame, text="Physical Metal Status:")
        self.lblMetBelayDeviceFunctStatus = Label(self.resultFrame, text="Function Metal Status:")
        self.lblBelayDeviceSpacerThree = Label(self.resultFrame, text="")
        self.lblBelayDevicePlasticHeaderResults = Label(self.resultFrame, text="Belay Device Plastic Results")
        self.lblPlastBelayDeviceVisual = Label(self.resultFrame, text="Visual Plastic Component:")
        self.lblPlastBelayDevicePhysical = Label(self.resultFrame, text="Physical Plastic Component:")        
        self.lblPlastBelayDeviceFunct = Label(self.resultFrame, text="Function Plastic Component:")
        self.lblPlastBelayDeviceVisualStatus = Label(self.resultFrame, text="Visual Plastic Status:")
        self.lblPlastBelayDevicePhysicalStatus = Label(self.resultFrame, text="Physical Plastic Status:")
        self.lblPlastBelayDeviceFunctStatus = Label(self.resultFrame, text="Function Plastic Status:")

        # Set the row staring point
        if Bool_Flag.blnComplexWith_Two_ConnectorFlag is True:
            row = 39
        elif (Bool_Flag.blnComplexWithBelayDeviceFlag is True) and (Bool_Flag.blnComplexWithConnectorFlag is True):
            row = 19
        else:
            row = 0
            
        # List of labels for Belay Device information
        belayDeviceLabels = [
        self.lblBelayDeviceSpacerOne, self.lblBelayDeviceHeaderInfo, self.lblBelayDeviceName, 
        self.lblBelayDeviceType, self.lblBelayDeviceSerialNum, self.lblBelayDeviceBumperNum,
        self.lblBelayDeviceManuName, self.lblBelayDeviceManDate, self.lblBelayDeviceInstallDate, 
        self.lblBelayDeviceLastInsDate, self.lblBelayDeviceNextInsDate, self.lblBelayDeviceInUse, 
        self.lblBelayDeviceLocation, self.lblBelayDeviceSpacerTwo, self.lblBelayDeviceMetalHeaderResults, 
        self.lblMetBelayDeviceVisual, self.lblMetBelayDevicePhysical, self.lblMetBelayDeviceFunct, 
        self.lblMetBelayDeviceVisualStatus, self.lblMetBelayDevicePhysicalStatus, self.lblMetBelayDeviceFunctStatus,
        self.lblBelayDeviceSpacerThree, self.lblBelayDevicePlasticHeaderResults, self.lblPlastBelayDeviceVisual, 
        self.lblPlastBelayDevicePhysical, self.lblPlastBelayDeviceFunct, self.lblPlastBelayDeviceVisualStatus, 
        self.lblPlastBelayDevicePhysicalStatus, self.lblPlastBelayDeviceFunctStatus
        ]                

        if row == 0:
            belayDeviceLabels.pop(0)
            
        # Iterate through the labels and grid them with incremental row numbers
        for label in belayDeviceLabels:
            # Determine columnspan based on label text content
            # print(label.cget("text"))
            columnspan = 2 if "Information" in label.cget("text") or "Results" in label.cget("text") else 1
            
            # Determine the padx based on label text content
            padx = 220 if "Information" in label.cget("text") or "Results" in label.cget("text") else 50
                
            # For labels that are headers or results, which span across columns, we want them centered
            if columnspan == 2:
                # To visually center the label, especially if it's a header/results, adjust 'sticky'
                label.grid(row=row, padx=padx, column=0, columnspan=columnspan, sticky='EW')
            else:
                # For all other labels, align them to the west
                label.grid(row=row, padx=padx, column=0, columnspan=columnspan, sticky='W')
            row += 1  # Increment row for the next label
        
        # Create the output boxes to display the results as normal
        self.BelayDeviceNameOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceTypeOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceSerialNumOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceBumperNumOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceManuNameOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceManDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceInstallDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceLastInsDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceNextInsDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceInUseOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceLocationOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceMetVisualOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceMetPhysicalOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceMetFunctOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceMetVisStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceMetPhysStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceMetFunctStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDevicePlastVisualOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDevicePlastPhysicalOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDevicePlastFunctOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDevicePlastVisStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDevicePlastPhysStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDevicePlastFunctStatusOutput = Entry(self.resultFrame, width=40, state='normal')

    def BelayDeviceEntryComposable(self):
        """ 
        Function Name: BelayDeviceEntryComposable
        Function Purpose: This function is the complete the inspection for the BelayDevice Entry 
        """
        # Set the values to the output boxes 
        self.BelayDeviceNameOutput.insert(0, BelayDevices.strBelayDeviceName)
        self.BelayDeviceTypeOutput.insert(0, BelayDevices.strDeviceType)
        self.BelayDeviceSerialNumOutput.insert(0, BelayDevices.strSerialNum)
        self.BelayDeviceBumperNumOutput.insert(0, BelayDevices.strBumperNum)
        self.BelayDeviceManuNameOutput.insert(0, BelayDevices.strManufactureName)
        self.BelayDeviceManDateOutput.insert(0, BelayDevices.dtmManufactureDate)
        self.BelayDeviceInstallDateOutput.insert(0, BelayDevices.dtmInstallationDate)
        self.BelayDeviceLastInsDateOutput.insert(0, self.LastInspectionDate)
        self.BelayDeviceNextInsDateOutput.insert(0, self.NextInspectionDate)
        self.BelayDeviceInUseOutput.insert(0, BelayDevices.strEquipInUse)
        self.BelayDeviceLocationOutput.insert(0, WallLocation.strWallLocationDesc)
        self.BelayDeviceMetVisualOutput.insert(0, BelayDeviceVisSelection.strBelayDeviceVisMetSelect)
        self.BelayDeviceMetPhysicalOutput.insert(0, BelayDevicePhysSelection.strBelayDevicePhysMetSelect)
        self.BelayDeviceMetFunctOutput.insert(0, BelayDeviceFunctSelection.strBelayDeviceFunctSelect)
        self.BelayDeviceMetVisStatusOutput.insert(0, BelayDeviceVisSelection.strBelayDeviceVisStatus)
        self.BelayDeviceMetPhysStatusOutput.insert(0, BelayDevicePhysSelection.strBelayDevicePhysStatus)
        self.BelayDeviceMetFunctStatusOutput.insert(0, BelayDeviceFunctSelection.strBelayDeviceFunctStatus)
        self.BelayDevicePlastVisualOutput.insert(0, BelayDevicePlasticVisSelection.strBelayDeviceVisPlastSelect)
        self.BelayDevicePlastPhysicalOutput.insert(0, BelayDevicePlasticPhysSelection.strBelayDevicePhysPlastSelect)
        self.BelayDevicePlastFunctOutput.insert(0, BelayDevicePlasticFunctSelection.strBelayDeviceFunctPlastSelect)
        self.BelayDevicePlastVisStatusOutput.insert(0, BelayDevicePlasticVisSelection.strBelayDeviceVisStatus)
        self.BelayDevicePlastPhysStatusOutput.insert(0, BelayDevicePlasticPhysSelection.strBelayDevicePhysStatus)
        self.BelayDevicePlastFunctStatusOutput.insert(0, BelayDevicePlasticFunctSelection.strBelayDeviceFunctStatus)

        # Create the output boxes to display the results as readonly after the inputs have been placed
        self.BelayDeviceNameOutput.configure(state='readonly')
        self.BelayDeviceTypeOutput.configure(state='readonly')
        self.BelayDeviceSerialNumOutput.configure(state='readonly')
        self.BelayDeviceBumperNumOutput.configure(state='readonly')
        self.BelayDeviceManuNameOutput.configure(state='readonly')
        self.BelayDeviceManDateOutput.configure(state='readonly')
        self.BelayDeviceInstallDateOutput.configure(state='readonly')
        self.BelayDeviceLastInsDateOutput.configure(state='readonly')
        self.BelayDeviceNextInsDateOutput.configure(state='readonly')
        self.BelayDeviceInUseOutput.configure(state='readonly')
        self.BelayDeviceLocationOutput.configure(state='readonly')
        self.BelayDeviceMetVisualOutput.configure(state='readonly')
        self.BelayDeviceMetPhysicalOutput.configure(state='readonly')
        self.BelayDeviceMetFunctOutput.configure(state='readonly')
        self.BelayDeviceMetVisStatusOutput.configure(state='readonly')
        self.BelayDeviceMetPhysStatusOutput.configure(state='readonly')
        self.BelayDeviceMetFunctStatusOutput.configure(state='readonly')
        self.BelayDevicePlastVisualOutput.configure(state='readonly')
        self.BelayDevicePlastPhysicalOutput.configure(state='readonly')
        self.BelayDevicePlastFunctOutput.configure(state='readonly')
        self.BelayDevicePlastVisStatusOutput.configure(state='readonly')
        self.BelayDevicePlastPhysStatusOutput.configure(state='readonly')
        self.BelayDevicePlastFunctStatusOutput.configure(state='readonly')   

        # Set the row staring point
        if Bool_Flag.blnComplexWith_Two_ConnectorFlag is True:
            row = 41
        elif (Bool_Flag.blnComplexWithBelayDeviceFlag is True) and (Bool_Flag.blnComplexWithConnectorFlag is True):
            row = 21
        else:
            row = 1

        # List of entry fields for Belay Device information
        belayDeviceEntryFields = [
            self.BelayDeviceNameOutput, self.BelayDeviceTypeOutput, self.BelayDeviceSerialNumOutput,   
            self.BelayDeviceBumperNumOutput, self.BelayDeviceManuNameOutput, self.BelayDeviceManDateOutput, 
            self.BelayDeviceInstallDateOutput, self.BelayDeviceLastInsDateOutput, self.BelayDeviceNextInsDateOutput,  
            self.BelayDeviceInUseOutput, self.BelayDeviceLocationOutput, 
            # Skip 2 rows before visual status entries
            None, None, self.BelayDeviceMetVisualOutput, self.BelayDeviceMetPhysicalOutput, self.BelayDeviceMetFunctOutput,
            self.BelayDeviceMetVisStatusOutput, self.BelayDeviceMetPhysStatusOutput, self.BelayDeviceMetFunctStatusOutput,
            # Skip 2 rows before plastic visual status entries
            None, None, self.BelayDevicePlastVisualOutput, self.BelayDevicePlastPhysicalOutput, self.BelayDevicePlastFunctOutput,
            self.BelayDevicePlastVisStatusOutput, self.BelayDevicePlastPhysStatusOutput, self.BelayDevicePlastFunctStatusOutput
        ]

        # Iterate through the entry fields and grid them with incremental row numbers
        for entryField in belayDeviceEntryFields:
            if entryField is None:
                row += 1  # Skip a row for None placeholder
                continue
            padx = (0, 20)
            entryField.grid(row=row, column=1, padx=padx)
            row += 1  # Increment row for the next entry field
                                                                
    def RopeComposable(self):
        """ 
        Function Name: RopeComposable
        Function Purpose: This function is the complete the inspection for the Rope
        """
        # Create the label for the drop down menu lists
        self.lblRopeSpacerOne = Label(self.resultFrame, text="")
        self.lblRopeHeaderInfo = Label(self.resultFrame, text="Rope Information")
        self.lblRopeElasticity = Label(self.resultFrame, text="Rope Elasticity:")
        self.lblRopeLength = Label(self.resultFrame, text="Rope Length:")
        self.lblRopeDiameter = Label(self.resultFrame, text="Rope Diameter:")
        self.lblRopeSerialNum = Label(self.resultFrame, text="Serial Number:")
        self.lblRopeBumperNum = Label(self.resultFrame, text="Bumper Number:")
        self.lblRopeManuName = Label(self.resultFrame, text="Manufacture Name:")
        self.lblRopeManDate = Label(self.resultFrame, text="Manufacture Date:")
        self.lblRopeInstallDate= Label(self.resultFrame, text="Install Date:")
        self.lblRopeLastInsDate = Label(self.resultFrame, text="Last Inspection Date:")
        self.lblRopeNextInsDate = Label(self.resultFrame, text="Next Inspection Date:")
        self.lblRopeInUse = Label(self.resultFrame, text="Rope In Use:")
        self.lblRopeLocation = Label(self.resultFrame, text="Rope Location:")
        self.lblRopeSpacerTwo = Label(self.resultFrame, text="")
        self.lblRopeHeaderResults = Label(self.resultFrame, text="Rope Textile Results")
        self.lblRopeTextVisual = Label(self.resultFrame, text="Visual Textile Component:")
        self.lblRopeTextPhysical = Label(self.resultFrame, text="Physical Textile Component:")        
        self.lblRopeTextVisualStatus = Label(self.resultFrame, text="Visual Textile Status:")
        self.lblRopeTextPhysicalStatus = Label(self.resultFrame, text="Physical Textile Status:")        

        # Set the row staring point
        if Bool_Flag.blnComplexWith_Two_ConnectorFlag is True:
                row = 68
        elif (Bool_Flag.blnComplexWithBelayDeviceFlag is True) and (Bool_Flag.blnComplexWithConnectorFlag is True):
                row = 48
        elif (Bool_Flag.blnComplexWithBelayDeviceFlag is True):
                row = 28                
        else:
                row = 0
                
        # List of labels for Rope information
        ropeLabels = [
        self.lblRopeSpacerOne, self.lblRopeHeaderInfo, self.lblRopeElasticity, self.lblRopeLength,
        self.lblRopeDiameter, self.lblRopeSerialNum, self.lblRopeBumperNum, self.lblRopeManuName,
        self.lblRopeManDate, self.lblRopeInstallDate, self.lblRopeLastInsDate, self.lblRopeNextInsDate,
        self.lblRopeInUse, self.lblRopeLocation, self.lblRopeSpacerTwo, self.lblRopeHeaderResults,
        self.lblRopeTextVisual, self.lblRopeTextPhysical, self.lblRopeTextVisualStatus, self.lblRopeTextPhysicalStatus
        ]

        # Iterate through the labels and grid them with incremental row numbers
        for label in ropeLabels:
            padx = 50
            sticky = 'W'
            # For labels that span across columns
            if label in [self.lblRopeHeaderInfo, self.lblRopeHeaderResults]:
                sticky = 'EW'
                label.grid(row=row, padx=padx, column=0, columnspan=2, sticky=sticky)
            else:
                label.grid(row=row, padx=padx, column=0, sticky=sticky)
            row += 1
                
        # Create the output boxes to display the results as normal
        self.RopeElasticityOutput = Entry(self.resultFrame, width=40, state='normal')
        self.RopeLengthOutput = Entry(self.resultFrame, width=40, state='normal')
        self.RopeDiameterOutput = Entry(self.resultFrame, width=40, state='normal')
        self.RopeSerialNumOutput = Entry(self.resultFrame, width=40, state='normal')
        self.RopeBumperNumOutput = Entry(self.resultFrame, width=40, state='normal')
        self.RopeManuNameOutput = Entry(self.resultFrame, width=40, state='normal')
        self.RopeManDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.RopeInstallDateOutput = Entry(self.resultFrame, width=40, state='normal')        
        self.RopeLastInsDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.RopeNextInsDateOutput = Entry(self.resultFrame, width=40, state='normal') 
        self.RopeInUseOutput = Entry(self.resultFrame, width=40, state='normal')
        self.RopeLocationOutput = Entry(self.resultFrame, width=40, state='normal')
        self.RopeTextVisualOutput = Entry(self.resultFrame, width=40, state='normal') 
        self.RopeTextPhysicalOutput = Entry(self.resultFrame, width=40, state='normal') 
        self.RopeTextVisualStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.RopeTextPhysicalStatusOutput = Entry(self.resultFrame, width=40, state='normal')

    def RopeEntryComposable(self):
        """ 
        Function Name: RopeEntryComposable
        Function Purpose: This function is the complete the inspection for the Rope
        """
        # Set the values to the output boxes 
        self.RopeElasticityOutput.insert(0, Ropes.strElasticity)
        self.RopeLengthOutput.insert(0, Ropes.strRopeLength)
        self.RopeDiameterOutput.insert(0, Ropes.strDiameter)
        self.RopeSerialNumOutput.insert(0, Ropes.strSerialNum)
        self.RopeBumperNumOutput.insert(0, Ropes.strBumperNum)
        self.RopeManuNameOutput.insert(0, Ropes.strManufactureName)
        self.RopeManDateOutput.insert(0, Ropes.dtmManufactureDate)
        self.RopeInstallDateOutput.insert(0, Ropes.dtmInstallationDate)      
        self.RopeLastInsDateOutput.insert(0, self.LastInspectionDate)
        self.RopeNextInsDateOutput.insert(0, self.NextInspectionDate)
        self.RopeInUseOutput.insert(0, Ropes.strEquipInUse)
        self.RopeLocationOutput.insert(0, WallLocation.strWallLocationDesc)
        self.RopeTextVisualOutput.insert(0, RopeVisSelection.strRopeVisTextSelect) 
        self.RopeTextPhysicalOutput.insert(0, RopePhysSelection.strRopePhysTextSelect) 
        self.RopeTextVisualStatusOutput.insert(0, RopeVisSelection.strRopeVisStatus)
        self.RopeTextPhysicalStatusOutput.insert(0, RopePhysSelection.strRopePhysStatus)

        # Create the output boxes to display the results as readonly after the inputs have been placed
        self.RopeElasticityOutput.configure(state='readonly')
        self.RopeLengthOutput.configure(state='readonly')
        self.RopeDiameterOutput.configure(state='readonly')
        self.RopeSerialNumOutput.configure(state='readonly')
        self.RopeBumperNumOutput.configure(state='readonly')
        self.RopeManuNameOutput.configure(state='readonly')
        self.RopeManDateOutput.configure(state='readonly')
        self.RopeInstallDateOutput.configure(state='readonly')        
        self.RopeLastInsDateOutput.configure(state='readonly')
        self.RopeNextInsDateOutput.configure(state='readonly')
        self.RopeInUseOutput.configure(state='readonly')
        self.RopeLocationOutput.configure(state='readonly')
        self.RopeTextVisualOutput.configure(state='readonly') 
        self.RopeTextPhysicalOutput.configure(state='readonly')
        self.RopeTextVisualStatusOutput.configure(state='readonly')
        self.RopeTextPhysicalStatusOutput.configure(state='readonly')

        # Set the row staring point
        if Bool_Flag.blnComplexWith_Two_ConnectorFlag is True:
            row = 70
        elif (Bool_Flag.blnComplexWithBelayDeviceFlag is True) and (Bool_Flag.blnComplexWithConnectorFlag is True):
            row = 50
        elif (Bool_Flag.blnComplexWithBelayDeviceFlag is True):
            row = 30
        else:
            row = 2
                
        # List of entry field objects for Rope information
        ropeEntryFields = [
        self.RopeElasticityOutput, self.RopeLengthOutput, self.RopeDiameterOutput,
        self.RopeSerialNumOutput, self.RopeBumperNumOutput, self.RopeManuNameOutput,
        self.RopeManDateOutput, self.RopeInstallDateOutput, self.RopeLastInsDateOutput,
        self.RopeNextInsDateOutput, self.RopeInUseOutput, self.RopeLocationOutput,
        # Skip 2 rows before visual status entries
        None, None, self.RopeTextVisualOutput, self.RopeTextPhysicalOutput,
        self.RopeTextVisualStatusOutput, self.RopeTextPhysicalStatusOutput
        ]

        # Iterate through the entry fields and grid them with incremental row numbers
        for entryField in ropeEntryFields:
            if entryField is None:
                row += 1  
                continue
            padx = (0, 20)
            entryField.grid(row=row, column=1, padx=padx)
            row += 1             
                                        
    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the new location to the db. Else, reset
        """
        # Check first with the user if the entry's are correct before dumping to DB
        if messagebox.askyesno(message='CAUTION! \n\n Proceed to submit Rope inspection?') is True:     
            # Load the user data and prep the data for db dump
            Complex_Rope_InspectionResults.Submit_Standard_Inspection_Rope(self)
            if (Bool_Flag.blnComplexWithBelayDeviceFlag is True):
                Complex_Rope_InspectionResults.Submit_Standard_Inspection_BelayDevice(self)
            if (Bool_Flag.blnComplexWith_Two_ConnectorFlag is True):
                Complex_Rope_InspectionResults.Submit_Standard_Inspection_TwoConnectors(self)
            else:
                Complex_Rope_InspectionResults.Submit_Standard_Inspection_Single_Connector(self)
            
            # Reset the objects list 
            self.Reset_Object_Lists()

            # Check if the user would like to add another inspection
            if messagebox.askyesno(message='SUCCESSFUL UPLOAD! \n\n Would you like to complete another inspection?') is True:
                # Clear the input fields and after data is submitted to the database
                Complex_Rope_InspectionResults.Exit(self)
                Start_Menu.Load_Obj_Lists(self)
                GymRopeSelection()
            else:
                Complex_Rope_InspectionResults.Exit(self)
                Ropes_Menu()
        else:
            pass  

    def Submit_Standard_Inspection_Single_Connector(self):
        """ 
        Function Name: Submit_Standard_Inspection_Single_Connector
        Function Purpose: This function is executed once the user clicks on the submit button and all the standard
        inspection data cached arrays will be pulled and dumped into the the database
        """    
        # Set the global Connector Attributes
        Connectors.Update_Connectors_Inspect_Dates(Connectors)        
        
        # Commit the Connector Inspection data to the database
        ConnectorVisSelection.Add_ConnectorVisSelectList_Query(self)
        ConnectorPhysSelection.Add_ConnectorPhysSelectList_Query(self)
        ConnectorFunctSelection.Add_ConnectorFunctSelection_Query(self)
        ConnectorVisualInspect.Add_ConnectorVisualInspect_Query(self)
        ConnectorPhysicalInspect.Add_ConnectorPhysicalInspect_Query(self)
        ConnectorFunctionInspect.Add_ConnectorFunctInspect_Query(self)
        StandardConnectorInspect.Add_StandConnectorInspect_Query(self)
        
        # Get the Connector overall status and update the units in use status 
        Connectors.Update_Connectors_InUse_Status(Connectors)
        
        # Commit the ConnectorInspect data to the database
        ConnectorInspect.Add_ConnectorInspection_Query(self)
        ConnectorInspect.Add_ConnectorInspector_Query(self)
        ConnectorInspect.Add_ConnectorLocation_Query(self)
        
        # First check if the unit has been packaged for reservice to add report to db
        if Bool_Flag.Get_ConnectorRetired_Bool_Value(Bool_Flag) is True:
            ConnectorsRetiredReport.Add_Connector_RetiredReport_Query(self)
        
    def Submit_Standard_Inspection_TwoConnectors(self):
        """ 
        Function Name: Submit_Standard_Inspection_TwoConnectors
        Function Purpose: This function is executed once the user clicks on the submit button and all the standard
        inspection data cached arrays will be pulled and dumped into the the database
        """    
        # Set the global Connector Attributes
        Connectors.Update_Connectors_Inspect_Dates(Connectors)        
        
        # Commit the Connector Inspection data to the database
        ConnectorVisSelection.Set_TwoConnectorVisualSelect_Data(self)
        ConnectorPhysSelection.Set_TwoConnectorPhysicalSelect_Data(self)
        ConnectorFunctSelection.Set_TwoConnectorFunctionalSelect_Data(self)
        ConnectorVisualInspect.Add_TwoConnectorVisualInspect_Query(self)
        ConnectorPhysicalInspect.Add_TwoConnectorPhysicalInspect_Query(self)
        ConnectorFunctionInspect.Add_TwoConnectorFunctInspect_Query(self)
        StandardConnectorInspect.Add_TwoStandConnectorInspect_Query(self)
        
        # Get the Connector overall status and update the units in use status 
        Connectors.Update_TwoConnectors_InUse_Status(Connectors)
        
        # Commit the ConnectorInspect data to the database
        ConnectorInspect.Add_TwoConnectorInspection_Query(self)
        ConnectorInspect.Add_TwoConnectorInspector_Query(self)
        ConnectorInspect.Add_TwoConnectorLocation_Query(self)
        
        # First check if the unit has been packaged for reservice to add report to db
        if Bool_Flag.Get_ConnectorRetired_Bool_Value(Bool_Flag) is True:
            # Get the two connectors data
            aLastTwoConnectorInspectList = ConnectorsRetiredReport.Get_Last_Two_Connectors_Data(ConnectorsRetiredReport)
            
            for i in range(2):
                self.intConnectorInspectionID = aLastTwoConnectorInspectList[i][0]
                ConnectorsRetiredReport.Add_Connector_RetiredReport_Query(self)
        
    def Submit_Standard_Inspection_BelayDevice(self):
        """ 
        Function Name: Submit_Standard_Inspection_BelayDevice
        Function Purpose: This function is executed once the user clicks on the submit button and all the standard
        inspection data cached arrays will be pulled and dumped into the the database
        """    
        # Set the global BelayDevice Attributes
        BelayDevices.Update_BelayDevices_Inspect_Dates(BelayDevices)        
        
        # Commit the BelayDevice Inspection data to the database
        BelayDeviceVisSelection.Add_BelayDeviceVisSelection_Query(self)
        BelayDevicePhysSelection.Add_BelayDevicePhysSelection_Query(self)
        BelayDeviceFunctSelection.Add_BelayDeviceFunctSelection_Query(self)
        BelayDevicePlasticVisSelection.Add_BelayDeviceVis_Plastic_Selection_Query(self)
        BelayDevicePlasticPhysSelection.Add_BelayDevicePhys_Plastic_Selection_Query(self)
        BelayDevicePlasticFunctSelection.Add_BelayDevicePlasticFunctSelection_Query(self)
        BelayDeviceVisualInspect.Add_BelayDeviceVisualInspect_Query(self)
        BelayDevicePhysicalInspect.Add_BelayDevicePhysicalInspect_Query(self)
        BelayDeviceFunctionInspect.Add_BelayDeviceFunctInspect_Query(self)
        StandardBelayDeviceInspect.Add_StandBelayDeviceInspect_Query(self)
        
        # Get the BelayDevice overall status and update the units in use status 
        BelayDevices.Update_BelayDevices_InUse_Status(BelayDevices)
        
        # Commit the BelayDeviceInspect data to the database
        BelayDeviceInspect.Add_BelayDeviceInspection_Query(self)
        BelayDeviceInspect.Add_BelayDeviceInspector_Query(self)
        BelayDeviceInspect.Add_BelayDeviceLocation_Query(self)
        
        # Check if the unit has been packaged for reservice to add report to db
        if Bool_Flag.Get_BelayDeviceRetired_Bool_Value(Bool_Flag) is True:
            BelayDevicesRetiredReport.Add_BelayDevice_RetiredReport_Query(self)

    def Submit_Standard_Inspection_Rope(self):
        """ 
        Function Name: Submit_Standard_Inspection_Rope
        Function Purpose: This function is executed once the user clicks on the submit button and all the standard
        inspection data cached arrays will be pulled and dumped into the the database
        """    
        # Set the global BelayDevice Attributes
        Ropes.Update_Ropes_Inspect_Dates(Ropes)        
        
        # Commit the BelayDevice Inspection data to the database
        RopeVisSelection.Add_RopeVisSelectList_Query(self)
        RopePhysSelection.Add_RopePhysSelectList_Query(self)
        RopeVisualInspect.Add_RopeVisualInspect_Query(self)
        RopePhysicalInspect.Add_RopePhysicalInspect_Query(self)
        StandardRopeInspect.Add_StandRopeInspect_Query(self)
        
        # Get the BelayDevice overall status and update the units in use status 
        Ropes.Update_Ropes_InUse_Status(Ropes)
        
        # Commit the BelayDeviceInspect data to the database
        RopeInspect.Add_RopeInspection_Query(self)
        RopeInspect.Add_RopeInspector_Query(self)
        RopeInspect.Add_RopeLocation_Query(self)
        
        # Check if the unit has been packaged for reservice to add report to db
        if Bool_Flag.Get_RopeRetired_Bool_Value(Bool_Flag) is True:
            RopesRetiredReport.Add_Rope_RetiredReport_Query(self)

    def Reset_Object_Lists(self):
        """ 
        Function Name: Reset_Object_Lists
        Function Purpose: This function is executed once all the data has been pushed to the db and the list objects 
        need to be reset.
        """     
        Start_Menu.Set_Default_Bool_Values(self)
        
        # Delete the stored data in the class attributes
        StandardConnectorInspect.Delete_Connector_Data(self)       
        StandardBelayDeviceInspect.Delete_BelayDevice_Data(self)
        StandardRopeInspect.Delete_Rope_Data(self)
        Start_Menu.Delete_Obj_Lists(self)        
                                
    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Expose the window widget to the user
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """     
        # Hide the current window
        self.Exit()  

        # Show the main window after the new window is closed
        RopeInspection()

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
                

#######################################################################################################
# Connectors Menu Class
#######################################################################################################        

class Connectors_Menu(tk.Tk):
    """
    Class Name: Connectors_Menu
    Class Description: This class is for the Connectors main menu. 
    """
    def __init__(self):
        # Load the data from the database
        Start_Menu.Load_Obj_Lists(self)
        
        # Create the root tkinter variable
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (560/2)     
        self.y = (self.heightSize/2) - (330/2)    
                        
        # Create the Window attributes
        self.WindowTitle = self.title("Connector Menu")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (560, 330, self.x, self.y))
        self.WindowSize = self.resizable(False, False)
        
        # Create the frame for the buttons
        self.btnFrame = LabelFrame(self, text='Menu Selection')
        self.btnFrame.place(x=160, y=15, width=250, height=285)

        # Create the Buttons
        self.btnNewInspect = Button(self.btnFrame, width=25, text = "New Inspection", command=lambda:Connectors_Menu.Open_NewInspection(self))        
        self.btnViewFutureInspectDate = Button(self.btnFrame, width=25, text = "View Future Inspection Dates", command=lambda:Connectors_Menu.Open_ViewLastNext_InspectionDates(self))
        self.btnViewConnectorDates = Button(self.btnFrame, width=25, text = "View Connector Dates", command=lambda:Connectors_Menu.Open_ConnectorDates(self))
        self.btnViewConnectorInfo = Button(self.btnFrame, width=25, text = "View Connector Info", command=lambda:Connectors_Menu.Open_ConnectorInfo(self))
        self.btnViewConnectorWallLocation = Button(self.btnFrame, width=25, text = "View Connector Wall Locations", command=lambda:Connectors_Menu.Open_Connector_WallLocations(self))
        self.btnDownloadReport = Button(self.btnFrame, width=25, text = "Download Reports", command=lambda:Connectors_Menu.Open_DownloadReports(self))
        self.btnOpenReport = Button(self.btnFrame, width=25, text = "Open Reports", command=lambda:Connectors_Menu.Open_Records_Dir(self))
        self.btnExit = Button(self.btnFrame, width=25, text = "Home", command=lambda:Connectors_Menu.Exit(self))

        # Create the button grid
        self.btnNewInspect.grid(row=1, column=1, padx=29, pady=3)
        self.btnViewFutureInspectDate.grid(row=2, column=1, pady=3)
        self.btnViewConnectorDates.grid(row=3, column=1, pady=3)
        self.btnViewConnectorInfo.grid(row=4, column=1, pady=3)
        self.btnViewConnectorWallLocation.grid(row=5, column=1, pady=3)
        self.btnDownloadReport.grid(row=6, column=1, pady=3)
        self.btnOpenReport.grid(row=7, column=1, pady=3)
        self.btnExit.grid(row=8, column=1, pady=3)
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()  
        
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)   
        
        # Send the user back to the main menu        
        Start_Menu()        

    def Open_NewInspection(self):
        """ 
        Function Name: Open_NewInspection
        Function Purpose: This function is executed if the user clicks new inspection button. The 
        call is to the inspection class and will execute and add a new inspection to the database.
        """
        # Delete the root window
        self.destroy()
        
        # Open the New Inspection Window
        ConnectorSelection()

    def Open_ViewLastNext_InspectionDates(self):
        """ 
        Function Name: Open_ViewLastNext_InspectionDates
        Function Purpose: This function is executed if the user clicks view Connector Next/Last inspection dates button. 
        """
        # Delete the root window
        self.destroy()
        
        # Determine the Caller_ID based on the class
        Caller_ID = "Connector"
        
        # Open the add new location window
        View_LastNext_InspectDate(Class_CallerID=Caller_ID)
        
    def Open_ConnectorDates(self):
        """ 
        Function Name: Open_ConnectorDates
        Function Purpose: This function is executed if the user clicks View Connector Dates button. 
        """
        # Delete the root window
        self.destroy()
        
        # Determine the Caller_ID based on the class
        Caller_ID = "Connector"
                        
        # Open the view location window
        View_ItemDates(Class_CallerID=Caller_ID)  

    def Open_ConnectorInfo(self):
        """ 
        Function Name: Open_ConnectorInfo
        Function Purpose: This function is executed if the user clicks View Connector Info button. 
        """
        # Delete the root window
        self.destroy()
        
        # Determine the Caller_ID based on the class
        Caller_ID = "Connector"
                        
        # Open the view location window
        View_Device_Info(Class_CallerID=Caller_ID) 
        
    def Open_Connector_WallLocations(self):
        """ 
        Function Name: Open_Connector_WallLocations
        Function Purpose: This function is executed if the user clicks View Connector Wall Locations button. 
        """
        # Delete the root window
        self.destroy()
        
        # Determine the Caller_ID based on the class
        Caller_ID = "Connector"
                        
        # Open the view location window
        View_Item_WallLocations(Class_CallerID=Caller_ID)  

    def Open_AutoBelay_OutOfService(self):
        """ 
        Function Name: Open_AutoBelay_OutOfService
        Function Purpose: This function is executed if the user clicks View Connector Out For Reservice button. 
        """
        # Delete the root window
        self.destroy()
        
        # Open the view location window
        View_AutoBelay_WallLocations() 
        
    def Open_Records_Dir(self):
        """ 
        Function Name: Open_Records_Dir
        Function Purpose: This function is executed if the user clicks Open Report Information button. 
        """
        # Open the send reports window
        Records.Open_Records_Dir()   
        
    def Open_DownloadReports(self):
        """ 
        Function Name: Open_DownloadReports
        Function Purpose: This function executes whenever the user clicks the 'Download Reports' button. This function
        pulls from the db specific views and downloads the views to a desired directory. Each file is saved as an excel
        file. 
        """
        Queries.Download_Files(Queries, user_triggered=True)       
        messagebox.showwarning(message='SUCCESSFUL DOWNLOAD \n\n All files have been downloaded to the Records Directory.', icon='warning')
        
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed if the user clicks exit button. The main menu will
        exit once this button is clicked and will return the user to the login page.
        """
        # Delete the root window
        self.destroy()
        
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)  
        
        # Send the user back to the main menu   
        Start_Menu()
        
                        
#######################################################################################################
# Connector Inspection Class
#######################################################################################################

class ConnectorInspection(tk.Tk): 
    """
    Class Name: ConnectorInspection
    Class Description: This class is to conduct connector inspections.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new Connector inspection. User must click
        'Next' Button in order to progress to the next inspection type. A Visual, Physical, and Functional inspection
        must be performed to complete the inspection.
        """
        # Load the data from the database
        # Start_Menu.Load_Obj_Lists(self) # Make sure to comment this out after testing
        
        # Create the root tkinter var and init
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk window 
        self.x = (self.widthSize/2) - (805/2)     
        self.y = (self.heightSize/2) - (625/2)          
        
        # Create the Window attributes                
        self.title("Connector Inspection")
        self.geometry('%dx%d+%d+%d' % (805, 625, self.x, self.y))
        self.resizable(False, False)

        # Load the query selection widget for Search by serial or bumper num
        self.Selection_Widget()
        
        # Create the frame fields       
        self.visCheckListFrame = tk.LabelFrame(self, text="Visual Inspection Results")
        self.visCheckListFrame.place(x=95, y=135, width=300, height=200)
        self.physCheckListFrame = tk.LabelFrame(self, text="Physical Inspection Results")
        self.physCheckListFrame.place(x=405, y=135, width=300, height=200)
        self.functCheckListFrame = tk.LabelFrame(self, text="Functional Inspection Results")
        self.functCheckListFrame.place(x=95, y=340, width=610, height=125)
        self.commFrame = tk.LabelFrame(self, text="Inspection Comment")
        self.commFrame.place(x=95, y=470, width=610, height=100)
                        
        # Create the label for the checkboxes
        self.lblConnectVisualStatus = tk.Label(self.visCheckListFrame, text="Visual Status:")
        self.lblConnectPhysicalStatus = tk.Label(self.physCheckListFrame, text="Physical Status:")
        self.lblConnectFunctStatus = tk.Label(self.functCheckListFrame, text="Function Status:")
                        
        # Create the label locations
        self.lblConnectVisualStatus.place(x=5, y=140)
        self.lblConnectPhysicalStatus.place(x=5, y=140)
        self.lblConnectFunctStatus.place(x=155, y=65)

        # Create the drop down menu list for each attribute
        self.dropConnectVisStatus = ttk.Combobox(self.visCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropConnectPhysStatus = ttk.Combobox(self.physCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropConnectFunctStatus = ttk.Combobox(self.functCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        
        # Create the drop down menu size for each attribute
        self.dropConnectVisStatus.configure(width=20)
        self.dropConnectPhysStatus.configure(width=20)
        self.dropConnectFunctStatus.configure(width=20)
        
        # Create the grid for the drop down menu list objects   
        self.dropConnectVisStatus.place(x=125, y=140)  
        self.dropConnectPhysStatus.place(x=125, y=140)  
        self.dropConnectFunctStatus.place(x=290, y=65)  

        # Create the master list for the metallic and functional inspection types
        self.selectItems = Metallic.astrMetallicInspectionDesc 
        self.functItems = CarabinerFunction.astrCarabinerFunctionDesc
        
        # Create the checkbox lists for visual, physical, and functional
        self.visCheckList = [] 
        self.physCheckList = []
        self.functCheckList = []
        
        # Create an empty list to store selected items
        self.checkboxVisStates = {}
        self.checkboxPhysStates = {}
        self.checkboxFuncStates = {}

        # Create the checkbox list
        self.Create_Check_Buttons(self.selectItems, self.visCheckListFrame, ConnectorVisSelection.astrConnectorVisMetalSelect, self.visCheckList, self.checkboxVisStates, self.Get_VisCheckbox_List, "visual")
        self.Create_Check_Buttons(self.selectItems, self.physCheckListFrame, ConnectorPhysSelection.astrConnectorPhysMetalSelect, self.physCheckList, self.checkboxPhysStates, self.Get_PhysCheckbox_List, "physical")
        self.Create_Check_Buttons(self.functItems, self.functCheckListFrame, ConnectorFunctSelection.astrConnectorFunctSelect, self.functCheckList, self.checkboxFuncStates, self.Get_FuncCheckbox_List, "functional")

        # First check if the selection values have been assigned
        self.Set_Previous_Checkbox_List(ConnectorVisSelection.astrConnectorVisMetalSelect, self.visCheckList, self.selectItems)
        self.Set_Previous_Checkbox_List(ConnectorPhysSelection.astrConnectorPhysMetalSelect, self.physCheckList, self.selectItems)
        self.Set_Previous_Checkbox_List(ConnectorFunctSelection.astrConnectorFunctSelect, self.functCheckList, self.functItems)
                
        # Check if the cache values for any drop menus have been previously selected and set the values
        if Bool_Flag.blnConnectorPersistFlag == True:
            self.Set_Previous_Drop_List(ConnectorVisSelection.strConnectorVisStatus, self.dropConnectVisStatus)
            self.Set_Previous_Drop_List(ConnectorPhysSelection.strConnectorPhysStatus, self.dropConnectPhysStatus)
            self.Set_Previous_Drop_List(ConnectorFunctSelection.strConnectorFunctStatus, self.dropConnectFunctStatus)

        # Create the comment field
        self.commInput = tk.Text(self.commFrame, state='normal')
        self.commInput.grid(row=0, column=0, padx=5, pady=4)
        self.commInput.configure(width=74, height=4, padx=0)
        
        # Create the buttons
        self.btnBack = Button(self, text="Back", width=10, command=self.Back)
        self.btnClear = Button(self, text="Clear", width=10, command=self.Clear)
        self.btnExit = Button(self, text="Exit", width=10, command=self.Exit)
        self.btnNext = Button(self, text="Next", width=10, command=self.Next)
            
        # Create the position of the button
        self.btnBack.place(x=160, y=585)
        self.btnExit.place(x=290, y=585) 
        self.btnClear.place(x=420, y=585)
        self.btnNext.place(x=550, y=585) 
        
        # Keep the window open while the user is interacting with the widgets
        self.mainloop()

        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the stored data in the class attributes
        StandardConnectorInspect.Delete_Connector_Data(self)
                        
        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)

        # Show the main window after the new window is closed
        Connectors_Menu()      

    def Selection_Widget(self):
        """ 
        Function Name: Selection_Widget
        Function Purpose: This function populates the search by widget for Serial or Bumper Num search.
        """           
        # Create the first frame to hold the input fields
        self.typeFrame = tk.LabelFrame(self, text="Selected Connector")
        self.typeFrame.place(x=95, y=10, width=610, height=120)

        # Create the labels 
        self.lblConnectSerial = Label(self.typeFrame, text="Serial ID:")
        self.lblConnectBumper = Label(self.typeFrame, text="Bumper ID:")
        self.lblConnectType = tk.Label(self.typeFrame, text="Connector Type:")

        # Create the label locations
        self.lblConnectSerial.place(x=197, y=5)
        self.lblConnectBumper.place(x=183, y=35)
        self.lblConnectType.place(x=155, y=65)

        # Create the entry input box
        self.SerialNumOut = Entry(self.typeFrame, width=30, state='normal')
        self.BumperNumOut = Entry(self.typeFrame, width=30, state='normal')
        self.ConnectType = Entry(self.typeFrame, width=30, state='normal')
        
        # Set the values selected from the user
        self.SerialNumOut.insert(0, Connectors.strSerialNum)
        self.BumperNumOut.insert(0, Connectors.strBumperNum)
        self.ConnectType.insert(0, Connectors.strDeviceType)
        
        # Configure the state to disabled
        self.SerialNumOut.configure(state='disabled')
        self.BumperNumOut.configure(state='disabled')
        self.ConnectType.configure(state='disabled')
        
        # Create the grid for all of the entry input fields
        self.SerialNumOut.place(x=275, y=5)
        self.BumperNumOut.place(x=275, y=35)
        self.ConnectType.place(x=275, y=65) 

    def Create_Check_Buttons(self, selectItems, checkListFrame, arrayObject, checkList, checkboxStates, callback, strInsType):
        """ 
        Function Name: Create_Check_Buttons
        Function Description: This helper method to create the checkbox buttons
        """
        if strInsType == "visual" or strInsType == "physical":
            maxColPerRow = 2
        else:
            maxColPerRow = 4

        for index, item in enumerate(selectItems):
            # Check if the item was previously selected (exists in arrayObject)
            is_selected = item in arrayObject
            var = tk.StringVar(value='1' if is_selected else '0')
            checkList.append(var)

            # Use a lambda function to capture the current item in the loop
            checkBox = tk.Checkbutton(checkListFrame, text=item, variable=var, onvalue='1', offvalue='0', 
                                    command=lambda item=item, var=var: callback(item, var))
            
            # Store the variable in the checkboxStates dictionary
            checkboxStates[item] = var

            # Calculate the row and column position of checkbutton based on index and max columns 
            rowPosition = index // maxColPerRow
            colPosition = index % maxColPerRow
            checkBox.grid(row=rowPosition, column=colPosition, sticky="w", padx=10)

    def Set_Previous_Checkbox_List(self, selectList, checkboxList, paramsList):
        """
        Function Name: Set_Vis_Previous_Checkbox_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the checkboxes from the cache array list for all checkboxes.
        """   
        # First check if the cache values have been assigned
        if len(selectList) == 0:
            # Check the first item of the list    
            checkboxList[0].set('1')
        else:
            # Set the Selection data to the objects in the window
            for i, item in enumerate(paramsList):
                if item in selectList:
                    checkboxList[i].set('1')

    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)

    def Get_VisCheckbox_List(self, item, var):
        """
        Function Name: Get_VisCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':            
            self.Update_Checkbox_List(self.visCheckList, item, self.checkboxVisStates, "visual", ConnectorVisSelection.astrConnectorVisMetalSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.visCheckList, item, self.checkboxVisStates, "visual", ConnectorVisSelection.astrConnectorVisMetalSelect)
            
    def Get_PhysCheckbox_List(self, item, var):
        """
        Function Name: Get_PhysCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':          
            self.Update_Checkbox_List(self.physCheckList, item, self.checkboxPhysStates, "physical", ConnectorPhysSelection.astrConnectorPhysMetalSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.physCheckList, item, self.checkboxPhysStates, "physical", ConnectorPhysSelection.astrConnectorPhysMetalSelect)

    def Get_FuncCheckbox_List(self, item, var):
        """
        Function Name: Get_FuncCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':          
            self.Update_Checkbox_List(self.functCheckList, item, self.checkboxFuncStates, "functional", ConnectorFunctSelection.astrConnectorFunctSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.functCheckList, item, self.checkboxFuncStates, "functional", ConnectorFunctSelection.astrConnectorFunctSelect)

    def Update_Checkbox_List(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Update_Checkbox_List
        Function Purpose: Updates checkbox states and persistent data with special handling for the default (first) item.
        """
        # Identify the correct item list based on the selectionKey
        itemList = self.determine_item_list(selectionKey)
        
        # Check if the selected item is in the itemList
        if item not in itemList:
            print(f"Error: Item '{item}' not found in itemList for selectionKey '{selectionKey}'.")
            return  # Exit the function to avoid further errors

        # Find the index of the selected item in the item list
        selectedIndex = itemList.index(item)

        # If the first item is selected, deselect all others
        if selectedIndex == 0:
            for i in range(1, len(checkboxList)):
                checkboxList[i].set('0')
                checkboxStates[itemList[i]] = '0'
        else:
            # If any other item is selected, deselect the first item
            checkboxList[0].set('0')
            checkboxStates[itemList[0]] = '0'

            # Update the state for the selected item
            checkboxList[selectedIndex].set('1')
            checkboxStates[item] = '1'

        # Update the persistent array object based on the current selection state
        selectedItemsList = [item for i, item in enumerate(itemList) if checkboxList[i].get() == '1']
        self.Update_Persistent_Array(arrayObject, selectedItemsList)

    def determine_item_list(self, selectionKey):
        """
        Determines the correct item list based on the selection key.
        """
        if 'functional' in selectionKey:
            return self.functItems
        else:
            return self.selectItems
        
    def Handle_Deselection(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Handle_Deselection
        Function Purpose: This function is called when a checkbox is deselected.
        """
        # # For now, I'm just printing a message. You can modify this to implement the desired behavior.
        # print(f"Checkbox {item} was deselected!")

        # If you want to remove an item from a persisted list or dictionary upon deselection, you can do so here:
        checkboxStates.pop(item, None)
        arrayObject.remove(item)
        
    def Update_Persistent_Array(self, arrayObject, selectedItemsList):
        """
        Function Name: Update_Persistent_Array
        Function Description: This function updates the arrayObject with the selected items list, while keeping existing persisted data.
        """
        # print("Selected Items:", selectedItemsList)
        # print("Before update:", arrayObject)

        selectedSet = set(selectedItemsList)
        arraySet = set(arrayObject)

        # Find items to add and remove
        toAdd = selectedSet - arraySet
        toRemove = arraySet - selectedSet

        for item in toAdd:
            arrayObject.append(item)
        for item in toRemove:
            arrayObject.remove(item)

    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.', icon='warning')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate
    
    def Check_Checkbox_Input(lstCheckBox, strFieldDesc):
        """
        Function Name: Check_Checkbox_Input
        Function Purpose: This function is called whenever a checkbox is present and needs to check if any of the entries are empty. If so,
        warn the user.
        """    
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)
            
        try:
            for i in range(0, len(lstCheckBox)):
                if lstCheckBox[i].get() == '1':
                    # Set blnValidated to True
                    blnValidate = True

            # Check if the blnValidated flag is true or false and warn the user if the entire field is empty
            if blnValidate is True:
                pass
            else:
                messagebox.showwarning(title='ERROR', message='%s field should not be empty. Please verify your selection.'%(strFieldDesc), icon='warning')
                blnValidate = False
                # Select the first checkbox
                lstCheckBox[0].set('1')

        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate  
    
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        def validate_field(input_field, checklist, field_name):
            if not ConnectorInspection.Check_Input(input_field.get()):
                input_field.focus()
                return False

            if not ConnectorInspection.Check_Checkbox_Input(checklist, field_name):
                return False

            return True

        # Define field names
        strVisField = "Visual Result"
        strPhysField = "Physical Result"
        strFunctField = "Functional Result"

        # Validate each field
        if not validate_field(self.dropConnectVisStatus, self.visCheckList, strVisField):
            return False

        if not validate_field(self.dropConnectPhysStatus, self.physCheckList, strPhysField):
            return False

        if not validate_field(self.dropConnectFunctStatus, self.functCheckList, strFunctField):
            return False

        # All validations passed
        return True
        
    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        """       
        # Declare Local Variables
        sqlConnectorVisSel = ("TConnectorVisMetalSelects", "intConnectorVisMetalSelectID", "strConnectorVisMetalSelect")
        sqlConnectorPhysSel = ("TConnectorPhysMetalSelects", "intConnectorPhysMetalSelectID", "strConnectorPhysMetalSelect")
        sqlConnectorFunctSel = ("TConnectorFunctSelects", "intConnectorFunctSelectID", "strConnectorFunctSelect")
        sqlConnectorVisIns = ("TConnectorVisualInspections", "intConnectorVisualInspectionID")
        sqlConnectorPhysIns = ("TConnectorPhysicalInspections", "intConnectorPhysicalInspectionID") 
        sqlConnectorFunctIns = ("TConnectorFunctionInspections", "intConnectorFunctionInspectID") 
        sqlConnectorStandIns = ("TStandardConnectorInspections", "intStandardConnectorInspectionID")

        # Check if the comment is empty. If not, pass in the values. If empty, pass in 'None'
        if self.commInput.get("1.0", "end-1c") != "":
            self.strComment = str(self.commInput.get("1.0", "end-1c"))
            self.strComment += "; "
            # Add the comment to the AutoBelay Comment object
            ConnectorInspect.strComment = ''.join(self.strComment)
        else:
            self.strComment = 'None'
            ConnectorInspect.strComment = self.strComment
        
        # Get the selected values
        ConnectorVisMetSelect = self.Get_Combined_Selection(ConnectorVisSelection.astrConnectorVisMetalSelect, self.selectItems[0])
        ConnectorPhysMetSelect = self.Get_Combined_Selection(ConnectorPhysSelection.astrConnectorPhysMetalSelect, self.selectItems[0])
        ConnectorFunctSelect = self.Get_Combined_Selection(ConnectorFunctSelection.astrConnectorFunctSelect, self.functItems[0])

        # # Display the string representation
        # print(ConnectorVisMetSelect) 
        # print(ConnectorPhysMetSelect)
        # print(ConnectorFunctSelect)
        
        # Get the status for the visual, physical selection
        ConnectorVisStatus = self.dropConnectVisStatus.get()
        ConnectorPhysStatus = self.dropConnectPhysStatus.get()
        ConnectorFunctStatus = self.dropConnectFunctStatus.get()
        
        # Get the ID of the selected status item
        ConnectorVisStatusID = InspectionStatus.astrInspectionStatusDesc.index(ConnectorVisStatus) + 1
        ConnectorPhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(ConnectorPhysStatus) + 1
        ConnectorFunctStatusID = InspectionStatus.astrInspectionStatusDesc.index(ConnectorFunctStatus) + 1
        
        # Get the type of selection, either physical, visual 
        VisInsTypeDesc = InspectionType.astrInspectionTypeDesc[0]
        PhysInsTypeDesc = InspectionType.astrInspectionTypeDesc[1]
        FunctInsTypeDesc = InspectionType.astrInspectionTypeDesc[2]

        # Get the ID of the selected Type item
        VisInsTypeID = InspectionType.astrInspectionTypeDesc.index(VisInsTypeDesc) + 1
        PhysInsTypeID = InspectionType.astrInspectionTypeDesc.index(PhysInsTypeDesc) + 1
        FunctInsTypeID = InspectionType.astrInspectionTypeDesc.index(FunctInsTypeDesc) + 1

        # Get the list of items selected and attach them to the selection object for Visual and Physical Selection
        ConnectorVisMetalSelectID = self.Get_Or_Create_ID(ConnectorVisMetSelect, sqlConnectorVisSel)              
        ConnectorPhysMetalSelectID = self.Get_Or_Create_ID(ConnectorPhysMetSelect, sqlConnectorPhysSel)
        ConnectorFunctSelectID = self.Get_Or_Create_ID(ConnectorFunctSelect, sqlConnectorFunctSel)
                            
        # Get the ID's for the base objects in each class
        ConnectorVisualInsID = self.Get_Max_Primary_Key(sqlConnectorVisIns[0], sqlConnectorVisIns[1])
        ConnectorPhysicalInsID = self.Get_Max_Primary_Key(sqlConnectorPhysIns[0], sqlConnectorPhysIns[1])  
        ConnectorFunctionInspectID = self.Get_Max_Primary_Key(sqlConnectorFunctIns[0], sqlConnectorFunctIns[1])      
        StandardConnectorInspectionID = self.Get_Max_Primary_Key(sqlConnectorStandIns[0], sqlConnectorStandIns[1])

        # Assign the local object to the class objects
        cvs = ConnectorVisSelection(ConnectorVisMetalSelectID, ConnectorVisMetSelect, ConnectorVisStatus)
        cps = ConnectorPhysSelection(ConnectorPhysMetalSelectID, ConnectorPhysMetSelect, ConnectorPhysStatus)
        cfs = ConnectorFunctSelection(ConnectorFunctSelectID, ConnectorFunctSelect, ConnectorFunctStatus)        

        # Commit the data to the visual inspection
        ConnectorVisSelection.intConnectorVisMetalSelectID = cvs.intConnectorVisMetalSelectID
        ConnectorVisSelection.strConnectorVisMetalSelect = cvs.strConnectorVisMetalSelect
        ConnectorVisSelection.strConnectorVisStatus = cvs.strConnectorVisStatus
        ConnectorVisualInspect.aConnectorVisualCache = (ConnectorVisualInsID, Connectors.intConnectorID, VisInsTypeID, cvs.intConnectorVisMetalSelectID, ConnectorVisStatusID)

        # Commit the data to the physical inspection
        ConnectorPhysSelection.intConnectorPhysMetalSelectID = cps.intConnectorPhysMetalSelectID
        ConnectorPhysSelection.strConnectorPhysMetalSelect = cps.strConnectorPhysMetalSelect
        ConnectorPhysSelection.strConnectorPhysStatus = cps.strConnectorPhysStatus
        ConnectorPhysicalInspect.aConnectorPhysicalCache = (ConnectorPhysicalInsID, Connectors.intConnectorID, PhysInsTypeID, cps.intConnectorPhysMetalSelectID, ConnectorPhysStatusID)    

        # Commit the data to the function inspection
        ConnectorFunctSelection.intConnectorFunctSelectID = cfs.intConnectorFunctSelectID
        ConnectorFunctSelection.strConnectorFunctSelect = cfs.strConnectorFunctSelect
        ConnectorFunctSelection.strConnectorFunctStatus = cfs.strConnectorFunctStatus
        ConnectorFunctionInspect.aConnectorFunctCache = (ConnectorFunctionInspectID, Connectors.intConnectorID, FunctInsTypeID, cfs.intConnectorFunctSelectID, ConnectorFunctStatusID)  

        # Commit the data to the standard inspection
        StandardConnectorInspect.aStandardConnectorInsCache = (StandardConnectorInspectionID, ConnectorVisualInsID, ConnectorPhysicalInsID, ConnectorFunctionInspectID)

    def Get_Combined_Selection(self, persisted_array, default_value):
        """
        Function Name: Get_Combined_Selection
        Function Purpose: This function combines the array elements into a comma-separated string,
        and Connectors the case when the persisted array is empty by setting a default value.
        """
        if len(persisted_array) == 0:
            return default_value
        else:
            return ",".join(persisted_array)
        
    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
    
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlStatement[0], sqlStatement[1]))    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
    
    def Next(self):
        """ 
        Function Name: Next
        Function Purpose: This function is executed once the user clicks on the "Next" button. Once the inputs 
        are validated, the inspection results loads the user selected data and is retained at the object class locations 
        before committing to the database. If all inputs are valid and confirmed by the user, the next stage of inspections is executed.
        """
        global blnValidate
        blnValidate = bool(False)             
        
        # First check if the input is empty, if so, notify the user the input needs attention 
        blnValidate = self.Validate_InputFields()
        
        # If status is true then proceed to update the result field, else, reset the fields
        if blnValidate is True:
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to next inspection component?', icon='question') is True:
                # print(ConnectorVisSelection.astrConnectorVisMetalSelect)
                # print(ConnectorPhysSelection.astrConnectorPhysMetalSelect) 
                # print(ConnectorFunctSelection.astrConnectorFunctSelect)
                # Load the user data and prep the data for db dump
                self.Pull_UserInput()     
                
                # Set the global class bool to true
                Bool_Flag.Set_Connector_Bool_Value_True(Bool_Flag)
                
                # Go to the next inspection component
                self.Next_Inspection()
            else:
                # Check if the user would like to reset the fields
                if messagebox.askyesno(message='ATTENTION! \n\n Would you like to reset the fields?', icon='question') is True:
                    # Clear the input fields and after data is submitted to the database
                    self.Clear()                

    def Clear(self):
        """ 
        Function Name: Clear
        Function Purpose: This function is executed once the user clicks on the Clear button inside the
        frame. If the user clicks 'Clear', all data is set back to default.
        """     
        # Set the list objects first element to the drop click object
        self.dropConnectVisStatus.set("")
        self.dropConnectVisStatus.set("")
        self.dropConnectFunctStatus.set("")
        
        # Reset the checkboxes to empty selections
        BaseFunctions.Deselect_All_Checkbox(self.visCheckList)
        BaseFunctions.Deselect_All_Checkbox(self.physCheckList)
        BaseFunctions.Deselect_All_Checkbox(self.functCheckList)

        # Set the first item in the list to the first checkbox item displayed
        self.visCheckList[0].set('1')
        self.physCheckList[0].set('1')
        self.functCheckList[0].set('1')

        # Clear the class objects
        StandardConnectorInspect.Reset_Connector_Data(self)
        StandardConnectorInspect.Delete_Connector_Data(self)
        
        # Delete the comment field 
        self.commInput.delete("1.0", "end-1c") 
        
    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Expose the window widget to the user
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """     
        # Hide the current window
        self.Exit()  

        # Show the main window after the new window is closed
        ConnectorSelection()

    def Next_Inspection(self):
        """ 
        Function Name: Next_Inspection
        Function Purpose: This function is executed once the user clicks on Next button to move to the nex inspection
        type window. Withdraw the parent window and load the new window.
        """           
        # Hide the main window
        self.Exit()  

        # Check if the rope system is complex
        if (Bool_Flag.blnComplexWith_Two_ConnectorFlag is True) and (Bool_Flag.blnComplexWithBelayDeviceFlag is True):
            BelayDeviceSelection()
        elif (Bool_Flag.blnComplexWith_Two_ConnectorFlag is True):
            RopeInspection()     
        elif (Bool_Flag.blnComplexWithConnectorFlag is True) and (Bool_Flag.blnComplexWithBelayDeviceFlag is True):
            BelayDeviceSelection()                     
        elif (Bool_Flag.blnComplexWithConnectorFlag is True):
            RopeInspection()
        else:
            # Display the results of the inspection
            ConnectorInspectionResults()
        
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        

#######################################################################################################
# Connector Selection Class
#######################################################################################################   

class ConnectorSelection(tk.Tk, Connectors):
    """
    Class Name: ConnectorSelection
    Class Description: This class is to conduct Connector Selection.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new Connector Selection. User must click
        'Next' Button in order to progress to the next inspection type.
        """
        # Load the data from the database
        # Start_Menu.Load_Obj_Lists(self) # Make sure to comment this out after testing
                
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (650/2)     
        self.y = (self.heightSize/2) - (410/2)          
        
        # Create the Window attributes                
        self.title("Connector Selection")
        self.geometry('%dx%d+%d+%d' % (650, 410, self.x, self.y))
        self.resizable(False, False)

        # Load the query selection widget
        self.Selection_Widget()
        
        # Create the frame fields
        self.typeFrame = tk.LabelFrame(self, text="Additional Info")
        self.typeFrame.place(x=100, y=140, width=450, height=200)
                
        # Create the label for the checkboxes
        self.lblConnectorLocation = tk.Label(self.typeFrame, text="Connector Location:")
        self.lblInUse = tk.Label(self.typeFrame, text="Device In Use:")
        self.lblQuestion = tk.Label(self.typeFrame, text="Can't find what you're looking for?")
                        
        # Create the label locations
        self.lblConnectorLocation.place(x=35, y=15)
        self.lblInUse.place(x=70, y=55)
        self.lblQuestion.place(x=125, y=95)

        # Create the drop down menu list for each attribute
        self.dropConnectorLocation = ttk.Combobox(self.typeFrame, values=WallLocation.astrWallLocationDesc, state='readonly')
        self.dropInUse = ttk.Combobox(self.typeFrame, values=['Yes', 'No'], state='readonly')
        
        # Create the drop down menu size for each attribute
        self.dropConnectorLocation.configure(width=25)
        self.dropInUse.configure(width=25)
        
        # Create the grid for the drop down menu list objects
        self.dropConnectorLocation.place(x=190, y=15)  
        self.dropInUse.place(x=190, y=55)  

        if Bool_Flag.blnComplexWithConnectorFlag is True:
            # Disable the drop location if this class is called from ropes inspection
            self.dropConnectorLocation.set(WallLocation.strWallLocationDesc)
            self.dropConnectorLocation.configure(state='disabled')
            self.dropInUse.set("Yes")
            self.dropInUse.configure(state='disabled')
            
        # Check if the cache values for any drop menus have been previously selected and set the values
        if Bool_Flag.blnConnectorPersistFlag == True:
            if (Bool_Flag.blnSerialNumRadioSelect == True):
                self.Set_Previous_Drop_List(Connectors.strSerialNum, self.dropConnectorSelection)
            else:
                self.objRadioValue.set("bumper")
                self.dropConnectorSelection["values"] = self.astrBumperNumList
                self.Set_Previous_Drop_List(Connectors.strBumperNum, self.dropConnectorSelection)
            self.Set_Previous_Drop_List(Connectors.strEquipInUse, self.dropInUse)
            self.Set_Previous_Drop_List(WallLocation.strWallLocationDesc, self.dropConnectorLocation)
            
        # Create the buttons
        self.btnUpdateConnectorInfo = Button(self.typeFrame, width=12, text = "Update Device", command=self.Update_Connectors_Info)
        self.btnAddConnector = Button(self.typeFrame, width=12, text="Add Connector", command=self.Add_Connector)
        self.btnAddLocation = Button(self.typeFrame, width=12, text = "Add Location", command=self.Add_Location)
        self.btnExit = Button(self, width=10, text="Back", command=self.Back)
        self.btnReset = Button(self, width=10, text="Reset",command=self.Reset)
        self.btnNext = Button(self, width=10, text="Next", command=self.Next)
            
        # Create the position of the button
        self.btnUpdateConnectorInfo.place(x=40, y=140)
        self.btnAddConnector.place(x=175, y=140) 
        self.btnAddLocation.place(x=310, y=140)
        self.btnExit.place(x=170, y=360) 
        self.btnNext.place(x=400, y=360) 
        self.btnReset.place(x=285, y=360)
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()

        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the object lists
        Start_Menu.Delete_Obj_Lists(self)

        if Bool_Flag.blnComplexWithConnectorFlag is True:
            # Return back to the rope selection window
            GymRopeSelection()
        else:
            Connectors_Menu()    

    def Selection_Widget(self):
        """ 
        Function Name: Selection_Widget
        Function Purpose: This function populates the search by widget for Serial or Bumper Num search.
        """           
        # Create the first frame to hold the input fields
        self.selectInput = LabelFrame(self, text="Select Connector")
        self.selectInput.place(x=100, y=35, width=450, height=100)

        # Create the labels 
        self.lblSearchByConnectorID = Label(self.selectInput, text="Query by Connector ID:")
        self.lblConnectorSelection = Label(self.selectInput, text="Connector ID Selection:")

        # Create the label locations
        self.lblSearchByConnectorID.place(x=19, y=5)
        self.lblConnectorSelection.place(x=18, y=40)

        # Create variables to hold the value of the selected radio button
        self.objRadioValue = tk.StringVar(value='serial')
        self.objComboValue = tk.StringVar()

        # List objects of serial and bumper values
        self.astrSerialNumList = self.astrSerialNumCache
        self.astrBumperNumList = self.astrBumperNumCache

        # Create the radio buttons
        self.rbSerial = tk.Radiobutton(self.selectInput, text="Serial Number", variable=self.objRadioValue, value="serial", command=self.Populate_Dropdown)
        self.rbBumper = tk.Radiobutton(self.selectInput, text="Bumper Number", variable=self.objRadioValue, value="bumper", command=self.Populate_Dropdown)

        # Place the radio buttons next to each other using .place()
        self.rbSerial.place(x=190, y=5)
        self.rbBumper.place(x=300, y=5)
                    
        # Create the entry input box
        self.dropConnectorSelection = ttk.Combobox(self.selectInput, values=self.astrSerialNumList, state='readonly')
        self.dropConnectorSelection.configure(width=25,)

        # Populate the dropdown based on the default radio button selection
        self.Populate_Dropdown()

        # Create the grid for all of the entry input fields
        self.dropConnectorSelection.place(x=190, y=40) 

    def Populate_Dropdown(self):
        """ 
        Function Name: Populate_Dropdown
        Function Purpose: This function populates the dropdown based on the radio button selection.
        """           
        if self.objRadioValue.get() == "serial":
            self.dropConnectorSelection["values"] = self.astrSerialNumList
        else:
            self.dropConnectorSelection["values"] = self.astrBumperNumList
        self.dropConnectorSelection.set("")                                  
        
    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)
        
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.', icon='warning')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate
    
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)  

        # Check the user input
        blnValidate = ConnectorSelection.Check_Input(self.dropConnectorSelection.get())

        # Check if the input is valid
        if (blnValidate is True):
            # Check the user input
            blnValidate = ConnectorSelection.Check_Input(self.dropConnectorLocation.get())         
            
            # Check if the input is valid
            if (blnValidate is True):
                # Check the user input
                blnValidate = ConnectorSelection.Check_Input(self.dropInUse.get())         
                
                # Check if the input is valid
                if (blnValidate is True):
                    blnValidate = True
                else:
                    # Return blnValidate as False
                    blnValidate = False
                    self.dropInUse.focus()
            else:
                # Return blnValidate as False
                blnValidate = False
                self.dropConnectorLocation.focus()                                                
        else:
            # Return blnValidate as False
            blnValidate = False
            self.dropConnectorSelection.focus()

        return blnValidate            

    def Next_Inspection(self):
        """ 
        Function Name: Next_Inspection
        Function Purpose: This function is executed once the user clicks on Next button to move to the nex inspection
        type window. Withdraw the parent window and load the new window.
        """           
        # Hide the main window
        self.Exit()  

        # Open the new window
        ConnectorInspection()

    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the root
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Hide the current window
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """   
        
        # Hide the current window
        self.Exit()  

        if Bool_Flag.blnComplexWithConnectorFlag is True:
            # Return back to the rope selection window
            GymRopeSelection()
        else:
            # Delete the object arrays
            Start_Menu.Delete_Obj_Lists(self)
                        
            # Set all the bool values back to False
            Start_Menu.Set_Default_Bool_Values(self)
            Connectors_Menu()    

    def Update_Dropdown_Values(self):
        """ 
        Function Name: Update_Dropdown_Values
        Function Purpose: This function is executed once the user clicks on AddConnector or AddLocation button and updates the drop down
        object list with the new values.
        """             
        # Ensure the dropdowns are Comboboxes and clear their current selections
        if isinstance(self.dropConnectorSelection, ttk.Combobox):
            self.dropConnectorSelection.set("") 
        if isinstance(self.dropConnectorLocation, ttk.Combobox):
            self.dropConnectorLocation.set("")

        # Update the values for connector selection dropdown
        self.astrSerialNumList = Connectors.astrSerialNumCache
        self.astrBumperNumList = Connectors.astrBumperNumCache
        if isinstance(self.dropConnectorSelection, ttk.Combobox):
            self.dropConnectorSelection['values'] = self.astrSerialNumList

        # Update the values for connector location dropdown
        if isinstance(self.dropConnectorLocation, ttk.Combobox):
            self.dropConnectorLocation['values'] = WallLocation.astrWallLocationDesc

        if Bool_Flag.blnComplexWithConnectorFlag is True:
            # Disable the drop location if this class is called from ropes inspection
            self.dropConnectorLocation.set(WallLocation.strWallLocationDesc)
            self.dropConnectorLocation.configure(state='disabled')
            
    def Add_Connector(self):
        """ 
        Function Name: Add_Connector
        Function Purpose: This function is executed once the user clicks on AddConnector button and updates the drop down
        object list with the new values.
        """           
        # Hide the main window
        self.Withdraw()  

        # Call your AddConnector function here
        newWindow = AddConnector(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Show the main window after the new window is closed
        self.Deiconify()  

        # Update the drop-down menu values
        self.Update_Dropdown_Values()

    def Update_Connectors_Info(self):
        """ 
        Function Name: Update_Connectors_Info
        Function Purpose: This function is executed if the user clicks Update Connectors Information button. 
        """
        # Hide the main window
        self.Withdraw()  

        # Call your AddConnector function here
        newWindow = UpdateConnectorInfo(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Show the main window after the new window is closed
        self.Deiconify()  

        # Update the drop-down menu values
        self.Update_Dropdown_Values()
        
    def Add_Location(self):
        """ 
        Function Name: Add_Location
        Function Purpose: This function is executed once the user clicks on AddLocation button and updates the drop down
        object list with the new values.
        """           
        # Hide the main window
        self.Withdraw()  

        # Call your AddLocation function here
        newWindow = AddLocation(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Show the main window after the new window is closed
        self.Deiconify()  

        # Update the drop-down menu values
        self.Update_Dropdown_Values()

    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        """   
        # Get the selected values from the drop menus
        if self.dropConnectorSelection.get() in Connectors.astrSerialNumCache:
            SerialNum = self.dropConnectorSelection.get()
            Bool_Flag.Set_SerialRadio_Bool_Value_True(Bool_Flag)
        else:
            intPrimID = Connectors.astrBumperNumCache.index(self.dropConnectorSelection.get()) + 1
            SerialNum = Connectors.astrSerialNumCache[intPrimID]
            Bool_Flag.Set_BumperRadio_Bool_Value_True(Bool_Flag)
            
        ConnectorLocation = self.dropConnectorLocation.get()
        InUseStatus = self.dropInUse.get()

        # Commit the data to load the Connectors class objects with the data from the db
        Connectors.strSerialNum = SerialNum
        Connectors.strEquipInUse = InUseStatus
        Connectors.Set_Connectors_Selection(Connectors)

        # Commit the data to load the WallLocation class objects with the data from the db
        WallLocation.strWallLocationDesc = ConnectorLocation
        WallLocation.Get_WallLocation_Selection(WallLocation)

    def Next(self):
        """ 
        Function Name: Next
        Function Purpose: This function is executed once the user clicks on the "Next" button. Once the inputs 
        are validated, the inspection results loads the user selected data and is retained at the object class locations 
        before committing to the database. If all inputs are valid and confirmed by the user, the next stage of inspections is executed.
        """
        global blnValidate
        blnValidate = bool(False)             
        
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

    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This function is executed once the user clicks on the reset button inside the root
        frame. If the user clicks 'Reset', all data is set back to default.
        """     
        # Set the list objects first element to the drop click object
        self.dropConnectorSelection.set("")
        self.dropConnectorLocation.set("")
        self.dropInUse.set("")

        # Reset the radio button to its default value
        self.objRadioValue.set("serial")

        # Populate the dropdown based on default radio button selection
        self.Populate_Dropdown()

        # Re-Populate the dropdown menus 
        self.dropConnectorSelection["values"] = self.astrSerialNumList
        
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()


#######################################################################################################
# Two Connector Selection Class
#######################################################################################################   

class TwoConnectorSelection(tk.Tk, Connectors):
    """
    Class Name: TwoConnectorSelection
    Class Description: This class is to conduct Connector Selection.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new Connector Selection. User must click
        'Next' Button in order to progress to the next inspection type.
        """
        # Load the data from the database
        # Start_Menu.Load_Obj_Lists(self) # Make sure to comment this out after testing
                
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (650/2)     
        self.y = (self.heightSize/2) - (420/2)          
        
        # Create the Window attributes                
        self.title("Connector Selection")
        self.geometry('%dx%d+%d+%d' % (650, 420, self.x, self.y))
        self.resizable(False, False)

        # Load the query selection widget
        self.Selection_Widget()
        
        # Create the frame fields
        self.typeFrame = tk.LabelFrame(self, text="Additional Info")
        self.typeFrame.place(x=100, y=160, width=450, height=200)
                
        # Create the label for the checkboxes
        self.lblConnectorLocation = tk.Label(self.typeFrame, text="Connector Location:")
        self.lblInUse = tk.Label(self.typeFrame, text="Device In Use:")
        self.lblQuestion = tk.Label(self.typeFrame, text="Can't find what you're looking for?")
                        
        # Create the label locations
        self.lblConnectorLocation.place(x=35, y=15)
        self.lblInUse.place(x=70, y=55)
        self.lblQuestion.place(x=125, y=95)

        # Create the entry outputs for each attribute
        self.ConnectorLocationOutput = Entry(self.typeFrame, width=25, state='normal')
        self.InUseStatusOutput = Entry(self.typeFrame, width=25, state='normal')

        # Disable the entry objects
        self.ConnectorLocationOutput.insert(0, WallLocation.strWallLocationDesc)
        self.InUseStatusOutput.insert(0, "Yes")
        
        self.ConnectorLocationOutput.configure(state='disabled')
        self.InUseStatusOutput.configure(state='disabled')
                
        # Create the grid for the entry objects
        self.ConnectorLocationOutput.place(x=190, y=15)  
        self.InUseStatusOutput.place(x=190, y=55)  

        # Check if the cache values for any drop menus have been previously selected and set the values
        if Bool_Flag.blnConnectorPersistFlag == True:
            if (Bool_Flag.blnSerialNumRadioSelect == True):
                self.Set_Previous_Drop_List(Connectors.aTwoConnectorsCache[0][1], self.dropFirstTwoConnectorSelection)
                self.Set_Previous_Drop_List(Connectors.aTwoConnectorsCache[1][1], self.dropSecondTwoConnectorSelection)
            else:
                self.objRadioValue.set("bumper")
                self.dropFirstTwoConnectorSelection["values"] = self.astrSerialNumList
                self.dropSecondTwoConnectorSelection["values"] = self.astrBumperNumList
                self.Set_Previous_Drop_List(Connectors.aTwoConnectorsCache[0][2], self.dropFirstTwoConnectorSelection)
                self.Set_Previous_Drop_List(Connectors.aTwoConnectorsCache[1][2], self.dropSecondTwoConnectorSelection)
            
        # Create the buttons
        self.btnUpdateConnectorInfo = Button(self.typeFrame, width=12, text = "Update Device", command=self.Update_Connectors_Info)
        self.btnAddConnector = Button(self.typeFrame, width=12, text="Add Connector", command=self.Add_Connector)
        self.btnAddLocation = Button(self.typeFrame, width=12, text = "Add Location", command=self.Add_Location)
        self.btnExit = Button(self, width=10, text="Back", command=self.Back)
        self.btnReset = Button(self, width=10, text="Reset",command=self.Reset)
        self.btnNext = Button(self, width=10, text="Next", command=self.Next)
            
        # Create the position of the button
        self.btnUpdateConnectorInfo.place(x=40, y=140)
        self.btnAddConnector.place(x=175, y=140) 
        self.btnAddLocation.place(x=310, y=140)
        self.btnExit.place(x=170, y=375) 
        self.btnNext.place(x=400, y=375) 
        self.btnReset.place(x=285, y=375)
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()

        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the object lists
        Start_Menu.Delete_Obj_Lists(self)

        # Return back to the rope selection window
        GymRopeSelection()

    def Selection_Widget(self):
        """ 
        Function Name: Selection_Widget
        Function Purpose: This function populates the search by widget for Serial or Bumper Num search.
        """           
        # Create the first frame to hold the input fields
        self.selectInput = LabelFrame(self, text="Select Connector's")
        self.selectInput.place(x=100, y=35, width=450, height=120)

        # Create the labels 
        self.lblSearchByConnectorID = Label(self.selectInput, text="Query by Connector ID:")
        self.lblFirstTwoConnectorSelection = Label(self.selectInput, text="Connector One ID Selection:")
        self.lblSecondTwoConnectorSelection = Label(self.selectInput, text="Connector Two ID Selection:")

        # Create the label locations
        self.lblSearchByConnectorID.place(x=19, y=5)
        self.lblFirstTwoConnectorSelection.place(x=18, y=35)
        self.lblSecondTwoConnectorSelection.place(x=18, y=65)

        # Create variables to hold the value of the selected radio button
        self.objRadioValue = tk.StringVar(value='serial')
        self.objComboValue = tk.StringVar()

        # List objects of serial and bumper values
        self.astrSerialNumList = self.astrSerialNumCache
        self.astrBumperNumList = self.astrBumperNumCache

        # Create the radio buttons
        self.rbSerial = tk.Radiobutton(self.selectInput, text="Serial Number", variable=self.objRadioValue, value="serial", command=self.Populate_Dropdown)
        self.rbBumper = tk.Radiobutton(self.selectInput, text="Bumper Number", variable=self.objRadioValue, value="bumper", command=self.Populate_Dropdown)

        # Place the radio buttons next to each other using .place()
        self.rbSerial.place(x=190, y=5)
        self.rbBumper.place(x=300, y=5)
                    
        # Create the entry input box
        self.dropFirstTwoConnectorSelection = ttk.Combobox(self.selectInput, values=self.astrSerialNumList, state='readonly')
        self.dropFirstTwoConnectorSelection.configure(width=25,)
        self.dropSecondTwoConnectorSelection = ttk.Combobox(self.selectInput, values=self.astrSerialNumList, state='readonly')
        self.dropSecondTwoConnectorSelection.configure(width=25,)
        
        # Populate the dropdown based on the default radio button selection
        self.Populate_Dropdown()

        # Create the grid for all of the entry input fields
        self.dropFirstTwoConnectorSelection.place(x=190, y=35) 
        self.dropSecondTwoConnectorSelection.place(x=190, y=65) 

    def Populate_Dropdown(self):
        """ 
        Function Name: Populate_Dropdown
        Function Purpose: This function populates the dropdown based on the radio button selection.
        """           
        if self.objRadioValue.get() == "serial":
            self.dropFirstTwoConnectorSelection["values"] = self.astrSerialNumList
            self.dropSecondTwoConnectorSelection["values"] = self.astrSerialNumList
        else:
            self.dropFirstTwoConnectorSelection["values"] = self.astrBumperNumList
            self.dropSecondTwoConnectorSelection["values"] = self.astrBumperNumList
        self.dropFirstTwoConnectorSelection.set("") 
        self.dropSecondTwoConnectorSelection.set("")                                  
        
    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)
        
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.', icon='warning')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate
    
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        def validate_field(input_field):
            if not TwoConnectorSelection.Check_Input(input_field.get()):
                input_field.focus()
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.', icon='warning')
                return False
            return True
                
        # Check the user input
        if not validate_field(self.dropFirstTwoConnectorSelection):
            return False
        
        if not validate_field(self.dropSecondTwoConnectorSelection):
            return False

        # Check if the two connectors selected are the same
        if self.dropFirstTwoConnectorSelection.get() == self.dropSecondTwoConnectorSelection.get():
            self.Reset()
            self.dropFirstTwoConnectorSelection.focus()
            messagebox.showwarning(title='ERROR', message='You have chosen the same connector for both selections. Please make different choices.', icon='warning')
            return False
        
        # All validations passed
        return True        

    def Next_Inspection(self):
        """ 
        Function Name: Next_Inspection
        Function Purpose: This function is executed once the user clicks on Next button to move to the nex inspection
        type window. Withdraw the parent window and load the new window.
        """           
        # Hide the main window
        self.Exit()  

        # Open the new window
        TwoConnectorInspection()

    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the root
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Hide the current window
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """   
        # Hide the current window
        self.Exit()  
        
        # Return back to the rope selection window
        GymRopeSelection()  

    def Update_Dropdown_Values(self):
        """ 
        Function Name: Update_Dropdown_Values
        Function Purpose: This function is executed once the user clicks on AddConnector or AddLocation button and updates the drop down
        object list with the new values.
        """             
        # Ensure the dropdowns are Comboboxes and clear their current selections
        if isinstance(self.dropFirstTwoConnectorSelection, ttk.Combobox):
            self.dropFirstTwoConnectorSelection.set("") 
        if isinstance(self.dropSecondTwoConnectorSelection, ttk.Combobox):
            self.dropSecondTwoConnectorSelection.set("")             

        # Update the values for connector selection dropdown
        self.astrSerialNumList = Connectors.astrSerialNumCache
        self.astrBumperNumList = Connectors.astrBumperNumCache
        if isinstance(self.dropFirstTwoConnectorSelection, ttk.Combobox):
            self.dropFirstTwoConnectorSelection['values'] = self.astrSerialNumList
        if isinstance(self.dropSecondTwoConnectorSelection, ttk.Combobox):
            self.dropSecondTwoConnectorSelection['values'] = self.astrSerialNumList
            
    def Add_Connector(self):
        """ 
        Function Name: Add_Connector
        Function Purpose: This function is executed once the user clicks on AddConnector button and updates the drop down
        object list with the new values.
        """           
        # Hide the main window
        self.Withdraw()  

        # Call your AddConnector function here
        newWindow = AddConnector(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Show the main window after the new window is closed
        self.Deiconify()  

        # Update the drop-down menu values
        self.Update_Dropdown_Values()

    def Update_Connectors_Info(self):
        """ 
        Function Name: Update_Connectors_Info
        Function Purpose: This function is executed if the user clicks Update Connectors Information button. 
        """
        # Hide the main window
        self.Withdraw()  

        # Call your AddConnector function here
        newWindow = UpdateConnectorInfo(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Show the main window after the new window is closed
        self.Deiconify()  

        # Update the drop-down menu values
        self.Update_Dropdown_Values()
        
    def Add_Location(self):
        """ 
        Function Name: Add_Location
        Function Purpose: This function is executed once the user clicks on AddLocation button and updates the drop down
        object list with the new values.
        """           
        # Hide the main window
        self.Withdraw()  

        # Call your AddLocation function here
        newWindow = AddLocation(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Show the main window after the new window is closed
        self.Deiconify()  

        # Update the drop-down menu values
        self.Update_Dropdown_Values()

    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        """   
        # Get the selected values from the drop menus
        if self.dropFirstTwoConnectorSelection.get() in Connectors.astrSerialNumCache:
            FirstSerialNum = self.dropFirstTwoConnectorSelection.get()
            SecondSerialNum = self.dropSecondTwoConnectorSelection.get()
            Bool_Flag.Set_SerialRadio_Bool_Value_True(Bool_Flag)
        else:
            intFirstPrimID = Connectors.astrBumperNumCache.index(self.dropFirstTwoConnectorSelection.get()) + 1
            FirstSerialNum = Connectors.astrSerialNumCache[intFirstPrimID]
            intSecondPrimID = Connectors.astrBumperNumCache.index(self.dropFirstTwoConnectorSelection.get()) + 1
            SecondSerialNum = Connectors.astrSerialNumCache[intSecondPrimID]
            Bool_Flag.Set_BumperRadio_Bool_Value_True(Bool_Flag)

        # Commit the data to load the Connectors class objects with the data from the db
        InUseStatus = self.InUseStatusOutput.get()
        Connectors.strSerialNum = FirstSerialNum
        Connectors.strEquipInUse = InUseStatus
        
        # Set the connector data for the first connector and append the data to the list object for two conn
        Connectors.Set_Connectors_Selection(Connectors)
        Connectors.Set_TwoConnectorsCache_Attributes(Connectors)
        
        # Set the connector data for the second connector and append the data to the list object for two conn
        Connectors.strSerialNum = SecondSerialNum
        Connectors.Set_Connectors_Selection(Connectors)
        Connectors.Set_TwoConnectorsCache_Attributes(Connectors)

    def Next(self):
        """ 
        Function Name: Next
        Function Purpose: This function is executed once the user clicks on the "Next" button. Once the inputs 
        are validated, the inspection results loads the user selected data and is retained at the object class locations 
        before committing to the database. If all inputs are valid and confirmed by the user, the next stage of inspections is executed.
        """
        global blnValidate
        blnValidate = bool(False)             
        
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

    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This function is executed once the user clicks on the reset button inside the root
        frame. If the user clicks 'Reset', all data is set back to default.
        """     
        # Set the list objects first element to the drop click object
        self.dropFirstTwoConnectorSelection.set("")
        self.dropSecondTwoConnectorSelection.set("")

        # Reset the radio button to its default value
        self.objRadioValue.set("serial")

        # Populate the dropdown based on default radio button selection
        self.Populate_Dropdown()

        # Re-Populate the dropdown menus 
        self.dropFirstTwoConnectorSelection["values"] = self.astrSerialNumList
        self.dropSecondTwoConnectorSelection["values"] = self.astrSerialNumList
        
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()


#######################################################################################################
# Two Connector Inspection Class
#######################################################################################################

class TwoConnectorInspection(tk.Tk): 
    """
    Class Name: ConnectorInspection
    Class Description: This class is to conduct connector inspections.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new Connector inspection. User must click
        'Next' Button in order to progress to the next inspection type. A Visual, Physical, and Functional inspection
        must be performed to complete the inspection.
        """
        # Load the data from the database
        # Start_Menu.Load_Obj_Lists(self) # Make sure to comment this out after testing
        
        # Create the root tkinter var and init
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk window 
        self.x = (self.widthSize/2) - (805/2)     
        self.y = (self.heightSize/2) - (630/2)          
        
        # Create the Window attributes                
        self.title("Connector Inspection")
        self.geometry('%dx%d+%d+%d' % (805, 630, self.x, self.y))
        self.resizable(False, False)

        # Load the query selection widget for Search by serial or bumper num
        self.Selection_Widget()

        # Create the scrollbar frame
        self.scrollFrame = LabelFrame(self, text='Inspection Results')
        self.scrollFrame.place(x=35, y=140, width=735, height=445)
        self.resultCanvas = Canvas(self.scrollFrame)
        self.resultCanvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.resultScrollBar = Scrollbar(self.scrollFrame, orient=VERTICAL, command=self.resultCanvas.yview)
        self.resultScrollBar.pack(side=RIGHT, fill=Y)
        self.resultCanvas.configure(yscrollcommand=self.resultScrollBar.set)
        self.resultCanvas.bind('<Configure>', lambda event: self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all")))
        
        # Create the third frame to hold the result fields
        self.resultFrame = Frame(self.resultCanvas)
        self.resultCanvas.create_window((0,0), window=self.resultFrame, anchor='nw')
        
        # Bind mousewheel scrolling
        self.resultCanvas.bind_all("<MouseWheel>", self.on_vertical_scroll)
                
        # Create the frame fields
        self.visFirstCheckListFrame = tk.LabelFrame(self.resultFrame, text="First Connector Visual Inspection Results")
        self.physFirstCheckListFrame = tk.LabelFrame(self.resultFrame, text="First Connector Physical Inspection Results")
        self.functFirstCheckListFrame = tk.LabelFrame(self.resultFrame, text="First Connector Functional Inspection Results")
        self.visSecondCheckListFrame = tk.LabelFrame(self.resultFrame, text="Second Connector Visual Inspection Results")
        self.physSecondCheckListFrame = tk.LabelFrame(self.resultFrame, text="Second Connector Physical Inspection Results")
        self.functSecondCheckListFrame = tk.LabelFrame(self.resultFrame, text="Second Connector Functional Inspection Results")
        self.commFrame = tk.LabelFrame(self.resultFrame, text="Inspection Comment")

        # Layout for the frames inside the scrollable area
        self.visFirstCheckListFrame.grid(row=0, column=0, padx=(50, 7), pady=10, sticky="nw")
        self.physFirstCheckListFrame.grid(row=0, column=1, padx=(7, 50), pady=10, sticky="nw")
        self.functFirstCheckListFrame.grid(row=1, column=0, columnspan=2, padx=(50, 50), pady=10, sticky="nw")

        # Separator label
        self.lblSeparator = tk.Label(self.resultFrame, text="-------------------------------------------------------------------------------------------------------------------------------")
        self.lblSeparator.grid(row=2, column=0, columnspan=2, sticky="ew", padx=0, pady=5)

        # Layout for the Plastic Inspection frames
        self.visSecondCheckListFrame.grid(row=3, column=0, padx=(50, 7), pady=10, sticky="nw")
        self.physSecondCheckListFrame.grid(row=3, column=1, padx=(7, 50), pady=10, sticky="nw")
        self.functSecondCheckListFrame.grid(row=4, column=0, columnspan=2, padx=(50, 50), pady=10, sticky="nw")
        self.commFrame.grid(row=6, column=0, columnspan=2, padx=(50, 50), pady=10, sticky="nw")

        # Update the scroll region to encompass the entire resultFrame
        self.resultFrame.bind("<Configure>", self.onFrameConfigure)
                                
        # Create the label for the checkboxes
        self.lblFirstConnectVisualStatus = tk.Label(self.visFirstCheckListFrame, text="Visual Status:")
        self.lblFirstConnectPhysicalStatus = tk.Label(self.physFirstCheckListFrame, text="Physical Status:")
        self.lblFirstConnectFunctStatus = tk.Label(self.functFirstCheckListFrame, text="Function Status:")
        self.lblSecondConnectVisualStatus = tk.Label(self.visSecondCheckListFrame, text="Visual Status:")
        self.lblSecondConnectPhysicalStatus = tk.Label(self.physSecondCheckListFrame, text="Physical Status:")
        self.lblSecondConnectFunctStatus = tk.Label(self.functSecondCheckListFrame, text="Function Status:")
                        
        # Create the label locations
        self.lblFirstConnectVisualStatus.grid(row=5, column=0, sticky="w", padx=5, pady=10)
        self.lblFirstConnectPhysicalStatus.grid(row=5, column=0, sticky="w", padx=5, pady=10)
        self.lblFirstConnectFunctStatus.grid(row=3, column=1, sticky="w", padx=5, pady=10)
        self.lblSecondConnectVisualStatus.grid(row=5, column=0, sticky="w", padx=5, pady=10)
        self.lblSecondConnectPhysicalStatus.grid(row=5, column=0, sticky="w", padx=5, pady=10)
        self.lblSecondConnectFunctStatus.grid(row=3, column=1, sticky="w", padx=5, pady=10)

        # Create the drop down menu list for each attribute
        self.dropFirstVisStatus = ttk.Combobox(self.visFirstCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropFirstPhysStatus = ttk.Combobox(self.physFirstCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropFirstFunctStatus = ttk.Combobox(self.functFirstCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropSecondVisStatus = ttk.Combobox(self.visSecondCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropSecondPhysStatus = ttk.Combobox(self.physSecondCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropSecondFunctStatus = ttk.Combobox(self.functSecondCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        
        # Create the drop down menu size for each attribute
        self.dropFirstVisStatus.configure(width=20)
        self.dropFirstPhysStatus.configure(width=20)
        self.dropFirstFunctStatus.configure(width=20)
        self.dropSecondVisStatus.configure(width=20)
        self.dropSecondPhysStatus.configure(width=20)
        self.dropSecondFunctStatus.configure(width=20)
                
        # Create the grid for the drop down menu list objects   
        self.dropFirstVisStatus.place(x=125, y=135)  
        self.dropFirstPhysStatus.place(x=125, y=135)  
        self.dropFirstFunctStatus.place(x=290, y=60)  
        self.dropSecondVisStatus.place(x=125, y=135)  
        self.dropSecondPhysStatus.place(x=125, y=135)  
        self.dropSecondFunctStatus.place(x=290, y=60) 

        # Create the master list for the metallic and functional inspection types
        self.selectItems = Metallic.astrMetallicInspectionDesc 
        self.functItems = CarabinerFunction.astrCarabinerFunctionDesc
        
        # Create the checkbox lists for visual, physical, and functional
        self.visFirstCheckList = [] 
        self.physFirstCheckList = []
        self.functFirstCheckList = []
        self.visSecondCheckList = [] 
        self.physSecondCheckList = []
        self.functSecondCheckList = []        
        
        # Create an empty list to store selected items
        self.checkboxFirstVisStates = {}
        self.checkboxFirstPhysStates = {}
        self.checkboxFirstFuncStates = {}
        self.checkboxSecondVisStates = {}
        self.checkboxSecondPhysStates = {}
        self.checkboxSecondFuncStates = {}
        
        # Set the flag to first
        strConnectorFlag = "First"
        strSecondConnectorFlag = "Second"
        
        # Create the checkbox list
        self.Create_Check_Buttons(self.selectItems, self.visFirstCheckListFrame, ConnectorVisSelection.astrConnectorVisMetalSelect, self.visFirstCheckList, self.checkboxFirstVisStates, self.Get_VisCheckbox_List, "visual", strConnectorFlag)
        self.Create_Check_Buttons(self.selectItems, self.physFirstCheckListFrame, ConnectorPhysSelection.astrConnectorPhysMetalSelect, self.physFirstCheckList, self.checkboxFirstPhysStates, self.Get_PhysCheckbox_List, "physical", strConnectorFlag)
        self.Create_Check_Buttons(self.functItems, self.functFirstCheckListFrame, ConnectorFunctSelection.astrConnectorFunctSelect, self.functFirstCheckList, self.checkboxFirstFuncStates, self.Get_FuncCheckbox_List, "functional", strConnectorFlag)
        self.Create_Check_Buttons(self.selectItems, self.visSecondCheckListFrame, ConnectorVisSelection.astrSecondConnectorVisMetalSelect, self.visSecondCheckList, self.checkboxSecondVisStates, self.Get_VisCheckbox_List, "visual", strSecondConnectorFlag)
        self.Create_Check_Buttons(self.selectItems, self.physSecondCheckListFrame, ConnectorPhysSelection.astrSecondConnectorPhysMetalSelect, self.physSecondCheckList, self.checkboxSecondPhysStates, self.Get_PhysCheckbox_List, "physical", strSecondConnectorFlag)
        self.Create_Check_Buttons(self.functItems, self.functSecondCheckListFrame, ConnectorFunctSelection.astrSecondConnectorFunctSelect, self.functSecondCheckList, self.checkboxSecondFuncStates, self.Get_FuncCheckbox_List, "functional", strSecondConnectorFlag)

        # First check if the selection values have been assigned
        self.Set_Previous_Checkbox_List(ConnectorVisSelection.astrConnectorVisMetalSelect, self.visFirstCheckList, self.selectItems)
        self.Set_Previous_Checkbox_List(ConnectorPhysSelection.astrConnectorPhysMetalSelect, self.physFirstCheckList, self.selectItems)
        self.Set_Previous_Checkbox_List(ConnectorFunctSelection.astrConnectorFunctSelect, self.functFirstCheckList, self.functItems)
        self.Set_Previous_Checkbox_List(ConnectorVisSelection.astrSecondConnectorVisMetalSelect, self.visSecondCheckList, self.selectItems)
        self.Set_Previous_Checkbox_List(ConnectorPhysSelection.astrSecondConnectorPhysMetalSelect, self.physSecondCheckList, self.selectItems)
        self.Set_Previous_Checkbox_List(ConnectorFunctSelection.astrSecondConnectorFunctSelect, self.functSecondCheckList, self.functItems)
                                
        # Check if the cache values for any drop menus have been previously selected and set the values
        if Bool_Flag.blnConnectorPersistFlag == True:
            self.Set_Previous_Drop_List(ConnectorVisSelection.aTwoConnectorVisSelectCache[0][2], self.dropFirstVisStatus)
            self.Set_Previous_Drop_List(ConnectorPhysSelection.aTwoConnectorPhysSelectCache[0][2], self.dropFirstPhysStatus)
            self.Set_Previous_Drop_List(ConnectorFunctSelection.aTwoConnectorFunctSelectCache[0][2], self.dropFirstFunctStatus)
            self.Set_Previous_Drop_List(ConnectorVisSelection.aTwoConnectorVisSelectCache[1][2], self.dropSecondVisStatus)
            self.Set_Previous_Drop_List(ConnectorPhysSelection.aTwoConnectorPhysSelectCache[1][2], self.dropSecondPhysStatus)
            self.Set_Previous_Drop_List(ConnectorFunctSelection.aTwoConnectorFunctSelectCache[1][2], self.dropSecondFunctStatus)
            
        # Create the comment field
        self.commInput = tk.Text(self.commFrame, state='normal')
        self.commInput.grid(row=0, column=0, padx=(4, 10), pady=4)
        self.commInput.configure(width=77, height=4, padx=0)
        
        # Create the buttons
        self.btnBack = Button(self, text="Back", width=10, command=self.Back)
        self.btnClear = Button(self, text="Clear", width=10, command=self.Clear)
        self.btnExit = Button(self, text="Exit", width=10, command=self.Exit)
        self.btnNext = Button(self, text="Next", width=10, command=self.Next)
            
        # Create the position of the button
        self.btnBack.place(x=165, y=595)
        self.btnExit.place(x=295, y=595) 
        self.btnClear.place(x=425, y=595)
        self.btnNext.place(x=555, y=595)  
        
        # Keep the window open while the user is interacting with the widgets
        self.mainloop()

        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the stored data in the class attributes
        StandardConnectorInspect.Delete_Connector_Data(self)
                        
        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)

        # Show the main window after the new window is closed
        Ropes_Menu()      

    def on_vertical_scroll(self, event):
        """Scroll the canvas vertically using the mouse wheel."""
        self.resultCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
    def onFrameConfigure(self, event=None):
        """ 
        Function Name: onFrameConfigure
        Function Purpose: This function is a method that gets called whenever the 'resultFrame' is reconfigured.
        """          
        # Update the scrollable region to fit the size of the resultFrame
        self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all"))
        
    def Selection_Widget(self):
        """ 
        Function Name: Selection_Widget
        Function Purpose: This function populates the search by widget for Serial or Bumper Num search.
        """           
        # Create the first frame to hold the input fields
        self.typeFrame = tk.LabelFrame(self, text="Selected Connector")
        self.typeFrame.place(x=35, y=10, width=735, height=120)

        # Create the labels 
        self.lblFirstConnectSerial = Label(self.typeFrame, text="First Serial ID:")
        self.lblFirstConnectBumper = Label(self.typeFrame, text="Bumper ID:")
        self.lblFirstConnectType = tk.Label(self.typeFrame, text="Connector Type:")
        self.lblSecondConnectSerial = Label(self.typeFrame, text="Second Serial ID:")
        self.lblSecondConnectBumper = Label(self.typeFrame, text="Bumper ID:")
        self.lblSecondConnectType = tk.Label(self.typeFrame, text="Connector Type:")
        
        # Create the label locations
        self.lblFirstConnectSerial.place(x=33, y=5)
        self.lblFirstConnectBumper.place(x=43, y=35)
        self.lblFirstConnectType.place(x=15, y=65)
        self.lblSecondConnectSerial.place(x=375, y=5)
        self.lblSecondConnectBumper.place(x=403, y=35)
        self.lblSecondConnectType.place(x=375, y=65)
        
        # Create the entry input box
        self.FirstSerialNumOut = Entry(self.typeFrame, width=30, state='normal')
        self.FirstBumperNumOut = Entry(self.typeFrame, width=30, state='normal')
        self.FirstConnectType = Entry(self.typeFrame, width=30, state='normal')
        self.SecondSerialNumOut = Entry(self.typeFrame, width=30, state='normal')
        self.SecondBumperNumOut = Entry(self.typeFrame, width=30, state='normal')
        self.SecondConnectType = Entry(self.typeFrame, width=30, state='normal')
        
        # Get the two selected connectors
        amultiConnectorList = Connectors.Get_TwoConnector_StageList_Obj(Connectors)
                
        # Set the values selected from the user
        self.FirstSerialNumOut.insert(0, amultiConnectorList[0][1])
        self.FirstBumperNumOut.insert(0, amultiConnectorList[0][2])
        self.FirstConnectType.insert(0, amultiConnectorList[0][8])
        self.SecondSerialNumOut.insert(0, amultiConnectorList[1][1])
        self.SecondBumperNumOut.insert(0, amultiConnectorList[1][2])
        self.SecondConnectType.insert(0, amultiConnectorList[1][8])

        # Set the values selected from the user
        # self.FirstSerialNumOut.insert(0, '123')
        # self.FirstBumperNumOut.insert(0, 'b-123')
        # self.FirstConnectType.insert(0, 'Type')
        # self.SecondSerialNumOut.insert(0, '234')
        # self.SecondBumperNumOut.insert(0, 'b-234')
        # self.SecondConnectType.insert(0, 'Type')
                        
        # Configure the state to disabled
        self.FirstSerialNumOut.configure(state='disabled')
        self.FirstBumperNumOut.configure(state='disabled')
        self.FirstConnectType.configure(state='disabled')
        self.SecondSerialNumOut.configure(state='disabled')
        self.SecondBumperNumOut.configure(state='disabled')
        self.SecondConnectType.configure(state='disabled')
                
        # Create the grid for all of the entry input fields
        self.FirstSerialNumOut.place(x=125, y=5)
        self.FirstBumperNumOut.place(x=125, y=35)
        self.FirstConnectType.place(x=125, y=65) 
        self.SecondSerialNumOut.place(x=485, y=5)
        self.SecondBumperNumOut.place(x=485, y=35)
        self.SecondConnectType.place(x=485, y=65)
        
    def Create_Check_Buttons(self, selectItems, checkListFrame, arrayObject, checkList, checkboxStates, callback, strInsType, connectorType):
        """ 
        Function Name: Create_Check_Buttons
        Function Description: This helper method to create the checkbox buttons
        """
        if strInsType == "visual" or strInsType == "physical":
            maxColPerRow = 2
            padx_value = 10
        else:
            maxColPerRow = 4
            padx_value = 15

        for index, item in enumerate(selectItems):
            # Check if the item was previously selected (exists in arrayObject)
            is_selected = item in arrayObject
            var = tk.StringVar(value='1' if is_selected else '0')
            checkList.append(var)

            # Use a lambda function to capture the current item in the loop
            checkBox = tk.Checkbutton(checkListFrame, text=item, variable=var, onvalue='1', offvalue='0', 
                                    command=lambda item=item, var=var: callback(item, var, connectorType))
            
            # Store the variable in the checkboxStates dictionary
            checkboxStates[item] = var

            # Calculate the row and column position of checkbutton based on index and max columns 
            rowPosition = index // maxColPerRow
            colPosition = index % maxColPerRow
            checkBox.grid(row=rowPosition, column=colPosition, sticky="w", padx=padx_value)
            
    def Set_Previous_Checkbox_List(self, selectList, checkboxList, paramsList):
        """
        Function Name: Set_Vis_Previous_Checkbox_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the checkboxes from the cache array list for all checkboxes.
        """   
        # First check if the cache values have been assigned
        if len(selectList) == 0:
            # Check the first item of the list    
            checkboxList[0].set('1')
        else:
            # Set the Selection data to the objects in the window
            for i, item in enumerate(paramsList):
                if item in selectList:
                    checkboxList[i].set('1')

    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)

    def Get_VisCheckbox_List(self, item, var, connectorType):
        """
        Function Name: Get_VisCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        if connectorType == 'First':
            # Check if the checkbox is selected
            if state == '1':
                self.Update_Checkbox_List(self.visFirstCheckList, item, self.checkboxFirstVisStates, "visual", ConnectorVisSelection.astrConnectorVisMetalSelect)
            else:
                # Checkbox was deselected
                self.Handle_Deselection(self.visFirstCheckList, item, self.checkboxFirstVisStates, "visual", ConnectorVisSelection.astrConnectorVisMetalSelect)
        elif connectorType == 'Second':
            # Check if the checkbox is selected
            if state == '1':
                self.Update_Checkbox_List(self.visSecondCheckList, item, self.checkboxSecondVisStates, "visual", ConnectorVisSelection.astrSecondConnectorVisMetalSelect)
            else:
                # Checkbox was deselected
                self.Handle_Deselection(self.visSecondCheckList, item, self.checkboxSecondVisStates, "visual", ConnectorVisSelection.astrSecondConnectorVisMetalSelect)

    def Get_PhysCheckbox_List(self, item, var, connectorType):
        """
        Function Name: Get_PhysCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        if connectorType == 'First':
            # Check if the checkbox is selected
            if state == '1':          
                self.Update_Checkbox_List(self.physFirstCheckList, item, self.checkboxFirstPhysStates, "physical", ConnectorPhysSelection.astrConnectorPhysMetalSelect)
            # Checkbox was deselected
            else:
                self.Handle_Deselection(self.physFirstCheckList, item, self.checkboxFirstPhysStates, "physical", ConnectorPhysSelection.astrConnectorPhysMetalSelect)
        elif connectorType == 'Second':
            # Check if the checkbox is selected
            if state == '1':
                self.Update_Checkbox_List(self.physSecondCheckList, item, self.checkboxSecondPhysStates, "physical", ConnectorPhysSelection.astrSecondConnectorPhysMetalSelect)
            else:
                # Checkbox was deselected
                self.Handle_Deselection(self.physSecondCheckList, item, self.checkboxSecondPhysStates, "physical", ConnectorPhysSelection.astrSecondConnectorPhysMetalSelect)

    def Get_FuncCheckbox_List(self, item, var, connectorType):
        """
        Function Name: Get_FuncCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        if connectorType == 'First':
            # Check if the checkbox is selected
            if state == '1':          
                self.Update_Checkbox_List(self.functFirstCheckList, item, self.checkboxFirstFuncStates, "functional", ConnectorFunctSelection.astrConnectorFunctSelect)
            # Checkbox was deselected
            else:
                self.Handle_Deselection(self.functFirstCheckList, item, self.checkboxFirstFuncStates, "functional", ConnectorFunctSelection.astrConnectorFunctSelect)

        elif connectorType == 'Second':
            # Check if the checkbox is selected
            if state == '1':
                self.Update_Checkbox_List(self.functSecondCheckList, item, self.checkboxSecondFuncStates, "functional", ConnectorFunctSelection.astrSecondConnectorFunctSelect)
            else:
                # Checkbox was deselected
                self.Handle_Deselection(self.functSecondCheckList, item, self.checkboxSecondFuncStates, "functional", ConnectorFunctSelection.astrSecondConnectorFunctSelect)

    def Update_Checkbox_List(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Update_Checkbox_List
        Function Purpose: This function is a generalized method to update checkbox states and persistent data.
        """
        # Check if the first item is selected and deselect all remaining items
        firstItem = self.selectItems[0] if selectionKey != 'functional' else self.functItems[0]

        # If the first item is selected, deselect all others
        if item == firstItem:
            for i, selectedItem in enumerate(checkboxList):
                if i != 0:  # Skip the first item
                    selectedItem.set('0')
                    checkboxStates[self.selectItems[i]] = '0'
        else:
            # If any other item is selected, deselect the first item
            checkboxList[0].set('0')
            checkboxStates[firstItem] = '0'

        # Update the checkbox states dictionary
        index = self.functItems.index(item) if selectionKey == 'functional' else self.selectItems.index(item)
        checkboxStates[item] = '1' if checkboxList[index].get() == '1' else '0'

        # Update the persistent data based on the updated checkbox states
        selectedItemsList = [item for item, state in checkboxStates.items() if state == '1']
        
        # Update the arrayObject with selectedItemsList        
        self.Update_Persistent_Array(arrayObject, selectedItemsList)

    def Handle_Deselection(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Handle_Deselection
        Function Purpose: This function is called when a checkbox is deselected.
        """
        # If you want to remove an item from a persisted list or dictionary upon deselection, you can do so here:
        checkboxStates.pop(item, None)
        arrayObject.remove(item)
        
    def Update_Persistent_Array(self, arrayObject, selectedItemsList):
        """
        Function Name: Update_Persistent_Array
        Function Description: This function updates the arrayObject with the selected items list, while keeping existing persisted data.
        """
        # print("Selected Items:", selectedItemsList)
        # print("Before update:", arrayObject)

        selectedSet = set(selectedItemsList)
        arraySet = set(arrayObject)

        # Find items to add and remove
        toAdd = selectedSet - arraySet
        toRemove = arraySet - selectedSet

        for item in toAdd:
            arrayObject.append(item)
        for item in toRemove:
            arrayObject.remove(item)

    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.', icon='warning')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate
    
    def Check_Checkbox_Input(lstCheckBox, strFieldDesc):
        """
        Function Name: Check_Checkbox_Input
        Function Purpose: This function is called whenever a checkbox is present and needs to check if any of the entries are empty. If so,
        warn the user.
        """    
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)
            
        try:
            for i in range(0, len(lstCheckBox)):
                if lstCheckBox[i].get() == '1':
                    # Set blnValidated to True
                    blnValidate = True

            # Check if the blnValidated flag is true or false and warn the user if the entire field is empty
            if blnValidate is True:
                pass
            else:
                messagebox.showwarning(title='ERROR', message='%s field should not be empty. Please verify your selection.'%(strFieldDesc), icon='warning')
                blnValidate = False
                # Select the first checkbox
                lstCheckBox[0].set('1')

        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate  
    
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        def validate_field(input_field, checklist, field_name):
            if not TwoConnectorInspection.Check_Input(input_field.get()):
                input_field.focus()
                return False

            if not TwoConnectorInspection.Check_Checkbox_Input(checklist, field_name):
                return False

            return True

        # Define field names
        strVisField = "Visual Result"
        strPhysField = "Physical Result"
        strFunctField = "Functional Result"

        # Validate each field
        if not validate_field(self.dropFirstVisStatus, self.visFirstCheckList, strVisField):
            return False

        if not validate_field(self.dropFirstPhysStatus, self.physFirstCheckList, strPhysField):
            return False

        if not validate_field(self.dropFirstFunctStatus, self.functFirstCheckList, strFunctField):
            return False

        if not validate_field(self.dropSecondVisStatus, self.visSecondCheckList, strVisField):
            return False

        if not validate_field(self.dropSecondPhysStatus, self.physSecondCheckList, strPhysField):
            return False

        if not validate_field(self.dropSecondFunctStatus, self.functSecondCheckList, strFunctField):
            return False
        
        # All validations passed
        return True
        
    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        """       
        # Declare Local Variables
        sqlConnectorVisSel = ("TConnectorVisMetalSelects", "intConnectorVisMetalSelectID", "strConnectorVisMetalSelect")
        sqlConnectorPhysSel = ("TConnectorPhysMetalSelects", "intConnectorPhysMetalSelectID", "strConnectorPhysMetalSelect")
        sqlConnectorFunctSel = ("TConnectorFunctSelects", "intConnectorFunctSelectID", "strConnectorFunctSelect")
        sqlConnectorVisIns = ("TConnectorVisualInspections", "intConnectorVisualInspectionID")
        sqlConnectorPhysIns = ("TConnectorPhysicalInspections", "intConnectorPhysicalInspectionID") 
        sqlConnectorFunctIns = ("TConnectorFunctionInspections", "intConnectorFunctionInspectID") 
        sqlConnectorStandIns = ("TStandardConnectorInspections", "intStandardConnectorInspectionID")

        # Check if the comment is empty. If not, pass in the values. If empty, pass in 'None'
        if self.commInput.get("1.0", "end-1c") != "":
            self.strComment = str(self.commInput.get("1.0", "end-1c"))
            self.strComment += "; "
            # Add the comment to the AutoBelay Comment object
            ConnectorInspect.strComment = ''.join(self.strComment)
        else:
            self.strComment = 'None'
            ConnectorInspect.strComment = self.strComment
        
        # Get the selected values
        FirstConnectorVisMetSelect = self.Get_Combined_Selection(ConnectorVisSelection.astrConnectorVisMetalSelect, self.selectItems[0])
        FirstConnectorPhysMetSelect = self.Get_Combined_Selection(ConnectorPhysSelection.astrConnectorPhysMetalSelect, self.selectItems[0])
        FirstConnectorFunctSelect = self.Get_Combined_Selection(ConnectorFunctSelection.astrConnectorFunctSelect, self.functItems[0])
        SecondConnectorVisMetSelect = self.Get_Combined_Selection(ConnectorVisSelection.astrSecondConnectorVisMetalSelect, self.selectItems[0])
        SecondConnectorPhysMetSelect = self.Get_Combined_Selection(ConnectorPhysSelection.astrSecondConnectorPhysMetalSelect, self.selectItems[0])
        SecondConnectorFunctSelect = self.Get_Combined_Selection(ConnectorFunctSelection.astrSecondConnectorFunctSelect, self.functItems[0])

        # # Display the string representation
        # print(FirstConnectorVisMetSelect)
        # print(FirstConnectorPhysMetSelect)
        # print(FirstConnectorFunctSelect)
        # print(SecondConnectorVisMetSelect)
        # print(SecondConnectorPhysMetSelect)
        # print(SecondConnectorFunctSelect)
        
        # Get the status for the visual, physical selection
        FirstConnectorVisStatus = self.dropFirstVisStatus.get()
        FirstConnectorPhysStatus = self.dropFirstPhysStatus.get()
        FirstConnectorFunctStatus = self.dropFirstFunctStatus.get()
        SecondConnectorVisStatus = self.dropSecondVisStatus.get()
        SecondConnectorPhysStatus = self.dropSecondPhysStatus.get()
        SecondConnectorFunctStatus = self.dropSecondFunctStatus.get()
                
        # Get the ID of the selected status item
        FirstConnectorVisStatusID = InspectionStatus.astrInspectionStatusDesc.index(FirstConnectorVisStatus) + 1
        FirstConnectorPhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(FirstConnectorPhysStatus) + 1
        FirstConnectorFunctStatusID = InspectionStatus.astrInspectionStatusDesc.index(FirstConnectorFunctStatus) + 1
        SecondConnectorVisStatusID = InspectionStatus.astrInspectionStatusDesc.index(SecondConnectorVisStatus) + 1
        SecondConnectorPhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(SecondConnectorPhysStatus) + 1
        SecondConnectorFunctStatusID = InspectionStatus.astrInspectionStatusDesc.index(SecondConnectorFunctStatus) + 1

        # Get the type of selection, either physical, visual 
        VisInsTypeDesc = InspectionType.astrInspectionTypeDesc[0]
        PhysInsTypeDesc = InspectionType.astrInspectionTypeDesc[1]
        FunctInsTypeDesc = InspectionType.astrInspectionTypeDesc[2]

        # Get the ID of the selected Type item
        VisInsTypeID = InspectionType.astrInspectionTypeDesc.index(VisInsTypeDesc) + 1
        PhysInsTypeID = InspectionType.astrInspectionTypeDesc.index(PhysInsTypeDesc) + 1
        FunctInsTypeID = InspectionType.astrInspectionTypeDesc.index(FunctInsTypeDesc) + 1

        # Get the list of items selected and attach them to the selection object for Visual and Physical Selection
        FirstConnectorVisMetalSelectID = self.Get_Or_Create_ID(FirstConnectorVisMetSelect, sqlConnectorVisSel)              
        FirstConnectorPhysMetalSelectID = self.Get_Or_Create_ID(FirstConnectorPhysMetSelect, sqlConnectorPhysSel)
        FirstConnectorFunctSelectID = self.Get_Or_Create_ID(FirstConnectorFunctSelect, sqlConnectorFunctSel)
        SecondConnectorVisMetalSelectID = FirstConnectorVisMetalSelectID + 1              
        SecondConnectorPhysMetalSelectID = FirstConnectorPhysMetalSelectID + 1
        SecondConnectorFunctSelectID = FirstConnectorFunctSelectID + 1
                                    
        # Get the ID's for the base objects in each class
        ConnectorVisualInsID = self.Get_Max_Primary_Key(sqlConnectorVisIns[0], sqlConnectorVisIns[1])
        ConnectorPhysicalInsID = self.Get_Max_Primary_Key(sqlConnectorPhysIns[0], sqlConnectorPhysIns[1])  
        ConnectorFunctionInspectID = self.Get_Max_Primary_Key(sqlConnectorFunctIns[0], sqlConnectorFunctIns[1])      
        StandardConnectorInspectionID = self.Get_Max_Primary_Key(sqlConnectorStandIns[0], sqlConnectorStandIns[1])

        # Assign the local object to the class objects
        fcvs = ConnectorVisSelection(FirstConnectorVisMetalSelectID, FirstConnectorVisMetSelect, FirstConnectorVisStatus)
        fcps = ConnectorPhysSelection(FirstConnectorPhysMetalSelectID, FirstConnectorPhysMetSelect, FirstConnectorPhysStatus)
        fcfs = ConnectorFunctSelection(FirstConnectorFunctSelectID, FirstConnectorFunctSelect, FirstConnectorFunctStatus)        
        scvs = ConnectorVisSelection(SecondConnectorVisMetalSelectID, SecondConnectorVisMetSelect, SecondConnectorVisStatus)
        scps = ConnectorPhysSelection(SecondConnectorPhysMetalSelectID, SecondConnectorPhysMetSelect, SecondConnectorPhysStatus)
        scfs = ConnectorFunctSelection(SecondConnectorFunctSelectID, SecondConnectorFunctSelect, SecondConnectorFunctStatus) 
        
        # Get the two selected connector ID's
        amultiConnectorList = Connectors.Get_TwoConnector_StageList_Obj(Connectors)
        
        for i in range(2):
            # Update status IDs based on the iteration
            if i == 0:
                VisStatusID = FirstConnectorVisStatusID
                PhysStatusID = FirstConnectorPhysStatusID
                FunctStatusID = FirstConnectorFunctStatusID
                ConnectorID = amultiConnectorList[0][0]
                
                # Commit the data to the visual inspection
                ConnectorVisSelection.intConnectorVisMetalSelectID = fcvs.intConnectorVisMetalSelectID
                ConnectorVisSelection.strConnectorVisMetalSelect = fcvs.strConnectorVisMetalSelect
                ConnectorVisSelection.strConnectorVisStatus = fcvs.strConnectorVisStatus
                
                # Commit the data to the physical inspection
                ConnectorPhysSelection.intConnectorPhysMetalSelectID = fcps.intConnectorPhysMetalSelectID
                ConnectorPhysSelection.strConnectorPhysMetalSelect = fcps.strConnectorPhysMetalSelect
                ConnectorPhysSelection.strConnectorPhysStatus = fcps.strConnectorPhysStatus       
                
                # Commit the data to the function inspection
                ConnectorFunctSelection.intConnectorFunctSelectID = fcfs.intConnectorFunctSelectID
                ConnectorFunctSelection.strConnectorFunctSelect = fcfs.strConnectorFunctSelect
                ConnectorFunctSelection.strConnectorFunctStatus = fcfs.strConnectorFunctStatus    

                # Commit the data to the visual inspection cache
                ConnectorVisSelection.aTwoConnectorVisSelectCache = (fcvs.intConnectorVisMetalSelectID, fcvs.strConnectorVisMetalSelect, fcvs.strConnectorVisStatus)
                ConnectorVisualInspect.aConnectorVisualCache = (ConnectorVisualInsID, ConnectorID, VisInsTypeID, fcvs.intConnectorVisMetalSelectID, VisStatusID)

                # Commit the data to the physical inspection cache
                ConnectorPhysSelection.aTwoConnectorPhysSelectCache = (fcps.intConnectorPhysMetalSelectID, fcps.strConnectorPhysMetalSelect, fcps.strConnectorPhysStatus)
                ConnectorPhysicalInspect.aConnectorPhysicalCache = (ConnectorPhysicalInsID, ConnectorID, PhysInsTypeID, fcps.intConnectorPhysMetalSelectID, PhysStatusID)    

                # Commit the data to the functional inspection cache
                ConnectorFunctSelection.aTwoConnectorFunctSelectCache = (fcfs.intConnectorFunctSelectID, fcfs.strConnectorFunctSelect, fcfs.strConnectorFunctStatus)
                ConnectorFunctionInspect.aConnectorFunctCache = (ConnectorFunctionInspectID, ConnectorID, FunctInsTypeID, fcfs.intConnectorFunctSelectID, FunctStatusID)  

                # Commit the data to the standard inspection cache
                StandardConnectorInspect.aStandardConnectorInsCache = (StandardConnectorInspectionID, ConnectorVisualInsID, ConnectorPhysicalInsID, ConnectorFunctionInspectID)

            else:
                VisStatusID = SecondConnectorVisStatusID
                PhysStatusID = SecondConnectorPhysStatusID
                FunctStatusID = SecondConnectorFunctStatusID
                ConnectorID = amultiConnectorList[1][0]
                
                # Commit the data to the visual inspection
                ConnectorVisSelection.intConnectorVisMetalSelectID = scvs.intConnectorVisMetalSelectID
                ConnectorVisSelection.strConnectorVisMetalSelect = scvs.strConnectorVisMetalSelect
                ConnectorVisSelection.strConnectorVisStatus = scvs.strConnectorVisStatus
                
                # Commit the data to the physical inspection
                ConnectorPhysSelection.intConnectorPhysMetalSelectID = scps.intConnectorPhysMetalSelectID
                ConnectorPhysSelection.strConnectorPhysMetalSelect = scps.strConnectorPhysMetalSelect
                ConnectorPhysSelection.strConnectorPhysStatus = scps.strConnectorPhysStatus       
                
                # Commit the data to the function inspection
                ConnectorFunctSelection.intConnectorFunctSelectID = scfs.intConnectorFunctSelectID
                ConnectorFunctSelection.strConnectorFunctSelect = scfs.strConnectorFunctSelect
                ConnectorFunctSelection.strConnectorFunctStatus = scfs.strConnectorFunctStatus

                # Commit the data to the visual inspection cache
                ConnectorVisualInsID += 1
                ConnectorPhysicalInsID += 1
                ConnectorFunctionInspectID += 1
                StandardConnectorInspectionID += 1
                
                # Commit the data to the visual inspection cache
                aSecondVisConnectorSelectList = (scvs.intConnectorVisMetalSelectID, scvs.strConnectorVisMetalSelect, scvs.strConnectorVisStatus)
                ConnectorVisSelection.aTwoConnectorVisSelectCache = (ConnectorVisSelection.aTwoConnectorVisSelectCache, aSecondVisConnectorSelectList)
                aSecondVisConnectorList = (ConnectorVisualInsID, ConnectorID, VisInsTypeID, scvs.intConnectorVisMetalSelectID, VisStatusID)
                ConnectorVisualInspect.aConnectorVisualCache = (ConnectorVisualInspect.aConnectorVisualCache, (aSecondVisConnectorList))
                
                # Commit the data to the physical inspection cache
                aSecondPhysConnectorSelectList = (scps.intConnectorPhysMetalSelectID, scps.strConnectorPhysMetalSelect, scps.strConnectorPhysStatus)
                ConnectorPhysSelection.aTwoConnectorPhysSelectCache = (ConnectorPhysSelection.aTwoConnectorPhysSelectCache, aSecondPhysConnectorSelectList)                
                aSecondPhysConnectorList = (ConnectorPhysicalInsID, ConnectorID, PhysInsTypeID, scps.intConnectorPhysMetalSelectID, PhysStatusID)    
                ConnectorPhysicalInspect.aConnectorPhysicalCache = (ConnectorPhysicalInspect.aConnectorPhysicalCache, (aSecondPhysConnectorList))
                
                # Commit the data to the functional inspection cache
                aSecondFunctConnectorSelectList = (scfs.intConnectorFunctSelectID, scfs.strConnectorFunctSelect, scfs.strConnectorFunctStatus)
                ConnectorFunctSelection.aTwoConnectorFunctSelectCache = (ConnectorFunctSelection.aTwoConnectorFunctSelectCache, aSecondFunctConnectorSelectList)                
                aSecondFunctConnectorList = (ConnectorFunctionInspectID, ConnectorID, FunctInsTypeID, scfs.intConnectorFunctSelectID, FunctStatusID)  
                ConnectorFunctionInspect.aConnectorFunctCache = (ConnectorFunctionInspect.aConnectorFunctCache, (aSecondFunctConnectorList))
                
                # Commit the data to the standard inspection cache
                aSecondStandConnectorList = (StandardConnectorInspectionID, ConnectorVisualInsID, ConnectorPhysicalInsID, ConnectorFunctionInspectID)
                StandardConnectorInspect.aStandardConnectorInsCache = (StandardConnectorInspect.aStandardConnectorInsCache, (aSecondStandConnectorList))
        
        # # Display the string representation
        # print(ConnectorVisSelection.aTwoConnectorVisSelectCache)
        # print(ConnectorPhysSelection.aTwoConnectorPhysSelectCache)
        # print(ConnectorFunctSelection.aTwoConnectorFunctSelectCache)       
        # print(ConnectorVisualInspect.aConnectorVisualCache) 
        # print(ConnectorPhysicalInspect.aConnectorPhysicalCache)
        # print(ConnectorFunctionInspect.aConnectorFunctCache)
        # print(StandardConnectorInspect.aStandardConnectorInsCache)

        
    def Get_Combined_Selection(self, persisted_array, default_value):
        """
        Function Name: Get_Combined_Selection
        Function Purpose: This function combines the array elements into a comma-separated string,
        and Connectors the case when the persisted array is empty by setting a default value.
        """
        if len(persisted_array) == 0:
            return default_value
        else:
            return ",".join(persisted_array)
        
    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
    
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlStatement[0], sqlStatement[1]))    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
    
    def Next(self):
        """ 
        Function Name: Next
        Function Purpose: This function is executed once the user clicks on the "Next" button. Once the inputs 
        are validated, the inspection results loads the user selected data and is retained at the object class locations 
        before committing to the database. If all inputs are valid and confirmed by the user, the next stage of inspections is executed.
        """
        global blnValidate
        blnValidate = bool(False)             
        
        # First check if the input is empty, if so, notify the user the input needs attention 
        blnValidate = self.Validate_InputFields()
        
        # If status is true then proceed to update the result field, else, reset the fields
        if blnValidate is True:
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to next inspection component?', icon='question') is True:
                # print(ConnectorVisSelection.astrConnectorVisMetalSelect)
                # print(ConnectorPhysSelection.astrConnectorPhysMetalSelect) 
                # print(ConnectorFunctSelection.astrConnectorFunctSelect)
                # Load the user data and prep the data for db dump
                self.Pull_UserInput()     
                
                # Set the global class bool to true
                Bool_Flag.Set_Connector_Bool_Value_True(Bool_Flag)
                
                # Go to the next inspection component
                self.Next_Inspection()
            else:
                # Check if the user would like to reset the fields
                if messagebox.askyesno(message='ATTENTION! \n\n Would you like to reset the fields?', icon='question') is True:
                    # Clear the input fields and after data is submitted to the database
                    self.Clear()                

    def Clear(self):
        """ 
        Function Name: Clear
        Function Purpose: This function is executed once the user clicks on the Clear button inside the
        frame. If the user clicks 'Clear', all data is set back to default.
        """     
        # Set the list objects first element to the drop click object
        self.dropConnectVisStatus.set("")
        self.dropConnectVisStatus.set("")
        self.dropConnectFunctStatus.set("")
        
        # Reset the checkboxes to empty selections
        BaseFunctions.Deselect_All_Checkbox(self.visCheckList)
        BaseFunctions.Deselect_All_Checkbox(self.physCheckList)
        BaseFunctions.Deselect_All_Checkbox(self.functCheckList)

        # Set the first item in the list to the first checkbox item displayed
        self.visCheckList[0].set('1')
        self.physCheckList[0].set('1')
        self.functCheckList[0].set('1')

        # Clear the class objects
        StandardConnectorInspect.Reset_Connector_Data(self)
        StandardConnectorInspect.Delete_Connector_Data(self)
        
        # Delete the comment field 
        self.commInput.delete("1.0", "end-1c") 
        
    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Expose the window widget to the user
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """     
        # Hide the current window
        self.Exit()  

        # Show the main window after the new window is closed
        TwoConnectorSelection()

    def Next_Inspection(self):
        """ 
        Function Name: Next_Inspection
        Function Purpose: This function is executed once the user clicks on Next button to move to the nex inspection
        type window. Withdraw the parent window and load the new window.
        """           
        # Hide the main window
        self.Exit()  

        if (Bool_Flag.blnComplexWith_Two_ConnectorFlag is True) and (Bool_Flag.blnComplexWithBelayDeviceFlag is True):
            # Display the results of the inspection
            BelayDeviceSelection()
        else:
            RopeInspection()
                
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()


# #######################################################################################################
# # Add New Connector Class
# ####################################################################################################### 

class AddConnector(tk.Toplevel, Connectors):
    """
    Class Name: AddConnector
    Class Description: This class adds a new Connector to the database.
    """
    def __init__(self, parent):
        # Load the data from the database
        # Start_Menu.Load_Obj_Lists(self) # Make sure to comment this out after testing
                        
        # Initialize the Toplevel window
        super().__init__(parent)

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (580/2)     
        self.y = (self.heightSize/2) - (300/2)    
                                        
        # Create the Window attributes
        self.title("Add New Connector")
        self.geometry('%dx%d+%d+%d' % (580, 300, self.x, self.y))
        self.resizable(False, False)

        # Create the second frame to hold the input fields
        self.frameInput = tk.LabelFrame(self, text="Connector Credentials")
        self.frameInput.place(x=90, y=10, width=405, height=235)

        # Create the labels 
        self.lblManuName = tk.Label(self.frameInput, text="Manufacture Name:")
        self.lblSerialNum = tk.Label(self.frameInput, text="Serial Number:")
        self.lblBumperNum = tk.Label(self.frameInput, text="Bumper Number:")      
        self.lblManuDate = tk.Label(self.frameInput, text="Manufacture Date:")
        self.lblInstallDate = tk.Label(self.frameInput, text="Install Date:")
        self.lblConnectorType = tk.Label(self.frameInput, text="Connector Type:")
        self.lblConnectorInUse = tk.Label(self.frameInput, text="Connector In Use:")

        # Create the label locations
        self.lblManuName.grid(row=0, column=0, sticky='W', padx=5)
        self.lblSerialNum.grid(row=1, column=0, sticky='W', padx=5)
        self.lblBumperNum.grid(row=2, column=0, sticky='W', padx=5)
        self.lblManuDate.grid(row=3, column=0, sticky='W', padx=5)
        self.lblInstallDate.grid(row=4, column=0, sticky='W', padx=5)
        self.lblConnectorType.grid(row=5, column=0, sticky='W', padx=5)
        self.lblConnectorInUse.grid(row=6, column=0, sticky='W', padx=5)

        # Create the entry input box
        self.ManuNameInput = Entry(self.frameInput, width=40)
        self.SerialNumInput = Entry(self.frameInput, width=40)
        self.BumperNumInput = Entry(self.frameInput, width=40)
        self.ManuDateInput = Entry(self.frameInput, width=40)
        self.InstallDateInput = Entry(self.frameInput, width=40)

        # Create the drop down menu list objects
        self.dropCarabType = ttk.Combobox(self.frameInput, values=Carabiner.astrCarabinerType, state='readonly')
        self.dropInUseSelection = ttk.Combobox(self.frameInput, values=['Yes', 'No'], state='readonly')

        # Create the drop down menu size for each attribute
        self.dropCarabType.configure(width=37)
        self.dropInUseSelection.configure(width=37)
        
        # Create the grid for the drop down menu
        self.dropCarabType.grid(row=5, column=1, padx=5, pady=5)
        self.dropInUseSelection.grid(row=6, column=1, padx=5, pady=5)

        # Create a list of all the entry objects
        aEntryList = (self.ManuDateInput, self.InstallDateInput, self.BumperNumInput) 
        astrPlaceHolder = ("MM/DD/YYYY", "MM/DD/YYYY", "Optional")

        # Insert the placeholders at the desired entry points
        for i, entry in enumerate(aEntryList):
            entry.insert(0, astrPlaceHolder[i])
            entry.config(fg='grey')
            entry.bind('<FocusIn>', lambda event, entry=entry, placeholder=astrPlaceHolder[i]: self.On_Entry_Click(event, entry, placeholder))
            entry.bind('<FocusOut>', lambda event, entry=entry, placeholder=astrPlaceHolder[i]: self.On_FocusOut(event, entry, placeholder))
            
        # Create the grid for all of the entry input fields
        self.ManuNameInput.grid(row=0, column=1, padx=25, pady=5)
        self.SerialNumInput.grid(row=1, column=1, pady=5)
        self.BumperNumInput.grid(row=2, column=1, pady=5)
        self.ManuDateInput.grid(row=3, column=1, pady=5)
        self.InstallDateInput.grid(row=4, column=1, pady=5)

        # Create the buttons
        self.btnExit = Button(self, text="Back", width=10, command=lambda:self.Exit())
        self.btnReset = Button(self, text="Reset", width=10, command=lambda:self.Reset())
        self.btnSubmit = Button(self, text="Submit", width=10, command=lambda:self.Submit())

        # Create the button grid
        self.btnExit.place(x=120, y=260)
        self.btnReset.place(x=250, y=260)
        self.btnSubmit.place(x=380, y=260)

    def On_Entry_Click(self, event, entry, strPlaceHolder):
        """ 
        Function Name: On_Entry_Click
        Function Purpose: This function gets called whenever entry is clicked by a user to start a new entry.
        """    
        if entry.get() == strPlaceHolder:
            entry.delete(0, "end") 
            entry.insert(0, '') 
            entry.config(fg='black')
            
    def On_FocusOut(self, event, entry, strPlaceHolder):
        """ 
        Function Name: On_FocusOut
        Function Purpose: This function gets called whenever the entry loses focus.
        """            
        if entry.get() == '':
            entry.insert(0, strPlaceHolder)
            entry.config(fg='grey') 
                                            
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate
        
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        def set_invalid(input_field, msg):
            """
            Set the input field to show invalid data.
            """
            input_field.delete(0, tk.END)
            input_field.configure(background='Yellow')
            input_field.focus()
            messagebox.showwarning("Input Error", msg)

        # Validate Manufacturer Name
        if not (AddConnector.Check_Input(self.ManuNameInput.get()) and
                BaseFunctions.Validate_String_Input(self.ManuNameInput.get())):
            set_invalid(self.ManuNameInput)
            return False
        
        # Validate Serial Number
        if not (AddConnector.Check_Input(self.SerialNumInput.get()) and
                BaseFunctions.Validate_Serial_Input(self.SerialNumInput.get()) and
                self.SerialNumInput.get() not in Connectors.astrSerialNumCache):
            set_invalid(self.SerialNumInput)
            return False
        
        # Get the Primary Key ID
        sqlPrimKey = ("TConnectors", "intConnectorID")   
        self.ConnectorIDResult = self.Get_Or_Create_ID(self.SerialNumInput.get(), sqlPrimKey)
        
        # Validate Bumper Number if it exists
        bumper_num = self.BumperNumInput.get()
        if bumper_num != "" and not BaseFunctions.Validate_Serial_Input(bumper_num) and bumper_num not in Connectors.astrBumperNumCache:
            set_invalid(self.BumperNumInput)
            return False

        self.BumperNumInput.delete(0, tk.END)
        new_bumper_num_value = bumper_num if bumper_num != "" else 'Optional'
        self.BumperNumInput.insert(0, new_bumper_num_value)
        
        # Validate Manufacturing Date
        if not AddConnector.Check_Input(self.ManuDateInput.get()):
            set_invalid(self.ManuDateInput)
            return False

        result_tup = BaseFunctions.Validate_Date_Input(self.ManuDateInput.get())
        if not result_tup[0]:
            set_invalid(self.ManuDateInput)
            return False

        self.ManuDateInputResult = AddConnector.Change_Date_To_Format(self.ManuDateInput, result_tup)

        # Validate Installation Date
        if not AddConnector.Check_Input(self.InstallDateInput.get()):
            set_invalid(self.InstallDateInput)
            return False

        result_tup = BaseFunctions.Validate_Date_Input(self.InstallDateInput.get())
        if not result_tup[0]:
            set_invalid(self.InstallDateInput)
            return False

        self.InstallDateResult = AddConnector.Change_Date_To_Format(self.InstallDateInput, result_tup)

        # Validate dropCarabType
        if not AddConnector.Check_Input(self.dropCarabType.get()):
            set_invalid(self.dropCarabType)
            return False
                    
        # Validate 'In Use' Selection
        if not AddConnector.Check_Input(self.dropInUseSelection.get()):
            set_invalid(self.dropInUseSelection)
            return False
        
        return True


    def Change_Date_To_Format(dtmObject, aResultTup):
        """ 
        Function Name: Change_Date_To_Format
        Function Purpose: This function is executed every call of the validation check to ensure the dates are all
        changed to the same format no matter if the character is valid.
        """ 
        dtmObject.delete(0, END)
        dtmObject.insert(0, aResultTup[1])
        dtmObject = aResultTup[1]

        return dtmObject

    def Get_UserInput(self):
        """ 
        Function Name: Get_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        Then the data will be sent to the db.
        """       
        # Get the current date for last and next inspection
        aDateResult = BaseFunctions.Update_Inspection_Date()
        lastDate = datetime.strftime(aDateResult[0], '%m/%d/%Y')
        nextDate =  datetime.strftime(aDateResult[1], '%m/%d/%Y')
        
        # Assign value to the objects
        ConnectorID = self.ConnectorIDResult
        SerialNum = self.SerialNumInput.get()
        BumperNum = self.BumperNumInput.get()
        ManufactureDate = self.ManuDateInputResult
        InstallationDate = self.InstallDateResult
        LastInspectionDate = lastDate
        NextInspectionDate = nextDate
        ConnectorType = self.dropCarabType.get()
        ConnectorInUse = self.dropInUseSelection.get()

        # If BumperNum = "Optional" place a 'None' string
        if BumperNum == "Optional":
            BumperNum = "None"
            
        # Capitalize the first letter of each word and append a space after splitting the user input into a list
        resultList = self.ManuNameInput.get().split()
        self.Cap_ManuName = [result.capitalize() for result in resultList]
        ManuName = ' '.join(self.Cap_ManuName)                
        
        # Assign the local objects to the class objects
        self.intConnectorID = ConnectorID
        self.strSerialNum = SerialNum
        self.strBumperNum = BumperNum
        self.strManufactureName = ManuName
        self.dtmManufactureDate = ManufactureDate
        self.dtmInstallationDate = InstallationDate
        self.dtmLastInspectionDate = LastInspectionDate
        self.dtmNextInspectionDate = NextInspectionDate
        self.strDeviceType = ConnectorType
        self.strEquipInUse = ConnectorInUse

    def Get_Combined_Selection(self, persisted_array, default_value):
        """
        Function Name: Get_Combined_Selection
        Function Purpose: This function combines the array elements into a comma-separated string,
        and handles the case when the persisted array is empty by setting a default value.
        """
        if len(persisted_array) == 0:
            return default_value
        else:
            return ",".join(persisted_array)
        
    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
                        
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlStatement[0], sqlStatement[1]))    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
    
    def Clear_BG_Color(self):
        """ 
        Function Name: Clear_BG_Color
        Function Purpose: This button executes when the user submits their entries and clears the background
        color before any validation checks.
        """
        # Delete the button after submission
        self.ManuNameInput.configure(background='White')
        self.SerialNumInput.configure(background='White')
        self.BumperNumInput.configure(background='White')
        self.ManuDateInput.configure(background='White')
        self.InstallDateInput.configure(background='White')
        
    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This button executes when the user wants to reset the values.
        """
        # Delete the button after submission
        self.ManuNameInput.delete(0, END)
        self.SerialNumInput.delete(0, END)
        self.BumperNumInput.delete(0, END)
        self.ManuDateInput.delete(0, END)
        self.InstallDateInput.delete(0, END)
        
        # Reset the drop menus
        self.dropCarabType.set("")
        self.dropInUseSelection.set("")
        
        # Clear out the background colors and set to default as 'white'
        AddConnector.Clear_BG_Color(self)

        # Create a list of all the entry objects
        aEntryList = (self.ManuDateInput, self.InstallDateInput, self.BumperNumInput) 
        astrPlaceHolder = ("MM/DD/YYYY", "MM/DD/YYYY", "Optional")

        # Insert the placeholders at the desired entry points
        for i, entry in enumerate(aEntryList):
            entry.insert(0, astrPlaceHolder[i])
            entry.config(fg='grey')
            entry.bind('<FocusIn>', lambda event, entry=entry, placeholder=astrPlaceHolder[i]: self.On_Entry_Click(event, entry, placeholder))
            entry.bind('<FocusOut>', lambda event, entry=entry, placeholder=astrPlaceHolder[i]: self.On_FocusOut(event, entry, placeholder))
            
    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the new Connector Connector to the db. Else, reset
        """
        # Check if all of the inputs are valid
        global blnValidate 
        blnValidate = bool(False)
        
        # Clear out the background colors and set to default as 'white'
        AddConnector.Clear_BG_Color(self)
        
        # Get the blnValidate status
        blnValidate = AddConnector.Validate_InputFields(self)
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to add new Connector?') is True:     
                # Load the user data and prep the data for db dump
                AddConnector.Get_UserInput(self)
                Connectors.Add_Connectors_Query(self)                     

                # Check if the user would like to add another Connector
                if messagebox.askyesno(message='SUCCESSFUL UPLOAD! \n\n Would you like to add another Connector?') is True:
                    # Clear the input fields and after data is submitted to the database
                    AddConnector.Reset(self)
                else:
                    AddConnector.Exit(self)
            
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
                

#######################################################################################################
# Update Connectors Info
#######################################################################################################

class UpdateConnectorInfo(tk.Toplevel, Connectors):
    """
    Class Name: UpdateConnectorInfo
    Class Description: This class updates any Connector to the database.
    """
    def __init__(self, parent):
        # Load the data from the database
        # Start_Menu.Load_Obj_Lists(self) # Make sure to comment this out after testing
        
        # Initialize the Toplevel window
        super().__init__(parent)

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (560/2)     
        self.y = (self.heightSize/2) - (440/2)  
                                        
        # Create the Window attributes
        self.WindowTitle = self.title("Update Connector Information")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (560, 440, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Load the query selection widget
        self.Selection_Widget()
                
        # Create the second frame to hold the input fields
        self.frameInput = LabelFrame(self, text="Connector Credentials")
        self.frameInput.place(x=75, y=170, width=405, height=205)

        # Create the labels 
        self.lblSerialNum = tk.Label(self.frameInput, text="Serial Number:")
        self.lblBumperNum = tk.Label(self.frameInput, text="Bumper Number:")      
        self.lblManuDate = tk.Label(self.frameInput, text="Manufacture Date:")
        self.lblInstallDate = tk.Label(self.frameInput, text="Install Date:")
        self.lblConnectorType = tk.Label(self.frameInput, text="Connector Type:")
        self.lblConnectorInUse = tk.Label(self.frameInput, text="Connector In Use:")

        # Create the label locations
        self.lblSerialNum.grid(row=1, column=0, sticky='W', padx=5)
        self.lblBumperNum.grid(row=2, column=0, sticky='W', padx=5)
        self.lblManuDate.grid(row=3, column=0, sticky='W', padx=5)
        self.lblInstallDate.grid(row=4, column=0, sticky='W', padx=5)
        self.lblConnectorType.grid(row=5, column=0, sticky='W', padx=5)
        self.lblConnectorInUse.grid(row=6, column=0, sticky='W', padx=5)
        
        # Create the entry input box
        self.SerialNumInput = Entry(self.frameInput, width=39, state='disabled')
        self.BumperNumInput = Entry(self.frameInput, width=39, state='disabled')
        self.ManuDateInput = Entry(self.frameInput, width=39, state='disabled')
        self.InstallDateInput = Entry(self.frameInput, width=39, state='disabled')

        # Create the combo box
        self.aInUseSelectionList = ('Yes', 'No', 'Retired')
        self.dropCarabType = ttk.Combobox(self.frameInput, values=Carabiner.astrCarabinerType, state='disabled')
        self.dropInUseSelection = ttk.Combobox(self.frameInput, values=self.aInUseSelectionList, state='disabled')
        self.dropCarabType.configure(width=36,)
        self.dropInUseSelection.configure(width=36,)

        # Create the grid for all of the entry input fields
        self.SerialNumInput.grid(row=1, column=1, padx=25, pady=5)
        self.BumperNumInput.grid(row=2, column=1, pady=5)
        self.ManuDateInput.grid(row=3, column=1, pady=5)
        self.InstallDateInput.grid(row=4, column=1, pady=5)
        self.dropCarabType.grid(row=5, column=1, pady=5)
        self.dropInUseSelection.grid(row=6, column=1, pady=5)

        # Create the buttons
        self.btnExit = Button(self, text="Back", width=10, command=lambda:UpdateConnectorInfo.Exit(self))
        self.btnReset = Button(self, text="Reset", width=10, command=lambda:UpdateConnectorInfo.Reset(self))
        self.btnSubmit = Button(self, text="Submit", width=10, command=lambda:UpdateConnectorInfo.Submit(self))

        # Create the button grid
        self.btnExit.place(x=105, y=390)
        self.btnReset.place(x=235, y=390)
        self.btnSubmit.place(x=365, y=390)

    def Selection_Widget(self):
        """ 
        Function Name: Selection_Widget
        Function Purpose: This function populates the search by widget for Serial or Bumper Num search.
        """           
        # Create the first frame to hold the input fields
        self.selectInput = LabelFrame(self, text="Select Connector")
        self.selectInput.place(x=75, y=35, width=405, height=130)

        # Create the labels 
        self.lblSearchByConnectorID = Label(self.selectInput, text="Query by Device ID:")
        self.lblConnectorSelection = Label(self.selectInput, text="Device ID Selection:")

        # Create the label locations
        self.lblSearchByConnectorID.place(x=5, y=5)
        self.lblConnectorSelection.place(x=5, y=35)

        # Create variables to hold the value of the selected radio button
        self.objRadioValue = tk.StringVar(value='serial')
        self.objComboValue = tk.StringVar()

        # List objects of serial and bumper values
        self.astrSerialNumList = self.astrSerialNumCache
        self.astrBumperNumList = self.astrBumperNumCache

        # Create the radio buttons
        self.rbSerial = tk.Radiobutton(self.selectInput, text="Serial Number", variable=self.objRadioValue, value="serial", command=self.Populate_Dropdown)
        self.rbBumper = tk.Radiobutton(self.selectInput, text="Bumper Number", variable=self.objRadioValue, value="bumper", command=self.Populate_Dropdown)

        # Place the radio buttons next to each other using .place()
        self.rbSerial.place(x=135, y=5)
        self.rbBumper.place(x=265, y=5)
                    
        # Create the combo box
        self.dropConnectorSelection = ttk.Combobox(self.selectInput, values=self.astrSerialNumList, state='readonly')
        self.dropConnectorSelection.configure(width=36,)

        # Populate the dropdown based on the default radio button selection
        self.Populate_Dropdown()

        # Create the grid for all of the entry input fields
        self.dropConnectorSelection.place(x=140, y=35)

        # Create the buttons
        self.btnSelectSubmit = Button(self.selectInput, text="Submit", width=10, command=lambda:UpdateConnectorInfo.SubmitSelect(self))

        # Create the button grid
        self.btnSelectSubmit.place(x=165, y=70)  

    def Populate_Dropdown(self):
        """ 
        Function Name: Populate_Dropdown
        Function Purpose: This function populates the dropdown based on the radio button selection.
        """           
        if self.objRadioValue.get() == "serial":
            self.dropConnectorSelection["values"] = self.astrSerialNumList
        else:
            self.dropConnectorSelection["values"] = self.astrBumperNumList
        self.dropConnectorSelection.set("")                                 
        
    def Change_Date_To_Format(dtmObject, aResultTup):
        """ 
        Function Name: Change_Date_To_Format
        Function Purpose: This function is executed every call of the validation check to ensure the dates are all
        changed to the same format no matter if the character is valid.
        """ 
        dtmObject.delete(0, END)
        dtmObject.insert(0, aResultTup[1])
        dtmObject = aResultTup[1]

        return dtmObject

    def Convert_Date_Format(date_str):
        """ 
        Function Name: SubmitSelect
        Function Purpose: This button Convert date from "YYYY-MM-DD" to "MM/DD/YYYY"
        """
        year, month, day = date_str.split('-')
        return f"{month}/{day}/{year}"

    def Disable_After_Submit(self):
        """ 
        Function Name: Disable_After_Submit
        Function Purpose: This function disables certain controls after submission.
        """   
        # Disable the submit button
        self.btnSubmit.configure(state='disabled')
        
        # Reset the value of the dropdown
        self.dropConnectorSelection.set("")

    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)
        
    def Check_Serial_Or_Bumper(self):
        """ 
        Function Name: Check_Serial_Or_Bumper
        Function Purpose: This function is executed once the user clicks on the option of query search by serial
        number or bumper number. 
        """        
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Get the primary key ID from the dropdown
        strSelectionID = self.dropConnectorSelection.get()
        
        # Determine the primary key for the query
        if strSelectionID in Connectors.astrSerialNumCache:
            primary_key = Connectors.astrSerialNumCache.index(strSelectionID) + 1
            blnFlag = True
        elif strSelectionID in Connectors.astrBumperNumCache:
            primary_key =  Connectors.astrBumperNumCache.index(strSelectionID) + 1
            blnFlag = False
            
        # Return the primary key
        return (blnFlag, primary_key)
                
    def SubmitSelect(self):
        """ 
        Function Name: SubmitSelect
        Function Purpose: This button executes when the user selects the Connector.
        """
        # Set the state of the inputs
        for entry in [self.SerialNumInput, self.BumperNumInput, self.ManuDateInput, self.InstallDateInput]:
            entry.configure(state='normal')

        # Configure the drop menu for in use
        self.dropCarabType.configure(state='readonly')
        self.dropInUseSelection.configure(state='readonly')

        # Determine the primary key for the query
        resultTup =  self.Check_Serial_Or_Bumper()
        primary_key =  resultTup[1]

        # Execute the query
        aParams = ('TConnectors', 'intConnectorID', primary_key)
        QueryResult = Queries.Get_All_DB_Values_OnePrimKey(Queries, aParams)
        
        if QueryResult:
            self.SerialNumInput.insert(0, QueryResult[1])
            self.BumperNumInput.insert(0, QueryResult[2])
            self.ManuDateInput.insert(0, UpdateConnectorInfo.Convert_Date_Format(QueryResult[4]))
            self.InstallDateInput.insert(0, UpdateConnectorInfo.Convert_Date_Format(QueryResult[5]))
            self.Set_Previous_Drop_List(QueryResult[8], self.dropCarabType)
            self.Set_Previous_Drop_List(QueryResult[9], self.dropInUseSelection)
        
        # Disable the select submit button
        self.btnSelectSubmit.configure(state='disabled')
        
        # Enable the submit and reset buttons
        self.btnSubmit.configure(state='normal')
        self.btnReset.configure(state='normal')
                
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate
        
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        def set_invalid(input_field):
            """
            Set the input field to show invalid data.
            """
            input_field.delete(0, tk.END)
            input_field.configure(background='Yellow')
            input_field.focus()

        # Validate Serial Number
        if not (UpdateConnectorInfo.Check_Input(self.SerialNumInput.get()) and
                BaseFunctions.Validate_Serial_Input(self.SerialNumInput.get())):
            set_invalid(self.SerialNumInput)
            return False

        # Validate Bumper Number
        bumper_num = self.BumperNumInput.get()
        if bumper_num != "" and not BaseFunctions.Validate_Serial_Input(bumper_num):
            set_invalid(self.BumperNumInput)
            return False

        self.BumperNumInput.delete(0, tk.END)
        new_bumper_num_value = bumper_num if bumper_num != "" else 'Optional'
        self.BumperNumInput.insert(0, new_bumper_num_value)
        
        # Validate Manufacturing Date
        if not UpdateConnectorInfo.Check_Input(self.ManuDateInput.get()):
            set_invalid(self.ManuDateInput)
            return False

        result_tup = BaseFunctions.Validate_Date_Input(self.ManuDateInput.get())
        if not result_tup[0]:
            set_invalid(self.ManuDateInput)
            return False

        self.ManuDateInputResult = UpdateConnectorInfo.Change_Date_To_Format(self.ManuDateInput, result_tup)

        # Validate Installation Date
        if not UpdateConnectorInfo.Check_Input(self.InstallDateInput.get()):
            set_invalid(self.InstallDateInput)
            return False

        result_tup = BaseFunctions.Validate_Date_Input(self.InstallDateInput.get())
        if not result_tup[0]:
            set_invalid(self.InstallDateInput)
            return False

        self.InstallDateResult = UpdateConnectorInfo.Change_Date_To_Format(self.InstallDateInput, result_tup)

        # Validate dropCarabType
        if not UpdateConnectorInfo.Check_Input(self.dropCarabType.get()):
            set_invalid(self.dropCarabType)
            return False
                    
        # Validate 'In Use' Selection
        if not UpdateConnectorInfo.Check_Input(self.dropInUseSelection.get()):
            set_invalid(self.dropInUseSelection)
            return False
        
        return True
    
    def Get_UserInput(self):
        """ 
        Function Name: Get_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        Then the data will be sent to the db.
        """                
        # Assign value to the objects
        SerialNum = self.SerialNumInput.get()
        BumperNum = self.BumperNumInput.get()
        ManuDate = datetime.strptime(self.ManuDateInputResult, '%m/%d/%Y').date()
        InstallationDate = datetime.strptime(self.InstallDateResult, '%m/%d/%Y').date()
        ManuDate = str(ManuDate)
        InstallationDate = str(InstallationDate)
        ConnectorType = self.dropCarabType.get()
        ConnectorInUse = self.dropInUseSelection.get()
        
        # First check if the serial or bumper number was selected 
        resultTup =  self.Check_Serial_Or_Bumper()
        intPrimKey = resultTup[1] - 1

        # Commit the data to load the Connectors class objects with the data from the db
        Connectors.strSerialNum = Connectors.astrSerialNumCache[intPrimKey]
        Connectors.Set_Connectors_Data(Connectors)
            
        # Finish by updating the Connectors class objects before the database dump
        c = Connectors(self.intConnectorID, SerialNum, BumperNum, self.strManufactureName, ManuDate, InstallationDate, 
                    self.dtmLastInspectionDate, self.dtmNextInspectionDate, ConnectorType, ConnectorInUse)
        
        Connectors.intConnectorID = c.intConnectorID
        Connectors.strSerialNum = c.strSerialNum
        Connectors.strBumperNum = c.strBumperNum
        Connectors.strManufactureName = c.strManufactureName
        Connectors.dtmManufactureDate = c.dtmManufactureDate
        Connectors.dtmInstallationDate = c.dtmInstallationDate
        Connectors.dtmLastInspectionDate = c.dtmLastInspectionDate
        Connectors.dtmNextInspectionDate = c.dtmNextInspectionDate
        Connectors.strDeviceType = c.strDeviceType
        Connectors.strEquipInUse = c.strEquipInUse
        
    def Clear_BG_Color(self):
        """ 
        Function Name: Clear_BG_Color
        Function Purpose: This button executes when the user submits their entries and clears the background
        color before any validation checks.
        """
        # Delete the button after submission
        self.SerialNumInput.configure(background='White')
        self.BumperNumInput.configure(background='White')
        self.ManuDateInput.configure(background='White')
        self.InstallDateInput.configure(background='White')
        
    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This button executes when the user wants to reset the values.
        """
        # Delete the entries
        self.dropConnectorSelection.set("")
        self.dropCarabType.set("")
        self.SerialNumInput.delete(0, END)
        self.BumperNumInput.delete(0, END)
        self.ManuDateInput.delete(0, END)
        self.InstallDateInput.delete(0, END)
        self.dropInUseSelection.set("")
        
        # Re-configure input entries to be disabled
        self.dropCarabType.configure(state='disabled')
        self.SerialNumInput.configure(state='disabled')
        self.BumperNumInput.configure(state='disabled')
        self.ManuDateInput.configure(state='disabled')
        self.InstallDateInput.configure(state='disabled')       
        self.dropInUseSelection.configure(state='disabled') 

        # Disable/enable the select, submit, and reset submit button
        self.btnSelectSubmit.configure(state='normal')
        self.btnReset.configure(state='disabled')
        self.btnSubmit.configure(state='disabled') 

        # Reset the radio button to its default value
        self.objRadioValue.set("serial")
        
        # Populate the dropdown based on default radio button selection
        self.Populate_Dropdown()

        # Re-Populate the dropdown menus 
        self.dropConnectorSelection["values"] = self.astrSerialNumList
        self.dropInUseSelection["values"] = self.aInUseSelectionList
        
        # Clear out the background colors and set to default as 'white'
        UpdateConnectorInfo.Clear_BG_Color(self)

        # Call the function to disable controls after submission
        self.Disable_After_Submit()
        
    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the updated Connectors Connector information to the db. 
        Else, reset
        """
        # Check if all of the inputs are valid
        global blnValidate 
        blnValidate = bool(False)
        
        # Clear out the background colors and set to default as 'white'
        UpdateConnectorInfo.Clear_BG_Color(self)
        
        # Get the blnValidate status
        blnValidate = UpdateConnectorInfo.Validate_InputFields(self)
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to update the Connector information?') is True:     
                # Load the user data and prep the data for db dump
                UpdateConnectorInfo.Get_UserInput(self)             
                Connectors.Update_NewConnectors_Query(self)
                
                # Check if the user would like to update another Connector
                if messagebox.askyesno(message='SUCCESSFUL UPDATE! \n\n Would you like to update another Connector?') is True:
                    # Clear the input fields and after data is submitted to the database
                    UpdateConnectorInfo.Reset(self)
                else:
                    UpdateConnectorInfo.Exit(self)

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()


#######################################################################################################
# Connector Inspection Results Class
#######################################################################################################   

class ConnectorInspectionResults(tk.Tk):
    """
    Class Name: ConnectorInspectionResults
    Class Description: This class is to display the selected inspection components to the user before the 
    data is dumped to the db. User must complete all previous inspection selection modules in order to submit
    data to the database for a standard inspection.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new unit inspection. Display a message
        to the user regarding the protocol for each inspection. User must click 'Check' Button in order to submit
        the data to the db.
        """
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (610/2)     
        self.y = (self.heightSize/2) - (280/2)    
                        
        # Create the Window attributes                
        self.title("Inspection Results")
        self.geometry('%dx%d+%d+%d' % (610, 280, self.x, self.y))
        self.resizable(False, False)

        # Create the scrollbar frame
        self.scrollFrame = LabelFrame(self, text='Results')
        self.scrollFrame.place(x=5, width=600, height=230)  # Adjusted the y-coordinate
        self.resultCanvas = Canvas(self.scrollFrame)
        self.resultCanvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.resultScrollBar = Scrollbar(self.scrollFrame, orient=VERTICAL, command=self.resultCanvas.yview)
        self.resultScrollBar.pack(side=RIGHT, fill=Y)
        self.resultCanvas.configure(yscrollcommand=self.resultScrollBar.set)
        self.resultCanvas.bind('<Configure>', lambda event: self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all")))

        # Create the third frame to hold the result fields
        self.resultFrame = Frame(self.resultCanvas)
        self.resultCanvas.create_window((0,0), window=self.resultFrame, anchor='nw')
        
        # Bind mousewheel scrolling
        self.resultCanvas.bind_all("<MouseWheel>", self.on_vertical_scroll)

        # Create the label for the drop down menu lists
        self.lblConnectorType = Label(self.resultFrame, text="Connector Type:")
        self.lblSerialNum = Label(self.resultFrame, text="Serial Number:")
        self.lblBumperNum = Label(self.resultFrame, text="Bumper Number:")
        self.lblManuName = Label(self.resultFrame, text="Manufacture Name:")
        self.lblManDate = Label(self.resultFrame, text="Manufacture Date:")
        self.lblInstallDate= Label(self.resultFrame, text="Install Date:")
        self.lblLastInsDate = Label(self.resultFrame, text="Last Inspection Date:")
        self.lblNextInsDate = Label(self.resultFrame, text="Next Inspection Date:")
        self.lblInUse = Label(self.resultFrame, text="Device In Use:")
        self.lblConnectorLocation = Label(self.resultFrame, text="Connector Location:")
        self.lblConnectorLine = Label(self.resultFrame, text="----------------------------------")
        self.lblConnectorVisual = Label(self.resultFrame, text="Visual Component:")
        self.lblConnectorPhysical = Label(self.resultFrame, text="Physical Component:")        
        self.lblConnectorFunct = Label(self.resultFrame, text="Function Component:")
        self.lblConnectorVisualStatus = Label(self.resultFrame, text="Visual Status:")
        self.lblConnectorPhysicalStatus = Label(self.resultFrame, text="Physical Status:")
        self.lblConnectorFunctStatus = Label(self.resultFrame, text="Function Status:")

        # Create the label locations
        self.lblConnectorType.grid(row=0, padx=50,  column=0, sticky='W') 
        self.lblSerialNum.grid(row=1, padx=50,  column=0, sticky='W')
        self.lblBumperNum.grid(row=2, padx=50,  column=0, sticky='W')
        self.lblManuName.grid(row=3, padx=50, column=0, sticky='W')
        self.lblManDate.grid(row=4, padx=50,  column=0, sticky='W')
        self.lblInstallDate.grid(row=5, padx=50,  column=0, sticky='W')
        self.lblLastInsDate.grid(row=6, padx=50,  column=0, sticky='W')
        self.lblNextInsDate.grid(row=7, padx=50,  column=0, sticky='W')        
        self.lblInUse.grid(row=8, padx=50,  column=0, sticky='W') 
        self.lblConnectorLocation.grid(row=9, padx=50,  column=0, sticky='W') 
        self.lblConnectorLine.grid(row=10, padx=50,  column=0, sticky='W') 
        self.lblConnectorVisual.grid(row=11, padx=50,  column=0, sticky='W') 
        self.lblConnectorPhysical.grid(row=12, padx=50,  column=0, sticky='W') 
        self.lblConnectorFunct.grid(row=13, padx=50,  column=0, sticky='W') 
        self.lblConnectorVisualStatus.grid(row=14, padx=50,  column=0, sticky='W') 
        self.lblConnectorPhysicalStatus.grid(row=15, padx=50,  column=0, sticky='W') 
        self.lblConnectorFunctStatus.grid(row=16, padx=50,  column=0, sticky='W') 

        # Create the output boxes to display the results as normal
        self.ConnectorTypeOutput = Entry(self.resultFrame, width=40, state='normal')
        self.SerialNumOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BumperNumOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ManuNameOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ManDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.InstallDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.LastInsDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.NextInsDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.InUseOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorLocationOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorVisualOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorPhysicalOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorFunctOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorVisStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorPhysStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ConnectorFunctStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        
        # Set the last and next inspection date based off of the current date
        aDateResult = BaseFunctions.Update_Inspection_Date()
        LastInspectionDate = datetime.strftime(aDateResult[0], '%Y-%m-%d')
        NextInspectionDate = datetime.strftime(aDateResult[1], '%Y-%m-%d')
                
        # Set the values to the output boxes 
        self.ConnectorTypeOutput.insert(0, Connectors.strDeviceType)
        self.SerialNumOutput.insert(0, Connectors.strSerialNum)
        self.BumperNumOutput.insert(0, Connectors.strBumperNum)
        self.ManuNameOutput.insert(0, Connectors.strManufactureName)
        self.ManDateOutput.insert(0, Connectors.dtmManufactureDate)
        self.InstallDateOutput.insert(0, Connectors.dtmInstallationDate)
        self.LastInsDateOutput.insert(0, LastInspectionDate)
        self.NextInsDateOutput.insert(0, NextInspectionDate)
        self.InUseOutput.insert(0, Connectors.strEquipInUse)
        self.ConnectorLocationOutput.insert(0, WallLocation.strWallLocationDesc)
        self.ConnectorVisualOutput.insert(0, ConnectorVisSelection.strConnectorVisMetalSelect)
        self.ConnectorPhysicalOutput.insert(0, ConnectorPhysSelection.strConnectorPhysMetalSelect)
        self.ConnectorFunctOutput.insert(0, ConnectorFunctSelection.strConnectorFunctSelect)
        self.ConnectorVisStatusOutput.insert(0, ConnectorVisSelection.strConnectorVisStatus)
        self.ConnectorPhysStatusOutput.insert(0, ConnectorPhysSelection.strConnectorPhysStatus)
        self.ConnectorFunctStatusOutput.insert(0, ConnectorFunctSelection.strConnectorFunctStatus)

        # Create the output boxes to display the results as readonly after the inputs have been placed
        self.ConnectorTypeOutput.configure(state='readonly')
        self.SerialNumOutput.configure(state='readonly')
        self.BumperNumOutput.configure(state='readonly')
        self.ManuNameOutput.configure(state='readonly')
        self.ManDateOutput.configure(state='readonly')
        self.InstallDateOutput.configure(state='readonly')
        self.LastInsDateOutput.configure(state='readonly')
        self.NextInsDateOutput.configure(state='readonly')
        self.InUseOutput.configure(state='readonly')
        self.ConnectorLocationOutput.configure(state='readonly')
        self.ConnectorVisualOutput.configure(state='readonly')
        self.ConnectorPhysicalOutput.configure(state='readonly')
        self.ConnectorFunctOutput.configure(state='readonly')
        self.ConnectorVisStatusOutput.configure(state='readonly')
        self.ConnectorPhysStatusOutput.configure(state='readonly')
        self.ConnectorFunctStatusOutput.configure(state='readonly')
        
        # Create the grid for the drop down menu list objects
        self.ConnectorTypeOutput.grid(row=0, column=1)
        self.SerialNumOutput.grid(row=1, column=1)   
        self.BumperNumOutput.grid(row=2, column=1) 
        self.ManuNameOutput.grid(row=3, column=1)  
        self.ManDateOutput.grid(row=4, column=1) 
        self.InstallDateOutput.grid(row=5, column=1)
        self.LastInsDateOutput.grid(row=6, column=1) 
        self.NextInsDateOutput.grid(row=7, column=1)   
        self.InUseOutput.grid(row=8, column=1)
        self.ConnectorLocationOutput.grid(row=9, column=1)
        self.ConnectorVisualOutput.grid(row=11, column=1)
        self.ConnectorPhysicalOutput.grid(row=12, column=1)
        self.ConnectorFunctOutput.grid(row=13, column=1)
        self.ConnectorVisStatusOutput.grid(row=14, column=1)
        self.ConnectorPhysStatusOutput.grid(row=15, column=1)
        self.ConnectorFunctStatusOutput.grid(row=16, column=1)
        
        # Create the buttons
        self.btnExit = Button(self, text="Exit", width=10, command=self.Exit)
        self.btnSubmit = Button(self, text="Submit", width=10, command=self.Submit)
        self.btnBack = Button(self, text="Back", width=10, command=self.Back)
            
        # Create the position of the button
        self.btnBack.place(x=140, y=240)
        self.btnSubmit.place(x=270, y=240)
        self.btnExit.place(x=400, y=240)

        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()    

        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the stored data in the class attributes
        StandardConnectorInspect.Delete_StandConnectorInspect_Data(self)
                
        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)
        Connectors_Menu()         

    def on_vertical_scroll(self, event):
        """Scroll the canvas vertically using the mouse wheel."""
        self.resultCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the new location to the db. Else, reset
        """
        # Check first with the user if the entry's are correct before dumping to DB
        if messagebox.askyesno(message='CAUTION! \n\n Proceed to submit Connector inspection?') is True:     
            # Load the user data and prep the data for db dump
            ConnectorInspectionResults.Submit_Standard_Inspection(self)
            
            # Check if the user would like to add another inspection
            if messagebox.askyesno(message='SUCCESSFUL UPLOAD! \n\n Would you like to complete another inspection?') is True:
                # Clear the input fields and after data is submitted to the database
                ConnectorInspectionResults.Exit(self)
                if Bool_Flag.blnComplexWith_Two_ConnectorFlag is True:
                    BelayDeviceSelection()
                else:
                    ConnectorSelection()
            else:
                ConnectorInspectionResults.Exit(self)
                Connectors_Menu()
        else:
            pass  

    def Submit_Standard_Inspection(self):
        """ 
        Function Name: Submit_Standard_Inspection
        Function Purpose: This function is executed once the user clicks on the submit button and all the standard
        inspection data cached arrays will be pulled and dumped into the the database
        """    
        # Set the global Connector Attributes
        Connectors.Update_Connectors_Inspect_Dates(Connectors)        
        
        # Commit the Connector Inspection data to the database
        ConnectorVisSelection.Add_ConnectorVisSelectList_Query(self)
        ConnectorPhysSelection.Add_ConnectorPhysSelectList_Query(self)
        ConnectorFunctSelection.Add_ConnectorFunctSelection_Query(self)
        ConnectorVisualInspect.Add_ConnectorVisualInspect_Query(self)
        ConnectorPhysicalInspect.Add_ConnectorPhysicalInspect_Query(self)
        ConnectorFunctionInspect.Add_ConnectorFunctInspect_Query(self)
        StandardConnectorInspect.Add_StandConnectorInspect_Query(self)
        
        # Get the Connector overall status and update the units in use status 
        Connectors.Update_Connectors_InUse_Status(Connectors)
        
        # Commit the ConnectorInspect data to the database
        ConnectorInspect.Add_ConnectorInspection_Query(self)
        ConnectorInspect.Add_ConnectorInspector_Query(self)
        ConnectorInspect.Add_ConnectorLocation_Query(self)
        
        # First check if the unit has been packaged for reservice to add report to db
        if Bool_Flag.Get_ConnectorRetired_Bool_Value(Bool_Flag) is True:
            ConnectorsRetiredReport.Add_Connector_RetiredReport_Query(self)
        
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)
        
        # Delete the stored data in the class attributes
        StandardConnectorInspect.Delete_StandConnectorInspect_Data(self)       
        ConnectorsRetiredReport.Delete_Connector_RetiredReport_Data(self)
        Start_Menu.Delete_Obj_Lists(self)        

        # Reload the object lists
        Start_Menu.Load_Obj_Lists(Start_Menu)
                
    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Expose the window widget to the user
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """     
        # Hide the current window
        self.Exit()  

        # Show the main window after the new window is closed
        ConnectorInspection()

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
                            

#######################################################################################################
# Belay Device Menu Class
#######################################################################################################        

class BelayDevices_Menu(tk.Tk):
    """
    Class Name: BelayDevices_Menu
    Class Description: This class is for the BelayDevices main menu. 
    """
    def __init__(self, ):
        # Load the data from the database
        Start_Menu.Load_Obj_Lists(self)
        
        # Create the root tkinter variable
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (560/2)     
        self.y = (self.heightSize/2) - (330/2)
                        
        # Create the Window attributes
        self.WindowTitle = self.title("Belay Device Menu")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (560, 330, self.x, self.y))
        self.WindowSize = self.resizable(False, False)
        
        # Create the frame for the buttons
        self.btnFrame = LabelFrame(self, text='Menu Selection')
        self.btnFrame.place(x=160, y=15, width=250, height=285)

        # Create the Buttons
        self.btnNewInspect = Button(self.btnFrame, width=25, text = "New Inspection", command=lambda:BelayDevices_Menu.Open_NewInspection(self))        
        self.btnViewFutureInspectDate = Button(self.btnFrame, width=25, text = "View Future Inspection Dates", command=lambda:BelayDevices_Menu.Open_ViewLastNext_InspectionDates(self))
        self.btnViewBelayDeviceDates = Button(self.btnFrame, width=25, text = "View Belay Device Dates", command=lambda:BelayDevices_Menu.Open_BelayDeviceDates(self))
        self.btnViewBelayDeviceInfo = Button(self.btnFrame, width=25, text = "View Belay Device Info", command=lambda:BelayDevices_Menu.Open_BelayDeviceInfo(self))
        self.btnViewBelayDeviceWallLocation = Button(self.btnFrame, width=25, text = "View Belay Device Wall Locations", command=lambda:BelayDevices_Menu.Open_BelayDevice_WallLocations(self))
        self.btnDownloadReport = Button(self.btnFrame, width=25, text = "Download Reports", command=lambda:BelayDevices_Menu.Open_DownloadReports(self))
        self.btnOpenReport = Button(self.btnFrame, width=25, text = "Open Reports", command=lambda:BelayDevices_Menu.Open_Records_Dir(self))
        self.btnExit = Button(self.btnFrame, width=25, text = "Home", command=lambda:BelayDevices_Menu.Exit(self))

        # Create the button grid
        self.btnNewInspect.grid(row=1, column=1, padx=29, pady=3)
        self.btnViewFutureInspectDate.grid(row=2, column=1, pady=3)
        self.btnViewBelayDeviceDates.grid(row=3, column=1, pady=3)
        self.btnViewBelayDeviceInfo.grid(row=4, column=1, pady=3)
        self.btnViewBelayDeviceWallLocation.grid(row=5, column=1, pady=3)
        self.btnDownloadReport.grid(row=6, column=1, pady=3)
        self.btnOpenReport.grid(row=7, column=1, pady=3)
        self.btnExit.grid(row=8, column=1, pady=3)
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()  
        
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)   
        
        # Send the user back to the main menu        
        Start_Menu()

    def Open_NewInspection(self):
        """ 
        Function Name: Open_NewInspection
        Function Purpose: This function is executed if the user clicks new inspection button. The 
        call is to the inspection class and will execute and add a new inspection to the database.
        """
        # Delete the root window
        self.destroy()
        
        # Open the New Inspection Window
        BelayDeviceSelection()

    def Open_ViewLastNext_InspectionDates(self):
        """ 
        Function Name: Open_ViewLastNext_InspectionDates
        Function Purpose: This function is executed if the user clicks view BelayDevice Next/Last inspection dates button. 
        """
        # Delete the root window
        self.destroy()
        
        # Determine the Caller_ID based on the class
        Caller_ID = "BelayDevice"
        
        # Open the add new location window
        View_LastNext_InspectDate(Class_CallerID=Caller_ID)

    def Open_BelayDeviceDates(self):
        """ 
        Function Name: Open_BelayDeviceDates
        Function Purpose: This function is executed if the user clicks View BelayDevice Dates button. 
        """
        # Delete the root window
        self.destroy()
        
        # Determine the Caller_ID based on the class
        Caller_ID = "BelayDevice"
                        
        # Open the view location window
        View_ItemDates(Class_CallerID=Caller_ID)  

    def Open_BelayDeviceInfo(self):
        """ 
        Function Name: Open_BelayDeviceInfo
        Function Purpose: This function is executed if the user clicks View BelayDevice Info button. 
        """
        # Delete the root window
        self.destroy()
        
        # Determine the Caller_ID based on the class
        Caller_ID = "BelayDevice"
                        
        # Open the view location window
        View_Device_Info(Class_CallerID=Caller_ID) 

    def Open_BelayDevice_WallLocations(self):
        """ 
        Function Name: Open_BelayDevice_WallLocations
        Function Purpose: This function is executed if the user clicks View BelayDevice Wall Locations button. 
        """
        # Delete the root window
        self.destroy()
        
        # Determine the Caller_ID based on the class
        Caller_ID = "BelayDevice"
                        
        # Open the view location window
        View_Item_WallLocations(Class_CallerID=Caller_ID)  

    def Open_BelayDevice_OutOfService(self):
        """ 
        Function Name: Open_BelayDevice_OutOfService
        Function Purpose: This function is executed if the user clicks View BelayDevice Retired button. 
        """
        # Delete the root window
        self.destroy()
        
        # Open the view location window
        View_AutoBelay_WallLocations() 
        
    def Open_Records_Dir(self):
        """ 
        Function Name: Open_Records_Dir
        Function Purpose: This function is executed if the user clicks Open Report Information button. 
        """
        # Open the send reports window
        Records.Open_Records_Dir()   
        
    def Open_DownloadReports(self):
        """ 
        Function Name: Open_DownloadReports
        Function Purpose: This function executes whenever the user clicks the 'Download Reports' button. This function
        pulls from the db specific views and downloads the views to a desired directory. Each file is saved as an excel
        file. 
        """
        Queries.Download_Files(Queries, user_triggered=True)       
        messagebox.showwarning(message='SUCCESSFUL DOWNLOAD \n\n All files have been downloaded to the Records Directory.', icon='warning')
        
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed if the user clicks exit button. The main menu will
        exit once this button is clicked and will return the user to the login page.
        """
        # Delete the root window
        self.destroy()
        
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)  
        
        # Send the user back to the main menu   
        Start_Menu()
        

#######################################################################################################
# BelayDevice Selection Class
#######################################################################################################   

class BelayDeviceSelection(tk.Tk, BelayDevices):
    """
    Class Name: BelayDeviceSelection
    Class Description: This class is to conduct BelayDevice Selection.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new BelayDevice Selection. User must click
        'Next' Button in order to progress to the next inspection type.
        """
        # Load the data from the database
        # Start_Menu.Load_Obj_Lists(self) # Make sure to comment this out after testing
        
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (650/2)     
        self.y = (self.heightSize/2) - (410/2)          
        
        # Create the Window attributes                
        self.title("Belay Device Selection")
        self.geometry('%dx%d+%d+%d' % (650, 410, self.x, self.y))
        self.resizable(False, False)

        # Load the query selection widget
        self.Selection_Widget()
        
        # Create the frame fields
        self.typeFrame = tk.LabelFrame(self, text="Additional Info")
        self.typeFrame.place(x=100, y=140, width=450, height=200)
                
        # Create the label for the checkboxes
        self.lblBelayDeviceLocation = tk.Label(self.typeFrame, text="Belay Device Location:")
        self.lblInUse = tk.Label(self.typeFrame, text="Device In Use:")
        self.lblQuestion = tk.Label(self.typeFrame, text="Can't find what you're looking for?")
                        
        # Create the label locations
        self.lblBelayDeviceLocation.place(x=25, y=15)
        self.lblInUse.place(x=70, y=55)
        self.lblQuestion.place(x=125, y=95)

        # Create the drop down menu list for each attribute
        self.dropBelayDeviceLocation = ttk.Combobox(self.typeFrame, values=WallLocation.astrWallLocationDesc, state='readonly')
        self.dropInUse = ttk.Combobox(self.typeFrame, values=['Yes', 'No'], state='readonly')
        
        # Create the drop down menu size for each attribute
        self.dropBelayDeviceLocation.configure(width=25)
        self.dropInUse.configure(width=25)
        
        # Create the grid for the drop down menu list objects
        self.dropBelayDeviceLocation.place(x=190, y=15)  
        self.dropInUse.place(x=190, y=55)  

        if Bool_Flag.blnComplexWithBelayDeviceFlag is True:
            # Disable the drop location if this class is called from ropes inspection
            self.dropBelayDeviceLocation.set(WallLocation.strWallLocationDesc)
            self.dropInUse.set("Yes")
            self.dropBelayDeviceLocation.configure(state='disabled')
            self.dropInUse.configure(state='disabled')
            
        # Check if the cache values for any drop menus have been previously selected and set the values
        if Bool_Flag.blnBelayDevicePersistFlag == True:
            if (Bool_Flag.blnSerialNumRadioSelect == True):
                self.Set_Previous_Drop_List(BelayDevices.strSerialNum, self.dropBelayDeviceSelection)
            else:
                self.objRadioValue.set("bumper")
                self.dropBelayDeviceSelection["values"] = self.astrBumperNumList
                self.Set_Previous_Drop_List(BelayDevices.strBumperNum, self.dropBelayDeviceSelection)
            self.Set_Previous_Drop_List(BelayDevices.strEquipInUse, self.dropInUse)
            self.Set_Previous_Drop_List(WallLocation.strWallLocationDesc, self.dropBelayDeviceLocation)
            
        # Create the buttons
        self.btnUpdateBelayDeviceInfo = Button(self.typeFrame, width=12, text = "Update Device", command=self.Update_BelayDevices_Info)
        self.btnAddBelayDevice = Button(self.typeFrame, width=12, text="Add Device", command=self.Add_BelayDevice)
        self.btnAddLocation = Button(self.typeFrame, width=12, text = "Add Location", command=self.Add_Location)
        self.btnExit = Button(self, width=10, text="Back", command=self.Back)
        self.btnReset = Button(self, width=10, text="Reset",command=self.Reset)
        self.btnNext = Button(self, width=10, text="Next", command=self.Next)
            
        # Create the position of the button
        self.btnUpdateBelayDeviceInfo.place(x=40, y=140)
        self.btnAddBelayDevice.place(x=175, y=140) 
        self.btnAddLocation.place(x=310, y=140)
        self.btnExit.place(x=170, y=360) 
        self.btnNext.place(x=400, y=360) 
        self.btnReset.place(x=285, y=360)
        
        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()

        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the object lists
        Start_Menu.Delete_Obj_Lists(self)
        
        if Bool_Flag.blnComplexWithBelayDeviceFlag is True:
            # Return back to the rope selection window
            GymRopeSelection()
        else:
            BelayDevices_Menu()
            
    def Selection_Widget(self):
        """ 
        Function Name: Selection_Widget
        Function Purpose: This function populates the search by widget for Serial or Bumper Num search.
        """           
        # Create the first frame to hold the input fields
        self.selectInput = LabelFrame(self, text="Select Belay Device")
        self.selectInput.place(x=100, y=35, width=450, height=100)

        # Create the labels 
        self.lblSearchByBelayDeviceID = Label(self.selectInput, text="Query by Device ID:")
        self.lblBelayDeviceSelection = Label(self.selectInput, text="Device ID Selection:")

        # Create the label locations
        self.lblSearchByBelayDeviceID.place(x=40, y=5)
        self.lblBelayDeviceSelection.place(x=40, y=40)

        # Create variables to hold the value of the selected radio button
        self.objRadioValue = tk.StringVar(value='serial')
        self.objComboValue = tk.StringVar()

        # List objects of serial and bumper values
        self.astrSerialNumList = self.astrSerialNumCache
        self.astrBumperNumList = self.astrBumperNumCache

        # Create the radio buttons
        self.rbSerial = tk.Radiobutton(self.selectInput, text="Serial Number", variable=self.objRadioValue, value="serial", command=self.Populate_Dropdown)
        self.rbBumper = tk.Radiobutton(self.selectInput, text="Bumper Number", variable=self.objRadioValue, value="bumper", command=self.Populate_Dropdown)

        # Place the radio buttons next to each other using .place()
        self.rbSerial.place(x=190, y=5)
        self.rbBumper.place(x=300, y=5)
                    
        # Create the entry input box
        self.dropBelayDeviceSelection = ttk.Combobox(self.selectInput, values=self.astrSerialNumList, state='readonly')
        self.dropBelayDeviceSelection.configure(width=25,)

        # Populate the dropdown based on the default radio button selection
        self.Populate_Dropdown()

        # Create the grid for all of the entry input fields
        self.dropBelayDeviceSelection.place(x=190, y=40) 

    def Populate_Dropdown(self):
        """ 
        Function Name: Populate_Dropdown
        Function Purpose: This function populates the dropdown based on the radio button selection.
        """           
        if self.objRadioValue.get() == "serial":
            self.dropBelayDeviceSelection["values"] = self.astrSerialNumList
        else:
            self.dropBelayDeviceSelection["values"] = self.astrBumperNumList
        self.dropBelayDeviceSelection.set("")                                  
        
    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)
        
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.', icon='warning')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate
    
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)  

        # Check the user input
        blnValidate = BelayDeviceSelection.Check_Input(self.dropBelayDeviceSelection.get())

        # Check if the input is valid
        if (blnValidate is True):
            # Check the user input
            blnValidate = BelayDeviceSelection.Check_Input(self.dropBelayDeviceLocation.get())         
            
            # Check if the input is valid
            if (blnValidate is True):
                # Check the user input
                blnValidate = BelayDeviceSelection.Check_Input(self.dropInUse.get())         
                
                # Check if the input is valid
                if (blnValidate is True):
                    blnValidate = True
                else:
                    # Return blnValidate as False
                    blnValidate = False
                    self.dropInUse.focus()
            else:
                # Return blnValidate as False
                blnValidate = False
                self.dropBelayDeviceLocation.focus()                                                
        else:
            # Return blnValidate as False
            blnValidate = False
            self.dropBelayDeviceSelection.focus()

        return blnValidate            

    def Next_Inspection(self):
        """ 
        Function Name: Next_Inspection
        Function Purpose: This function is executed once the user clicks on Next button to move to the nex inspection
        type window. Withdraw the parent window and load the new window.
        """           
        # Hide the main window
        self.Exit()  

        # Open the new window
        BelayDeviceInspection()

    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the root
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Hide the current window
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the root
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """     
        # Hide the current window
        self.Exit()  

        if Bool_Flag.blnComplexWithBelayDeviceFlag is True:
            if Bool_Flag.blnComplexWith_Two_ConnectorFlag is True:
                TwoConnectorInspection()
            elif Bool_Flag.blnComplexWithConnectorFlag is True:
                ConnectorInspection()
            else:
                # Return back to the rope selection window
                GymRopeSelection()
        else:
            # Delete the object lists
            Start_Menu.Delete_Obj_Lists(self)
                        
            # Set all the bool values back to False
            Start_Menu.Set_Default_Bool_Values(self)            
            BelayDevices_Menu()

    def Update_Dropdown_Values(self):
        """ 
        Function Name: Update_Dropdown_Values
        Function Purpose: This function is executed once the user clicks on AddBelayDevice or AddLocation button and updates the drop down
        object list with the new values.
        """  
        # Ensure the dropdowns are Comboboxes and clear their current selections
        if isinstance(self.dropBelayDeviceSelection, ttk.Combobox):
            self.dropBelayDeviceSelection.set("") 
        if isinstance(self.dropBelayDeviceLocation, ttk.Combobox):
            self.dropBelayDeviceLocation.set("")

        # Update the values for connector selection dropdown
        self.astrSerialNumList = BelayDevices.astrSerialNumCache
        self.astrBumperNumList = BelayDevices.astrBumperNumCache
        if isinstance(self.dropBelayDeviceSelection, ttk.Combobox):
            self.dropBelayDeviceSelection['values'] = self.astrSerialNumList

        # Update the values for connector location dropdown
        if isinstance(self.dropBelayDeviceLocation, ttk.Combobox):
            self.dropBelayDeviceLocation['values'] = WallLocation.astrWallLocationDesc

        if Bool_Flag.blnComplexWithBelayDeviceFlag is True:
            # Disable the drop location if this class is called from ropes inspection
            self.dropConnectorLocation.set(WallLocation.strWallLocationDesc)
            self.dropConnectorLocation.configure(state='disabled')

        # # Populate the dropdown menus
        # self.dropBelayDeviceSelection.set("") 
        # self.astrSerialNumList = BelayDevices.astrSerialNumCache
        # self.astrBumperNumList = BelayDevices.astrBumperNumCache
        # self.dropBelayDeviceSelection['values'] = self.astrSerialNumList
        # self.dropBelayDeviceLocation['values'] = WallLocation.astrWallLocationDesc

    def Add_BelayDevice(self):
        """ 
        Function Name: Add_BelayDevice
        Function Purpose: This function is executed once the user clicks on AddBelayDevice button and updates the drop down
        object list with the new values.
        """           
        # Hide the main window
        self.Withdraw()  

        # Call your AddBelayDevice function here
        newWindow = AddBelayDevice(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Show the main window after the new window is closed
        self.Deiconify()  

        # Update the drop-down menu values
        self.Update_Dropdown_Values()

    def Update_BelayDevices_Info(self):
        """ 
        Function Name: Update_BelayDevices_Info
        Function Purpose: This function is executed if the user clicks Update BelayDevices Information button. 
        """
        # Hide the main window
        self.Withdraw()  

        # Call your AddBelayDevice function here
        newWindow = UpdateBelayDeviceInfo(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Show the main window after the new window is closed
        self.Deiconify()  

        # Update the drop-down menu values
        self.Update_Dropdown_Values()
        
    def Add_Location(self):
        """ 
        Function Name: Add_Location
        Function Purpose: This function is executed once the user clicks on AddLocation button and updates the drop down
        object list with the new values.
        """           
        # Hide the main window
        self.Withdraw()  

        # Call your AddLocation function here
        newWindow = AddLocation(self)

        # Wait for the new window to close
        newWindow.wait_window()

        # Show the main window after the new window is closed
        self.Deiconify()  

        # Update the drop-down menu values
        self.Update_Dropdown_Values()

    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        """   
        # Get the selected values from the drop menus
        if self.dropBelayDeviceSelection.get() in BelayDevices.astrSerialNumCache:
            SerialNum = self.dropBelayDeviceSelection.get()
            Bool_Flag.Set_SerialRadio_Bool_Value_True(Bool_Flag)
        else:
            intPrimID = BelayDevices.astrBumperNumCache.index(self.dropBelayDeviceSelection.get()) + 1
            SerialNum = BelayDevices.astrSerialNumCache[intPrimID]
            Bool_Flag.Set_BumperRadio_Bool_Value_True(Bool_Flag)
            
        BelayDeviceLocation = self.dropBelayDeviceLocation.get()
        InUseStatus = self.dropInUse.get()

        # Commit the data to load the BelayDevices class objects with the data from the db
        BelayDevices.strSerialNum = SerialNum
        BelayDevices.strEquipInUse = InUseStatus
        BelayDevices.Set_BelayDevices_Selection(BelayDevices)

        # Commit the data to load the WallLocation class objects with the data from the db
        WallLocation.strWallLocationDesc = BelayDeviceLocation
        WallLocation.Get_WallLocation_Selection(WallLocation)

    def Next(self):
        """ 
        Function Name: Next
        Function Purpose: This function is executed once the user clicks on the "Next" button. Once the inputs 
        are validated, the inspection results loads the user selected data and is retained at the object class locations 
        before committing to the database. If all inputs are valid and confirmed by the user, the next stage of inspections is executed.
        """
        global blnValidate
        blnValidate = bool(False)             
        
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

    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This function is executed once the user clicks on the reset button inside the root
        frame. If the user clicks 'Reset', all data is set back to default.
        """     
        # Set the list objects first element to the drop click object
        self.dropBelayDeviceSelection.set("")
        self.dropBelayDeviceLocation.set("")
        self.dropInUse.set("")

        # Reset the radio button to its default value
        self.objRadioValue.set("serial")

        # Populate the dropdown based on default radio button selection
        self.Populate_Dropdown()

        # Re-Populate the dropdown menus 
        self.dropBelayDeviceSelection["values"] = self.astrSerialNumList
        
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        

        
# #######################################################################################################
# # Add New BelayDevice Class
# ####################################################################################################### 

class AddBelayDevice(tk.Toplevel, BelayDevices):
    """
    Class Name: AddBelayDevice
    Class Description: This class adds a new BelayDevice to the database.
    """
    def __init__(self, parent):
        # Load the data from the database
        # Start_Menu.Load_Obj_Lists(self) # Make sure to comment this out after testing
                                
        # Initialize the Toplevel window
        super().__init__(parent)

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (580/2)     
        self.y = (self.heightSize/2) - (325/2)    
                                        
        # Create the Window attributes
        self.title("Add New BelayDevice")
        self.geometry('%dx%d+%d+%d' % (580, 325, self.x, self.y))
        self.resizable(False, False)

        # Create the second frame to hold the input fields
        self.frameInput = tk.LabelFrame(self, text="Belay Device Credentials")
        self.frameInput.place(x=90, y=10, width=405, height=255)

        # Create the labels 
        self.lblDeviceName = tk.Label(self.frameInput, text="Device Name:")
        self.lblManuName = tk.Label(self.frameInput, text="Manufacture Name:")
        self.lblSerialNum = tk.Label(self.frameInput, text="Serial Number:")
        self.lblBumperNum = tk.Label(self.frameInput, text="Bumper Number:")      
        self.lblManuDate = tk.Label(self.frameInput, text="Manufacture Date:")
        self.lblInstallDate = tk.Label(self.frameInput, text="Install Date:")
        self.lblBelayDeviceType = tk.Label(self.frameInput, text="Belay Device Type:")
        self.lblBelayDeviceInUse = tk.Label(self.frameInput, text="Belay Device In Use:")

        # Create the label locations
        self.lblDeviceName.grid(row=0, column=0, sticky='W', padx=5)
        self.lblManuName.grid(row=1, column=0, sticky='W', padx=5)
        self.lblSerialNum.grid(row=2, column=0, sticky='W', padx=5)
        self.lblBumperNum.grid(row=3, column=0, sticky='W', padx=5)
        self.lblManuDate.grid(row=4, column=0, sticky='W', padx=5)
        self.lblInstallDate.grid(row=5, column=0, sticky='W', padx=5)
        self.lblBelayDeviceType.grid(row=6, column=0, sticky='W', padx=5)
        self.lblBelayDeviceInUse.grid(row=7, column=0, sticky='W', padx=5)

        # Create the entry input box
        self.DeviceNameInput = Entry(self.frameInput, width=40)
        self.ManuNameInput = Entry(self.frameInput, width=40)
        self.SerialNumInput = Entry(self.frameInput, width=40)
        self.BumperNumInput = Entry(self.frameInput, width=40)
        self.ManuDateInput = Entry(self.frameInput, width=40)
        self.InstallDateInput = Entry(self.frameInput, width=40)

        # Create the grid for all of the entry input fields
        self.DeviceNameInput.grid(row=0, column=1, padx=25, pady=5)
        self.ManuNameInput.grid(row=1, column=1, padx=5)
        self.SerialNumInput.grid(row=2, column=1, pady=5)
        self.BumperNumInput.grid(row=3, column=1, pady=5)
        self.ManuDateInput.grid(row=4, column=1, pady=5)
        self.InstallDateInput.grid(row=5, column=1, pady=5)

        # Create the drop down menu list objects
        self.dropDeviceType = ttk.Combobox(self.frameInput, values=['Manual Braking', 'Assisted Braking'], state='readonly')
        self.dropInUse = ttk.Combobox(self.frameInput, values=['Yes', 'No'], state='readonly')

        # Create the drop down menu size for each attribute
        self.dropDeviceType.configure(width=37)
        self.dropInUse.configure(width=37)
        
        # Create the grid for the drop down menu
        self.dropDeviceType.grid(row=6, column=1, padx=5, pady=5)
        self.dropInUse.grid(row=7, column=1, padx=5, pady=5)

        # Create a list of all the entry objects
        aEntryList = (self.ManuDateInput, self.InstallDateInput, self.BumperNumInput) 
        astrPlaceHolder = ("MM/DD/YYYY", "MM/DD/YYYY", "Optional")

        # Insert the placeholders at the desired entry points
        for i, entry in enumerate(aEntryList):
            entry.insert(0, astrPlaceHolder[i])
            entry.config(fg='grey')
            entry.bind('<FocusIn>', lambda event, entry=entry, placeholder=astrPlaceHolder[i]: self.On_Entry_Click(event, entry, placeholder))
            entry.bind('<FocusOut>', lambda event, entry=entry, placeholder=astrPlaceHolder[i]: self.On_FocusOut(event, entry, placeholder))
            
        # Create the buttons
        self.btnExit = Button(self, text="Back", width=10, command=lambda:AddBelayDevice.Exit(self))
        self.btnReset = Button(self, text="Reset", width=10, command=lambda:AddBelayDevice.Reset(self))
        self.btnSubmit = Button(self, text="Submit", width=10, command=lambda:AddBelayDevice.Submit(self))

        # Create the button grid
        self.btnExit.place(x=120, y=280)
        self.btnReset.place(x=250, y=280)
        self.btnSubmit.place(x=380, y=280)

    def On_Entry_Click(self, event, entry, strPlaceHolder):
        """ 
        Function Name: On_Entry_Click
        Function Purpose: This function gets called whenever entry is clicked by a user to start a new entry.
        """    
        if entry.get() == strPlaceHolder:
            entry.delete(0, "end") 
            entry.insert(0, '') 
            entry.config(fg='black')
            
    def On_FocusOut(self, event, entry, strPlaceHolder):
        """ 
        Function Name: On_FocusOut
        Function Purpose: This function gets called whenever the entry loses focus.
        """            
        if entry.get() == '':
            entry.insert(0, strPlaceHolder)
            entry.config(fg='grey') 
                                            
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate
        
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        def set_invalid(input_field):
            """
            Set the input field to show invalid data.
            """
            input_field.delete(0, tk.END)
            input_field.configure(background='Yellow')
            input_field.focus()

        # Validate Manufacturer Name
        if not (AddBelayDevice.Check_Input(self.DeviceNameInput.get()) and
                BaseFunctions.Validate_String_Input(self.DeviceNameInput.get())):
            set_invalid(self.DeviceNameInput)
            return False
        
        # Validate Manufacturer Name
        if not (AddBelayDevice.Check_Input(self.ManuNameInput.get()) and
                BaseFunctions.Validate_String_Input(self.ManuNameInput.get())):
            set_invalid(self.ManuNameInput)
            return False
        
        # Validate Serial Number
        if not (AddBelayDevice.Check_Input(self.SerialNumInput.get()) and
                BaseFunctions.Validate_Serial_Input(self.SerialNumInput.get()) and
                self.SerialNumInput.get() not in BelayDevices.astrSerialNumCache):
            set_invalid(self.SerialNumInput)
            return False

        # Get the Primary Key ID
        sqlPrimKey = ("TBelayDevices", "intBelayDeviceID")   
        self.BelayDeviceIDResult = self.Get_Or_Create_ID(self.SerialNumInput.get(), sqlPrimKey)
        
        # Validate Bumper Number if it exists
        bumper_num = self.BumperNumInput.get()
        if bumper_num != "" and not BaseFunctions.Validate_Serial_Input(bumper_num) and bumper_num not in BelayDevices.astrBumperNumCache:
            set_invalid(self.BumperNumInput)
            return False

        self.BumperNumInput.delete(0, tk.END)
        new_bumper_num_value = bumper_num if bumper_num != "" else 'Optional'
        self.BumperNumInput.insert(0, new_bumper_num_value)
        
        # Validate Manufacturing Date
        if not AddBelayDevice.Check_Input(self.ManuDateInput.get()):
            set_invalid(self.ManuDateInput)
            return False

        result_tup = BaseFunctions.Validate_Date_Input(self.ManuDateInput.get())
        if not result_tup[0]:
            set_invalid(self.ManuDateInput)
            return False

        self.ManuDateInputResult = AddBelayDevice.Change_Date_To_Format(self.ManuDateInput, result_tup)

        # Validate Installation Date
        if not AddBelayDevice.Check_Input(self.InstallDateInput.get()):
            set_invalid(self.InstallDateInput)
            return False

        result_tup = BaseFunctions.Validate_Date_Input(self.InstallDateInput.get())
        if not result_tup[0]:
            set_invalid(self.InstallDateInput)
            return False

        self.InstallDateResult = AddBelayDevice.Change_Date_To_Format(self.InstallDateInput, result_tup)

        # Validate dropDeviceType
        if not AddBelayDevice.Check_Input(self.dropDeviceType.get()):
            set_invalid(self.dropDeviceType)
            return False
                    
        # Validate 'In Use' Selection
        if not AddBelayDevice.Check_Input(self.dropInUse.get()):
            set_invalid(self.dropInUse)
            return False
        
        return True

    def Change_Date_To_Format(dtmObject, aResultTup):
        """ 
        Function Name: Change_Date_To_Format
        Function Purpose: This function is executed every call of the validation check to ensure the dates are all
        changed to the same format no matter if the character is valid.
        """ 
        dtmObject.delete(0, END)
        dtmObject.insert(0, aResultTup[1])
        dtmObject = aResultTup[1]

        return dtmObject

    def Get_UserInput(self):
        """ 
        Function Name: Get_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        Then the data will be sent to the db.
        """       
        # Get the current date for last and next inspection
        aDateResult = BaseFunctions.Update_Inspection_Date()
        lastDate = datetime.strftime(aDateResult[0], '%m/%d/%Y')
        nextDate =  datetime.strftime(aDateResult[1], '%m/%d/%Y')
        
        # Assign value to the objects
        BelayDeviceID = self.BelayDeviceIDResult
        SerialNum = self.SerialNumInput.get()
        BumperNum = self.BumperNumInput.get()
        ManufactureDate = self.ManuDateInputResult
        InstallationDate = self.InstallDateResult
        LastInspectionDate = lastDate
        NextInspectionDate = nextDate
        BelayDeviceType = self.dropDeviceType.get()
        BelayDeviceInUse = self.dropInUse.get()

        # If BumperNum = "Optional" place a 'None' string
        if BumperNum == "Optional":
            BumperNum = "None"
            
        # Capitalize the first letter of each word and append a space after splitting the user input into a list
        resultList = self.DeviceNameInput.get().split()
        self.Cap_DeviceName = [result.capitalize() for result in resultList]
        DeviceName = ' '.join(self.Cap_DeviceName)                

        resultList = self.ManuNameInput.get().split()
        self.Cap_ManuName = [result.capitalize() for result in resultList]
        ManuName = ' '.join(self.Cap_ManuName)                
        
        # Assign the local objects to the class objects
        self.intBelayDeviceID = BelayDeviceID
        self.strBelayDeviceName = DeviceName
        self.strSerialNum = SerialNum
        self.strBumperNum = BumperNum
        self.strManufactureName = ManuName
        self.dtmManufactureDate = ManufactureDate
        self.dtmInstallationDate = InstallationDate
        self.dtmLastInspectionDate = LastInspectionDate
        self.dtmNextInspectionDate = NextInspectionDate
        self.strDeviceType = BelayDeviceType
        self.strEquipInUse = BelayDeviceInUse

    def Get_Combined_Selection(self, persisted_array, default_value):
        """
        Function Name: Get_Combined_Selection
        Function Purpose: This function combines the array elements into a comma-separated string,
        and handles the case when the persisted array is empty by setting a default value.
        """
        if len(persisted_array) == 0:
            return default_value
        else:
            return ",".join(persisted_array)
        
    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
                        
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlStatement[0], sqlStatement[1]))    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
    
    def Clear_BG_Color(self):
        """ 
        Function Name: Clear_BG_Color
        Function Purpose: This button executes when the user submits their entries and clears the background
        color before any validation checks.
        """
        # Delete the button after submission
        self.DeviceNameInput.configure(background='White')
        self.ManuNameInput.configure(background='White')
        self.SerialNumInput.configure(background='White')
        self.BumperNumInput.configure(background='White')
        self.ManuDateInput.configure(background='White')
        self.InstallDateInput.configure(background='White')
        
    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This button executes when the user wants to reset the values.
        """
        # Delete the button after submission
        self.DeviceNameInput.delete(0, END)
        self.ManuNameInput.delete(0, END)
        self.SerialNumInput.delete(0, END)
        self.BumperNumInput.delete(0, END)
        self.ManuDateInput.delete(0, END)
        self.InstallDateInput.delete(0, END)
        
        # Reset the drop menus
        self.dropDeviceType.set("")
        self.dropInUse.set("")
        
        # Clear out the background colors and set to default as 'white'
        AddBelayDevice.Clear_BG_Color(self)

        # Create a list of all the entry objects
        aEntryList = (self.ManuDateInput, self.InstallDateInput, self.BumperNumInput) 
        astrPlaceHolder = ("MM/DD/YYYY", "MM/DD/YYYY", "Optional")

        # Insert the placeholders at the desired entry points
        for i, entry in enumerate(aEntryList):
            entry.insert(0, astrPlaceHolder[i])
            entry.config(fg='grey')
            entry.bind('<FocusIn>', lambda event, entry=entry, placeholder=astrPlaceHolder[i]: self.On_Entry_Click(event, entry, placeholder))
            entry.bind('<FocusOut>', lambda event, entry=entry, placeholder=astrPlaceHolder[i]: self.On_FocusOut(event, entry, placeholder))
            
    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the new BelayDevice BelayDevice to the db. Else, reset
        """
        # Check if all of the inputs are valid
        global blnValidate 
        blnValidate = bool(False)
        
        # Clear out the background colors and set to default as 'white'
        AddBelayDevice.Clear_BG_Color(self)
        
        # Get the blnValidate status
        blnValidate = AddBelayDevice.Validate_InputFields(self)
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to add new Belay Device?') is True:     
                # Load the user data and prep the data for db dump
                AddBelayDevice.Get_UserInput(self)
                BelayDevices.Add_BelayDevices_Query(self)                     

                # Check if the user would like to add another BelayDevice
                if messagebox.askyesno(message='SUCCESSFUL UPLOAD! \n\n Would you like to add another Belay Device?') is True:
                    # Clear the input fields and after data is submitted to the database
                    AddBelayDevice.Reset(self)
                else:
                    AddBelayDevice.Exit(self)
            else:
                pass
            
    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
                

#######################################################################################################
# Update BelayDevices Info
#######################################################################################################

class UpdateBelayDeviceInfo(tk.Toplevel, BelayDevices):
    """
    Class Name: UpdateBelayDeviceInfo
    Class Description: This class updates any Belay Device to the database.
    """
    def __init__(self, parent):
        # Load the data from the database
        # Start_Menu.Load_Obj_Lists(self) # Make sure to comment this out after testing
                
        # Initialize the Toplevel window
        super().__init__(parent)

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (560/2)     
        self.y = (self.heightSize/2) - (490/2)  
                                        
        # Create the Window attributes
        self.WindowTitle = self.title("Update Belay Device Information")
        self.WindowGeo = self.geometry('%dx%d+%d+%d' % (560, 490, self.x, self.y))
        self.WindowSize = self.resizable(False, False)

        # Load the query selection widget
        self.Selection_Widget()
                
        # Create the second frame to hold the input fields
        self.frameInput = LabelFrame(self, text="Belay Device Credentials")
        self.frameInput.place(x=75, y=170, width=405, height=260)

        # Create the labels 
        self.lblDeviceName = tk.Label(self.frameInput, text="Device Name:")
        self.lblManuName = tk.Label(self.frameInput, text="Manufacture Name:")
        self.lblSerialNum = tk.Label(self.frameInput, text="Serial Number:")
        self.lblBumperNum = tk.Label(self.frameInput, text="Bumper Number:")      
        self.lblManuDate = tk.Label(self.frameInput, text="Manufacture Date:")
        self.lblInstallDate = tk.Label(self.frameInput, text="Install Date:")
        self.lblBelayDeviceType = tk.Label(self.frameInput, text="Belay Device Type:")
        self.lblBelayDeviceInUse = tk.Label(self.frameInput, text="Belay Device In Use:")

        # Create the label locations
        self.lblDeviceName.grid(row=0, column=0, sticky='W', padx=5)
        self.lblManuName.grid(row=1, column=0, sticky='W', padx=5)
        self.lblSerialNum.grid(row=2, column=0, sticky='W', padx=5)
        self.lblBumperNum.grid(row=3, column=0, sticky='W', padx=5)
        self.lblManuDate.grid(row=4, column=0, sticky='W', padx=5)
        self.lblInstallDate.grid(row=5, column=0, sticky='W', padx=5)
        self.lblBelayDeviceType.grid(row=6, column=0, sticky='W', padx=5)
        self.lblBelayDeviceInUse.grid(row=7, column=0, sticky='W', padx=5)
        
        # Create the entry input box
        self.DeviceNameInput = Entry(self.frameInput, width=39, state='disabled')
        self.ManuNameInput = Entry(self.frameInput, width=39, state='disabled')
        self.SerialNumInput = Entry(self.frameInput, width=39, state='disabled')
        self.BumperNumInput = Entry(self.frameInput, width=39, state='disabled')
        self.ManuDateInput = Entry(self.frameInput, width=39, state='disabled')
        self.InstallDateInput = Entry(self.frameInput, width=39, state='disabled')

        # Create the combo box
        self.aInUseSelectionList = ('Yes', 'No', 'Retired')
        self.aDeviceTypeSelectionList = ('Manual Braking', 'Assisted Braking')
        self.dropDeviceType = ttk.Combobox(self.frameInput, values=self.aDeviceTypeSelectionList, state='disabled')
        self.dropInUseSelection = ttk.Combobox(self.frameInput, values=self.aInUseSelectionList, state='disabled')
        self.dropDeviceType.configure(width=36,)
        self.dropInUseSelection.configure(width=36,)

        # Create the grid for all of the entry input fields
        self.DeviceNameInput.grid(row=0, column=1, padx=25, pady=5)
        self.ManuNameInput.grid(row=1, column=1, pady=5)
        self.SerialNumInput.grid(row=2, column=1, pady=5)
        self.BumperNumInput.grid(row=3, column=1, pady=5)
        self.ManuDateInput.grid(row=4, column=1, pady=5)
        self.InstallDateInput.grid(row=5, column=1, pady=5)
        self.dropDeviceType.grid(row=6, column=1, pady=5)
        self.dropInUseSelection.grid(row=7, column=1, pady=5)

        # Create the buttons
        self.btnExit = Button(self, text="Back", width=10, command=lambda:UpdateBelayDeviceInfo.Exit(self))
        self.btnReset = Button(self, text="Reset", width=10, command=lambda:UpdateBelayDeviceInfo.Reset(self))
        self.btnSubmit = Button(self, text="Submit", width=10, command=lambda:UpdateBelayDeviceInfo.Submit(self))

        # Create the button grid
        self.btnExit.place(x=105, y=445)
        self.btnReset.place(x=235, y=445)
        self.btnSubmit.place(x=365, y=445)

    def Selection_Widget(self):
        """ 
        Function Name: Selection_Widget
        Function Purpose: This function populates the search by widget for Serial or Bumper Num search.
        """           
        # Create the first frame to hold the input fields
        self.selectInput = LabelFrame(self, text="Select Belay Device")
        self.selectInput.place(x=75, y=35, width=405, height=130)

        # Create the labels 
        self.lblSearchByBelayDeviceID = Label(self.selectInput, text="Query by Device ID:")
        self.lblBelayDeviceSelection = Label(self.selectInput, text="Device ID Selection:")

        # Create the label locations
        self.lblSearchByBelayDeviceID.place(x=5, y=5)
        self.lblBelayDeviceSelection.place(x=5, y=35)

        # Create variables to hold the value of the selected radio button
        self.objRadioValue = tk.StringVar(value='serial')
        self.objComboValue = tk.StringVar()

        # List objects of serial and bumper values
        self.astrSerialNumList = self.astrSerialNumCache
        self.astrBumperNumList = self.astrBumperNumCache

        # Create the radio buttons
        self.rbSerial = tk.Radiobutton(self.selectInput, text="Serial Number", variable=self.objRadioValue, value="serial", command=self.Populate_Dropdown)
        self.rbBumper = tk.Radiobutton(self.selectInput, text="Bumper Number", variable=self.objRadioValue, value="bumper", command=self.Populate_Dropdown)

        # Place the radio buttons next to each other using .place()
        self.rbSerial.place(x=135, y=5)
        self.rbBumper.place(x=265, y=5)
                    
        # Create the combo box
        self.dropBelayDeviceSelection = ttk.Combobox(self.selectInput, values=self.astrSerialNumList, state='readonly')
        self.dropBelayDeviceSelection.configure(width=36,)

        # Populate the dropdown based on the default radio button selection
        self.Populate_Dropdown()

        # Create the grid for all of the entry input fields
        self.dropBelayDeviceSelection.place(x=140, y=35)

        # Create the buttons
        self.btnSelectSubmit = Button(self.selectInput, text="Submit", width=10, command=lambda:UpdateBelayDeviceInfo.SubmitSelect(self))

        # Create the button grid
        self.btnSelectSubmit.place(x=165, y=70)  

    def Populate_Dropdown(self):
        """ 
        Function Name: Populate_Dropdown
        Function Purpose: This function populates the dropdown based on the radio button selection.
        """           
        if self.objRadioValue.get() == "serial":
            self.dropBelayDeviceSelection["values"] = self.astrSerialNumList
        else:
            self.dropBelayDeviceSelection["values"] = self.astrBumperNumList
        self.dropBelayDeviceSelection.set("")                                 
        
    def Change_Date_To_Format(dtmObject, aResultTup):
        """ 
        Function Name: Change_Date_To_Format
        Function Purpose: This function is executed every call of the validation check to ensure the dates are all
        changed to the same format no matter if the character is valid.
        """ 
        dtmObject.delete(0, END)
        dtmObject.insert(0, aResultTup[1])
        dtmObject = aResultTup[1]

        return dtmObject

    def Convert_Date_Format(date_str):
        """ 
        Function Name: SubmitSelect
        Function Purpose: This button Convert date from "YYYY-MM-DD" to "MM/DD/YYYY"
        """
        year, month, day = date_str.split('-')
        return f"{month}/{day}/{year}"

    def Disable_After_Submit(self):
        """ 
        Function Name: Disable_After_Submit
        Function Purpose: This function disables certain controls after submission.
        """   
        # Disable the submit button
        self.btnSubmit.configure(state='disabled')
        
        # Reset the value of the dropdown
        self.dropBelayDeviceSelection.set("")

    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)
        
    def Check_Serial_Or_Bumper(self):
        """ 
        Function Name: Check_Serial_Or_Bumper
        Function Purpose: This function is executed once the user clicks on the option of query search by serial
        number or bumper number. 
        """        
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Get the primary key ID from the dropdown
        strSelectionID = self.dropBelayDeviceSelection.get()
        
        # Determine the primary key for the query
        if strSelectionID in BelayDevices.astrSerialNumCache:
            primary_key = BelayDevices.astrSerialNumCache.index(strSelectionID) + 1
            blnFlag = True
        elif strSelectionID in BelayDevices.astrBumperNumCache:
            primary_key =  BelayDevices.astrBumperNumCache.index(strSelectionID) + 1
            blnFlag = False
            
        # Return the primary key
        return (blnFlag, primary_key)
                
    def SubmitSelect(self):
        """ 
        Function Name: SubmitSelect
        Function Purpose: This button executes when the user selects the BelayDevice.
        """
        # Set the state of the inputs
        for entry in [self.DeviceNameInput, self.ManuNameInput, self.SerialNumInput, self.BumperNumInput, self.ManuDateInput, self.InstallDateInput]:
            entry.configure(state='normal')

        # Configure the drop menu for in use
        self.dropDeviceType.configure(state='readonly')
        self.dropInUseSelection.configure(state='readonly')

        # Determine the primary key for the query
        resultTup =  self.Check_Serial_Or_Bumper()
        primary_key =  resultTup[1]

        # Execute the query
        aParams = ('TBelayDevices', 'intBelayDeviceID', primary_key)
        QueryResult = Queries.Get_All_DB_Values_OnePrimKey(Queries, aParams)
        
        if QueryResult:
            self.DeviceNameInput.insert(0, QueryResult[1])
            self.SerialNumInput.insert(0, QueryResult[2])
            self.BumperNumInput.insert(0, QueryResult[3])
            self.ManuNameInput.insert(0, QueryResult[4])
            self.ManuDateInput.insert(0, UpdateBelayDeviceInfo.Convert_Date_Format(QueryResult[5]))
            self.InstallDateInput.insert(0, UpdateBelayDeviceInfo.Convert_Date_Format(QueryResult[6]))
            self.Set_Previous_Drop_List(QueryResult[9], self.dropDeviceType)
            self.Set_Previous_Drop_List(QueryResult[10], self.dropInUseSelection)
        
        # Disable the select submit button
        self.btnSelectSubmit.configure(state='disabled')
        
        # Enable the submit and reset buttons
        self.btnSubmit.configure(state='normal')
        self.btnReset.configure(state='normal')
                
    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.')
            blnValidate = False
            
        return blnValidate
        
    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        def set_invalid(input_field):
            """
            Set the input field to show invalid data.
            """
            input_field.delete(0, tk.END)
            input_field.configure(background='Yellow')
            input_field.focus()

        # Validate Manufacturer Name
        if not (AddBelayDevice.Check_Input(self.DeviceNameInput.get()) and
                BaseFunctions.Validate_String_Input(self.DeviceNameInput.get())):
            set_invalid(self.DeviceNameInput)
            return False
        
        # Validate Manufacturer Name
        if not (AddBelayDevice.Check_Input(self.ManuNameInput.get()) and
                BaseFunctions.Validate_String_Input(self.ManuNameInput.get())):
            set_invalid(self.ManuNameInput)
            return False
        
        # Validate Serial Number
        if not (AddBelayDevice.Check_Input(self.SerialNumInput.get()) and
                BaseFunctions.Validate_Serial_Input(self.SerialNumInput.get())):
            set_invalid(self.SerialNumInput)
            return False
        
        # Validate Bumper Number if it exists
        bumper_num = self.BumperNumInput.get()
        if bumper_num != "" and not BaseFunctions.Validate_Serial_Input(bumper_num):
            set_invalid(self.BumperNumInput)
            return False

        self.BumperNumInput.delete(0, tk.END)
        new_bumper_num_value = bumper_num if bumper_num != "" else 'Optional'
        self.BumperNumInput.insert(0, new_bumper_num_value)
        
        # Validate Manufacturing Date
        if not AddBelayDevice.Check_Input(self.ManuDateInput.get()):
            set_invalid(self.ManuDateInput)
            return False

        result_tup = BaseFunctions.Validate_Date_Input(self.ManuDateInput.get())
        if not result_tup[0]:
            set_invalid(self.ManuDateInput)
            return False

        self.ManuDateInputResult = AddBelayDevice.Change_Date_To_Format(self.ManuDateInput, result_tup)

        # Validate Installation Date
        if not AddBelayDevice.Check_Input(self.InstallDateInput.get()):
            set_invalid(self.InstallDateInput)
            return False

        result_tup = BaseFunctions.Validate_Date_Input(self.InstallDateInput.get())
        if not result_tup[0]:
            set_invalid(self.InstallDateInput)
            return False

        self.InstallDateResult = AddBelayDevice.Change_Date_To_Format(self.InstallDateInput, result_tup)

        # Validate dropDeviceType
        if not AddBelayDevice.Check_Input(self.dropDeviceType.get()):
            set_invalid(self.dropDeviceType)
            return False
                    
        # Validate 'In Use' Selection
        if not AddBelayDevice.Check_Input(self.dropInUseSelection.get()):
            set_invalid(self.dropInUseSelection)
            return False
        
        return True

    def Get_UserInput(self):
        """ 
        Function Name: Get_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        Then the data will be sent to the db.
        """                
        # Assign value to the objects
        SerialNum = self.SerialNumInput.get()
        BumperNum = self.BumperNumInput.get()
        ManuDate = datetime.strptime(self.ManuDateInputResult, '%m/%d/%Y').date()
        InstallationDate = datetime.strptime(self.InstallDateResult, '%m/%d/%Y').date()
        ManuDate = str(ManuDate)
        InstallationDate = str(InstallationDate)
        BelayDeviceType = self.dropDeviceType.get()
        BelayDeviceInUse = self.dropInUseSelection.get()
        
        # Capitalize these inputs
        ManuName = ' '.join(manu.capitalize() for manu in self.ManuNameInput.get().split())
        DeviceName = ' '.join(device.capitalize() for device in self.DeviceNameInput.get().split())
        
        # First check if the serial or bumper number was selected 
        resultTup =  self.Check_Serial_Or_Bumper()
        intPrimKey = resultTup[1] - 1

        # Commit the data to load the BelayDevices class objects with the data from the db
        BelayDevices.strSerialNum = BelayDevices.astrSerialNumCache[intPrimKey]
        BelayDevices.Set_BelayDevices_Data(BelayDevices)
            
        # Finish by updating the BelayDevices class objects before the database dump
        bd = BelayDevices(self.intBelayDeviceID, DeviceName, SerialNum, BumperNum, ManuName, ManuDate, InstallationDate, 
                    self.dtmLastInspectionDate, self.dtmNextInspectionDate, BelayDeviceType, BelayDeviceInUse)
        
        BelayDevices.intBelayDeviceID = bd.intBelayDeviceID
        BelayDevices.strBelayDeviceName = bd.strBelayDeviceName
        BelayDevices.strSerialNum = bd.strSerialNum
        BelayDevices.strBumperNum = bd.strBumperNum
        BelayDevices.strManufactureName = bd.strManufactureName
        BelayDevices.dtmManufactureDate = bd.dtmManufactureDate
        BelayDevices.dtmInstallationDate = bd.dtmInstallationDate
        BelayDevices.dtmLastInspectionDate = bd.dtmLastInspectionDate
        BelayDevices.dtmNextInspectionDate = bd.dtmNextInspectionDate
        BelayDevices.strDeviceType = bd.strDeviceType
        BelayDevices.strEquipInUse = bd.strEquipInUse
        
    def Clear_BG_Color(self):
        """ 
        Function Name: Clear_BG_Color
        Function Purpose: This button executes when the user submits their entries and clears the background
        color before any validation checks.
        """
        # Delete the button after submission
        self.DeviceNameInput.configure(background='White')
        self.ManuNameInput.configure(background='White')
        self.SerialNumInput.configure(background='White')
        self.BumperNumInput.configure(background='White')
        self.ManuDateInput.configure(background='White')
        self.InstallDateInput.configure(background='White')
        
    def Reset(self):
        """ 
        Function Name: Reset
        Function Purpose: This button executes when the user wants to reset the values.
        """
        # Delete the entries
        self.DeviceNameInput.delete(0, END)
        self.ManuNameInput.delete(0, END)
        self.SerialNumInput.delete(0, END)
        self.BumperNumInput.delete(0, END)
        self.ManuDateInput.delete(0, END)
        self.InstallDateInput.delete(0, END)
        
        # Reset the drop menus
        self.dropDeviceType.set("")
        self.dropInUseSelection.set("")
        self.dropBelayDeviceSelection.set("")
                
        # Re-configure input entries to be disabled
        self.dropDeviceType.configure(state='disabled')
        self.DeviceNameInput.configure(state='disabled')
        self.ManuNameInput.configure(state='disabled')
        self.SerialNumInput.configure(state='disabled')
        self.BumperNumInput.configure(state='disabled')
        self.ManuDateInput.configure(state='disabled')
        self.InstallDateInput.configure(state='disabled')       
        self.dropInUseSelection.configure(state='disabled') 

        # Disable/enable the select, submit, and reset submit button
        self.btnSelectSubmit.configure(state='normal')
        self.btnReset.configure(state='disabled')
        self.btnSubmit.configure(state='disabled') 

        # Reset the radio button to its default value
        self.objRadioValue.set("serial")
        
        # Populate the dropdown based on default radio button selection
        self.Populate_Dropdown()

        # Re-Populate the dropdown menus 
        self.dropBelayDeviceSelection["values"] = self.astrSerialNumList
        self.dropDeviceType["values"] = self.aDeviceTypeSelectionList
        self.dropInUseSelection["values"] = self.aInUseSelectionList
        
        # Clear out the background colors and set to default as 'white'
        UpdateBelayDeviceInfo.Clear_BG_Color(self)

        # Call the function to disable controls after submission
        self.Disable_After_Submit()
        
    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the updated BelayDevices BelayDevice information to the db. 
        Else, reset
        """
        # Check if all of the inputs are valid
        global blnValidate 
        blnValidate = bool(False)
        
        # Clear out the background colors and set to default as 'white'
        UpdateBelayDeviceInfo.Clear_BG_Color(self)
        
        # Get the blnValidate status
        blnValidate = UpdateBelayDeviceInfo.Validate_InputFields(self)
        
        # Check if the input is valid
        if (blnValidate is True):
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to update the BelayDevice information?') is True:     
                # Load the user data and prep the data for db dump
                UpdateBelayDeviceInfo.Get_UserInput(self)             
                BelayDevices.Update_NewBelayDevices_Query(self)
                
                # Check if the user would like to update another BelayDevice
                if messagebox.askyesno(message='SUCCESSFUL UPDATE! \n\n Would you like to update another BelayDevice?') is True:
                    # Clear the input fields and after data is submitted to the database
                    UpdateBelayDeviceInfo.Reset(self)
                else:
                    UpdateBelayDeviceInfo.Exit(self)
            else:
                pass

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        
        
#######################################################################################################
# BelayDevice Inspection Class
#######################################################################################################

class BelayDeviceInspection(tk.Tk): 
    """
    Class Name: BelayDeviceInspection
    Class Description: This class is to conduct belay device inspections.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new BelayDevice inspection. User must click
        'Next' Button in order to progress to the next inspection type. A Visual, Physical, and Functional inspection
        must be performed to complete the inspection.
        """
        # Load the data from the database
        # Start_Menu.Load_Obj_Lists(self) # Make sure to comment this out after testing
        
        # Create the root tkinter var and init
        super().__init__()

        # Declare the class bool for plastic flag
        self.blnPlasticFlag = False
        
        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # Calculate x and y coordinates for the Tk window 
        self.x = (self.widthSize/2) - (805/2)     
        self.y = (self.heightSize/2) - (640/2)          
        
        # Create the Window attributes                
        self.title("Belay Device Inspection")
        self.geometry('%dx%d+%d+%d' % (805, 640, self.x, self.y))
        self.resizable(False, False)

        # Load the query selection widget for Search by serial or bumper num
        self.Selection_Widget()
        
        # Create the scrollbar frame
        self.scrollFrame = LabelFrame(self, text='Inspection Results')
        self.scrollFrame.place(x=35, y=140, width=735, height=445)
        self.resultCanvas = Canvas(self.scrollFrame)
        self.resultCanvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.resultScrollBar = Scrollbar(self.scrollFrame, orient=VERTICAL, command=self.resultCanvas.yview)
        self.resultScrollBar.pack(side=RIGHT, fill=Y)
        self.resultCanvas.configure(yscrollcommand=self.resultScrollBar.set)
        self.resultCanvas.bind('<Configure>', lambda event: self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all")))
        
        # Create the third frame to hold the result fields
        self.resultFrame = Frame(self.resultCanvas)
        self.resultCanvas.create_window((0,0), window=self.resultFrame, anchor='nw')
        
        # Bind mousewheel scrolling
        self.resultCanvas.bind_all("<MouseWheel>", self.on_vertical_scroll)
        
        # Create the frame fields
        self.visCheckListFrame = tk.LabelFrame(self.resultFrame, text="Visual Metal Inspection Results")
        self.physCheckListFrame = tk.LabelFrame(self.resultFrame, text="Physical Metal Inspection Results")
        self.functCheckListFrame = tk.LabelFrame(self.resultFrame, text="Functional Metal Inspection Results")
        self.visPlasCheckListFrame = tk.LabelFrame(self.resultFrame, text="Visual Plastic Inspection Results")
        self.physPlasCheckListFrame = tk.LabelFrame(self.resultFrame, text="Physical Plastic Inspection Results")
        self.functPlasCheckListFrame = tk.LabelFrame(self.resultFrame, text="Functional Plastic Inspection Results")
        self.commFrame = tk.LabelFrame(self.resultFrame, text="Inspection Comment")

        # Layout for the frames inside the scrollable area
        self.visCheckListFrame.grid(row=0, column=0, padx=(50, 7), pady=10, sticky="nw")
        self.physCheckListFrame.grid(row=0, column=1, padx=(7, 50), pady=10, sticky="nw")
        self.functCheckListFrame.grid(row=1, column=0, columnspan=2, padx=(50, 10), pady=10, sticky="nw")

        # Separator label
        self.lblSeparator = tk.Label(self.resultFrame, text="-------------------------------------------------------------------------------------------------------------------------------")
        self.lblSeparator.grid(row=2, column=0, columnspan=2, sticky="ew", padx=0, pady=5)

        # Layout for the Plastic Inspection frames
        self.visPlasCheckListFrame.grid(row=3, column=0, padx=(50, 7), pady=10, sticky="nw")
        self.physPlasCheckListFrame.grid(row=3, column=1, padx=(7, 50), pady=10, sticky="nw")
        self.functPlasCheckListFrame.grid(row=4, column=0, columnspan=2, padx=(50, 10), pady=10, sticky="nw")
        self.commFrame.grid(row=6, column=0, columnspan=2, padx=(50, 50), pady=10, sticky="nw")

        # Update the scroll region to encompass the entire resultFrame
        self.resultFrame.bind("<Configure>", self.onFrameConfigure)

        # Create and place the labels within their respective frames
        self.lblBelayDeviceVisualStatus = tk.Label(self.visCheckListFrame, text="Visual Status:")
        self.lblBelayDevicePhysicalStatus = tk.Label(self.physCheckListFrame, text="Physical Status:")
        self.lblBelayDeviceFunctStatus = tk.Label(self.functCheckListFrame, text="Function Status:")
        self.lblBelayDeviceVisualPastStatus = tk.Label(self.visPlasCheckListFrame, text="Visual Status:")
        self.lblBelayDevicePhysicalPastStatus = tk.Label(self.physPlasCheckListFrame, text="Physical Status:")
        self.lblBelayDeviceFunctPastStatus = tk.Label(self.functPlasCheckListFrame, text="Function Status:")
        
        # Place the labels at the bottom using large pady
        self.lblBelayDeviceVisualStatus.grid(row=5, column=0, sticky="w", padx=5, pady=10)
        self.lblBelayDevicePhysicalStatus.grid(row=5, column=0, sticky="w", padx=5, pady=10)
        self.lblBelayDeviceFunctStatus.grid(row=3, column=1, sticky="w", padx=5, pady=10)
        self.lblBelayDeviceVisualPastStatus.grid(row=5, column=0, sticky="w", padx=5, pady=10)
        self.lblBelayDevicePhysicalPastStatus.grid(row=5, column=0, sticky="w", padx=5, pady=10)
        self.lblBelayDeviceFunctPastStatus.grid(row=3, column=1, sticky="w", padx=5, pady=10)
        
        # Create the drop down menu list for each attribute
        self.dropBelayDeviceVisStatus = ttk.Combobox(self.visCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropBelayDevicePhysStatus = ttk.Combobox(self.physCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropBelayDeviceFunctStatus = ttk.Combobox(self.functCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropBelayDeviceVisPlastStatus = ttk.Combobox(self.visPlasCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropBelayDevicePhysPlastStatus = ttk.Combobox(self.physPlasCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        self.dropBelayDeviceFunctPlastStatus = ttk.Combobox(self.functPlasCheckListFrame, values=InspectionStatus.astrInspectionStatusDesc, state='readonly')
        
        # Create the drop down menu size for each attribute
        self.dropBelayDeviceVisStatus.configure(width=20)
        self.dropBelayDevicePhysStatus.configure(width=20)
        self.dropBelayDeviceFunctStatus.configure(width=20)
        self.dropBelayDeviceVisPlastStatus.configure(width=20)
        self.dropBelayDevicePhysPlastStatus.configure(width=20)
        self.dropBelayDeviceFunctPlastStatus.configure(width=20)
                
        # Create the grid for the drop down menu list objects   
        self.dropBelayDeviceVisStatus.place(x=125, y=135)  
        self.dropBelayDevicePhysStatus.place(x=125, y=135)  
        self.dropBelayDeviceFunctStatus.place(x=290, y=85)  
        self.dropBelayDeviceVisPlastStatus.place(x=125, y=135)  
        self.dropBelayDevicePhysPlastStatus.place(x=125, y=135)  
        self.dropBelayDeviceFunctPlastStatus.place(x=290, y=85)        

        # Create the master list for the metallic and functional inspection types
        self.selectItems = Metallic.astrMetallicInspectionDesc 
        self.plasticItems = Plastic.astrPlasticInspectionDesc
        self.functItems = ["No Functional Issues", "Side Plate Misalignment", "Side Plate Closure", "Cam Immobility", 
                            "Axle Mobility", "Axle Misalighment", "Rivet Mobility", "Rivet Misalighment", "Handle Misalignment",
                            "Handle Closure", "Other Functional Issues"]
        
        # Create the checkbox lists for visual, physical, and functional
        self.visCheckList = [] 
        self.physCheckList = []
        self.functCheckList = []
        self.visPlastCheckList = [] 
        self.physPlastCheckList = []
        self.functPlastCheckList = []
                
        # Create an empty list to store selected items
        self.checkboxVisStates = {}
        self.checkboxPhysStates = {}
        self.checkboxFuncStates = {}
        self.checkboxPlastVisStates = {}
        self.checkboxPlastPhysStates = {}
        self.checkboxPlastFuncStates = {}        

        # Create the checkbox list
        self.Create_Check_Buttons(self.selectItems, self.visCheckListFrame, BelayDeviceVisSelection.astrBelayDeviceVisMetSelect, self.visCheckList, self.checkboxVisStates, self.Get_VisCheckbox_List, "visual", "visual metal")
        self.Create_Check_Buttons(self.selectItems, self.physCheckListFrame, BelayDevicePhysSelection.astrBelayDevicePhysMetSelect, self.physCheckList, self.checkboxPhysStates, self.Get_PhysCheckbox_List, "physical", "physical metal")
        self.Create_Check_Buttons(self.functItems, self.functCheckListFrame, BelayDeviceFunctSelection.astrBelayDeviceFunctSelect, self.functCheckList, self.checkboxFuncStates, self.Get_FuncCheckbox_List, "functional", "functional metal")
        self.Create_Check_Buttons(self.plasticItems, self.visPlasCheckListFrame, BelayDevicePlasticVisSelection.astrBelayDeviceVisPlastSelect, self.visPlastCheckList, self.checkboxPlastVisStates, self.Get_Vis_Plastic_Checkbox_List, "visual", "visual plastic")
        self.Create_Check_Buttons(self.plasticItems, self.physPlasCheckListFrame, BelayDevicePlasticPhysSelection.astrBelayDevicePhysPlastSelect, self.physPlastCheckList, self.checkboxPlastPhysStates, self.Get_Phys_Plastic_Checkbox_List, "physical", "physical plastic")
        self.Create_Check_Buttons(self.functItems, self.functPlasCheckListFrame, BelayDevicePlasticFunctSelection.astrBelayDevicePlasticFunctSelect, self.functPlastCheckList, self.checkboxPlastFuncStates, self.Get_Func_Plastic_Checkbox_List, "functional", "functional plastic")

        # First check if the selection values have been assigned
        self.Set_Previous_Checkbox_List(BelayDeviceVisSelection.astrBelayDeviceVisMetSelect, self.visCheckList, self.selectItems)
        self.Set_Previous_Checkbox_List(BelayDevicePhysSelection.astrBelayDevicePhysMetSelect, self.physCheckList, self.selectItems)
        self.Set_Previous_Checkbox_List(BelayDeviceFunctSelection.astrBelayDeviceFunctSelect, self.functCheckList, self.functItems)
        self.Set_Previous_Checkbox_List(BelayDevicePlasticVisSelection.astrBelayDeviceVisPlastSelect, self.visPlastCheckList, self.plasticItems)
        self.Set_Previous_Checkbox_List(BelayDevicePlasticPhysSelection.astrBelayDevicePhysPlastSelect, self.physPlastCheckList, self.plasticItems)
        self.Set_Previous_Checkbox_List(BelayDevicePlasticFunctSelection.astrBelayDevicePlasticFunctSelect, self.functPlastCheckList, self.functItems)
                
        # Check if the cache values for any drop menus have been previously selected and set the values
        if Bool_Flag.blnBelayDevicePersistFlag == True:
            self.Set_Previous_Drop_List(BelayDeviceVisSelection.strBelayDeviceVisStatus, self.dropBelayDeviceVisStatus)
            self.Set_Previous_Drop_List(BelayDevicePhysSelection.strBelayDevicePhysStatus, self.dropBelayDevicePhysStatus)
            self.Set_Previous_Drop_List(BelayDeviceFunctSelection.strBelayDeviceFunctStatus, self.dropBelayDeviceFunctStatus)
            self.Set_Previous_Drop_List(BelayDevicePlasticVisSelection.strBelayDeviceVisStatus, self.dropBelayDeviceVisPlastStatus)
            self.Set_Previous_Drop_List(BelayDevicePlasticPhysSelection.strBelayDevicePhysStatus, self.dropBelayDevicePhysPlastStatus)
            self.Set_Previous_Drop_List(BelayDevicePlasticFunctSelection.strBelayDeviceFunctStatus, self.dropBelayDeviceFunctPlastStatus)            

        # Create the comment field
        self.commInput = tk.Text(self.commFrame, state='normal')
        self.commInput.grid(row=0, column=0, padx=(4, 5), pady=4)
        self.commInput.configure(width=77, height=4, padx=0)
        
        # Create the buttons
        self.btnBack = Button(self, text="Back", width=10, command=self.Back)
        self.btnClear = Button(self, text="Clear", width=10, command=self.Clear)
        self.btnExit = Button(self, text="Exit", width=10, command=self.Exit)
        self.btnNext = Button(self, text="Next", width=10, command=self.Next)
            
        # Create the position of the button
        self.btnBack.place(x=165, y=595)
        self.btnExit.place(x=295, y=595) 
        self.btnClear.place(x=425, y=595)
        self.btnNext.place(x=555, y=595) 
        
        # Keep the window open while the user is interacting with the widgets
        self.mainloop() 

        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the stored data in the class attributes
        StandardBelayDeviceInspect.Delete_BelayDevice_Data(self)
                        
        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)
        BelayDevices_Menu()          

    def on_vertical_scroll(self, event):
        """Scroll the canvas vertically using the mouse wheel."""
        self.resultCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
    def onFrameConfigure(self, event=None):
        """ 
        Function Name: onFrameConfigure
        Function Purpose: This function is a method that gets called whenever the 'resultFrame' is reconfigured.
        """          
        # Update the scrollable region to fit the size of the resultFrame
        self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all"))

    def Selection_Widget(self):
        """ 
        Function Name: Selection_Widget
        Function Purpose: This function populates the search by widget for Serial or Bumper Num search.
        """           
        # Create the first frame to hold the input fields
        self.typeFrame = tk.LabelFrame(self, text="Selected Belay Device")
        self.typeFrame.place(x=35, y=10, width=735, height=120)

        # Create the labels 
        self.lblBelayDeviceSerial = Label(self.typeFrame, text="Serial ID:")
        self.lblBelayDeviceBumper = Label(self.typeFrame, text="Bumper ID:")
        self.lblBelayDeviceType = tk.Label(self.typeFrame, text="Belay Device Type:")

        # Create the label locations
        self.lblBelayDeviceSerial.place(x=257, y=5)
        self.lblBelayDeviceBumper.place(x=243, y=35)
        self.lblBelayDeviceType.place(x=205, y=65)

        # Create the entry input box
        self.SerialNumOut = Entry(self.typeFrame, width=30, state='normal')
        self.BumperNumOut = Entry(self.typeFrame, width=30, state='normal')
        self.BelayDeviceType = Entry(self.typeFrame, width=30, state='normal')
        
        # Set the values selected from the user
        self.SerialNumOut.insert(0, BelayDevices.strSerialNum)
        self.BumperNumOut.insert(0, BelayDevices.strBumperNum)
        self.BelayDeviceType.insert(0, BelayDevices.strDeviceType)
        
        # Configure the state to disabled
        self.SerialNumOut.configure(state='disabled')
        self.BumperNumOut.configure(state='disabled')
        self.BelayDeviceType.configure(state='disabled')
        
        # Create the grid for all of the entry input fields
        self.SerialNumOut.place(x=345, y=5)
        self.BumperNumOut.place(x=345, y=35)
        self.BelayDeviceType.place(x=345, y=65) 

    def Create_Check_Buttons(self, selectItems, checkListFrame, arrayObject, checkList, checkboxStates, callback, strInsType, selectionKey):
        """ 
        Function Name: Create_Check_Buttons
        Function Description: This helper method to create the checkbox buttons
        """
        # Conditions for setting max columns and padding based on inspection type
        isVisualOrPhysical = strInsType in ["visual", "physical"]
                
        # Set max columns and padding values based on the condition
        maxColPerRow = 2 if isVisualOrPhysical else 4
        padx_value = 10 if isVisualOrPhysical else 6

        for index, item in enumerate(selectItems):
            # Check if the item was previously selected (exists in arrayObject)
            is_selected = item in arrayObject
            var = tk.StringVar(value='1' if is_selected else '0')
            checkList.append(var)

            # Use a lambda function to capture the current item in the loop
            checkBox = tk.Checkbutton(checkListFrame, text=item, variable=var, onvalue='1', offvalue='0', 
                        command=lambda item=item, var=var: callback(item, var, selectionKey))
            
            # Store the variable in the checkboxStates dictionary
            checkboxStates[item] = var

            # Calculate the row and column position of checkbutton based on index and max columns 
            rowPosition = index // maxColPerRow
            colPosition = index % maxColPerRow
            checkBox.grid(row=rowPosition, column=colPosition, sticky="w", padx=padx_value)

    def Set_Previous_Checkbox_List(self, selectList, checkboxList, paramsList):
        """
        Function Name: Set_Vis_Previous_Checkbox_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the checkboxes from the cache array list for all checkboxes.
        """   
        # First check if the cache values have been assigned
        if len(selectList) == 0:
            # Check the first item of the list    
            checkboxList[0].set('1')
        else:
            # Set the Selection data to the objects in the window
            for i, item in enumerate(paramsList):
                if item in selectList:
                    checkboxList[i].set('1')

    def Set_Previous_Drop_List(self, selectString, dropMenu):
        """
        Function Name: Set_Previous_Drop_List
        Function Purpose: This function is called whenever there is a callback from a child window to a parent window and selects
        the drop menu item from the cache array list for all drop menus.
        """   
        # Set the Selection data to the objects in the window
        dropMenu.set(selectString)

    def Get_VisCheckbox_List(self, item, var, selectionKey):
        """
        Function Name: Get_VisCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # Execute checkbox update logic...
        state = var.get()
        if state == '1':            
            self.Update_Checkbox_List(self.visCheckList, item, self.checkboxVisStates, selectionKey, BelayDeviceVisSelection.astrBelayDeviceVisMetSelect)
        else:
            self.Handle_Deselection(self.visCheckList, item, self.checkboxVisStates, selectionKey, BelayDeviceVisSelection.astrBelayDeviceVisMetSelect)

    def Get_PhysCheckbox_List(self, item, var, selectionKey):
        """
        Function Name: Get_PhysCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # Execute checkbox update logic...
        state = var.get()
        if state == '1':          
            self.Update_Checkbox_List(self.physCheckList, item, self.checkboxPhysStates, selectionKey, BelayDevicePhysSelection.astrBelayDevicePhysMetSelect)
        else:
            self.Handle_Deselection(self.physCheckList, item, self.checkboxPhysStates, selectionKey, BelayDevicePhysSelection.astrBelayDevicePhysMetSelect)

    def Get_FuncCheckbox_List(self, item, var, selectionKey):
        """
        Function Name: Get_FuncCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':          
            self.Update_Checkbox_List(self.functCheckList, item, self.checkboxFuncStates, selectionKey, BelayDeviceFunctSelection.astrBelayDeviceFunctSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.functCheckList, item, self.checkboxFuncStates, selectionKey, BelayDeviceFunctSelection.astrBelayDeviceFunctSelect)

    def Get_Vis_Plastic_Checkbox_List(self, item, var, selectionKey):
        """
        Function Name: Get_VisCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # Update the plastic flag based on the selectionKey
        self.blnPlasticFlag = "plastic" in selectionKey
        
        # Execute checkbox update logic...
        state = var.get()
        if state == '1':            
            self.Update_Checkbox_List(self.visPlastCheckList, item, self.checkboxPlastVisStates, selectionKey, BelayDevicePlasticVisSelection.astrBelayDeviceVisPlastSelect)
        else:
            self.Handle_Deselection(self.visPlastCheckList, item, self.checkboxPlastVisStates, selectionKey, BelayDevicePlasticVisSelection.astrBelayDeviceVisPlastSelect)

    def Get_Phys_Plastic_Checkbox_List(self, item, var, selectionKey):
        """
        Function Name: Get_PhysCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # Update the plastic flag based on the selectionKey
        self.blnPlasticFlag = "plastic" in selectionKey
        
        # Execute checkbox update logic...
        state = var.get()
        if state == '1':          
            self.Update_Checkbox_List(self.physPlastCheckList, item, self.checkboxPlastPhysStates, selectionKey, BelayDevicePlasticPhysSelection.astrBelayDevicePhysPlastSelect)
        else:
            self.Handle_Deselection(self.physPlastCheckList, item, self.checkboxPlastPhysStates, selectionKey, BelayDevicePlasticPhysSelection.astrBelayDevicePhysPlastSelect)

    def Get_Func_Plastic_Checkbox_List(self, item, var, selectionKey):
        """
        Function Name: Get_FuncCheckbox_List
        Function Purpose: This function is called whenever there is an item selected in the Visual checkbox and creates a list of objects
        """
        # This gets the current state of the checkbox
        state = var.get()
        # Check if the checkbox is selected
        if state == '1':          
            self.Update_Checkbox_List(self.functPlastCheckList, item, self.checkboxPlastFuncStates, selectionKey, BelayDevicePlasticFunctSelection.astrBelayDevicePlasticFunctSelect)
        # Checkbox was deselected
        else:
            self.Handle_Deselection(self.functPlastCheckList, item, self.checkboxPlastFuncStates, selectionKey, BelayDevicePlasticFunctSelection.astrBelayDevicePlasticFunctSelect)

    def Update_Checkbox_List(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Update_Checkbox_List
        Function Purpose: Updates checkbox states and persistent data with special handling for the default (first) item.
        """
        # Identify the correct item list based on the selectionKey
        itemList = self.determine_item_list(selectionKey)
        
        # Check if the selected item is in the itemList
        if item not in itemList:
            print(f"Error: Item '{item}' not found in itemList for selectionKey '{selectionKey}'.")
            return  # Exit the function to avoid further errors

        # Find the index of the selected item in the item list
        selectedIndex = itemList.index(item)

        # If the first item is selected, deselect all others
        if selectedIndex == 0:
            for i in range(1, len(checkboxList)):
                checkboxList[i].set('0')
                checkboxStates[itemList[i]] = '0'
        else:
            # If any other item is selected, deselect the first item
            checkboxList[0].set('0')
            checkboxStates[itemList[0]] = '0'

            # Update the state for the selected item
            checkboxList[selectedIndex].set('1')
            checkboxStates[item] = '1'

        # Update the persistent array object based on the current selection state
        selectedItemsList = [item for i, item in enumerate(itemList) if checkboxList[i].get() == '1']
        self.Update_Persistent_Array(arrayObject, selectedItemsList)
                        
    def determine_item_list(self, selectionKey):
        """
        Determines the correct item list based on the selection key.
        """
        if 'functional' in selectionKey:
            return self.functItems
        elif 'plastic' in selectionKey:
            return self.plasticItems
        else:
            return self.selectItems

    def Handle_Deselection(self, checkboxList, item, checkboxStates, selectionKey, arrayObject):
        """
        Function Name: Handle_Deselection
        Function Purpose: This function is called when a checkbox is deselected.
        """
        # If you want to remove an item from a persisted list or dictionary upon deselection, you can do so here:
        checkboxStates.pop(item, None)
        arrayObject.remove(item)
        
    def Update_Persistent_Array(self, arrayObject, selectedItemsList):
        """
        Function Name: Update_Persistent_Array
        Function Description: This function updates the arrayObject with the selected items list, while keeping existing persisted data.
        """
        # print("Selected Items:", selectedItemsList)
        # print("Before update:", arrayObject)

        selectedSet = set(selectedItemsList)
        arraySet = set(arrayObject)

        # Find items to add and remove
        toAdd = selectedSet - arraySet
        toRemove = arraySet - selectedSet

        for item in toAdd:
            arrayObject.append(item)
        for item in toRemove:
            arrayObject.remove(item)

    def Check_Input(dropArgs):
        """ 
        Function Name: Check_Input
        Function Purpose: This function executes when the user clicks the 'Check' button and finds any missing 
        input fields that will need to be selected before the user can submit to db.
        """   
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)

        try:
            if dropArgs != "":
                # Set blnValidated to True
                blnValidate = True
            else:
                messagebox.showwarning(title='ERROR', message='Input should not be empty. Please Try again.', icon='warning')
                blnValidate = False
        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate
    
    def Check_Checkbox_Input(lstCheckBox, strFieldDesc):
        """
        Function Name: Check_Checkbox_Input
        Function Purpose: This function is called whenever a checkbox is present and needs to check if any of the entries are empty. If so,
        warn the user.
        """    
        # Declare Local Variables
        global blnValidate
        blnValidate = bool(False)
            
        try:
            for i in range(0, len(lstCheckBox)):
                if lstCheckBox[i].get() == '1':
                    # Set blnValidated to True
                    blnValidate = True

            # Check if the blnValidated flag is true or false and warn the user if the entire field is empty
            if blnValidate is True:
                pass
            else:
                messagebox.showwarning(title='ERROR', message='%s field should not be empty. Please verify your selection.'%(strFieldDesc), icon='warning')
                blnValidate = False
                # Select the first checkbox
                lstCheckBox[0].set('1')

        except ValueError:
            messagebox.showwarning(title='ERROR', message='Invalid input. Please Try again.', icon='warning')
            blnValidate = False
            
        return blnValidate 

    def Validate_InputFields(self):
        """ 
        Function Name: Validate_InputFields
        Function Purpose: This function validates the user inputs.
        """
        def validate_field(input_field, checklist, field_name):
            if not BelayDeviceInspection.Check_Input(input_field.get()):
                input_field.focus()
                return False

            if not BelayDeviceInspection.Check_Checkbox_Input(checklist, field_name):
                return False

            return True

        # Define field names
        strVisField = "Visual Result"
        strPhysField = "Physical Result"
        strFunctField = "Functional Result"

        # Validate each field
        if not validate_field(self.dropBelayDeviceVisStatus, self.visCheckList, strVisField):
            return False

        if not validate_field(self.dropBelayDevicePhysStatus, self.physCheckList, strPhysField):
            return False

        if not validate_field(self.dropBelayDeviceFunctStatus, self.functCheckList, strFunctField):
            return False
        
        if not validate_field(self.dropBelayDeviceVisPlastStatus, self.visPlastCheckList, strVisField):
            return False

        if not validate_field(self.dropBelayDevicePhysPlastStatus, self.physPlastCheckList, strPhysField):
            return False

        if not validate_field(self.dropBelayDeviceFunctPlastStatus, self.functPlastCheckList, strFunctField):
            return False

        # All validations passed
        return True
    
    def Pull_UserInput(self):
        """ 
        Function Name: Pull_UserInput
        Function Purpose: This function is executed once the user clicks on the submit button inside the result
        frame. If the user clicks 'Submit', all data is pulled and dumped into the corresponding class objects. 
        """       
        # Declare Local Variables
        sqlBelayDeviceVisMetalSel = ("TBelayDeviceVisMetalSelects", "intBelayDeviceVisMetalSelectID", "strBelayDeviceVisMetalSelect")
        sqlBelayDevicePhysMetalSel = ("TBelayDevicePhysMetalSelects", "intBelayDevicePhysMetalSelectID", "strBelayDevicePhysMetalSelect")
        sqlBelayDeviceFunctMetalSel = ("TBelayDeviceFunctSelects", "intBelayDeviceFunctSelectID", "strBelayDeviceFunctSelect")
        sqlBelayDeviceVisPlastSel = ("TBelayDeviceVisPlasticSelects", "intBelayDeviceVisPlasticSelectID", "strBelayDeviceVisPlastSelect")
        sqlBelayDevicePhysPlastSel = ("TBelayDevicePhysPlasticSelects", "intBelayDevicePhysPlasticSelectID", "strBelayDevicePhysPlastSelect")
        sqlBelayDeviceFunctPlastSel = ("TBelayDeviceFunctPlasticSelects", "intBelayDeviceFunctPlastSelectID", "strBelayDeviceFunctPlastSelect")
        sqlBelayDeviceVisIns = ("TBelayDeviceVisualInspections", "intBelayDeviceVisualInspectionID")
        sqlBelayDevicePhysIns = ("TBelayDevicePhysicalInspections", "intBelayDevicePhysicalInspectionID") 
        sqlBelayDeviceFunctIns = ("TBelayDeviceFunctionInspections", "intBelayDeviceFunctionInspectID") 
        sqlBelayDeviceStandIns = ("TStandardBelayDeviceInspections", "intStandardBelayDeviceInspectionID")

        # Check if the comment is empty. If not, pass in the values. If empty, pass in 'None'
        if self.commInput.get("1.0", "end-1c") != "":
            self.strComment = str(self.commInput.get("1.0", "end-1c"))
            self.strComment += "; "
            # Add the comment to the AutoBelay Comment object
            BelayDeviceInspect.strComment = ''.join(self.strComment)
        else:
            self.strComment = 'None'
            BelayDeviceInspect.strComment = self.strComment
        
        # Get the selected values
        BelayDeviceVisMetSelect = self.Get_Combined_Selection(BelayDeviceVisSelection.astrBelayDeviceVisMetSelect, self.selectItems[0])
        BelayDevicePhysMetSelect = self.Get_Combined_Selection(BelayDevicePhysSelection.astrBelayDevicePhysMetSelect, self.selectItems[0])
        BelayDeviceFunctMetSelect = self.Get_Combined_Selection(BelayDeviceFunctSelection.astrBelayDeviceFunctSelect, self.functItems[0])
        BelayDeviceVisPlastSelect = self.Get_Combined_Selection(BelayDevicePlasticVisSelection.astrBelayDeviceVisPlastSelect, self.plasticItems[0])
        BelayDevicePhysPlastSelect = self.Get_Combined_Selection(BelayDevicePlasticPhysSelection.astrBelayDevicePhysPlastSelect, self.plasticItems[0])
        BelayDeviceFunctPlastSelect = self.Get_Combined_Selection(BelayDevicePlasticFunctSelection.astrBelayDevicePlasticFunctSelect, self.functItems[0])
        
        # # Display the string representation
        # print(BelayDeviceVisMetSelect) 
        # print(BelayDevicePhysMetSelect)
        # print(BelayDeviceFunctMetSelect)
        # print(BelayDeviceVisPlastSelect) 
        # print(BelayDevicePhysPlastSelect)
        # print(BelayDeviceFunctPlastSelect)
        
        # Get the status for the visual, physical selection
        BelayDeviceVisMetStatus = self.dropBelayDeviceVisStatus.get()
        BelayDevicePhysMetStatus = self.dropBelayDevicePhysStatus.get()
        BelayDeviceFunctMetStatus = self.dropBelayDeviceFunctStatus.get()
        BelayDeviceVisPlastStatus = self.dropBelayDeviceVisPlastStatus.get()
        BelayDevicePhysPlastStatus = self.dropBelayDevicePhysPlastStatus.get()
        BelayDeviceFunctPlastStatus = self.dropBelayDeviceFunctPlastStatus.get()
        
        # Get the ID of the selected status item
        BelayDeviceVisMetStatusID = InspectionStatus.astrInspectionStatusDesc.index(BelayDeviceVisMetStatus) + 1
        BelayDevicePhysMetStatusID = InspectionStatus.astrInspectionStatusDesc.index(BelayDevicePhysMetStatus) + 1
        BelayDeviceFunctMetStatusID = InspectionStatus.astrInspectionStatusDesc.index(BelayDeviceFunctMetStatus) + 1
        BelayDeviceVisPlastStatusID = InspectionStatus.astrInspectionStatusDesc.index(BelayDeviceVisPlastStatus) + 1
        BelayDevicePhysPlastStatusID = InspectionStatus.astrInspectionStatusDesc.index(BelayDevicePhysPlastStatus) + 1
        BelayDeviceFunctPlastStatusID = InspectionStatus.astrInspectionStatusDesc.index(BelayDeviceFunctPlastStatus) + 1
        
        # Set the visual, physical, and functional pairs
        visOverallStatusList = (BelayDeviceVisMetStatusID, BelayDeviceVisPlastStatusID)
        physOverallStatusList = (BelayDevicePhysMetStatusID, BelayDevicePhysPlastStatusID)
        functOverallStatusList = (BelayDeviceFunctMetStatusID, BelayDeviceFunctPlastStatusID)
        
        # Get the overall inspection status for each pair
        intVisOverallStatus = BaseFunctions.Check_Overall_Status(visOverallStatusList)
        intPhysOverallStatus = BaseFunctions.Check_Overall_Status(physOverallStatusList)
        intFunctOverallStatus = BaseFunctions.Check_Overall_Status(functOverallStatusList)
        
        # Get the type of selection, either physical, visual, or functional
        VisInsTypeDesc = InspectionType.astrInspectionTypeDesc[0]
        PhysInsTypeDesc = InspectionType.astrInspectionTypeDesc[1]
        FunctInsTypeDesc = InspectionType.astrInspectionTypeDesc[2]

        # Get the ID of the selected Type item
        VisInsTypeID = InspectionType.astrInspectionTypeDesc.index(VisInsTypeDesc) + 1
        PhysInsTypeID = InspectionType.astrInspectionTypeDesc.index(PhysInsTypeDesc) + 1
        FunctInsTypeID = InspectionType.astrInspectionTypeDesc.index(FunctInsTypeDesc) + 1

        # Get the list of items selected and attach them to the selection object for Visual and Physical Selection
        BelayDeviceVisMetalSelectID = self.Get_Or_Create_ID(BelayDeviceVisMetSelect, sqlBelayDeviceVisMetalSel)              
        BelayDevicePhysMetalSelectID = self.Get_Or_Create_ID(BelayDevicePhysMetSelect, sqlBelayDevicePhysMetalSel)
        BelayDeviceFunctMetSelectID = self.Get_Or_Create_ID(BelayDeviceFunctMetSelect, sqlBelayDeviceFunctMetalSel)
        BelayDeviceVisPlastSelectID = self.Get_Or_Create_ID(BelayDeviceVisPlastSelect, sqlBelayDeviceVisPlastSel)              
        BelayDevicePhysPlastSelectID = self.Get_Or_Create_ID(BelayDevicePhysPlastSelect, sqlBelayDevicePhysPlastSel)
        BelayDeviceFunctPlastSelectID = self.Get_Or_Create_ID(BelayDeviceFunctPlastSelect, sqlBelayDeviceFunctPlastSel)
                                    
        # Get the ID's for the base objects in each class
        BelayDeviceVisualInsID = self.Get_Max_Primary_Key(sqlBelayDeviceVisIns[0], sqlBelayDeviceVisIns[1])
        BelayDevicePhysicalInsID = self.Get_Max_Primary_Key(sqlBelayDevicePhysIns[0], sqlBelayDevicePhysIns[1])  
        BelayDeviceFunctionInspectID = self.Get_Max_Primary_Key(sqlBelayDeviceFunctIns[0], sqlBelayDeviceFunctIns[1])      
        StandardBelayDeviceInspectionID = self.Get_Max_Primary_Key(sqlBelayDeviceStandIns[0], sqlBelayDeviceStandIns[1])

        # Assign the local object to the class objects
        bvms = BelayDeviceVisSelection(BelayDeviceVisMetalSelectID, BelayDeviceVisMetSelect, BelayDeviceVisMetStatus)
        bpms = BelayDevicePhysSelection(BelayDevicePhysMetalSelectID, BelayDevicePhysMetSelect, BelayDevicePhysMetStatus)
        bfms = BelayDeviceFunctSelection(BelayDeviceFunctMetSelectID, BelayDeviceFunctMetSelect, BelayDeviceFunctMetStatus)        
        bvps = BelayDevicePlasticVisSelection(BelayDeviceVisPlastSelectID, BelayDeviceVisPlastSelect, BelayDeviceVisPlastStatus)
        bpps = BelayDevicePlasticPhysSelection(BelayDevicePhysPlastSelectID, BelayDevicePhysPlastSelect, BelayDevicePhysPlastStatus)
        bfps = BelayDevicePlasticFunctSelection(BelayDeviceFunctPlastSelectID, BelayDeviceFunctPlastSelect, BelayDeviceFunctPlastStatus)  
        
        # Commit the data to the visual metal inspection
        BelayDeviceVisSelection.intBelayDeviceVisMetalSelectID = bvms.intBelayDeviceVisMetalSelectID
        BelayDeviceVisSelection.strBelayDeviceVisMetSelect = bvms.strBelayDeviceVisMetSelect
        BelayDeviceVisSelection.strBelayDeviceVisStatus = bvms.strBelayDeviceVisStatus
        BelayDevicePlasticVisSelection.intBelayDeviceVisPlasticSelectID = bvps.intBelayDeviceVisPlasticSelectID
        BelayDevicePlasticVisSelection.strBelayDeviceVisPlastSelect = bvps.strBelayDeviceVisPlastSelect
        BelayDevicePlasticVisSelection.strBelayDeviceVisStatus = bvps.strBelayDeviceVisStatus
        BelayDeviceVisualInspect.aBelayDeviceVisualInspectionCache = (BelayDeviceVisualInsID, BelayDevices.intBelayDeviceID, VisInsTypeID, bvms.intBelayDeviceVisMetalSelectID, 
                                                                    bvps.intBelayDeviceVisPlasticSelectID, intVisOverallStatus)

        # Commit the data to the physical metal inspection
        BelayDevicePhysSelection.intBelayDevicePhysMetalSelectID = bpms.intBelayDevicePhysMetalSelectID
        BelayDevicePhysSelection.strBelayDevicePhysMetSelect = bpms.strBelayDevicePhysMetSelect
        BelayDevicePhysSelection.strBelayDevicePhysStatus = bpms.strBelayDevicePhysStatus
        BelayDevicePlasticPhysSelection.intBelayDevicePhysPlasticSelectID = bpps.intBelayDevicePhysPlasticSelectID
        BelayDevicePlasticPhysSelection.strBelayDevicePhysPlastSelect = bpps.strBelayDevicePhysPlastSelect
        BelayDevicePlasticPhysSelection.strBelayDevicePhysStatus = bpps.strBelayDevicePhysStatus        
        BelayDevicePhysicalInspect.aBelayDevicePhysicalCache = (BelayDevicePhysicalInsID, BelayDevices.intBelayDeviceID, PhysInsTypeID, bpms.intBelayDevicePhysMetalSelectID, 
                                                                    bpps.intBelayDevicePhysPlasticSelectID, intPhysOverallStatus)    

        # Commit the data to the function metal inspection
        BelayDeviceFunctSelection.intBelayDeviceFunctSelectID = bfms.intBelayDeviceFunctSelectID
        BelayDeviceFunctSelection.strBelayDeviceFunctSelect = bfms.strBelayDeviceFunctSelect
        BelayDeviceFunctSelection.strBelayDeviceFunctStatus = bfms.strBelayDeviceFunctStatus
        BelayDevicePlasticFunctSelection.intBelayDeviceFunctPlastSelectID = bfps.intBelayDeviceFunctPlastSelectID
        BelayDevicePlasticFunctSelection.strBelayDeviceFunctPlastSelect = bfps.strBelayDeviceFunctPlastSelect
        BelayDevicePlasticFunctSelection.strBelayDeviceFunctStatus = bfps.strBelayDeviceFunctStatus        
        BelayDeviceFunctionInspect.aBelayDeviceFunctCache = (BelayDeviceFunctionInspectID, BelayDevices.intBelayDeviceID, FunctInsTypeID, bfms.intBelayDeviceFunctSelectID,
                                                                    bfps.intBelayDeviceFunctPlastSelectID, intFunctOverallStatus)  

        # Commit the data to the standard inspection
        StandardBelayDeviceInspect.aStandardBelayDeviceInsCache = (StandardBelayDeviceInspectionID, BelayDeviceVisualInsID, BelayDevicePhysicalInsID, BelayDeviceFunctionInspectID)

    def Get_Combined_Selection(self, persisted_array, default_value):
        """
        Function Name: Get_Combined_Selection
        Function Purpose: This function combines the array elements into a comma-separated string,
        and BelayDevices the case when the persisted array is empty by setting a default value.
        """
        if len(persisted_array) == 0:
            return default_value
        else:
            return ",".join(persisted_array)
        
    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = self.Check_Duplicate(item_list, sql_tuple)
        # Check if the flag status has changed to true, if yes, there is a duplicate in the database and keyID was already assigned
        if aReturn[0] is False:
            return Queries.Get_MaxPrimaryKeys(Queries, sql_tuple[0], sql_tuple[1])
        else:
            return aReturn[1]

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
    
    def Check_Duplicate(self, aSelect, sqlStatement):
        """ 
        Function Name: Check_Duplicate
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        selection. Returns the bool value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        keyID = int(0)

        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlStatement[0], sqlStatement[1]))    

        for item in sqlDupValues:
            if aSelect in item:
                keyID = item[0]
                aSelect = item[1]
                blnFlag = bool(True)
                break

        return (blnFlag, keyID, aSelect)
                    
    def Next(self):
        """ 
        Function Name: Next
        Function Purpose: This function is executed once the user clicks on the "Next" button. Once the inputs 
        are validated, the inspection results loads the user selected data and is retained at the object class locations 
        before committing to the database. If all inputs are valid and confirmed by the user, the next stage of inspections is executed.
        """
        global blnValidate
        blnValidate = bool(False)             
        
        # First check if the input is empty, if so, notify the user the input needs attention 
        blnValidate = self.Validate_InputFields()
        
        # If status is true then proceed to update the result field, else, reset the fields
        if blnValidate is True:
            # Check first with the user if the entry's are correct before dumping to DB
            if messagebox.askyesno(message='CAUTION! \n\n Proceed to next inspection page?', icon='question') is True:
                # print(BelayDeviceVisSelection.astrBelayDeviceVisMetSelect)
                # print(BelayDevicePhysSelection.astrBelayDevicePhysMetSelect) 
                # print(BelayDeviceFunctSelection.astrBelayDeviceFunctSelect)
                # Load the user data and prep the data for db dump
                self.Pull_UserInput()     

                # Set the global class bool to true
                Bool_Flag.Set_BelayDevice_Bool_Value_True(Bool_Flag)
                
                # Go to the next inspection component
                self.Next_Inspection()
            else:
                # Check if the user would like to reset the fields
                if messagebox.askyesno(message='ATTENTION! \n\n Would you like to reset the fields?', icon='question') is True:
                    # Clear the input fields and after data is submitted to the database
                    self.Clear()                

    def Clear(self):
        """ 
        Function Name: Clear
        Function Purpose: This function is executed once the user clicks on the Clear button inside the
        frame. If the user clicks 'Clear', all data is set back to default.
        """     
        # Set the list objects first element to the drop click object
        self.dropBelayDeviceVisStatus.set("")
        self.dropBelayDevicePhysStatus.set("")
        self.dropBelayDeviceFunctStatus.set("")
        self.dropBelayDeviceVisPlastStatus.set("")
        self.dropBelayDevicePhysPlastStatus.set("")
        self.dropBelayDeviceFunctPlastStatus.set("")
        
        # Reset the checkboxes to empty selections
        BaseFunctions.Deselect_All_Checkbox(self.visCheckList)
        BaseFunctions.Deselect_All_Checkbox(self.physCheckList)
        BaseFunctions.Deselect_All_Checkbox(self.functCheckList)
        BaseFunctions.Deselect_All_Checkbox(self.visPlastCheckList)
        BaseFunctions.Deselect_All_Checkbox(self.physPlastCheckList)
        BaseFunctions.Deselect_All_Checkbox(self.functPlastCheckList)        

        # Set the first item in the list to the first checkbox item displayed
        self.visCheckList[0].set('1')
        self.physCheckList[0].set('1')
        self.functCheckList[0].set('1')
        self.visPlastCheckList[0].set('1')
        self.physPlastCheckList[0].set('1')
        self.functPlastCheckList[0].set('1')        

        # Clear the class objects
        StandardBelayDeviceInspect.Reset_BelayDevice_Data(self)
        StandardBelayDeviceInspect.Delete_BelayDevice_Data(self)
        
        # Delete the comment field 
        self.commInput.delete("1.0", "end-1c") 
        
    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Expose the window widget to the user
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """     
        # Hide the current window
        self.Exit()  

        # Show the main window after the new window is closed
        BelayDeviceSelection()

    def Next_Inspection(self):
        """ 
        Function Name: Next_Inspection
        Function Purpose: This function is executed once the user clicks on Next button to move to the nex inspection
        type window. Withdraw the parent window and load the new window.
        """           
        # Hide the main window
        self.Exit()  

        if (Bool_Flag.blnComplexWith_Two_ConnectorFlag is True) or (Bool_Flag.blnComplexWithConnectorFlag is True) or (Bool_Flag.blnComplexWithBelayDeviceFlag is True):
            RopeInspection()
        else:
            # Display the results of the inspection
            BelayDeviceInspectionResults()

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        

#######################################################################################################
# BelayDevice Inspection Results Class
#######################################################################################################   

class BelayDeviceInspectionResults(tk.Tk):
    """
    Class Name: BelayDeviceInspectionResults
    Class Description: This class is to display the selected inspection components to the user before the 
    data is dumped to the db. User must complete all previous inspection selection modules in order to submit
    data to the database for a standard inspection.
    """
    def __init__(self):
        """ 
        Function Name: Instantiate the new window
        Function Purpose: This function is executed if the user conducts a new unit inspection. Display a message
        to the user regarding the protocol for each inspection. User must click 'Check' Button in order to submit
        the data to the db.
        """
        # Initialize the Toplevel window
        super().__init__()

        # Get the screen width and height 
        self.widthSize = self.winfo_screenwidth() 
        self.heightSize = self.winfo_screenheight()         

        # calculate x and y coordinates for the Tk root window 
        self.x = (self.widthSize/2) - (610/2)     
        self.y = (self.heightSize/2) - (280/2)    
                        
        # Create the Window attributes                
        self.title("Inspection Results")
        self.geometry('%dx%d+%d+%d' % (610, 280, self.x, self.y))
        self.resizable(False, False)

        # Create the scrollbar frame
        self.scrollFrame = LabelFrame(self, text='Results')
        self.scrollFrame.place(x=5, width=600, height=230)
        self.resultCanvas = Canvas(self.scrollFrame)
        self.resultCanvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.resultScrollBar = Scrollbar(self.scrollFrame, orient=VERTICAL, command=self.resultCanvas.yview)
        self.resultScrollBar.pack(side=RIGHT, fill=Y)
        self.resultCanvas.configure(yscrollcommand=self.resultScrollBar.set)
        self.resultCanvas.bind('<Configure>', lambda event: self.resultCanvas.configure(scrollregion=self.resultCanvas.bbox("all")))

        # Create the third frame to hold the result fields
        self.resultFrame = Frame(self.resultCanvas)
        self.resultCanvas.create_window((0,0), window=self.resultFrame, anchor='nw')
        
        # Bind mousewheel scrolling
        self.resultCanvas.bind_all("<MouseWheel>", self.on_vertical_scroll)

        # Create the label for the drop down menu lists
        self.lblDeviceName = Label(self.resultFrame, text="Belay Device Name:")
        self.lblBelayDeviceType = Label(self.resultFrame, text="Belay Device Type:")
        self.lblSerialNum = Label(self.resultFrame, text="Serial Number:")
        self.lblBumperNum = Label(self.resultFrame, text="Bumper Number:")
        self.lblManuName = Label(self.resultFrame, text="Manufacture Name:")
        self.lblManDate = Label(self.resultFrame, text="Manufacture Date:")
        self.lblInstallDate= Label(self.resultFrame, text="Install Date:")
        self.lblLastInsDate = Label(self.resultFrame, text="Last Inspection Date:")
        self.lblNextInsDate = Label(self.resultFrame, text="Next Inspection Date:")
        self.lblInUse = Label(self.resultFrame, text="Device In Use:")
        self.lblBelayDeviceLocation = Label(self.resultFrame, text="Belay Device Location:")
        self.lblFirstBelayDeviceLine = Label(self.resultFrame, text="----------------------------------")
        self.lblMetBelayDeviceVisual = Label(self.resultFrame, text="Visual Metal Component:")
        self.lblMetBelayDevicePhysical = Label(self.resultFrame, text="Physical Metal Component:")        
        self.lblMetBelayDeviceFunct = Label(self.resultFrame, text="Function Metal Component:")
        self.lblMetBelayDeviceVisualStatus = Label(self.resultFrame, text="Visual Metal Status:")
        self.lblMetBelayDevicePhysicalStatus = Label(self.resultFrame, text="Physical Metal Status:")
        self.lblMetBelayDeviceFunctStatus = Label(self.resultFrame, text="Function Metal Status:")
        self.lblSecondBelayDeviceLine = Label(self.resultFrame, text="----------------------------------")
        self.lblPlastBelayDeviceVisual = Label(self.resultFrame, text="Visual Plastic Component:")
        self.lblPlastBelayDevicePhysical = Label(self.resultFrame, text="Physical Plastic Component:")        
        self.lblPlastBelayDeviceFunct = Label(self.resultFrame, text="Function Plastic Component:")
        self.lblPlastBelayDeviceVisualStatus = Label(self.resultFrame, text="Visual Plastic Status:")
        self.lblPlastBelayDevicePhysicalStatus = Label(self.resultFrame, text="Physical Plastic Status:")
        self.lblPlastBelayDeviceFunctStatus = Label(self.resultFrame, text="Function Plastic Status:")
        
        # Create the label locations
        self.lblDeviceName.grid(row=0, padx=50,  column=0, sticky='W')
        self.lblBelayDeviceType.grid(row=1, padx=50,  column=0, sticky='W') 
        self.lblSerialNum.grid(row=2, padx=50,  column=0, sticky='W')
        self.lblBumperNum.grid(row=3, padx=50,  column=0, sticky='W')
        self.lblManuName.grid(row=4, padx=50, column=0, sticky='W')
        self.lblManDate.grid(row=5, padx=50,  column=0, sticky='W')
        self.lblInstallDate.grid(row=6, padx=50,  column=0, sticky='W')
        self.lblLastInsDate.grid(row=7, padx=50,  column=0, sticky='W')
        self.lblNextInsDate.grid(row=8, padx=50,  column=0, sticky='W')        
        self.lblInUse.grid(row=9, padx=50,  column=0, sticky='W') 
        self.lblBelayDeviceLocation.grid(row=10, padx=50,  column=0, sticky='W') 
        self.lblFirstBelayDeviceLine.grid(row=11, padx=50,  column=0, sticky='W') 
        self.lblMetBelayDeviceVisual.grid(row=12, padx=50,  column=0, sticky='W') 
        self.lblMetBelayDevicePhysical.grid(row=13, padx=50,  column=0, sticky='W') 
        self.lblMetBelayDeviceFunct.grid(row=14, padx=50,  column=0, sticky='W') 
        self.lblMetBelayDeviceVisualStatus.grid(row=15, padx=50,  column=0, sticky='W') 
        self.lblMetBelayDevicePhysicalStatus.grid(row=16, padx=50,  column=0, sticky='W') 
        self.lblMetBelayDeviceFunctStatus.grid(row=17, padx=50,  column=0, sticky='W')
        self.lblSecondBelayDeviceLine.grid(row=18, padx=50,  column=0, sticky='W')  
        self.lblPlastBelayDeviceVisual.grid(row=19, padx=50,  column=0, sticky='W') 
        self.lblPlastBelayDevicePhysical.grid(row=20, padx=50,  column=0, sticky='W') 
        self.lblPlastBelayDeviceFunct.grid(row=21, padx=50,  column=0, sticky='W') 
        self.lblPlastBelayDeviceVisualStatus.grid(row=22, padx=50,  column=0, sticky='W') 
        self.lblPlastBelayDevicePhysicalStatus.grid(row=23, padx=50,  column=0, sticky='W') 
        self.lblPlastBelayDeviceFunctStatus.grid(row=24, padx=50,  column=0, sticky='W') 

        # Create the output boxes to display the results as normal
        self.DeviceNameOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceTypeOutput = Entry(self.resultFrame, width=40, state='normal')
        self.SerialNumOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BumperNumOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ManuNameOutput = Entry(self.resultFrame, width=40, state='normal')
        self.ManDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.InstallDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.LastInsDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.NextInsDateOutput = Entry(self.resultFrame, width=40, state='normal')
        self.InUseOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceLocationOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceMetVisualOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceMetPhysicalOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceMetFunctOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceMetVisStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceMetPhysStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDeviceMetFunctStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDevicePlastVisualOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDevicePlastPhysicalOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDevicePlastFunctOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDevicePlastVisStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDevicePlastPhysStatusOutput = Entry(self.resultFrame, width=40, state='normal')
        self.BelayDevicePlastFunctStatusOutput = Entry(self.resultFrame, width=40, state='normal')        
        
        # Set the last and next inspection date based off of the current date
        aDateResult = BaseFunctions.Update_Inspection_Date()
        LastInspectionDate = datetime.strftime(aDateResult[0], '%Y-%m-%d')
        NextInspectionDate = datetime.strftime(aDateResult[1], '%Y-%m-%d')
                
        # Set the values to the output boxes 
        self.DeviceNameOutput.insert(0, BelayDevices.strBelayDeviceName)
        self.BelayDeviceTypeOutput.insert(0, BelayDevices.strDeviceType)
        self.SerialNumOutput.insert(0, BelayDevices.strSerialNum)
        self.BumperNumOutput.insert(0, BelayDevices.strBumperNum)
        self.ManuNameOutput.insert(0, BelayDevices.strManufactureName)
        self.ManDateOutput.insert(0, BelayDevices.dtmManufactureDate)
        self.InstallDateOutput.insert(0, BelayDevices.dtmInstallationDate)
        self.LastInsDateOutput.insert(0, LastInspectionDate)
        self.NextInsDateOutput.insert(0, NextInspectionDate)
        self.InUseOutput.insert(0, BelayDevices.strEquipInUse)
        self.BelayDeviceLocationOutput.insert(0, WallLocation.strWallLocationDesc)
        self.BelayDeviceMetVisualOutput.insert(0, BelayDeviceVisSelection.strBelayDeviceVisMetSelect)
        self.BelayDeviceMetPhysicalOutput.insert(0, BelayDevicePhysSelection.strBelayDevicePhysMetSelect)
        self.BelayDeviceMetFunctOutput.insert(0, BelayDeviceFunctSelection.strBelayDeviceFunctSelect)
        self.BelayDeviceMetVisStatusOutput.insert(0, BelayDeviceVisSelection.strBelayDeviceVisStatus)
        self.BelayDeviceMetPhysStatusOutput.insert(0, BelayDevicePhysSelection.strBelayDevicePhysStatus)
        self.BelayDeviceMetFunctStatusOutput.insert(0, BelayDeviceFunctSelection.strBelayDeviceFunctStatus)
        self.BelayDevicePlastVisualOutput.insert(0, BelayDevicePlasticVisSelection.strBelayDeviceVisPlastSelect)
        self.BelayDevicePlastPhysicalOutput.insert(0, BelayDevicePlasticPhysSelection.strBelayDevicePhysPlastSelect)
        self.BelayDevicePlastFunctOutput.insert(0, BelayDevicePlasticFunctSelection.strBelayDeviceFunctPlastSelect)
        self.BelayDevicePlastVisStatusOutput.insert(0, BelayDevicePlasticVisSelection.strBelayDeviceVisStatus)
        self.BelayDevicePlastPhysStatusOutput.insert(0, BelayDevicePlasticPhysSelection.strBelayDevicePhysStatus)
        self.BelayDevicePlastFunctStatusOutput.insert(0, BelayDevicePlasticFunctSelection.strBelayDeviceFunctStatus)

        # Create the output boxes to display the results as readonly after the inputs have been placed
        self.DeviceNameOutput.configure(state='readonly')
        self.BelayDeviceTypeOutput.configure(state='readonly')
        self.SerialNumOutput.configure(state='readonly')
        self.BumperNumOutput.configure(state='readonly')
        self.ManuNameOutput.configure(state='readonly')
        self.ManDateOutput.configure(state='readonly')
        self.InstallDateOutput.configure(state='readonly')
        self.LastInsDateOutput.configure(state='readonly')
        self.NextInsDateOutput.configure(state='readonly')
        self.InUseOutput.configure(state='readonly')
        self.BelayDeviceLocationOutput.configure(state='readonly')
        self.BelayDeviceMetVisualOutput.configure(state='readonly')
        self.BelayDeviceMetPhysicalOutput.configure(state='readonly')
        self.BelayDeviceMetFunctOutput.configure(state='readonly')
        self.BelayDeviceMetVisStatusOutput.configure(state='readonly')
        self.BelayDeviceMetPhysStatusOutput.configure(state='readonly')
        self.BelayDeviceMetFunctStatusOutput.configure(state='readonly')
        self.BelayDevicePlastVisualOutput.configure(state='readonly')
        self.BelayDevicePlastPhysicalOutput.configure(state='readonly')
        self.BelayDevicePlastFunctOutput.configure(state='readonly')
        self.BelayDevicePlastVisStatusOutput.configure(state='readonly')
        self.BelayDevicePlastPhysStatusOutput.configure(state='readonly')
        self.BelayDevicePlastFunctStatusOutput.configure(state='readonly')        
        
        # Create the grid for the drop down menu list objects
        self.DeviceNameOutput.grid(row=0, column=1)
        self.BelayDeviceTypeOutput.grid(row=1, column=1)
        self.SerialNumOutput.grid(row=2, column=1)   
        self.BumperNumOutput.grid(row=3, column=1) 
        self.ManuNameOutput.grid(row=4, column=1)  
        self.ManDateOutput.grid(row=5, column=1) 
        self.InstallDateOutput.grid(row=6, column=1)
        self.LastInsDateOutput.grid(row=7, column=1) 
        self.NextInsDateOutput.grid(row=8, column=1)   
        self.InUseOutput.grid(row=9, column=1)
        self.BelayDeviceLocationOutput.grid(row=10, column=1)
        self.BelayDeviceMetVisualOutput.grid(row=12, column=1)
        self.BelayDeviceMetPhysicalOutput.grid(row=13, column=1)
        self.BelayDeviceMetFunctOutput.grid(row=14, column=1)
        self.BelayDeviceMetVisStatusOutput.grid(row=15, column=1)
        self.BelayDeviceMetPhysStatusOutput.grid(row=16, column=1)
        self.BelayDeviceMetFunctStatusOutput.grid(row=17, column=1)
        self.BelayDevicePlastVisualOutput.grid(row=19, column=1)
        self.BelayDevicePlastPhysicalOutput.grid(row=20, column=1)
        self.BelayDevicePlastFunctOutput.grid(row=21, column=1)
        self.BelayDevicePlastVisStatusOutput.grid(row=22, column=1)
        self.BelayDevicePlastPhysStatusOutput.grid(row=23, column=1)
        self.BelayDevicePlastFunctStatusOutput.grid(row=24, column=1)
        
        # Create the buttons
        self.btnExit = Button(self, text="Exit", width=10, command=self.Exit)
        self.btnSubmit = Button(self, text="Submit", width=10, command=self.Submit)
        self.btnBack = Button(self, text="Back", width=10, command=self.Back)
            
        # Create the position of the button
        self.btnBack.place(x=140, y=240)
        self.btnSubmit.place(x=270, y=240)
        self.btnExit.place(x=400, y=240)

        # Keep the root window open while the user is interacting with the widgets
        self.mainloop()    

        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)

        # Delete the stored data in the class attributes
        StandardBelayDeviceInspect.Delete_StandBelayDeviceInspect_Data(self)
                
        # Open the Main Menu
        Start_Menu.Delete_Obj_Lists(self)
        BelayDevices_Menu()         

    def on_vertical_scroll(self, event):
        """Scroll the canvas vertically using the mouse wheel."""
        self.resultCanvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
    def Submit(self):
        """ 
        Function Name: Submit
        Function Purpose: This button executes when the user wants to submit the values to the db. First check
        if all of the values are valid. If yes, proceed to upload the new location to the db. Else, reset
        """
        # Check first with the user if the entry's are correct before dumping to DB
        if messagebox.askyesno(message='CAUTION! \n\n Proceed to submit Belay Device inspection?') is True:     
            # Load the user data and prep the data for db dump
            BelayDeviceInspectionResults.Submit_Standard_Inspection(self)
            
            # Check if the user would like to add another inspection
            if messagebox.askyesno(message='SUCCESSFUL UPLOAD! \n\n Would you like to complete another inspection?') is True:
                # Clear the input fields and after data is submitted to the database
                BelayDeviceInspectionResults.Exit(self)
                BelayDeviceSelection()
            else:
                BelayDeviceInspectionResults.Exit(self)
                BelayDevices_Menu()
        else:
            pass  

    def Submit_Standard_Inspection(self):
        """ 
        Function Name: Submit_Standard_Inspection
        Function Purpose: This function is executed once the user clicks on the submit button and all the standard
        inspection data cached arrays will be pulled and dumped into the the database
        """    
        # Set the global BelayDevice Attributes
        BelayDevices.Update_BelayDevices_Inspect_Dates(BelayDevices)        
        
        # Commit the BelayDevice Inspection data to the database
        BelayDeviceVisSelection.Add_BelayDeviceVisSelection_Query(self)
        BelayDevicePhysSelection.Add_BelayDevicePhysSelection_Query(self)
        BelayDeviceFunctSelection.Add_BelayDeviceFunctSelection_Query(self)
        BelayDevicePlasticVisSelection.Add_BelayDeviceVis_Plastic_Selection_Query(self)
        BelayDevicePlasticPhysSelection.Add_BelayDevicePhys_Plastic_Selection_Query(self)
        BelayDevicePlasticFunctSelection.Add_BelayDevicePlasticFunctSelection_Query(self)
        BelayDeviceVisualInspect.Add_BelayDeviceVisualInspect_Query(self)
        BelayDevicePhysicalInspect.Add_BelayDevicePhysicalInspect_Query(self)
        BelayDeviceFunctionInspect.Add_BelayDeviceFunctInspect_Query(self)
        StandardBelayDeviceInspect.Add_StandBelayDeviceInspect_Query(self)
        
        # Get the BelayDevice overall status and update the units in use status 
        BelayDevices.Update_BelayDevices_InUse_Status(BelayDevices)
        
        # Commit the BelayDeviceInspect data to the database
        BelayDeviceInspect.Add_BelayDeviceInspection_Query(self)
        BelayDeviceInspect.Add_BelayDeviceInspector_Query(self)
        BelayDeviceInspect.Add_BelayDeviceLocation_Query(self)
        
        # First check if the unit has been packaged for reservice to add report to db
        if Bool_Flag.Get_BelayDeviceRetired_Bool_Value(Bool_Flag) is True:
            BelayDevicesRetiredReport.Add_BelayDevice_RetiredReport_Query(self)
            
        # Set all the bool values back to False
        Start_Menu.Set_Default_Bool_Values(self)
        
        # Delete the stored data in the class attributes
        StandardBelayDeviceInspect.Delete_StandBelayDeviceInspect_Data(self)       
        BelayDevicesRetiredReport.Delete_BelayDevice_RetiredReport_Data(self)
        Start_Menu.Delete_Obj_Lists(self)        

        # Reload the object lists
        Start_Menu.Load_Obj_Lists(Start_Menu)
                
    def Withdraw(self):
        """ 
        Function Name: Withdraw
        Function Purpose: This function is executed once the user clicks on the Next button inside the
        frame. The window will automatically be hidden from the user until the user either clicks on the Back button.
        """     
        # Hide the window widget from the user
        self.withdraw()  

    def Deiconify(self):
        """ 
        Function Name: Deiconify
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. The window will automatically be exposed to the user and restore all selected information.
        """     
        # Expose the window widget to the user
        self.deiconify()

    def Back(self):
        """ 
        Function Name: Back
        Function Purpose: This function is executed once the user clicks on the Back button inside the
        frame. If the user clicks 'Back', all data is set back to what is stored locally at the class level.
        """     
        # Hide the current window
        self.Exit()  

        # Show the main window after the new window is closed
        BelayDeviceInspection()

    def Exit(self):
        """ 
        Function Name: Exit
        Function Purpose: This function is executed once the user clicks on the exit button inside the result
        frame. If the user clicks 'Exit', the widow is destroyed and the user is sent back to main menu 
        """         
        self.destroy()
        
        
######################################################################################################
# Main Start of Program
#######################################################################################################         

def Main():
    """ 
    Function Name: Main Start Program
    Function Description: This function begins the program. Open the GUI Login Page
    """
    try:
        # Check if python is installed 
        # BaseFunctions.Install_Python()
        
        # Load the requirements for all python libraries
        # BaseFunctions.Install_Requirements()

        # Set the database attributes
        Database.dbSet_Database_Attr(Database)
        
        # Make sure to comment out before production 
        Start_Menu()
        #AutoBelay_Menu()
        #Ropes_Menu()
        #Build_Rope_Sys_Setup()
        #GymRopeSelection()
        #RopeInspection()
        #Connectors_Menu()
        #ConnectorSelection()
        #TwoConnectorSelection()
        #TwoConnectorInspection()
        #ConnectorInspection()
        #BelayDevices_Menu()
        #elayDeviceSelection()
        #BelayDeviceInspection()
        
        # Send the files to the recipients
        Send_Email.check_Primary_Inspect_EmailQuery()
        
        # Start the main GUI window
        # UserLogin_Main()    
        
    # Display error message if the entry is invalid
    except Exception as err:
        print("Exception occurred because", err)

# This is the start of main program
if __name__ == '__main__':
    Main()