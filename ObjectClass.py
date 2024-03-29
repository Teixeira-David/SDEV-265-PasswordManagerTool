"""
.______    _______ .___________.    ___         .______   .______       _______     ___       __  ___ 
|   _  \  |   ____||           |   /   \        |   _  \  |   _  \     |   ____|   /   \     |  |/  / 
|  |_)  | |  |__   `---|  |----`  /  ^  \       |  |_)  | |  |_)  |    |  |__     /  ^  \    |  '  /  
|   _  <  |   __|      |  |      /  /_\  \      |   _  <  |      /     |   __|   /  /_\  \   |    <   
|  |_)  | |  |____     |  |     /  _____  \     |  |_)  | |  |\  \----.|  |____ /  _____  \  |  .  \  
|______/  |_______|    |__|    /__/     \__\    |______/  | _| `._____||_______/__/     \__\ |__|\__\                                                                                                       
"""
# ----------------------------------------------------------------------------------------------------
# Module Name: Object Class Module
# Module Description: This module contains all the classes for each Inspector, Login Cred, Facility,
# and Fire Extinguisher Component. 
# ----------------------------------------------------------------------------------------------------

# Import Python Libraries
from datetime import datetime, date
from tkinter import *
from pyisemail import is_email
from tkinter import *
from tkinter import messagebox, filedialog

# Import from Project modules
from BaseFunctionClass import BaseFunctions
from DatabaseScript import Database, Queries

#######################################################################################################
# Primary Class Objects
#######################################################################################################
class Bool_Flag():
    """
    Class Name: Bool_Flag
    Class Description: This class is used to determine the persisted value status for any class object after a window
    is loaded and has user interaction.
    """
    def __init__(self, blnCarabPersistFlag=False, blnLanyardPersistFlag=False, blnBrakePersistFlag=False,
                blnCasePersistFlag=False, blnHandlePersistFlag=False, blnAutoBelayPersistFlag=False,
                blnOutForService=False, blnSerialNumRadioSelect=False, blnBumperNumRadioSelect=False,
                blnRopePersistFlag=False, blnConnectorPersistFlag=False, blnBelayDevicePersistFlag=False,
                blnRopeSystemPersistFlag=False, blnComplexWithConnectorFlag=False, blnComplexWithBelayDeviceFlag=False,
                blnRopeRetiredFlag=False, blnConnectorRetiredFlag=False, blnBelayDeviceRetiredFlag=False,
                blnComplexWith_Two_ConnectorFlag=False, blnSimpleRopeFlag=False,
                ):
        self.blnCarabPersistFlag = blnCarabPersistFlag
        self.blnLanyardPersistFlag = blnLanyardPersistFlag
        self.blnBrakePersistFlag = blnBrakePersistFlag
        self.blnCasePersistFlag = blnCasePersistFlag
        self.blnHandlePersistFlag = blnHandlePersistFlag
        self.blnAutoBelayPersistFlag = blnAutoBelayPersistFlag
        self.blnOutForService = blnOutForService
        self.blnSerialNumRadioSelect = blnSerialNumRadioSelect
        self.blnBumperNumRadioSelect = blnBumperNumRadioSelect
        self.blnRopePersistFlag = blnRopePersistFlag
        self.blnConnectorPersistFlag = blnConnectorPersistFlag
        self.blnBelayDevicePersistFlag = blnBelayDevicePersistFlag
        self.blnRopeSystemPersistFlag = blnRopeSystemPersistFlag
        self.blnComplexWithConnectorFlag = blnComplexWithConnectorFlag
        self.blnComplexWithBelayDeviceFlag = blnComplexWithBelayDeviceFlag
        self.blnRopeRetiredFlag = blnRopeRetiredFlag
        self.blnConnectorRetiredFlag = blnConnectorRetiredFlag
        self.blnBelayDeviceRetiredFlag = blnBelayDeviceRetiredFlag
        self.blnComplexWith_Two_ConnectorFlag = blnComplexWith_Two_ConnectorFlag,
        self.blnSimpleRopeFlag = blnSimpleRopeFlag
        
    # Property decorator object get function to access private blnCarabPersistFlag
    @property
    def blnCarabPersistFlag(self):
        return self._blnCarabPersistFlag

    # Property decorator object get function to access private blnLanyardPersistFlag
    @property
    def blnLanyardPersistFlag(self):
        return self._blnLanyardPersistFlag
    
    # Property decorator object get function to access private blnBrakePersistFlag
    @property
    def blnBrakePersistFlag(self):
        return self._blnBrakePersistFlag

    # Property decorator object get function to access private blnCasePersistFlag
    @property
    def blnCasePersistFlag(self):
        return self._blnCasePersistFlag

    # Property decorator object get function to access private blnHandlePersistFlag
    @property
    def blnHandlePersistFlag(self):
        return self._blnHandlePersistFlag

    # Property decorator object get function to access private blnAutoBelayPersistFlag
    @property
    def blnAutoBelayPersistFlag(self):
        return self._blnAutoBelayPersistFlag

    # Property decorator object get function to access private blnSerialNumRadioSelect
    @property
    def blnSerialNumRadioSelect(self):
        return self._blnSerialNumRadioSelect

    # Property decorator object get function to access private blnOutForService
    @property
    def blnOutForService(self):
        return self._blnOutForService
    
    # Property decorator object get function to access private blnSerialNumRadioSelect
    @property
    def blnSerialNumRadioSelect(self):
        return self._blnSerialNumRadioSelect

    # Property decorator object get function to access private blnBumperNumRadioSelect
    @property
    def blnBumperNumRadioSelect(self):
        return self.blnBumperNumRadioSelect

    # Property decorator object get function to access private blnRopePersistFlag
    @property
    def blnRopePersistFlag(self):
        return self.blnRopePersistFlag

    # Property decorator object get function to access private blnConnectorPersistFlag
    @property
    def blnConnectorPersistFlag(self):
        return self.blnConnectorPersistFlag
    
    # Property decorator object get function to access private blnBelayDevicePersistFlag
    @property
    def blnBelayDevicePersistFlag(self):
        return self.blnBelayDevicePersistFlag
    
    # Property decorator object get function to access private blnRopeSystemPersistFlag
    @property
    def blnRopeSystemPersistFlag(self):
        return self.blnRopeSystemPersistFlag    

    # Property decorator object get function to access private blnComplexWithConnectorFlag
    @property
    def blnComplexWithConnectorFlag(self):
        return self.blnComplexWithConnectorFlag
    
    # Property decorator object get function to access private blnComplexWithBelayDeviceFlag
    @property
    def blnComplexWithBelayDeviceFlag(self):
        return self.blnComplexWithBelayDeviceFlag   

    # Property decorator object get function to access private blnRopeRetiredFlag
    @property
    def blnRopeRetiredFlag(self):
        return self.blnRopeRetiredFlag    

    # Property decorator object get function to access private blnConnectorRetiredFlag
    @property
    def blnConnectorRetiredFlag(self):
        return self.blnConnectorRetiredFlag
    
    # Property decorator object get function to access private blnBelayDeviceRetiredFlag
    @property
    def blnBelayDeviceRetiredFlag(self):
        return self.blnBelayDeviceRetiredFlag   

    # Property decorator object get function to access private blnComplexWith_Two_ConnectorFlag
    @property
    def blnComplexWith_Two_ConnectorFlag(self):
        return self.blnComplexWith_Two_ConnectorFlag 

    # Property decorator object get function to access private blnSimpleRopeFlag
    @property
    def blnSimpleRopeFlag(self):
        return self.blnSimpleRopeFlag 
                    
    # setter method 
    @blnCarabPersistFlag.setter 
    def blnCarabPersistFlag(self, blnCarabPersistFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnCarabPersistFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnCarabPersistFlag = blnCarabPersistFlag

    # setter method 
    @blnCarabPersistFlag.setter 
    def blnCarabPersistFlag(self, blnCarabPersistFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnCarabPersistFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnCarabPersistFlag = blnCarabPersistFlag

    # setter method 
    @blnLanyardPersistFlag.setter 
    def blnLanyardPersistFlag(self, blnLanyardPersistFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnLanyardPersistFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnLanyardPersistFlag = blnLanyardPersistFlag

    # setter method 
    @blnBrakePersistFlag.setter 
    def blnBrakePersistFlag(self, blnBrakePersistFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnBrakePersistFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnBrakePersistFlag = blnBrakePersistFlag

    # setter method 
    @blnCasePersistFlag.setter 
    def blnCasePersistFlag(self, blnCasePersistFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnCasePersistFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnCasePersistFlag = blnCasePersistFlag

    # setter method 
    @blnHandlePersistFlag.setter 
    def blnHandlePersistFlag(self, blnHandlePersistFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnHandlePersistFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnHandlePersistFlag = blnHandlePersistFlag

    # setter method 
    @blnAutoBelayPersistFlag.setter 
    def blnAutoBelayPersistFlag(self, blnAutoBelayPersistFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnAutoBelayPersistFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnAutoBelayPersistFlag = blnAutoBelayPersistFlag

    # setter method 
    @blnOutForService.setter 
    def blnOutForService(self, blnOutForService): 
        # Return true if specified object is of str type
        if not isinstance(blnOutForService, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnOutForService = blnOutForService

    # setter method 
    @blnSerialNumRadioSelect.setter 
    def blnSerialNumRadioSelect(self, blnSerialNumRadioSelect): 
        # Return true if specified object is of str type
        if not isinstance(blnSerialNumRadioSelect, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnSerialNumRadioSelect = blnSerialNumRadioSelect

    # setter method 
    @blnBumperNumRadioSelect.setter 
    def blnBumperNumRadioSelect(self, blnBumperNumRadioSelect): 
        # Return true if specified object is of str type
        if not isinstance(blnBumperNumRadioSelect, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnBumperNumRadioSelect = blnBumperNumRadioSelect
            
    # setter method 
    @blnRopePersistFlag.setter 
    def blnRopePersistFlag(self, blnRopePersistFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnRopePersistFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnRopePersistFlag = blnRopePersistFlag            

    # setter method 
    @blnConnectorPersistFlag.setter 
    def blnConnectorPersistFlag(self, blnConnectorPersistFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnConnectorPersistFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnConnectorPersistFlag = blnConnectorPersistFlag 

    # setter method 
    @blnBelayDevicePersistFlag.setter 
    def blnBelayDevicePersistFlag(self, blnBelayDevicePersistFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnBelayDevicePersistFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnBelayDevicePersistFlag = blnBelayDevicePersistFlag 

    # setter method 
    @blnRopeSystemPersistFlag.setter 
    def blnRopeSystemPersistFlag(self, blnRopeSystemPersistFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnRopeSystemPersistFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnRopeSystemPersistFlag = blnRopeSystemPersistFlag 

    # setter method 
    @blnComplexWithConnectorFlag.setter 
    def blnComplexWithConnectorFlag(self, blnComplexWithConnectorFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnComplexWithConnectorFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnComplexWithConnectorFlag = blnComplexWithConnectorFlag 

    # setter method 
    @blnComplexWithBelayDeviceFlag.setter 
    def blnComplexWithBelayDeviceFlag(self, blnComplexWithBelayDeviceFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnComplexWithBelayDeviceFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnComplexWithBelayDeviceFlag = blnComplexWithBelayDeviceFlag 

    # setter method 
    @blnRopeRetiredFlag.setter 
    def blnRopeRetiredFlag(self, blnRopeRetiredFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnRopeRetiredFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnRopeRetiredFlag = blnRopeRetiredFlag 

    # setter method 
    @blnConnectorRetiredFlag.setter 
    def blnConnectorRetiredFlag(self, blnConnectorRetiredFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnConnectorRetiredFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnConnectorRetiredFlag = blnConnectorRetiredFlag 

    # setter method 
    @blnBelayDeviceRetiredFlag.setter 
    def blnBelayDeviceRetiredFlag(self, blnBelayDeviceRetiredFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnBelayDeviceRetiredFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnBelayDeviceRetiredFlag = blnBelayDeviceRetiredFlag 

    # setter method 
    @blnComplexWith_Two_ConnectorFlag.setter 
    def blnComplexWith_Two_ConnectorFlag(self, blnComplexWith_Two_ConnectorFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnComplexWith_Two_ConnectorFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnComplexWith_Two_ConnectorFlag = blnComplexWith_Two_ConnectorFlag 

    # setter method 
    @blnSimpleRopeFlag.setter 
    def blnSimpleRopeFlag(self, blnSimpleRopeFlag): 
        # Return true if specified object is of str type
        if not isinstance(blnSimpleRopeFlag, bool): 
            raise TypeError('Flag input must be a boolean') 
        else:
            self._blnSimpleRopeFlag = blnSimpleRopeFlag                                                
                                                                                    
    def Get_Carab_Bool_Value(self):
        return self.blnCarabPersistFlag

    def Get_Lanyard_Bool_Value(self):
        return self.blnLanyardPersistFlag

    def Get_Brake_Bool_Value(self):
        return self.blnBrakePersistFlag

    def Get_Case_Bool_Value(self):
        return self.blnCasePersistFlag

    def Get_Handle_Bool_Value(self):
        return self.blnHandlePersistFlag

    def Get_AutoBelay_Bool_Value(self):
        return self.blnAutoBelayPersistFlag

    def Get_OutForService_Bool_Value(self):
        return self.blnOutForService
    
    def Get_SerialNumRadio_Bool_Value(self):
        return self.blnSerialNumRadioSelect    

    def Get_BumperNumRadio_Bool_Value(self):
        return self.blnBumperNumRadioSelect
    
    def Get_RopeSystem_Bool_Value(self):
        return self.blnRopeSystemPersistFlag

    def Get_ComplexWithConnector_Bool_Value(self):
        return self.blnComplexWithConnectorFlag
    
    def Get_ComplexWithBelayDevice_Bool_Value(self):
        return self.blnComplexWithBelayDeviceFlag

    def Get_RopeRetired_Bool_Value(self):
        return self.blnRopeRetiredFlag

    def Get_ConnectorRetired_Bool_Value(self):
        return self.blnConnectorRetiredFlag
    
    def Get_BelayDeviceRetired_Bool_Value(self):
        return self.blnBelayDeviceRetiredFlag

    def Get_ComplexWithTwo_Bool_Value(self):
        return self.blnComplexWith_Two_ConnectorFlag

    def Get_SimpleRope_Bool_Value(self):
        return self.blnSimpleRopeFlag
                
    def Set_Carab_Bool_Value_True(self):
        self.blnCarabPersistFlag = True

    def Set_Carab_Bool_Value_False(self):
        self.blnCarabPersistFlag = False

    def Set_Lanyard_Bool_Value_True(self):
        self.blnLanyardPersistFlag = True

    def Set_Lanyard_Bool_Value_False(self):
        self.blnLanyardPersistFlag = False

    def Set_Brake_Bool_Value_True(self):
        self.blnBrakePersistFlag = True

    def Set_Brake_Bool_Value_False(self):
        self.blnBrakePersistFlag = False

    def Set_Case_Bool_Value_True(self):
        self.blnCasePersistFlag = True

    def Set_Case_Bool_Value_False(self):
        self.blnCasePersistFlag = False

    def Set_Handle_Bool_Value_True(self):
        self.blnHandlePersistFlag = True

    def Set_Handle_Bool_Value_False(self):
        self.blnHandlePersistFlag = False

    def Set_AutoBelay_Bool_Value_True(self):
        self.blnAutoBelayPersistFlag = True

    def Set_AutoBelay_Bool_Value_False(self):
        self.blnAutoBelayPersistFlag = False

    def Set_OutForService_Bool_Value_True(self):
        self.blnOutForService = True

    def Set_OutForService_Bool_Value_False(self):
        self.blnOutForService = False

    def Set_SerialRadio_Bool_Value_True(self):
        self.blnSerialNumRadioSelect = True

    def Set_SerialRadio_Bool_Value_False(self):
        self.blnSerialNumRadioSelect = False

    def Set_BumperRadio_Bool_Value_True(self):
        self.blnBumperNumRadioSelect = True

    def Set_BumperRadio_Bool_Value_False(self):
        self.blnBumperNumRadioSelect = False
        
    def Set_Rope_Bool_Value_True(self):
        self.blnRopePersistFlag = True

    def Set_Rope_Bool_Value_False(self):
        self.blnRopePersistFlag = False     

    def Set_Connector_Bool_Value_True(self):
        self.blnConnectorPersistFlag = True

    def Set_Connector_Bool_Value_False(self):
        self.blnConnectorPersistFlag = False  
        
    def Set_BelayDevice_Bool_Value_True(self):
        self.blnBelayDevicePersistFlag = True

    def Set_BelayDevice_Bool_Value_False(self):
        self.blnBelayDevicePersistFlag = False   

    def Set_RopeSystem_Bool_Value_True(self):
        self.blnRopeSystemPersistFlag = True

    def Set_RopeSystem_Bool_Value_False(self):
        self.blnRopeSystemPersistFlag = False

    def Set_ComplexWithConnector_Bool_Value_True(self):
        self.blnComplexWithConnectorFlag = True

    def Set_ComplexWithConnector_Bool_Value_False(self):
        self.blnComplexWithConnectorFlag = False

    def Set_ComplexWithBelayDevice_Bool_Value_True(self):
        self.blnComplexWithBelayDeviceFlag = True

    def Set_ComplexWithBelayDevice_Bool_Value_False(self):
        self.blnComplexWithBelayDeviceFlag = False                          

    def Set_RopeRetired_Bool_Value_False(self):
        self.blnRopeRetiredFlag = False

    def Set_RopeRetired_Bool_Value_True(self):
        self.blnRopeRetiredFlag = True

    def Set_ConnectorRetired_Bool_Value_False(self):
        self.blnConnectorRetiredFlag = False

    def Set_ConnectorRetired_Bool_Value_True(self):
        self.blnConnectorRetiredFlag = True 

    def Set_BelayDeviceRetired_Bool_Value_False(self):
        self.blnBelayDeviceRetiredFlag = False

    def Set_BelayDeviceRetired_Bool_Value_True(self):
        self.blnBelayDeviceRetiredFlag = True

    def Set_ComplexWithTwo_Bool_Value_False(self):
        self.blnComplexWith_Two_ConnectorFlag = False

    def Set_ComplexWithTwo_Bool_Value_True(self):
        self.blnComplexWith_Two_ConnectorFlag = True

    def Set_SimpleRope_Bool_Value_False(self):
        self.blnSimpleRopeFlag = False

    def Set_SimpleRope_Bool_Value_True(self):
        self.blnSimpleRopeFlag = True        
        
                                
class Inspector():
    """
    Class Name: Inspector
    Class Description: This class gets and sets inspector information (fName, lName, Email)
    """
    # Create class variable shared amongst all Inspector methods
    aintInspectorID = []   
    astrLoginName = []
    
    # Common base class for all Inspectors information. Instantiates the base class
    def __init__(self, intInspectorID, strFirstName, strLastName, strEmail):
        self.intInspectorID = intInspectorID
        self.strFirstname = strFirstName
        self.strLastname = strLastName
        self.strEmail = strEmail 

    # Create a string with first and last names appended together
    def __str__(self):
        # Assign the first and last names to appended string
        return str(self.strLastName + '.' + self.strFirstName)
                    
    # Property decorator object get function to access private Inspector ID
    @property
    def intInspectorID(self):
        return self._intInspectorID

    # Property decorator object get function to access private First Name
    @property
    def strFirstName(self):
        return self._strFirstName

    # Property decorator object get function to access private Last Name
    @property
    def strLastName(self):
        return self._strLastName         

    # Property decorator object get function to access private Email
    @property
    def strEmail(self):
        return self._strEmail

    # setter method 
    @intInspectorID.setter 
    def intInspectorID(self, intInspectorID): 
        # Return true if specified object is of int type
        if not isinstance(intInspectorID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intInspectorID < 0:  
            raise ValueError('ID cannot be empty') 

        self._intInspectorID = intInspectorID
    
    # setter method 
    @strFirstName.setter 
    def strFirstName(self, strFirstName): 
        # Return true if specified object is of str type
        if not isinstance(strFirstName, str): 
            raise TypeError('First Name must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha
        if strFirstName.isspace(): 
            raise ValueError('First Name cannot be empty') 
        # Set the attribute to the value if true
        elif strFirstName.isalpha():
            self._strFirstName = strFirstName.capitalize()

    # setter method 
    @strLastName.setter 
    def strLastName(self, strLastName): 
        # Return true if specified object is of str type
        if not isinstance(strLastName, str):
            raise TypeError('Last Name must be a string') 
        # Check if the value is empty, otherwise check if the value is isascii
        if strLastName.isspace(): 
            raise ValueError('Last Name cannot be empty') 
        # Set the attribute to the value if true
        elif strLastName.isascii():
            self._strLastName = strLastName.capitalize()

    # setter method 
    @strEmail.setter 
    def strEmail(self, strEmail): 
        blnFLAG = bool(False)
        blnFLAG = is_email(strEmail,  allow_gtld=True)
        # Return true if specified object is of str type
        if not isinstance(strEmail, str): 
            raise TypeError('Email must be an string') 
        # Check if the value is empty, otherwise check if the value is isascii
        if strEmail.isspace(): 
            raise ValueError('Email cannot be empty') 
        # Set the attribute to the value if true
        if strEmail.isascii() and blnFLAG is True:
            self._strEmail = strEmail                   
        
    def Append_InspectorIDList(self, intObject):
        """ 
        Function Name: Append_InspectorIDList
        Function Description: This function appends objects to the Inspector ID list
        """    
        self.aintInspectorID.append(intObject)

    def Remove_InspectorIDList(self, intObject):
        """ 
        Function Name: Remove_InspectorIDList
        Function Description: This function removes objects in the Inspector ID list
        """    
        self.aintInspectorID.remove(intObject)

    def Get_InspectorIDList_Obj(self):
        """ 
        Function Name: Get_InspectorIDList_Obj
        Function Description: This function gets all the objects in the Inspector ID list
        """    
        return self.aintInspectorID

    def Append_InspectorNameList(self, intObject):
        """ 
        Function Name: Append_InspectorNameList
        Function Description: This function appends objects to the Inspector Name list
        """    
        self.astrLoginName.append(intObject)

    def Remove_InspectorNameList(self, intObject):
        """ 
        Function Name: Remove_InspectorNameList
        Function Description: This function removes objects in the Inspector Name list
        """    
        self.astrLoginName.remove(intObject)

    def Get_InspectorNameList_Obj(self):
        """ 
        Function Name: Get_InspectorNameList_Obj
        Function Description: This function gets all the objects in the Inspector Name list
        """    
        return self.astrLoginName
    
    def Delete_Inspector_Data(self):
        """ 
        Function Name: Delete_Inspector_Data
        Function Description: This function removes all the objects in the Inspector class
        """    
        Inspector.aintInspectorID = []   
        Inspector.astrLoginName = []

    def Get_Inspector_Data(self):
        """ 
        Function Name: Get_Login_Data
        Function Description: This function gets all the objects in the Logins table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TInspectors"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the housing Data List
        for i in range(len(QueryResultList)):
            Inspector.Append_InspectorIDList(self, QueryResultList[i][0])
            Inspector.Append_InspectorNameList(self, (QueryResultList[i][1] + '.' + QueryResultList[i][2]))

    def Add_NewInspector_Query(self):
        """ 
        Function Name: Add_NewInspector_Query
        Function Description: This function updates the database with all of the new Inspector objects executing
        the stored procedure uspAddNewInspector
        """    
        # Create the sql query string
        sqlTableCol = ("intInspectorID", "strFirstName", "strLastName", "strEmail")
        sqlTableName = "TInspectors"   
        sqlTableValues = (self.intInspectorID, self.strFirstName, self.strLastName, self.strEmail)   
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)        

    def Update_InspectorCred_Query(self):
        """ 
        Function Name: Update_InspectorCred_Query
        Function Description: This function updates the database with all of the new Inspector objects executing
        the stored procedure uspAddNewInspector
        """    
        # Create the sql query string
        sqlTableCol = ("strFirstName", "strLastName", "strEmail")
        sqlTableName = "TInspectors"   
        sqlPrimID = "intInspectorID"
        sqlTableValues = (self.strFirstName, self.strLastName, self.strEmail)
        sqlKeyID = self.intInspectorID
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlPrimID, sqlKeyID)
        
        # Execute the stored procedure
        Queries.dbExeUSP_UpdateValues(Queries, sqlParams)

        # Clear the attributes
        # self.Clear_Inspector_Attributes()
        self.Delete_Inspector_Data()
        
    def Clear_Inspector_Attributes(self):
        """ 
        Function Name: Clear_Inspector_Attributes
        Function Description: This function clears the Inspector attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intInspectorID", "strFirstName", "strLastName", "strEmail")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                    
        
class LoginName():
    """
    Class Name: LoginName
    Class Description: This class gets and sets the user login name. 
    """
    # Create class variable shared amongst all LoginName methods
    aintLoginID = []   
    astrLoginName = []
    astrLoginPassword = []
        
    # Common base class for all user login names. Instantiates the base class
    def __init__(self, intLoginID, strLoginName, strLoginPassword):
        self.intLoginID = intLoginID
        self.strLoginName = strLoginName
        self.strLoginPassword = strLoginPassword

    # Append the First and Last names to assign a login name
    def __str__(self):
        self.strLoginName = str(self.strFirstName + "." + self.strLastName)
        return self.strLoginName
            
    # Property decorator object get function to access private User Login ID
    @property
    def intLoginID(self):
        return self._intLoginID

    # Property decorator object get function to access private User Login Name
    @property
    def strLoginName(self):
        return self._strLoginName

    # Property decorator object get function to access private strPassword
    @property
    def strLoginPassword(self):
        return self._strLoginPassword   
            
    # setter method 
    @intLoginID.setter 
    def intLoginID(self, intLoginID): 
        # Return true if specified object is of int type
        if not isinstance(intLoginID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intLoginID < 0: 
            raise ValueError('ID cannot be empty') 
        self._intLoginID = intLoginID
                
    # setter method 
    @strLoginName.setter 
    def strLoginName(self, strLoginName): 
        # Return true if specified object is of str type
        if not isinstance(strLoginName, str): 
            raise TypeError('Login Name must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha
        if strLoginName.isspace(): 
            raise ValueError('Login Name cannot be empty') 
        elif strLoginName.isascii():
            self._strLoginName = strLoginName

    # setter method 
    @strLoginPassword.setter 
    def strLoginPassword(self, strLoginPassword): 
        # Return true if specified object is of str type
        if not isinstance(strLoginPassword, str): 
            raise TypeError('Password must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strLoginPassword.isspace(): 
            raise ValueError('Password cannot be empty') 
        elif strLoginPassword.isascii():
            self._strLoginPassword = strLoginPassword
            
    def Append_LoginIDList(self, intObject):
        """ 
        Function Name: Append_LoginIDList
        Function Description: This function appends objects to the Login ID list
        """
        self.aintLoginID.append(intObject)

    def Remove_LoginIDList(self, intObject):
        """ 
        Function Name: Remove_LoginIDList
        Function Description: This function removes objects in the Login ID list
        """    
        self.aintLoginID.remove(intObject)

    def Get_LoginIDList_Obj(self):
        """ 
        Function Name: Get_LoginIDList_Obj
        Function Description: This function gets all the objects in the Login ID list
        """    
        return self._aintLoginID
    
    def Append_LoginNameList(self, strObject):
        """ 
        Function Name: Append_LoginNameList
        Function Description: This function appends objects to the Login name list
        """    
        self.astrLoginName.append(strObject)

    def Remove_LoginNameList(self, strObject):
        """ 
        Function Name: Remove_LoginNameList
        Function Description: This function removes objects in the Login name list
        """    
        self.astrLoginName.remove(strObject)

    def Get_LoginNameList_Obj(self):
        """ 
        Function Name: Get_LoginNameList_Obj
        Function Description: This function gets all the objects in the Login name list
        """    
        return self.astrLoginName
    
    def Append_LoginPswrdList(self, strObject):
        """ 
        Function Name: Append_LoginPswrdList
        Function Description: This function appends objects to the Login Password list
        """    
        self.astrLoginPassword.append(strObject)

    def Remove_LoginPswrdList(self, strObject):
        """ 
        Function Name: Remove_LoginPswrdList
        Function Description: This function removes objects in the Login Password list
        """    
        self.astrLoginPassword.remove(strObject)

    def Get_LoginPswrdList_Obj(self):
        """ 
        Function Name: Get_LoginPswrdList_Obj
        Function Description: This function gets all the objects in the Login Password list
        """    
        return self._astrLoginPassword    

    def Delete_Login_Data(self):
        """ 
        Function Name: Delete_Login_Data
        Function Description: This function removes all the objects in the LoginName class
        """    
        self.aintLoginID = []
        self.astrLoginName = []
        self.astrLoginPassword = []

    def Get_Login_Data(self):
        """ 
        Function Name: Get_Login_Data
        Function Description: This function gets all the objects in the Logins table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TLogins"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the housing Data List
        for i in range(len(QueryResultList)):
            LoginName.Append_LoginIDList(self, QueryResultList[i][0])
            LoginName.Append_LoginNameList(self, QueryResultList[i][1])
            LoginName.Append_LoginPswrdList(self, QueryResultList[i][2]) 
                                    
    def Add_NewLoginName_Query(self):
        """ 
        Function Name: Add_NewLoginName_Query
        Function Description: This function updates the database with all of the new LoginName objects executing
        the stored procedure uspAddNewLogin
        """    
        # Create the sql query string
        sqlTableCol = ("intLoginID", "strLoginName", "strPassword")
        sqlTableName = "TLogins"  
        
        # Get the max primary key
        self.intLoginID = Queries.Get_MaxPrimaryKeys(Queries, sqlTableName, sqlTableCol[0])
        
        # Load the values                
        sqlTableValues = (self.intLoginID, self.strLoginName, self.strLoginPassword)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)
        
        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)      

    def Update_LoginCred_Query(self):
        """ 
        Function Name: Update_LoginCred_Query
        Function Description: This function updates the database with all of the new Inspector objects executing
        the stored procedure uspAddNewInspector
        """    
        # Get the login names 
        self.Get_Login_Data()
        
        # Get the ID of the user login name selected 
        for i, value in enumerate(self.astrLoginName):
            if self.strLoginName == value:
                self.intLoginID = i + 1
                
        # Create the sql query string
        sqlTableCol = ("strLoginName", "strPassword")
        sqlTableName = "TLogins"  
        sqlPrimID = "intLoginID"
        sqlTableValues = (self.strLoginName, self.strLoginPassword)
        sqlKeyID = self.intLoginID
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlPrimID, sqlKeyID)
        
        # Execute the stored procedure
        Queries.dbExeUSP_UpdateValues(Queries, sqlParams)

        # Clear the attributes
        # self.Clear_Login_Attributes()
        self.Delete_Login_Data()

    def Clear_Login_Attributes(self):
        """ 
        Function Name: Clear_Login_Attributes
        Function Description: This function clears the Login attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intLoginID", "strLoginName", "strPassword")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                                
    def Check_Login_Name(logName):
        """ 
        Function Name: Check_Login_Name
        Function Description: This function validates the user user login name and returns a tuple of the 
        blnValidated status, login name from the user, and the login ID number
        """   
        # Declare Local Variables
        global blnValidated
        blnValidated = bool(False)
        strTable = "TLogins"
        aQueryList = []
        logID = int(0)

        # Get the user login name
        try:
            # Get the database login keys and values
            aQueryList = Queries.Get_All_DB_Values(Queries, strTable)

            # Check if the login name entered by the user is in the database
            for i, item in enumerate(aQueryList):
                if (logName == item[1]):
                    # Set the LoginID and the LoginName to the values held at the element index
                    logID = i + 1
                    blnValidated = True
                    break
                else:
                    blnValidated = False 

        except ValueError as err:
            blnValidated = bool(False)
            messagebox.showwarning(title='ERROR', message='Exception Error because {}'.format(err))

        # Return the Validated status
        return [blnValidated, logName, logID]

    def Check_LoginPassword(logPswrd):
        """ 
        Function Name: Check_LoginPassword
        Function Description: This function checks if hashed password is in the database
        index
        """  
        global blnValidated
        blnValidated = bool(False)
        sqlQuery = ("TLogins", "strPassword")   
        logPswrdIndex = int(0)
        
        # Get the database password values
        aQueryList = Queries.Get_DB_Value(sqlQuery[1], tuple(sqlQuery[0], sqlQuery[1], logPswrd))
        
        try:
            if logPswrd in aQueryList:
                logPswrdIndex = aQueryList.index(logPswrd) + 1
                blnValidated = True
            else:
                blnValidated = False

        except ValueError as err:
            blnValidated = bool(False)
            messagebox.showwarning(title='ERROR', message='Exception Error because {}'.format(err))
            
        return [blnValidated, logPswrd, logPswrdIndex]

    def Validate_Login_Password(strInput):
        """ 
        Function Name: Validate_Login_Password
        Function Description: This function validates the user password has one capital letter, one number,
        and one character, password length, and if all is true, hash the password and return a tuple
        """          
        # Declare Local Variable
        global blnValidated
        blnValidated = bool(False)
        pswrdReturnList = []

        # Validate the string password holds the correct parameters for character authentication
        # Try and Except Validation of all required characters of string
        try:
            # Validate the password length
            blnValidated = BaseFunctions.Validate_Password_Length(strInput)
                                # Check if the input is valid
            if (blnValidated is True):
                # Check if the password contains a capital letter
                blnValidated = BaseFunctions.Validate_CapitalChar(strInput)

                # Check if the input is valid
                if (blnValidated is True):
                    # Check if the password contains any of the three categories of special characters
                    blnValidated = BaseFunctions.Validate_Symbol_Character(strInput)

                    # Check if the input is valid
                    if (blnValidated is True):
                        # Check if the password has a number character
                        blnValidated = BaseFunctions.Validate_NumberChar(strInput)

                        # Check if the input is valid
                        if (blnValidated is True):
                            # Hash the password
                            strHashOutput = BaseFunctions.Hash_Password(strInput)

                            # Check if the password is correct 
                            pswrdReturnList = Queries.Get_All_DB_Values(Queries, "TLogins")
                            for i in pswrdReturnList:
                                if strHashOutput == i[2]:
                                    blnValidated = True
                                    break
                                else:                                      
                                    blnValidated = False                   
                        else:
                            messagebox.showwarning(title='ERROR', message='The password must contain at least one number. \n Please try again.')     
                            blnValidated = False
                    else:
                        messagebox.showwarning(title='ERROR', message='The password must contain at least one special character. \n Please try again.')         
                        blnValidated = False           
                else:
                    messagebox.showwarning(title='ERROR', message='The password must contain at least one capital letter. \n Please try again.') 
                    blnValidated = False
            else:
                messagebox.showwarning(title='ERROR', message='The password must be a minimum of four characters in length. \n Please try again.') 
                blnValidated = False

        except ValueError:
            # Set value to zero
            blnValidated = bool(False)

        return [blnValidated, strInput]
                
class UserLogins(LoginName):
    """
    Class Name: UserLogin
    Class Description: This class takes the InspectorID, and LoginID from classes LoginName.
    This holds the UserLoginID and the strPassword input from the user. 
    """
    # Create class variable shared amongst all UserLogins methods
    aintUserLoginID = []  
    aCurrentUserLogin = []
        
    # Inheritance for all user logins and passwords. Instantiates the base class
    def __init__(self, intUserLoginID, intInspectorID, intLoginID):
        # Inherits the child class with all the necessary objects
        super().__init__(intInspectorID, intLoginID)
        self.intUserLoginID = intUserLoginID

    # Property decorator object get function to access private intUserLoginID
    @property
    def intUserLoginID(self):
        return self._intUserLoginID
    
    # setter method 
    @intUserLoginID.setter 
    def intUserLoginID(self, intUserLoginID): 
        # Return true if specified object is of int type
        if not isinstance(intUserLoginID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intUserLoginID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intUserLoginID = intUserLoginID

    def Append_UserLoginIDList(self, intObject):
        """ 
        Function Name: Append_LoginIDList
        Function Description: This function appends objects to the User Login ID list
        """    
        self.aintUserLoginID.append(intObject)

    def Remove_UserLoginIDList(self, intObject):
        """ 
        Function Name: Remove_LoginIDList
        Function Description: This function removes objects in the User Login ID list
        """    
        self.aintUserLoginID.remove(intObject)

    def Get_UserLoginIDList_Obj(self):
        """ 
        Function Name: Get_LoginIDList_Obj
        Function Description: This function gets all the objects in the User Login ID list
        """    
        return self.aintUserLoginID

    def Append_CurrentUserLoginList(self, intObject):
        """ 
        Function Name: Append_CurrentUserLoginList
        Function Description: This function appends objects to the Current User Login list
        """    
        self.aCurrentUserLogin.append(intObject)

    def Remove_CurrentUserLoginList(self, intObject):
        """ 
        Function Name: Remove_CurrentUserLoginList
        Function Description: This function removes objects in the Current User Login list
        """    
        self.aCurrentUserLogin.remove(intObject)

    def Get_CurrentUserLoginList_Obj(self):
        """ 
        Function Name: Get_CurrentUserLoginList_Obj
        Function Description: This function gets all the objects in the Current User Login list
        """    
        return self.aCurrentUserLogin    

    def Get_UserLogin_Data(self):
        """ 
        Function Name: Get_UserLogin_Data
        Function Description: This function gets all the objects in the User Login table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TUserLogins"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the housing Data List
        for i in range(len(QueryResultList)):
            UserLogins.Append_UserLoginIDList(self, QueryResultList[i][0])
                            
    def Add_NewUserLogin_Query(self):
        """ 
        Function Name: Add_NewUserLogin_Query
        Function Description: This function updates the database with all of the new UserLoginNames objects executing
        the stored procedure uspAddNewUserLogin
        """    
        # Create the sql query string
        sqlTableCol = ("intUserLoginID", "intInspectorID", "intLoginID") 
        sqlTableName = ("TUserLogins")

        # Get the max primary key
        self.intUserLoginID = Queries.Get_MaxPrimaryKeys(Queries, sqlTableName, sqlTableCol[0])
        
        # Load the values 
        sqlTableValues = (self.intUserLoginID, self.intInspectorID, self.intLoginID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues) 

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams) 

    def Update_UserLoginCred_Query(self):
        """ 
        Function Name: Update_UserLoginCred_Query
        Function Description: This function updates the database with all of the new User Login objects executing
        the stored procedure uspAddNewInspector
        """    
        # Create the sql query string
        sqlTableCol = ("intUserLoginID", "intInspectorID", "intLoginID") 
        sqlTableName = "TUserLogins"   
        sqlTableValues = (self.intUserLoginID, self.intInspectorID, self.intLoginID)   
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], sqlTableValues[0]) 

        # Execute the stored procedure
        Queries.dbExeUSP_UpdateValues(Queries, sqlParams)

        # Clear the attributes
        self.Delete_UserLogin_Data()
        
    def Delete_UserLogin_Data(self):
        """ 
        Function Name: Delete_UserLogin_Data
        Function Description: This function removes all the objects in the User Login class
        """    
        UserLogins.aintUserLoginID = [] 
        
    def Clear_UserLogin_Attributes(self):
        """ 
        Function Name: Clear_UserLogin_Attributes
        Function Description: This function clears the User Login attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intUserLoginID", "intInspectorID", "intLoginID") 
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            

class AdminUsers(LoginName):
    """
    Class Name: AdminUsers
    Class Description: This class takes the InspectorID, and LoginID from classes LoginName.
    This holds the intAdminUserID, intInspectorID, and intLoginID. 
    """
    # Create class variable shared amongst all AdminUser methods
    aintAdminUserID = []  
    aintAdminInspectorID = [] 
    aintAdminLoginID = [] 
        
    # Inheritance for all admin user credentials. Instantiates the base class
    def __init__(self, intAdminUserID, intInspectorID, intLoginID):
        # Inherits the child class with all the necessary objects
        super().__init__(intInspectorID, intLoginID)
        self.intAdminUserID = intAdminUserID

    # Property decorator object get function to access private intAdminUserID
    @property
    def intAdminUserID(self):
        return self._intAdminUserID
    
    # setter method 
    @intAdminUserID.setter 
    def intAdminUserID(self, intAdminUserID): 
        # Return true if specified object is of int type
        if not isinstance(intAdminUserID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intAdminUserID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intAdminUserID = intAdminUserID

    def Append_AdminUserIDList(self, intObject):
        """ 
        Function Name: Append_AdminUserIDList
        Function Description: This function appends objects to the Admin User ID list
        """    
        self.aintAdminUserID.append(intObject)

    def Remove_AdminUserIDList(self, intObject):
        """ 
        Function Name: Remove_AdminUserIDList
        Function Description: This function removes objects in the Admin User ID list
        """    
        self.aintAdminUserID.remove(intObject)

    def Get_AdminUserIDList_Obj(self):
        """ 
        Function Name: Get_AdminUserIDList_Obj
        Function Description: This function gets all the objects in the Admin User ID list
        """    
        return self.aintAdminUserID

    def Append_AdminInspectorIDList(self, intObject):
        """ 
        Function Name: Append_AdminInspectorIDList
        Function Description: This function appends objects to the Admin Inspector ID list
        """    
        self.aintAdminInspectorID.append(intObject)

    def Remove_AdminInspectorIDList(self, intObject):
        """ 
        Function Name: Remove_AdminInspectorIDList
        Function Description: This function removes objects in the Admin Inspector ID list
        """    
        self.aintAdminInspectorID.remove(intObject)

    def Get_AdminInspectorIDList_Obj(self):
        """ 
        Function Name: Get_AdminInspectorIDList_Obj
        Function Description: This function gets all the objects in the Admin Inspector ID list
        """    
        return self.aintAdminInspectorID
    
    def Append_AdminLoginIDList(self, intObject):
        """ 
        Function Name: Append_AdminLoginIDList
        Function Description: This function appends objects to the Admin Login ID list
        """    
        self.aintAdminLoginID.append(intObject)

    def Remove_AdminLoginIDList(self, intObject):
        """ 
        Function Name: Remove_AdminLoginIDList
        Function Description: This function removes objects in the Admin Login ID list
        """    
        self.aintAdminLoginID.remove(intObject)

    def Get_AdminLoginIDList_Obj(self):
        """ 
        Function Name: Get_AdminLoginIDList_Obj
        Function Description: This function gets all the objects in the Admin Login ID list
        """    
        return self.aintAdminLoginID

    def Delete_Admin_Data(self):
        """ 
        Function Name: Delete_Admin_Data
        Function Description: This function removes all the objects in the Admin class
        """    
        AdminUsers.aintAdminUserID = [] 
        AdminUsers.aintAdminInspectorID = []  
        AdminUsers.aintAdminLoginID = []
            
    def Get_AdminUser_Data(self):
        """ 
        Function Name: Get_AdminUser_Data
        Function Description: This function gets all the objects in the Logins table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TAdminUsers"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the housing Data List
        for i in range(len(QueryResultList)):
            AdminUsers.Append_AdminUserIDList(self, QueryResultList[i][0])
            AdminUsers.Append_AdminInspectorIDList(self, (QueryResultList[i][1]))
            AdminUsers.Append_AdminLoginIDList(self, (QueryResultList[i][2]))
                                
    def Add_AdminUser_Query(self):
        """ 
        Function Name: Add_AdminUserIDList_Query
        Function Description: This function updates the database with all of the new AdminUserNames objects executing
        the stored procedure uspAddNewAdminUser
        """    
        # Create the sql query string
        sqlTableCol = ("intAdminUserID", "intInspectorID", "intLoginID") 
        sqlTableName = ("TAdminUsers")

        # Get the max primary key value for the table values
        self.intAdminUserID = Queries.Get_MaxPrimaryKeys(Queries, sqlTableName, sqlTableCol[0])
        
        # Set the parameters
        sqlTableValues = (self.intAdminUserID, self.intInspectorID, self.intLoginID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues) 

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)          
        
                
class InspectionStatus():
    """
    Class Name: InspectionStatus
    Class Description: This class gets and sets all of the Inspection Status attributes. 
    """
    # Create class variable shared amongst all InspectionStatus methods
    aintInspectionStatusID = []
    astrInspectionStatusDesc = []
    
    # Instantiate the following attributes
    def __init__(self, intInspectionStatusID, strInspectionStatusDesc):
        self.intInspectionStatusID = intInspectionStatusID
        self.strInspectionStatusDesc = strInspectionStatusDesc

    # Display the Inspection Status descriptions
    def __str__(self):
        return self.strInspectionStatusDesc
    
    # Property decorator object get function to access private intInspectionStatusID
    @property
    def intInspectionStatusID(self):
        return self._intInspectionStatusID

    # Property decorator object get function to access private strInspectionStatusDesc
    @property
    def strInspectionStatusDesc(self):
        return self._strInspectionStatusDesc
        
    # setter method 
    @intInspectionStatusID.setter 
    def intInspectionStatusID(self, intInspectionStatusID): 
        # Return true if specified object is of int type
        if not isinstance(intInspectionStatusID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intInspectionStatusID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intInspectionStatusID = intInspectionStatusID        

    # setter method 
    @strInspectionStatusDesc.setter 
    def strInspectionStatusDesc(self, strInspectionStatusDesc): 
        # Return true if specified object is of str type
        if not isinstance(strInspectionStatusDesc, str): 
            raise TypeError('Status must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha
        if strInspectionStatusDesc.isspace(): 
            raise ValueError('Status cannot be empty') 
        # Set the attribute to the value if true
        elif strInspectionStatusDesc.isascii():
            self._strInspectionStatusDesc = strInspectionStatusDesc

    def Append_StatusIDList(self, intObject):
        """ 
        Function Name: Append_StatusIDList
        Function Description: This function appends objects to the Inspection Status ID list
        """    
        self.aintInspectionStatusID.append(intObject)

    def Remove_StatusIDList(self, intObject):
        """ 
        Function Name: Remove_StatusIDList
        Function Description: This function removes objects in the Inspection Status ID list
        """    
        self.aintInspectionStatusID.remove(intObject)

    def Get_StatusIDList_Obj(self):
        """ 
        Function Name: Get_StatusIDList_Obj
        Function Description: This function gets all the objects in the Inspection Status ID list
        """    
        return self.aintInspectionStatusID
    
    def Append_StatusDescList(self, strObject):
        """ 
        Function Name: Append_StatusDescList
        Function Description: This function appends objects to the Inspection Status list
        """    
        self.astrInspectionStatusDesc.append(strObject)

    def Remove_StatusDescList(self, strObject):
        """ 
        Function Name: Remove_StatusDescList
        Function Description: This function removes objects in the Inspection Status list
        """    
        self.astrInspectionStatusDesc.remove(strObject)

    def Get_StatusDescList_Obj(self):
        """ 
        Function Name: Get_StatusDescList_Obj
        Function Description: This function gets all the objects in the Inspection Status list
        """    
        return self.astrInspectionStatusDesc   
    
    def Get_InspectionStatus_Data(self):
        """ 
        Function Name: Get_InspectionStatus_Data
        Function Description: This function gets all the objects in the Inspection Status list
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TInspectionStatus"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the housing Data List
        for i in range(len(QueryResultList)):
            InspectionStatus.Append_StatusIDList(self, QueryResultList[i][0])
            InspectionStatus.Append_StatusDescList(self, QueryResultList[i][1])

    def Delete_InspectionStatus_Data(self):
        """ 
        Function Name: Delete_InspectionStatus_Data
        Function Description: This function removes all the objects in the Inspection Status list
        """    
        InspectionStatus.aintInspectionStatusID = []
        InspectionStatus.astrInspectionStatusDesc = []
                    

class InspectionType():
    """
    Class Name: InspectionType
    Class Description: This class gets and sets all of the Inspection Type attributes. 
    """
    # Create class variable shared amongst all Inspection Type methods
    aintInspectionTypeID = []
    astrInspectionTypeDesc = []
    
    # Instantiate the following attributes
    def __init__(self, intInspectionTypeID, strInspectionTypeDesc):
        self.intInspectionTypeID = intInspectionTypeID
        self.strInspectionTypeDesc = strInspectionTypeDesc

    # Display the Inspection Type descriptions
    def __str__(self):
        return self.strInspectionTypeDesc
    
    # Property decorator object get function to access private intInspectionTypeID
    @property
    def intInspectionTypeID(self):
        return self._intInspectionTypeID

    # Property decorator object get function to access private strInspectionTypeDesc
    @property
    def strInspectionTypeDesc(self):
        return self._strInspectionTypeDesc
        
    # setter method 
    @intInspectionTypeID.setter 
    def intInspectionTypeID(self, intInspectionTypeID): 
        # Return true if specified object is of int type
        if not isinstance(intInspectionTypeID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intInspectionTypeID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intInspectionTypeID = intInspectionTypeID        

    # setter method 
    @strInspectionTypeDesc.setter 
    def strInspectionTypeDesc(self, strInspectionTypeDesc): 
        # Return true if specified object is of str type
        if not isinstance(strInspectionTypeDesc, str): 
            raise TypeError('Inspection Type must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha
        if strInspectionTypeDesc.isspace(): 
            raise ValueError('Inspection Type cannot be empty') 
        # Set the attribute to the value if true
        elif strInspectionTypeDesc.isascii():
            self._strInspectionTypeDesc = strInspectionTypeDesc

    def Append_TypeIDList(self, intObject):
        """ 
        Function Name: Append_TypeIDList
        Function Description: This function appends objects to the Inspection Type ID list
        """    
        self.aintInspectionTypeID.append(intObject)

    def Remove_TypeIDList(self, intObject):
        """ 
        Function Name: Remove_TypeIDList
        Function Description: This function removes objects in the Inspection Type ID list
        """    
        self.aintInspectionTypeID.remove(intObject)

    def Get_TypeIDList_Obj(self):
        """ 
        Function Name: Get_TypeIDList_Obj
        Function Description: This function gets all the objects in the Inspection Type ID list
        """    
        return self.aintInspectionTypeID
    
    def Append_TypeDescList(self, strObject):
        """ 
        Function Name: Append_TypeDescList
        Function Description: This function appends objects to the Inspection Type list
        """    
        self.astrInspectionTypeDesc.append(strObject)

    def Remove_TypeDescList(self, strObject):
        """ 
        Function Name: Remove_TypeDescList
        Function Description: This function removes objects in the Inspection Type list
        """    
        self.astrInspectionTypeDesc.remove(strObject)

    def Get_TypeDescList_Obj(self):
        """ 
        Function Name: Get_TypeDescList_Obj
        Function Description: This function gets all the objects in the Inspection Type list
        """    
        return self.astrInspectionTypeDesc   
    
    def Get_InspectionType_Data(self):
        """ 
        Function Name: Load_InspectionStatus_Data
        Function Description: This function gets all the objects in the Inspection Status list
        """    
       # Create the sql query string
        sqlQuery = """SELECT * FROM TInspectionTypes"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the housing Data List
        for i in range(len(QueryResultList)):
            InspectionType.Append_TypeIDList(self, QueryResultList[i][0])
            InspectionType.Append_TypeDescList(self, QueryResultList[i][1])

    def Delete_InspectionStatus_Data(self):
        """ 
        Function Name: Delete_InspectionStatus_Data
        Function Description: This function removes all the objects in the Inspection Status list
        """    
        InspectionType.aintInspectionTypeID = []
        InspectionType.astrInspectionTypeDesc = []
        

class Metallic():
    """
    Class Name: Metallic
    Class Description: This class gets and sets all of the Metallic Inspection attributes. 
    """
    # Create class variable shared amongst all Metallic Inspection methods
    aintMetallicInspectionID = []
    astrMetallicInspectionDesc = []
    
    # Instantiate the following attributes
    def __init__(self, intMetallicInspectionID, strMetallicInspectionDesc):
        self.intMetallicInspectionID = intMetallicInspectionID
        self.strMetallicInspectionDesc = strMetallicInspectionDesc

    # Display the Metallic Inspection descriptions
    def __str__(self):
        return self.strMetallicInspectionDesc
    
    # Property decorator object get function to access private intMetallicInspectionID
    @property
    def intMetallicInspectionID(self):
        return self._intMetallicInspectionID

    # Property decorator object get function to access private strMetallicInspectionDesc
    @property
    def strMetallicInspectionDesc(self):
        return self._strMetallicInspectionDesc
        
    # setter method 
    @intMetallicInspectionID.setter 
    def intMetallicInspectionID(self, intMetallicInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intMetallicInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intMetallicInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intMetallicInspectionID = intMetallicInspectionID        

    # setter method 
    @strMetallicInspectionDesc.setter 
    def strMetallicInspectionDesc(self, strMetallicInspectionDesc): 
        # Return true if specified object is of str type
        if not isinstance(strMetallicInspectionDesc, str): 
            raise TypeError('Metallic Inspection Type must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha
        if strMetallicInspectionDesc.isspace(): 
            raise ValueError('Metallic Inspection Type cannot be empty') 
        # Set the attribute to the value if true
        elif strMetallicInspectionDesc.isascii():
            self._strMetallicInspectionDesc = strMetallicInspectionDesc

    def Append_MetallicIDList(self, intObject):
        """ 
        Function Name: Append_MetallicIDList
        Function Description: This function appends objects to the Metallic Inspection Type ID list
        """    
        self.aintMetallicInspectionID.append(intObject)

    def Remove_MetallicIDList(self, intObject):
        """ 
        Function Name: Remove_MetallicIDList
        Function Description: This function removes objects in the Metallic Inspection Type ID list
        """    
        self.aintMetallicInspectionID.remove(intObject)

    def Get_MetallicIDList_Obj(self):
        """ 
        Function Name: Get_MetallicIDList_Obj
        Function Description: This function gets all the objects in the Metallic Inspection Type ID list
        """    
        return self.aintMetallicInspectionID
    
    def Append_MetallicTypeDescList(self, strObject):
        """ 
        Function Name: Append_MetallicTypeDescList
        Function Description: This function appends objects to the Metallic Inspection Type list
        """    
        self.astrMetallicInspectionDesc.append(strObject)

    def Remove_MetallicTypeDescList(self, strObject):
        """ 
        Function Name: Remove_MetallicTypeDescList
        Function Description: This function removes objects in the Metallic Inspection Type list
        """    
        self.astrMetallicInspectionDesc.remove(strObject)

    def Get_MetallicTypeDescList_Obj(self):
        """ 
        Function Name: Get_MetallicTypeDescList_Obj
        Function Description: This function gets all the objects in the Metallic Inspection Type list
        """    
        return self.astrMetallicInspectionDesc   
    
    def Get_MetallicInspectionType_Data(self):
        """ 
        Function Name: Get_MetallicInspectionType_Data
        Function Description: This function gets all the objects in the Metallic Inspection list
        """    
       # Create the sql query string
        sqlQuery = """SELECT * FROM TMetallicInspections"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the housing Data List
        for i in range(len(QueryResultList)):
            Metallic.Append_MetallicIDList(self, QueryResultList[i][0])
            Metallic.Append_MetallicTypeDescList(self, QueryResultList[i][1])

    def Delete_MetallicInspection_Data(self):
        """ 
        Function Name: Delete_MetallicInspection_Data
        Function Description: This function removes all the objects in the Metallic Inspection Type list
        """    
        Metallic.aintMetallicInspectionID = []
        Metallic.astrMetallicInspectionDesc = []
        

class Textile():
    """
    Class Name: Textile
    Class Description: This class gets and sets all of the Textile Inspection attributes. 
    """
    # Create class variable shared amongst all Textile Inspection methods
    aintTextileInspectionID = []
    astrTextileInspectionDesc = []
    
    # Instantiate the following attributes
    def __init__(self, intTextileInspectionID, strTextileInspectionDesc):
        self.intTextileInspectionID = intTextileInspectionID
        self.strTextileInspectionDesc = strTextileInspectionDesc

    # Display the Textile Inspection descriptions
    def __str__(self):
        return self.strTextileInspectionDesc
    
    # Property decorator object get function to access private intTextileInspectionID
    @property
    def intTextileInspectionID(self):
        return self._intTextileInspectionID

    # Property decorator object get function to access private strTextileInspectionDesc
    @property
    def strTextileInspectionDesc(self):
        return self._strTextileInspectionDesc
        
    # setter method 
    @intTextileInspectionID.setter 
    def intTextileInspectionID(self, intTextileInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intTextileInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intTextileInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intTextileInspectionID = intTextileInspectionID        

    # setter method 
    @strTextileInspectionDesc.setter 
    def strTextileInspectionDesc(self, strTextileInspectionDesc): 
        # Return true if specified object is of str type
        if not isinstance(strTextileInspectionDesc, str): 
            raise TypeError('Metallic Inspection Type must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha
        if strTextileInspectionDesc.isspace(): 
            raise ValueError('Metallic Inspection Type cannot be empty') 
        # Set the attribute to the value if true
        elif strTextileInspectionDesc.isascii():
            self._strTextileInspectionDesc = strTextileInspectionDesc

    def Append_TextileIDList(self, intObject):
        """ 
        Function Name: Append_TextileIDList
        Function Description: This function appends objects to the Textile Inspection Type ID list
        """    
        self.aintTextileInspectionID.append(intObject)

    def Remove_TextileIDList(self, intObject):
        """ 
        Function Name: Remove_TextileIDList
        Function Description: This function removes objects in the Textile Inspection Type ID list
        """    
        self.aintTextileInspectionID.remove(intObject)

    def Get_TextileIDList_Obj(self):
        """ 
        Function Name: Get_TextileIDList_Obj
        Function Description: This function gets all the objects in the Textile Inspection Type ID list
        """    
        return self.aintTextileInspectionID
    
    def Append_TextileTypeDescList(self, strObject):
        """ 
        Function Name: Append_TextileTypeDescList
        Function Description: This function appends objects to the Textile Inspection Type list
        """    
        self.astrTextileInspectionDesc.append(strObject)

    def Remove_TextileTypeDescList(self, strObject):
        """ 
        Function Name: Remove_TextileTypeDescList
        Function Description: This function removes objects in the Textile Inspection Type list
        """    
        self.astrTextileInspectionDesc.remove(strObject)

    def Get_TextileTypeDescList_Obj(self):
        """ 
        Function Name: Get_TextileTypeDescList_Obj
        Function Description: This function gets all the objects in the Textile Inspection Type list
        """    
        return self.astrTextileInspectionDesc   
    
    def Get_TextileInspectionType_Data(self):
        """ 
        Function Name: Get_TextileInspectionType_Data
        Function Description: This function gets all the objects in the Textile Inspection list
        """    
       # Create the sql query string
        sqlQuery = """SELECT * FROM TTextileInspections"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the housing Data List
        for i in range(len(QueryResultList)):
            Textile.Append_TextileIDList(self, QueryResultList[i][0])
            Textile.Append_TextileTypeDescList(self, QueryResultList[i][1])

    def Delete_TextileInspection_Data(self):
        """ 
        Function Name: Delete_TextileInspection_Data
        Function Description: This function removes all the objects in the Textile Inspection Type list
        """    
        Textile.aintTextileInspectionID = []
        Textile.astrTextileInspectionDesc = []
        
                
class Plastic():
    """
    Class Name: Plastic
    Class Description: This class gets and sets all of the Plastic Inspection attributes. 
    """
    # Create class variable shared amongst all Plastic Inspection methods
    aintPlasticInspectionID = []
    astrPlasticInspectionDesc = []
    
    # Instantiate the following attributes
    def __init__(self, intPlasticInspectionID, strPlasticInspectionDesc):
        self.intPlasticInspectionID = intPlasticInspectionID
        self.strPlasticInspectionDesc = strPlasticInspectionDesc

    # Display the Plastic Inspection descriptions
    def __str__(self):
        return self.strPlasticInspectionDesc
    
    # Property decorator object get function to access private intPlasticInspectionID
    @property
    def intPlasticInspectionID(self):
        return self._intPlasticInspectionID

    # Property decorator object get function to access private strPlasticInspectionDesc
    @property
    def strPlasticInspectionDesc(self):
        return self._strPlasticInspectionDesc
        
    # setter method 
    @intPlasticInspectionID.setter 
    def intPlasticInspectionID(self, intPlasticInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intPlasticInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intPlasticInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intPlasticInspectionID = intPlasticInspectionID        

    # setter method 
    @strPlasticInspectionDesc.setter 
    def strPlasticInspectionDesc(self, strPlasticInspectionDesc): 
        # Return true if specified object is of str type
        if not isinstance(strPlasticInspectionDesc, str): 
            raise TypeError('Metallic Inspection Type must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha
        if strPlasticInspectionDesc.isspace(): 
            raise ValueError('Metallic Inspection Type cannot be empty') 
        # Set the attribute to the value if true
        elif strPlasticInspectionDesc.isascii():
            self._strPlasticInspectionDesc = strPlasticInspectionDesc

    def Append_PlasticIDList(self, intObject):
        """ 
        Function Name: Append_PlasticIDList
        Function Description: This function appends objects to the Plastic Inspection Type ID list
        """    
        self.aintPlasticInspectionID.append(intObject)

    def Remove_PlasticIDList(self, intObject):
        """ 
        Function Name: Remove_PlasticIDList
        Function Description: This function removes objects in the Plastic Inspection Type ID list
        """    
        self.aintPlasticInspectionID.remove(intObject)

    def Get_PlasticIDList_Obj(self):
        """ 
        Function Name: Get_PlasticIDList_Obj
        Function Description: This function gets all the objects in the Plastic Inspection Type ID list
        """    
        return self.aintPlasticInspectionID
    
    def Append_PlasticTypeDescList(self, strObject):
        """ 
        Function Name: Append_PlasticTypeDescList
        Function Description: This function appends objects to the Plastic Inspection Type list
        """    
        self.astrPlasticInspectionDesc.append(strObject)

    def Remove_PlasticTypeDescList(self, strObject):
        """ 
        Function Name: Remove_PlasticTypeDescList
        Function Description: This function removes objects in the Plastic Inspection Type list
        """    
        self.astrPlasticInspectionDesc.remove(strObject)

    def Get_PlasticTypeDescList_Obj(self):
        """ 
        Function Name: Get_PlasticTypeDescList_Obj
        Function Description: This function gets all the objects in the Plastic Inspection Type list
        """    
        return self.astrPlasticInspectionDesc   
    
    def Get_PlasticInspectionType_Data(self):
        """ 
        Function Name: Get_PlasticInspectionType_Data
        Function Description: This function gets all the objects in the Plastic Inspection list
        """    
       # Create the sql query string
        sqlQuery = """SELECT * FROM TPlasticInspections"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the housing Data List
        for i in range(len(QueryResultList)):
            Plastic.Append_PlasticIDList(self, QueryResultList[i][0])
            Plastic.Append_PlasticTypeDescList(self, QueryResultList[i][1])

    def Delete_PlasticInspection_Data(self):
        """ 
        Function Name: Delete_PlasticInspection_Data
        Function Description: This function removes all the objects in the Plastic Inspection Type list
        """    
        Plastic.aintPlasticInspectionID = []
        Plastic.astrPlasticInspectionDesc = []
                                
class Carabiner():
    """
    Class Name: Carabiner
    Class Description: This class gets and sets all of the Carabiner attributes. 
    """
    # Create class variable shared amongst all Carabiner methods
    aintCarabinerID = []
    astrCarabinerType = []
        
    # Instantiate the following attributes
    def __init__(self, intCarabinerID, strCarabinerType):
        self.intCarabinerID = intCarabinerID
        self.strCarabinerType = strCarabinerType

    # Property decorator object get function to access private intCarabinerID
    @property
    def intCarabinerID(self):
        return self._intCarabinerID

    # Property decorator object get function to access private strCarabinerType
    @property
    def strCarabinerType(self):
        return self._strCarabinerType
        
    # setter method 
    @intCarabinerID.setter 
    def intCarabinerID(self, intCarabinerID): 
        # Return true if specified object is of int type
        if not isinstance(intCarabinerID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intCarabinerID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intCarabinerID = intCarabinerID 
        
    # setter method 
    @strCarabinerType.setter 
    def strCarabinerType(self, strCarabinerType): 
        # Return true if specified object is of str type
        if not isinstance(strCarabinerType, str): 
            raise TypeError('Carabiner input must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if strCarabinerType.isspace(): 
            raise ValueError('Carabiner input cannot be empty') 
        # Set the attribute to the value if true
        elif strCarabinerType.isascii():
            self._strCarabinerType = strCarabinerType
            # Set the global class bool to true
            Bool_Flag.Set_Carab_Bool_Value_True(Bool_Flag)

    def Append_CarabinerIDList(self, intObject):
        """ 
        Function Name: Append_CarabinerIDList
        Function Description: This function appends objects to the Carabiner ID list
        """    
        self.aintCarabinerID.append(intObject)

    def Remove_CarabinerIDList(self, intObject):
        """ 
        Function Name: Remove_CarabinerIDList
        Function Description: This function removes objects in the Carabiner ID list
        """    
        self.aintCarabinerID.remove(intObject)

    def Get_CarabinerIDList_Obj(self):
        """ 
        Function Name: Get_CarabinerIDList_Obj
        Function Description: This function gets all the objects in the Carabiner ID list
        """    
        return self.aintCarabinerID
    
    def Append_CarabinerTypeList(self, strObject):
        """ 
        Function Name: Append_CarabinerTypeList
        Function Description: This function appends objects to the Carabiner Type list
        """    
        self.astrCarabinerType.append(strObject)

    def Remove_CarabinerTypeList(self, strObject):
        """ 
        Function Name: Remove_CarabinerTypeList
        Function Description: This function removes objects in the Carabiner Type list
        """    
        self.astrCarabinerType.remove(strObject)

    def Get_CarabinerTypeList_Obj(self):
        """ 
        Function Name: Get_CarabinerTypeList_Obj
        Function Description: This function gets all the objects in the Carabiner Type list
        """    
        return self.astrCarabinerType   
                    
    def Get_Carabiner_Data(self):
        """ 
        Function Name: Get_Carabiner_Data
        Function Description: This function gets all the objects in the Carabiner table
        """    
       # Create the sql query string
        sqlQuery = """SELECT * FROM TCarabiners"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the housing Data List
        for i in range(len(QueryResultList)):
            Carabiner.Append_CarabinerIDList(self, QueryResultList[i][0])
            Carabiner.Append_CarabinerTypeList(self, QueryResultList[i][1]) 
            
    def Delete_Carabiner_Data(self):
        """ 
        Function Name: Delete_Carabiner_Data
        Function Description: This function removes all the objects in the Carabiner class
        """    
        Carabiner.aintCarabinerID = []
        Carabiner.astrCarabinerType = []
               
                                
class CarabinerFunction():
    """
    Class Name: CarabinerFunction
    Class Description: This class gets and sets all of the Carabiner Function attributes. 
    """
    # Create class variable shared amongst all Carabiner Function methods
    aintCarabinerFunctionID = []
    astrCarabinerFunctionDesc = []
        
    # Instantiate the following attributes
    def __init__(self, intCarabinerFunctionID, strCarabinerFunctionDesc):
        self.intCarabinerFunctionID = intCarabinerFunctionID
        self.strCarabinerFunctionDesc = strCarabinerFunctionDesc

    # Property decorator object get function to access private intCarabinerFunctionID
    @property
    def intCarabinerFunctionID(self):
        return self._intCarabinerFunctionID

    # Property decorator object get function to access private strCarabinerFunctionDesc
    @property
    def strCarabinerFunctionDesc(self):
        return self._strCarabinerFunctionDesc
        
    # setter method 
    @intCarabinerFunctionID.setter 
    def intCarabinerFunctionID(self, intCarabinerFunctionID): 
        # Return true if specified object is of int type
        if not isinstance(intCarabinerFunctionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intCarabinerFunctionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intCarabinerFunctionID = intCarabinerFunctionID 
        
    # setter method 
    @strCarabinerFunctionDesc.setter 
    def strCarabinerFunctionDesc(self, strCarabinerFunctionDesc): 
        # Return true if specified object is of str type
        if not isinstance(strCarabinerFunctionDesc, str): 
            raise TypeError('Hose Length must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if strCarabinerFunctionDesc.isspace(): 
            raise ValueError('Hose Length cannot be empty') 
        # Set the attribute to the value if true
        elif strCarabinerFunctionDesc.isascii():
            self._strCarabinerFunctionDesc = strCarabinerFunctionDesc

    def Append_CarabinerFunctIDList(self, intObject):
        """ 
        Function Name: Append_CarabinerFunctIDList
        Function Description: This function appends objects to the Carabiner Function ID list
        """    
        self.aintCarabinerFunctionID.append(intObject)

    def Remove_CarabinerFunctIDList(self, intObject):
        """ 
        Function Name: Remove_CarabinerFunctIDList
        Function Description: This function removes objects in the Carabiner Function ID list
        """    
        self.aintCarabinerFunctionID.remove(intObject)

    def Get_CarabinerFunctIDList_Obj(self):
        """ 
        Function Name: Get_CarabinerFunctIDList_Obj
        Function Description: This function gets all the objects in the Carabiner Function ID list
        """    
        return self.aintCarabinerFunctionID
    
    def Append_CarabinerFunctList(self, strObject):
        """ 
        Function Name: Append_CarabinerFunctList
        Function Description: This function appends objects to the Carabiner Function list
        """    
        self.astrCarabinerFunctionDesc.append(strObject)

    def Remove_CarabinerFunctList(self, strObject):
        """ 
        Function Name: Remove_CarabinerFunctList
        Function Description: This function removes objects in the Carabiner Function list
        """    
        self.astrCarabinerFunctionDesc.remove(strObject)

    def Get_CarabinerFunctList_Obj(self):
        """ 
        Function Name: Get_CarabinerFunctList_Obj
        Function Description: This function gets all the objects in the Carabiner Function list
        """    
        return self.astrCarabinerFunctionDesc   

    def Get_CarabinerFunct_Data(self):
        """ 
        Function Name: Get_CarabinerFunct_Data
        Function Description: This function gets all the objects in the Carabiner Functions table
        """    
       # Create the sql query string
        sqlQuery = """SELECT * FROM TCarabinerFunctions"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the housing Data List
        for i in range(len(QueryResultList)):
            CarabinerFunction.Append_CarabinerFunctIDList(self, QueryResultList[i][0])
            CarabinerFunction.Append_CarabinerFunctList(self, QueryResultList[i][1]) 

    def Delete_CarabinerFunct_Data(self):
        """ 
        Function Name: Delete_CarabinerFunct_Data
        Function Description: This function removes all the objects in the Carabiner Function class
        """    
        CarabinerFunction.aintCarabinerFunctionID = []
        CarabinerFunction.astrCarabinerFunctionDesc = []
                    

class CarabVisSelection():
    """
    Class Name: CarabVisSelection
    Class Description: This class gets and sets all of the Carabiner Visual Selections. 
    """
    # Create class variable shared amongst all Carabiner visual methods
    aintCarabVisMetalSelectID = []
    astrCarabVisMetSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intCarabVisMetalSelectID, strCarabVisMetSelect, strCarabVisStatus):
        self.intCarabVisMetalSelectID = intCarabVisMetalSelectID
        self.strCarabVisMetSelect = strCarabVisMetSelect
        self.strCarabVisStatus = strCarabVisStatus

    # Property decorator object get function to access private intCarabVisMetalSelectID
    @property
    def intCarabVisMetalSelectID(self):
        return self._intCarabVisMetalSelectID

    # Property decorator object get function to access private strCarabVisMetSelect
    @property
    def strCarabVisMetSelect(self):
        return self._strCarabVisMetSelect

    # Property decorator object get function to access private strCarabVisStatus
    @property
    def strCarabVisStatus(self):
        return self._strCarabVisStatus
                
    # setter method 
    @intCarabVisMetalSelectID.setter 
    def intCarabVisMetalSelectID(self, intCarabVisMetalSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intCarabVisMetalSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intCarabVisMetalSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intCarabVisMetalSelectID = intCarabVisMetalSelectID 
        
    # setter method 
    @strCarabVisMetSelect.setter 
    def strCarabVisMetSelect(self, strCarabVisMetSelect): 
        # Return true if specified object is of str type
        if not isinstance(strCarabVisMetSelect, str): 
            raise TypeError('Carabiner visual input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strCarabVisMetSelect.isspace(): 
            raise ValueError('Carabiner visual input cannot be empty') 
        # Set the attribute to the value if true
        elif strCarabVisMetSelect.isascii():
            self._strCarabVisMetSelect = strCarabVisMetSelect

    # setter method 
    @strCarabVisStatus.setter 
    def strCarabVisStatus(self, strCarabVisStatus): 
        # Return true if specified object is of str type
        if not isinstance(strCarabVisStatus, str): 
            raise TypeError('Carabiner visual status input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strCarabVisStatus.isspace(): 
            raise ValueError('Carabiner visual status input cannot be empty') 
        # Set the attribute to the value if true
        elif strCarabVisStatus.isascii():
            self._strCarabVisStatus = strCarabVisStatus

    def Append_CarabVisIDList(self, intObject):
        """ 
        Function Name: Append_CarabVisIDList
        Function Description: This function appends objects to the Carabiner Visual Selection ID list
        """    
        self.aintCarabVisMetalSelectID.append(intObject)

    def Remove_CarabVisIDList(self, intObject):
        """ 
        Function Name: Remove_CarabVisIDList
        Function Description: This function removes objects in the Carabiner Visual Selection ID list
        """    
        self.aintCarabVisMetalSelectID.remove(intObject)

    def Get_CarabVisIDList_Obj(self):
        """ 
        Function Name: Get_CarabVisIDList_Obj
        Function Description: This function gets all the objects in the Carabiner Visual Selection ID list
        """    
        return self.aintCarabVisMetalSelectID
    
    def Append_CarabVisSelectList(self, strObject):
        """ 
        Function Name: Append_CarabVisSelectList
        Function Description: This function appends objects to the Carabiner Visual Selection list
        """    
        self.astrCarabVisMetSelect.append(strObject)

    def Remove_CarabVisSelectList(self, strObject):
        """ 
        Function Name: Remove_CarabVisSelectList
        Function Description: This function removes objects in the Carabiner Visual Selection list
        """    
        self.astrCarabVisMetSelect.remove(strObject)

    def Get_CarabVisSelectList_Obj(self):
        """ 
        Function Name: Get_CarabVisSelectList_Obj
        Function Description: This function gets all the objects in the Carabiner Visual Selection list
        """    
        return self.astrCarabVisMetSelect   
                    
    def Delete_CarabVisSelection_Data(self):
        """ 
        Function Name: Delete_CarabVisSelection_Data
        Function Description: This function removes all the objects in the Carabiner Visual Selection class
        """    
        CarabVisSelection.aintCarabVisMetalSelectID = []
        CarabVisSelection.astrCarabVisMetSelect = []

    def Check_CarabVisSelection_Dup(self):
        """ 
        Function Name: Check_CarabVisSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        carabiner visual selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intCarabVisMetalSelectID", "strCarabVisMetSelect")   
        sqlTableName = "TCarabVisMetalSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strCarabVisMetSelect in sqlDupValues[i]:
                self.intCarabVisMetalSelectID = sqlDupValues[i][0]
                self.strCarabVisMetSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag
                                            
    def Add_CarabVisSelection_Query(self):
        """ 
        Function Name: Add_CarabVisSelection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewCarabVisSelection
        """    
        # Create the sql query params
        sqlTableCol = ("intCarabVisMetalSelectID", "strCarabVisMetSelect")   
        sqlTableName = "TCarabVisMetalSelects"
        sqlTableValues = (CarabVisSelection.intCarabVisMetalSelectID, CarabVisSelection.strCarabVisMetSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)                               

    def Clear_CarabVisSel_Attributes(self):
        """ 
        Function Name: Clear_CarabVisSel_Attributes
        Function Description: This function clears the Carabiner Visual Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intCarabVisMetalSelectID", "strCarabVisMetSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None) 
            
                                 
class CarabinerVisualInspect(Carabiner, InspectionType, CarabVisSelection, InspectionStatus):
    """
    Class Name: CarabinerVisualInspect
    Class Description: This class gets and sets all of the Carabiner Visual Inspection attributes. 
    """
    # Create class variable shared amongst all Carabiner Visual Inspection methods
    aintCarabinerVisualID = []
    aCarabVisualCache = []
        
    # Instantiate the following attributes
    def __init__(self, intCarabinerVisualID, intCarabinerID, intInspectionTypeID, intCarabVisMetalSelectID, intInspectionStatusID):
        self.intCarabinerVisualID = intCarabinerVisualID
        # Inherits the child class with all the necessary objects
        Carabiner.__init__(intCarabinerID)
        InspectionType.__init__(intInspectionTypeID)
        CarabVisSelection.__init__(intCarabVisMetalSelectID)
        InspectionStatus.__init__(intInspectionStatusID)
        
    # Property decorator object get function to access private intCarabinerVisualID
    @property
    def intCarabinerVisualID(self):
        return self._intCarabinerVisualID

    # setter method 
    @intCarabinerVisualID.setter 
    def intCarabinerVisualID(self, intCarabinerVisualID): 
        # Return true if specified object is of int type
        if not isinstance(intCarabinerVisualID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Carabiner Visual Inspection ID to value
        if intCarabinerVisualID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intCarabinerVisualID = intCarabinerVisualID 

    def Append_CarabinerVisualIDList(self, intObject):
        """ 
        Function Name: Append_CarabinerVisualIDList
        Function Description: This function appends objects to the Carabiner Visual Inspection ID list
        """    
        self.aintCarabinerVisualID.append(intObject)

    def Remove_CarabinerVisualIDList(self, intObject):
        """ 
        Function Name: Remove_CarabinerVisualIDList
        Function Description: This function removes objects in the Carabiner Visual Inspection ID list
        """    
        self.aintCarabinerVisualID.remove(intObject)

    def Get_CarabinerVisualIDList_Obj(self):
        """ 
        Function Name: Get_CarabinerVisualIDList_Obj
        Function Description: This function gets all the objects in the Carabiner Visual Inspection ID list
        """    
        return self.aintCarabinerVisualID
                
    def Delete_CarabinerVisualInspect_Data(self):
        """ 
        Function Name: Delete_CarabinerVisualInspect_Data
        Function Description: This function removes all the objects in the Carabiner Visual Inspection ID class
        """    
        CarabinerVisualInspect.aintCarabinerVisualID = []
        CarabinerVisualInspect.aCarabVisualCache = []

    def Set_CarabinerVisualInspect_Data(self):
        """ 
        Function Name: Set_CarabinerVisualInspect_Data
        Function Description: This function sets all the objects in the Carabiner Visual Inspection class
        """    
        self.intCarabinerVisualID = CarabinerVisualInspect.aCarabVisualCache[0]
        self.intCarabinerID = CarabinerVisualInspect.aCarabVisualCache[1]
        self.intInspectionTypeID = CarabinerVisualInspect.aCarabVisualCache[2]
        self.intCarabVisMetalSelectID = CarabinerVisualInspect.aCarabVisualCache[3]
        self.intInspectionStatusID = CarabinerVisualInspect.aCarabVisualCache[4]
        
    def Add_CarabinerVisualInspect_Query(self):
        """ 
        Function Name: Add_CarabinerVisualInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewCarabinerVisualInspection
        """    
        # Set the class variables before dumping the data to the database
        CarabinerVisualInspect.Set_CarabinerVisualInspect_Data(self)
        
        # Create the sql query string       
        sqlTableCol = ("intCarabinerVisualID", "intCarabinerID", "intInspectionTypeID", "intCarabVisMetalSelectID", "intInspectionStatusID")     
        sqlTableName = "TCarabinerVisualInspections"
        sqlTableValues = (self.intCarabinerVisualID, self.intCarabinerID, self.intInspectionTypeID, self.intCarabVisMetalSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)           

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)         
                                
    def Clear_CarabVisInspect_Attributes(self):
        """ 
        Function Name: Clear_CarabVisInspect_Attributes
        Function Description: This function clears the Carabiner Visual Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intCarabinerVisualID", "intCarabinerID", "intInspectionTypeID", "intCarabVisMetalSelectID", "intInspectionStatusID")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            
            
class CarabPhysSelection():
    """
    Class Name: CarabPhysSelection
    Class Description: This class gets and sets all of the Carabiner Physical Selections. 
    """
    # Create class variable shared amongst all Carabiner physical methods
    aintCarabPhysMetalSelectID = []
    astrCarabPhysMetSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intCarabPhysMetalSelectID, strCarabPhysMetSelect, strCarabPhysStatus):
        self.intCarabPhysMetalSelectID = intCarabPhysMetalSelectID
        self.strCarabPhysMetSelect = strCarabPhysMetSelect
        self.strCarabPhysStatus = strCarabPhysStatus

    # Property decorator object get function to access private intCarabPhysMetalSelectID
    @property
    def intCarabPhysMetalSelectID(self):
        return self._intCarabPhysMetalSelectID

    # Property decorator object get function to access private strCarabPhysMetSelect
    @property
    def strCarabPhysMetSelect(self):
        return self._strCarabPhysMetSelect
        
    # Property decorator object get function to access private strCarabPhysStatus
    @property
    def strCarabPhysStatus(self):
        return self._strCarabPhysStatus
                
    # setter method 
    @intCarabPhysMetalSelectID.setter 
    def intCarabPhysMetalSelectID(self, intCarabPhysMetalSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intCarabPhysMetalSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intCarabPhysMetalSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intCarabPhysMetalSelectID = intCarabPhysMetalSelectID 
        
    # setter method 
    @strCarabPhysMetSelect.setter 
    def strCarabPhysMetSelect(self, strCarabPhysMetSelect): 
        # Return true if specified object is of str type
        if not isinstance(strCarabPhysMetSelect, str): 
            raise TypeError('Carabiner physical input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strCarabPhysMetSelect.isspace(): 
            raise ValueError('Carabiner physical input cannot be empty') 
        # Set the attribute to the value if true
        elif strCarabPhysMetSelect.isascii():
            self._strCarabPhysMetSelect = strCarabPhysMetSelect

    # setter method 
    @strCarabPhysStatus.setter 
    def strCarabPhysStatus(self, strCarabPhysStatus): 
        # Return true if specified object is of str type
        if not isinstance(strCarabPhysStatus, str): 
            raise TypeError('Carabiner physical status input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strCarabPhysStatus.isspace(): 
            raise ValueError('Carabiner physical status input cannot be empty') 
        # Set the attribute to the value if true
        elif strCarabPhysStatus.isascii():
            self._strCarabPhysStatus = strCarabPhysStatus

    def Append_CarabPhysIDList(self, intObject):
        """ 
        Function Name: Append_CarabPhysIDList
        Function Description: This function appends objects to the Carabiner Physical Selection ID list
        """    
        self.aintCarabPhysMetalSelectID.append(intObject)

    def Remove_CarabPhysIDList(self, intObject):
        """ 
        Function Name: Remove_CarabPhysIDList
        Function Description: This function removes objects in the Carabiner Physical Selection ID list
        """    
        self.aintCarabPhysMetalSelectID.remove(intObject)

    def Get_CarabPhysIDList_Obj(self):
        """ 
        Function Name: Get_CarabPhysIDList_Obj
        Function Description: This function gets all the objects in the Carabiner Physical Selection ID list
        """    
        return self.aintCarabPhysMetalSelectID
    
    def Append_CarabPhysSelectList(self, strObject):
        """ 
        Function Name: Append_CarabPhysSelectList
        Function Description: This function appends objects to the Carabiner Physical Selection list
        """    
        self.astrCarabPhysMetSelect.append(strObject)

    def Remove_CarabPhysSelectList(self, strObject):
        """ 
        Function Name: Remove_CarabPhysSelectList
        Function Description: This function removes objects in the Carabiner Physical Selection list
        """    
        self.astrCarabPhysMetSelect.remove(strObject)

    def Get_CarabPhysSelectList_Obj(self):
        """ 
        Function Name: Get_CarabPhysSelectList_Obj
        Function Description: This function gets all the objects in the Carabiner Physical Selection list
        """    
        return self.astrCarabPhysMetSelect   
                    
    def Delete_CarabPhysSelection_Data(self):
        """ 
        Function Name: Delete_CarabPhysSelection_Data
        Function Description: This function removes all the objects in the Carabiner Physical Selection class
        """    
        CarabPhysSelection.aintCarabPhysMetalSelectID = []
        CarabPhysSelection.astrCarabPhysMetSelect = []

    def Check_CarabPhysSelection_Dup(self):
        """ 
        Function Name: Check_CarabPhysSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        carabiner physical selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intCarabPhysMetalSelectID", "strCarabPhysMetSelect")   
        sqlTableName = "TCarabPhysMetalSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strCarabPhysMetSelect in sqlDupValues[i]:
                self.intCarabPhysMetalSelectID = sqlDupValues[i][0]
                self.strCarabPhysMetSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag
            
    def Add_CarabPhysSelection_Query(self):
        """ 
        Function Name: Add_CarabPhysSelection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewCarabPhysSelection
        """    
        # Create the sql query string
        sqlTableCol = ("intCarabPhysMetalSelectID", "strCarabPhysMetSelect")   
        sqlTableName = "TCarabPhysMetalSelects"
        sqlTableValues = (CarabPhysSelection.intCarabPhysMetalSelectID, CarabPhysSelection.strCarabPhysMetSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams) 
        
    def Clear_CarabPhysSel_Attributes(self):
        """ 
        Function Name: Clear_CarabPhysSel_Attributes
        Function Description: This function clears the Carabiner Physical Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intCarabPhysMetalSelectID", "strCarabPhysMetSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            
                    
class CarabinerPhysicalInspect(Carabiner, InspectionType, CarabPhysSelection, InspectionStatus):
    """
    Class Name: CarabinerPhysicalInspect
    Class Description: This class gets and sets all of the Carabiner Physical Inspection  attributes. 
    """
    # Create class variable shared amongst all Carabiner Physical Inspection methods
    aintCarabinerPhysicalID = []
    aCarabPhysicalCache = []
        
    # Instantiate the following attributes
    def __init__(self, intCarabinerPhysicalID, intCarabinerID, intInspectionTypeID, intCarabPhysMetalSelectID, intInspectionStatusID):
        self.intCarabinerPhysicalID = intCarabinerPhysicalID
        # Inherits the child class with all the necessary objects
        Carabiner.__init__(intCarabinerID)
        InspectionType.__init__(intInspectionTypeID)
        CarabPhysSelection.__init__(intCarabPhysMetalSelectID)
        InspectionStatus.__init__(intInspectionStatusID)
        
    # Property decorator object get function to access private intCarabinerPhysicalID
    @property
    def intCarabinerPhysicalID(self):
        return self._intCarabinerPhysicalID

    # setter method 
    @intCarabinerPhysicalID.setter 
    def intCarabinerPhysicalID(self, intCarabinerPhysicalID): 
        # Return true if specified object is of int type
        if not isinstance(intCarabinerPhysicalID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Carabiner Physical Inspection ID to value
        if intCarabinerPhysicalID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intCarabinerPhysicalID = intCarabinerPhysicalID 

    def Append_CarabinerPhysicalIDList(self, intObject):
        """ 
        Function Name: Append_CarabinerPhysicalIDList
        Function Description: This function appends objects to the Carabiner Physical Inspection ID list
        """    
        self.aintCarabinerPhysicalID.append(intObject)

    def Remove_CarabinerPhysicalIDList(self, intObject):
        """ 
        Function Name: Remove_CarabinerPhysicalIDList
        Function Description: This function removes objects in the Carabiner Physical Inspection ID list
        """    
        self.aintCarabinerPhysicalID.remove(intObject)

    def Get_CarabinerPhysicalIDList_Obj(self):
        """ 
        Function Name: Get_CarabinerPhysicalIDList_Obj
        Function Description: This function gets all the objects in the Carabiner Physical Inspection ID list
        """    
        return self.aintCarabinerPhysicalID
                
    def Delete_CarabinerPhysicalInspect_Data(self):
        """ 
        Function Name: Delete_CarabinerPhysicalInspect_Data
        Function Description: This function removes all the objects in the Carabiner Physical Inspection ID class
        """    
        CarabinerPhysicalInspect.aintCarabinerPhysicalID = []
        CarabinerPhysicalInspect.aCarabPhysicalCache = []

    def Set_CarabinerPhysicalInspect_Data(self):
        """ 
        Function Name: Set_CarabinerVisualInspect_Data
        Function Description: This function sets all the objects in the Carabiner Physical Inspection class
        """    
        self.intCarabinerPhysicalID = CarabinerPhysicalInspect.aCarabPhysicalCache[0]
        self.intCarabinerID = CarabinerPhysicalInspect.aCarabPhysicalCache[1]
        self.intInspectionTypeID = CarabinerPhysicalInspect.aCarabPhysicalCache[2]
        self.intCarabPhysMetalSelectID = CarabinerPhysicalInspect.aCarabPhysicalCache[3]
        self.intInspectionStatusID = CarabinerPhysicalInspect.aCarabPhysicalCache[4]
                
    def Add_CarabinerPhysicalInspect_Query(self):
        """ 
        Function Name: Add_CarabinerPhysicalInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewCarabinerPhysicalInspection
        """    
        # Set the class variables before dumping the data to the database
        CarabinerPhysicalInspect.Set_CarabinerPhysicalInspect_Data(self)
                
        # Create the sql query string
        sqlTableCol = ("intCarabinerPhysicalID", "intCarabinerID", "intInspectionTypeID", "intCarabPhysMetalSelectID", "intInspectionStatusID")     
        sqlTableName = "TCarabinerPhysicalInspections"
        sqlTableValues = (self.intCarabinerPhysicalID, self.intCarabinerID, self.intInspectionTypeID, self.intCarabPhysMetalSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)           

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)       

    def Clear_CarabPhysInspect_Attributes(self):
        """ 
        Function Name: Clear_CarabPhysInspect_Attributes
        Function Description: This function clears the Carabiner Physical Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intCarabinerPhysicalID", "intCarabinerID", "intInspectionTypeID", "intCarabPhysMetalSelectID", "intInspectionStatusID")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                    

class CarabFunctSelection():
    """
    Class Name: CarabFunctSelection
    Class Description: This class gets and sets all of the Carabiner Function Selections. 
    """
    # Create class variable shared amongst all Carabiner Function methods
    aintCarabFunctSelectID = []
    astrCarabFunctSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intCarabFunctSelectID, strCarabFunctSelect, strCarabFunctStatus):
        self.intCarabFunctSelectID = intCarabFunctSelectID
        self.strCarabFunctSelect = strCarabFunctSelect
        self.strCarabFunctStatus = strCarabFunctStatus

    # Property decorator object get function to access private intCarabFunctSelectID
    @property
    def intCarabFunctSelectID(self):
        return self._intCarabFunctSelectID

    # Property decorator object get function to access private strCarabFunctSelect
    @property
    def strCarabFunctSelect(self):
        return self._strCarabFunctSelect

    # Property decorator object get function to access private strCarabFunctStatus
    @property
    def strCarabFunctStatus(self):
        return self._strCarabFunctStatus

    # setter method 
    @intCarabFunctSelectID.setter 
    def intCarabFunctSelectID(self, intCarabFunctSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intCarabFunctSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intCarabFunctSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intCarabFunctSelectID = intCarabFunctSelectID 
        
    # setter method 
    @strCarabFunctSelect.setter 
    def strCarabFunctSelect(self, strCarabFunctSelect): 
        # Return true if specified object is of str type
        if not isinstance(strCarabFunctSelect, str): 
            raise TypeError('Carabiner function input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strCarabFunctSelect.isspace(): 
            raise ValueError('Carabiner function input cannot be empty') 
        # Set the attribute to the value if true
        elif strCarabFunctSelect.isascii():
            self._strCarabFunctSelect = strCarabFunctSelect

    # setter method 
    @strCarabFunctStatus.setter 
    def strCarabFunctStatus(self, strCarabFunctStatus): 
        # Return true if specified object is of str type
        if not isinstance(strCarabFunctStatus, str): 
            raise TypeError('Carabiner function status input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strCarabFunctStatus.isspace(): 
            raise ValueError('Carabiner function status input cannot be empty') 
        # Set the attribute to the value if true
        elif strCarabFunctStatus.isascii():
            self._strCarabFunctStatus = strCarabFunctStatus

    def Append_CarabFunctIDList(self, intObject):
        """ 
        Function Name: Append_CarabFunctIDList
        Function Description: This function appends objects to the Carabiner Function Selection ID list
        """    
        self.aintCarabFunctSelectID.append(intObject)

    def Remove_CarabFunctIDList(self, intObject):
        """ 
        Function Name: Remove_CarabFunctIDList
        Function Description: This function removes objects in the Carabiner Function Selection ID list
        """    
        self.aintCarabFunctSelectID.remove(intObject)

    def Get_CarabFunctIDList_Obj(self):
        """ 
        Function Name: Get_CarabFunctIDList_Obj
        Function Description: This function gets all the objects in the Carabiner Function Selection ID list
        """    
        return self.aintCarabFunctSelectID
    
    def Append_CarabFunctSelectList(self, strObject):
        """ 
        Function Name: Append_CarabFunctSelectList
        Function Description: This function appends objects to the Carabiner Function Selection list
        """    
        self.astrCarabFunctSelect.append(strObject)

    def Remove_CarabFunctSelectList(self, strObject):
        """ 
        Function Name: Remove_CarabFunctSelectList
        Function Description: This function removes objects in the Carabiner Function Selection list
        """    
        self.astrCarabFunctSelect.remove(strObject)

    def Get_CarabFunctSelectList_Obj(self):
        """ 
        Function Name: Get_CarabFunctSelectList_Obj
        Function Description: This function gets all the objects in the Carabiner Function Selection list
        """    
        return self.astrCarabFunctSelect   
                    
    def Delete_CarabFunctSelection_Data(self):
        """ 
        Function Name: Delete_CarabFunctSelection_Data
        Function Description: This function removes all the objects in the Carabiner Function Selection class
        """    
        CarabFunctSelection.aintCarabFunctSelectID = []
        CarabFunctSelection.astrCarabFunctSelect = []

    def Check_CarabFunctSelection_Dup(self):
        """ 
        Function Name: Check_CarabFunctSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        carabiner function selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intCarabFunctSelectID", "strCarabFunctSelect")   
        sqlTableName = "TCarabFunctSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strCarabFunctSelect in sqlDupValues[i]:
                self.intCarabFunctSelectID = sqlDupValues[i][0]
                self.strCarabFunctSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag
            
    def Add_CarabFunctSelection_Query(self):
        """ 
        Function Name: Add_CarabFunctSelection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewCarabFunctSelection
        """    
        # Create the sql query string
        sqlTableCol = ("intCarabFunctSelectID", "strCarabFunctSelect")   
        sqlTableName = "TCarabFunctSelects"
        sqlTableValues = (CarabFunctSelection.intCarabFunctSelectID, CarabFunctSelection.strCarabFunctSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)                            

    def Clear_CarabFuncSel_Attributes(self):
        """ 
        Function Name: Clear_CarabFuncSel_Attributes
        Function Description: This function clears the Carabiner Function Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intCarabFunctSelectID", "strCarabFunctSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None) 
                    
                
class CarabinerFunctionInspect(Carabiner, InspectionType, CarabFunctSelection, InspectionStatus):
    """
    Class Name: CarabinerFunctionInspect
    Class Description: This class gets and sets all of the Carabiner Function Inspection  attributes. 
    """
    # Create class variable shared amongst all Carabiner Function Inspection methods
    aintCarabinerFunctionInspectID = []
    aCarabFunctCache = []
        
    # Instantiate the following attributes
    def __init__(self, intCarabinerFunctionInspectID, intCarabinerID, intInspectionTypeID, intCarabFunctSelectID, intInspectionStatusID):
        self.intCarabinerFunctionInspectID = intCarabinerFunctionInspectID
        # Inherits the child class with all the necessary objects
        Carabiner.__init__(intCarabinerID)
        InspectionType.__init__(intInspectionTypeID)
        CarabFunctSelection.__init__(intCarabFunctSelectID)
        InspectionStatus.__init__(intInspectionStatusID)

    # Property decorator object get function to access private intCarabinerFunctionInspectID
    @property
    def intCarabinerFunctionInspectID(self):
        return self._intCarabinerFunctionInspectID

    # setter method 
    @intCarabinerFunctionInspectID.setter 
    def intCarabinerFunctionInspectID(self, intCarabinerFunctionInspectID): 
        # Return true if specified object is of int type
        if not isinstance(intCarabinerFunctionInspectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Carabiner Function Inspection ID to value
        if intCarabinerFunctionInspectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intCarabinerFunctionInspectID = intCarabinerFunctionInspectID 

    def Append_CarabinerFunctIDList(self, intObject):
        """ 
        Function Name: Append_CarabinerFunctIDList
        Function Description: This function appends objects to the Carabiner Function Inspection ID list
        """    
        self.aintCarabinerFunctionInspectID.append(intObject)

    def Remove_CarabinerFunctIDList(self, intObject):
        """ 
        Function Name: Remove_CarabinerFunctIDList
        Function Description: This function removes objects in the Carabiner Function Inspection ID list
        """    
        self.aintCarabinerFunctionInspectID.remove(intObject)

    def Get_CarabinerFunctIDList_Obj(self):
        """ 
        Function Name: Get_CarabinerFunctIDList_Obj
        Function Description: This function gets all the objects in the Carabiner Function Inspection ID list
        """    
        return self.aintCarabinerFunctionInspectID
                
    def Delete_CarabinerFunctInspect_Data(self):
        """ 
        Function Name: Delete_CarabinerFunctInspect_Data
        Function Description: This function removes all the objects in the Carabiner Function Inspection ID class
        """    
        CarabinerFunctionInspect.aintCarabinerFunctionInspectID = []
        CarabinerFunctionInspect.aCarabFunctCache = []

    def Set_CarabinerFunctInspect_Data(self):
        """ 
        Function Name: Set_CarabinerFunctInspect_Data
        Function Description: This function sets all the objects in the Carabiner Function Inspection class
        """    
        self.intCarabinerFunctionInspectID = CarabinerFunctionInspect.aCarabFunctCache[0]
        self.intCarabinerID = CarabinerFunctionInspect.aCarabFunctCache[1]
        self.intInspectionTypeID = CarabinerFunctionInspect.aCarabFunctCache[2]
        self.intCarabFunctSelectID = CarabinerFunctionInspect.aCarabFunctCache[3]
        self.intInspectionStatusID = CarabinerFunctionInspect.aCarabFunctCache[4]
                
    def Add_CarabinerFunctInspect_Query(self):
        """ 
        Function Name: Add_CarabinerFunctInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewCarabinerFunctionInspection
        """    
        # Set the class variables before dumping the data to the database
        CarabinerFunctionInspect.Set_CarabinerFunctInspect_Data(self)
                
        # Create the sql query string
        sqlTableCol = ("intCarabinerFunctionInspectID", "intCarabinerID", "intInspectionTypeID", "intCarabFunctSelectID", "intInspectionStatusID")     
        sqlTableName = "TCarabinerFunctionInspections"
        sqlTableValues = (self.intCarabinerFunctionInspectID, self.intCarabinerID, self.intInspectionTypeID, self.intCarabFunctSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)           

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Clear_CarabFuncInspect_Attributes(self):
        """ 
        Function Name: Clear_CarabFuncInspect_Attributes
        Function Description: This function clears the Carabiner Function Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intCarabinerFunctionInspectID", "intCarabinerID", "intInspectionTypeID", "intCarabFunctSelectID", "intInspectionStatusID")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            
                                                                                                    
class StandardCarabinerInspect(CarabinerVisualInspect, CarabinerPhysicalInspect, CarabinerFunctionInspect):
    """
    Class Name: StandardCarabinerInspect
    Class Description: This class gets and sets all of the Standard Carabiner Inspection attributes. 
    Pass in the Carabiner Visual, Physical, and Function Inspection Status classes. 
    """
    # Create class variable shared amongst all StandardCarabinerInspect methods
    aintStandardCarabinerInspectionID = []
    aStandardCarabInsCache = []
        
    # Instantiate the following attributes
    def __init__(self, intStandardCarabinerInspectionID, intCarabinerVisualID, intCarabinerPhysicalID, intCarabinerFunctionInspectID):
        self.intStandardCarabinerInspectionID = intStandardCarabinerInspectionID
        CarabinerVisualInspect.__init__(self, intCarabinerVisualID)
        CarabinerPhysicalInspect.__init__(self, intCarabinerPhysicalID)
        CarabinerFunctionInspect.__init__(self, intCarabinerFunctionInspectID)
        
    # Property decorator object get function to access private intStandardCarabinerInspectionID
    @property
    def intStandardCarabinerInspectionID(self):
        return self._intStandardCarabinerInspectionID

    # setter method 
    @intStandardCarabinerInspectionID.setter 
    def intStandardCarabinerInspectionID(self, intStandardCarabinerInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intStandardCarabinerInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intStandardCarabinerInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intStandardCarabinerInspectionID = intStandardCarabinerInspectionID 
        
    def Append_StandCarabinerInspectIDList(self, intObject):
        """ 
        Function Name: Append_StandCarabinerInspectIDList
        Function Description: This function appends objects to the Standard Carabiner Inspection ID list
        """    
        self.aintStandardCarabinerInspectionID.append(intObject)

    def Remove_StandCarabinerInspectIDList(self, intObject):
        """ 
        Function Name: Remove_StandCarabinerInspectIDList
        Function Description: This function removes objects in the Standard Carabiner Inspection ID list
        """    
        self.aintStandardCarabinerInspectionID.remove(intObject)

    def Get_StandCarabinerInspectIDList_Obj(self):
        """ 
        Function Name: Get_StandCarabinerInspectIDList_Obj
        Function Description: This function gets all the objects in the Standard Carabiner Inspection ID list
        """    
        return self.aintStandardCarabinerInspectionID

    def Add_StandCarabinerInspect_Query(self):
        """ 
        Function Name: Add_StandCarabinerInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewStandardCarabinerInspection
        """    
        # Create the sql query string
        sqlTableNames = ("TStandardCarabinerInspections")
        sqlTableCol = ("intStandardCarabinerInspectionID", "intCarabinerVisualID", "intCarabinerPhysicalID", 
                       "intCarabinerFunctionInspectID", "intInspectionStatusID")
        # Set the primary key values from the cached array object
        aPrimKeyValues = [item for item in StandardCarabinerInspect.aStandardCarabInsCache]

        # Get the visual, physical, and functional status IDs
        VisStatusID = InspectionStatus.astrInspectionStatusDesc.index(CarabVisSelection.strCarabVisStatus) + 1
        PhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(CarabPhysSelection.strCarabPhysStatus) + 1
        FunctStatusID = InspectionStatus.astrInspectionStatusDesc.index(CarabFunctSelection.strCarabFunctStatus) + 1
        aInsStatusID = [VisStatusID, PhysStatusID, FunctStatusID]

        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(aInsStatusID)
        
        # Append the AutoBelay Status array 
        AutoBelayInspect.aAutoBelayInspectStatus.append(intOverallStatus)
         
        # Append the primary key list with the new over status ID
        aPrimKeyValues.append(intOverallStatus)                      
        
        # Set the parameters
        sqlParams = (sqlTableNames, sqlTableCol, tuple(aPrimKeyValues))

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Delete_StandCarabInspect_Data(self):
        """ 
        Function Name: Delete_StandCarabInspect_Data
        Function Description: This function removes all the objects in the Standard Carabiner Inspection class
        """    
        StandardCarabinerInspect.aintStandardCarabinerInspectionID = []
        StandardCarabinerInspect.aStandardCarabInsCache = []

    def Clear_CarabStandardInspect_Attributes(self):
        """ 
        Function Name: Clear_CarabStandardInspect_Attributes
        Function Description: This function clears the Carabiner Standard Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intStandardCarabinerInspectionID", "intCarabinerVisualID", "intCarabinerPhysicalID", 
                       "intCarabinerFunctionInspectID", "intInspectionStatusID")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)

    def Reset_Carabiner_Data(self):
        """ 
        Function Name: Reset_Carabiner_Data
        Function Description: This function clears the Carabiner data attributes 
        """  
        # Clear the class attributes
        CarabVisSelection.Clear_CarabVisSel_Attributes(self)
        CarabPhysSelection.Clear_CarabPhysSel_Attributes(self)
        CarabFunctSelection.Clear_CarabFuncSel_Attributes(self)
        CarabinerVisualInspect.Clear_CarabVisInspect_Attributes(self)
        CarabinerPhysicalInspect.Clear_CarabPhysInspect_Attributes(self)
        CarabinerFunctionInspect.Clear_CarabFuncInspect_Attributes(self)
        StandardCarabinerInspect.Clear_CarabStandardInspect_Attributes(self)

    def Delete_Carabiner_Data(self):
        """ 
        Function Name: Delete_Brake_Data
        Function Description: This function clears the Brake data arrays 
        """  
        # Clear the class arrays
        CarabVisSelection.Delete_CarabVisSelection_Data(self)
        CarabPhysSelection.Delete_CarabPhysSelection_Data(self)
        CarabFunctSelection.Delete_CarabFunctSelection_Data(self)
        CarabinerPhysicalInspect.Delete_CarabinerPhysicalInspect_Data(self)
        CarabinerVisualInspect.Delete_CarabinerVisualInspect_Data(self)
        CarabinerFunctionInspect.Delete_CarabinerFunctInspect_Data(self)
        StandardCarabinerInspect.Delete_StandCarabInspect_Data(self)
                                                    
                
class DeviceHandle():
    """
    Class Name: DeviceHandle
    Class Description: This class gets and sets all of the Device Handle attributes. 
    """
    # Create class variable shared amongst all Device Handle methods
    aintDeviceHandleID = []
    astrHandleType = []
    
    # Instantiate the following attributes
    def __init__(self, intDeviceHandleID, strHandleType):
        self.intDeviceHandleID = intDeviceHandleID
        self.strHandleType = strHandleType

    # Property decorator object get function to access private intDeviceHandleID
    @property
    def intDeviceHandleID(self):
        return self._intDeviceHandleID

    # Property decorator object get function to access private strHandleType
    @property
    def strHandleType(self):
        return self._strHandleType

    # setter method 
    @intDeviceHandleID.setter 
    def intDeviceHandleID(self, intDeviceHandleID): 
        # Return true if specified object is of int type
        if not isinstance(intDeviceHandleID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intDeviceHandleID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intDeviceHandleID = intDeviceHandleID 
        
    # setter method 
    @strHandleType.setter 
    def strHandleType(self, strHandleType): 
        # Return true if specified object is of str type
        if not isinstance(strHandleType, str): 
            raise TypeError('Handle Type must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha
        if strHandleType.isspace(): 
            raise ValueError('Handle Type cannot be empty') 
        # Set the attribute to the value if true
        elif strHandleType.isascii():
            self._strHandleType = strHandleType
            # Set the global class bool to true
            Bool_Flag.Set_Handle_Bool_Value_True(Bool_Flag)

    def Append_HandleIDList(self, intObject):
        """ 
        Function Name: Append_HandleIDList
        Function Description: This function appends objects to the Handle ID list
        """    
        self.aintDeviceHandleID.append(intObject)

    def Remove_HandleIDList(self, intObject):
        """ 
        Function Name: Remove_HandleIDList
        Function Description: This function removes objects in the Device Handle ID list
        """    
        self.aintDeviceHandleID.remove(intObject)

    def Get_HandleIDList_Obj(self):
        """ 
        Function Name: Get_HandleIDList_Obj
        Function Description: This function gets all the objects in the Device Handle ID list
        """    
        return self.aintDeviceHandleID
    
    def Append_HandleTypeList(self, strObject):
        """ 
        Function Name: Append_HandleTypeList
        Function Description: This function appends objects to the Device Handle Type list
        """    
        self.astrHandleType.append(strObject)

    def Remove_HandleTypeList(self, strObject):
        """ 
        Function Name: Remove_HandleTypeList
        Function Description: This function removes objects in the Device Handle Type list
        """    
        self.astrHandleType.remove(strObject)

    def Get_HandleTypeList_Obj(self):
        """ 
        Function Name: Get_HandleTypeList_Obj
        Function Description: This function gets all the objects in the Device Handle Type list
        """    
        return self.astrHandleType  

    def Get_Handel_Data(self):
        """ 
        Function Name: Get_Handel_Data
        Function Description: This function gets all the objects in the Device Handle table
        """    
       # Create the sql query string
        sqlQuery = """SELECT * FROM TDeviceHandles"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the housing Data List
        for i in range(len(QueryResultList)):
            DeviceHandle.Append_HandleIDList(self, QueryResultList[i][0])
            DeviceHandle.Append_HandleTypeList(self, QueryResultList[i][1]) 

    def Delete_Handle_Data(self):
        """ 
        Function Name: Delete_Handle_Data
        Function Description: This function removes all the objects in the Device Handle class
        """    
        DeviceHandle.aintDeviceHandleID = []
        DeviceHandle.astrHandleType = []
        

class HandleVisSelection():
    """
    Class Name: HandleVisSelection
    Class Description: This class gets and sets all of the Handle Visual Selections. 
    """
    # Create class variable shared amongst all Handle visual methods
    aintHandVisMetalSelectID = []
    astrHandVisMetSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intHandVisMetalSelectID, strHandVisMetSelect, strHandleVisStatus):
        self.intHandVisMetalSelectID = intHandVisMetalSelectID
        self.strHandVisMetSelect = strHandVisMetSelect
        self.strHandleVisStatus = strHandleVisStatus

    # Property decorator object get function to access private intHandVisMetalSelectID
    @property
    def intHandVisMetalSelectID(self):
        return self._intHandVisMetalSelectID

    # Property decorator object get function to access private strHandVisMetSelect
    @property
    def strHandVisMetSelect(self):
        return self._strHandVisMetSelect

    # Property decorator object get function to access private strHandleVisStatus
    @property
    def strHandleVisStatus(self):
        return self._strHandleVisStatus
                
    # setter method 
    @intHandVisMetalSelectID.setter 
    def intHandVisMetalSelectID(self, intHandVisMetalSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intHandVisMetalSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intHandVisMetalSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intHandVisMetalSelectID = intHandVisMetalSelectID 
        
    # setter method 
    @strHandVisMetSelect.setter 
    def strHandVisMetSelect(self, strHandVisMetSelect): 
        # Return true if specified object is of str type
        if not isinstance(strHandVisMetSelect, str): 
            raise TypeError('Handle visual input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strHandVisMetSelect.isspace(): 
            raise ValueError('Handle visual input cannot be empty') 
        # Set the attribute to the value if true
        elif strHandVisMetSelect.isascii():
            self._strHandVisMetSelect = strHandVisMetSelect

    # setter method 
    @strHandleVisStatus.setter 
    def strHandleVisStatus(self, strHandleVisStatus): 
        # Return true if specified object is of str type
        if not isinstance(strHandleVisStatus, str): 
            raise TypeError('Handle visual input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strHandleVisStatus.isspace(): 
            raise ValueError('Handle visual input cannot be empty') 
        # Set the attribute to the value if true
        elif strHandleVisStatus.isascii():
            self._strHandleVisStatus = strHandleVisStatus

    def Append_HandVisIDList(self, intObject):
        """ 
        Function Name: Append_HandVisIDList
        Function Description: This function appends objects to the Handle Visual Selection ID list
        """    
        self.aintHandVisMetalSelectID.append(intObject)

    def Remove_HandVisIDList(self, intObject):
        """ 
        Function Name: Remove_HandVisIDList
        Function Description: This function removes objects in the Handle Visual Selection ID list
        """    
        self.aintHandVisMetalSelectID.remove(intObject)

    def Get_HandVisIDList_Obj(self):
        """ 
        Function Name: Get_HandVisIDList_Obj
        Function Description: This function gets all the objects in the Handle Visual Selection ID list
        """    
        return self.aintHandVisMetalSelectID
    
    def Append_HandVisSelectList(self, strObject):
        """ 
        Function Name: Append_HandVisSelectList
        Function Description: This function appends objects to the Handle Visual Selection list
        """    
        self.astrHandVisMetSelect.append(strObject)

    def Remove_HandVisSelectList(self, strObject):
        """ 
        Function Name: Remove_HandVisSelectList
        Function Description: This function removes objects in the Handle Visual Selection list
        """    
        self.astrHandVisMetSelect.remove(strObject)

    def Get_HandVisSelectList_Obj(self):
        """ 
        Function Name: Get_HandVisSelectList_Obj
        Function Description: This function gets all the objects in the Handle Visual Selection list
        """    
        return self.astrHandVisMetSelect   
                    
    def Delete_HandVisSelection_Data(self):
        """ 
        Function Name: Delete_HandVisSelection_Data
        Function Description: This function removes all the objects in the Handle Visual Selection class
        """    
        HandleVisSelection.aintHandVisMetalSelectID = []
        HandleVisSelection.astrHandVisMetSelect = []
        
    def Add_HandVisSelection_Query(self):
        """ 
        Function Name: Add_HandVisSelection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewHandleVisSelection
        """    
        # Create the sql query params
        sqlTableCol = ("intHandVisMetalSelectID", "strHandVisMetSelect")
        sqlTableName = "THandleVisMetalSelects"
        sqlTableValues = (HandleVisSelection.intHandVisMetalSelectID, HandleVisSelection.strHandVisMetSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)
        
        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Clear_HandleVisSel_Attributes(self):
        """ 
        Function Name: Clear_HandleVisSel_Attributes
        Function Description: This function clears the Handle Visual Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intHandVisMetalSelectID", "strHandVisMetSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)  
                    
        
class HandleVisualInspect(DeviceHandle, InspectionType, HandleVisSelection, InspectionStatus):
    """
    Class Name: HandleVisualInspect
    Class Description: This class gets and sets all of the Device Handle Visual Inspection attributes. 
    """
    # Create class variable shared amongst all Device Handle Visual Inspection methods
    aintHandleVisualID = []
    aHandleVisCache = []
        
    # Instantiate the following attributes
    def __init__(self, intHandleVisualID, intDeviceHandleID, intInspectionTypeID, intHandVisMetalSelectID, intInspectionStatusID):
        self.intHandleVisualID = intHandleVisualID
        # Inherits the child class with all the necessary objects
        DeviceHandle.__init__(intDeviceHandleID)
        InspectionType.__init__(intInspectionTypeID)
        HandleVisSelection.__init__(intHandVisMetalSelectID)
        InspectionStatus.__init__(intInspectionStatusID)

    # Property decorator object get function to access private intHandleVisualID
    @property
    def intHandleVisualID(self):
        return self._intHandleVisualID

    # setter method 
    @intHandleVisualID.setter 
    def intHandleVisualID(self, intHandleVisualID): 
        # Return true if specified object is of int type
        if not isinstance(intHandleVisualID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Device Handle Visual Inspection ID to value
        if intHandleVisualID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intHandleVisualID = intHandleVisualID 

    def Append_HandleVisualIDList(self, intObject):
        """ 
        Function Name: Append_HandleVisualIDList
        Function Description: This function appends objects to the Device Handle Visual Inspection ID list
        """    
        self.aintHandleVisualID.append(intObject)

    def Remove_HandleVisualIDList(self, intObject):
        """ 
        Function Name: Remove_HandleVisualIDList
        Function Description: This function removes objects in the Device Handle Visual Inspection ID list
        """    
        self.aintHandleVisualID.remove(intObject)

    def Get_HandleVisualIDList_Obj(self):
        """ 
        Function Name: Get_HandleVisualIDList_Obj
        Function Description: This function gets all the objects in the Device Handle Visual Inspection ID list
        """    
        return self.aintHandleVisualID
                
    def Delete_HandleVisualInspect_Data(self):
        """ 
        Function Name: Delete_HandleVisualInspect_Data
        Function Description: This function removes all the objects in the Device Handle Visual Inspection ID class
        """    
        HandleVisualInspect.aintHandleVisualID = []
        HandleVisualInspect.aHandleVisCache = []

    def Set_HandleVisualInspect_Data(self):
        """ 
        Function Name: Set_HandleVisualInspect_Data
        Function Description: This function sets all the objects in the Handle Visual Inspection class
        """    
        self.intHandleVisualID = HandleVisualInspect.aHandleVisCache[0]
        self.intDeviceHandleID = HandleVisualInspect.aHandleVisCache[1]
        self.intInspectionTypeID = HandleVisualInspect.aHandleVisCache[2]
        self.intHandVisMetalSelectID = HandleVisualInspect.aHandleVisCache[3]
        self.intInspectionStatusID = HandleVisualInspect.aHandleVisCache[4]
                                        
    def Add_HandelVisInspect_Query(self):
        """ 
        Function Name: Add_HandelVisInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Set the class variables before dumping the data to the database
        HandleVisualInspect.Set_HandleVisualInspect_Data(self)
                
        # Create the sql query string
        sqlTableCol = ("intHandleVisualID", "intDeviceHandleID", "intInspectionTypeID", "intHandVisMetalSelectID", "intInspectionStatusID")     
        sqlTableName = "THandleVisualInspections"
        sqlTableValues = (self.intHandleVisualID, self.intDeviceHandleID, self.intInspectionTypeID, self.intHandVisMetalSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)           

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)                                                            

    def Clear_HandleVisInspect_Attributes(self):
        """ 
        Function Name: Clear_HandleVisInspect_Attributes
        Function Description: This function clears the Handle Visual Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intHandleVisualID", "intDeviceHandleID", "intInspectionTypeID", "intHandVisMetalSelectID", "intInspectionStatusID")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            

class HandlePhysSelection():
    """
    Class Name: HandPhysSelection
    Class Description: This class gets and sets all of the Handle Physical Selections. 
    """
    # Create class variable shared amongst all Handle physical methods
    aintHandPhysMetalSelectID = []
    astrHandPhysMetSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intHandPhysMetalSelectID, strHandPhysMetSelect, strHandlePhysStatus):
        self.intHandPhysMetalSelectID = intHandPhysMetalSelectID
        self.strHandPhysMetSelect = strHandPhysMetSelect
        self.strHandlePhysStatus = strHandlePhysStatus

    # Property decorator object get function to access private intHandPhysMetalSelectID
    @property
    def intHandPhysMetalSelectID(self):
        return self._intHandPhysMetalSelectID

    # Property decorator object get function to access private strHandPhysMetSelect
    @property
    def strHandPhysMetSelect(self):
        return self._strHandPhysMetSelect

    # Property decorator object get function to access private strHandlePhysStatus
    @property
    def strHandlePhysStatus(self):
        return self._strHandlePhysStatus
            
    # setter method 
    @intHandPhysMetalSelectID.setter 
    def intHandPhysMetalSelectID(self, intHandPhysMetalSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intHandPhysMetalSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intHandPhysMetalSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intHandPhysMetalSelectID = intHandPhysMetalSelectID 
        
    # setter method 
    @strHandPhysMetSelect.setter 
    def strHandPhysMetSelect(self, strHandPhysMetSelect): 
        # Return true if specified object is of str type
        if not isinstance(strHandPhysMetSelect, str): 
            raise TypeError('Handle physical input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strHandPhysMetSelect.isspace(): 
            raise ValueError('Handle physical input cannot be empty') 
        # Set the attribute to the value if true
        elif strHandPhysMetSelect.isascii():
            self._strHandPhysMetSelect = strHandPhysMetSelect

    # setter method 
    @strHandlePhysStatus.setter 
    def strHandlePhysStatus(self, strHandlePhysStatus): 
        # Return true if specified object is of str type
        if not isinstance(strHandlePhysStatus, str): 
            raise TypeError('Handle physical status must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strHandlePhysStatus.isspace(): 
            raise ValueError('Handle physical status cannot be empty') 
        # Set the attribute to the value if true
        elif strHandlePhysStatus.isascii():
            self._strHandlePhysStatus = strHandlePhysStatus

    def Append_HandPhysIDList(self, intObject):
        """ 
        Function Name: Append_HandPhysIDList
        Function Description: This function appends objects to the Handle Physical Selection ID list
        """    
        self.aintHandPhysMetalSelectID.append(intObject)

    def Remove_HandPhysIDList(self, intObject):
        """ 
        Function Name: Remove_HandPhysIDList
        Function Description: This function removes objects in the Handle Physical Selection ID list
        """    
        self.aintHandPhysMetalSelectID.remove(intObject)

    def Get_HandPhysIDList_Obj(self):
        """ 
        Function Name: Get_HandPhysIDList_Obj
        Function Description: This function gets all the objects in the Handle Physical Selection ID list
        """    
        return self.aintHandPhysMetalSelectID
    
    def Append_HandPhysSelectList(self, strObject):
        """ 
        Function Name: Append_HandPhysSelectList
        Function Description: This function appends objects to the Handle Physical Selection list
        """    
        self.astrHandPhysMetSelect.append(strObject)

    def Remove_HandPhysSelectList(self, strObject):
        """ 
        Function Name: Remove_HandPhysSelectList
        Function Description: This function removes objects in the Handle Physical Selection list
        """    
        self.astrHandPhysMetSelect.remove(strObject)

    def Get_HandPhysSelectList_Obj(self):
        """ 
        Function Name: Get_HandPhysSelectList_Obj
        Function Description: This function gets all the objects in the Handle Physical Selection list
        """    
        return self.astrHandPhysMetSelect   
                    
    def Delete_HandPhysSelectList_Data(self):
        """ 
        Function Name: Delete_HandPhysSelectList_Data
        Function Description: This function removes all the objects in the Handle Physical Selection class
        """    
        HandlePhysSelection.aintHandPhysMetalSelectID = []
        HandlePhysSelection.astrHandPhysMetSelect = []
        
    def Add_HandPhysSelection_Query(self):
        """ 
        Function Name: Add_HandPhysSelection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewHandlePhysSelection
        """    
        # Create the sql query string
        sqlTableCol = ("intHandPhysMetalSelectID", "strHandPhysMetSelect")   
        sqlTableName = "THandlePhysMetalSelects"
        sqlTableValues = (HandlePhysSelection.intHandPhysMetalSelectID, HandlePhysSelection.strHandPhysMetSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)        

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Clear_HandlePhysSel_Attributes(self):
        """ 
        Function Name: Clear_HandlePhysSel_Attributes
        Function Description: This function clears the Handle Physical Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intHandPhysMetalSelectID", "strHandPhysMetSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                    
        
class HandlePhysicalInspect(DeviceHandle, InspectionType, HandlePhysSelection, InspectionStatus):
    """
    Class Name: HandlePhysicalInspect
    Class Description: This class gets and sets all of the Device Handle Physical Inspection  attributes. 
    """
    # Create class variable shared amongst all Device Handle Physical Inspection methods
    aintHandlePhysicalID = []
    aHandlePhysCache = []
        
    # Instantiate the following attributes
    def __init__(self, intHandlePhysicalID, intDeviceHandleID, intInspectionTypeID, intHandPhysMetalSelectID, intInspectionStatusID):
        self.intHandlePhysicalID = intHandlePhysicalID
        # Inherits the child class with all the necessary objects
        DeviceHandle.__init__(intDeviceHandleID)
        InspectionType.__init__(intInspectionTypeID)
        HandlePhysSelection.__init__(intHandPhysMetalSelectID)
        InspectionStatus.__init__(intInspectionStatusID)
        
    # Property decorator object get function to access private intHandlePhysicalID
    @property
    def intHandlePhysicalID(self):
        return self._intHandlePhysicalID

    # setter method 
    @intHandlePhysicalID.setter 
    def intHandlePhysicalID(self, intHandlePhysicalID): 
        # Return true if specified object is of int type
        if not isinstance(intHandlePhysicalID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Handle Physical Inspection ID to value
        if intHandlePhysicalID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intHandlePhysicalID = intHandlePhysicalID 

    def Append_HandlePhysicalIDList(self, intObject):
        """ 
        Function Name: Append_HandlePhysicalIDList
        Function Description: This function appends objects to the Device Handle Physical Inspection ID list
        """    
        self.aintHandlePhysicalID.append(intObject)

    def Remove_HandlePhysicalIDList(self, intObject):
        """ 
        Function Name: Remove_HandlePhysicalIDList
        Function Description: This function removes objects in the Device Handle Physical Inspection ID list
        """    
        self.aintHandlePhysicalID.remove(intObject)

    def Get_HandlePhysicalIDList_Obj(self):
        """ 
        Function Name: Get_HandlePhysicalIDList_Obj
        Function Description: This function gets all the objects in the Device Handle Physical Inspection ID list
        """    
        return self.aintHandlePhysicalID
                
    def Delete_HandlePhysicalInspect_Data(self):
        """ 
        Function Name: Delete_HandlePhysicalInspect_Data
        Function Description: This function removes all the objects in the Device Handle Physical Inspection ID class
        """    
        HandlePhysicalInspect.aintHandlePhysicalID = []
        HandlePhysicalInspect.aHandlePhysCache = []

    def Set_HandlePhysicalInspect_Data(self):
        """ 
        Function Name: Set_HandlePhysicalInspect_Data
        Function Description: This function sets all the objects in the Handle Physical Inspection class
        """    
        self.intHandlePhysicalID = HandlePhysicalInspect.aHandlePhysCache[0]
        self.intDeviceHandleID = HandlePhysicalInspect.aHandlePhysCache[1]
        self.intInspectionTypeID = HandlePhysicalInspect.aHandlePhysCache[2]
        self.intHandPhysMetalSelectID = HandlePhysicalInspect.aHandlePhysCache[3]
        self.intInspectionStatusID = HandlePhysicalInspect.aHandlePhysCache[4]
                                        
    def Add_HandelPhysInspect_Query(self):
        """ 
        Function Name: Add_HandelPhysInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Set the class variables before dumping the data to the database
        HandlePhysicalInspect.Set_HandlePhysicalInspect_Data(self)
                
        # Create the sql query string
        sqlTableCol = ("intHandlePhysicalID", "intDeviceHandleID", "intInspectionTypeID", "intHandPhysMetalSelectID", "intInspectionStatusID")     
        sqlTableName = "THandlePhysicalInspections"
        sqlTableValues = (self.intHandlePhysicalID, self.intDeviceHandleID, self.intInspectionTypeID, self.intHandPhysMetalSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)          

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)  

    def Clear_HandlePhysInspect_Attributes(self):
        """ 
        Function Name: Clear_HandlePhysInspect_Attributes
        Function Description: This function clears the Handle Physical Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intHandleVisualID", "intDeviceHandleID", "intInspectionTypeID", "intHandVisMetalSelectID", "intInspectionStatusID")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                    
        
class StandardHandelInspect(HandleVisualInspect, HandlePhysicalInspect):
    """
    Class Name: StandardHandelInspect
    Class Description: This class gets and sets all of the Standard Handel Inspection attributes. 
    Pass in the Handel Visual and Physical Inspection Classes.
    """
    # Create class variable shared amongst all Standard Handel methods
    aintStandardHandleInspectionID = []
    aStandardHandleInsCache = []
            
    # Instantiate the following attributes
    def __init__(self, intStandardHandleInspectionID, intHandleVisualID, intHandlePhysicalID):
        self.intStandardHandleInspectionID = intStandardHandleInspectionID
        # Inherits the child class with all the necessary objects
        HandleVisualInspect.__init__(intHandleVisualID)
        HandlePhysicalInspect.__init__(intHandlePhysicalID)

    # Property decorator object get function to access private intStandardHandleInspectionID
    @property
    def intStandardHandleInspectionID(self):
        return self._intStandardHandleInspectionID
    
    # setter method 
    @intStandardHandleInspectionID.setter 
    def intStandardHandleInspectionID(self, intStandardHandleInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intStandardHandleInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intStandardHandleInspectionID < 0:             
            raise ValueError('ID cannot be negative') 

        self._intStandardHandleInspectionID = intStandardHandleInspectionID 

    def Append_StandHoseInspectIDList(self, intObject):
        """ 
        Function Name: Append_StandHoseInspectIDList
        Function Description: This function appends objects to the Standard Hose Inspection ID list
        """    
        self.aintStandardHandleInspectionID.append(intObject)
        
    def Remove_StandHoseInspectIDList(self, intObject):
        """ 
        Function Name: Remove_StandHoseInspectIDList
        Function Description: This function removes objects in the Standard Hose Inspection ID list
        """    
        self.aintStandardHandleInspectionID.remove(intObject)

    def Get_StandHoseInspectIDList_Obj(self):
        """ 
        Function Name: Get_StandHoseInspectIDList_Obj
        Function Description: This function gets all the objects in the Standard Hose Inspection ID list
        """    
        return self.aintStandardHandleInspectionID

    def Add_StandHandleInspect_Query(self):
        """ 
        Function Name: Add_StandHandleInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewStandardCarabinerInspection
        """    
        # Create the sql query string
        sqlTableNames = ("TStandardHandleInspections")
        sqlTableCol = ("intStandardHandleInspectionID", "intHandleVisualID", "intHandlePhysicalID", "intInspectionStatusID")
        
        # Set the primary key values from the cached array object
        aPrimKeyValues = [item for item in StandardHandelInspect.aStandardHandleInsCache]

        # Get the visual, physical, and functional status IDs
        VisStatusID = InspectionStatus.astrInspectionStatusDesc.index(HandleVisSelection.strHandleVisStatus) + 1
        PhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(HandlePhysSelection.strHandlePhysStatus) + 1
        aInsStatusID = [VisStatusID, PhysStatusID]

        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(aInsStatusID)

        # Append the AutoBelay Status array 
        AutoBelayInspect.aAutoBelayInspectStatus.append(intOverallStatus)
                 
        # Append the primary key list with the new over status ID
        aPrimKeyValues.append(intOverallStatus)                      
        
        # Set the parameters
        sqlParams = (sqlTableNames, sqlTableCol, tuple(aPrimKeyValues))

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)        
                
    def Delete_StandHandleInspect_Data(self):
        """ 
        Function Name: Delete_StandHandleInspect_Data
        Function Description: This function removes all the objects in the Standard Handle Inspection class
        """    
        StandardHandelInspect.aintStandardHandleInspectionID = []
        StandardHandelInspect.aStandardHandleInsCache = []

    def Clear_HandleStandardInspect_Attributes(self):
        """ 
        Function Name: Clear_HandleStandardInspect_Attributes
        Function Description: This function clears the Handle Visual Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intStandardHandleInspectionID", "intHandleVisualID", "intHandlePhysicalID", "intInspectionStatusID")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            
    def Reset_Handle_Data(self):
        """ 
        Function Name: Reset_Handle_Data
        Function Description: This function clears the Handle data attributes 
        """  
        # Clear the class attributes
        HandleVisSelection.Clear_HandleVisSel_Attributes(self)
        HandlePhysSelection.Clear_HandlePhysSel_Attributes(self)
        HandleVisualInspect.Clear_HandleVisInspect_Attributes(self)
        HandlePhysicalInspect.Clear_HandlePhysInspect_Attributes(self)
        StandardHandelInspect.Clear_HandleStandardInspect_Attributes(self)

    def Delete_Handle_Data(self):
        """ 
        Function Name: Delete_Handle_Data
        Function Description: This function clears the Handle data arrays 
        """  
        # Clear the class arrays                
        HandleVisSelection.Delete_HandVisSelection_Data(self)
        HandlePhysSelection.Delete_HandPhysSelectList_Data(self)
        HandleVisualInspect.Delete_HandleVisualInspect_Data(self)
        HandlePhysicalInspect.Delete_HandlePhysicalInspect_Data(self)
        StandardHandelInspect.Delete_StandHandleInspect_Data(self)
        
                                                    
class CaseHousing():
    """
    Class Name: CaseHousing
    Class Description: This class gets and sets all of the Case Housing attributes. 
    """
    # Create class variable shared amongst all Case Housing methods
    aintCaseHousingID = []
    astrCaseComponentDescs = []
        
    # Instantiate the following attributes
    def __init__(self, intCaseHousingID, strCaseComponentDesc):
        self.intCaseHousingID = intCaseHousingID
        self.strCaseComponentDesc = strCaseComponentDesc
        
    # Property decorator object get function to access private intCaseHousingID
    @property
    def intCaseHousingID(self):
        return self._intCaseHousingID

    # Property decorator object get function to access private strCaseComponentDesc
    @property
    def strCaseComponentDesc(self):
        return self._strCaseComponentDesc

    # setter method 
    @intCaseHousingID.setter 
    def intCaseHousingID(self, intCaseHousingID): 
        # Return true if specified object is of int type
        if not isinstance(intCaseHousingID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intCaseHousingID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intCaseHousingID = intCaseHousingID    

    # setter method 
    @strCaseComponentDesc.setter 
    def strCaseComponentDesc(self, strCaseComponentDesc): 
        # Return true if specified object is of str type
        if not isinstance(strCaseComponentDesc, str): 
            raise TypeError('Case Weight must be a string') 
        # Check if the value is empty, otherwise return if the value is alpha 
        if strCaseComponentDesc.isspace(): 
            raise ValueError('Case Weight cannot be empty') 
        # Set the attribute to the value if true
        elif strCaseComponentDesc.isascii():
            self._strCaseComponentDesc = strCaseComponentDesc
            Bool_Flag.Set_Bool_Value_True(Bool_Flag)

    def Append_CaseIDList(self, intObject):
        """ 
        Function Name: Append_CaseIDList
        Function Description: This function appends objects to the Case Housing ID list
        """    
        self.aintCaseHousingID.append(intObject)

    def Remove_CaseIDList(self, intObject):
        """ 
        Function Name: Remove_CaseIDList
        Function Description: This function removes objects in the Case Housing ID list
        """    
        self.aintCaseHousingID.remove(intObject)

    def Get_CaseIDList_Obj(self):
        """ 
        Function Name: Get_CaseIDList_Obj
        Function Description: This function gets all the objects in the Case Housing ID list
        """    
        return self.aintCaseHousingID            

    def Append_CaseDescList(self, strObject):
        """ 
        Function Name: Append_CaseDescList
        Function Description: This function appends objects to the Case Housing Description list
        """    
        self.astrCaseComponentDescs.append(strObject)

    def Remove_CaseDescList(self, strObject):
        """ 
        Function Name: Remove_CaseDescList
        Function Description: This function removes objects in the Case Housing Description list
        """    
        self.astrCaseComponentDescs.remove(strObject)

    def Get_CaseDescList_Obj(self):
        """ 
        Function Name: Get_CaseDescList_Obj
        Function Description: This function gets all the objects in the Case Housing Description list
        """    
        return self.astrCaseComponentDescs  

    def Get_CaseHousing_Data(self):
        """ 
        Function Name: Get_CaseHousing_Data
        Function Description: This function gets all the objects in the Case Housing table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TCaseHousings"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the housing Data List
        for i in range(len(QueryResultList)):
            CaseHousing.Append_CaseIDList(self, QueryResultList[i][0])
            CaseHousing.Append_CaseDescList(self, QueryResultList[i][1]) 
                            
    def Delete_Case_Data(self):
        """ 
        Function Name: Delete_Case_Data
        Function Description: This function removes all the objects in the Case class
        """    
        CaseHousing.aintCaseHousingID = []
        CaseHousing.astrCaseComponentDescs = []  
            
            
class CaseCompSelection():
    """
    Class Name: CaseCompSelection
    Class Description: This class gets and sets all of the Case Component Selections. 
    """
    # Create class variable shared amongst all Case Component methods
    aintCaseCompSelectID = []
    astrCaseCompSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intCaseCompSelectID, strCaseCompSelect):
        self.intCaseCompSelectID = intCaseCompSelectID
        self.strCaseCompSelect = strCaseCompSelect        

    # Property decorator object get function to access private intCaseCompSelectID
    @property
    def intCaseCompSelectID(self):
        return self._intCaseCompSelectID

    # Property decorator object get function to access private strCaseCompSelect
    @property
    def strCaseCompSelect(self):
        return self._strCaseCompSelect

    # setter method 
    @intCaseCompSelectID.setter 
    def intCaseCompSelectID(self, intCaseCompSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intCaseCompSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intCaseCompSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intCaseCompSelectID = intCaseCompSelectID 
        
    # setter method 
    @strCaseCompSelect.setter 
    def strCaseCompSelect(self, strCaseCompSelect): 
        # Return true if specified object is of str type
        if not isinstance(strCaseCompSelect, str): 
            raise TypeError('Case Component input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strCaseCompSelect.isspace(): 
            raise ValueError('Case Component input cannot be empty') 
        # Set the attribute to the value if true
        elif strCaseCompSelect.isascii():
            self._strCaseCompSelect = strCaseCompSelect
            # Set the global class bool to true
            Bool_Flag.Set_Case_Bool_Value_True(Bool_Flag)

    def Append_CaseCompIDList(self, intObject):
        """ 
        Function Name: Append_CaseCompIDList
        Function Description: This function appends objects to the Case Component Selection ID list
        """    
        self.aintCaseCompSelectID.append(intObject)

    def Remove_CaseCompIDList(self, intObject):
        """ 
        Function Name: Remove_CaseCompIDList
        Function Description: This function removes objects in the Case Component Selection ID list
        """    
        self.aintCaseCompSelectID.remove(intObject)

    def Get_CaseCompIDList_Obj(self):
        """ 
        Function Name: Get_CaseCompIDList_Obj
        Function Description: This function gets all the objects in the Case Component Selection ID list
        """    
        return self.aintCaseCompSelectID
    
    def Append_CaseCompSelectList(self, strObject):
        """ 
        Function Name: Append_CaseCompSelectList
        Function Description: This function appends objects to the Case Component Selection list
        """    
        self.astrCaseCompSelect.append(strObject)

    def Remove_CaseCompSelectList(self, strObject):
        """ 
        Function Name: Remove_CaseCompSelectList
        Function Description: This function removes objects in the Case Component Selection list
        """    
        self.astrCaseCompSelect.remove(strObject)

    def Get_CaseCompSelectList_Obj(self):
        """ 
        Function Name: Get_CaseCompSelectList_Obj
        Function Description: This function gets all the objects in the Case Component Selection list
        """    
        return self.astrCaseCompSelect   
                    
    def Delete_CaseCompSelection_Data(self):
        """ 
        Function Name: Delete_CaseCompSelection_Data
        Function Description: This function removes all the objects in the Case Component Selection class
        """    
        CaseCompSelection.aintCaseCompSelectID = []
        CaseCompSelection.astrCaseCompSelect = []
        
    def Add_CaseCompSelection_Query(self):
        """ 
        Function Name: Add_CaseCompSelection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewCaseCompSelection
        """    
        # Create the sql query params
        sqlTableCol = ("intCaseCompSelectID", "strCaseCompSelect")
        sqlTableName = "TCaseCompSelects"
        sqlTableValues = (CaseCompSelection.intCaseCompSelectID, CaseCompSelection.strCaseCompSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)
        
        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams) 
        
    def Clear_CaseCompSel_Attributes(self):
        """ 
        Function Name: Clear_CaseCompSel_Attributes
        Function Description: This function clears the Case Comp Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intCaseCompSelectID", "strCaseCompSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            
        
class CaseVisSelection():
    """
    Class Name: CaseVisSelection
    Class Description: This class gets and sets all of the Case Visual Selections. 
    """
    # Create class variable shared amongst all Case visual methods
    aintCaseVisMetalSelectID = []
    astrCaseVisMetSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intCaseVisMetalSelectID, strCaseVisMetSelect, strCaseVisStatus):
        self.intCaseVisMetalSelectID = intCaseVisMetalSelectID
        self.strCaseVisMetSelect = strCaseVisMetSelect
        self.strCaseVisStatus = strCaseVisStatus

    # Property decorator object get function to access private intCaseVisMetalSelectID
    @property
    def intCaseVisMetalSelectID(self):
        return self._intCaseVisMetalSelectID

    # Property decorator object get function to access private strCaseVisMetSelect
    @property
    def strCaseVisMetSelect(self):
        return self._strCaseVisMetSelect

    # Property decorator object get function to access private strCaseVisStatus
    @property
    def strCaseVisStatus(self):
        return self._strCaseVisStatus
                    
    # setter method 
    @intCaseVisMetalSelectID.setter 
    def intCaseVisMetalSelectID(self, intCaseVisMetalSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intCaseVisMetalSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intCaseVisMetalSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intCaseVisMetalSelectID = intCaseVisMetalSelectID 
        
    # setter method 
    @strCaseVisMetSelect.setter 
    def strCaseVisMetSelect(self, strCaseVisMetSelect): 
        # Return true if specified object is of str type
        if not isinstance(strCaseVisMetSelect, str): 
            raise TypeError('Case visual input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strCaseVisMetSelect.isspace(): 
            raise ValueError('Case visual input cannot be empty') 
        # Set the attribute to the value if true
        elif strCaseVisMetSelect.isascii():
            self._strCaseVisMetSelect = strCaseVisMetSelect

    # setter method 
    @strCaseVisStatus.setter 
    def strCaseVisStatus(self, strCaseVisStatus): 
        # Return true if specified object is of str type
        if not isinstance(strCaseVisStatus, str): 
            raise TypeError('Case Component status must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strCaseVisStatus.isspace(): 
            raise ValueError('Case Component status cannot be empty') 
        # Set the attribute to the value if true
        elif strCaseVisStatus.isascii():
            self._strCaseVisStatus = strCaseVisStatus

    def Append_CaseVisIDList(self, intObject):
        """ 
        Function Name: Append_CaseVisIDList
        Function Description: This function appends objects to the Case Visual Selection ID list
        """    
        self.aintCaseVisMetalSelectID.append(intObject)

    def Remove_CaseVisIDList(self, intObject):
        """ 
        Function Name: Remove_CaseVisIDList
        Function Description: This function removes objects in the Case Visual Selection ID list
        """    
        self.aintCaseVisMetalSelectID.remove(intObject)

    def Get_CaseVisIDList_Obj(self):
        """ 
        Function Name: Get_CaseVisIDList_Obj
        Function Description: This function gets all the objects in the Case Visual Selection ID list
        """    
        return self.aintCaseVisMetalSelectID
    
    def Append_CaseVisSelectList(self, strObject):
        """ 
        Function Name: Append_CaseVisSelectList
        Function Description: This function appends objects to the Case Visual Selection list
        """    
        self.astrCaseVisMetSelect.append(strObject)

    def Remove_CaseVisSelectList(self, strObject):
        """ 
        Function Name: Remove_CaseVisSelectList
        Function Description: This function removes objects in the Case Visual Selection list
        """    
        self.astrCaseVisMetSelect.remove(strObject)

    def Get_CaseVisSelectList_Obj(self):
        """ 
        Function Name: Get_CaseVisSelectList_Obj
        Function Description: This function gets all the objects in the Case Visual Selection list
        """    
        return self.astrCaseVisMetSelect   
                    
    def Delete_CaseVisSelection_Data(self):
        """ 
        Function Name: Delete_CaseVisSelection_Data
        Function Description: This function removes all the objects in the Case Visual Selection class
        """    
        CaseVisSelection.aintCaseVisMetalSelectID = []
        CaseVisSelection.astrCaseVisMetSelect = []
        
    def Add_CaseVisSelection_Query(self):
        """ 
        Function Name: Add_CaseVisSelection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewCaseVisSelection
        """    
        # Create the sql query params
        sqlTableCol = ("intCaseVisMetalSelectID", "strCaseVisMetSelect")
        sqlTableName = "TCaseVisMetalSelects"
        sqlTableValues = (CaseVisSelection.intCaseVisMetalSelectID, CaseVisSelection.strCaseVisMetSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)
        
        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)     

    def Clear_CaseVisSel_Attributes(self):
        """ 
        Function Name: Clear_CaseVisSel_Attributes
        Function Description: This function clears the Case Visual Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intHandVisMetalSelectID", "strHandVisMetSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                    
        
class CaseVisualInspect(CaseCompSelection, InspectionType, CaseVisSelection, InspectionStatus):
    """
    Class Name: CaseVisualInspect
    Class Description: This class gets and sets all of the Case Housing Visual Inspection attributes. 
    """
    # Create class variable shared amongst all Case Housing Visual Inspection methods
    aintCaseHousingVisualInspectionID = []
    aCaseVisInsCache = []
        
    # Instantiate the following attributes
    def __init__(self, intCaseHousingVisualInspectionID, intCaseCompSelectID, intInspectionTypeID, intCaseVisMetalSelectID, intInspectionStatusID):
        self.intCaseHousingVisualInspectionID = intCaseHousingVisualInspectionID
        # Inherits the child class with all the necessary objects
        CaseCompSelection.__init__(intCaseCompSelectID)
        InspectionType.__init__(intInspectionTypeID)
        CaseVisSelection.__init__(intCaseVisMetalSelectID)
        InspectionStatus.__init__(intInspectionStatusID)

    # Property decorator object get function to access private intCaseHousingVisualInspectionID
    @property
    def intCaseHousingVisualInspectionID(self):
        return self._intCaseHousingVisualInspectionID

    # setter method 
    @intCaseHousingVisualInspectionID.setter 
    def intCaseHousingVisualInspectionID(self, intCaseHousingVisualInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intCaseHousingVisualInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Case Housing Visual Inspection ID to value
        if intCaseHousingVisualInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intCaseHousingVisualInspectionID = intCaseHousingVisualInspectionID 

    def Append_CaseVisualIDList(self, intObject):
        """ 
        Function Name: Append_CaseVisualIDList
        Function Description: This function appends objects to the Case Housing Visual Inspection ID list
        """    
        self.aintCaseHousingVisualInspectionID.append(intObject)

    def Remove_CaseVisualIDList(self, intObject):
        """ 
        Function Name: Remove_CaseVisualIDList
        Function Description: This function removes objects in the Case Housing Visual Inspection ID list
        """    
        self.aintCaseHousingVisualInspectionID.remove(intObject)

    def Get_CaseVisualIDList_Obj(self):
        """ 
        Function Name: Get_CaseVisualIDList_Obj
        Function Description: This function gets all the objects in the Case Housing Visual Inspection ID list
        """    
        return self.aintCaseHousingVisualInspectionID
                
    def Delete_CaseVisualInspect_Data(self):
        """ 
        Function Name: Delete_CaseVisualInspect_Data
        Function Description: This function removes all the objects in the Case Housing Visual Inspection ID class
        """    
        CaseVisualInspect.aintCaseHousingVisualInspectionID = []
        CaseVisSelection.aintCaseVisInsCache = []

    def Set_CaseVisualInspect_Data(self):
        """ 
        Function Name: Set_CaseVisualInspect_Data
        Function Description: This function sets all the objects in the Case Visual Inspection class
        """    
        self.intCaseHousingVisualInspectionID = CaseVisualInspect.aCaseVisInsCache[0]
        self.intCaseCompSelectID = CaseVisualInspect.aCaseVisInsCache[1]
        self.intInspectionTypeID = CaseVisualInspect.aCaseVisInsCache[2]
        self.intCaseVisMetalSelectID = CaseVisualInspect.aCaseVisInsCache[3]
        self.intInspectionStatusID = CaseVisualInspect.aCaseVisInsCache[4]
        
    def Add_CaseVisualInspect_Query(self):
        """ 
        Function Name: Add_CaseVisualInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewCaseHousingVisualInspection
        """    
        # Set the class variables before dumping the data to the database
        CaseVisualInspect.Set_CaseVisualInspect_Data(self)
                
        # Create the sql query string
        sqlTableCol = ("intCaseHousingVisualInspectionID", "intCaseCompSelectID", "intInspectionTypeID", "intCaseVisMetalSelectID", "intInspectionStatusID")     
        sqlTableName = "TCaseHousingVisualInspections"
        sqlTableValues = (self.intCaseHousingVisualInspectionID, self.intCaseCompSelectID, self.intInspectionTypeID, self.intCaseVisMetalSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)           

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Clear_CaseVisInspect_Attributes(self):
        """ 
        Function Name: Clear_CaseVisInspect_Attributes
        Function Description: This function clears the Case Visual Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intCaseHousingVisualInspectionID", "intCaseCompSelectID", "intInspectionTypeID", "intCaseVisMetalSelectID", "intInspectionStatusID")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                    

class CasePhysSelection():
    """
    Class Name: CasePhysSelection
    Class Description: This class gets and sets all of the Case Physical Selections. 
    """
    # Create class variable shared amongst all Case physical methods
    aintCasePhysMetalSelectID = []
    astrCasePhysMetSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intCasePhysMetalSelectID, strCasePhysMetSelect, strCasePhysStatus):
        self.intCasePhysMetalSelectID = intCasePhysMetalSelectID
        self.strCasePhysMetSelect = strCasePhysMetSelect
        self.strCasePhysStatus = strCasePhysStatus

    # Property decorator object get function to access private intCasePhysMetalSelectID
    @property
    def intCasePhysMetalSelectID(self):
        return self._intCasePhysMetalSelectID

    # Property decorator object get function to access private strCasePhysMetSelect
    @property
    def strCasePhysMetSelect(self):
        return self._strCasePhysMetSelect

    # Property decorator object get function to access private strCasePhysStatus
    @property
    def strCasePhysStatus(self):
        return self._strCasePhysStatus
                
    # setter method 
    @intCasePhysMetalSelectID.setter 
    def intCasePhysMetalSelectID(self, intCasePhysMetalSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intCasePhysMetalSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intCasePhysMetalSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intCasePhysMetalSelectID = intCasePhysMetalSelectID 
        
    # setter method 
    @strCasePhysMetSelect.setter 
    def strCasePhysMetSelect(self, strCasePhysMetSelect): 
        # Return true if specified object is of str type
        if not isinstance(strCasePhysMetSelect, str): 
            raise TypeError('Case physical input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strCasePhysMetSelect.isspace(): 
            raise ValueError('Case physical input cannot be empty') 
        # Set the attribute to the value if true
        elif strCasePhysMetSelect.isascii():
            self._strCasePhysMetSelect = strCasePhysMetSelect

    # setter method 
    @strCasePhysStatus.setter 
    def strCasePhysStatus(self, strCasePhysStatus): 
        # Return true if specified object is of str type
        if not isinstance(strCasePhysStatus, str): 
            raise TypeError('Case physical status must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strCasePhysStatus.isspace(): 
            raise ValueError('Case physical status cannot be empty') 
        # Set the attribute to the value if true
        elif strCasePhysStatus.isascii():
            self._strCasePhysStatus = strCasePhysStatus

    def Append_CasePhysIDList(self, intObject):
        """ 
        Function Name: Append_CasePhysIDList
        Function Description: This function appends objects to the Case Physical Selection ID list
        """    
        self.aintCasePhysMetalSelectID.append(intObject)

    def Remove_CasePhysIDList(self, intObject):
        """ 
        Function Name: Remove_CasePhysIDList
        Function Description: This function removes objects in the Case Physical Selection ID list
        """    
        self.aintCasePhysMetalSelectID.remove(intObject)

    def Get_CasePhysIDList_Obj(self):
        """ 
        Function Name: Get_CasePhysIDList_Obj
        Function Description: This function gets all the objects in the Case Physical Selection ID list
        """    
        return self.aintCasePhysMetalSelectID
    
    def Append_CasePhysSelectList(self, strObject):
        """ 
        Function Name: Append_CasePhysSelectList
        Function Description: This function appends objects to the Case Physical Selection list
        """    
        self.astrCasePhysMetSelect.append(strObject)

    def Remove_CasePhysSelectList(self, strObject):
        """ 
        Function Name: Remove_CasePhysSelectList
        Function Description: This function removes objects in the Case Physical Selection list
        """    
        self.astrCasePhysMetSelect.remove(strObject)

    def Get_CasePhysSelectList_Obj(self):
        """ 
        Function Name: Get_CasePhysSelectList_Obj
        Function Description: This function gets all the objects in the Case Physical Selection list
        """    
        return self.astrCasePhysMetSelect   
                    
    def Delete_CasePhysSelection_Data(self):
        """ 
        Function Name: Delete_CasePhysSelection_Data
        Function Description: This function removes all the objects in the Case Physical Selection class
        """    
        CasePhysSelection.aintCasePhysMetalSelectID = []
        CasePhysSelection.astrCasePhysMetSelect = []
        
    def Add_CasePhysSelection_Query(self):
        """ 
        Function Name: Add_CasePhysSelection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewCasePhysSelection
        """    
        # Create the sql query params
        sqlTableCol = ("intCasePhysMetalSelectID", "strCasePhysMetSelect")
        sqlTableName = "TCasePhysMetalSelects"
        sqlTableValues = (CasePhysSelection.intCasePhysMetalSelectID, CasePhysSelection.strCasePhysMetSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)
        
        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams) 
               
    def Clear_CasePhysSel_Attributes(self):
        """ 
        Function Name: Clear_CasePhysSel_Attributes
        Function Description: This function clears the Case Physical Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intCasePhysMetalSelectID", "strCasePhysMetSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            
        
class CasePhysicalInspect(CaseCompSelection, InspectionType, CasePhysSelection, InspectionStatus):
    """
    Class Name: CaseVisualInspect
    Class Description: This class gets and sets all of the Case Housing Physical Inspection attributes. 
    """
    # Create class variable shared amongst all Case Housing Physical Inspection methods
    aintCaseHousingPhysicalInspectionID = []
    aCasePhysInsCache = []
        
    # Instantiate the following attributes
    def __init__(self, intCaseHousingPhysicalInspectionID, intCaseCompSelectID, intInspectionTypeID, intCasePhysMetalSelectID, intInspectionStatusID):
        self.intCaseHousingPhysicalInspectionID = intCaseHousingPhysicalInspectionID
        # Inherits the child class with all the necessary objects
        CaseCompSelection.__init__(intCaseCompSelectID)
        InspectionType.__init__(intInspectionTypeID)
        CasePhysSelection.__init__(intCasePhysMetalSelectID)
        InspectionStatus.__init__(intInspectionStatusID)

    # Property decorator object get function to access private intCaseHousingPhysicalInspectionID
    @property
    def intCaseHousingPhysicalInspectionID(self):
        return self._intCaseHousingPhysicalInspectionID

    # setter method 
    @intCaseHousingPhysicalInspectionID.setter 
    def intCaseHousingPhysicalInspectionID(self, intCaseHousingPhysicalInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intCaseHousingPhysicalInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Case Housing Physical Inspection ID to value
        if intCaseHousingPhysicalInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intCaseHousingPhysicalInspectionID = intCaseHousingPhysicalInspectionID 

    def Append_CasePhysicalIDList(self, intObject):
        """ 
        Function Name: Append_CasePhysicalIDList
        Function Description: This function appends objects to the Case Housing Physical Inspection ID list
        """    
        self.aintCaseHousingPhysicalInspectionID.append(intObject)

    def Remove_CasePhysicalIDList(self, intObject):
        """ 
        Function Name: Remove_CasePhysicalIDList
        Function Description: This function removes objects in the Case Housing Physical Inspection ID list
        """    
        self.aintCaseHousingPhysicalInspectionID.remove(intObject)

    def Get_CasePhysicalIDList_Obj(self):
        """ 
        Function Name: Get_CasePhysicalIDList_Obj
        Function Description: This function gets all the objects in the Case Housing Physical Inspection ID list
        """    
        return self.aintCaseHousingPhysicalInspectionID
                
    def Delete_CasePhysicalInspect_Data(self):
        """ 
        Function Name: Delete_CasePhysicalInspect_Data
        Function Description: This function removes all the objects in the Case Housing Physical Inspection ID class
        """    
        CasePhysicalInspect.aintCaseHousingPhysicalInspectionID = []
        CasePhysicalInspect.aCasePhysInsCache = []

    def Set_CasePhysicalInspect_Data(self):
        """ 
        Function Name: Set_CasePhysicalInspect_Data
        Function Description: This function sets all the objects in the Case Visual Inspection class
        """    
        self.intCaseHousingPhysicalInspectionID = CasePhysicalInspect.aCasePhysInsCache[0]
        self.intCaseCompSelectID = CasePhysicalInspect.aCasePhysInsCache[1]
        self.intInspectionTypeID = CasePhysicalInspect.aCasePhysInsCache[2]
        self.intCasePhysMetalSelectID = CasePhysicalInspect.aCasePhysInsCache[3]
        self.intInspectionStatusID = CasePhysicalInspect.aCasePhysInsCache[4]
        
    def Add_CasePhysicalInspect_Query(self):
        """ 
        Function Name: Add_CasePhysicalInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewCaseHousingPhysicalInspection
        """    
        # Set the class variables before dumping the data to the database
        CasePhysicalInspect.Set_CasePhysicalInspect_Data(self)
                
        # Create the sql query string
        sqlTableCol = ("intCaseHousingPhysicalInspectionID", "intCaseCompSelectID", "intInspectionTypeID", "intCasePhysMetalSelectID", "intInspectionStatusID")     
        sqlTableName = "TCaseHousingPhysicalInspections"
        sqlTableValues = (self.intCaseHousingPhysicalInspectionID, self.intCaseCompSelectID, self.intInspectionTypeID, self.intCasePhysMetalSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)          

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)
        
    def Clear_CasePhysInspect_Attributes(self):
        """ 
        Function Name: Clear_CasePhysInspect_Attributes
        Function Description: This function clears the Case Physical Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intCaseHousingPhysicalInspectionID", "intCaseCompSelectID", "intInspectionTypeID", "intCasePhysMetalSelectID", "intInspectionStatusID")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            
                                            
class StandardCaseInspect(CaseVisualInspect, CasePhysicalInspect):
    """
    Class Name: StandardCaseInspect
    Class Description: This class gets and sets all of the Standard Case Inspection attributes. 
    Pass in the Case Visual and Physical classes. 
    """
    # Create class variable shared amongst all Standard Case Inspection methods
    aintStandardCaseHousingInspectionID = []
    aStandardCaseInsCache = []
        
    # Instantiate the following attributes
    def __init__(self, intStandardCaseHousingInspectionID, intCaseHousingVisualInspectionID, intCaseHousingPhysicalInspectionID):
        self.intStandardCaseHousingInspectionID = intStandardCaseHousingInspectionID
        # Inherits the child class with all the necessary objects
        CaseVisualInspect.__init__(intCaseHousingVisualInspectionID)
        CasePhysicalInspect.__init__(intCaseHousingPhysicalInspectionID)
        
    # Property decorator object get function to access private intStandardCaseHousingInspectionID
    @property
    def intStandardCaseHousingInspectionID(self):
        return self._intStandardCaseHousingInspectionID
    
    # setter method 
    @intStandardCaseHousingInspectionID.setter 
    def intStandardCaseHousingInspectionID(self, intStandardCaseHousingInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intStandardCaseHousingInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intStandardCaseHousingInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intStandardCaseHousingInspectionID = intStandardCaseHousingInspectionID   

    def Append_StandCaseInspectIDList(self, intObject):
        """ 
        Function Name: Append_StandCaseInspectIDList
        Function Description: This function appends objects to the Standard Case Inspection ID list
        """    
        self.aintStandardCaseHousingInspectionID.append(intObject)

    def Remove_StandCaseInspectIDList(self, intObject):
        """ 
        Function Name: Remove_StandCaseInspectIDList
        Function Description: This function removes objects in the Standard Case Inspection ID list
        """    
        self.aintStandardCaseHousingInspectionID.remove(intObject)

    def Get_StandCaseInspectIDList_Obj(self):
        """ 
        Function Name: Get_StandCaseInspectIDList_Obj
        Function Description: This function gets all the objects in the Standard Case Inspection ID list
        """    
        return self.aintStandardCaseHousingInspectionID            
    
    # def Get_MaxStandCaseInspectID(self):
    #     """ 
    #     Function Name: Get_MaxStandCaseInspectID
    #     Function Description: This function gets the max ID inside the TStandardCaseHousingInspections table
    #     """    
    #     # Create the sql query string
    #     sqlQuery = """SELECT MAX(intStandardCaseHousingInspectionID) FROM TStandardCaseHousingInspections"""
    #     QueryID = int(0)

    #     # Execute the query
    #     self.intStandardCaseHousingInspectionID = SQLQueries.Get_SingleValue_Query(sqlQuery, QueryID)

    def Add_StandCaseInspect_Query(self):
        """ 
        Function Name: Add_StandCaseInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewStandardCarabinerInspection
        """    
        # Create the sql query string
        sqlTableNames = ("TStandardCaseHousingInspections")
        sqlTableCol = ("intStandardCaseHousingInspectionID", "intCaseHousingVisualInspectionID", 
                       "intCaseHousingPhysicalInspectionID", "intInspectionStatusID")
        # Set the primary key values from the cached array object
        aPrimKeyValues = [item for item in StandardCaseInspect.aStandardCaseInsCache]

        # Get the visual, physical, and functional status IDs
        VisStatusID = InspectionStatus.astrInspectionStatusDesc.index(BrakeVisSelection.strBrakeVisStatus) + 1
        PhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(CasePhysSelection.strCasePhysStatus) + 1
        aInsStatusID = [VisStatusID, PhysStatusID]

        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(aInsStatusID)

        # Append the AutoBelay Status array 
        AutoBelayInspect.aAutoBelayInspectStatus.append(intOverallStatus)
                 
        # Append the primary key list with the new over status ID
        aPrimKeyValues.append(intOverallStatus)                      
        
        # Set the parameters
        sqlParams = (sqlTableNames, sqlTableCol, tuple(aPrimKeyValues))

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)        
                
    def Delete_StandCaseInspect_Data(self):
        """ 
        Function Name: Delete_StandCaseInspect_Data
        Function Description: This function removes all the objects in the Standard Case Inspection class
        """    
        StandardCaseInspect.aintStandardCaseHousingInspectionID = []
        StandardCaseInspect.aStandardCaseInsCache = []

    def Clear_CaseStandardInspect_Attributes(self):
        """ 
        Function Name: Clear_CaseStandardInspect_Attributes
        Function Description: This function clears the Case Standard Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intStandardCaseHousingInspectionID", "intCaseHousingVisualInspectionID", 
                       "intCaseHousingPhysicalInspectionID", "intInspectionStatusID")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)

    def Reset_Case_Data(self):
        """ 
        Function Name: Reset_Case_Data
        Function Description: This function clears the Case data attributes 
        """  
        # Clear the class attributes
        CaseCompSelection.Clear_CaseCompSel_Attributes(self)
        CaseVisSelection.Clear_CaseVisSel_Attributes(self)
        CaseVisualInspect.Clear_CaseVisInspect_Attributes(self)
        CasePhysSelection.Clear_CasePhysSel_Attributes(self)
        CasePhysicalInspect.Clear_CasePhysInspect_Attributes(self)
        StandardCaseInspect.Clear_CaseStandardInspect_Attributes(self)
                                    
    def Delete_Case_Data(self):
        """ 
        Function Name: Delete_Case_Data
        Function Description: This function clears the Case data arrays 
        """  
        # Clear the class arrays
        CaseCompSelection.Delete_CaseCompSelection_Data(self)
        CaseVisSelection.Delete_CaseVisSelection_Data(self)
        CaseVisualInspect.Delete_CaseVisualInspect_Data(self)
        CasePhysSelection.Delete_CasePhysSelection_Data(self)
        CasePhysicalInspect.Delete_CasePhysicalInspect_Data(self)
        StandardCaseInspect.Delete_StandCaseInspect_Data(self)
                
                                
class BrakeHousing():
    """
    Class Name: BrakeHousing
    Class Description: This class gets and sets all of the Brake Housing attributes. 
    """
    # Create class variable shared amongst all Brake Housing methods
    aintBrakeHousingID = []
    astrBrakeComponentDesc = []    
    
    # Instantiate the following attributes
    def __init__(self, intBrakeHousingID, strBrakeComponentDesc):
        self.intBrakeHousingID = intBrakeHousingID
        self.strBrakeComponentDesc = strBrakeComponentDesc

    # Property decorator object get function to access private intBrakeHousingID
    @property
    def intBrakeHousingID(self):
        return self._intBrakeHousingID

    # Property decorator object get function to access private strBrakeComponentDesc
    @property
    def strBrakeComponentDesc(self):
        return self._strBrakeComponentDesc

    # setter method 
    @intBrakeHousingID.setter 
    def intBrakeHousingID(self, intBrakeHousingID): 
        # Return true if specified object is of int type
        if not isinstance(intBrakeHousingID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intBrakeHousingID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBrakeHousingID = intBrakeHousingID    

    # setter method 
    @strBrakeComponentDesc.setter 
    def strBrakeComponentDesc(self, strBrakeComponentDesc): 
        # Return true if specified object is of str type
        if not isinstance(strBrakeComponentDesc, str): 
            raise TypeError('Housing Description must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if strBrakeComponentDesc.isspace(): 
            raise ValueError('Housing Description cannot be empty') 
        # Set the attribute to the value if true
        elif strBrakeComponentDesc.isascii():
            self._strBrakeComponentDesc = strBrakeComponentDesc

    def Append_BrakeHouseIDList(self, intObject):
        """ 
        Function Name: Append_BrakeHouseIDList
        Function Description: This function appends objects to the Brake House ID list
        """    
        self.aintBrakeHousingID.append(intObject)

    def Remove_BrakeHouseIDList(self, intObject):
        """ 
        Function Name: Remove_BrakeHouseIDList
        Function Description: This function removes objects in the Brake House ID list
        """    
        self.aintBrakeHousingID.remove(intObject)

    def Get_BrakeHouseIDList_Obj(self):
        """ 
        Function Name: Get_BrakeHouseIDList_Obj
        Function Description: This function gets all the objects in the Brake House ID list
        """    
        return self.aintBrakeHousingID            

    def Append_BrakeHouseDescList(self, strObject):
        """ 
        Function Name: Append_BrakeHouseDescList
        Function Description: This function appends objects to the Brake House Description list
        """    
        self.astrBrakeComponentDesc.append(strObject)

    def Remove_BrakeHouseDescList(self, strObject):
        """ 
        Function Name: Remove_BrakeHouseDescList
        Function Description: This function removes objects in the Brake House Description list
        """    
        self.astrBrakeComponentDesc.remove(strObject)

    def Get_BrakeHouseDescList_Obj(self):
        """ 
        Function Name: Get_BrakeHouseDescList_Obj
        Function Description: This function gets all the objects in the Brake House Description list
        """    
        return self.astrBrakeComponentDesc  

    def Get_BrakeHousing_Data(self):
        """ 
        Function Name: Get_BrakeHousing_Data
        Function Description: This function gets all the objects in the Brake Housing table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TBrakeHousings"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the housing Data List
        for i in range(len(QueryResultList)):
            BrakeHousing.Append_BrakeHouseIDList(self, QueryResultList[i][0])
            BrakeHousing.Append_BrakeHouseDescList(self, QueryResultList[i][1]) 
            
    def Delete_BrakeHousing_Data(self):
        """ 
        Function Name: Delete_BrakeHousing_Data
        Function Description: This function removes all the objects in the Housing class
        """    
        BrakeHousing.aintBrakeHousingID = []
        BrakeHousing.astrBrakeComponentDesc = []


class BrakeCompSelection():
    """
    Class Name: BrakeCompSelection
    Class Description: This class gets and sets all of the Brake Component Selections. 
    """
    # Create class variable shared amongst all Brake Component methods
    aintBrakeCompSelectID = []
    astrBrakeCompSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intBrakeCompSelectID, strBrakeCompSelect):
        self.intBrakeCompSelectID = intBrakeCompSelectID
        self.strBrakeCompSelect = strBrakeCompSelect

    # Property decorator object get function to access private intBrakeCompSelectID
    @property
    def intBrakeCompSelectID(self):
        return self._intBrakeCompSelectID

    # Property decorator object get function to access private strBrakeCompSelect
    @property
    def strBrakeCompSelect(self):
        return self._strBrakeCompSelect
        
    # setter method 
    @intBrakeCompSelectID.setter 
    def intBrakeCompSelectID(self, intBrakeCompSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intBrakeCompSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intBrakeCompSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBrakeCompSelectID = intBrakeCompSelectID 
        
    # setter method 
    @strBrakeCompSelect.setter 
    def strBrakeCompSelect(self, strBrakeCompSelect): 
        # Return true if specified object is of str type
        if not isinstance(strBrakeCompSelect, str): 
            raise TypeError('Brake Component input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBrakeCompSelect.isspace(): 
            raise ValueError('Brake Component input cannot be empty') 
        # Set the attribute to the value if true
        elif strBrakeCompSelect.isascii():
            self._strBrakeCompSelect = strBrakeCompSelect
            # Set the global class bool to true
            Bool_Flag.Set_Brake_Bool_Value_True(Bool_Flag)
            
    def Append_BrakeCompIDList(self, intObject):
        """ 
        Function Name: Append_BrakeCompIDList
        Function Description: This function appends objects to the Brake Component Selection ID list
        """    
        self.aintBrakeCompSelectID.append(intObject)

    def Remove_BrakeCompIDList(self, intObject):
        """ 
        Function Name: Remove_BrakeCompIDList
        Function Description: This function removes objects in the Brake Component Selection ID list
        """    
        self.aintBrakeCompSelectID.remove(intObject)

    def Get_BrakeCompIDList_Obj(self):
        """ 
        Function Name: Get_BrakeCompIDList_Obj
        Function Description: This function gets all the objects in the Brake Component Selection ID list
        """    
        return self.aintBrakeCompSelectID
    
    def Append_BrakeCompSelectList(self, strObject):
        """ 
        Function Name: Append_BrakeCompSelectList
        Function Description: This function appends objects to the Brake Component Selection list
        """    
        self.astrBrakeCompSelect.append(strObject)

    def Remove_BrakeCompSelectList(self, strObject):
        """ 
        Function Name: Remove_BrakeCompSelectList
        Function Description: This function removes objects in the Brake Component Selection list
        """    
        self.astrBrakeCompSelect.remove(strObject)

    def Get_BrakeCompSelectList_Obj(self):
        """ 
        Function Name: Get_BrakeCompSelectList_Obj
        Function Description: This function gets all the objects in the Brake Component Selection list
        """    
        return self.astrBrakeCompSelect   
                    
    def Delete_BrakeCompSelection_Data(self):
        """ 
        Function Name: Delete_BrakeCompSelection_Data
        Function Description: This function removes all the objects in the Brake Component Selection class
        """    
        BrakeCompSelection.aintBrakeCompSelectID = []
        BrakeCompSelection.astrBrakeCompSelect = []
        
    def Add_BrakeCompSelection_Query(self):
        """ 
        Function Name: Add_BrakeCompSelection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewBrakeCompSelection
        """    
        # Create the sql query params
        sqlTableCol = ("intBrakeCompSelectID", "strBrakeCompSelect")
        sqlTableName = "TBrakeCompSelects"
        sqlTableValues = (BrakeCompSelection.intBrakeCompSelectID, BrakeCompSelection.strBrakeCompSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)
        
        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)      
        
    def Clear_BrakeCompSel_Attributes(self):
        """ 
        Function Name: Clear_BrakeCompSel_Attributes
        Function Description: This function clears the Brake Comp Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intBrakeCompSelectID", "strBrakeCompSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            
                    
class BrakeVisSelection():
    """
    Class Name: BrakeVisSelection
    Class Description: This class gets and sets all of the Brake Visual Selections. 
    """
    # Create class variable shared amongst all Brake visual methods
    aintBrakeVisMetalSelectID = []
    astrBrakeVisMetSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intBrakeVisMetalSelectID, strBrakeVisMetSelect, strBrakeVisStatus):
        self.intBrakeVisMetalSelectID = intBrakeVisMetalSelectID
        self.strBrakeVisMetSelect = strBrakeVisMetSelect
        self.strBrakeVisStatus = strBrakeVisStatus

    # Property decorator object get function to access private intBrakeVisMetalSelectID
    @property
    def intBrakeVisMetalSelectID(self):
        return self._intBrakeVisMetalSelectID

    # Property decorator object get function to access private strBrakeVisMetSelect
    @property
    def strBrakeVisMetSelect(self):
        return self._strBrakeVisMetSelect

    # Property decorator object get function to access private strBrakeVisStatus
    @property
    def strBrakeVisStatus(self):
        return self._strBrakeVisStatus
            
    # setter method 
    @intBrakeVisMetalSelectID.setter 
    def intBrakeVisMetalSelectID(self, intBrakeVisMetalSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intBrakeVisMetalSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intBrakeVisMetalSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBrakeVisMetalSelectID = intBrakeVisMetalSelectID 
        
    # setter method 
    @strBrakeVisMetSelect.setter 
    def strBrakeVisMetSelect(self, strBrakeVisMetSelect): 
        # Return true if specified object is of str type
        if not isinstance(strBrakeVisMetSelect, str): 
            raise TypeError('Brake visual input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBrakeVisMetSelect.isspace(): 
            raise ValueError('Brake visual input cannot be empty') 
        # Set the attribute to the value if true
        elif strBrakeVisMetSelect.isascii():
            self._strBrakeVisMetSelect = strBrakeVisMetSelect

    # setter method 
    @strBrakeVisStatus.setter 
    def strBrakeVisStatus(self, strBrakeVisStatus): 
        # Return true if specified object is of str type
        if not isinstance(strBrakeVisStatus, str): 
            raise TypeError('Brake visual status must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBrakeVisStatus.isspace(): 
            raise ValueError('Brake visual status cannot be empty') 
        # Set the attribute to the value if true
        elif strBrakeVisStatus.isascii():
            self._strBrakeVisStatus = strBrakeVisStatus

    def Append_BrakeVisIDList(self, intObject):
        """ 
        Function Name: Append_BrakeVisIDList
        Function Description: This function appends objects to the Brake Visual Selection ID list
        """    
        self.aintBrakeVisMetalSelectID.append(intObject)

    def Remove_BrakeVisIDList(self, intObject):
        """ 
        Function Name: Remove_BrakeVisIDList
        Function Description: This function removes objects in the Brake Visual Selection ID list
        """    
        self.aintBrakeVisMetalSelectID.remove(intObject)

    def Get_BrakeVisIDList_Obj(self):
        """ 
        Function Name: Get_BrakeVisIDList_Obj
        Function Description: This function gets all the objects in the Brake Visual Selection ID list
        """    
        return self.aintBrakeVisMetalSelectID
    
    def Append_BrakeVisSelectList(self, strObject):
        """ 
        Function Name: Append_BrakeVisSelectList
        Function Description: This function appends objects to the Brake Visual Selection list
        """    
        self.astrBrakeVisMetSelect.append(strObject)

    def Remove_BrakeVisSelectList(self, strObject):
        """ 
        Function Name: Remove_BrakeVisSelectList
        Function Description: This function removes objects in the Brake Visual Selection list
        """    
        self.astrBrakeVisMetSelect.remove(strObject)

    def Get_BrakeVisSelectList_Obj(self):
        """ 
        Function Name: Get_BrakeVisSelectList_Obj
        Function Description: This function gets all the objects in the Brake Visual Selection list
        """    
        return self.astrBrakeVisMetSelect   
                    
    def Delete_BrakeVisSelectList_Data(self):
        """ 
        Function Name: Delete_BrakeVisSelectList_Data
        Function Description: This function removes all the objects in the Brake Visual Selection class
        """    
        BrakeVisSelection.aintBrakeVisMetalSelectID = []
        BrakeVisSelection.astrBrakeVisMetSelect = []
        
    def Add_BrakeVisSelectList_Query(self):
        """ 
        Function Name: Add_BrakeVisSelectList_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewBrakeVisSelection
        """    
        # Create the sql query params
        sqlTableCol = ("intBrakeVisMetalSelectID", "strBrakeVisMetSelect")
        sqlTableName = "TBrakeVisMetalSelects"
        sqlTableValues = (BrakeVisSelection.intBrakeVisMetalSelectID, BrakeVisSelection.strBrakeVisMetSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)
        
        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)   

    def Clear_BrakeVisSel_Attributes(self):
        """ 
        Function Name: Clear_BrakeVisSel_Attributes
        Function Description: This function clears the Brake Visual Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intBrakeVisMetalSelectID", "strBrakeVisMetSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                                    
                    
class BrakeVisualInspect(BrakeCompSelection, InspectionType, BrakeVisSelection, InspectionStatus):
    """
    Class Name: BrakeVisualInspect
    Class Description: This class gets and sets all of the Brake Housing Visual Inspection attributes. 
    """
    # Create class variable shared amongst all Brake Housing Visual Inspection methods
    aintBrakeHousingVisualInspectionID = []
    aBrakeVisInsCache = []
        
    # Instantiate the following attributes
    def __init__(self, intBrakeHousingVisualInspectionID, intBrakeCompSelectID, intInspectionTypeID, intBrakeVisMetalSelectID, intInspectionStatusID):
        self.intBrakeHousingVisualInspectionID = intBrakeHousingVisualInspectionID
        # Inherits the child class with all the necessary objects
        BrakeCompSelection.__init__(intBrakeCompSelectID)
        InspectionType.__init__(intInspectionTypeID)
        BrakeVisSelection.__init__(intBrakeVisMetalSelectID)
        InspectionStatus.__init__(intInspectionStatusID)

    # Property decorator object get function to access private intBrakeHousingVisualInspectionID
    @property
    def intBrakeHousingVisualInspectionID(self):
        return self._intBrakeHousingVisualInspectionID

    # setter method 
    @intBrakeHousingVisualInspectionID.setter 
    def intBrakeHousingVisualInspectionID(self, intBrakeHousingVisualInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intBrakeHousingVisualInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Brake Housing Visual Inspection ID to value
        if intBrakeHousingVisualInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBrakeHousingVisualInspectionID = intBrakeHousingVisualInspectionID 

    def Append_BrakeVisualIDList(self, intObject):
        """ 
        Function Name: Append_BrakeVisualIDList
        Function Description: This function appends objects to the Brake Housing Visual Inspection ID list
        """    
        self.aintBrakeHousingVisualInspectionID.append(intObject)

    def Remove_BrakeVisualIDList(self, intObject):
        """ 
        Function Name: Remove_BrakeVisualIDList
        Function Description: This function removes objects in the Brake Housing Visual Inspection ID list
        """    
        self.aintBrakeHousingVisualInspectionID.remove(intObject)

    def Get_BrakeVisualIDList_Obj(self):
        """ 
        Function Name: Get_BrakeVisualIDList_Obj
        Function Description: This function gets all the objects in the Brake Housing Visual Inspection ID list
        """    
        return self.aintBrakeHousingVisualInspectionID
                
    def Delete_BrakeVisualInspect_Data(self):
        """ 
        Function Name: Delete_BrakeVisualInspect_Data
        Function Description: This function removes all the objects in the Brake Housing Visual Inspection ID class
        """    
        BrakeVisualInspect.aintBrakeHousingVisualInspectionID = []
        BrakeVisualInspect.aBrakeVisInsCache = []

    def Set_BrakeVisualInspect_Data(self):
        """ 
        Function Name: Set_BrakeVisualInspect_Data
        Function Description: This function sets all the objects in the Brake Visual Inspection class
        """    
        self.intBrakeHousingVisualInspectionID = BrakeVisualInspect.aBrakeVisInsCache[0]
        self.intBrakeCompSelectID = BrakeVisualInspect.aBrakeVisInsCache[1]
        self.intInspectionTypeID = BrakeVisualInspect.aBrakeVisInsCache[2]
        self.intBrakeVisMetalSelectID = BrakeVisualInspect.aBrakeVisInsCache[3]
        self.intInspectionStatusID = BrakeVisualInspect.aBrakeVisInsCache[4]
        
    def Add_BrakeVisualInspect_Query(self):
        """ 
        Function Name: Add_BrakeVisualInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewBrakeHousingVisualInspection
        """    
        # Set the class variables before dumping the data to the database
        BrakeVisualInspect.Set_BrakeVisualInspect_Data(self)
                
        # Create the sql query string
        sqlTableCol = ("intBrakeHousingVisualInspectionID", "intBrakeCompSelectID", "intInspectionTypeID", "intBrakeVisMetalSelectID", "intInspectionStatusID")     
        sqlTableName = "TBrakeHousingVisualInspections"
        sqlTableValues = (self.intBrakeHousingVisualInspectionID, self.intBrakeCompSelectID, self.intInspectionTypeID, self.intBrakeVisMetalSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)           

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)
        
    def Clear_BrakeVisInspect_Attributes(self):
        """ 
        Function Name: Clear_BrakeVisInspect_Attributes
        Function Description: This function clears the Brake Visual Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intBrakeHousingVisualInspectionID", "intBrakeCompSelectID", "intInspectionTypeID", "intBrakeVisMetalSelectID", "intInspectionStatusID")     
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            
            
class BrakePhysSelection():
    """
    Class Name: BrakePhysSelection
    Class Description: This class gets and sets all of the Brake Physical Selections. 
    """
    # Create class variable shared amongst all Brake Physical methods
    aintBrakePhysMetalSelectID = []
    astrBrakePhysMetSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intBrakePhysMetalSelectID, strBrakePhysMetSelect, strBrakePhysStatus):
        self.intBrakePhysMetalSelectID = intBrakePhysMetalSelectID
        self.strBrakePhysMetSelect = strBrakePhysMetSelect
        self.strBrakePhysStatus = strBrakePhysStatus

    # Property decorator object get function to access private intBrakePhysMetalSelectID
    @property
    def intBrakePhysMetalSelectID(self):
        return self._intBrakePhysMetalSelectID

    # Property decorator object get function to access private strBrakePhysMetSelect
    @property
    def strBrakePhysMetSelect(self):
        return self._strBrakePhysMetSelect

    # Property decorator object get function to access private strBrakePhysStatus
    @property
    def strBrakePhysStatus(self):
        return self._strBrakePhysStatus
            
    # setter method 
    @intBrakePhysMetalSelectID.setter 
    def intBrakePhysMetalSelectID(self, intBrakePhysMetalSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intBrakePhysMetalSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intBrakePhysMetalSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBrakePhysMetalSelectID = intBrakePhysMetalSelectID 
        
    # setter method 
    @strBrakePhysMetSelect.setter 
    def strBrakePhysMetSelect(self, strBrakePhysMetSelect): 
        # Return true if specified object is of str type
        if not isinstance(strBrakePhysMetSelect, str): 
            raise TypeError('Brake physical input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBrakePhysMetSelect.isspace(): 
            raise ValueError('Brake physical input cannot be empty') 
        # Set the attribute to the value if true
        elif strBrakePhysMetSelect.isascii():
            self._strBrakePhysMetSelect = strBrakePhysMetSelect

    # setter method 
    @strBrakePhysStatus.setter 
    def strBrakePhysStatus(self, strBrakePhysStatus): 
        # Return true if specified object is of str type
        if not isinstance(strBrakePhysStatus, str): 
            raise TypeError('Brake physical input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBrakePhysStatus.isspace(): 
            raise ValueError('Brake physical input cannot be empty') 
        # Set the attribute to the value if true
        elif strBrakePhysStatus.isascii():
            self._strBrakePhysStatus = strBrakePhysStatus

    def Append_BrakePhysIDList(self, intObject):
        """ 
        Function Name: Append_BrakePhysIDList
        Function Description: This function appends objects to the Brake Physical Selection ID list
        """    
        self.aintBrakePhysMetalSelectID.append(intObject)

    def Remove_BrakePhysIDList(self, intObject):
        """ 
        Function Name: Remove_BrakePhysIDList
        Function Description: This function removes objects in the Brake Physical Selection ID list
        """    
        self.aintBrakePhysMetalSelectID.remove(intObject)

    def Get_BrakePhysIDList_Obj(self):
        """ 
        Function Name: Get_BrakePhysIDList_Obj
        Function Description: This function gets all the objects in the Brake Visual Selection ID list
        """    
        return self.aintBrakePhysMetalSelectID
    
    def Append_BrakePhysSelectList(self, strObject):
        """ 
        Function Name: Append_BrakePhysSelectList
        Function Description: This function appends objects to the Brake Visual Selection list
        """    
        self.astrBrakePhysMetSelect.append(strObject)

    def Remove_BrakePhysSelectList(self, strObject):
        """ 
        Function Name: Remove_BrakePhysSelectList
        Function Description: This function removes objects in the Brake Visual Selection list
        """    
        self.astrBrakePhysMetSelect.remove(strObject)

    def Get_BrakePhysSelectList_Obj(self):
        """ 
        Function Name: Get_BrakePhysSelectList_Obj
        Function Description: This function gets all the objects in the Brake Visual Selection list
        """    
        return self.astrBrakePhysMetSelect   
                    
    def Delete_BrakePhysSelectList_Data(self):
        """ 
        Function Name: Delete_BrakePhysSelectList_Data
        Function Description: This function removes all the objects in the Brake Visual Selection class
        """    
        BrakePhysSelection.aintBrakePhysMetalSelectID = []
        BrakePhysSelection.astrBrakePhysMetSelect = []
        
    def Add_BrakePhysSelectList_Query(self):
        """ 
        Function Name: Add_BrakePhysSelectList_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewBrakePhysSelection
        """    
        # Create the sql query params
        sqlTableCol = ("intBrakePhysMetalSelectID", "strBrakePhysMetSelect")
        sqlTableName = "TBrakePhysMetalSelects"
        sqlTableValues = (BrakePhysSelection.intBrakePhysMetalSelectID, BrakePhysSelection.strBrakePhysMetSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)
        
        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Clear_BrakePhysSel_Attributes(self):
        """ 
        Function Name: Clear_BrakePhysSel_Attributes
        Function Description: This function clears the Brake Physical Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intBrakePhysMetalSelectID", "strBrakePhysMetSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                    
        
class BrakePhysicalInspect(BrakeCompSelection, InspectionType, BrakePhysSelection, InspectionStatus):
    """
    Class Name: BrakePhysicalInspect
    Class Description: This class gets and sets all of the Brake Housing Physical Inspection attributes. 
    """
    # Create class variable shared amongst all Brake Housing Physical Inspection methods
    aintBrakeHousingPhysicalInspectionID = []
    aBrakePhysInsCache = []
        
    # Instantiate the following attributes
    def __init__(self, intBrakeHousingPhysicalInspectionID, intBrakeCompSelectID, intInspectionTypeID, intBrakePhysMetalSelectID, intInspectionStatusID):
        self.intBrakeHousingPhysicalInspectionID = intBrakeHousingPhysicalInspectionID
        # Inherits the child class with all the necessary objects
        BrakeCompSelection.__init__(intBrakeCompSelectID)
        InspectionType.__init__(intInspectionTypeID)
        BrakePhysSelection.__init__(intBrakePhysMetalSelectID)
        InspectionStatus.__init__(intInspectionStatusID)

    # Property decorator object get function to access private intBrakeHousingPhysicalInspectionID
    @property
    def intBrakeHousingPhysicalInspectionID(self):
        return self._intBrakeHousingPhysicalInspectionID

    # setter method 
    @intBrakeHousingPhysicalInspectionID.setter 
    def intBrakeHousingPhysicalInspectionID(self, intBrakeHousingPhysicalInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intBrakeHousingPhysicalInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Brake Housing Visual Inspection ID to value
        if intBrakeHousingPhysicalInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBrakeHousingPhysicalInspectionID = intBrakeHousingPhysicalInspectionID 

    def Append_BrakePhysicalIDList(self, intObject):
        """ 
        Function Name: Append_BrakePhysicalIDList
        Function Description: This function appends objects to the Brake Housing Physical Inspection ID list
        """    
        self.aintBrakeHousingPhysicalInspectionID.append(intObject)

    def Remove_BrakePhysicalIDList(self, intObject):
        """ 
        Function Name: Remove_BrakePhysicalIDList
        Function Description: This function removes objects in the Brake Housing Physical Inspection ID list
        """    
        self.aintBrakeHousingPhysicalInspectionID.remove(intObject)

    def Get_BrakePhysicalIDList_Obj(self):
        """ 
        Function Name: Get_BrakePhysicalIDList_Obj
        Function Description: This function gets all the objects in the Brake Housing Physical Inspection ID list
        """    
        return self.aintBrakeHousingPhysicalInspectionID
                
    def Delete_BrakePhysicalInspect_Data(self):
        """ 
        Function Name: Delete_BrakePhysicalInspect_Data
        Function Description: This function removes all the objects in the Brake Housing Physical Inspection ID class
        """    
        BrakePhysicalInspect.aintBrakeHousingPhysicalInspectionID = []
        BrakePhysicalInspect.aBrakePhysInsCache = []

    def Set_BrakePhysicalInspect_Data(self):
        """ 
        Function Name: Set_BrakePhysicalInspect_Data
        Function Description: This function sets all the objects in the Case Visual Inspection class
        """    
        self.intBrakeHousingPhysicalInspectionID = BrakePhysicalInspect.aBrakePhysInsCache[0]
        self.intBrakeCompSelectID = BrakePhysicalInspect.aBrakePhysInsCache[1]
        self.intInspectionTypeID = BrakePhysicalInspect.aBrakePhysInsCache[2]
        self.intBrakePhysMetalSelectID = BrakePhysicalInspect.aBrakePhysInsCache[3]
        self.intInspectionStatusID = BrakePhysicalInspect.aBrakePhysInsCache[4]
        
    def Add_BrakePhysicalInspect_Query(self):
        """ 
        Function Name: Add_BrakePhysicalInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewBrakeHousingPhysicalInspection
        """    
        # Set the class variables before dumping the data to the database
        BrakePhysicalInspect.Set_BrakePhysicalInspect_Data(self)
                
        # Create the sql query string
        sqlTableCol = ("intBrakeHousingPhysicalInspectionID", "intBrakeCompSelectID", "intInspectionTypeID", "intBrakePhysMetalSelectID", "intInspectionStatusID")     
        sqlTableName = "TBrakeHousingPhysicalInspections"
        sqlTableValues = (self.intBrakeHousingPhysicalInspectionID, self.intBrakeCompSelectID, self.intInspectionTypeID, self.intBrakePhysMetalSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)           

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Clear_BrakePhysInspect_Attributes(self):
        """ 
        Function Name: Clear_BrakePhysInspect_Attributes
        Function Description: This function clears the Brake Physical Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intBrakeHousingPhysicalInspectionID", "intBrakeCompSelectID", "intInspectionTypeID", "intBrakePhysMetalSelectID", "intInspectionStatusID")     
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                    
                                
class StandardBrakeInspect(BrakeVisualInspect, BrakePhysicalInspect):
    """
    Class Name: StandardBrakeInspect
    Class Description: This class gets and sets all of the Standard Brake Housing Inspection attributes. 
    Pass in the Brake Visual and Physical classes. 
    """
    # Create class variable shared amongst all Standard Brake Housing methods
    aintStandardBrakeHousingInspectionID = []
    aStandardBrakeInsCache = []
    
    # Instantiate the following attributes
    def __init__(self, intStandardBrakeHousingInspectionID, intBrakeHousingVisualInspectionID, intBrakeHousingPhysicalInspectionID):
        self.intStandardBrakeHousingInspectionID = intStandardBrakeHousingInspectionID
        # Inherits the child class with all the necessary objects
        BrakeVisualInspect.__init__(intBrakeHousingVisualInspectionID)
        BrakePhysicalInspect.__init__(intBrakeHousingPhysicalInspectionID)
        
    # Property decorator object get function to access private intStandardBrakeHousingInspectionID
    @property
    def intStandardBrakeHousingInspectionID(self):
        return self._intStandardBrakeHousingInspectionID
    
    # setter method 
    @intStandardBrakeHousingInspectionID.setter 
    def intStandardBrakeHousingInspectionID(self, intStandardBrakeHousingInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intStandardBrakeHousingInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intStandardBrakeHousingInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intStandardBrakeHousingInspectionID = intStandardBrakeHousingInspectionID    

    def Append_StandBrakeInspectIDList(self, intObject):
        """ 
        Function Name: Append_StandBrakeInspectIDList
        Function Description: This function appends objects to the Standard Brake Inspection ID list
        """    
        self.aintStandardBrakeHousingInspectionID.append(intObject)

    def Remove_StandBrakeInspectIDList(self, intObject):
        """ 
        Function Name: Remove_StandBrakeInspectIDList
        Function Description: This function removes objects in the Standard Brake Inspection ID list
        """    
        self.aintStandardBrakeHousingInspectionID.remove(intObject)

    def Get_StandBrakeInspectIDList_Obj(self):
        """ 
        Function Name: Get_StandBrakeInspectIDList_Obj
        Function Description: This function gets all the objects in the Standard Brake Inspection ID list
        """    
        return self.aintStandardBrakeHousingInspectionID            

    def Add_StandBrakeInspect_Query(self):
        """ 
        Function Name: Add_StandBrakeInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewStandardCarabinerInspection
        """    
        # Create the sql query string
        sqlTableNames = ("TStandardBrakeHousingInspections")
        sqlTableCol = ("intStandardBrakeHousingInspectionID", "intBrakeHousingVisualInspectionID", 
                       "intBrakeHousingPhysicalInspectionID", "intInspectionStatusID")
        # Set the primary key values from the cached array object
        aPrimKeyValues = [item for item in StandardBrakeInspect.aStandardBrakeInsCache]

        # Get the visual, physical, and functional status IDs
        VisStatusID = InspectionStatus.astrInspectionStatusDesc.index(BrakeVisSelection.strBrakeVisStatus) + 1
        PhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(BrakePhysSelection.strBrakePhysStatus) + 1
        aInsStatusID = [VisStatusID, PhysStatusID]

        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(aInsStatusID)

        # Append the AutoBelay Status array 
        AutoBelayInspect.aAutoBelayInspectStatus.append(intOverallStatus)
                 
        # Append the primary key list with the new over status ID
        aPrimKeyValues.append(intOverallStatus)                      
        
        # Set the parameters
        sqlParams = (sqlTableNames, sqlTableCol, tuple(aPrimKeyValues))

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)        
                
    def Delete_StandBrakeInspect_Data(self):
        """ 
        Function Name: Delete_StandHousingInspect_Data
        Function Description: This function removes all the objects in the Standard Housing Inspection class
        """    
        StandardBrakeInspect.aStandardBrakeInsCache = []
        StandardBrakeInspect.aStandardBrakeInsCache = []
        
    def Clear_BrakeStandardInspect_Attributes(self):
        """ 
        Function Name: Clear_BrakeStandardInspect_Attributes
        Function Description: This function clears the Brake Standard Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intStandardBrakeHousingInspectionID", "intBrakeHousingVisualInspectionID", 
                       "intBrakeHousingPhysicalInspectionID", "intInspectionStatusID")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)      

    def Reset_Brake_Data(self):
        """ 
        Function Name: Reset_Brake_Data
        Function Description: This function clears the Brake data attributes 
        """  
        # Clear the class attributes
        BrakeCompSelection.Clear_BrakeCompSel_Attributes(self)
        BrakeVisSelection.Clear_BrakeVisSel_Attributes(self)
        BrakeVisualInspect.Clear_BrakeVisInspect_Attributes(self)
        BrakePhysSelection.Clear_BrakePhysSel_Attributes(self)
        BrakePhysicalInspect.Clear_BrakePhysInspect_Attributes(self)
        StandardBrakeInspect.Clear_BrakeStandardInspect_Attributes(self)
                       
    def Delete_Brake_Data(self):
        """ 
        Function Name: Delete_Brake_Data
        Function Description: This function clears the Brake data arrays 
        """  
        # Clear the class arrays
        BrakeCompSelection.Delete_BrakeCompSelection_Data(self) 
        BrakeVisSelection.Delete_BrakeVisSelectList_Data(self)
        BrakeVisualInspect.Delete_BrakeVisualInspect_Data(self)
        BrakePhysSelection.Delete_BrakePhysSelectList_Data(self)
        BrakePhysicalInspect.Delete_BrakePhysicalInspect_Data(self)
        StandardBrakeInspect.Delete_StandBrakeInspect_Data(self)


class Lanyard():
    """
    Class Name: Lanyard
    Class Description: This class gets and sets all of the Lanyard attributes. 
    """
    # Create class variable shared amongst all Lanyard methods
    aintLanyardID = []
    astrLanyardLength = []   
    aLanyardLenCache = []
        
    # Instantiate the following attributes
    def __init__(self, intLanyardID, strLanyardLength):
        self.intLanyardID = intLanyardID
        self.strLanyardLength = strLanyardLength

    # Property decorator object get function to access private intLanyardID
    @property
    def intLanyardID(self):
        return self._intLanyardID

    # Property decorator object get function to access private strLanyardLength
    @property
    def strLanyardLength(self):
        return self._strLanyardLength
    
    # setter method 
    @intLanyardID.setter 
    def intLanyardID(self, intLanyardID): 
        # Return true if specified object is of int type
        if not isinstance(intLanyardID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intLanyardID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intLanyardID = intLanyardID    

    # setter method 
    @strLanyardLength.setter 
    def strLanyardLength(self, strLanyardLength): 
        # Return true if specified object is of str type
        if not isinstance(strLanyardLength, str): 
            raise TypeError('State must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strLanyardLength.isspace(): 
            raise ValueError('State cannot be empty') 
        # Set the attribute to the value if true
        elif strLanyardLength.isalnum():
            self._strLanyardLength = strLanyardLength
            # Set the global class bool to true
            Bool_Flag.Set_Lanyard_Bool_Value_True(Bool_Flag)
       
    def Append_LanyardIDList(self, intObject):
        """ 
        Function Name: Append_LanyardIDList
        Function Description: This function appends objects to the Lanyard ID list
        """    
        self.aintLanyardID.append(intObject)

    def Remove_LanyardIDList(self, intObject):
        """ 
        Function Name: Remove_LanyardIDList
        Function Description: This function removes objects in the Lanyard ID list
        """    
        self.aintLanyardID.remove(intObject)

    def Get_LanyardIDList_Obj(self):
        """ 
        Function Name: Get_LanyardIDList_Obj
        Function Description: This function gets all the objects in the Lanyard ID list
        """    
        return self.aintLanyardID            

    def Append_LanyardLengthList(self, strObject):
        """ 
        Function Name: Append_LanyardLengthList
        Function Description: This function appends objects to the Lanyard Length list
        """    
        self.astrLanyardLength.append(strObject)

    def Remove_LanyardLengthList(self, strObject):
        """ 
        Function Name: Remove_LanyardLengthList
        Function Description: This function removes objects in the Lanyard Length list
        """    
        self.astrLanyardLength.remove(strObject)

    def Get_LanyardLengthList_Obj(self):
        """ 
        Function Name: Get_LanyardLengthList_Obj
        Function Description: This function gets all the objects in the Lanyard Length list
        """    
        return self.astrLanyardLength.sort() 
            
    def Get_Lanyard_Data(self):
        """ 
        Function Name: Get_Lanyard_Data
        Function Description: This function gets all the objects in the Lanyard table
        """    
        # Create the sql query string
        sqlQuery = "SELECT * FROM TLanyards"
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the State Data List
        for i in range(len(QueryResultList)):
            Lanyard.Append_LanyardIDList(self, QueryResultList[i][0])
            Lanyard.Append_LanyardLengthList(self, QueryResultList[i][1]) 
        Lanyard.aintLanyardID.sort()
        Lanyard.astrLanyardLength.sort()   

    def Check_LanLen_Dup(self):
        """ 
        Function Name: Check_LanLen_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        Lanyard Length selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intLanyardID", "strLanyardLength")   
        sqlTableName = "TLanyards"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strLanyardLength in sqlDupValues[i]:
                self.intLanyardID = sqlDupValues[i][0]
                self.strLanyardLength = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag
    
    def Add_LanyardLen_Query(self):
        """ 
        Function Name: Add_LanyardLen_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewLanyardLen
        """    
        # Create the sql query string
        sqlTableCol = ("intLanyardID", "strLanyardLength")   
        sqlTableName = "TLanyards"  
        sqlTableValues = (self.intLanyardID, self.strLanyardLength)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)
        
    def Delete_Lanyard_Data(self):
        """ 
        Function Name: Delete_Lanyard_Data
        Function Description: This function removes all the objects in the Lanyard class
        """   
        Lanyard.aintLanyardID = []
        Lanyard.astrLanyardLength = []


class RetractorFunct():
    """
    Class Name: RetractorFunct
    Class Description: This class gets and sets all of the RetractorFunct attributes. 
    """
    # Create class variable shared amongst all RetractorFunct methods
    aintRetractFunctionID = []
    astrRetractFunctionDesc = []   
        
    # Instantiate the following attributes
    def __init__(self, intRetractFunctionID, strRetractFunctionDesc):
        self.intRetractFunctionID = intRetractFunctionID
        self.strRetractFunctionDesc = strRetractFunctionDesc

    # Property decorator object get function to access private intRetractFunctionID
    @property
    def intRetractFunctionID(self):
        return self._intRetractFunctionID

    # Property decorator object get function to access private strRetractFunctionDesc
    @property
    def strRetractFunctionDesc(self):
        return self._strRetractFunctionDesc
    
    # setter method 
    @intRetractFunctionID.setter 
    def intRetractFunctionID(self, intRetractFunctionID): 
        # Return true if specified object is of int type
        if not isinstance(intRetractFunctionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intRetractFunctionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intRetractFunctionID = intRetractFunctionID    

    # setter method 
    @strRetractFunctionDesc.setter 
    def strRetractFunctionDesc(self, strRetractFunctionDesc): 
        # Return true if specified object is of str type
        if not isinstance(strRetractFunctionDesc, str): 
            raise TypeError('State must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if strRetractFunctionDesc.isspace(): 
            raise ValueError('State cannot be empty') 
        # Set the attribute to the value if true
        elif strRetractFunctionDesc.isascii():
            self._strRetractFunctionDesc = strRetractFunctionDesc
       
    def Append_RetractFunctIDList(self, intObject):
        """ 
        Function Name: Append_RetractFunctIDList
        Function Description: This function appends objects to the RetractorFunct ID list
        """    
        self.aintRetractFunctionID.append(intObject)

    def Remove_RetractFunctIDList(self, intObject):
        """ 
        Function Name: Remove_RetractFunctIDList
        Function Description: This function removes objects in the RetractorFunct ID list
        """    
        self.aintRetractFunctionID.remove(intObject)

    def Get_RetractFunctIDList_Obj(self):
        """ 
        Function Name: Get_RetractFunctIDList_Obj
        Function Description: This function gets all the objects in the RetractorFunct ID list
        """    
        return self.aintRetractFunctionID            

    def Append_RetractFunctDescList(self, strObject):
        """ 
        Function Name: Append_RetractFunctDescList
        Function Description: This function appends objects to the RetractorFunct Description list
        """    
        self.astrRetractFunctionDesc.append(strObject)

    def Remove_RetractFunctDescList(self, strObject):
        """ 
        Function Name: Remove_RetractFunctDescList
        Function Description: This function removes objects in the RetractorFunct Description list
        """    
        self.astrRetractFunctionDesc.remove(strObject)

    def Get_RetractFunctDescList_Obj(self):
        """ 
        Function Name: Get_RetractFunctDescList_Obj
        Function Description: This function gets all the objects in the RetractorFunct Description list
        """    
        return self.astrRetractFunctionDesc       
            
    def Get_RetractFunct_Data(self):
        """ 
        Function Name: Get_RetractFunct_Data
        Function Description: This function gets all the objects in the RetractorFunct table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TRetractFunctions"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the State Data List
        for i in range(len(QueryResultList)):
            RetractorFunct.Append_RetractFunctIDList(self, QueryResultList[i][0])
            RetractorFunct.Append_RetractFunctDescList(self, QueryResultList[i][1]) 

    def Delete_RetractFunct_Data(self):
        """ 
        Function Name: Delete_RetractFunct_Data
        Function Description: This function removes all the objects in the RetractFunct class
        """   
        RetractorFunct.aintRetractFunctionID = []
        RetractorFunct.astrRetractFunctionDesc = []
                

class LanyardVisSelection():
    """
    Class Name: LanyardVisSelection
    Class Description: This class gets and sets all of the Lanyard Visual Selections. 
    """
    # Create class variable shared amongst all Lanyard visual methods
    aintLanVisTextSelectID = []
    astrLanVisTextSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intLanVisTextSelectID, strLanVisTextSelect, strLanVisStatus):
        self.intLanVisTextSelectID = intLanVisTextSelectID
        self.strLanVisTextSelect = strLanVisTextSelect
        self.strLanVisStatus = strLanVisStatus

    # Property decorator object get function to access private intLanVisTextSelectID
    @property
    def intLanVisTextSelectID(self):
        return self._intLanVisTextSelectID

    # Property decorator object get function to access private strLanVisTextSelect
    @property
    def strLanVisTextSelect(self):
        return self._strLanVisTextSelect

    # Property decorator object get function to access private strLanVisStatus
    @property
    def strLanVisStatus(self):
        return self._strLanVisStatus
            
    # setter method 
    @intLanVisTextSelectID.setter 
    def intLanVisTextSelectID(self, intLanVisTextSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intLanVisTextSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intLanVisTextSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intLanVisTextSelectID = intLanVisTextSelectID 
        
    # setter method 
    @strLanVisTextSelect.setter 
    def strLanVisTextSelect(self, strLanVisTextSelect): 
        # Return true if specified object is of str type
        if not isinstance(strLanVisTextSelect, str): 
            raise TypeError('Lanyard visual input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strLanVisTextSelect.isspace(): 
            raise ValueError('Lanyard visual input cannot be empty') 
        # Set the attribute to the value if true
        elif strLanVisTextSelect.isascii():
            self._strLanVisTextSelect = strLanVisTextSelect

    # setter method 
    @strLanVisStatus.setter 
    def strLanVisStatus(self, strLanVisStatus): 
        # Return true if specified object is of str type
        if not isinstance(strLanVisStatus, str): 
            raise TypeError('Lanyard visual status input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strLanVisStatus.isspace(): 
            raise ValueError('Lanyard visual status input cannot be empty') 
        # Set the attribute to the value if true
        elif strLanVisStatus.isascii():
            self._strLanVisStatus = strLanVisStatus

    def Append_LanyardVisIDList(self, intObject):
        """ 
        Function Name: Append_LanyardVisIDList
        Function Description: This function appends objects to the Lanyard Visual Selection ID list
        """    
        self.aintLanVisTextSelectID.append(intObject)

    def Remove_LanyardVisIDList(self, intObject):
        """ 
        Function Name: Remove_LanyardVisIDList
        Function Description: This function removes objects in the Lanyard Visual Selection ID list
        """    
        self.aintLanVisTextSelectID.remove(intObject)

    def Get_LanyardVisIDList_Obj(self):
        """ 
        Function Name: Get_LanyardVisIDList_Obj
        Function Description: This function gets all the objects in the Lanyard Visual Selection ID list
        """    
        return self.aintLanVisTextSelectID
    
    def Append_LanyardVisSelectList(self, strObject):
        """ 
        Function Name: Append_LanyardVisSelectList
        Function Description: This function appends objects to the Lanyard Visual Selection list
        """    
        self.astrLanVisTextSelect.append(strObject)

    def Remove_LanyardVisSelectList(self, strObject):
        """ 
        Function Name: Remove_LanyardVisSelectList
        Function Description: This function removes objects in the Lanyard Visual Selection list
        """    
        self.astrLanVisTextSelect.remove(strObject)

    def Get_LanyardVisSelectList_Obj(self):
        """ 
        Function Name: Get_LanyardVisSelectList_Obj
        Function Description: This function gets all the objects in the Lanyard Visual Selection list
        """    
        return self.astrLanVisTextSelect   
                    
    def Delete_LanyardVisSelectList_Data(self):
        """ 
        Function Name: Delete_LanyardVisSelectList_Data
        Function Description: This function removes all the objects in the Lanyard Visual Selection class
        """    
        LanyardVisSelection.aintLanVisTextSelectID = []
        LanyardVisSelection.astrLanVisTextSelect = []

    def Check_LanVisSelection_Dup(self):
        """ 
        Function Name: Check_LanVisSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        lanyard visual selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intLanVisTextSelectID", "strLanVisTextSelect")   
        sqlTableName = "TLanVisTextSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strLanVisTextSelect in sqlDupValues[i]:
                self.intLanVisTextSelectID = sqlDupValues[i][0]
                self.strLanVisTextSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag
            
    def Add_LanyardVisSelectList_Query(self):
        """ 
        Function Name: Add_LanyardVisSelectList_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewLanyardVisSelection
        """    
        # Create the sql query params
        sqlTableCol = ("intLanVisTextSelectID", "strLanVisTextSelect")   
        sqlTableName = "TLanVisTextSelects"
        sqlTableValues = (LanyardVisSelection.intLanVisTextSelectID, LanyardVisSelection.strLanVisTextSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams) 

    def Clear_LanyardVisSel_Attributes(self):
        """ 
        Function Name: Clear_LanyardVisSel_Attributes
        Function Description: This function clears the Lanyard Visual Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intLanVisTextSelectID", "strLanVisTextSelect")   
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                
                
class LanyardVisualInspect(Lanyard, InspectionType, LanyardVisSelection, InspectionStatus):
    """
    Class Name: LanyardVisualInspect
    Class Description: This class gets and sets all of the Lanyard Visual Inspection attributes. 
    """
    # Create class variable shared amongst all Lanyard Visual Inspection methods
    aintLanyardVisualInspectionID = []
    aLanyardVisualCache = []
        
    # Instantiate the following attributes
    def __init__(self, intLanyardVisualInspectionID, intLanyardID, intInspectionTypeID, intLanVisTextSelectID, intInspectionStatusID):
        self.intLanyardVisualInspectionID = intLanyardVisualInspectionID
        # Inherits the child class with all the necessary objects
        Lanyard.__init__(intLanyardID)
        InspectionType.__init__(intInspectionTypeID)
        LanyardVisSelection.__init__(intLanVisTextSelectID)
        InspectionStatus.__init__(intInspectionStatusID)

    # Property decorator object get function to access private intLanyardVisualInspectionID
    @property
    def intLanyardVisualInspectionID(self):
        return self._intLanyardVisualInspectionID

    # setter method 
    @intLanyardVisualInspectionID.setter 
    def intLanyardVisualInspectionID(self, intLanyardVisualInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intLanyardVisualInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Lanyard Visual Inspection ID to value
        if intLanyardVisualInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intLanyardVisualInspectionID = intLanyardVisualInspectionID 

    def Append_LanyardVisualIDList(self, intObject):
        """ 
        Function Name: Append_LanyardVisualIDList
        Function Description: This function appends objects to the Lanyard Visual Inspection ID list
        """    
        self.aintLanyardVisualInspectionID.append(intObject)

    def Remove_LanyardVisualIDList(self, intObject):
        """ 
        Function Name: Remove_LanyardVisualIDList
        Function Description: This function removes objects in the Lanyard Visual Inspection ID list
        """    
        self.aintLanyardVisualInspectionID.remove(intObject)

    def Get_LanyardVisualIDList_Obj(self):
        """ 
        Function Name: Get_LanyardVisualIDList_Obj
        Function Description: This function gets all the objects in the Lanyard Visual Inspection ID list
        """    
        return self.aintLanyardVisualInspectionID
                
    def Delete_LanyardVisualInspect_Data(self):
        """ 
        Function Name: Delete_LanyardVisualInspect_Data
        Function Description: This function removes all the objects in the Lanyard Visual Inspection ID class
        """    
        LanyardVisualInspect.aintLanyardVisualInspectionID = []
        LanyardVisualInspect.aLanyardVisualCache = []

    def Set_LanyardVisualInspect_Data(self):
        """ 
        Function Name: Set_LanyardVisualInspect_Data
        Function Description: This function sets all the objects in the Lanyard Visual Inspection class
        """    
        self.intLanyardVisualInspectionID = LanyardVisualInspect.aLanyardVisualCache[0]
        self.intLanyardID = LanyardVisualInspect.aLanyardVisualCache[1]
        self.intInspectionTypeID = LanyardVisualInspect.aLanyardVisualCache[2]
        self.intLanVisTextSelectID = LanyardVisualInspect.aLanyardVisualCache[3]
        self.intInspectionStatusID = LanyardVisualInspect.aLanyardVisualCache[4]
                
    def Add_LanyardVisualInspect_Query(self):
        """ 
        Function Name: Add_LanyardVisualInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewLanyardVisualInspection
        """    
        # Set the class variables before dumping the data to the database
        LanyardVisualInspect.Set_LanyardVisualInspect_Data(self)
        
        # Create the sql query string       
        sqlTableCol = ("intLanyardVisualInspectionID", "intLanyardID", "intInspectionTypeID", "intLanVisTextSelectID", "intInspectionStatusID")     
        sqlTableName = "TLanyardVisualInspections"
        sqlTableValues = (self.intLanyardVisualInspectionID, self.intLanyardID, self.intInspectionTypeID, self.intLanVisTextSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Clear_LanyardVisInspect_Attributes(self):
        """ 
        Function Name: Clear_LanyardVisInspect_Attributes
        Function Description: This function clears the Lanyard Visual Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intLanyardVisualInspectionID", "intLanyardID", "intInspectionTypeID", "intLanVisTextSelectID", "intInspectionStatusID")     
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            

class LanyardPhysSelection():
    """
    Class Name: LanyardPhysSelection
    Class Description: This class gets and sets all of the Lanyard Physical Selections. 
    """
    # Create class variable shared amongst all Lanyard Physical methods
    aintLanPhysTextSelectID = []
    astrLanPhysTextSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intLanPhysTextSelectID, strLanPhysTextSelect, strLanPhysStatus):
        self.intLanPhysTextSelectID = intLanPhysTextSelectID
        self.strLanPhysTextSelect = strLanPhysTextSelect
        self.strLanPhysStatus = strLanPhysStatus

    # Property decorator object get function to access private intLanPhysTextSelectID
    @property
    def intLanPhysTextSelectID(self):
        return self._intLanPhysTextSelectID

    # Property decorator object get function to access private strLanPhysTextSelect
    @property
    def strLanPhysTextSelect(self):
        return self._strLanPhysTextSelect
        
    # Property decorator object get function to access private strLanPhysStatus
    @property
    def strLanPhysStatus(self):
        return self._strLanPhysStatus
                
    # setter method 
    @intLanPhysTextSelectID.setter 
    def intLanPhysTextSelectID(self, intLanPhysTextSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intLanPhysTextSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intLanPhysTextSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intLanPhysTextSelectID = intLanPhysTextSelectID 
        
    # setter method 
    @strLanPhysTextSelect.setter 
    def strLanPhysTextSelect(self, strLanPhysTextSelect): 
        # Return true if specified object is of str type
        if not isinstance(strLanPhysTextSelect, str): 
            raise TypeError('Lanyard physical input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strLanPhysTextSelect.isspace(): 
            raise ValueError('Lanyard physical input cannot be empty') 
        # Set the attribute to the value if true
        elif strLanPhysTextSelect.isascii():
            self._strLanPhysTextSelect = strLanPhysTextSelect

    # setter method 
    @strLanPhysStatus.setter 
    def strLanPhysStatus(self, strLanPhysStatus): 
        # Return true if specified object is of str type
        if not isinstance(strLanPhysStatus, str): 
            raise TypeError('Lanyard physical status must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strLanPhysStatus.isspace(): 
            raise ValueError('Lanyard physical status cannot be empty') 
        # Set the attribute to the value if true
        elif strLanPhysStatus.isascii():
            self._strLanPhysStatus = strLanPhysStatus

    def Append_LanyardPhysIDList(self, intObject):
        """ 
        Function Name: Append_LanyardPhysIDList
        Function Description: This function appends objects to the Lanyard Physical Selection ID list
        """    
        self.aintLanPhysTextSelectID.append(intObject)

    def Remove_LanyardPhysIDList(self, intObject):
        """ 
        Function Name: Remove_LanyardPhysIDList
        Function Description: This function removes objects in the Lanyard Physical Selection ID list
        """    
        self.aintLanPhysTextSelectID.remove(intObject)

    def Get_LanyardPhysIDList_Obj(self):
        """ 
        Function Name: Get_LanyardPhysIDList_Obj
        Function Description: This function gets all the objects in the Lanyard Visual Selection ID list
        """    
        return self.aintLanPhysTextSelectID
    
    def Append_LanyardPhysSelectList(self, strObject):
        """ 
        Function Name: Append_LanyardPhysSelectList
        Function Description: This function appends objects to the Lanyard Visual Selection list
        """    
        self.astrLanPhysTextSelect.append(strObject)

    def Remove_LanyardPhysSelectList(self, strObject):
        """ 
        Function Name: Remove_LanyardPhysSelectList
        Function Description: This function removes objects in the Lanyard Visual Selection list
        """    
        self.astrLanPhysTextSelect.remove(strObject)

    def Get_LanyardPhysSelectList_Obj(self):
        """ 
        Function Name: Get_LanyardPhysSelectList_Obj
        Function Description: This function gets all the objects in the Lanyard Visual Selection list
        """    
        return self.astrLanPhysTextSelect   
                    
    def Delete_LanyardPhysSelectList_Data(self):
        """ 
        Function Name: Delete_LanyardPhysSelectList_Data
        Function Description: This function removes all the objects in the Lanyard Visual Selection class
        """    
        LanyardPhysSelection.aintLanPhysTextSelectID = []
        LanyardPhysSelection.astrLanPhysTextSelect = []

    def Check_LanPhysSelection_Dup(self):
        """ 
        Function Name: Check_LanPhysSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        lanyard physical selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intLanPhysTextSelectID", "strLanPhysTextSelect")   
        sqlTableName = "TLanPhysTextSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strLanPhysTextSelect in sqlDupValues[i]:
                self.intLanPhysTextSelectID = sqlDupValues[i][0]
                self.strLanPhysTextSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag
            
    def Add_LanyardPhysSelectList_Query(self):
        """ 
        Function Name: Add_LanyardPhysSelectList_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewLanyardPhysSelection
        """    
       # Create the sql query params
        sqlTableCol = ("intLanPhysTextSelectID", "strLanPhysTextSelect")   
        sqlTableName = "TLanPhysTextSelects"
        sqlTableValues = (LanyardPhysSelection.intLanPhysTextSelectID, LanyardPhysSelection.strLanPhysTextSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams) 
        
    def Clear_LanyardPhysSel_Attributes(self):
        """ 
        Function Name: Clear_LanyardPhysSel_Attributes
        Function Description: This function clears the Lanyard Physical Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intLanPhysTextSelectID", "strLanPhysTextSelect")   
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            
            
class LanyardPhysicalInspect(Lanyard, InspectionType, LanyardPhysSelection, InspectionStatus):
    """
    Class Name: LanyardPhysicalInspect
    Class Description: This class gets and sets all of the Lanyard Physical Inspection attributes. 
    """
    # Create class variable shared amongst all Lanyard Physical Inspection methods
    aintLanyardPhysicalInspectionID = []
    aLanyardPhysicalCache = []
        
    # Instantiate the following attributes
    def __init__(self, intLanyardPhysicalInspectionID, intLanyardID, intInspectionTypeID, intLanPhysTextSelectID, intInspectionStatusID):
        self.intLanyardPhysicalInspectionID = intLanyardPhysicalInspectionID
        # Inherits the child class with all the necessary objects
        Lanyard.__init__(intLanyardID)
        InspectionType.__init__(intInspectionTypeID)
        LanyardPhysSelection.__init__(intLanPhysTextSelectID)
        InspectionStatus.__init__(intInspectionStatusID)

    # Property decorator object get function to access private intLanyardPhysicalInspectionID
    @property
    def intLanyardPhysicalInspectionID(self):
        return self._intLanyardPhysicalInspectionID

    # setter method 
    @intLanyardPhysicalInspectionID.setter 
    def intLanyardPhysicalInspectionID(self, intLanyardPhysicalInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intLanyardPhysicalInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Lanyard Physical Inspection ID to value
        if intLanyardPhysicalInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intLanyardPhysicalInspectionID = intLanyardPhysicalInspectionID 

    def Append_LanyardPhysicalIDList(self, intObject):
        """ 
        Function Name: Append_LanyardPhysicalIDList
        Function Description: This function appends objects to the Lanyard Physical Inspection ID list
        """    
        self.aintLanyardPhysicalInspectionID.append(intObject)

    def Remove_LanyardPhysicalIDList(self, intObject):
        """ 
        Function Name: Remove_LanyardPhysicalIDList
        Function Description: This function removes objects in the Lanyard Physical Inspection ID list
        """    
        self.aintLanyardPhysicalInspectionID.remove(intObject)

    def Get_LanyardPhysicalIDList_Obj(self):
        """ 
        Function Name: Get_LanyardPhysicalIDList_Obj
        Function Description: This function gets all the objects in the Lanyard Physical Inspection ID list
        """    
        return self.aintLanyardPhysicalInspectionID
                
    def Delete_LanyardPhysicalInspect_Data(self):
        """ 
        Function Name: Delete_LanyardPhysicalInspect_Data
        Function Description: This function removes all the objects in the Lanyard Physical Inspection ID class
        """    
        LanyardPhysicalInspect.aintLanyardPhysicalInspectionID = []
        LanyardPhysicalInspect.aLanyardPhysicalCache = []

    def Set_LanyardPhysicalInspect_Data(self):
        """ 
        Function Name: Set_LanyardPhysicalInspect_Data
        Function Description: This function sets all the objects in the Lanyard Physical Inspection class
        """    
        self.intLanyardPhysicalInspectionID = LanyardPhysicalInspect.aLanyardPhysicalCache[0]
        self.intLanyardID = LanyardPhysicalInspect.aLanyardPhysicalCache[1]
        self.intInspectionTypeID = LanyardPhysicalInspect.aLanyardPhysicalCache[2]
        self.intLanPhysTextSelectID = LanyardPhysicalInspect.aLanyardPhysicalCache[3]
        self.intInspectionStatusID = LanyardPhysicalInspect.aLanyardPhysicalCache[4]
               
    def Add_LanyardPhysicalInspect_Query(self):
        """ 
        Function Name: Add_LanyardPhysicalInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewLanyardVisualInspection
        """    
        # Set the class variables before dumping the data to the database
        LanyardPhysicalInspect.Set_LanyardPhysicalInspect_Data(self)
        
        # Create the sql query string       
        sqlTableCol = ("intLanyardPhysicalInspectionID", "intLanyardID", "intInspectionTypeID", "intLanPhysTextSelectID", "intInspectionStatusID")     
        sqlTableName = "TLanyardPhysicalInspections"
        sqlTableValues = (self.intLanyardPhysicalInspectionID, self.intLanyardID, self.intInspectionTypeID, self.intLanPhysTextSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Clear_LanyardPhysInspect_Attributes(self):
        """ 
        Function Name: Clear_LanyardPhysInspect_Attributes
        Function Description: This function clears the Lanyard Physical Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intLanyardPhysicalInspectionID", "intLanyardID", "intInspectionTypeID", "intLanPhysTextSelectID", "intInspectionStatusID")     
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                                    

class RetractFunctSelection():
    """
    Class Name: RetractFunctSelection
    Class Description: This class gets and sets all of the Retract Function Selections. 
    """
    # Create class variable shared amongst all Retract Function methods
    aintRetractFunctSelectID = []
    astrRetractFunctSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intRetractFunctSelectID, strRetractFunctSelect, strRetractStatus):
        self.intRetractFunctSelectID = intRetractFunctSelectID
        self.strRetractFunctSelect = strRetractFunctSelect
        self.strRetractStatus = strRetractStatus

    # Property decorator object get function to access private intRetractFunctSelectID
    @property
    def intRetractFunctSelectID(self):
        return self._intRetractFunctSelectID

    # Property decorator object get function to access private strRetractFunctSelect
    @property
    def strRetractFunctSelect(self):
        return self._strRetractFunctSelect

    # Property decorator object get function to access private strRetractStatus
    @property
    def strRetractStatus(self):
        return self._strRetractStatus
                        
    # setter method 
    @intRetractFunctSelectID.setter 
    def intRetractFunctSelectID(self, intRetractFunctSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intRetractFunctSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intRetractFunctSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intRetractFunctSelectID = intRetractFunctSelectID 
        
    # setter method 
    @strRetractFunctSelect.setter 
    def strRetractFunctSelect(self, strRetractFunctSelect): 
        # Return true if specified object is of str type
        if not isinstance(strRetractFunctSelect, str): 
            raise TypeError('Retract function input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strRetractFunctSelect.isspace(): 
            raise ValueError('Retract function input cannot be empty') 
        # Set the attribute to the value if true
        elif strRetractFunctSelect.isascii():
            self._strRetractFunctSelect = strRetractFunctSelect

    # setter method 
    @strRetractStatus.setter 
    def strRetractStatus(self, strRetractStatus): 
        # Return true if specified object is of str type
        if not isinstance(strRetractStatus, str): 
            raise TypeError('Retract function status must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strRetractStatus.isspace(): 
            raise ValueError('Retract function status cannot be empty') 
        # Set the attribute to the value if true
        elif strRetractStatus.isascii():
            self._strRetractStatus = strRetractStatus

    def Append_RetractFunctIDList(self, intObject):
        """ 
        Function Name: Append_RetractFunctIDList
        Function Description: This function appends objects to the Retract Function Selection ID list
        """    
        self.aintRetractFunctSelectID.append(intObject)

    def Remove_RetractFunctIDList(self, intObject):
        """ 
        Function Name: Remove_RetractFunctIDList
        Function Description: This function removes objects in the Retract Function Selection ID list
        """    
        self.aintRetractFunctSelectID.remove(intObject)

    def Get_RetractFunctIDList_Obj(self):
        """ 
        Function Name: Get_RetractFunctIDList_Obj
        Function Description: This function gets all the objects in the Retract Function Selection ID list
        """    
        return self.aintRetractFunctSelectID
    
    def Append_RetractFunctSelectList(self, strObject):
        """ 
        Function Name: Append_RetractFunctSelectList
        Function Description: This function appends objects to the Retract Function Selection list
        """    
        self.astrRetractFunctSelect.append(strObject)

    def Remove_RetractFunctSelectList(self, strObject):
        """ 
        Function Name: Remove_RetractFunctSelectList
        Function Description: This function removes objects in the Retract Function Selection list
        """    
        self.astrRetractFunctSelect.remove(strObject)

    def Get_RetractFunctSelectList_Obj(self):
        """ 
        Function Name: Get_RetractFunctSelectList_Obj
        Function Description: This function gets all the objects in the Retract Function Selection list
        """    
        return self.astrRetractFunctSelect   
                    
    def Delete_RetractFunctSelection_Data(self):
        """ 
        Function Name: Delete_RetractFunctSelection_Data
        Function Description: This function removes all the objects in the Retract Function Selection class
        """    
        RetractFunctSelection.aintRetractFunctSelectID = []
        RetractFunctSelection.astrRetractFunctSelect = []

    def Check_RetractFunctSelection_Dup(self):
        """ 
        Function Name: Check_RetractFunctSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        Retract function selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intRetractFunctSelectID", "strRetractFunctSelect")   
        sqlTableName = "TRetractFunctSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strRetractFunctSelect in sqlDupValues[i]:
                self.intRetractFunctSelectID = sqlDupValues[i][0]
                self.strRetractFunctSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag
            
    def Add_RetractFunctSelection_Query(self):
        """ 
        Function Name: Add_RetractFunctSelection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewRetractFunctSelection
        """    
        # Create the sql query string
        sqlTableCol = ("intRetractFunctSelectID", "strRetractFunctSelect")   
        sqlTableName = "TRetractFunctSelects"
        sqlTableValues = (RetractFunctSelection.intRetractFunctSelectID, RetractFunctSelection.strRetractFunctSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)   

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)      

    def Clear_LanyardFuncSel_Attributes(self):
        """ 
        Function Name: Clear_LanyardFuncSel_Attributes
        Function Description: This function clears the Lanyard Function Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intRetractFunctSelectID", "strRetractFunctSelect")   
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                    
        
class LanyardFunctionInspect(Lanyard, InspectionType, RetractFunctSelection, InspectionStatus):
    """
    Class Name: LanyardFunctionInspect
    Class Description: This class gets and sets all of the Lanyard Function Inspection  attributes. 
    """
    # Create class variable shared amongst all Lanyard Function Inspection methods
    aintLanyardRetractFunctionInspectionID = []
    aLanyardFunctCache = []    
    
    # Instantiate the following attributes
    def __init__(self, intLanyardRetractFunctionInspectionID, intLanyardID, intInspectionTypeID, intRetractFunctSelectID, intInspectionStatusID):
        self.intLanyardRetractFunctionInspectionID = intLanyardRetractFunctionInspectionID
        # Inherits the child class with all the necessary objects
        Lanyard.__init__(intLanyardID)
        InspectionType.__init__(intInspectionTypeID)
        RetractFunctSelection.__init__(intRetractFunctSelectID)
        InspectionStatus.__init__(intInspectionStatusID)

    # Property decorator object get function to access private intLanyardRetractFunctionInspectionID
    @property
    def intLanyardRetractFunctionInspectionID(self):
        return self._intLanyardRetractFunctionInspectionID

    # setter method 
    @intLanyardRetractFunctionInspectionID.setter 
    def intLanyardRetractFunctionInspectionID(self, intLanyardRetractFunctionInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intLanyardRetractFunctionInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Lanyard Function Inspection ID to value
        if intLanyardRetractFunctionInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intLanyardRetractFunctionInspectionID = intLanyardRetractFunctionInspectionID 

    def Append_LanyardFunctIDList(self, intObject):
        """ 
        Function Name: Append_LanyardFunctIDList
        Function Description: This function appends objects to the Lanyard Function Inspection ID list
        """    
        self.aintLanyardRetractFunctionInspectionID.append(intObject)

    def Remove_LanyardFunctIDList(self, intObject):
        """ 
        Function Name: Remove_LanyardFunctIDList
        Function Description: This function removes objects in the Lanyard Function Inspection ID list
        """    
        self.aintLanyardRetractFunctionInspectionID.remove(intObject)

    def Get_LanyardFunctIDList_Obj(self):
        """ 
        Function Name: Get_LanyardFunctIDList_Obj
        Function Description: This function gets all the objects in the Lanyard Function Inspection ID list
        """    
        return self.aintLanyardRetractFunctionInspectionID
                
    def Delete_LanyardFunctInspect_Data(self):
        """ 
        Function Name: Delete_LanyardFunctInspect_Data
        Function Description: This function removes all the objects in the Lanyard Function Inspection ID class
        """    
        LanyardFunctionInspect.aintLanyardRetractFunctionInspectionID = []
        LanyardFunctionInspect.aLanyardFunctCache = []

    def Set_LanyardFunctInspect_Data(self):
        """ 
        Function Name: Set_LanyardFunctInspect_Data
        Function Description: This function sets all the objects in the Lanyard Function Inspection class
        """    
        self.intLanyardRetractFunctionInspectionID = LanyardFunctionInspect.aLanyardFunctCache[0]
        self.intLanyardID = LanyardFunctionInspect.aLanyardFunctCache[1]
        self.intInspectionTypeID = LanyardFunctionInspect.aLanyardFunctCache[2]
        self.intRetractFunctSelectID = LanyardFunctionInspect.aLanyardFunctCache[3]
        self.intInspectionStatusID = LanyardFunctionInspect.aLanyardFunctCache[4]
                                        
    def Add_LanyardFunctInspect_Query(self):
        """ 
        Function Name: Add_LanyardFunctInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewLanyardFunctionInspection
        """    
        # Set the class variables before dumping the data to the database
        LanyardFunctionInspect.Set_LanyardFunctInspect_Data(self)
                
        # Create the sql query string
        sqlTableCol = ("intLanyardRetractFunctionInspectionID", "intLanyardID", "intInspectionTypeID", "intRetractFunctSelectID", "intInspectionStatusID")     
        sqlTableName = "TLanyardRetractFunctionInspections"
        sqlTableValues = (self.intLanyardRetractFunctionInspectionID, self.intLanyardID, self.intInspectionTypeID, self.intRetractFunctSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)           

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Clear_LanyardFuncInspect_Attributes(self):
        """ 
        Function Name: Clear_LanyardFuncInspect_Attributes
        Function Description: This function clears the Lanyard Function Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intLanyardRetractFunctionInspectionID", "intLanyardID", "intInspectionTypeID", "intRetractFunctSelectID", "intInspectionStatusID")     
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            
            
class StandardLanyardInspect(LanyardVisualInspect, LanyardPhysicalInspect, LanyardFunctionInspect):
    """
    Class Name: StandardLanyardInspect
    Class Description: This class gets and sets all of the Standard Lanyard Inspection attributes. 
    Pass in the Lanyard Visual and Physical classes. 
    """
    # Create class variable shared amongst all Standard Lanyard Inspection methods
    aintStandardLanyardInspectionID = []
    aStandardLanyardInsCache = []
        
    # Instantiate the following attributes
    def __init__(self, intStandardLanyardInspectionID, intLanyardVisualInspectionID, intLanyardPhysicalInspectionID,
                 intLanyardRetractFunctionInspectionID):
        self.intStandardLanyardInspectionID = intStandardLanyardInspectionID
        # Inherits the child class with all the necessary objects
        LanyardVisualInspect.__init__(intLanyardVisualInspectionID)
        LanyardPhysicalInspect.__init__(intLanyardPhysicalInspectionID)
        LanyardFunctionInspect.__init__(intLanyardRetractFunctionInspectionID)
        
    # Property decorator object get function to access private intStandardLanyardInspectionID
    @property
    def intStandardLanyardInspectionID(self):
        return self._intStandardLanyardInspectionID
    
    # setter method 
    @intStandardLanyardInspectionID.setter 
    def intStandardLanyardInspectionID(self, intStandardLanyardInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intStandardLanyardInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intStandardLanyardInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intStandardLanyardInspectionID = intStandardLanyardInspectionID    

    def Append_StandLanyardInspectIDList(self, intObject):
        """ 
        Function Name: Append_StandLanyardInspectIDList
        Function Description: This function appends objects to the Standard Lanyard Inspection ID list
        """    
        self.aintStandardLanyardInspectionID.append(intObject)

    def Remove_StandLanyardInspectIDList(self, intObject):
        """ 
        Function Name: Remove_StandLanyardInspectIDList
        Function Description: This function removes objects in the Standard Lanyard Inspection ID list
        """    
        self.aintStandardLanyardInspectionID.remove(intObject)

    def Get_StandLanyardInspectIDList_Obj(self):
        """ 
        Function Name: Get_StandLanyardInspectIDList_Obj
        Function Description: This function gets all the objects in the Standard Lanyard Inspection ID list
        """    
        return self.aintStandardLanyardInspectionID     

    def Add_StandLanyardInspect_Query(self):
        """ 
        Function Name: Add_StandLanyardInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewStandardLanyardInspection
        """    
        # Create the sql query string
        sqlTableNames = ("TStandardLanyardInspections")
        sqlTableCol = ("intStandardLanyardInspectionID", "intLanyardVisualInspectionID", "intLanyardPhysicalInspectionID", 
                       "intLanyardRetractFunctionInspectionID", "intInspectionStatusID") 
        # Set the primary key values from the cached array object
        aPrimKeyValues = [item for item in StandardLanyardInspect.aStandardLanyardInsCache]        

        # Get the visual, physical, and functional status IDs
        VisStatusID = InspectionStatus.astrInspectionStatusDesc.index(LanyardVisSelection.strLanVisStatus) + 1
        PhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(LanyardPhysSelection.strLanPhysStatus) + 1
        FunctStatusID = InspectionStatus.astrInspectionStatusDesc.index(RetractFunctSelection.strRetractStatus) + 1
        aInsStatusID = [VisStatusID, PhysStatusID, FunctStatusID]

        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(aInsStatusID)

        # Append the AutoBelay Status array 
        AutoBelayInspect.aAutoBelayInspectStatus.append(intOverallStatus)
                          
        # Append the primary key list with the new over status ID
        aPrimKeyValues.append(intOverallStatus)                      
        
        # Set the parameters
        sqlParams = (sqlTableNames, sqlTableCol, tuple(aPrimKeyValues))

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)        

    def Delete_StandLanyardInspect_Data(self):
        """ 
        Function Name: Delete_StandCarabInspect_Data
        Function Description: This function removes all the objects in the Standard Carabiner Inspection class
        """    
        StandardLanyardInspect.aStandardLanyardInsCache = []                
        StandardLanyardInspect.aintStandardLanyardInspectionID = []

    def Clear_LanyardStandardInspect_Attributes(self):
        """ 
        Function Name: Clear_LanyardStandardInspect_Attributes
        Function Description: This function clears the Lanyard Standard Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intStandardLanyardInspectionID", "intLanyardVisualInspectionID", "intLanyardPhysicalInspectionID", 
                       "intLanyardRetractFunctionInspectionID", "intInspectionStatusID") 
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None) 

    def Reset_Lanyard_Data(self):
        """ 
        Function Name: Reset_Lanyard_Data
        Function Description: This function clears the Lanyard data attributes 
        """  
        # Clear the class attributes
        LanyardVisSelection.Clear_LanyardVisSel_Attributes(self)
        LanyardVisualInspect.Clear_LanyardVisInspect_Attributes(self)
        LanyardPhysSelection.Clear_LanyardPhysSel_Attributes(self)
        LanyardPhysicalInspect.Clear_LanyardPhysInspect_Attributes(self)
        RetractFunctSelection.Clear_LanyardFuncSel_Attributes(self)
        LanyardFunctionInspect.Clear_LanyardFuncInspect_Attributes(self)
        StandardLanyardInspect.Clear_LanyardStandardInspect_Attributes(self)
                                    
    def Delete_Lanyard_Data(self):
        """ 
        Function Name: Delete_Lanyard_Data
        Function Description: This function clears the Lanyard data arrays 
        """  
        # Clear the class arrays
        LanyardVisSelection.Delete_LanyardVisSelectList_Data(self)
        LanyardVisualInspect.Delete_LanyardVisualInspect_Data(self)
        LanyardPhysSelection.Delete_LanyardPhysSelectList_Data(self)
        LanyardPhysicalInspect.Delete_LanyardPhysicalInspect_Data(self)
        RetractFunctSelection.Delete_RetractFunctSelection_Data(self)
        LanyardFunctionInspect.Delete_LanyardFunctInspect_Data(self)
        StandardLanyardInspect.Delete_StandLanyardInspect_Data(self)
        
                                                                    
class States():
    """
    Class Name: States
    Class Description: This class gets and sets all of the States attributes. 
    """
    # Create class variable shared amongst all State methods
    aintStateIDList = []
    astrStateName = []   
        
    # Instantiate the following attributes
    def __init__(self, intStateID, strStateName):
        self.intStateID = intStateID
        self.strStateName = strStateName

    # Property decorator object get function to access private intStateID
    @property
    def intStateID(self):
        return self._intStateID

    # Property decorator object get function to access private strStateName
    @property
    def strStateName(self):
        return self._strStateName
    
    # setter method 
    @intStateID.setter 
    def intStateID(self, intStateID): 
        # Return true if specified object is of int type
        if not isinstance(intStateID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intStateID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intStateID = intStateID    

    # setter method 
    @strStateName.setter 
    def strStateName(self, strStateName): 
        # Return true if specified object is of str type
        if not isinstance(strStateName, str): 
            raise TypeError('State must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if strStateName.isspace(): 
            raise ValueError('State cannot be empty') 
        # Set the attribute to the value if true
        elif strStateName.isascii():
            self._strStateName = strStateName
       
    def Append_StateIDList(self, intObject):
        """ 
        Function Name: Append_StateIDList
        Function Description: This function appends objects to the State ID list
        """    
        self.aintStateIDList.append(intObject)

    def Remove_StateIDList(self, intObject):
        """ 
        Function Name: Remove_StateIDList
        Function Description: This function removes objects in the State ID list
        """    
        self.aintStateIDList.remove(intObject)

    def Get_StateIDList_Obj(self):
        """ 
        Function Name: Get_StateIDList_Obj
        Function Description: This function gets all the objects in the State ID list
        """    
        return self.aintStateIDList            

    def Append_StateNameList(self, strObject):
        """ 
        Function Name: Append_StateNameList
        Function Description: This function appends objects to the State Name list
        """    
        self.astrStateName.append(strObject)

    def Remove_StateNameList(self, strObject):
        """ 
        Function Name: Remove_StateNameList
        Function Description: This function removes objects in the State Name list
        """    
        self.astrStateName.remove(strObject)

    def Get_StateNameList_Obj(self):
        """ 
        Function Name: Get_StateNameList_Obj
        Function Description: This function gets all the objects in the State Name list
        """    
        return self.astrStateName       
            
    def Get_State_Data(self):
        """ 
        Function Name: Get_State_Data
        Function Description: This function gets all the objects in the state table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TStates"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the State Data List
        for i in range(len(QueryResultList)):
            States.Append_StateIDList(self, QueryResultList[i][0])
            States.Append_StateNameList(self, QueryResultList[i][1]) 

    def Delete_State_Data(self):
        """ 
        Function Name: Delete_State_Data
        Function Description: This function removes all the objects in the State class
        """   
        States.aintStateIDList = []
        States.astrStateName = []
        
                    
class WallLocation():
    """
    Class Name: WallLocation
    Class Description: This class gets and sets all of the WallLocation attributes. 
    """
    # Create class variable shared amongst all WallLocation methods
    aintWallLocationID= []
    astrWallLocationDesc = []
        
    # Instantiate the following attributes
    def __init__(self, intWallLocationID, strWallLocationDesc):
        self.intWallLocationID = intWallLocationID
        self.strWallLocationDesc = strWallLocationDesc

    # Property decorator object get function to access private intWallLocationID
    @property
    def intWallLocationID(self):
        return self._intWallLocationID

    # Property decorator object get function to access private strWallLocationDesc
    @property
    def strWallLocationDesc(self):
        return self._strWallLocationDesc
    
    # setter method 
    @intWallLocationID.setter 
    def intWallLocationID(self, intWallLocationID): 
        # Return true if specified object is of int type
        if not isinstance(intWallLocationID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intWallLocationID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intWallLocationID = intWallLocationID    
            
    # setter method 
    @strWallLocationDesc.setter 
    def strWallLocationDesc(self, strWallLocationDesc): 
        # Return true if specified object is of str type
        if not isinstance(strWallLocationDesc, str): 
            raise TypeError('Wall Location must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strWallLocationDesc.isspace(): 
            raise ValueError('Wall Location cannot be empty') 
        # Set the attribute to the value if true
        elif strWallLocationDesc.isascii():
            self._strWallLocationDesc = strWallLocationDesc  
            
    def Append_WallLocationIDList(self, intObject):
        """ 
        Function Name: Append_WallLocationIDList
        Function Description: This function appends objects to the WallLocation ID list
        """    
        self.aintWallLocationID.append(intObject)

    def Remove_WallLocationIDList(self, intObject):
        """ 
        Function Name: Remove_WallLocationIDList
        Function Description: This function removes objects in the WallLocation ID list
        """    
        self.aintWallLocationID.remove(intObject)

    def Get_WallLocationIDList_Obj(self):
        """ 
        Function Name: Get_WallLocationIDList_Obj
        Function Description: This function gets all the objects in the WallLocation ID list
        """    
        return self.aintWallLocationID               

    def Append_WallLocationNameList(self, strObject):
        """ 
        Function Name: Append_WallLocationNameList
        Function Description: This function appends objects to the Wall Location Name list
        """    
        self.astrWallLocationDesc.append(strObject)

    def Remove_WallLocationNameList(self, strObject):
        """ 
        Function Name: Remove_WallLocationNameList
        Function Description: This function removes objects in the Wall Location Name list
        """    
        self.astrWallLocationDesc.remove(strObject)

    def Get_WallLocationNameList_Obj(self):
        """ 
        Function Name: Get_WallLocationNameList_Obj
        Function Description: This function gets all the objects in the Wall Location Name list
        """    
        return self.astrWallLocationDesc  
    
    def Get_WallLocation_Data(self):
        """ 
        Function Name: Get_WallLocation_Data
        Function Description: This function gets all the objects in the Wall Locations table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TWallLocations"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the Hose Data List
        for i in range(len(QueryResultList)):
            WallLocation.Append_WallLocationIDList(self, QueryResultList[i][0])
            WallLocation.Append_WallLocationNameList(self, QueryResultList[i][1]) 

    def Get_WallLocation_Selection(self):
        """ 
        Function Name: Get_WallLocation_Selection
        Function Description: This function will get the selection name from the user and will update the 
        class objects with the data from the database.
        """    
        # First get the selection from the user 
        for i, item in enumerate(self.astrWallLocationDesc):
            if self.strWallLocationDesc == item:
                # Assign the iterable num to the ID num and assign the objects to the desired data sets                 
                self.intWallLocationID = self.aintWallLocationID[i]
                if not self.strWallLocationDesc:
                    self.strWallLocationDesc = self.astrWallLocationDesc[i]
                break

    def Add_NewWallLocation_Query(self):
        """ 
        Function Name: Add_NewWallLocation_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Create the sql query string
        sqlTableCol = ("intWallLocationID", "strWallLocationDesc")   
        sqlTableName = "TWallLocations"  

        # Set the Table values and the params tuple
        sqlTableValues = (self.intWallLocationID, self.strWallLocationDesc)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

        # Clear the attributes 
        # WallLocation.Clear_WallLocation_Attributes(WallLocation)

        # Reload the data after user submits entry
        WallLocation.Delete_WallLocation_Data(WallLocation)
        WallLocation.Get_WallLocation_Data(WallLocation)

    def Clear_WallLocation_Attributes(self):
        """ 
        Function Name: Clear_WallLocation_Attributes
        Function Description: This function clears the WallLocation attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intWallLocationID", "strWallLocationDesc")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            
    def Delete_WallLocation_Data(self):
        """ 
        Function Name: Delete_WallLocation_Data
        Function Description: This function removes all the objects in the Wall Location class
        """    
        WallLocation.aintWallLocationID = []
        WallLocation.astrWallLocationDesc = []
                        

class Location():
    """
    Class Name: Location
    Class Description: This class gets and sets all of the Location attributes. 
    """
    # Create class variable shared amongst all Location methods
    aintLocationID= []
    astrLocationName = []
        
    # Instantiate the following attributes
    def __init__(self, intLocationID, strLocationName):
        self.intLocationID = intLocationID
        self.strLocationName = strLocationName

    # Property decorator object get function to access private intLocationID
    @property
    def intLocationID(self):
        return self._intLocationID

    # Property decorator object get function to access private strLocationName
    @property
    def strLocationName(self):
        return self._strLocationName
    
    # setter method 
    @intLocationID.setter 
    def intLocationID(self, intLocationID): 
        # Return true if specified object is of int type
        if not isinstance(intLocationID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intLocationID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intLocationID = intLocationID     
            
    # setter method 
    @strLocationName.setter 
    def strLocationName(self, strLocationName): 
        # Return true if specified object is of str type
        if not isinstance(strLocationName, str): 
            raise TypeError('Location must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strLocationName.isspace(): 
            raise ValueError('Location cannot be empty') 
        # Set the attribute to the value if true
        elif strLocationName.isascii():
            self._strLocationName = strLocationName  
            
    def Append_LocationIDList(self, intObject):
        """ 
        Function Name: Append_LocationIDList
        Function Description: This function appends objects to the Location ID list
        """    
        self.aintLocationID.append(intObject)

    def Remove_LocationIDList(self, intObject):
        """ 
        Function Name: Remove_LocationIDList
        Function Description: This function removes objects in the Location ID list
        """    
        self.aintLocationID.remove(intObject)

    def Get_LocationIDList_Obj(self):
        """ 
        Function Name: Get_LocationIDList_Obj
        Function Description: This function gets all the objects in the Location ID list
        """    
        return self.aintLocationID               

    def Append_LocationNameList(self, strObject):
        """ 
        Function Name: Append_LocationNameList
        Function Description: This function appends objects to the Location Name list
        """    
        self.astrLocationName.append(strObject)

    def Remove_LocationNameList(self, strObject):
        """ 
        Function Name: Remove_LocationNameList
        Function Description: This function removes objects in the Location Name list
        """    
        self.astrLocationName.remove(strObject)

    def Get_LocationNameList_Obj(self):
        """ 
        Function Name: Get_LocationNameList_Obj
        Function Description: This function gets all the objects in the Location Name list
        """    
        return self.astrLocationName  
    
    def Get_Location_Data(self):
        """ 
        Function Name: Get_Location_Data
        Function Description: This function gets all the objects in the Locations table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TLocations"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the Hose Data List
        for i in range(len(QueryResultList)):
            Location.Append_LocationIDList(self, QueryResultList[i][0])
            Location.Append_LocationNameList(self, QueryResultList[i][1]) 

    def Get_Location_Selection(self):
        """ 
        Function Name: Get_Location_Selection
        Function Description: This function will get the selection name from the user and will update the 
        class objects with the data from the database.
        """    
        # First get the selection from the user 
        for i, item in enumerate(self.astrLocationName):
            if self.strLocationName == item:
                # Assign the iterable num to the ID num and assign the objects to the desired data sets                 
                self.intLocationID = self.aintLocationID[i]
                if not self.strLocationName:
                    self.strLocationName = self.astrLocationName[i]
                break

    def Add_NewLocation_Query(self):
        """ 
        Function Name: Add_NewLocation_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Create the sql query string
        sqlTableCol = ("intLocationID", "strLocationName")   
        sqlTableName = "TLocations"  

        # Set the Table values and the params tuple
        sqlTableValues = (self.intLocationID, self.strLocationName)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

        # Reload the data after user submits entry
        Location.Delete_Location_Data(Location)
        Location.Get_Location_Data(Location)

    def Clear_Location_Attributes(self):
        """ 
        Function Name: Clear_Location_Attributes
        Function Description: This function clears the Location attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intLocationID", "strLocationName")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            
    def Delete_Location_Data(self):
        """ 
        Function Name: Delete_Location_Data
        Function Description: This function removes all the objects in the Wall Location class
        """    
        Location.aintLocationID = []
        Location.astrLocationName = []
        
        
class GymFacility(States):
    """
    Class Name: GymFacility
    Class Description: This class gets and sets the GymFacility. Pass in the States attributes
    StateID
    """
    # Create class variable shared amongst all GymFacility methods
    aintGymLocationID = []
    astrGymName = []   
    
    # Instantiate the following attributes
    def __init__(self, intGymLocationID, strGymName, strAddress, intStateID, strZip):
        self.intGymLocationID = intGymLocationID
        self.strGymName = strGymName
        self.strAddress = strAddress
        self.strZip = strZip
        # Inherits the child class with all the necessary objects
        States.__init__(intStateID)        

    # Property decorator object get function to access private intGymLocationID
    @property
    def intGymLocationID(self):
        return self._intGymLocationID

    # Property decorator object get function to access private strGymName
    @property
    def strGymName(self):
        return self._strGymName

    # Property decorator object get function to access private strAddress
    @property
    def strAddress(self):
        return self._strAddress

    # Property decorator object get function to access private strZip
    @property
    def strZip(self):
        return self._strZip            

    # Property decorator object get function to access private strPhoneNum
    @property
    def strPhoneNum(self):
        return self._strPhoneNum
            
    # setter method 
    @intGymLocationID.setter 
    def intGymLocationID(self, intGymLocationID): 
        # Return true if specified object is of int type
        if not isinstance(intGymLocationID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intGymLocationID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intGymLocationID = intGymLocationID    
        
    # setter method 
    @strGymName.setter 
    def strFacilityName(self, strGymName): 
        # Return true if specified object is of str type
        if not isinstance(strGymName, str): 
            raise TypeError('Facility Name must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if strGymName.isspace(): 
            raise ValueError('Facility Name cannot be empty') 
        # Set the attribute to the value if true
        elif strGymName.isascii():
            self._strGymName = strGymName
            
    # setter method 
    @strAddress.setter 
    def strAddress(self, strAddress): 
        # Return true if specified object is of str type
        if not isinstance(strAddress, str): 
            raise TypeError('Address must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strAddress.isspace(): 
            raise ValueError('Address cannot be empty') 
        # Set the attribute to the value if true
        elif strAddress.isascii():
            self._strAddress = strAddress
            
    # setter method 
    @strZip.setter 
    def strZip(self, strZip): 
        # Return true if specified object is of str type
        if not isinstance(strZip, str): 
            raise TypeError('Zip Code must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strZip.isspace(): 
            raise ValueError('Zip Code cannot be empty') 
        # Set the attribute to the value if true
        elif strZip.isascii():
            self._strZip = strZip
            
    def Append_GymLocationIDList(self, intObject):
        """ 
        Function Name: Append_GymLocationIDList
        Function Description: This function appends objects to the GymLocation ID list
        """    
        self.aintGymLocationID.append(intObject)

    def Remove_GymLocationIDList(self, intObject):
        """ 
        Function Name: Remove_GymLocationIDList
        Function Description: This function removes objects in the GymLocation ID list
        """    
        self.aintGymLocationID.remove(intObject)

    def Get_GymLocationIDList_Obj(self):
        """ 
        Function Name: Get_GymLocationIDList_Obj
        Function Description: This function gets all the objects in the GymLocation ID list
        """    
        return self.aintGymLocationID                                                                    

    def Append_GymNameList(self, strObject):
        """ 
        Function Name: Append_GymNameList
        Function Description: This function appends objects to the GymLocation Name list
        """    
        self.astrGymName.append(strObject)

    def Remove_GymNameList(self, strObject):
        """ 
        Function Name: Remove_GymNameList
        Function Description: This function removes objects in the GymLocation Name list
        """    
        self.astrGymName.remove(strObject)

    def Get_GymNameList_Obj(self):
        """ 
        Function Name: Get_GymNameList_Obj
        Function Description: This function gets all the objects in the GymLocation Name list
        """    
        return self.astrGymName  

    def Get_Gym_Data(self):
        """ 
        Function Name: Get_Gym_Data
        Function Description: This function gets all the objects in the GymLocation Table
        """            
        # Create the sql query string
        sqlQuery = """SELECT * FROM TGymLocations"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the Facility Data List
        for i in range(len(QueryResultList)):
            GymFacility.Append_GymLocationIDList(self, QueryResultList[i][0])
            GymFacility.Append_GymNameList(self, QueryResultList[i][1]) 
            
    def Delete_Facility_Data(self):
        """ 
        Function Name: Delete_Facility_Data
        Function Description: This function removes all the objects in the GymFacility class
        """    
        GymFacility.aintGymLocationID = []
        GymFacility.astrGymName = []
                    
                
class AutoBelay():
    """
    Class Name: AutoBelay
    Class Description: This class is get and set all of the AutoBelay attributes. 
    """
    # Create class variable shared amongst all AutoBelay methods
    aintAutoBelayID = []
    astrDeviceName = []
    astrSerialNum = [] 
    astrBumperNum = [] 
    adtmManufactureDate = []
    adtmServiceDate = []
    adtmReserviceDate = []
    adtmInstallationDate = []
    adtmLastInspectionDate = []
    adtmNextInspectionDate = []
    ablnDeviceInUseStatus = []
    
    # Instantiate the following attributes
    def __init__(self, intAutoBelayID, strDeviceName, strSerialNum, strBumperNum, dtmManufactureDate, dtmServiceDate,
                 dtmReserviceDate, dtmInstallationDate, dtmLastInspectionDate, dtmNextInspectionDate,
                 blnDeviceInUse):
        self.intAutoBelayID = intAutoBelayID
        self.strDeviceName = strDeviceName
        self.strSerialNum = strSerialNum
        self.strBumperNum = strBumperNum
        self.dtmManufactureDate = dtmManufactureDate
        self.dtmServiceDate = dtmServiceDate
        self.dtmReserviceDate = dtmReserviceDate
        self.dtmInstallationDate = dtmInstallationDate
        self.dtmLastInspectionDate = dtmLastInspectionDate
        self.dtmNextInspectionDate = dtmNextInspectionDate
        self.blnDeviceInUse = blnDeviceInUse
        
    # Property decorator object get function to access private intAutoBelayID
    @property
    def intAutoBelayID(self):
        return self._intAutoBelayID

    # Property decorator object get function to access private strDeviceName
    @property
    def strDeviceName(self):
        return self._strDeviceName

    # Property decorator object get function to access private strSerialNum
    @property
    def strSerialNum(self):
        return self._strSerialNum

    # Property decorator object get function to access private strBumperNum
    @property
    def strBumperNum(self):
        return self._strBumperNum
    
    # Property decorator object get function to access private dtmManufactureDate
    @property
    def dtmManufactureDate(self):
        return self._dtmManufactureDate

    # Property decorator object get function to access private dtmServiceDate
    @property
    def dtmServiceDate(self):
        return self._dtmServiceDate

    # Property decorator object get function to access private dtmReserviceDate
    @property
    def dtmReserviceDate(self):
        return self._dtmReserviceDate

    # Property decorator object get function to access private dtmInstallationDate
    @property
    def dtmInstallationDate(self):
        return self._dtmInstallationDate

    # Property decorator object get function to access private dtmLastInspectionDate
    @property
    def dtmLastInspectionDate(self):
        return self._dtmLastInspectionDate

    # Property decorator object get function to access private dtmNextInspectionDate
    @property
    def dtmNextInspectionDate(self):
        return self._dtmNextInspectionDate

    # Property decorator object get function to access private blnDeviceInUse
    @property
    def blnDeviceInUse(self):
        return self._blnDeviceInUse   

    # setter method 
    @intAutoBelayID.setter 
    def intAutoBelayID(self, intAutoBelayID): 
        # Return true if specified object is of int type
        if not isinstance(intAutoBelayID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intAutoBelayID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intAutoBelayID = intAutoBelayID    

    # setter method 
    @strDeviceName.setter 
    def strDeviceName(self, strDeviceName):   
        # Return true if specified object is of str type
        if not isinstance(strDeviceName, str): 
            raise TypeError('Manufacture Name must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if strDeviceName.isspace(): 
            raise ValueError('Manufacture Name cannot be empty') 
        # Set the attribute to the value if true
        if strDeviceName.isascii():
            self._strDeviceName = strDeviceName     
            
    # setter method 
    @strSerialNum.setter 
    def strSerialNum(self, strSerialNum):  
        # Return true if specified object is of str type
        if not isinstance(strSerialNum, str): 
            raise TypeError('Serial Number must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strSerialNum.isspace(): 
            raise ValueError('Serial Number cannot be empty') 
        # Set the attribute to the value if true
        if strSerialNum.isascii():
            self._strSerialNum = strSerialNum  
            # Set the global class bool to true
            Bool_Flag.Set_AutoBelay_Bool_Value_True(Bool_Flag)

    # setter method 
    @strBumperNum.setter 
    def strBumperNum(self, strBumperNum): 
        # Return true if specified object is of str type
        if not isinstance(strBumperNum, str): 
            raise TypeError('Bumper Number must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strBumperNum.isspace(): 
            raise ValueError('Bumper Number cannot be empty') 
        # Set the attribute to the value if true
        if strBumperNum.isascii():
            self._strBumperNum = strBumperNum   
            
    # setter method 
    @dtmManufactureDate.setter 
    def dtmManufactureDate(self, dtmManufactureDate):           
        # Return true if specified object is of str type
        if not isinstance(dtmManufactureDate, str): 
            raise TypeError('Manufacture Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmManufactureDate.isspace(): 
            raise ValueError('Manufacture Date cannot be empty')       
        # Convert the date to string
        dtmManufactureDate = datetime.strptime(dtmManufactureDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmManufactureDate, date): 
            raise TypeError('Manufacture Date must be a valid date') 
        # Convert the date back to string
        dtmManufactureDate = str(dtmManufactureDate)

        self._dtmManufactureDate = dtmManufactureDate                 

    # setter method 
    @dtmServiceDate.setter 
    def dtmServiceDate(self, dtmServiceDate):                    
        # Return true if specified object is of str type
        if not isinstance(dtmServiceDate, str): 
            raise TypeError('Service Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmServiceDate.isspace(): 
            raise ValueError('Service Date cannot be empty')       
        # Convert the date to string
        dtmServiceDate = datetime.strptime(dtmServiceDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmServiceDate, date): 
            raise TypeError('Service Date must be a valid date') 
        # Convert the date back to string
        dtmServiceDate = str(dtmServiceDate)

        self._dtmServiceDate = dtmServiceDate   
        
    # setter method 
    @dtmReserviceDate.setter 
    def dtmReserviceDate(self, dtmReserviceDate): 
        # Return true if specified object is of str type
        if not isinstance(dtmReserviceDate, str): 
            raise TypeError('Re-service Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmReserviceDate.isspace(): 
            raise ValueError('Re-service Date cannot be empty')       
        # Convert the date to string
        dtmReserviceDate = datetime.strptime(dtmReserviceDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmReserviceDate, date): 
            raise TypeError('Re-service Date must be a valid date') 
        # Convert the date back to string
        dtmReserviceDate = str(dtmReserviceDate)

        self._dtmReserviceDate= dtmReserviceDate   
        
    # setter method 
    @dtmInstallationDate.setter 
    def dtmInstallationDate(self, dtmInstallationDate):               
        # Return true if specified object is of str type
        if not isinstance(dtmInstallationDate, str): 
            raise TypeError('Install Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmInstallationDate.isspace(): 
            raise ValueError('Install Date cannot be empty')       
        # Convert the date to string
        dtmInstallationDate = datetime.strptime(dtmInstallationDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmInstallationDate, date): 
            raise TypeError('Install Date must be a valid date') 
        # Convert the date back to string
        dtmInstallationDate = str(dtmInstallationDate)

        self._dtmInstallationDate = dtmInstallationDate   
        
    # setter method 
    @dtmLastInspectionDate.setter 
    def dtmLastInspectionDate(self, dtmLastInspectionDate):              
        # Return true if specified object is of str type
        if not isinstance(dtmLastInspectionDate, str): 
            raise TypeError('Last Inspection Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmLastInspectionDate.isspace(): 
            raise ValueError('Last Inspection Date cannot be empty')       
        # Convert the date to string
        dtmLastInspectionDate = datetime.strptime(dtmLastInspectionDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmLastInspectionDate, date): 
            raise TypeError('Last Inspection Date must be a valid date') 
        # Convert the date back to string
        dtmLastInspectionDate = str(dtmLastInspectionDate)

        self._dtmLastInspectionDate = dtmLastInspectionDate   

    # setter method 
    @dtmNextInspectionDate.setter 
    def dtmNextInspectionDate(self, dtmNextInspectionDate):         
        # Return true if specified object is of str type
        if not isinstance(dtmNextInspectionDate, str): 
            raise TypeError('Next Inspection Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmNextInspectionDate.isspace(): 
            raise ValueError('Next Inspection Date cannot be empty')       
        # Convert the date to string
        dtmNextInspectionDate = datetime.strptime(dtmNextInspectionDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmNextInspectionDate, date): 
            raise TypeError('Next Inspection Date must be a valid date') 
        # Convert the date back to string
        dtmNextInspectionDate = str(dtmNextInspectionDate)

        self._dtmNextInspectionDate = dtmNextInspectionDate   
                
    # setter method 
    @blnDeviceInUse.setter 
    def blnDeviceInUse(self, blnDeviceInUse):              
        # Return true if specified object is of str type
        if not isinstance(blnDeviceInUse, str): 
            raise TypeError('In Use Status must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if blnDeviceInUse.isspace(): 
            raise ValueError('In Use Status cannot be empty') 
        # Set the attribute to the value if true
        elif blnDeviceInUse.isalpha():
            self._blnDeviceInUse = blnDeviceInUse   
                            
    def Append_AutoBelayIDList(self, intObject):
        """ 
        Function Name: Append_AutoBelayIDList
        Function Description: This function appends objects to the AutoBelay ID list
        """    
        self.aintAutoBelayID.append(intObject)

    def Remove_AutoBelayIDList(self, intObject):
        """ 
        Function Name: Remove_AutoBelayIDList
        Function Description: This function removes objects in the AutoBelay ID list
        """    
        self.aintAutoBelayID.remove(intObject)

    def Get_AutoBelayIDList_Obj(self):
        """ 
        Funct               ion Name: Get_AutoBelayIDList_Obj
        Function Description: This function gets all the objects in the AutoBelay ID list
        """    
        return self.aintAutoBelayID

    def Append_AutoBelayNameList(self, strObject):
        """ 
        Function Name: Append_AutoBelayNameList
        Function Description: This function appends objects to the AutoBelay Name list
        """    
        self.astrDeviceName.append(strObject)

    def Remove_AutoBelayNameList(self, strObject):
        """ 
        Function Name: Remove_AutoBelayNameList
        Function Description: This function removes objects in the AutoBelay Name list
        """    
        self.astrDeviceName.remove(strObject)

    def Get_AutoBelayNameList_Obj(self):
        """ 
        Function Name: Get_AutoBelayNameList_Obj
        Function Description: This function gets all the objects in the AutoBelay Name list
        """    
        return self.astrDeviceName  
    
    def Append_AutoBelaySerialNumList(self, strObject):
        """ 
        Function Name: Append_AutoBelaySerialNumList
        Function Description: This function appends objects to the AutoBelay Serial Name list
        """    
        self.astrSerialNum.append(strObject)

    def Remove_AutoBelaySerialNumList(self, strObject):
        """ 
        Function Name: Remove_AutoBelaySerialNumList
        Function Description: This function removes objects in the AutoBelay Serial Number list
        """    
        self.astrSerialNum.remove(strObject)

    def Get_AutoBelaySerialNumList_Obj(self):
        """ 
        Function Name: Get_AutoBelaySerialNumList_Obj
        Function Description: This function gets all the objects in the AutoBelay Serial Number list
        """    
        return self.astrSerialNum  

    def Append_AutoBelayBumperNumList(self, strObject):
        """ 
        Function Name: Append_AutoBelaySerialNumList
        Function Description: This function appends objects to the AutoBelay Serial Name list
        """    
        self.astrBumperNum.append(strObject)

    def Remove_AutoBelayBumperNumList(self, strObject):
        """ 
        Function Name: Remove_AutoBelaySerialNumList
        Function Description: This function removes objects in the AutoBelay Serial Number list
        """    
        self.astrBumperNum.remove(strObject)

    def Get_AutoBelayBumperNumList_Obj(self):
        """ 
        Function Name: Get_AutoBelaySerialNumList_Obj
        Function Description: This function gets all the objects in the AutoBelay Serial Number list
        """    
        return self.astrBumperNum
    
    def Append_ManuFactDateList(self, strObject):
        """ 
        Function Name: Append_ManuFactDateList
        Function Description: This function appends objects to the AutoBelay Manufacture Date list
        """    
        self.adtmManufactureDate.append(strObject)

    def Remove_ManuFactDateList(self, strObject):
        """ 
        Function Name: Remove_ManuFactDateList
        Function Description: This function removes objects in the AutoBelay Manufacture Date list
        """    
        self.adtmManufactureDate.remove(strObject)

    def Get_ManuFactDateList_Obj(self):
        """ 
        Function Name: Get_ManuFactDateList_Obj
        Function Description: This function gets all the objects in the AutoBelay Manufacture Date list
        """    
        return self.adtmManufactureDate  

    def Append_ServiceDateList(self, strObject):
        """ 
        Function Name: Append_ServiceDateList
        Function Description: This function appends objects to the AutoBelay Service Date list
        """    
        self.adtmServiceDate.append(strObject)

    def Remove_ServiceDateList(self, strObject):
        """ 
        Function Name: Remove_ServiceDateList
        Function Description: This function removes objects in the AutoBelay Service Date list
        """    
        self.adtmServiceDate.remove(strObject)

    def Get_ServiceDateList_Obj(self):
        """ 
        Function Name: Get_ServiceDateList_Obj
        Function Description: This function gets all the objects in the AutoBelay Service Date list
        """    
        return self.adtmServiceDate  

    def Append_ReserviceDateList(self, strObject):
        """ 
        Function Name: Append_ReserviceDateList
        Function Description: This function appends objects to the AutoBelay Reservice Date list
        """    
        self.adtmReserviceDate.append(strObject)

    def Remove_ReserviceDateList(self, strObject):
        """ 
        Function Name: Remove_ReserviceDateList
        Function Description: This function removes objects in the AutoBelay Reservice Date list
        """    
        self.adtmReserviceDate.remove(strObject)

    def Get_ReserviceDateList_Obj(self):
        """ 
        Function Name: Get_ReserviceDateList_Obj
        Function Description: This function gets all the objects in the AutoBelay Reservice Date list
        """    
        return self.adtmReserviceDate  

    def Append_InstallDateList(self, strObject):
        """ 
        Function Name: Append_InstallDateList
        Function Description: This function appends objects to the AutoBelay Install Date list
        """    
        self.adtmInstallationDate.append(strObject)

    def Remove_InstallDateList(self, strObject):
        """ 
        Function Name: Remove_InstallDateList
        Function Description: This function removes objects in the AutoBelay Install Date list
        """    
        self.adtmInstallationDate.remove(strObject)

    def Get_InstallDateList_Obj(self):
        """ 
        Function Name: Get_InstallDateList_Obj
        Function Description: This function gets all the objects in the AutoBelay Install Date list
        """    
        return self.adtmInstallationDate  

    def Append_NextInspectDateList(self, strObject):
        """ 
        Function Name: Append_NextInspectDateList
        Function Description: This function appends objects to the AutoBelay Next Inspection Date list
        """    
        self.adtmNextInspectionDate.append(strObject)

    def Remove_NextInspectDateList(self, strObject):
        """ 
        Function Name: Remove_NextInspectDateList
        Function Description: This function removes objects in the AutoBelay Next Inspection Date list
        """    
        self.adtmNextInspectionDate.remove(strObject)

    def Get_NextInspectDateList_Obj(self):
        """ 
        Function Name: Get_NextInspectDateList_Obj
        Function Description: This function gets all the objects in the AutoBelay Next Inspection Date list
        """    
        return self.adtmNextInspectionDate  

    def Append_LastInspectDateList(self, strObject):
        """ 
        Function Name: Append_LastInspectDateList
        Function Description: This function appends objects to the AutoBelay Last Inspection Date list
        """    
        self.adtmLastInspectionDate.append(strObject)

    def Remove_LastInspectDateList(self, strObject):
        """ 
        Function Name: Remove_LastInspectDateList
        Function Description: This function removes objects in the AutoBelay Last Inspection Date list
        """    
        self.adtmLastInspectionDate.remove(strObject)

    def Get_LastInspectDateList_Obj(self):
        """ 
        Function Name: Get_LastInspectDateList_Obj
        Function Description: This function gets all the objects in the AutoBelay Last Inspection Date list
        """    
        return self.adtmLastInspectionDate          

    def Append_InUseStatusList(self, strObject):
        """ 
        Function Name: Append_InUseStatusList
        Function Description: This function appends objects to the AutoBelay In Use Status list
        """    
        self.ablnDeviceInUseStatus.append(strObject)

    def Remove_InUseStatusList(self, strObject):
        """ 
        Function Name: Remove_InUseStatusList
        Function Description: This function removes objects in the AutoBelay In Use Status list
        """    
        self.ablnDeviceInUseStatus.remove(strObject)

    def Get_InUseStatusList_Obj(self):
        """ 
        Function Name: Get_InUseStatusList_Obj
        Function Description: This function gets all the objects in the AutoBelay In Use Status list
        """    
        return self.ablnDeviceInUseStatus 
    
    def Get_AutoBelay_Data(self):
        """ 
        Function Name: Get_AutoBelay_Data
        Function Description: This function gets all the objects in the AutoBelay table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TAutoBelays"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # First check if the contents are found and if yes, proceed to get the contents of the table
        if QueryResultList is not None:
            # Append the Auto Belay Data List
            for i in range(len(QueryResultList)):
                AutoBelay.Append_AutoBelayIDList(self, QueryResultList[i][0])
                AutoBelay.Append_AutoBelayNameList(self, QueryResultList[i][1]) 
                AutoBelay.Append_AutoBelaySerialNumList(self, QueryResultList[i][2]) 
                AutoBelay.Append_AutoBelayBumperNumList(self, QueryResultList[i][3]) 
                AutoBelay.Append_ManuFactDateList(self, QueryResultList[i][4]) 
                AutoBelay.Append_ServiceDateList(self, QueryResultList[i][5]) 
                AutoBelay.Append_ReserviceDateList(self, QueryResultList[i][6]) 
                AutoBelay.Append_InstallDateList(self, QueryResultList[i][7]) 
                AutoBelay.Append_LastInspectDateList(self, QueryResultList[i][8]) 
                AutoBelay.Append_NextInspectDateList(self, QueryResultList[i][9]) 
                AutoBelay.Append_InUseStatusList(self, QueryResultList[i][10]) 

    def Set_AutoBelay_Selection(self):
        """ 
        Function Name: Set_AutoBelay_Selection
        Function Description: This function will set the selection name from the user and will update the 
        class objects with the data from the database.
        """    
        # First get the selection from the user 
        for i, item in enumerate(self.astrSerialNum):
            if self.strSerialNum == item:
                # Assign the iterable num to the ID num and assign the objects to the desired data sets    
                self.intAutoBelayID = self.aintAutoBelayID[i]
                self.strDeviceName = self.astrDeviceName[i]
                if not self.strSerialNum:                    
                    self.strSerialNum = self.astrSerialNum[i]
                self.strBumperNum = self.astrBumperNum[i]
                self.dtmManufactureDate = self.adtmManufactureDate[i]
                self.dtmServiceDate = self.adtmServiceDate[i]
                self.dtmReserviceDate = self.adtmReserviceDate[i]
                self.dtmInstallationDate = self.adtmInstallationDate[i]
                self.dtmLastInspectionDate = self.adtmLastInspectionDate[i]
                self.dtmNextInspectionDate = self.adtmNextInspectionDate[i]
                if not self.blnDeviceInUse:
                    self.blnDeviceInUse = self.ablnDeviceInUseStatus[i]
                # Set the global class bool to true
                Bool_Flag.Set_AutoBelay_Bool_Value_True(Bool_Flag)    
                
                break

    def Set_AutoBelay_Data(self):
        """ 
        Function Name: Set_AutoBelay_Data
        Function Description: This function will set the class objects for the device when selected
        """    
        # First get the selection from the user 
        for i, item in enumerate(self.astrSerialNum):
            if self.strSerialNum == item:
                # Assign the iterable num to the ID num and assign the objects to the desired data sets    
                self.intAutoBelayID = self.aintAutoBelayID[i]
                self.strDeviceName = self.astrDeviceName[i]                 
                self.strSerialNum = self.astrSerialNum[i]
                self.strBumperNum = self.astrBumperNum[i]
                self.dtmManufactureDate = self.adtmManufactureDate[i]
                self.dtmServiceDate = self.adtmServiceDate[i]
                self.dtmReserviceDate = self.adtmReserviceDate[i]
                self.dtmInstallationDate = self.adtmInstallationDate[i]
                self.dtmLastInspectionDate = self.adtmLastInspectionDate[i]
                self.dtmNextInspectionDate = self.adtmNextInspectionDate[i]
                self.blnDeviceInUse = self.ablnDeviceInUseStatus[i]
                # Set the global class bool to true
                Bool_Flag.Set_AutoBelay_Bool_Value_True(Bool_Flag)    
                break
                        
    def Add_NewAutoBelay_Query(self):
        """ 
        Function Name: Add_NewAutoBelay_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Create the sql query string
        sqlTableCol = ("intAutoBelayID", "strDeviceName", "strSerialNum", "strBumperNum", "dtmManufactureDate", 
                        "dtmServiceDate", "dtmReserviceDate", "dtmInstallationDate", "dtmLastInspectionDate", 
                        "dtmNextInspectionDate", "blnDeviceInUse")   
        sqlTableName = "TAutoBelays"  

        # Set the Table values and the params tuple
        sqlTableValues = (self.intAutoBelayID, self.strDeviceName, self.strSerialNum, self.strBumperNum, 
                            self.dtmManufactureDate, self.dtmServiceDate, self.dtmReserviceDate, self.dtmInstallationDate, 
                            self.dtmLastInspectionDate, self.dtmNextInspectionDate, self.blnDeviceInUse)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

        # Clear the attributes 
        # self.Clear_AutoBelay_Attributes()

        # Reload the data after user submits entry
        AutoBelay.Delete_AutoBelay_Data(AutoBelay)
        AutoBelay.Get_AutoBelay_Data(AutoBelay)

    def Update_AutoBelay_Inspect_Dates(self):
        """ 
        Function Name: Update_AutoBelay_Inspect_Dates
        Function Description: This function updated the database with inspection dates last and next
        """    
        # Create the sql query string
        sqlTableCol = ("intAutoBelayID", "dtmLastInspectionDate", "dtmNextInspectionDate")   
        sqlTableName = "TAutoBelays"  

        # Set the last and next inspection date based off of the current date
        aDateResult = BaseFunctions.Update_Inspection_Date()
        self.dtmLastInspectionDate = datetime.strftime(aDateResult[0], '%Y-%m-%d')
        self.dtmNextInspectionDate = datetime.strftime(aDateResult[1], '%Y-%m-%d')
        
        # Set the Table values and the params tuple
        sqlTableValues = (self.intAutoBelayID, self.dtmLastInspectionDate, self.dtmNextInspectionDate)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], sqlTableValues[0])         

        # Execute the stored procedure
        Queries.dbExeUSP_UpdateValues(Queries, sqlParams)

    def Update_AutoBelay_InUse_Status(self):
        """ 
        Function Name: Update_AutoBelay_InUse_Status
        Function Description: This function updated the database with in use status of the device
        """ 
        # Declare Local Variables
        intFailStatus = int(3)
        
        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(AutoBelayInspect.aAutoBelayInspectStatus)
            
        if intOverallStatus == intFailStatus:
            # Check if the user knows about the device being failed. If the user removed from wall, the unit is not longer in use
            if messagebox.askyesno(message='ATTENTION! \n\n We have identified an overall status --> FAIL <-- for this unit. \n Has the device been removed for reservicing?') is True:
                # Now check if the device has been packaged for re-servicing
                if messagebox.askyesno(message='ATTENTION! \n\n Has the device been packaged for reservice?') is True:
                    self.blnDeviceInUse = "Out For Reservice"
                    Bool_Flag.Set_OutForService_Bool_Value_True(Bool_Flag)
                else:
                    self.blnDeviceInUse = "No"
            else:
                self.blnDeviceInUse = "Yes"
                
        # Create the sql query string
        sqlTableCol = ("intAutoBelayID", "blnDeviceInUse")   
        sqlTableName = "TAutoBelays"  

        # Set the Table values and the params tuple
        sqlTableValues = (self.intAutoBelayID, self.blnDeviceInUse)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], sqlTableValues[0])         

        # Execute the stored procedure
        Queries.dbExeUSP_UpdateValues(Queries, sqlParams)
                
    def Update_NewAutoBelay_Query(self):
        """ 
        Function Name: Update_NewAutoBelay_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Create the sql query string
        sqlTableCol = ("intAutoBelayID", "strDeviceName", "strSerialNum", "strBumperNum", "dtmManufactureDate", 
                        "dtmServiceDate", "dtmReserviceDate", "dtmInstallationDate", "dtmLastInspectionDate", 
                        "dtmNextInspectionDate", "blnDeviceInUse")   
        sqlTableName = "TAutoBelays"  

        # Set the Table values and the params tuple
        sqlTableValues = (self.intAutoBelayID, self.strDeviceName, self.strSerialNum, self.strBumperNum, 
                            self.dtmManufactureDate, self.dtmServiceDate, self.dtmReserviceDate, self.dtmInstallationDate, 
                            self.dtmLastInspectionDate, self.dtmNextInspectionDate, self.blnDeviceInUse)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], sqlTableValues[0])         

        # Execute the stored procedure
        Queries.dbExeUSP_UpdateValues(Queries, sqlParams)

        # Clear the attributes 
        # self.Clear_AutoBelay_Attributes()

        # Reload the data after user submits entry
        AutoBelay.Delete_AutoBelay_Data(AutoBelay)
        AutoBelay.Get_AutoBelay_Data(AutoBelay)
        
    def Set_Global_AutoBelay_Attributes(self):
        """ 
        Function Name: Set_Global_AutoBelay_Attributes
        Function Description: This function sets AutoBelay attributes once the user proceeds with adding a new
        unit to the database.
        """    
        AutoBelay.strDeviceName = self.strDeviceName
        AutoBelay.strSerialNum = self.strSerialNum
        AutoBelay.strBumperNum = self.strBumperNum
        AutoBelay.dtmManufactureDate = self.dtmManufactureDate
        AutoBelay.dtmServiceDate = self.dtmServiceDate
        AutoBelay.dtmReserviceDate = self.dtmReserviceDate
        AutoBelay.dtmInstallationDate = self.dtmInstallationDate
        AutoBelay.dtmLastInspectionDate = self.dtmLastInspectionDate
        AutoBelay.dtmNextInspectionDate = self.dtmNextInspectionDate
        AutoBelay.blnDeviceInUse = self.blnDeviceInUse

    def Delete_AutoBelay_Data(self):
        """ 
        Function Name: Delete_AutoBelay_Data
        Function Description: This function removes all the objects in the AutoBelay class
        """    
        AutoBelay.aintAutoBelayID = []
        AutoBelay.astrDeviceName = []
        AutoBelay.astrSerialNum = []
        AutoBelay.astrBumperNum = [] 
        AutoBelay.adtmManufactureDate = []
        AutoBelay.adtmServiceDate = []
        AutoBelay.adtmReserviceDate = []
        AutoBelay.adtmInstallationDate = []
        AutoBelay.adtmLastInspectionDate = []
        AutoBelay.adtmNextInspectionDate = []
        AutoBelay.ablnDeviceInUseStatus = []
        
        
class StandardInspect(StandardCarabinerInspect, StandardHandelInspect, StandardCaseInspect, StandardBrakeInspect,
                      StandardLanyardInspect):
    """
    Class Name: StandardInspect
    Class Description: This class gets and sets all of the Standard Inspection attributes for classes:
    StandardCarabinerInspect, StandardHandelInspect, StandardCaseInspect, StandardBrakeInspect, StandardLanyardInspect
    """
    # Create class variable shared amongst all Standard Inspection  methods
    aintStandardInspectionID = []
        
    # Instantiate the following attributes
    def __init__(self, intStandardInspectionID, intStandardCarabinerInspectionID, intStandardHandleInspectionID, 
            intStandardCaseHousingInspectionID, intStandardBrakeHousingInspectionID, intStandardLanyardInspectionID):
        self.intStandardInspectionID = intStandardInspectionID
        # Inherits the child class with all the necessary objects
        StandardCarabinerInspect.__init__(intStandardCarabinerInspectionID)
        StandardHandelInspect.__init__(intStandardHandleInspectionID)
        StandardCaseInspect.__init__(intStandardCaseHousingInspectionID)
        StandardBrakeInspect.__init__(intStandardBrakeHousingInspectionID)
        StandardLanyardInspect.__init__(intStandardLanyardInspectionID)

    # Property decorator object get function to access private intStandardInspectionID
    @property
    def intStandardInspectionID(self):
        return self._intStandardInspectionID
    
    # setter method 
    @intStandardInspectionID.setter 
    def intStandardInspectionID(self, intStandardInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intStandardInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intStandardInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intStandardInspectionID = intStandardInspectionID    
        
    def Append_StandInspectIDList(self, intObject):
        """ 
        Function Name: Append_StandInspectIDList
        Function Description: This function appends objects to the Standard Inspection ID list
        """    
        self._aintStandardInspectionID.append(intObject)

    def Remove_StandInspectIDList(self, intObject):
        """ 
        Function Name: Remove_StandInspectIDList
        Function Description: This function removes objects in the Standard Inspection ID list
        """    
        self._aintStandardInspectionID.remove(intObject)

    def Get_StandInspectIDList_Obj(self):
        """ 
        Function Name: Get_StandInspectIDList_Obj
        Function Description: This function gets all the objects in the Standard Inspection ID list
        """    
        return self._aintStandardInspectionID                            

    def Add_StandInspect_Query(self):
        """ 
        Function Name: Add_StandInspect_Query
        Function Description: This function gets the max ID inside the TStandardInspections table
        """    
        # Create the sql query string
        sqlTableCol = ("intStandardInspectionID", "intStandardCarabinerInspectionID", "intStandardHandleInspectionID", 
                       "intStandardCaseHousingInspectionID", "intStandardBrakeHousingInspectionID", "intStandardLanyardInspectionID")
        sqlTableName = "TStandardInspections"
        # Execute the query
        StandardInspectionID = StandardInspect.Get_MaxStandardInspectID(self, sqlTableName, sqlTableCol[0])
        StandardInspect.intStandardInspectionID = StandardInspectionID
            
        # Perform the insert query
        aPrimKeyValues = (StandardInspect.intStandardInspectionID, StandardCarabinerInspect.aStandardCarabInsCache[0], 
                          StandardHandelInspect.aStandardHandleInsCache[0], StandardCaseInspect.aStandardCaseInsCache[0],
                          StandardBrakeInspect.aStandardBrakeInsCache[0], StandardLanyardInspect.aStandardLanyardInsCache[0])

        # Set the parameters
        sqlParams = (sqlTableName, sqlTableCol, tuple(aPrimKeyValues))

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)
        
    def Get_MaxStandardInspectID(self, table_name, id_column_name):
        """
        Function Name: Get_MaxStandardInspectID
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
                                            
    def Delete_StandInspection_Data(self):
        """ 
        Function Name: Delete_StandInspection_Data
        Function Description: This function removes all the objects in the Standard Inspection class
        """    
        StandardInspect.aintStandardInspectionID = []
                
                                    
class AutoBelayInspect(AutoBelay, WallLocation, StandardInspect, Inspector):
    """
    Class Name: AutoBelayInspect
    Class Description: This class gets and sets all of the AutoBelay Inspection attributes. 
    """
    # Create class variable shared amongst all AutoBelay Inspection methods
    aintAutoBelayInspectionID = []
    aAutoBelayInspectStatus = []
        
    # Instantiate the following attributes
    def __init__(self, intAutoBelayInspectionID, intAutoBelayID, intWallLocationID, intStandardInspectionID, 
                 intInspectorID, strComment):
        self.intAutoBelayInspectionID = intAutoBelayInspectionID
        self.strComment = strComment
        # Inherits the child class with all the necessary objects
        AutoBelay().__init__(intAutoBelayID)
        WallLocation().__init__(intWallLocationID)
        StandardInspect().__init__(intStandardInspectionID)
        Inspector().__init__(intInspectorID)

    # Property decorator object get function to access private intAutoBelayInspectionID
    @property
    def intAutoBelayInspectionID(self):
        return self._intAutoBelayInspectionID

    # Property decorator object get function to access private strComment
    @property
    def strComment(self):
        return self._strComment
            
    # setter method 
    @intAutoBelayInspectionID.setter 
    def intAutoBelayInspectionID(self, intAutoBelayInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intAutoBelayInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intAutoBelayInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intAutoBelayInspectionID = intAutoBelayInspectionID    

    # setter method 
    @strComment.setter 
    def strComment(self, strComment): 
        # Return true if specified object is of str type
        if not isinstance(strComment, str): 
            raise TypeError('Comment must be a string') 
        # Set the attribute to the value if true
        elif strComment.isascii():
            self._strComment = strComment   

    def Append_AutoBelayInspectIDList(self, intObject):
        """ 
        Function Name: Append_AutoBelayInspectIDList
        Function Description: This function appends objects to the AutoBelay Inspection ID list
        """    
        self.aintAutoBelayInspectionID.append(intObject)

    def Remove_AutoBelayInspectIDList(self, intObject):
        """ 
        Function Name: Remove_AutoBelayInspectIDList
        Function Description: This function removes objects in the AutoBelay Inspection ID list
        """    
        self.aintAutoBelayInspectionID.remove(intObject)

    def Get_AutoBelayInspectIDList_Obj(self):
        """ 
        Function Name: Get_AutoBelayInspectIDList_Obj
        Function Description: This function gets all the objects in the AutoBelay Inspection ID list
        """    
        return self.aintAutoBelayInspectionID   

    def Join_AutoBelayInspectComm_Obj(self, strObject):
        """ 
        Function Name: Join_AutoBelayInspectComm_Obj
        Function Description: This function joins the string objects in the AutoBelay Inspection comment
        """    
        self.strComment = self.strComment + " " + strObject

    def Get_MaxStandardInspectID(self, table_name, id_column_name):
        """
        Function Name: Get_MaxStandardInspectID
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)

    def Delete_AutoBelayInspect_Data(self):
        """ 
        Function Name: Delete_AutoBelayInspect_Data
        Function Description: This function removes all the objects in the AutoBelay Inspect class
        """    
        AutoBelayInspect.aintAutoBelayInspectionID = []
        AutoBelayInspect.aAutoBelayInspectStatus = []
                            
    def Add_AutoBelayInspection_Query(self):
        """ 
        Function Name: Add_AutoBelayInspection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewAutoBelayInspection
        """
        # Create the sql query string
        sqlTableCol = ("intAutoBelayInspectionID", "intAutoBelayID", "intWallLocationID", "intStandardInspectionID", 
                    "intInspectorID", "intInspectionStatusID", "dtmLastInspectionDate", "dtmNextInspectionDate", "strComment")
        sqlTableName = "TAutoBelayInspections"
        
        # Get the max primary key value for the table
        sqlMaxPrimKeyID = StandardInspect.Get_MaxStandardInspectID(self, sqlTableName, sqlTableCol[0])
        self.intAutoBelayInspectionID = sqlMaxPrimKeyID

        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(AutoBelayInspect.aAutoBelayInspectStatus)
            
        # For testing purposes, set the inspector ID to 1
        Inspector.intInspectorID = 1
        
        # Set the inspector ID
        # print(UserLogins.aCurrentUserLogin)
        # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID
        
        # Perform the insert query
        sqlTableValues = (self.intAutoBelayInspectionID, AutoBelay.intAutoBelayID, WallLocation.intWallLocationID, StandardInspect.intStandardInspectionID, 
                        Inspector.intInspectorID, intOverallStatus, AutoBelay.dtmLastInspectionDate, AutoBelay.dtmNextInspectionDate, AutoBelayInspect.strComment)
                        
                
        # Set the parameters
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)
        
    def Add_AutoBelayInspector_Query(self):
        """ 
        Function Name: Add_AutoBelayInspector_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewAutoBelayInspector
        """    
        # Create the sql query string
        sqlTableCol = ("intAutoBelayInspectorID", "intInspectorID", "intAutoBelayID")
        sqlTableName = "TAutoBelayInspectors"
        
        # Get the max primary key value for the table
        sqlMaxPrimKeyID = StandardInspect.Get_MaxStandardInspectID(self, sqlTableName, sqlTableCol[0])

        # # For testing purposes, set the inspector ID to 1
        Inspector.intInspectorID = 1
        
        # Set the inspector ID
        # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID
        
        # Perform the insert query
        sqlTableValues = (sqlMaxPrimKeyID, Inspector.intInspectorID, AutoBelay.intAutoBelayID)
                
        # Set the parameters
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)          
        
    def Add_AutoBelayLocation_Query(self):
        """ 
        Function Name: Add_AutoBelayLocation_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewAutoBelayWallLocation
        """    
        # Create the sql query string
        sqlTableAttr = ("TAutoBelayWallLocations", "intAutoBelayWallLocationID", "intWallLocationID", "intAutoBelayID")
        
        try:
            # Get the max primary key value for the table
            idList = (WallLocation.intWallLocationID, AutoBelay.intAutoBelayID)
            sqlMaxPrimKeyID = AutoBelayInspect.Get_Or_Create_ID(AutoBelayInspect, idList, sqlTableAttr)

            # For testing purposes, set the inspector ID to 1
            Inspector.intInspectorID = 1
            
            # Set the inspector ID
            # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID

            # Get the values
            sqlTableValues = (sqlMaxPrimKeyID, idList[0], idList[1])
                    
            # Set the parameters
            sqlParams = (sqlTableAttr[0], sqlTableAttr[1:], sqlTableValues)
            
            # Get the id list from TAutoBelayWallLocations
            existingRecords = Queries.Get_All_DB_Values(Queries, sqlTableAttr[0])
            
            # Remove duplicates if device is in use
            if AutoBelay.blnDeviceInUse == 'Yes':
                # TODO: Remove duplicates from the database
                for record in existingRecords:
                    if idList[0] == record[1] or idList[1] == record[2]:  # Check for duplicate IDs
                        Queries.Remove_Attribute_Query(Queries, sqlTableAttr[0], sqlTableAttr[1], record[0])

                # Add the new record
                Queries.dbExeUSP_AddValues(Queries, sqlParams)
            else:
                # Check if an update is needed
                updateNeeded = not any(idList == record[1:3] for record in existingRecords)
                if updateNeeded:
                    Queries.dbExeUSP_AddValues(Queries, sqlParams)
                    
        except Exception as e:
            print(f"Error in Add_AutoBelayLocation_Query: {e}")

    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = AutoBelayInspect.Check_Duplicate(AutoBelayInspect, item_list, sql_tuple)
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

class AutoBelayReserviceReport(AutoBelayInspect):
    """
    Class Name: AutoBelayReserviceReport
    Class Description: This class gets and sets all of the AutoBelay Reservice Report attributes. 
    """
    # Create class variable shared amongst all AutoBelay Reservice methods
    aintAutoBelayReserviceReportID = []

    # Instantiate the following attributes
    def __init__(self, intAutoBelayReserviceReportID, intAutoBelayInspectionID, intInspectorID, dtmReportDate):
        self.intAutoBelayReserviceReportID = intAutoBelayReserviceReportID
        self.dtmReportDate = dtmReportDate
        # Inherits the child class with all the necessary objects
        AutoBelayInspect().__init__(intAutoBelayInspectionID)
        Inspector().__init__(intInspectorID)

    # Property decorator object get function to access private intAutoBelayReserviceReportID
    @property
    def intAutoBelayReserviceReportID(self):
        return self._intAutoBelayReserviceReportID

    # Property decorator object get function to access private dtmReportDate
    @property
    def dtmReportDate(self):
        return self._dtmReportDate
            
    # setter method 
    @intAutoBelayReserviceReportID.setter 
    def intAutoBelayReserviceReportID(self, intAutoBelayReserviceReportID): 
        # Return true if specified object is of int type
        if not isinstance(intAutoBelayReserviceReportID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intAutoBelayReserviceReportID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intAutoBelayReserviceReportID = intAutoBelayReserviceReportID    

    # setter method 
    @dtmReportDate.setter 
    def dtmReportDate(self, dtmReportDate):              
        # Return true if specified object is of str type
        if not isinstance(dtmReportDate, str): 
            raise TypeError('Report Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmReportDate.isspace(): 
            raise ValueError('Report Date cannot be empty')       
        # Convert the date to string
        dtmReportDate = datetime.strptime(dtmReportDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmReportDate, date): 
            raise TypeError('Report Date must be a valid date') 
        # Convert the date back to string
        dtmReportDate = str(dtmReportDate)

        self._dtmReportDate = dtmReportDate  

    def Append_AutoBelay_ReserviceReportID_List(self, intObject):
        """ 
        Function Name: Append_AutoBelay_ReserviceReportID_List
        Function Description: This function appends objects to the AutoBelay Reservice Report ID list
        """    
        self.aintAutoBelayReserviceReportID.append(intObject)

    def Remove_AutoBelay_ReserviceReportID_List(self, intObject):
        """ 
        Function Name: Remove_AutoBelay_ReserviceReportID_List
        Function Description: This function removes objects in the AutoBelay Reservice Report ID list
        """    
        self.aintAutoBelayReserviceReportID.remove(intObject)

    def Get_AutoBelay_ReserviceReportID_List_Obj(self):
        """ 
        Function Name: Get_AutoBelay_ReserviceReportID_List_Obj
        Function Description: This function gets all the objects in the AutoBelay Reservice Report ID list
        """    
        return self.aintAutoBelayReserviceReportID   

    def Delete_AutoBelay_ReserviceReport_Data(self):
        """ 
        Function Name: Delete_AutoBelay_ReserviceReport_Data
        Function Description: This function removes all the objects in the AutoBelay Reservice Report class
        """    
        AutoBelayReserviceReport.aintAutoBelayReserviceReportID = []

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
                                
    def Add_AutoBelay_ReserviceReport_Query(self):
        """ 
        Function Name: Add_AutoBelay_ReserviceReport_Query
        Function Description: This function updated the database with all of the necessary objects
        """
        # Get todays date
        dtmToday = datetime.now().date()
        self.dtmReportDate = str(dtmToday)
                
        # Create the sql query string
        sqlTableCol = ("intAutoBelayReserviceReportID", "intAutoBelayInspectionID", "intInspectorID", "dtmReportDate")
        sqlTableName = "TAutoBelayReserviceReports"
        
        # Get the max primary key value for the table
        sqlMaxPrimKeyID = AutoBelayReserviceReport.Get_Max_Primary_Key(self, sqlTableName, sqlTableCol[0])

        # For testing purposes, set the inspector ID to 1
        Inspector.intInspectorID = 1
        
        # Set the inspector ID
        # print(UserLogins.aCurrentUserLogin)
        # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID
        
        # Get the max primary key value for the table
        AutoBelayInspectionID = AutoBelayReserviceReport.Get_Max_Primary_Key(self, "TAutoBelayInspections", "intAutoBelayInspectionID")

        if AutoBelayInspectionID > 1:
            # Perform the insert query
            sqlTableValues = (sqlMaxPrimKeyID, self.intAutoBelayInspectionID, Inspector.intInspectorID, self.dtmReportDate)
        else:
            sqlTableValues = (sqlMaxPrimKeyID, AutoBelayInspectionID, Inspector.intInspectorID, self.dtmReportDate)            
        # Set the parameters
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)
        
    def Update_AutoBelay_ReserviceReport_Query(self):
        """ 
        Function Name: Update_AutoBelay_ReserviceReport_Query
        Function Description: This function updated the database with all of the necessary objects
        """
        # Get todays date
        dtmToday = datetime.now().date()
        self.dtmReportDate = str(dtmToday)
                
        # Create the sql query string
        sqlTableCol = ("intAutoBelayReserviceReportID", "intAutoBelayInspectionID", "intInspectorID", "dtmReportDate")
        sqlTableName = "TAutoBelayReserviceReports"
        sqlViewName = "vABInspectID_OutForReservice"
        
        # Get the max primary key value for the table
        sqlABInspectValues = Queries.Get_All_DB_Values(self, sqlViewName) or None
        sqlABReserviceReportValues = Queries.Get_All_DB_Values(self, sqlTableName)
        
        # For testing purposes, set the inspector ID to 1
        Inspector.intInspectorID = 1
        
        # Set the inspector ID
        # print(UserLogins.aCurrentUserLogin)
        # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID

        # Process each inspection value
        if sqlABInspectValues is not None:
            existingReportIDs = [report[0] for report in sqlABReserviceReportValues]
            for inspectValue in sqlABInspectValues:
                inspectionID = inspectValue[0]

                if inspectionID not in existingReportIDs:
                    self.intAutoBelayInspectionID = inspectionID
                    AutoBelayReserviceReport.Add_AutoBelay_ReserviceReport_Query(self)
                elif self.blnDeviceInUse != "Out For Reservice":
                    Queries.Remove_Attribute_Query(Queries, sqlTableName, sqlTableCol[0], inspectionID)
                else:
                    sqlTableValues = (inspectionID, self.intAutoBelayInspectionID, Inspector.intInspectorID, self.dtmReportDate)
                    sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], inspectionID)
                    Queries.dbExeUSP_UpdateValues(Queries, sqlParams)
        else:
            AutoBelayReserviceReport.Add_AutoBelay_ReserviceReport_Query(self)

class Reports(UserLogins):
    # Create class variable shared amongst all methods/objects in the Reports class
    aintUserSentReportID = []
    adtmDateSent = []
    astrFileName = []
    astrReceiverEmail = []
    
    # Instantiate the following attributes
    def __init__(self, intUserSentReportID, intUserLoginID, dtmDateSent, strFileName, strReceiverEmail):
        self.intUserSentReportID = intUserSentReportID
        self.dtmDateSent = dtmDateSent
        self.strFileName = strFileName
        self.strReceiverEmail = strReceiverEmail
        # Inherits the child class with all the necessary objects
        super().__init__(intUserLoginID)

    # Property decorator object get function to access private intUserSentReportID
    @property
    def intUserSentReportID(self):
        return self.intUserSentReportID

    # Property decorator object get function to access private dtmDateSent
    @property
    def dtmDateSent(self):
        return self._dtmDateSent

    # Property decorator object get function to access private strFileName
    @property
    def strFileName(self):
        return self._strFileName    

    # Property decorator object get function to access private strReceiverEmail
    @property
    def strReceiverEmail(self):
        return self._strReceiverEmail
                
    # setter method 
    @intUserSentReportID.setter 
    def intUserSentReportID(self, intUserSentReportID): 
        # Return true if specified object is of int type
        if not isinstance(intUserSentReportID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intUserSentReportID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intUserSentReportID = intUserSentReportID    

    # setter method 
    @dtmDateSent.setter 
    def dtmDateSent(self, dtmDateSent): 
        # Return true if specified object is of str type
        if not isinstance(dtmDateSent, str): 
            raise TypeError('Date Sent must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmDateSent.isspace(): 
            raise ValueError('Date Sent cannot be empty')       
        # Convert the date to string
        dtmDateSent = datetime.strptime(dtmDateSent, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmDateSent, date): 
            raise TypeError('Date Sent must be a valid date') 
        # Convert the date back to string
        dtmDateSent = str(dtmDateSent)

        self._dtmDateSent = dtmDateSent  
        
    # setter method 
    @strFileName.setter 
    def strFileName(self, strFileName): 
        # Return true if specified object is of str type
        if not isinstance(strFileName, str): 
            raise TypeError('File Name must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if strFileName.isspace(): 
            raise ValueError('File Name cannot be empty') 
        # Set the attribute to the value if true
        elif strFileName.isascii():
            self._strFileName = strFileName   

    # setter method 
    @strReceiverEmail.setter 
    def strReceiverEmail(self, strReceiverEmail): 
        blnFLAG = bool(False)
        blnFLAG = is_email(strReceiverEmail,  allow_gtld=True)
        # Return true if specified object is of str type
        if not isinstance(strReceiverEmail, str): 
            raise TypeError('Email must be an string') 
        # Check if the value is empty, otherwise check if the value is isascii
        if strReceiverEmail.isspace(): 
            raise ValueError('Email cannot be empty') 
        # Set the attribute to the value if true
        if strReceiverEmail.isascii() and blnFLAG is True:
            self._strReceiverEmail = strReceiverEmail                    
            
    def Append_UserSentReportIDList(self, intObject):
        """ 
        Function Name: Append_UserSentReportIDList
        Function Description: This function appends objects to the User Sent Report ID list
        """    
        self.aintUserSentReportID.append(intObject)

    def Remove_UserSentReportIDList(self, intObject):
        """ 
        Function Name: Remove_UserSentReportIDList
        Function Description: This function removes objects in the User Sent Report ID list
        """    
        self.aintUserSentReportID.remove(intObject)

    def Get_UserSentReportIDList_Obj(self):
        """ 
        Function Name: Get_UserSentReportIDList_Obj
        Function Description: This function gets all the objects in the User Sent Report ID list
        """    
        return self.aintUserSentReportID   

    def Append_UsrSntReprt_DateSent_List(self, intObject):
        """ 
        Function Name: Append_UsrSntReprt_DateSent_List
        Function Description: This function appends objects to the User Sent Report Date Sent list
        """    
        self.adtmDateSent.append(intObject)

    def Remove_UsrSntReprt_DateSent_List(self, intObject):
        """ 
        Function Name: Remove_UsrSntReprt_DateSent_List
        Function Description: This function removes objects in the User Sent Report Date Sent list
        """    
        self.adtmDateSent.remove(intObject)

    def Get_UsrSntReprt_DateSent_List_Obj(self):
        """ 
        Function Name: Get_UsrSntReprt_DateSent_List_Obj
        Function Description: This function gets all the objects in the User Sent Report Date Sent list
        """    
        return self.adtmDateSent  
    
    def Append_UsrSntReprt_FileName_List(self, intObject):
        """ 
        Function Name: Append_UsrSntReprt_FileName_List
        Function Description: This function appends objects to the User Sent Report File Name list
        """    
        self.astrFileName.append(intObject)

    def Remove_UserSentReportIDList(self, intObject):
        """ 
        Function Name: Remove_UserSentReportIDList
        Function Description: This function removes objects in the User Sent Report File Name list
        """    
        self.astrFileName.remove(intObject)

    def Get_UsrSntReprt_FileName_List_Obj(self):
        """ 
        Function Name: Get_UsrSntReprt_FileName_List_Obj
        Function Description: This function gets all the objects in the User Sent Report File Name list
        """    
        return self.astrFileName  
    
    def Append_UsrSntReprt_ReEmail_ListList(self, intObject):
        """ 
        Function Name: Append_UsrSntReprt_ReEmail_ListList
        Function Description: This function appends objects to the User Sent Report Receiver Email list
        """    
        self.astrReceiverEmail.append(intObject)

    def Remove_UsrSntReprt_ReEmail_ListList(self, intObject):
        """ 
        Function Name: Remove_UsrSntReprt_ReEmail_ListList
        Function Description: This function removes objects in the User Sent Report Receiver Email list
        """    
        self.astrReceiverEmail.remove(intObject)

    def Get_UsrSntReprt_ReEmail_List_Obj(self):
        """ 
        Function Name: Get_UsrSntReprt_ReEmail_List_Obj
        Function Description: This function gets all the objects in the User Sent Report Receiver Email list
        """    
        return self.astrReceiverEmail  
                
    def Get_UserSentReportData(self):
        """ 
        Function Name: Get_UserSentReportData
        Function Description: This function gets all the objects in the TUserSentReports table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TUserSentReports"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the Hose Data List
        for i in range(len(QueryResultList)):
            Reports.Append_UserSentReportIDList(self, QueryResultList[i][0])
            Reports.Append_UsrSntReprt_DateSent_List(self, QueryResultList[i][2]) 
            Reports.Append_UsrSntReprt_FileName_List(self, QueryResultList[i][3]) 
            Reports.Append_UsrSntReprt_ReEmail_ListList(self, QueryResultList[i][4]) 


class CustomRopeSystem():
    """
    Class Name: CustomRopeSystem
    Class Description: This class gets and sets all of the CustomRopeSystem attributes. 
    """
    # Create class variable shared amongst all CustomRopeSystem methods
    aintRopeSystemIDCache = []
    astrRopeSystemNameCache = []
    astrComplexityCache = []
    astrPreTiedKnotCache = []
    aintConnectorCountCache = []
    astrFirstConnectorTypeCache = []
    astrSecondConnectorTypeCache = []
    astrDeviceTypeCache = []

    # Instantiate the following attributes
    def __init__(self, intRopeSystemID, strRopeSystemName, strComplexity, strPreTiedKnot, intConnectorCount, 
                strFirstConnectorType, strSecondConnectorType, strDeviceType,):
        self.intRopeSystemID = intRopeSystemID
        self.strRopeSystemName = strRopeSystemName
        self.strComplexity = strComplexity
        self.strPreTiedKnot = strPreTiedKnot
        self.intConnectorCount = intConnectorCount
        self.strFirstConnectorType = strFirstConnectorType
        self.strSecondConnectorType = strSecondConnectorType
        self.strDeviceType = strDeviceType

    # Property decorator object get function to access private intRopeSystemID
    @property
    def intRopeSystemID(self):
        return self._intRopeSystemID

    # Property decorator object get function to access private strRopeSystemName
    @property
    def strRopeSystemName(self):
        return self._strRopeSystemName
    
    # Property decorator object get function to access private strComplexity
    @property
    def strComplexity(self):
        return self._strComplexity

    # Property decorator object get function to access private strPreTiedKnot
    @property
    def strPreTiedKnot(self):
        return self._strPreTiedKnot
    
    # Property decorator object get function to access private intConnectorCount
    @property
    def intConnectorCount(self):
        return self._intConnectorCount

    # Property decorator object get function to access private strFirstConnectorType
    @property
    def strFirstConnectorType(self):
        return self._strFirstConnectorType
    
    # Property decorator object get function to access private strSecondConnectorType
    @property
    def strSecondConnectorType(self):
        return self._strSecondConnectorType
    
    # Property decorator object get function to access private strDeviceType
    @property
    def strDeviceType(self):
        return self._strDeviceType
        
    # setter method 
    @intRopeSystemID.setter 
    def intRopeSystemID(self, intRopeSystemID): 
        # Return true if specified object is of int type
        if not isinstance(intRopeSystemID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intRopeSystemID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intRopeSystemID = intRopeSystemID    

    # setter method 
    @strRopeSystemName.setter 
    def strRopeSystemName(self, strRopeSystemName): 
        # Return true if specified object is of str type
        if not isinstance(strRopeSystemName, str): 
            raise TypeError('Rope System Name must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strRopeSystemName.isspace(): 
            raise ValueError('Rope System Name cannot be empty') 
        # Set the attribute to the value if true
        if strRopeSystemName.isascii():
            self._strRopeSystemName = strRopeSystemName 
            # Set the global class bool to true
            Bool_Flag.Set_RopeSystem_Bool_Value_True(Bool_Flag)
            
    # setter method 
    @strComplexity.setter 
    def strComplexity(self, strComplexity): 
        # Return true if specified object is of str type
        if not isinstance(strComplexity, str): 
            raise TypeError('Complexity Type must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strComplexity.isspace(): 
            raise ValueError('Complexity Type cannot be empty') 
        # Set the attribute to the value if true
        if strComplexity.isascii():
            self._strComplexity = strComplexity  

    # setter method 
    @strPreTiedKnot.setter 
    def strPreTiedKnot(self, strPreTiedKnot): 
        # Return true if specified object is of str type
        if not isinstance(strPreTiedKnot, str): 
            raise TypeError('Pre-tied Knots must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strPreTiedKnot.isspace(): 
            raise ValueError('Pre-tied Knots cannot be empty') 
        # Set the attribute to the value if true
        if strPreTiedKnot.isascii():
            self._strPreTiedKnot = strPreTiedKnot
            
    # setter method 
    @intConnectorCount.setter 
    def intConnectorCount(self, intConnectorCount): 
        # Return true if specified object is of int type
        if not isinstance(intConnectorCount, int): 
            raise TypeError('Connector Count must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intConnectorCount < 0: 
            raise ValueError('Connector Count cannot be negative') 

        self._intConnectorCount = intConnectorCount     

    # setter method 
    @strFirstConnectorType.setter 
    def strFirstConnectorType(self, strFirstConnectorType): 
        # Return true if specified object is of str type
        if not isinstance(strFirstConnectorType, str): 
            raise TypeError('First Connector must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strFirstConnectorType.isspace(): 
            raise ValueError('First Connector cannot be empty') 
        # Set the attribute to the value if true
        if strFirstConnectorType.isascii():
            self._strFirstConnectorType = strFirstConnectorType 

    # setter method 
    @strSecondConnectorType.setter 
    def strSecondConnectorType(self, strSecondConnectorType): 
        # Return true if specified object is of str type
        if not isinstance(strSecondConnectorType, str): 
            raise TypeError('Second Connector must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strSecondConnectorType.isspace(): 
            raise ValueError('Second Connector cannot be empty') 
        # Set the attribute to the value if true
        if strSecondConnectorType.isascii():
            self._strSecondConnectorType = strSecondConnectorType 
                        
    # setter method 
    @strDeviceType.setter
    def strDeviceType(self, strDeviceType):
        # Check if the input is a string
        if not isinstance(strDeviceType, str):
            raise TypeError('Device Type must be a string')

        # Check if the string is empty or consists only of whitespace
        if strDeviceType.isspace() or not strDeviceType:
            raise ValueError('Device Type Status cannot be empty')

        # Check if the string is alpha or hyphenated
        if all(subpart.isalpha() for subpart in strDeviceType.split('-')):
            self._strDeviceType = strDeviceType
        else:
            raise ValueError('Device Type must be a string of letters or hyphenated words')    

    def Append_RopeSystemIDList(self, intObject):
        """ 
        Function Name: Append_RopeSystemIDList
        Function Description: This function appends objects to the Rope System ID list
        """    
        self.aintRopeSystemIDCache.append(intObject)

    def Remove_RopeSystemIDList(self, intObject):
        """ 
        Function Name: Remove_RopeSystemIDList
        Function Description: This function removes objects in the Rope System ID list
        """    
        self.aintRopeSystemIDCache.remove(intObject)

    def Get_RopeSystemIDList_Obj(self):
        """ 
        Function Name: Get_RopeSystemIDList_Obj
        Function Description: This function gets all the objects in the Rope System ID list
        """    
        return self.aintRopeSystemIDCache     

    def Append_RopeSystem_NameList(self, strObject):
        """ 
        Function Name: Append_RopeSystem_NameList
        Function Description: This function appends objects to the Name list
        """    
        self.astrRopeSystemNameCache.append(strObject)

    def Remove_RopeSystem_NameList(self, strObject):
        """ 
        Function Name: Remove_RopeSystem_NameList
        Function Description: This function removes objects in the Name list
        """    
        self.astrRopeSystemNameCache.remove(strObject)

    def Get_RopeSystem_NameList_Obj(self):
        """ 
        Function Name: Get_RopeSystem_NameList_Obj
        Function Description: This function gets all the objects in the Name list
        """    
        return self.astrRopeSystemNameCache
    
    def Append_RopeSystem_ComplexityList(self, strObject):
        """ 
        Function Name: Append_RopeSystem_ComplexityList
        Function Description: This function appends objects to the Complexity list
        """    
        self.astrComplexityCache.append(strObject)

    def Remove_RopeSystem_ComplexityList(self, strObject):
        """ 
        Function Name: Remove_RopeSystem_ComplexityList
        Function Description: This function removes objects in the Complexity list
        """    
        self.astrComplexityCache.remove(strObject)

    def Get_RopeSystem_ComplexityList_Obj(self):
        """ 
        Function Name: Get_RopeSystem_ComplexityList_Obj
        Function Description: This function gets all the objects in the Complexity list
        """    
        return self.astrComplexityCache 

    def Append_RopeSystem_PreTiedKnots_List(self, strObject):
        """ 
        Function Name: Append_RopeSystem_PreTiedKnots_List
        Function Description: This function appends objects to the Pre-tied Knots list
        """    
        self.astrPreTiedKnotCache.append(strObject)

    def Remove_RopeSystem_PreTiedKnots_List(self, strObject):
        """ 
        Function Name: Remove_RopeSystem_PreTiedKnots_List
        Function Description: This function removes objects in the Pre-tied Knots list
        """    
        self.astrPreTiedKnotCache.remove(strObject)

    def Get_RopeSystem_PreTiedKnots_List_Obj(self):
        """ 
        Function Name: Get_RopeSystem_PreTiedKnots_List_Obj
        Function Description: This function gets all the objects in the Pre-tied Knots list
        """    
        return self.astrPreTiedKnotCache 
    
    def Append_RopeSystem_ConnectorCountList(self, strObject):
        """ 
        Function Name: Append_RopeSystem_ConnectorCountList
        Function Description: This function appends objects to the Connector Count list
        """    
        self.aintConnectorCountCache.append(strObject)

    def Remove_RopeSystem_ConnectorCountList(self, strObject):
        """ 
        Function Name: Remove_RopeSystem_ConnectorCountList
        Function Description: This function removes objects in the Connector Count list
        """    
        self.aintConnectorCountCache.remove(strObject)

    def Get_RopeSystem_ConnectorCountList_Obj(self):
        """ 
        Function Name: Get_RopeSystem_ConnectorCountList_Obj
        Function Description: This function gets all the objects in the Connector Count list
        """    
        return self.aintConnectorCountCache  
    
    def Append_RopeSystem_FirstConnectorList(self, strObject):
        """ 
        Function Name: Append_RopeSystem_FirstConnectorList
        Function Description: This function appends objects to the First Connector list
        """    
        self.astrFirstConnectorTypeCache.append(strObject)

    def Remove_RopeSystem_FirstConnectorList(self, strObject):
        """ 
        Function Name: Remove_RopeSystem_FirstConnectorList
        Function Description: This function removes objects in the First Connector list
        """    
        self.astrFirstConnectorTypeCache.remove(strObject)

    def Get_RopeSystem_FirstConnectorList_Obj(self):
        """ 
        Function Name: Get_RopeSystem_FirstConnectorList_Obj
        Function Description: This function gets all the objects in the First Connector list
        """    
        return self.astrFirstConnectorTypeCache

    def Append_RopeSystem_SecondConnectorList(self, strObject):
        """ 
        Function Name: Append_RopeSystem_SecondConnectorList
        Function Description: This function appends objects to the Second Connector list
        """    
        self.astrSecondConnectorTypeCache.append(strObject)

    def Remove_RopeSystem_SecondConnectorList(self, strObject):
        """ 
        Function Name: Remove_RopeSystem_SecondConnectorList
        Function Description: This function removes objects in the Second Connector list
        """    
        self.astrSecondConnectorTypeCache.remove(strObject)

    def Get_RopeSystem_SecondConnectorList_Obj(self):
        """ 
        Function Name: Get_RopeSystem_SecondConnectorList_Obj
        Function Description: This function gets all the objects in the Second Connector list
        """    
        return self.astrSecondConnectorTypeCache
    
    def Append_RopeSystem_DeviceList(self, strObject):
        """ 
        Function Name: Append_RopeSystem_DeviceList
        Function Description: This function appends objects to the Rope Length list
        """    
        self.astrDeviceTypeCache.append(strObject)

    def Remove_RopeSystem_DeviceDList(self, strObject):
        """ 
        Function Name: Remove_RopeSystem_DeviceDList
        Function Description: This function removes objects in the Rope Length list
        """    
        self.astrDeviceTypeCache.remove(strObject)

    def Get_RopeSystem_DeviceList_Obj(self):
        """ 
        Function Name: Get_RopeSystem_DeviceList_Obj
        Function Description: This function gets all the objects in the Rope Length list
        """    
        return self.astrDeviceTypeCache
                        
    def Get_CustomRopeSystem_Data(self):
        """ 
        Function Name: Get_CustomRopeSystem_Data
        Function Description: This function gets all the objects in the CustomRopeSystem table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TCustomRopeSystems"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # First check if the contents are found and if yes, proceed to get the contents of the table
        if QueryResultList is not None:
            # Append the Auto Belay Data List
            for i in range(len(QueryResultList)):
                CustomRopeSystem.Append_RopeSystemIDList(self, QueryResultList[i][0])
                CustomRopeSystem.Append_RopeSystem_NameList(self, QueryResultList[i][1])
                CustomRopeSystem.Append_RopeSystem_ComplexityList(self, QueryResultList[i][2])
                CustomRopeSystem.Append_RopeSystem_PreTiedKnots_List(self, QueryResultList[i][3]) 
                CustomRopeSystem.Append_RopeSystem_ConnectorCountList(self, QueryResultList[i][4]) 
                CustomRopeSystem.Append_RopeSystem_FirstConnectorList(self, QueryResultList[i][5])
                CustomRopeSystem.Append_RopeSystem_SecondConnectorList(self, QueryResultList[i][6]) 
                CustomRopeSystem.Append_RopeSystem_DeviceList(self, QueryResultList[i][7]) 

    def Set_CustomRopeSystem_Selection(self):
        """ 
        Function Name: Set_CustomRopeSystem_Selection
        Function Description: This function will set the selection name from the user and will update the 
        class objects with the data from the database.
        """    
        # First get the selection from the user 
        for i, item in enumerate(self.astrRopeSystemNameCache):
            if self.strRopeSystemName == item:
                # Assign the iterable num to the ID num and assign the objects to the desired data sets    
                self.intRopeSystemID = self.aintRopeSystemIDCache[i]                
                if not self.strRopeSystemName:              
                    self.strRopeSystemName = self.astrRopeSystemNameCache[i]      
                self.strComplexity = self.astrComplexityCache[i]
                self.strPreTiedKnot = self.astrPreTiedKnotCache[i]
                self.intConnectorCount = self.aintConnectorCountCache[i]
                self.strFirstConnectorType = self.astrFirstConnectorTypeCache[i]
                self.strSecondConnectorType = self.astrSecondConnectorTypeCache[i]
                self.strDeviceType = self.astrDeviceTypeCache[i]
                
                # Set the global class bool to true
                Bool_Flag.Set_RopeSystem_Bool_Value_True(Bool_Flag)    
                break

    def Set_CustomRopeSystem_Data(self):
        """ 
        Function Name: Set_CustomRopeSystem_Data
        Function Description: This function will set the class objects for the device when selected
        """    
        # First get the selection from the user 
        for i, item in enumerate(self.astrRopeSystemNameCache):
            if self.strRopeSystemName == item:
                # Assign the iterable num to the ID num and assign the objects to the desired data sets    
                self.intRopeSystemID = self.aintRopeSystemIDCache[i]                              
                self.strRopeSystemName = self.astrRopeSystemNameCache[i]      
                self.strComplexity = self.astrComplexityCache[i]
                self.strPreTiedKnot = self.astrPreTiedKnotCache[i]
                self.intConnectorCount = self.aintConnectorCountCache[i]
                self.strFirstConnectorType = self.astrFirstConnectorTypeCache[i]
                self.strSecondConnectorType = self.astrSecondConnectorTypeCache[i]
                self.strDeviceType = self.astrDeviceTypeCache[i]

                # Set the global class bool to true
                Bool_Flag.Set_RopeSystem_Bool_Value_True(Bool_Flag)                    
                break

    def Add_CustomRopeSystem_Query(self):
        """ 
        Function Name: Add_CustomRopeSystem_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Create the sql query string
        sqlTableCol = ("intRopeSystemID", "strRopeSystemName", "strComplexity", "strPreTiedKnot", "intConnectorCount", 
                    "strFirstConnectorType", "strSecondConnectorType", "strDeviceType")   
        sqlTableName = "TCustomRopeSystems"  

        # Set the Table values and the params tuple
        sqlTableValues = (self.intRopeSystemID, self.strRopeSystemName, self.strComplexity, self.strPreTiedKnot, self.intConnectorCount, 
                        self.strFirstConnectorType, self.strSecondConnectorType, self.strDeviceType)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

        # Reload the data after user submits entry
        CustomRopeSystem.Delete_CustomRopeSystem_Data(CustomRopeSystem)
        CustomRopeSystem.Get_CustomRopeSystem_Data(CustomRopeSystem)
                
    def Update_NewCustomRopeSystem_Query(self):
        """ 
        Function Name: Update_NewCustomRopeSystem_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Create the sql query string
        sqlTableCol = ("intRopeSystemID", "strRopeSystemName", "strComplexity", "strPreTiedKnot", "intConnectorCount", 
                    "strFirstConnectorType", "strSecondConnectorType", "strDeviceType")   
        sqlTableName = "TCustomRopeSystems"  

        # Set the Table values and the params tuple
        sqlTableValues = (self.intRopeSystemID, self.strRopeSystemName, self.strComplexity, self.strPreTiedKnot, self.intConnectorCount, 
                        self.strFirstConnectorType, self.strSecondConnectorType, self.strDeviceType)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)       

        # Execute the stored procedure
        Queries.dbExeUSP_UpdateValues(Queries, sqlParams)

        # Reload the data after user submits entry
        CustomRopeSystem.Delete_CustomRopeSystem_Data(CustomRopeSystem)
        CustomRopeSystem.Get_CustomRopeSystem_Data(CustomRopeSystem)
        
    def Set_Global_CustomRopeSystem_Attributes(self):
        """ 
        Function Name: Set_Global_CustomRopeSystem_Attributes
        Function Description: This function sets CustomRopeSystem attributes once the user proceeds with adding a new
        CustomRopeSystem to the database.
        """    
        CustomRopeSystem.strRopeSystemName = self.strRopeSystemName
        CustomRopeSystem.strComplexity = self.strComplexity
        CustomRopeSystem.strPreTiedKnot = self.strPreTiedKnot
        CustomRopeSystem.intConnectorCount = self.intConnectorCount
        CustomRopeSystem.strFirstConnectorType = self.strFirstConnectorType
        CustomRopeSystem.strSecondConnectorType = self.strSecondConnectorType
        CustomRopeSystem.strDeviceType = self.strDeviceType

    def Delete_CustomRopeSystem_Data(self):
        """ 
        Function Name: Delete_CustomRopeSystem_Data
        Function Description: This function removes all the objects in the CustomRopeSystem class
        """    
        CustomRopeSystem.aintRopeSystemIDCache = []
        CustomRopeSystem.astrRopeSystemNameCache = []   
        CustomRopeSystem.astrComplexityCache = []
        CustomRopeSystem.astrPreTiedKnotCache = []
        CustomRopeSystem.aintConnectorCountCache = []
        CustomRopeSystem.astrFirstConnectorTypeCache = []
        CustomRopeSystem.astrSecondConnectorTypeCache = []
        CustomRopeSystem.astrDeviceTypeCache = []


class Ropes():
    """
    Class Name: Ropes
    Class Description: This class gets and sets all of the Ropes attributes. 
    """
    # Create class variable shared amongst all Ropes methods
    aintRopeIDCache = []
    astrSerialNumCache = []
    astrBumperNumCache = []
    astrDiameterCache = []
    astrRopeLengthCache = []
    astrElasticityCache = []
    astrManufactureNameCache = []
    adtmManufactureDateCache = []
    adtmInstallationDateCache = []
    adtmLastInspectionDateCache = []
    adtmNextInspectionDateCache = []
    astrEquipInUseCache = []

    # Instantiate the following attributes
    def __init__(self, intRopeID, strSerialNum, strBumperNum, strRopeLength, strDiameter, strElasticity,
                strManufactureName, dtmManufactureDate, dtmInstallationDate, dtmLastInspectionDate, 
                dtmNextInspectionDate, strEquipInUse):
        self.intRopeID = intRopeID
        self.strSerialNum = strSerialNum
        self.strBumperNum = strBumperNum
        self.strRopeLength = strRopeLength
        self.strDiameter = strDiameter
        self.strElasticity = strElasticity
        self.strManufactureName = strManufactureName
        self.dtmManufactureDate = dtmManufactureDate
        self.dtmInstallationDate = dtmInstallationDate
        self.dtmLastInspectionDate = dtmLastInspectionDate
        self.dtmNextInspectionDate = dtmNextInspectionDate
        self.strEquipInUse = strEquipInUse

    # Property decorator object get function to access private intRopeID
    @property
    def intRopeID(self):
        return self._intRopeID

    # Property decorator object get function to access private strSerialNum
    @property
    def strSerialNum(self):
        return self._strSerialNum

    # Property decorator object get function to access private strBumperNum
    @property
    def strBumperNum(self):
        return self._strBumperNum

    # Property decorator object get function to access private strRopeLength
    @property
    def strRopeLength(self):
        return self._strRopeLength
        
    # Property decorator object get function to access private strManufactureName
    @property
    def strManufactureName(self):
        return self._strManufactureName
        
    # Property decorator object get function to access private dtmManufactureDate
    @property
    def dtmManufactureDate(self):
        return self._dtmManufactureDate

    # Property decorator object get function to access private dtmInstallationDate
    @property
    def dtmInstallationDate(self):
        return self._dtmInstallationDate

    # Property decorator object get function to access private dtmLastInspectionDate
    @property
    def dtmLastInspectionDate(self):
        return self._dtmLastInspectionDate

    # Property decorator object get function to access private dtmNextInspectionDate
    @property
    def dtmNextInspectionDate(self):
        return self._dtmNextInspectionDate

    # Property decorator object get function to access private strEquipInUse
    @property
    def strEquipInUse(self):
        return self._strEquipInUse

    # setter method 
    @intRopeID.setter 
    def intRopeID(self, intRopeID): 
        # Return true if specified object is of int type
        if not isinstance(intRopeID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intRopeID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intRopeID = intRopeID    

    # setter method 
    @strSerialNum.setter 
    def strSerialNum(self, strSerialNum): 
        # Return true if specified object is of str type
        if not isinstance(strSerialNum, str): 
            raise TypeError('Serial Number must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strSerialNum.isspace(): 
            raise ValueError('Serial Number cannot be empty') 
        # Set the attribute to the value if true
        if strSerialNum.isascii():
            self._strSerialNum = strSerialNum  
            # Set the global class bool to true
            Bool_Flag.Set_Rope_Bool_Value_True(Bool_Flag)

    # setter method 
    @strBumperNum.setter 
    def strBumperNum(self, strBumperNum): 
        # Return true if specified object is of str type
        if not isinstance(strBumperNum, str): 
            raise TypeError('Bumper Number must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strBumperNum.isspace(): 
            raise ValueError('Bumper Number cannot be empty') 
        # Set the attribute to the value if true
        if strBumperNum.isascii():
            self._strBumperNum = strBumperNum   

    # setter method 
    @strRopeLength.setter 
    def strRopeLength(self, strRopeLength): 
        # Return true if specified object is of str type
        if not isinstance(strRopeLength, str): 
            raise TypeError('Rope Length must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strRopeLength.isspace(): 
            raise ValueError('Rope Length cannot be empty') 
        # Set the attribute to the value if true
        if strRopeLength.isascii():
            self._strRopeLength = strRopeLength    

    # setter method 
    @strManufactureName.setter 
    def strManufactureName(self, strManufactureName):   
        # Return true if specified object is of str type
        if not isinstance(strManufactureName, str): 
            raise TypeError('Manufacture Name must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if strManufactureName.isspace(): 
            raise ValueError('Manufacture Name cannot be empty') 
        # Set the attribute to the value if true
        if strManufactureName.isascii():
            self._strManufactureName = strManufactureName   
            
    # setter method 
    @dtmManufactureDate.setter 
    def dtmManufactureDate(self, dtmManufactureDate): 
        # Return true if specified object is of str type
        if not isinstance(dtmManufactureDate, str): 
            raise TypeError('Manufacture Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmManufactureDate.isspace(): 
            raise ValueError('Manufacture Date cannot be empty')       
        # Convert the date to string
        dtmManufactureDate = datetime.strptime(dtmManufactureDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmManufactureDate, date): 
            raise TypeError('Manufacture Date must be a valid date') 
        # Convert the date back to string
        dtmManufactureDate = str(dtmManufactureDate)

        self._dtmManufactureDate = dtmManufactureDate         
                
    # setter method 
    @dtmInstallationDate.setter 
    def dtmInstallationDate(self, dtmInstallationDate): 
        # Return true if specified object is of str type
        if not isinstance(dtmInstallationDate, str): 
            raise TypeError('Install Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmInstallationDate.isspace(): 
            raise ValueError('Install Date cannot be empty')       
        # Convert the date to string
        dtmInstallationDate = datetime.strptime(dtmInstallationDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmInstallationDate, date): 
            raise TypeError('Install Date must be a valid date') 
        # Convert the date back to string
        dtmInstallationDate = str(dtmInstallationDate)

        self._dtmInstallationDate = dtmInstallationDate   
        
    # setter method 
    @dtmLastInspectionDate.setter 
    def dtmLastInspectionDate(self, dtmLastInspectionDate): 
        # Return true if specified object is of str type
        if not isinstance(dtmLastInspectionDate, str): 
            raise TypeError('Last Inspection Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmLastInspectionDate.isspace(): 
            raise ValueError('Last Inspection Date cannot be empty')       
        # Convert the date to string
        dtmLastInspectionDate = datetime.strptime(dtmLastInspectionDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmLastInspectionDate, date): 
            raise TypeError('Last Inspection Date must be a valid date') 
        # Convert the date back to string
        dtmLastInspectionDate = str(dtmLastInspectionDate)

        self._dtmLastInspectionDate = dtmLastInspectionDate   

    # setter method 
    @dtmNextInspectionDate.setter 
    def dtmNextInspectionDate(self, dtmNextInspectionDate): 
        # Return true if specified object is of str type
        if not isinstance(dtmNextInspectionDate, str): 
            raise TypeError('Next Inspection Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmNextInspectionDate.isspace(): 
            raise ValueError('Next Inspection Date cannot be empty')       
        # Convert the date to string
        dtmNextInspectionDate = datetime.strptime(dtmNextInspectionDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmNextInspectionDate, date): 
            raise TypeError('Next Inspection Date must be a valid date') 
        # Convert the date back to string
        dtmNextInspectionDate = str(dtmNextInspectionDate)

        self._dtmNextInspectionDate = dtmNextInspectionDate   
                
    # setter method 
    @strEquipInUse.setter 
    def strEquipInUse(self, strEquipInUse): 
        # Return true if specified object is of str type
        if not isinstance(strEquipInUse, str): 
            raise TypeError('In Use Status must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if strEquipInUse.isspace(): 
            raise ValueError('In Use Status cannot be empty') 
        # Set the attribute to the value if true
        elif strEquipInUse.isalpha():
            self._strEquipInUse = strEquipInUse   

    def Append_RopeIDList(self, intObject):
        """ 
        Function Name: Append_RopeIDList
        Function Description: This function appends objects to the Rope ID list
        """    
        self.aintRopeIDCache.append(intObject)

    def Remove_RopeIDList(self, intObject):
        """ 
        Function Name: Remove_RopeIDList
        Function Description: This function removes objects in the Rope ID list
        """    
        self.aintRopeIDCache.remove(intObject)

    def Get_RopeIDList_Obj(self):
        """ 
        Function Name: Get_RopeIDList_Obj
        Function Description: This function gets all the objects in the Rope ID list
        """    
        return self.aintRopeIDCache            

    def Append_Rope_SerialNumList(self, strObject):
        """ 
        Function Name: Append_SerialNumList
        Function Description: This function appends objects to the Serial Num list
        """    
        self.astrSerialNumCache.append(strObject)

    def Remove_Rope_SerialNumList(self, strObject):
        """ 
        Function Name: Remove_SerialNumList
        Function Description: This function removes objects in the Serial Num list
        """    
        self.astrSerialNumCache.remove(strObject)

    def Get_Rope_SerialNumList_Obj(self):
        """ 
        Function Name: Get_SerialNumList_Obj
        Function Description: This function gets all the objects in the Serial Num list
        """    
        return self.astrSerialNumCache 

    def Append_Rope_BumperNumList(self, strObject):
        """ 
        Function Name: Append_BumperNumList
        Function Description: This function appends objects to the Bumper Num list
        """    
        self.astrBumperNumCache.append(strObject)

    def Remove_Rope_BumperNumList(self, strObject):
        """ 
        Function Name: Remove_BumperNumList
        Function Description: This function removes objects in the Bumper Num list
        """    
        self.astrBumperNumCache.remove(strObject)

    def Get_Rope_BumperNumList_Obj(self):
        """ 
        Function Name: Get_BumperNumList_Obj
        Function Description: This function gets all the objects in the Bumper Num list
        """    
        return self.astrBumperNumCache 

    def Append_RopeLengthList(self, strObject):
        """ 
        Function Name: Append_RopeLengthList
        Function Description: This function appends objects to the Rope Length list
        """    
        self.astrRopeLengthCache.append(strObject)

    def Remove_RopeLengthDList(self, strObject):
        """ 
        Function Name: Remove_RopeLengthDList
        Function Description: This function removes objects in the Rope Length list
        """    
        self.astrRopeLengthCache.remove(strObject)

    def Get_RopeLengthList_Obj(self):
        """ 
        Function Name: Get_RopeLengthList_Obj
        Function Description: This function gets all the objects in the Rope Length list
        """    
        return self.astrRopeLengthCache 
    
    def Append_Rope_DiameterList(self, strObject):
        """ 
        Function Name: Append_DiameterList
        Function Description: This function appends objects to the Diameter list
        """    
        self.astrDiameterCache.append(strObject)

    def Remove_Rope_DiameterList(self, strObject):
        """ 
        Function Name: Remove_DiameterList
        Function Description: This function removes objects in the Diameter list
        """    
        self.astrDiameterCache.remove(strObject)

    def Get_Rope_DiameterList_Obj(self):
        """ 
        Function Name: Get_DiameterList_Obj
        Function Description: This function gets all the objects in the Diameter list
        """    
        return self.astrDiameterCache

    def Append_Rope_ElasticityList(self, strObject):
        """ 
        Function Name: Append_Rope_ElasticityList
        Function Description: This function appends objects to the Elasticity list
        """    
        self.astrElasticityCache.append(strObject)

    def Remove_Rope_ElasticityList(self, strObject):
        """ 
        Function Name: Remove_Rope_ElasticityList
        Function Description: This function removes objects in the Elasticity list
        """    
        self.astrElasticityCache.remove(strObject)

    def Get_Rope_ElasticityList_Obj(self):
        """ 
        Function Name: Get_Rope_ElasticityList_Obj
        Function Description: This function gets all the objects in the Elasticity list
        """    
        return self.astrElasticityCache

    def Append_Rope_ManuNameList(self, strObject):
        """ 
        Function Name: Append_Rope_ManuNameList
        Function Description: This function appends objects to the ManuFacture Name list
        """    
        self.astrManufactureNameCache.append(strObject)

    def Remove_Rope_ManuNameList(self, strObject):
        """ 
        Function Name: Remove_Rope_ManuNameList
        Function Description: This function removes objects in the ManuFacture Name list
        """    
        self.astrManufactureNameCache.remove(strObject)

    def Get_Rope_ManuNameList_Obj(self):
        """ 
        Function Name: Get_Rope_ManuNameList_Obj
        Function Description: This function gets all the objects in the ManuFacture Name list
        """    
        return self.astrManufactureNameCache

    def Append_Rope_ManuDateList(self, strObject):
        """ 
        Function Name: Append_Rope_ManuDateList
        Function Description: This function appends objects to the ManuFacture Date list
        """    
        self.adtmManufactureDateCache.append(strObject)

    def Remove_Rope_ManuDateList(self, strObject):
        """ 
        Function Name: Remove_Rope_ManuDateList
        Function Description: This function removes objects in the ManuFacture Date list
        """    
        self.adtmManufactureDateCache.remove(strObject)

    def Get_Rope_ManuDateList_Obj(self):
        """ 
        Function Name: Get_Rope_ManuDateList_Obj
        Function Description: This function gets all the objects in the ManuFacture Date list
        """    
        return self.adtmManufactureDateCache

    def Append_Rope_InstallDateList(self, strObject):
        """ 
        Function Name: Append_Rope_InstallDateList
        Function Description: This function appends objects to the Install Date list
        """    
        self.adtmInstallationDateCache.append(strObject)

    def Remove_Rope_InstallDateList(self, strObject):
        """ 
        Function Name: Remove_Rope_InstallDateList
        Function Description: This function removes objects in the Install Date list
        """    
        self.adtmInstallationDateCache.remove(strObject)

    def Get_Rope_InstallDateList_Obj(self):
        """ 
        Function Name: Get_Rope_InstallDateList_Obj
        Function Description: This function gets all the objects in the Install Date list
        """    
        return self.adtmInstallationDateCache

    def Append_Rope_LastInspectDateList(self, strObject):
        """ 
        Function Name: Append_Rope_LastInspectDateList
        Function Description: This function appends objects to the Last Inspect Date list
        """    
        self.adtmLastInspectionDateCache.append(strObject)

    def Remove_Rope_LastInspectDateList(self, strObject):
        """ 
        Function Name: Remove_Rope_LastInspectDateList
        Function Description: This function removes objects in the Last Inspect Date list
        """    
        self.adtmLastInspectionDateCache.remove(strObject)

    def Get_Rope_LastInspectDateList_Obj(self):
        """ 
        Function Name: Get_Rope_LastInspectDateList_Obj
        Function Description: This function gets all the objects in the Last Inspect Date list
        """    
        return self.adtmLastInspectionDateCache

    def Append_Rope_NextInspectDateList(self, strObject):
        """ 
        Function Name: Append_Rope_NextInspectDateList
        Function Description: This function appends objects to the Next Inspect Date list
        """    
        self.adtmNextInspectionDateCache.append(strObject)

    def Remove_Rope_NextInspectDateList(self, strObject):
        """ 
        Function Name: Remove_Rope_NextInspectDateList
        Function Description: This function removes objects in the Next Inspect Date list
        """    
        self.adtmNextInspectionDateCache.remove(strObject)

    def Get_Rope_NextInspectDateList_Obj(self):
        """ 
        Function Name: Get_Rope_NextInspectDateList_Obj
        Function Description: This function gets all the objects in the Next Inspect Date list
        """    
        return self.adtmNextInspectionDateCache

    def Append_Rope_EquipInUseList(self, strObject):
        """ 
        Function Name: Append_Rope_EquipInUseList
        Function Description: This function appends objects to the Equipment In Use list
        """    
        self.astrEquipInUseCache.append(strObject)

    def Remove_Rope_EquipInUseList(self, strObject):
        """ 
        Function Name: Remove_Rope_EquipInUseList
        Function Description: This function removes objects in the Equipment In Use list
        """    
        self.astrEquipInUseCache.remove(strObject)

    def Get_Rope_EquipInUseList_Obj(self):
        """ 
        Function Name: Get_Rope_EquipInUseList_Obj
        Function Description: This function gets all the objects in the Equipment In Use list
        """    
        return self.astrEquipInUseCache
                        
    def Get_Ropes_Data(self):
        """ 
        Function Name: Get_Ropes_Data
        Function Description: This function gets all the objects in the Ropes table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TRopes"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # First check if the contents are found and if yes, proceed to get the contents of the table
        if QueryResultList is not None:
            # Append the Auto Belay Data List
            for i in range(len(QueryResultList)):
                Ropes.Append_RopeIDList(self, QueryResultList[i][0])
                Ropes.Append_Rope_SerialNumList(self, QueryResultList[i][1]) 
                Ropes.Append_Rope_BumperNumList(self, QueryResultList[i][2]) 
                Ropes.Append_RopeLengthList(self, QueryResultList[i][3]) 
                Ropes.Append_Rope_DiameterList(self, QueryResultList[i][4])
                Ropes.Append_Rope_ElasticityList(self, QueryResultList[i][5]) 
                Ropes.Append_Rope_ManuNameList(self, QueryResultList[i][6]) 
                Ropes.Append_Rope_ManuDateList(self, QueryResultList[i][7]) 
                Ropes.Append_Rope_InstallDateList(self, QueryResultList[i][8]) 
                Ropes.Append_Rope_LastInspectDateList(self, QueryResultList[i][9]) 
                Ropes.Append_Rope_NextInspectDateList(self, QueryResultList[i][10]) 
                Ropes.Append_Rope_EquipInUseList(self, QueryResultList[i][11]) 

    def Set_Ropes_Selection(self):
        """ 
        Function Name: Set_Ropes_Selection
        Function Description: This function will set the selection name from the user and will update the 
        class objects with the data from the database.
        """    
        # First get the selection from the user 
        for i, item in enumerate(self.astrSerialNumCache):
            if self.strSerialNum == item:
                # Assign the iterable num to the ID num and assign the objects to the desired data sets    
                self.intRopeID = self.aintRopeIDCache[i]
                if not self.strSerialNum:
                    self.strSerialNum = self.astrSerialNumCache[i]
                self.strBumperNum = self.astrBumperNumCache[i]
                self.strRopeLength = self.astrRopeLengthCache[i]
                self.strDiameter = self.astrDiameterCache[i]
                self.strElasticity = self.astrElasticityCache[i]
                self.strManufactureName = self.astrManufactureNameCache[i]
                self.dtmManufactureDate = self.adtmManufactureDateCache[i]
                self.dtmInstallationDate = self.adtmInstallationDateCache[i]
                self.dtmLastInspectionDate = self.adtmLastInspectionDateCache[i]
                self.dtmNextInspectionDate = self.adtmNextInspectionDateCache[i]
                if not self.strEquipInUse:
                    self.strEquipInUse = self.astrEquipInUseCache[i]                        
                
                break

    def Set_Ropes_Data(self):
        """ 
        Function Name: Set_Ropes_Data
        Function Description: This function will set the class objects for the device when selected
        """    
        # First get the selection from the user 
        for i, item in enumerate(self.astrSerialNumCache):
            if self.strSerialNum == item:
                # Assign the iterable num to the ID num and assign the objects to the desired data sets    
                self.intRopeID = self.aintRopeIDCache[i]                  
                self.strSerialNum = self.astrSerialNumCache[i]
                self.strBumperNum = self.astrBumperNumCache[i]
                self.strRopeLength = self.astrRopeLengthCache[i]
                self.strDiameter = self.astrDiameterCache[i]
                self.strElasticity = self.astrElasticityCache[i]
                self.strManufactureName = self.astrManufactureNameCache[i]
                self.dtmManufactureDate = self.adtmManufactureDateCache[i]
                self.dtmInstallationDate = self.adtmInstallationDateCache[i]
                self.dtmLastInspectionDate = self.adtmLastInspectionDateCache[i]
                self.dtmNextInspectionDate = self.adtmNextInspectionDateCache[i]
                self.strEquipInUse = self.astrEquipInUseCache[i]
                # Set the global class bool to true
                Bool_Flag.Set_Rope_Bool_Value_True(Bool_Flag)    
                
                break

    def Add_Ropes_Query(self):
        """ 
        Function Name: Add_Ropes_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Create the sql query string
        sqlTableCol = ("intRopeID", "strSerialNum", "strBumperNum", "strRopeLength", "strDiameter",
                        "strElasticity", "strManufactureName", "dtmManufactureDate", "dtmInstallationDate", 
                        "dtmLastInspectionDate", "dtmNextInspectionDate", "strEquipInUse")   
        sqlTableName = "TRopes"  

        # Set the Table values and the params tuple
        sqlTableValues = (self.intRopeID, self.strSerialNum, self.strBumperNum, self.strRopeLength, 
                        self.strDiameter, self.strElasticity, self.strManufactureName, self.dtmManufactureDate, 
                        self.dtmInstallationDate, self.dtmLastInspectionDate, self.dtmNextInspectionDate, self.strEquipInUse)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

        # Reload the data after user submits entry
        Ropes.Delete_Ropes_Data(Ropes)
        Ropes.Get_Ropes_Data(Ropes)

    def Update_Ropes_Inspect_Dates(self):
        """ 
        Function Name: Update_Ropes_Inspect_Dates
        Function Description: This function updated the database with inspection dates last and next
        """    
        # Create the sql query string
        sqlTableCol = ("intRopeID", "dtmLastInspectionDate", "dtmNextInspectionDate")   
        sqlTableName = "TRopes"  

        # Set the last and next inspection date based off of the current date
        aDateResult = BaseFunctions.Update_Inspection_Date()
        self.dtmLastInspectionDate = datetime.strftime(aDateResult[0], '%Y-%m-%d')
        self.dtmNextInspectionDate = datetime.strftime(aDateResult[1], '%Y-%m-%d')
        
        # Set the Table values and the params tuple
        sqlTableValues = (self.intRopeID, self.dtmLastInspectionDate, self.dtmNextInspectionDate)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], sqlTableValues[0])         

        # Execute the stored procedure
        Queries.dbExeUSP_UpdateValues(Queries, sqlParams)

    def Update_Ropes_InUse_Status(self):
        """ 
        Function Name: Update_Ropes_InUse_Status
        Function Description: This function updated the database with in use status of the rope
        """ 
        # Declare Local Variables
        intFailStatus = int(3)
        
        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(RopeInspect.aRopeInspectStatus)
            
        if intOverallStatus == intFailStatus:
            # Check if the user knows about the Rope being failed. If the user removed from wall, the Rope is not longer in use
            messagebox.showwarning(message='ATTENTION! \n\nWe have identified an overall status --> FAIL <-- for this Rope. \n\nPlease remove the retired rope from future use.')
            self.strEquipInUse = "Retired"
            Bool_Flag.Set_RopeRetired_Bool_Value_True(Bool_Flag)
            
        # Create the sql query string
        sqlTableCol = ("intRopeID", "strEquipInUse")   
        sqlTableName = "TRopes"  

        # Set the Table values and the params tuple
        sqlTableValues = (self.intRopeID, self.strEquipInUse)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], sqlTableValues[0])         

        # Execute the stored procedure
        Queries.dbExeUSP_UpdateValues(Queries, sqlParams)
                
    def Update_NewRopes_Query(self):
        """ 
        Function Name: Update_NewRopes_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Create the sql query string
        sqlTableCol = ("intRopeID", "strSerialNum", "strBumperNum", "strRopeLength", "strDiameter",
                        "strElasticity", "strManufactureName", "dtmManufactureDate", "dtmInstallationDate", 
                        "dtmLastInspectionDate", "dtmNextInspectionDate", "strEquipInUse")   
        sqlTableName = "TRopes"  

        # Set the Table values and the params tuple
        sqlTableValues = (self.intRopeID, self.strSerialNum, self.strBumperNum, self.strRopeLength, 
                            self.strDiameter, self.strElasticity, self.strManufactureName, self.dtmManufactureDate, 
                            self.dtmInstallationDate, self.dtmLastInspectionDate, self.dtmNextInspectionDate, self.strEquipInUse)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], sqlTableValues[0])       

        # Execute the stored procedure
        Queries.dbExeUSP_UpdateValues(Queries, sqlParams)

        # Reload the data after user submits entry
        Ropes.Delete_Ropes_Data(Ropes)
        Ropes.Get_Ropes_Data(Ropes)
        
    def Set_Global_Ropes_Attributes(self):
        """ 
        Function Name: Set_Global_Ropes_Attributes
        Function Description: This function sets Ropes attributes once the user proceeds with adding a new
        ropes to the database.
        """    
        Ropes.strSerialNum = self.strSerialNum
        Ropes.strBumperNum = self.strBumperNum
        Ropes.strRopeLength = self.strRopeLength
        Ropes.strDiameter = self.strDiameter
        Ropes.strElasticity = self.strElasticity
        Ropes.strDeviceName = self.strDeviceName
        Ropes.strManufactureName = self.strManufactureName
        Ropes.dtmManufactureDate = self.dtmManufactureDate
        Ropes.dtmInstallationDate = self.dtmInstallationDate
        Ropes.dtmLastInspectionDate = self.dtmLastInspectionDate
        Ropes.dtmNextInspectionDate = self.dtmNextInspectionDate
        Ropes.strEquipInUse = self.strEquipInUse

    def Delete_Ropes_Data(self):
        """ 
        Function Name: Delete_Ropes_Data
        Function Description: This function removes all the objects in the Ropes class
        """    
        Ropes.aintRopeIDCache = []
        Ropes.aintRopeLengthCache = []   
        Ropes.astrSerialNumCache = []
        Ropes.astrBumperNumCache = []
        Ropes.astrDiameterCache = []
        Ropes.astrRopeLengthCache = []
        Ropes.astrElasticityCache = []
        Ropes.astrManufactureNameCache = []
        Ropes.adtmManufactureDateCache = []
        Ropes.adtmInstallationDateCache = []
        Ropes.adtmLastInspectionDateCache = []
        Ropes.adtmNextInspectionDateCache = []
        Ropes.astrEquipInUseCache = []                                                                        
                        

class RopeVisSelection():
    """
    Class Name: RopeVisSelection
    Class Description: This class gets and sets all of the Rope Visual Selections. 
    """
    # Create class variable shared amongst all Rope visual methods
    aintRopeVisTextSelectID = []
    astrRopeVisTextSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intRopeVisTextSelectID, strRopeVisTextSelect, strRopeVisStatus):
        self.intRopeVisTextSelectID = intRopeVisTextSelectID
        self.strRopeVisTextSelect = strRopeVisTextSelect
        self.strRopeVisStatus = strRopeVisStatus

    # Property decorator object get function to access private intRopeVisTextSelectID
    @property
    def intRopeVisTextSelectID(self):
        return self._intRopeVisTextSelectID

    # Property decorator object get function to access private strRopeVisTextSelect
    @property
    def strRopeVisTextSelect(self):
        return self._strRopeVisTextSelect

    # Property decorator object get function to access private strRopeVisStatus
    @property
    def strRopeVisStatus(self):
        return self._strRopeVisStatus
            
    # setter method 
    @intRopeVisTextSelectID.setter 
    def intRopeVisTextSelectID(self, intRopeVisTextSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intRopeVisTextSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intRopeVisTextSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intRopeVisTextSelectID = intRopeVisTextSelectID 
        
    # setter method 
    @strRopeVisTextSelect.setter 
    def strRopeVisTextSelect(self, strRopeVisTextSelect): 
        # Return true if specified object is of str type
        if not isinstance(strRopeVisTextSelect, str): 
            raise TypeError('Rope visual input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strRopeVisTextSelect.isspace(): 
            raise ValueError('Rope visual input cannot be empty') 
        # Set the attribute to the value if true
        elif strRopeVisTextSelect.isascii():
            self._strRopeVisTextSelect = strRopeVisTextSelect

    # setter method 
    @strRopeVisStatus.setter 
    def strRopeVisStatus(self, strRopeVisStatus): 
        # Return true if specified object is of str type
        if not isinstance(strRopeVisStatus, str): 
            raise TypeError('Rope visual status input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strRopeVisStatus.isspace(): 
            raise ValueError('Rope visual status input cannot be empty') 
        # Set the attribute to the value if true
        elif strRopeVisStatus.isascii():
            self._strRopeVisStatus = strRopeVisStatus

    def Append_RopeVisIDList(self, intObject):
        """ 
        Function Name: Append_RopeVisIDList
        Function Description: This function appends objects to the Rope Visual Selection ID list
        """    
        self.aintRopeVisTextSelectID.append(intObject)

    def Remove_RopeVisIDList(self, intObject):
        """ 
        Function Name: Remove_RopeVisIDList
        Function Description: This function removes objects in the Rope Visual Selection ID list
        """    
        self.aintRopeVisTextSelectID.remove(intObject)

    def Get_RopeVisIDList_Obj(self):
        """ 
        Function Name: Get_RopeVisIDList_Obj
        Function Description: This function gets all the objects in the Rope Visual Selection ID list
        """    
        return self.aintRopeVisTextSelectID
    
    def Append_RopeVisSelectList(self, strObject):
        """ 
        Function Name: Append_RopeVisSelectList
        Function Description: This function appends objects to the Rope Visual Selection list
        """    
        self.astrRopeVisTextSelect.append(strObject)

    def Remove_RopeVisSelectList(self, strObject):
        """ 
        Function Name: Remove_RopeVisSelectList
        Function Description: This function removes objects in the Rope Visual Selection list
        """    
        self.astrRopeVisTextSelect.remove(strObject)

    def Get_RopeVisSelectList_Obj(self):
        """ 
        Function Name: Get_RopeVisSelectList_Obj
        Function Description: This function gets all the objects in the Rope Visual Selection list
        """    
        return self.astrRopeVisTextSelect   
                    
    def Delete_RopeVisSelectList_Data(self):
        """ 
        Function Name: Delete_RopeVisSelectList_Data
        Function Description: This function removes all the objects in the Rope Visual Selection class
        """    
        RopeVisSelection.aintRopeVisTextSelectID = []
        RopeVisSelection.astrRopeVisTextSelect = []

    def Check_RopeVisSelection_Dup(self):
        """ 
        Function Name: Check_RopeVisSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        Rope visual selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intRopeVisTextSelectID", "strRopeVisTextSelect")   
        sqlTableName = "TRopeVisTextSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strRopeVisTextSelect in sqlDupValues[i]:
                self.intRopeVisTextSelectID = sqlDupValues[i][0]
                self.strRopeVisTextSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag
            
    def Add_RopeVisSelectList_Query(self):
        """ 
        Function Name: Add_RopeVisSelectList_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewRopeVisSelection
        """    
        # Create the sql query params
        sqlTableCol = ("intRopeVisTextSelectID", "strRopeVisTextSelect")   
        sqlTableName = "TRopeVisTextSelects"
        sqlTableValues = (RopeVisSelection.intRopeVisTextSelectID, RopeVisSelection.strRopeVisTextSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams) 

    def Clear_RopeVisSel_Attributes(self):
        """ 
        Function Name: Clear_RopeVisSel_Attributes
        Function Description: This function clears the Rope Visual Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intRopeVisTextSelectID", "strRopeVisTextSelect")   
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                
                
class RopeVisualInspect(Ropes, InspectionType, RopeVisSelection, InspectionStatus):
    """
    Class Name: RopeVisualInspect
    Class Description: This class gets and sets all of the Rope Visual Inspection attributes. 
    """
    # Create class variable shared amongst all Rope Visual Inspection methods
    aintRopeVisualInspectionID = []
    aRopeVisualCache = []
        
    # Instantiate the following attributes
    def __init__(self, intRopeVisualInspectionID, intRopeID, intInspectionTypeID, intRopeVisTextSelectID, intInspectionStatusID):
        self.intRopeVisualInspectionID = intRopeVisualInspectionID
        # Inherits the child class with all the necessary objects
        Ropes.__init__(intRopeID)
        InspectionType.__init__(intInspectionTypeID)
        RopeVisSelection.__init__(intRopeVisTextSelectID)
        InspectionStatus.__init__(intInspectionStatusID)

    # Property decorator object get function to access private intRopeVisualInspectionID
    @property
    def intRopeVisualInspectionID(self):
        return self._intRopeVisualInspectionID

    # setter method 
    @intRopeVisualInspectionID.setter 
    def intRopeVisualInspectionID(self, intRopeVisualInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intRopeVisualInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Rope Visual Inspection ID to value
        if intRopeVisualInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intRopeVisualInspectionID = intRopeVisualInspectionID 

    def Append_RopeVisualIDList(self, intObject):
        """ 
        Function Name: Append_RopeVisualIDList
        Function Description: This function appends objects to the Rope Visual Inspection ID list
        """    
        self.aintRopeVisualInspectionID.append(intObject)

    def Remove_RopeVisualIDList(self, intObject):
        """ 
        Function Name: Remove_RopeVisualIDList
        Function Description: This function removes objects in the Rope Visual Inspection ID list
        """    
        self.aintRopeVisualInspectionID.remove(intObject)

    def Get_RopeVisualIDList_Obj(self):
        """ 
        Function Name: Get_RopeVisualIDList_Obj
        Function Description: This function gets all the objects in the Rope Visual Inspection ID list
        """    
        return self.aintRopeVisualInspectionID
                
    def Delete_RopeVisualInspect_Data(self):
        """ 
        Function Name: Delete_RopeVisualInspect_Data
        Function Description: This function removes all the objects in the Rope Visual Inspection ID class
        """    
        RopeVisualInspect.aintRopeVisualInspectionID = []
        RopeVisualInspect.aRopeVisualCache = []

    def Set_RopeVisualInspect_Data(self):
        """ 
        Function Name: Set_RopeVisualInspect_Data
        Function Description: This function sets all the objects in the Rope Visual Inspection class
        """    
        self.intRopeVisualInspectionID = RopeVisualInspect.aRopeVisualCache[0]
        self.intRopeID = RopeVisualInspect.aRopeVisualCache[1]
        self.intInspectionTypeID = RopeVisualInspect.aRopeVisualCache[2]
        self.intRopeVisTextSelectID = RopeVisualInspect.aRopeVisualCache[3]
        self.intInspectionStatusID = RopeVisualInspect.aRopeVisualCache[4]
                
    def Add_RopeVisualInspect_Query(self):
        """ 
        Function Name: Add_RopeVisualInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewRopeVisualInspection
        """    
        # Set the class variables before dumping the data to the database
        RopeVisualInspect.Set_RopeVisualInspect_Data(self)
        
        # Create the sql query string       
        sqlTableCol = ("intRopeVisualInspectionID", "intRopeID", "intInspectionTypeID", "intRopeVisTextSelectID", "intInspectionStatusID")     
        sqlTableName = "TRopeVisualInspections"
        sqlTableValues = (self.intRopeVisualInspectionID, self.intRopeID, self.intInspectionTypeID, self.intRopeVisTextSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Clear_RopeVisInspect_Attributes(self):
        """ 
        Function Name: Clear_RopeVisInspect_Attributes
        Function Description: This function clears the Rope Visual Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intRopeVisualInspectionID", "intRopeID", "intInspectionTypeID", "intRopeVisTextSelectID", "intInspectionStatusID")     
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            

class RopePhysSelection():
    """
    Class Name: RopePhysSelection
    Class Description: This class gets and sets all of the Rope Physical Selections. 
    """
    # Create class variable shared amongst all Rope Physical methods
    aintRopePhysTextSelectID = []
    astrRopePhysTextSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intRopePhysTextSelectID, strRopePhysTextSelect, strRopePhysStatus):
        self.intRopePhysTextSelectID = intRopePhysTextSelectID
        self.strRopePhysTextSelect = strRopePhysTextSelect
        self.strRopePhysStatus = strRopePhysStatus

    # Property decorator object get function to access private intRopePhysTextSelectID
    @property
    def intRopePhysTextSelectID(self):
        return self._intRopePhysTextSelectID

    # Property decorator object get function to access private strRopePhysTextSelect
    @property
    def strRopePhysTextSelect(self):
        return self._strRopePhysTextSelect
        
    # Property decorator object get function to access private strRopePhysStatus
    @property
    def strRopePhysStatus(self):
        return self._strRopePhysStatus
                
    # setter method 
    @intRopePhysTextSelectID.setter 
    def intRopePhysTextSelectID(self, intRopePhysTextSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intRopePhysTextSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intRopePhysTextSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intRopePhysTextSelectID = intRopePhysTextSelectID 
        
    # setter method 
    @strRopePhysTextSelect.setter 
    def strRopePhysTextSelect(self, strRopePhysTextSelect): 
        # Return true if specified object is of str type
        if not isinstance(strRopePhysTextSelect, str): 
            raise TypeError('Rope physical input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strRopePhysTextSelect.isspace(): 
            raise ValueError('Rope physical input cannot be empty') 
        # Set the attribute to the value if true
        elif strRopePhysTextSelect.isascii():
            self._strRopePhysTextSelect = strRopePhysTextSelect

    # setter method 
    @strRopePhysStatus.setter 
    def strRopePhysStatus(self, strRopePhysStatus): 
        # Return true if specified object is of str type
        if not isinstance(strRopePhysStatus, str): 
            raise TypeError('Rope physical status must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strRopePhysStatus.isspace(): 
            raise ValueError('Rope physical status cannot be empty') 
        # Set the attribute to the value if true
        elif strRopePhysStatus.isascii():
            self._strRopePhysStatus = strRopePhysStatus

    def Append_RopePhysIDList(self, intObject):
        """ 
        Function Name: Append_RopePhysIDList
        Function Description: This function appends objects to the Rope Physical Selection ID list
        """    
        self.aintRopePhysTextSelectID.append(intObject)

    def Remove_RopePhysIDList(self, intObject):
        """ 
        Function Name: Remove_RopePhysIDList
        Function Description: This function removes objects in the Rope Physical Selection ID list
        """    
        self.aintRopePhysTextSelectID.remove(intObject)

    def Get_RopePhysIDList_Obj(self):
        """ 
        Function Name: Get_RopePhysIDList_Obj
        Function Description: This function gets all the objects in the Rope Visual Selection ID list
        """    
        return self.aintRopePhysTextSelectID
    
    def Append_RopePhysSelectList(self, strObject):
        """ 
        Function Name: Append_RopePhysSelectList
        Function Description: This function appends objects to the Rope Visual Selection list
        """    
        self.astrRopePhysTextSelect.append(strObject)

    def Remove_RopePhysSelectList(self, strObject):
        """ 
        Function Name: Remove_RopePhysSelectList
        Function Description: This function removes objects in the Rope Visual Selection list
        """    
        self.astrRopePhysTextSelect.remove(strObject)

    def Get_RopePhysSelectList_Obj(self):
        """ 
        Function Name: Get_RopePhysSelectList_Obj
        Function Description: This function gets all the objects in the Rope Visual Selection list
        """    
        return self.astrRopePhysTextSelect   
                    
    def Delete_RopePhysSelectList_Data(self):
        """ 
        Function Name: Delete_RopePhysSelectList_Data
        Function Description: This function removes all the objects in the Rope Visual Selection class
        """    
        RopePhysSelection.aintRopePhysTextSelectID = []
        RopePhysSelection.astrRopePhysTextSelect = []

    def Check_RopePhysSelection_Dup(self):
        """ 
        Function Name: Check_RopePhysSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        Rope physical selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intRopePhysTextSelectID", "strRopePhysTextSelect")   
        sqlTableName = "TRopePhysTextSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strRopePhysTextSelect in sqlDupValues[i]:
                self.intRopePhysTextSelectID = sqlDupValues[i][0]
                self.strRopePhysTextSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag
            
    def Add_RopePhysSelectList_Query(self):
        """ 
        Function Name: Add_RopePhysSelectList_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewRopePhysSelection
        """    
        # Create the sql query params
        sqlTableCol = ("intRopePhysTextSelectID", "strRopePhysTextSelect")   
        sqlTableName = "TRopePhysTextSelects"
        sqlTableValues = (RopePhysSelection.intRopePhysTextSelectID, RopePhysSelection.strRopePhysTextSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams) 
        
    def Clear_RopePhysSel_Attributes(self):
        """ 
        Function Name: Clear_RopePhysSel_Attributes
        Function Description: This function clears the Rope Physical Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intRopePhysTextSelectID", "strRopePhysTextSelect")   
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            
            
class RopePhysicalInspect(Ropes, InspectionType, RopePhysSelection, InspectionStatus):
    """
    Class Name: RopePhysicalInspect
    Class Description: This class gets and sets all of the Rope Physical Inspection attributes. 
    """
    # Create class variable shared amongst all Rope Physical Inspection methods
    aintRopePhysicalInspectionID = []
    aRopePhysicalCache = []
        
    # Instantiate the following attributes
    def __init__(self, intRopePhysicalInspectionID, intRopeID, intInspectionTypeID, intRopePhysTextSelectID, intInspectionStatusID):
        self.intRopePhysicalInspectionID = intRopePhysicalInspectionID
        # Inherits the child class with all the necessary objects
        Ropes.__init__(intRopeID)
        InspectionType.__init__(intInspectionTypeID)
        RopePhysSelection.__init__(intRopePhysTextSelectID)
        InspectionStatus.__init__(intInspectionStatusID)

    # Property decorator object get function to access private intRopePhysicalInspectionID
    @property
    def intRopePhysicalInspectionID(self):
        return self._intRopePhysicalInspectionID

    # setter method 
    @intRopePhysicalInspectionID.setter 
    def intRopePhysicalInspectionID(self, intRopePhysicalInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intRopePhysicalInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Rope Physical Inspection ID to value
        if intRopePhysicalInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intRopePhysicalInspectionID = intRopePhysicalInspectionID 

    def Append_RopePhysicalIDList(self, intObject):
        """ 
        Function Name: Append_RopePhysicalIDList
        Function Description: This function appends objects to the Rope Physical Inspection ID list
        """    
        self.aintRopePhysicalInspectionID.append(intObject)

    def Remove_RopePhysicalIDList(self, intObject):
        """ 
        Function Name: Remove_RopePhysicalIDList
        Function Description: This function removes objects in the Rope Physical Inspection ID list
        """    
        self.aintRopePhysicalInspectionID.remove(intObject)

    def Get_RopePhysicalIDList_Obj(self):
        """ 
        Function Name: Get_RopePhysicalIDList_Obj
        Function Description: This function gets all the objects in the Rope Physical Inspection ID list
        """    
        return self.aintRopePhysicalInspectionID
                
    def Delete_RopePhysicalInspect_Data(self):
        """ 
        Function Name: Delete_RopePhysicalInspect_Data
        Function Description: This function removes all the objects in the Rope Physical Inspection ID class
        """    
        RopePhysicalInspect.aintRopePhysicalInspectionID = []
        RopePhysicalInspect.aRopePhysicalCache = []

    def Set_RopePhysicalInspect_Data(self):
        """ 
        Function Name: Set_RopePhysicalInspect_Data
        Function Description: This function sets all the objects in the Rope Physical Inspection class
        """    
        self.intRopePhysicalInspectionID = RopePhysicalInspect.aRopePhysicalCache[0]
        self.intRopeID = RopePhysicalInspect.aRopePhysicalCache[1]
        self.intInspectionTypeID = RopePhysicalInspect.aRopePhysicalCache[2]
        self.intRopePhysTextSelectID = RopePhysicalInspect.aRopePhysicalCache[3]
        self.intInspectionStatusID = RopePhysicalInspect.aRopePhysicalCache[4]

    def Add_RopePhysicalInspect_Query(self):
        """ 
        Function Name: Add_RopePhysicalInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewRopeVisualInspection
        """    
        # Set the class variables before dumping the data to the database
        RopePhysicalInspect.Set_RopePhysicalInspect_Data(self)
        
        # Create the sql query string       
        sqlTableCol = ("intRopePhysicalInspectionID", "intRopeID", "intInspectionTypeID", "intRopePhysTextSelectID", "intInspectionStatusID")     
        sqlTableName = "TRopePhysicalInspections"
        sqlTableValues = (self.intRopePhysicalInspectionID, self.intRopeID, self.intInspectionTypeID, self.intRopePhysTextSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Clear_RopePhysInspect_Attributes(self):
        """ 
        Function Name: Clear_RopePhysInspect_Attributes
        Function Description: This function clears the Rope Physical Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intRopePhysicalInspectionID", "intRopeID", "intInspectionTypeID", "intRopePhysTextSelectID", "intInspectionStatusID")     
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                
class StandardRopeInspect(RopeVisualInspect, RopePhysicalInspect):
    """
    Class Name: StandardRopeInspect
    Class Description: This class gets and sets all of the Standard Rope Inspection attributes. 
    Pass in the Rope Visual and Physical classes. 
    """
    # Create class variable shared amongst all Standard Rope Inspection methods
    aintStandardRopeInspectionID = []
    aStandardRopeInsCache = []
        
    # Instantiate the following attributes
    def __init__(self, intStandardRopeInspectionID, intRopeVisualInspectionID, intRopePhysicalInspectionID):
        self.intStandardRopeInspectionID = intStandardRopeInspectionID
        # Inherits the child class with all the necessary objects
        RopeVisualInspect.__init__(intRopeVisualInspectionID)
        RopePhysicalInspect.__init__(intRopePhysicalInspectionID)
        
    # Property decorator object get function to access private intStandardRopeInspectionID
    @property
    def intStandardRopeInspectionID(self):
        return self._intStandardRopeInspectionID
    
    # setter method 
    @intStandardRopeInspectionID.setter 
    def intStandardRopeInspectionID(self, intStandardRopeInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intStandardRopeInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intStandardRopeInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intStandardRopeInspectionID = intStandardRopeInspectionID    

    def Append_StandRopeInspectIDList(self, intObject):
        """ 
        Function Name: Append_StandRopeInspectIDList
        Function Description: This function appends objects to the Standard Rope Inspection ID list
        """    
        self.aintStandardRopeInspectionID.append(intObject)

    def Remove_StandRopeInspectIDList(self, intObject):
        """ 
        Function Name: Remove_StandRopeInspectIDList
        Function Description: This function removes objects in the Standard Rope Inspection ID list
        """    
        self.aintStandardRopeInspectionID.remove(intObject)

    def Get_StandRopeInspectIDList_Obj(self):
        """ 
        Function Name: Get_StandRopeInspectIDList_Obj
        Function Description: This function gets all the objects in the Standard Rope Inspection ID list
        """    
        return self.aintStandardRopeInspectionID     

    def Add_StandRopeInspect_Query(self):
        """ 
        Function Name: Add_StandRopeInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewStandardRopeInspection
        """    
        # Create the sql query string
        sqlTableNames = ("TStandardRopeInspections")
        sqlTableCol = ("intStandardRopeInspectionID", "intRopeVisualInspectionID", "intRopePhysicalInspectionID", 
                    "intInspectionStatusID") 
        # Set the primary key values from the cached array object
        aPrimKeyValues = [item for item in StandardRopeInspect.aStandardRopeInsCache]        

        # Get the visual, physical status IDs
        VisStatusID = InspectionStatus.astrInspectionStatusDesc.index(RopeVisSelection.strRopeVisStatus) + 1
        PhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(RopePhysSelection.strRopePhysStatus) + 1
        aInsStatusID = [VisStatusID, PhysStatusID]

        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(aInsStatusID)

        # Append the Rope Status array 
        RopeInspect.aRopeInspectStatus.append(intOverallStatus)

        # Append the primary key list with the new over status ID
        aPrimKeyValues.append(intOverallStatus)                      
        
        # Set the parameters
        sqlParams = (sqlTableNames, sqlTableCol, tuple(aPrimKeyValues))

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)        

    def Delete_StandRopeInspect_Data(self):
        """ 
        Function Name: Delete_StandCarabInspect_Data
        Function Description: This function removes all the objects in the Standard Carabiner Inspection class
        """    
        StandardRopeInspect.aStandardRopeInsCache = []                
        StandardRopeInspect.aintStandardRopeInspectionID = []

    def Clear_RopeStandardInspect_Attributes(self):
        """ 
        Function Name: Clear_RopeStandardInspect_Attributes
        Function Description: This function clears the Rope Standard Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intStandardRopeInspectionID", "intRopeVisualInspectionID", "intRopePhysicalInspectionID", 
                    "intInspectionStatusID") 
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None) 

    def Reset_Rope_Data(self):
        """ 
        Function Name: Reset_Rope_Data
        Function Description: This function clears the Rope data attributes 
        """  
        # Clear the class attributes
        RopeVisSelection.Clear_RopeVisSel_Attributes(self)
        RopeVisualInspect.Clear_RopeVisInspect_Attributes(self)
        RopePhysSelection.Clear_RopePhysSel_Attributes(self)
        RopePhysicalInspect.Clear_RopePhysInspect_Attributes(self)
        StandardRopeInspect.Clear_RopeStandardInspect_Attributes(self)
                                    
    def Delete_Rope_Data(self):
        """ 
        Function Name: Delete_Rope_Data
        Function Description: This function clears the Rope data arrays 
        """  
        # Clear the class arrays
        RopeVisSelection.Delete_RopeVisSelectList_Data(self)
        RopeVisualInspect.Delete_RopeVisualInspect_Data(self)
        RopePhysSelection.Delete_RopePhysSelectList_Data(self)
        RopePhysicalInspect.Delete_RopePhysicalInspect_Data(self)
        StandardRopeInspect.Delete_StandRopeInspect_Data(self)                


class RopeInspect(WallLocation, StandardRopeInspect, Inspector):
    """
    Class Name: RopeInspect
    Class Description: This class gets and sets all of the Rope Inspection attributes. 
    """
    # Create class variable shared amongst all Rope Inspection methods
    aintRopeInspectionID = []
    aRopeInspectStatus = []
        
    # Instantiate the following attributes
    def __init__(self, intRopeInspectionID, intWallLocationID, intStandardRopeInspectionID, 
                intInspectorID, strComment):
        self.intRopeInspectionID = intRopeInspectionID
        self.strComment = strComment
        # Inherits the child class with all the necessary objects
        WallLocation().__init__(intWallLocationID)
        StandardRopeInspect().__init__(intStandardRopeInspectionID)
        Inspector().__init__(intInspectorID)

    # Property decorator object get function to access private intRopeInspectionID
    @property
    def intRopeInspectionID(self):
        return self._intRopeInspectionID

    # Property decorator object get function to access private strComment
    @property
    def strComment(self):
        return self._strComment
            
    # setter method 
    @intRopeInspectionID.setter 
    def intRopeInspectionID(self, intRopeInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intRopeInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intRopeInspectionID < 0: 
            raise ValueError('ID cannot be negative') 
        self._intRopeInspectionID = intRopeInspectionID    

    # setter method 
    @strComment.setter 
    def strComment(self, strComment): 
        # Return true if specified object is of str type
        if not isinstance(strComment, str): 
            raise TypeError('Comment must be a string') 
        # Set the attribute to the value if true
        elif strComment.isascii():
            self._strComment = strComment   

    def Append_RopeInspectIDList(self, intObject):
        """ 
        Function Name: Append_RopeInspectIDList
        Function Description: This function appends objects to the Rope Inspection ID list
        """    
        self.aintRopeInspectionID.append(intObject)

    def Remove_RopeInspectIDList(self, intObject):
        """ 
        Function Name: Remove_RopeInspectIDList
        Function Description: This function removes objects in the Rope Inspection ID list
        """    
        self.aintRopeInspectionID.remove(intObject)

    def Get_RopeInspectIDList_Obj(self):
        """ 
        Function Name: Get_RopeInspectIDList_Obj
        Function Description: This function gets all the objects in the Rope Inspection ID list
        """    
        return self.aintRopeInspectionID   

    def Join_RopeInspectComm_Obj(self, strObject):
        """ 
        Function Name: Join_RopeInspectComm_Obj
        Function Description: This function joins the string objects in the Rope Inspection comment
        """    
        self.strComment = self.strComment + " " + strObject

    def Get_MaxStandardRopeInspectID(self, table_name, id_column_name):
        """
        Function Name: Get_MaxStandardRopeInspectID
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)

    def Delete_RopeInspect_Data(self):
        """ 
        Function Name: Delete_RopeInspect_Data
        Function Description: This function removes all the objects in the Rope Inspect class
        """    
        RopeInspect.aintRopeInspectionID = []
        RopeInspect.aRopeInspectStatus = []
                            
    def Add_RopeInspection_Query(self):
        """ 
        Function Name: Add_RopeInspection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewRopeInspection
        """
        # Create the sql query string
        sqlTableCol = ("intRopeInspectionID", "intRopeID", "intWallLocationID", "intStandardRopeInspectionID", 
                "intInspectorID", "intInspectionStatusID", "dtmLastInspectionDate", "dtmNextInspectionDate", 
                "strComment")
        sqlTableName = "TRopeInspections"
        
        # Get the max primary key value for the table
        sqlMaxPrimKeyID = RopeInspect.Get_MaxStandardRopeInspectID(self, sqlTableName, sqlTableCol[0])
        self.intRopeInspectionID = sqlMaxPrimKeyID

        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(RopeInspect.aRopeInspectStatus)

        # For testing purposes, set the inspector ID to 1
        Inspector.intInspectorID = 1
                    
        # Set the inspector ID
        # print(UserLogins.aCurrentUserLogin)
        # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID
        
        # Perform the insert query
        sqlTableValues = (self.intRopeInspectionID, Ropes.intRopeID, WallLocation.intWallLocationID, StandardRopeInspect.aStandardRopeInsCache[0], 
                        Inspector.intInspectorID, intOverallStatus, Ropes.dtmLastInspectionDate, Ropes.dtmNextInspectionDate, RopeInspect.strComment)
                        
        # Set the parameters
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)
        
    def Add_RopeInspector_Query(self):
        """ 
        Function Name: Add_RopeInspector_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewRopeInspector
        """    
        # Create the sql query string
        sqlTableCol = ("intRopeInspectorID", "intInspectorID", "intRopeID")
        sqlTableName = "TRopeInspectors"
        
        # Get the max primary key value for the table
        sqlMaxPrimKeyID = RopeInspect.Get_MaxStandardRopeInspectID(self, sqlTableName, sqlTableCol[0])

        # For testing purposes, set the inspector ID to 1
        Inspector.intInspectorID = 1
        
        # Set the inspector ID
        # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID
        
        # Perform the insert query
        sqlTableValues = (sqlMaxPrimKeyID, Inspector.intInspectorID, Ropes.intRopeID)
                
        # Set the parameters
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)          
        
    def Add_RopeLocation_Query(self):
        """ 
        Function Name: Add_RopeLocation_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewRopeWallLocation
        """    
        # Declare Local Variables
        blnFlag = False
        
        # Create the sql query string
        sqlTableAttr = ("TRopeWallLocations", "intRopeWallLocationID", "intWallLocationID", "intRopeID")
        
        try:
            # Get the max primary key value for the table
            idList = (WallLocation.intWallLocationID, Ropes.intRopeID)
            sqlMaxPrimKeyID = RopeInspect.Get_Or_Create_ID(RopeInspect, idList, sqlTableAttr)

            # For testing purposes, set the inspector ID to 1
            Inspector.intInspectorID = 1
            
            # Set the inspector ID
            # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID

            # Get the values
            sqlTableValues = (sqlMaxPrimKeyID, idList[0], idList[1])
                    
            # Set the parameters
            sqlParams = (sqlTableAttr[0], sqlTableAttr[1:], sqlTableValues)
            
            # Get the id list from TRopeWallLocations
            aidReturnList = Queries.Get_All_DB_Values(Queries, sqlTableAttr[0])
            
            # Check if the max ID is in the aidReturnList object
            if aidReturnList:
                for i in aidReturnList:
                    # Extract the IDs from the current entry for clarity
                    current_ids = i[1:3]

                    # Compare current IDs with the item's IDs
                    if idList == current_ids:
                        if Ropes.strEquipInUse == 'Yes':
                            # If device is in use and IDs match, no need to update.
                            blnFlag = True
                        else:
                            # If device is not in use, remove the item.
                            Queries.Remove_Attribute_Query(Queries, sqlTableAttr[0], sqlTableAttr[1], i[0])
                    elif idList[0] == current_ids[0] or idList[1] == current_ids[1]:
                        # If the connector ID matches the current entry's connector ID, remove the entry from the database
                        Queries.Remove_Attribute_Query(Queries, sqlTableAttr[0], sqlTableAttr[1], i[0])
                    
            # Add or update the database if needed
            if not blnFlag and Ropes.strEquipInUse == 'Yes':
                Queries.dbExeUSP_AddValues(Queries, sqlParams)
                    
        except Exception as e:
            print(f"Error in Add_RopeLocation_Query: {e}")

    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = RopeInspect.Check_Duplicate(RopeInspect, item_list, sql_tuple)
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
                    

class RopesRetiredReport(RopeInspect):
    """
    Class Name: RopesRetiredReport
    Class Description: This class gets and sets all of the Rope Retired Report attributes. 
    """
    # Create class variable shared amongst all Rope Retired methods
    aintRopesRetiredReportID = []

    # Instantiate the following attributes
    def __init__(self, intRopesRetiredReportID, intRopeInspectionID, intInspectorID, dtmReportDate):
        self.intRopesRetiredReportID = intRopesRetiredReportID
        self.dtmReportDate = dtmReportDate
        # Inherits the child class with all the necessary objects
        RopeInspect().__init__(intRopeInspectionID)
        Inspector().__init__(intInspectorID)

    # Property decorator object get function to access private intRopesRetiredReportID
    @property
    def intRopesRetiredReportID(self):
        return self._intRopesRetiredReportID

    # Property decorator object get function to access private dtmReportDate
    @property
    def dtmReportDate(self):
        return self._dtmReportDate
            
    # setter method 
    @intRopesRetiredReportID.setter 
    def intRopesRetiredReportID(self, intRopesRetiredReportID): 
        # Return true if specified object is of int type
        if not isinstance(intRopesRetiredReportID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intRopesRetiredReportID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intRopesRetiredReportID = intRopesRetiredReportID    

    # setter method 
    @dtmReportDate.setter 
    def dtmReportDate(self, dtmReportDate):              
        # Return true if specified object is of str type
        if not isinstance(dtmReportDate, str): 
            raise TypeError('Report Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmReportDate.isspace(): 
            raise ValueError('Report Date cannot be empty')       
        # Convert the date to string
        dtmReportDate = datetime.strptime(dtmReportDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmReportDate, date): 
            raise TypeError('Report Date must be a valid date') 
        # Convert the date back to string
        dtmReportDate = str(dtmReportDate)

        self._dtmReportDate = dtmReportDate  

    def Append_Rope_RetiredReportID_List(self, intObject):
        """ 
        Function Name: Append_Rope_RetiredReportID_List
        Function Description: This function appends objects to the Rope Retired Report ID list
        """    
        self.aintRopesRetiredReportID.append(intObject)

    def Remove_Rope_RetiredReportID_List(self, intObject):
        """ 
        Function Name: Remove_Rope_RetiredReportID_List
        Function Description: This function removes objects in the Rope Retired Report ID list
        """    
        self.aintRopesRetiredReportID.remove(intObject)

    def Get_Rope_RetiredReportID_List_Obj(self):
        """ 
        Function Name: Get_Rope_RetiredReportID_List_Obj
        Function Description: This function gets all the objects in the Rope Retired Report ID list
        """    
        return self.aintRopesRetiredReportID   

    def Delete_Rope_RetiredReport_Data(self):
        """ 
        Function Name: Delete_Rope_RetiredReport_Data
        Function Description: This function removes all the objects in the Rope Retired Report class
        """    
        RopesRetiredReport.aintRopesRetiredReportID = []

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
                                
    def Add_Rope_RetiredReport_Query(self):
        """ 
        Function Name: Add_Rope_RetiredReport_Query
        Function Description: This function updated the database with all of the necessary objects
        """
        # Get todays date
        dtmToday = datetime.now().date()
        self.dtmReportDate = str(dtmToday)
                
        # Create the sql query string
        sqlTableCol = ("intRopesRetiredReportID", "intRopeInspectionID", "intInspectorID", "dtmReportDate")
        sqlTableName = "TRopeRetiredReports"
        
        # Get the max primary key value for the table
        sqlMaxPrimKeyID = RopesRetiredReport.Get_Max_Primary_Key(self, sqlTableName, sqlTableCol[0])

        # For testing purposes, set the inspector ID to 1
        Inspector.intInspectorID = 1
        
        # Set the inspector ID
        # print(UserLogins.aCurrentUserLogin)
        # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID
        
        # Perform the insert query
        sqlTableValues = (sqlMaxPrimKeyID, self.intRopeInspectionID, Inspector.intInspectorID, self.dtmReportDate)

        # Set the parameters
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Update_Rope_RetiredReport_Query(self):
        """ 
        Function Name: Update_Rope_RetiredReport_Query
        Function Description: This function updated the database with all of the necessary objects
        """
        # Get todays date
        dtmToday = datetime.now().date()
        self.dtmReportDate = str(dtmToday)
                
        # Create the sql query string
        sqlTableCol = ("intRopesRetiredReportID", "intRopeInspectionID", "intInspectorID", "dtmReportDate")
        sqlTableName = "TRopeRetiredReports"
        sqlViewName = "vRopeInspectID_OutOfService"
        
        # Get the max primary key value for the table
        sqlRopeInspectValues = Queries.Get_All_DB_Values(self, sqlViewName)
        sqlRopeRetiredReportValues = Queries.Get_All_DB_Values(self, sqlTableName)
        
        # For testing purposes, set the inspector ID to 1
        Inspector.intInspectorID = 1
        
        # Set the inspector ID
        # print(UserLogins.aCurrentUserLogin)
        # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID

        # Process each inspection value
        for inspectValue in sqlRopeInspectValues:
            inspectionID = inspectValue[0]
            if inspectionID not in [report[0] for report in sqlRopeRetiredReportValues]:
                # Inspection ID not found in the report, consider adding it
                self.intRopeInspectionID = inspectionID
                RopesRetiredReport.Add_Rope_RetiredReport_Query(self)

            elif self.strEquipInUse != "Retired":
                # Remove the report if the device is no longer in service
                Queries.Remove_Attribute_Query(Queries, sqlTableName, sqlTableCol[0], inspectionID)

            else:
                # Update the existing report
                sqlTableValues = (inspectionID, self.intRopeInspectionID, Inspector.intInspectorID, self.dtmReportDate)
                sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], inspectionID)
                Queries.dbExeUSP_UpdateValues(Queries, sqlParams)
                
                                                
class Connectors():
    """
    Class Name: Connectors
    Class Description: This class gets and sets all of the Connectors attributes. 
    """
    # Create class variable shared amongst all Connectors methods
    aintConnectorIDCache = []
    astrSerialNumCache = []
    astrBumperNumCache = []
    astrManufactureNameCache = []
    adtmManufactureDateCache = []
    adtmInstallationDateCache = []
    adtmLastInspectionDateCache = []
    adtmNextInspectionDateCache = []
    astrDeviceTypeCache = []
    astrEquipInUseCache = []
    aTwoConnectorsCache = []

    # Instantiate the following attributes
    def __init__(self, intConnectorID, strSerialNum, strBumperNum, strManufactureName,
                    dtmManufactureDate, dtmInstallationDate, dtmLastInspectionDate, dtmNextInspectionDate, 
                    strDeviceType, strEquipInUse):
        self.intConnectorID = intConnectorID
        self.strSerialNum = strSerialNum
        self.strBumperNum = strBumperNum
        self.strManufactureName = strManufactureName
        self.dtmManufactureDate = dtmManufactureDate
        self.dtmInstallationDate = dtmInstallationDate
        self.dtmLastInspectionDate = dtmLastInspectionDate
        self.dtmNextInspectionDate = dtmNextInspectionDate
        self.strDeviceType = strDeviceType
        self.strEquipInUse = strEquipInUse

    # Property decorator object get function to access private intConnectorID
    @property
    def intConnectorID(self):
        return self._intConnectorID

    # Property decorator object get function to access private strSerialNum
    @property
    def strSerialNum(self):
        return self._strSerialNum

    # Property decorator object get function to access private strBumperNum
    @property
    def strBumperNum(self):
        return self._strBumperNum

    # Property decorator object get function to access private strManufactureName
    @property
    def strManufactureName(self):
        return self._strManufactureName
        
    # Property decorator object get function to access private dtmManufactureDate
    @property
    def dtmManufactureDate(self):
        return self._dtmManufactureDate

    # Property decorator object get function to access private dtmInstallationDate
    @property
    def dtmInstallationDate(self):
        return self._dtmInstallationDate

    # Property decorator object get function to access private dtmLastInspectionDate
    @property
    def dtmLastInspectionDate(self):
        return self._dtmLastInspectionDate

    # Property decorator object get function to access private dtmNextInspectionDate
    @property
    def dtmNextInspectionDate(self):
        return self._dtmNextInspectionDate

    # Property decorator object get function to access private strDeviceType
    @property
    def strDeviceType(self):
        return self._strDeviceType
    
    # Property decorator object get function to access private strEquipInUse
    @property
    def strEquipInUse(self):
        return self._strEquipInUse

    # setter method 
    @intConnectorID.setter 
    def intConnectorID(self, intConnectorID): 
        # Return true if specified object is of int type
        if not isinstance(intConnectorID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intConnectorID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intConnectorID = intConnectorID    

    # setter method 
    @strSerialNum.setter 
    def strSerialNum(self, strSerialNum): 
        # Return true if specified object is of str type
        if not isinstance(strSerialNum, str): 
            raise TypeError('Serial Number must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strSerialNum.isspace(): 
            raise ValueError('Serial Number cannot be empty') 
        # Set the attribute to the value if true
        if strSerialNum.isascii():
            self._strSerialNum = strSerialNum  

    # setter method 
    @strBumperNum.setter 
    def strBumperNum(self, strBumperNum): 
        # Return true if specified object is of str type
        if not isinstance(strBumperNum, str): 
            raise TypeError('Bumper Number must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strBumperNum.isspace(): 
            raise ValueError('Bumper Number cannot be empty') 
        # Set the attribute to the value if true
        if strBumperNum.isascii():
            self._strBumperNum = strBumperNum   

    # setter method 
    @strManufactureName.setter 
    def strManufactureName(self, strManufactureName):   
        # Return true if specified object is of str type
        if not isinstance(strManufactureName, str): 
            raise TypeError('Manufacture Name must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if strManufactureName.isspace(): 
            raise ValueError('Manufacture Name cannot be empty') 
        # Set the attribute to the value if true
        if strManufactureName.isascii():
            self._strManufactureName = strManufactureName   
                        
    # setter method 
    @dtmManufactureDate.setter 
    def dtmManufactureDate(self, dtmManufactureDate): 
        # Return true if specified object is of str type
        if not isinstance(dtmManufactureDate, str): 
            raise TypeError('Manufacture Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmManufactureDate.isspace(): 
            raise ValueError('Manufacture Date cannot be empty')       
        # Convert the date to string
        dtmManufactureDate = datetime.strptime(dtmManufactureDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmManufactureDate, date): 
            raise TypeError('Manufacture Date must be a valid date') 
        # Convert the date back to string
        dtmManufactureDate = str(dtmManufactureDate)

        self._dtmManufactureDate = dtmManufactureDate   

    # setter method 
    @dtmInstallationDate.setter 
    def dtmInstallationDate(self, dtmInstallationDate): 
        # Return true if specified object is of str type
        if not isinstance(dtmInstallationDate, str): 
            raise TypeError('Install Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmInstallationDate.isspace(): 
            raise ValueError('Install Date cannot be empty')       
        # Convert the date to string
        dtmInstallationDate = datetime.strptime(dtmInstallationDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmInstallationDate, date): 
            raise TypeError('Install Date must be a valid date') 
        # Convert the date back to string
        dtmInstallationDate = str(dtmInstallationDate)

        self._dtmInstallationDate = dtmInstallationDate    
        
    # setter method 
    @dtmLastInspectionDate.setter 
    def dtmLastInspectionDate(self, dtmLastInspectionDate): 
        # Return true if specified object is of str type
        if not isinstance(dtmLastInspectionDate, str): 
            raise TypeError('Last Inspection Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmLastInspectionDate.isspace(): 
            raise ValueError('Last Inspection Date cannot be empty')       
        # Convert the date to string
        dtmLastInspectionDate = datetime.strptime(dtmLastInspectionDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmLastInspectionDate, date): 
            raise TypeError('Last Inspection Date must be a valid date') 
        # Convert the date back to string
        dtmLastInspectionDate = str(dtmLastInspectionDate)

        self._dtmLastInspectionDate = dtmLastInspectionDate   

    # setter method 
    @dtmNextInspectionDate.setter 
    def dtmNextInspectionDate(self, dtmNextInspectionDate): 
        # Return true if specified object is of str type
        if not isinstance(dtmNextInspectionDate, str): 
            raise TypeError('Next Inspection Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmNextInspectionDate.isspace(): 
            raise ValueError('Next Inspection Date cannot be empty')       
        # Convert the date to string
        dtmNextInspectionDate = datetime.strptime(dtmNextInspectionDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmNextInspectionDate, date): 
            raise TypeError('Next Inspection Date must be a valid date') 
        # Convert the date back to string
        dtmNextInspectionDate = str(dtmNextInspectionDate)

        self._dtmNextInspectionDate = dtmNextInspectionDate   
                
    # setter method 
    @strDeviceType.setter
    def strDeviceType(self, strDeviceType):
        # Check if the input is a string
        if not isinstance(strDeviceType, str):
            raise TypeError('Device Type must be a string')

        # Check if the string is empty or consists only of whitespace
        if strDeviceType.isspace() or not strDeviceType:
            raise ValueError('Device Type Status cannot be empty')

        # Split the string by spaces and check each word
        words = strDeviceType.split()
        for word in words:
            # Check if the word is alpha or hyphenated
            if not all(subpart.isalpha() for subpart in word.split('-')):
                raise ValueError('Device Type must be a string of letters, hyphenated words, or multiple words separated by spaces')

        self._strDeviceType = strDeviceType   

    # setter method 
    @strEquipInUse.setter 
    def strEquipInUse(self, strEquipInUse): 
        # Return true if specified object is of str type
        if not isinstance(strEquipInUse, str): 
            raise TypeError('In Use Status must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if strEquipInUse.isspace(): 
            raise ValueError('In Use Status cannot be empty') 
        # Set the attribute to the value if true
        elif strEquipInUse.isalpha():
            self._strEquipInUse = strEquipInUse   

    def Append_ConnectorIDList(self, intObject):
        """ 
        Function Name: Append_ConnectorIDList
        Function Description: This function appends objects to the Connector ID list
        """    
        self.aintConnectorIDCache.append(intObject)

    def Remove_ConnectorIDList(self, intObject):
        """ 
        Function Name: Remove_ConnectorIDList
        Function Description: This function removes objects in the Connector ID list
        """    
        self.aintConnectorIDCache.remove(intObject)

    def Get_ConnectorIDList_Obj(self):
        """ 
        Function Name: Get_ConnectorIDList_Obj
        Function Description: This function gets all the objects in the Connector ID list
        """    
        return self.aintConnectorIDCache            

    def Append_Connector_SerialNumList(self, strObject):
        """ 
        Function Name: Append_Connector_SerialNumList
        Function Description: This function appends objects to the Serial Num list
        """    
        self.astrSerialNumCache.append(strObject)

    def Remove_Connector_SerialNumList(self, strObject):
        """ 
        Function Name: Remove_Connector_SerialNumList
        Function Description: This function removes objects in the Serial Num list
        """    
        self.astrSerialNumCache.remove(strObject)

    def Get_Connector_SerialNumList_Obj(self):
        """ 
        Function Name: Get_Connector_SerialNumList_Obj
        Function Description: This function gets all the objects in the Serial Num list
        """    
        return self.astrSerialNumCache 

    def Append_Connector_BumperNumList(self, strObject):
        """ 
        Function Name: Append_Connector_BumperNumList
        Function Description: This function appends objects to the Bumper Num list
        """    
        self.astrBumperNumCache.append(strObject)

    def Remove_Connector_BumperNumList(self, strObject):
        """ 
        Function Name: Remove_Connector_BumperNumList
        Function Description: This function removes objects in the Bumper Num list
        """    
        self.astrBumperNumCache.remove(strObject)

    def Get_Connector_BumperNumList_Obj(self):
        """ 
        Function Name: Get_Connector_BumperNumList_Obj
        Function Description: This function gets all the objects in the Bumper Num list
        """    
        return self.astrBumperNumCache 

    def Append_Connector_ManuNameList(self, strObject):
        """ 
        Function Name: Append_Connector_ManuNameList
        Function Description: This function appends objects to the ManuFacture Name list
        """    
        self.astrManufactureNameCache.append(strObject)

    def Remove_Connector_ManuNameList(self, strObject):
        """ 
        Function Name: Remove_Connector_ManuNameList
        Function Description: This function removes objects in the ManuFacture Name list
        """    
        self.astrManufactureNameCache.remove(strObject)

    def Get_Connector_ManuNameList_Obj(self):
        """ 
        Function Name: Get_Connector_ManuNameList_Obj
        Function Description: This function gets all the objects in the ManuFacture Name list
        """    
        return self.astrManufactureNameCache

    def Append_Connector_ManuDateList(self, strObject):
        """ 
        Function Name: Append_Connector_ManuDateList
        Function Description: This function appends objects to the ManuFacture Date list
        """    
        self.adtmManufactureDateCache.append(strObject)

    def Remove_Connector_ManuDateList(self, strObject):
        """ 
        Function Name: Remove_Connector_ManuDateList
        Function Description: This function removes objects in the ManuFacture Date list
        """    
        self.adtmManufactureDateCache.remove(strObject)

    def Get_Connector_ManuDateList_Obj(self):
        """ 
        Function Name: Get_Connector_ManuDateList_Obj
        Function Description: This function gets all the objects in the ManuFacture Date list
        """    
        return self.adtmManufactureDateCache

    def Append_Connector_InstallDateList(self, strObject):
        """ 
        Function Name: Append_Connector_InstallDateList
        Function Description: This function appends objects to the Install Date list
        """    
        self.adtmInstallationDateCache.append(strObject)

    def Remove_Connector_InstallDateList(self, strObject):
        """ 
        Function Name: Remove_Connector_InstallDateList
        Function Description: This function removes objects in the Install Date list
        """    
        self.adtmInstallationDateCache.remove(strObject)

    def Get_Connector_InstallDateList_Obj(self):
        """ 
        Function Name: Get_Connector_InstallDateList_Obj
        Function Description: This function gets all the objects in the Install Date list
        """    
        return self.adtmInstallationDateCache

    def Append_Connector_LastInspectDateList(self, strObject):
        """ 
        Function Name: Append_Connector_LastInspectDateList
        Function Description: This function appends objects to the Last Inspect Date list
        """    
        self.adtmLastInspectionDateCache.append(strObject)

    def Remove_Connector_LastInspectDateList(self, strObject):
        """ 
        Function Name: Remove_Connector_LastInspectDateList
        Function Description: This function removes objects in the Last Inspect Date list
        """    
        self.adtmLastInspectionDateCache.remove(strObject)

    def Get_Connector_LastInspectDateList_Obj(self):
        """ 
        Function Name: Get_Connector_LastInspectDateList_Obj
        Function Description: This function gets all the objects in the Last Inspect Date list
        """    
        return self.adtmLastInspectionDateCache

    def Append_Connector_NextInspectDateList(self, strObject):
        """ 
        Function Name: Append_Connector_NextInspectDateList
        Function Description: This function appends objects to the Next Inspect Date list
        """    
        self.adtmNextInspectionDateCache.append(strObject)

    def Remove_Connector_NextInspectDateList(self, strObject):
        """ 
        Function Name: Remove_Connector_NextInspectDateList
        Function Description: This function removes objects in the Next Inspect Date list
        """    
        self.adtmNextInspectionDateCache.remove(strObject)

    def Get_Connector_NextInspectDateList_Obj(self):
        """ 
        Function Name: Get_Connector_NextInspectDateList_Obj
        Function Description: This function gets all the objects in the Next Inspect Date list
        """    
        return self.adtmNextInspectionDateCache

    def Append_Connector_Device_Type_EquipInUseList(self, strObject):
        """ 
        Function Name: Append_Device_Type_EquipInUseList
        Function Description: This function appends objects to the Device Type list
        """    
        self.astrDeviceTypeCache.append(strObject)

    def Remove_Connector_Device_Type_EquipInUseList(self, strObject):
        """ 
        Function Name: Remove_Device_Type_EquipInUseList
        Function Description: This function removes objects in the Device Type list
        """    
        self.astrDeviceTypeCache.remove(strObject)

    def Get_Connector_Device_Type_List_Obj(self):
        """ 
        Function Name: Get_Device_Type_List_Obj
        Function Description: This function gets all the objects in the Device Type list
        """    
        return self.astrDeviceTypeCache
    
    def Append_Connector_EquipInUseList(self, strObject):
        """ 
        Function Name: Append_Connector_EquipInUseList
        Function Description: This function appends objects to the Equipment In Use list
        """    
        self.astrEquipInUseCache.append(strObject)

    def Remove_Connector_EquipInUseList(self, strObject):
        """ 
        Function Name: Remove_Connector_EquipInUseList
        Function Description: This function removes objects in the Equipment In Use list
        """    
        self.astrEquipInUseCache.remove(strObject)

    def Get_Connector_EquipInUseList_Obj(self):
        """ 
        Function Name: Get_Connector_EquipInUseList_Obj
        Function Description: This function gets all the objects in the Equipment In Use list
        """    
        return self.astrEquipInUseCache

    def Append_TwoConnector_StageList(self, strObject):
        """ 
        Function Name: Append_Connector_EquipInUseList
        Function Description: This function appends objects to the Equipment In Use list
        """    
        self.aTwoConnectorsCache.append(strObject)

    def Remove_TwoConnector_StageList(self, strObject):
        """ 
        Function Name: Remove_Connector_EquipInUseList
        Function Description: This function removes objects in the Equipment In Use list
        """    
        self.aTwoConnectorsCache.remove(strObject)

    def Get_TwoConnector_StageList_Obj(self):
        """ 
        Function Name: Get_Connector_EquipInUseList_Obj
        Function Description: This function gets all the objects in the Equipment In Use list
        """    
        return self.aTwoConnectorsCache    
                
    def Get_Connectors_Data(self):
        """ 
        Function Name: Get_Connectors_Data
        Function Description: This function gets all the objects in the Connectors table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TConnectors"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # First check if the contents are found and if yes, proceed to get the contents of the table
        if QueryResultList is not None:
            # Append the Auto Belay Data List
            for i in range(len(QueryResultList)):
                Connectors.Append_ConnectorIDList(self, QueryResultList[i][0])
                Connectors.Append_Connector_SerialNumList(self, QueryResultList[i][1]) 
                Connectors.Append_Connector_BumperNumList(self, QueryResultList[i][2]) 
                Connectors.Append_Connector_ManuNameList(self, QueryResultList[i][3]) 
                Connectors.Append_Connector_ManuDateList(self, QueryResultList[i][4]) 
                Connectors.Append_Connector_InstallDateList(self, QueryResultList[i][5]) 
                Connectors.Append_Connector_LastInspectDateList(self, QueryResultList[i][6]) 
                Connectors.Append_Connector_NextInspectDateList(self, QueryResultList[i][7]) 
                Connectors.Append_Connector_Device_Type_EquipInUseList(self, QueryResultList[i][8]) 
                Connectors.Append_Connector_EquipInUseList(self, QueryResultList[i][9]) 
                
    def Set_Connectors_Selection(self):
        """ 
        Function Name: Set_Connectors_Selection
        Function Description: This function will set the selection name from the user and will update the 
        class objects with the data from the database.
        """    
        # First get the selection from the user 
        for i, item in enumerate(self.astrSerialNumCache):
            if self.strSerialNum == item:
                # Assign the iterable num to the ID num and assign the objects to the desired data sets    
                self.intConnectorID = self.aintConnectorIDCache[i]
                if not self.strSerialNum:                    
                    self.strSerialNum = self.astrSerialNumCache[i]
                self.strBumperNum = self.astrBumperNumCache[i]
                self.strManufactureName = self.astrManufactureNameCache[i]
                self.dtmManufactureDate = self.adtmManufactureDateCache[i]
                self.dtmInstallationDate = self.adtmInstallationDateCache[i]
                self.dtmServiceDate = self.adtmInstallationDateCache[i]
                self.dtmLastInspectionDate = self.adtmLastInspectionDateCache[i]
                self.dtmNextInspectionDate = self.adtmNextInspectionDateCache[i]
                self.strDeviceType = self.astrDeviceTypeCache[i]
                if not self.strEquipInUse:
                    self.strEquipInUse = self.astrEquipInUseCache[i] 
                
                break

    def Set_Connectors_Data(self):
        """ 
        Function Name: Set_Connectors_Data
        Function Description: This function will set the class objects for the device when selected
        """    
        # First get the selection from the user 
        for i, item in enumerate(self.astrSerialNumCache):
            if self.strSerialNum == item:
                # Assign the iterable num to the ID num and assign the objects to the desired data sets    
                self.intConnectorID = self.aintConnectorIDCache[i]                
                self.strSerialNum = self.astrSerialNumCache[i]
                self.strBumperNum = self.astrBumperNumCache[i]
                self.strManufactureName = self.astrManufactureNameCache[i]
                self.dtmManufactureDate = self.adtmManufactureDateCache[i]
                self.dtmInstallationDate = self.adtmInstallationDateCache[i]
                self.dtmLastInspectionDate = self.adtmLastInspectionDateCache[i]
                self.dtmNextInspectionDate = self.adtmNextInspectionDateCache[i]
                self.strDeviceType = self.astrDeviceTypeCache[i]
                self.strEquipInUse = self.astrEquipInUseCache[i]
                # Set the global class bool to true
                Bool_Flag.Set_Connector_Bool_Value_True(Bool_Flag)    
                
                break

    def Add_Connectors_Query(self):
        """ 
        Function Name: Add_Connectors_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Create the sql query string
        sqlTableCol = ("intConnectorID", "strSerialNum", "strBumperNum", "strManufactureName", "dtmManufactureDate", 
                    "dtmInstallationDate", "dtmLastInspectionDate", "dtmNextInspectionDate", "strDeviceType", "strEquipInUse")   
        sqlTableName = "TConnectors"  

        # Set the Table values and the params tuple
        sqlTableValues = (self.intConnectorID, self.strSerialNum, self.strBumperNum, self.strManufactureName, 
                            self.dtmManufactureDate, self.dtmInstallationDate, self.dtmLastInspectionDate, 
                            self.dtmNextInspectionDate, self.strDeviceType, self.strEquipInUse)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

        # Reload the data after user submits entry
        Connectors.Delete_Connectors_Data(Connectors)
        Connectors.Get_Connectors_Data(Connectors)

    def Update_Connectors_Inspect_Dates(self):
        """ 
        Function Name: Update_Connectors_Inspect_Dates
        Function Description: This function updated the database with inspection dates last and next
        """    
        # Create the sql query string
        sqlTableCol = ("intConnectorID", "dtmLastInspectionDate", "dtmNextInspectionDate")   
        sqlTableName = "TConnectors"  

        # Set the last and next inspection date based off of the current date
        aDateResult = BaseFunctions.Update_Inspection_Date()
        self.dtmLastInspectionDate = datetime.strftime(aDateResult[0], '%Y-%m-%d')
        self.dtmNextInspectionDate = datetime.strftime(aDateResult[1], '%Y-%m-%d')
        
        # Set the Table values and the params tuple
        sqlTableValues = (self.intConnectorID, self.dtmLastInspectionDate, self.dtmNextInspectionDate)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], sqlTableValues[0])         

        # Execute the stored procedure
        Queries.dbExeUSP_UpdateValues(Queries, sqlParams)

    def Update_Connectors_InUse_Status(self):
        """ 
        Function Name: Update_Connectors_InUse_Status
        Function Description: This function updated the database with in use status of the Connector
        """ 
        # Declare Local Variables
        intFailStatus = int(3)
        
        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(ConnectorInspect.aConnectorInspectStatus)
            
        if intOverallStatus == intFailStatus:
            # Check if the user knows about the Connector being failed. If the user removed from wall, the Connector is not longer in use
            messagebox.showwarning(message='ATTENTION! \n\nWe have identified an overall status --> FAIL <-- for this Connector. \n\nPlease remove the retired connector from future use.')
            self.strEquipInUse = "Retired"
            Bool_Flag.Set_ConnectorRetired_Bool_Value_True(Bool_Flag)
            
        # Create the sql query string
        sqlTableCol = ("intConnectorID", "strEquipInUse")   
        sqlTableName = "TConnectors"  

        # Set the Table values and the params tuple
        sqlTableValues = (self.intConnectorID, self.strEquipInUse)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], sqlTableValues[0])         

        # Execute the stored procedure
        Queries.dbExeUSP_UpdateValues(Queries, sqlParams)

    def Update_TwoConnectors_InUse_Status(self):
        """ 
        Function Name: Update_TwoConnectors_InUse_Status
        Function Description: This function updated the database with in use status of the Two Connector
        """ 
        # Declare Local Variables
        intFailStatus = int(3)
        strRetiredStatus = str("Retired")

        # Create the sql query string
        sqlTableCol = ("intConnectorID", "strEquipInUse")   
        sqlTableName = "TConnectors"  
        
        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(ConnectorInspect.aConnectorInspectStatus)
            
        if intOverallStatus == intFailStatus:
            # Prompt the user about the failed status and instruct to retire the connector
            user_response = messagebox.showwarning(
                title="Attention Required!",
                message='ATTENTION!\n\nWe have identified an overall status --> FAIL <-- for a Connector(s).'
                        ' \n\nPlease remove the retired connector from future use.'
            )
            if user_response:
                Bool_Flag.Set_ConnectorRetired_Bool_Value_True(Bool_Flag)

        # Get the two connectors data
        aTwoConnectorList = Connectors.Get_TwoConnector_StageList_Obj(Connectors)
        
        for i, item in enumerate(aTwoConnectorList):    
            connectorID = item[0]
            
            # Set the currentStatus based off of the overall status
            if ConnectorInspect.aConnectorInspectStatus[i] == intFailStatus:
                currentStatus = strRetiredStatus
            else:
                currentStatus = item[9]
                
            # Set the Table values and the params tuple
            sqlTableValues = (connectorID, currentStatus)
            sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], sqlTableValues[0])         

            # Execute the stored procedure
            Queries.dbExeUSP_UpdateValues(Queries, sqlParams)
                        
    def Update_NewConnectors_Query(self):
        """ 
        Function Name: Update_NewConnectors_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Create the sql query string
        sqlTableCol = ("intConnectorID", "strSerialNum", "strBumperNum", "strManufactureName", 
                        "dtmManufactureDate", "dtmInstallationDate", "dtmLastInspectionDate", 
                        "dtmNextInspectionDate", "strDeviceType", "strEquipInUse")   
        sqlTableName = "TConnectors"  

        # Set the Table values and the params tuple
        sqlTableValues = (self.intConnectorID, self.strSerialNum, self.strBumperNum, self.strManufactureName, 
                        self.dtmManufactureDate, self.dtmInstallationDate, self.dtmLastInspectionDate, 
                        self.dtmNextInspectionDate, self.strDeviceType, self.strEquipInUse)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], sqlTableValues[0])       

        # Execute the stored procedure
        Queries.dbExeUSP_UpdateValues(Queries, sqlParams)

        # Reload the data after user submits entry
        Connectors.Delete_Connectors_Data(Connectors)
        Connectors.Get_Connectors_Data(Connectors)
        
    def Set_Global_Connectors_Attributes(self):
        """ 
        Function Name: Set_Global_Connectors_Attributes
        Function Description: This function sets Connectors attributes once the user proceeds with adding a new
        Connectors to the database.
        """    
        Connectors.strSerialNum = self.strSerialNum
        Connectors.strBumperNum = self.strBumperNum
        Connectors.strManufactureName = self.strManufactureName
        Connectors.dtmManufactureDate = self.dtmManufactureDate
        Connectors.dtmInstallationDate = self.dtmInstallationDate
        Connectors.dtmLastInspectionDate = self.dtmLastInspectionDate
        Connectors.dtmNextInspectionDate = self.dtmNextInspectionDate
        Connectors.strDeviceType = self.strDeviceType
        Connectors.strEquipInUse = self.strEquipInUse

    def Delete_Connectors_Data(self):
        """ 
        Function Name: Delete_Connectors_Data
        Function Description: This function removes all the objects in the Connectors class
        """    
        Connectors.aintConnectorIDCache = []  
        Connectors.astrSerialNumCache = []
        Connectors.astrBumperNumCache = []
        Connectors.astrManufactureNameCache = []
        Connectors.adtmManufactureDateCache = []
        Connectors.adtmInstallationDateCache = []
        Connectors.adtmLastInspectionDateCache = []
        Connectors.adtmNextInspectionDateCache = []
        Connectors.astrDeviceTypeCache = []
        Connectors.astrEquipInUseCache = []    
        Connectors.aTwoConnectorsCache = []

    def Set_TwoConnectorsCache_Attributes(self):
        """ 
        Function Name: Set_TwoConnectorsCache_Attributes
        Function Description: This function sets Connectors attributes once the user proceeds with inspecting two 
        connectors.
        """    
        # Set the Table values and the params tuple
        aValues = (self.intConnectorID, self.strSerialNum, self.strBumperNum, self.strManufactureName, 
                        self.dtmManufactureDate, self.dtmInstallationDate, self.dtmLastInspectionDate, 
                        self.dtmNextInspectionDate, self.strDeviceType, self.strEquipInUse)
        
        Connectors.Append_TwoConnector_StageList(self, aValues)
            
class ConnectorFunction():
    """
    Class Name: ConnectorFunction
    Class Description: This class gets and sets all of the Connector Function attributes. 
    """
    # Create class variable shared amongst all Connector Function methods
    aintConnectorFunctionID = []
    astrConnectorFunctionDesc = []
        
    # Instantiate the following attributes
    def __init__(self, intConnectorFunctionID, strConnectorFunctionDesc):
        self.intConnectorFunctionID = intConnectorFunctionID
        self.strConnectorFunctionDesc = strConnectorFunctionDesc

    # Property decorator object get function to access private intConnectorFunctionID
    @property
    def intConnectorFunctionID(self):
        return self._intConnectorFunctionID

    # Property decorator object get function to access private strConnectorFunctionDesc
    @property
    def strConnectorFunctionDesc(self):
        return self._strConnectorFunctionDesc
        
    # setter method 
    @intConnectorFunctionID.setter 
    def intConnectorFunctionID(self, intConnectorFunctionID): 
        # Return true if specified object is of int type
        if not isinstance(intConnectorFunctionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intConnectorFunctionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intConnectorFunctionID = intConnectorFunctionID 
        
    # setter method 
    @strConnectorFunctionDesc.setter 
    def strConnectorFunctionDesc(self, strConnectorFunctionDesc): 
        # Return true if specified object is of str type
        if not isinstance(strConnectorFunctionDesc, str): 
            raise TypeError('Hose Length must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if strConnectorFunctionDesc.isspace(): 
            raise ValueError('Hose Length cannot be empty') 
        # Set the attribute to the value if true
        elif strConnectorFunctionDesc.isascii():
            self._strConnectorFunctionDesc = strConnectorFunctionDesc

    def Append_ConnectorFunctIDList(self, intObject):
        """ 
        Function Name: Append_ConnectorFunctIDList
        Function Description: This function appends objects to the Connector Function ID list
        """    
        self.aintConnectorFunctionID.append(intObject)

    def Remove_ConnectorFunctIDList(self, intObject):
        """ 
        Function Name: Remove_ConnectorFunctIDList
        Function Description: This function removes objects in the Connector Function ID list
        """    
        self.aintConnectorFunctionID.remove(intObject)

    def Get_ConnectorFunctIDList_Obj(self):
        """ 
        Function Name: Get_ConnectorFunctIDList_Obj
        Function Description: This function gets all the objects in the Connector Function ID list
        """    
        return self.aintConnectorFunctionID
    
    def Append_ConnectorFunctList(self, strObject):
        """ 
        Function Name: Append_ConnectorFunctList
        Function Description: This function appends objects to the Connector Function list
        """    
        self.astrConnectorFunctionDesc.append(strObject)

    def Remove_ConnectorFunctList(self, strObject):
        """ 
        Function Name: Remove_ConnectorFunctList
        Function Description: This function removes objects in the Connector Function list
        """    
        self.astrConnectorFunctionDesc.remove(strObject)

    def Get_ConnectorFunctList_Obj(self):
        """ 
        Function Name: Get_ConnectorFunctList_Obj
        Function Description: This function gets all the objects in the Connector Function list
        """    
        return self.astrConnectorFunctionDesc   

    def Get_ConnectorFunct_Data(self):
        """ 
        Function Name: Get_ConnectorFunct_Data
        Function Description: This function gets all the objects in the Connector Functions table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TConnectorFunctions"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the housing Data List
        for i in range(len(QueryResultList)):
            ConnectorFunction.Append_ConnectorFunctIDList(self, QueryResultList[i][0])
            ConnectorFunction.Append_ConnectorFunctList(self, QueryResultList[i][1]) 

    def Delete_ConnectorFunct_Data(self):
        """ 
        Function Name: Delete_ConnectorFunct_Data
        Function Description: This function removes all the objects in the Connector Function class
        """    
        ConnectorFunction.aintConnectorFunctionID = []
        ConnectorFunction.astrConnectorFunctionDesc = []
        
        

class ConnectorVisSelection():
    """
    Class Name: ConnectorVisSelection
    Class Description: This class gets and sets all of the Connector Visual Selections. 
    """
    # Create class variable shared amongst all Connector visual methods
    aintConnectorVisMetalSelectID = []
    astrConnectorVisMetalSelect = []
    astrSecondConnectorVisMetalSelect = []
    aTwoConnectorVisSelectCache = []
        
    # Instantiate the following attributes
    def __init__(self, intConnectorVisMetalSelectID, strConnectorVisMetalSelect, strConnectorVisStatus):
        self.intConnectorVisMetalSelectID = intConnectorVisMetalSelectID
        self.strConnectorVisMetalSelect = strConnectorVisMetalSelect
        self.strConnectorVisStatus = strConnectorVisStatus

    # Property decorator object get function to access private intConnectorVisMetalSelectID
    @property
    def intConnectorVisMetalSelectID(self):
        return self._intConnectorVisMetalSelectID

    # Property decorator object get function to access private strConnectorVisMetalSelect
    @property
    def strConnectorVisMetalSelect(self):
        return self._strConnectorVisMetalSelect

    # Property decorator object get function to access private strConnectorVisStatus
    @property
    def strConnectorVisStatus(self):
        return self._strConnectorVisStatus
            
    # setter method 
    @intConnectorVisMetalSelectID.setter 
    def intConnectorVisMetalSelectID(self, intConnectorVisMetalSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intConnectorVisMetalSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intConnectorVisMetalSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intConnectorVisMetalSelectID = intConnectorVisMetalSelectID 
        
    # setter method 
    @strConnectorVisMetalSelect.setter 
    def strConnectorVisMetalSelect(self, strConnectorVisMetalSelect): 
        # Return true if specified object is of str type
        if not isinstance(strConnectorVisMetalSelect, str): 
            raise TypeError('Connector visual input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strConnectorVisMetalSelect.isspace(): 
            raise ValueError('Connector visual input cannot be empty') 
        # Set the attribute to the value if true
        elif strConnectorVisMetalSelect.isascii():
            self._strConnectorVisMetalSelect = strConnectorVisMetalSelect

    # setter method 
    @strConnectorVisStatus.setter 
    def strConnectorVisStatus(self, strConnectorVisStatus): 
        # Return true if specified object is of str type
        if not isinstance(strConnectorVisStatus, str): 
            raise TypeError('Connector visual status input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strConnectorVisStatus.isspace(): 
            raise ValueError('Connector visual status input cannot be empty') 
        # Set the attribute to the value if true
        elif strConnectorVisStatus.isascii():
            self._strConnectorVisStatus = strConnectorVisStatus

    def Append_ConnectorVisIDList(self, intObject):
        """ 
        Function Name: Append_ConnectorVisIDList
        Function Description: This function appends objects to the Connector Visual Selection ID list
        """    
        self.aintConnectorVisMetalSelectID.append(intObject)

    def Remove_ConnectorVisIDList(self, intObject):
        """ 
        Function Name: Remove_ConnectorVisIDList
        Function Description: This function removes objects in the Connector Visual Selection ID list
        """    
        self.aintConnectorVisMetalSelectID.remove(intObject)

    def Get_ConnectorVisIDList_Obj(self):
        """ 
        Function Name: Get_ConnectorVisIDList_Obj
        Function Description: This function gets all the objects in the Connector Visual Selection ID list
        """    
        return self.aintConnectorVisMetalSelectID
    
    def Append_ConnectorVisSelectList(self, strObject):
        """ 
        Function Name: Append_ConnectorVisSelectList
        Function Description: This function appends objects to the Connector Visual Selection list
        """    
        self.astrConnectorVisMetalSelect.append(strObject)

    def Remove_ConnectorVisSelectList(self, strObject):
        """ 
        Function Name: Remove_ConnectorVisSelectList
        Function Description: This function removes objects in the Connector Visual Selection list
        """    
        self.astrConnectorVisMetalSelect.remove(strObject)

    def Get_ConnectorVisSelectList_Obj(self):
        """ 
        Function Name: Get_ConnectorVisSelectList_Obj
        Function Description: This function gets all the objects in the Connector Visual Selection list
        """    
        return self.astrConnectorVisMetalSelect   

    def Append_Second_ConnectorVisSelectList(self, strObject):
        """ 
        Function Name: Append_Second_ConnectorVisSelectList
        Function Description: This function appends objects to the Second Connector Visual Selection list
        """    
        self.astrSecondConnectorVisMetalSelect.append(strObject)

    def Remove_Second_ConnectorVisSelectList(self, strObject):
        """ 
        Function Name: Remove_Second_ConnectorVisSelectList
        Function Description: This function removes objects in the Second Connector Visual Selection list
        """    
        self.astrSecondConnectorVisMetalSelect.remove(strObject)

    def Get_Second_ConnectorVisSelectList_Obj(self):
        """ 
        Function Name: Get_Second_ConnectorVisSelectList_Obj
        Function Description: This function gets all the objects in the Second Connector Visual Selection list
        """    
        return self.astrSecondConnectorVisMetalSelect 

    def Append_Two_ConnectorVisSelect_CacheList(self, strObject):
        """ 
        Function Name: Append_Two_ConnectorVisSelect_CacheList
        Function Description: This function appends objects to the Two Connector Visual Selection list
        """    
        self.aTwoConnectorVisSelectCache.append(strObject)

    def Remove_Two_ConnectorVisSelect_CacheList(self, strObject):
        """ 
        Function Name: Remove_Two_ConnectorVisSelect_CacheList
        Function Description: This function removes objects in the Two Connector Visual Selection list
        """    
        self.aTwoConnectorVisSelectCache.remove(strObject)

    def Get_Two_ConnectorVisSelect_CacheList_Obj(self):
        """ 
        Function Name: Get_Two_ConnectorVisSelect_CacheList_Obj
        Function Description: This function gets all the objects in the Two Connector Visual Selection list
        """    
        return self.aTwoConnectorVisSelectCache 
                            
    def Delete_ConnectorVisSelectList_Data(self):
        """ 
        Function Name: Delete_ConnectorVisSelectList_Data
        Function Description: This function removes all the objects in the Connector Visual Selection class
        """    
        ConnectorVisSelection.aintConnectorVisMetalSelectID = []
        ConnectorVisSelection.astrConnectorVisMetalSelect = []
        ConnectorVisSelection.astrSecondConnectorVisMetalSelect = []
        ConnectorVisSelection.aTwoConnectorVisSelectCache = []

    def Check_ConnectorVisSelection_Dup(self):
        """ 
        Function Name: Check_ConnectorVisSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        Connector visual selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intConnectorVisMetalSelectID", "strConnectorVisMetalSelect")   
        sqlTableName = "TConnectorVisTextSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strConnectorVisMetalSelect in sqlDupValues[i]:
                self.intConnectorVisMetalSelectID = sqlDupValues[i][0]
                self.strConnectorVisMetalSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag

    def Set_TwoConnectorVisualSelect_Data(self):
        """ 
        Function Name: Set_TwoConnectorVisualSelect_Data
        Function Description: This function sets all the objects in the Connector Visual Selection class
        """ 
        # Check if there is a duplicate, if so, only add one entry to the database
        if ConnectorVisSelection.aTwoConnectorVisSelectCache[0][0] != ConnectorVisSelection.aTwoConnectorVisSelectCache[1][0]:
            for v in ConnectorVisSelection.aTwoConnectorVisSelectCache:
                self.intConnectorVisMetalSelectID = v[0]
                self.strConnectorVisMetalSelect = v[1]
                self.strConnectorVisStatus = v[2]
            
                # Execute the stored procedure
                ConnectorVisSelection.Add_ConnectorVisSelectList_Query(ConnectorVisSelection)
        else:
            self.intConnectorVisMetalSelectID = ConnectorVisSelection.aTwoConnectorVisSelectCache[0][0]
            self.strConnectorVisMetalSelect = ConnectorVisSelection.aTwoConnectorVisSelectCache[0][1]
            self.strConnectorVisStatus = ConnectorVisSelection.aTwoConnectorVisSelectCache[0][2]
            
            # Execute the stored procedure
            ConnectorVisSelection.Add_ConnectorVisSelectList_Query(ConnectorVisSelection)
                
    def Add_ConnectorVisSelectList_Query(self):
        """ 
        Function Name: Add_ConnectorVisSelectList_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewConnectorVisSelection
        """    
        # Create the sql query params
        sqlTableCol = ("intConnectorVisMetalSelectID", "strConnectorVisMetalSelect")   
        sqlTableName = "TConnectorVisMetalSelects"
        sqlTableValues = (ConnectorVisSelection.intConnectorVisMetalSelectID, ConnectorVisSelection.strConnectorVisMetalSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams) 

    def Clear_ConnectorVisSel_Attributes(self):
        """ 
        Function Name: Clear_ConnectorVisSel_Attributes
        Function Description: This function clears the Connector Visual Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intConnectorVisMetalSelectID", "strConnectorVisMetalSelect")   
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                
                
class ConnectorVisualInspect(Connectors, InspectionType, ConnectorVisSelection, InspectionStatus):
    """
    Class Name: ConnectorVisualInspect
    Class Description: This class gets and sets all of the Connector Visual Inspection attributes. 
    """
    # Create class variable shared amongst all Connector Visual Inspection methods
    aintConnectorVisualInspectionID = []
    aConnectorVisualCache = []
        
    # Instantiate the following attributes
    def __init__(self, intConnectorVisualInspectionID, intConnectorID, intInspectionTypeID, intConnectorVisMetalSelectID, intInspectionStatusID):
        self.intConnectorVisualInspectionID = intConnectorVisualInspectionID
        # Inherits the child class with all the necessary objects
        Connectors.__init__(intConnectorID)
        InspectionType.__init__(intInspectionTypeID)
        ConnectorVisSelection.__init__(intConnectorVisMetalSelectID)
        InspectionStatus.__init__(intInspectionStatusID)

    # property decorator object get function to access private intConnectorVisualInspectionID
    @property
    def intConnectorVisualInspectionID(self):
        return self._intConnectorVisualInspectionID

    # setter method 
    @intConnectorVisualInspectionID.setter 
    def intConnectorVisualInspectionID(self, intConnectorVisualInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intConnectorVisualInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Connector Visual Inspection ID to value
        if intConnectorVisualInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intConnectorVisualInspectionID = intConnectorVisualInspectionID 

    def Append_ConnectorVisualIDList(self, intObject):
        """ 
        Function Name: Append_ConnectorVisualIDList
        Function Description: This function appends objects to the Connector Visual Inspection ID list
        """    
        self.aintConnectorVisualInspectionID.append(intObject)

    def Remove_ConnectorVisualIDList(self, intObject):
        """ 
        Function Name: Remove_ConnectorVisualIDList
        Function Description: This function removes objects in the Connector Visual Inspection ID list
        """    
        self.aintConnectorVisualInspectionID.remove(intObject)

    def Get_ConnectorVisualIDList_Obj(self):
        """ 
        Function Name: Get_ConnectorVisualIDList_Obj
        Function Description: This function gets all the objects in the Connector Visual Inspection ID list
        """    
        return self.aintConnectorVisualInspectionID
                
    def Delete_ConnectorVisualInspect_Data(self):
        """ 
        Function Name: Delete_ConnectorVisualInspect_Data
        Function Description: This function removes all the objects in the Connector Visual Inspection ID class
        """    
        ConnectorVisualInspect.aintConnectorVisualInspectionID = []
        ConnectorVisualInspect.aConnectorVisualCache = []

    def Set_ConnectorVisualInspect_Data(self):
        """ 
        Function Name: Set_ConnectorVisualInspect_Data
        Function Description: This function sets all the objects in the Connector Visual Inspection class
        """    
        self.intConnectorVisualInspectionID = ConnectorVisualInspect.aConnectorVisualCache[0]
        self.intConnectorID = ConnectorVisualInspect.aConnectorVisualCache[1]
        self.intInspectionTypeID = ConnectorVisualInspect.aConnectorVisualCache[2]
        self.intConnectorVisMetalSelectID = ConnectorVisualInspect.aConnectorVisualCache[3]
        self.intInspectionStatusID = ConnectorVisualInspect.aConnectorVisualCache[4]

    def Add_ConnectorVisualInspect_Query(self):
        """ 
        Function Name: Add_ConnectorVisualInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewConnectorVisualInspection
        """    
        # Set the class variables before dumping the data to the database
        ConnectorVisualInspect.Set_ConnectorVisualInspect_Data(self)
        
        # Create the sql query string       
        sqlTableCol = ("intConnectorVisualInspectionID", "intConnectorID", "intInspectionTypeID", "intConnectorVisMetalSelectID", "intInspectionStatusID")     
        sqlTableName = "TConnectorVisualInspections"
        sqlTableValues = (self.intConnectorVisualInspectionID, self.intConnectorID, self.intInspectionTypeID, self.intConnectorVisMetalSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Add_TwoConnectorVisualInspect_Query(self):
        """ 
        Function Name: Add_TwoConnectorVisualInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Set the class variables before dumping the data to the database
        for vi in ConnectorVisualInspect.aConnectorVisualCache:
            self.intConnectorVisualInspectionID = vi[0]
            self.intConnectorID = vi[1]
            self.intInspectionTypeID = vi[2]
            self.intConnectorVisMetalSelectID = vi[3]
            self.intInspectionStatusID = vi[4]
        
            # Create the sql query string       
            sqlTableCol = ("intConnectorVisualInspectionID", "intConnectorID", "intInspectionTypeID", "intConnectorVisMetalSelectID", "intInspectionStatusID")     
            sqlTableName = "TConnectorVisualInspections"
            sqlTableValues = (self.intConnectorVisualInspectionID, self.intConnectorID, self.intInspectionTypeID, self.intConnectorVisMetalSelectID, self.intInspectionStatusID)
            sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

            # Execute the stored procedure
            Queries.dbExeUSP_AddValues(Queries, sqlParams)
            
    def Clear_ConnectorVisInspect_Attributes(self):
        """ 
        Function Name: Clear_ConnectorVisInspect_Attributes
        Function Description: This function clears the Connector Visual Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intConnectorVisualInspectionID", "intConnectorID", "intInspectionTypeID", "intConnectorVisMetalSelectID", "intInspectionStatusID")     
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            

class ConnectorPhysSelection():
    """
    Class Name: ConnectorPhysSelection
    Class Description: This class gets and sets all of the Connector Physical Selections. 
    """
    # Create class variable shared amongst all Connector Physical methods
    aintConnectorPhysMetalSelectID = []
    astrConnectorPhysMetalSelect = []
    astrSecondConnectorPhysMetalSelect = []
    aTwoConnectorPhysSelectCache = []
        
    # Instantiate the following attributes
    def __init__(self, intConnectorPhysMetalSelectID, strConnectorPhysMetalSelect, strConnectorPhysStatus):
        self.intConnectorPhysMetalSelectID = intConnectorPhysMetalSelectID
        self.strConnectorPhysMetalSelect = strConnectorPhysMetalSelect
        self.strConnectorPhysStatus = strConnectorPhysStatus

    # Property decorator object get function to access private intConnectorPhysMetalSelectID
    @property
    def intConnectorPhysMetalSelectID(self):
        return self._intConnectorPhysMetalSelectID

    # Property decorator object get function to access private strConnectorPhysMetalSelect
    @property
    def strConnectorPhysMetalSelect(self):
        return self._strConnectorPhysMetalSelect
        
    # Property decorator object get function to access private strConnectorPhysStatus
    @property
    def strConnectorPhysStatus(self):
        return self._strConnectorPhysStatus
                
    # setter method 
    @intConnectorPhysMetalSelectID.setter 
    def intConnectorPhysMetalSelectID(self, intConnectorPhysMetalSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intConnectorPhysMetalSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intConnectorPhysMetalSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intConnectorPhysMetalSelectID = intConnectorPhysMetalSelectID 
        
    # setter method 
    @strConnectorPhysMetalSelect.setter 
    def strConnectorPhysMetalSelect(self, strConnectorPhysMetalSelect): 
        # Return true if specified object is of str type
        if not isinstance(strConnectorPhysMetalSelect, str): 
            raise TypeError('Connector physical input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strConnectorPhysMetalSelect.isspace(): 
            raise ValueError('Connector physical input cannot be empty') 
        # Set the attribute to the value if true
        elif strConnectorPhysMetalSelect.isascii():
            self._strConnectorPhysMetalSelect = strConnectorPhysMetalSelect

    # setter method 
    @strConnectorPhysStatus.setter 
    def strConnectorPhysStatus(self, strConnectorPhysStatus): 
        # Return true if specified object is of str type
        if not isinstance(strConnectorPhysStatus, str): 
            raise TypeError('Connector physical status must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strConnectorPhysStatus.isspace(): 
            raise ValueError('Connector physical status cannot be empty') 
        # Set the attribute to the value if true
        elif strConnectorPhysStatus.isascii():
            self._strConnectorPhysStatus = strConnectorPhysStatus

    def Append_ConnectorPhysIDList(self, intObject):
        """ 
        Function Name: Append_ConnectorPhysIDList
        Function Description: This function appends objects to the Connector Physical Selection ID list
        """    
        self.aintConnectorPhysMetalSelectID.append(intObject)

    def Remove_ConnectorPhysIDList(self, intObject):
        """ 
        Function Name: Remove_ConnectorPhysIDList
        Function Description: This function removes objects in the Connector Physical Selection ID list
        """    
        self.aintConnectorPhysMetalSelectID.remove(intObject)

    def Get_ConnectorPhysIDList_Obj(self):
        """ 
        Function Name: Get_ConnectorPhysIDList_Obj
        Function Description: This function gets all the objects in the Connector Visual Selection ID list
        """    
        return self.aintConnectorPhysMetalSelectID
    
    def Append_ConnectorPhysSelectList(self, strObject):
        """ 
        Function Name: Append_ConnectorPhysSelectList
        Function Description: This function appends objects to the Connector Visual Selection list
        """    
        self.astrConnectorPhysMetalSelect.append(strObject)

    def Remove_ConnectorPhysSelectList(self, strObject):
        """ 
        Function Name: Remove_ConnectorPhysSelectList
        Function Description: This function removes objects in the Connector Visual Selection list
        """    
        self.astrConnectorPhysMetalSelect.remove(strObject)

    def Get_ConnectorPhysSelectList_Obj(self):
        """ 
        Function Name: Get_ConnectorPhysSelectList_Obj
        Function Description: This function gets all the objects in the Connector Visual Selection list
        """    
        return self.astrConnectorPhysMetalSelect   

    def Append_Second_ConnectorPhysSelectList(self, strObject):
        """ 
        Function Name: Append_Second_ConnectorPhysSelectList
        Function Description: This function appends objects to the Second Connector Visual Selection list
        """    
        self.astrSecondConnectorPhysMetalSelect.append(strObject)

    def Remove_Second_ConnectorPhysSelectList(self, strObject):
        """ 
        Function Name: Remove_Second_ConnectorPhysSelectList
        Function Description: This function removes objects in the Second Connector Visual Selection list
        """    
        self.astrSecondConnectorPhysMetalSelect.remove(strObject)

    def Get_Second_ConnectorPhysSelectList_Obj(self):
        """ 
        Function Name: Get_Second_ConnectorPhysSelectList_Obj
        Function Description: This function gets all the objects in the Second Connector Visual Selection list
        """    
        return self.astrSecondConnectorPhysMetalSelect 

    def Append_Two_ConnectorPhysSelect_CacheList(self, strObject):
        """ 
        Function Name: Append_Two_ConnectorPhysSelect_CacheList
        Function Description: This function appends objects to the Two Connector Physical Selection list
        """    
        self.aTwoConnectorPhysSelectCache.append(strObject)

    def Remove_Two_ConnectorPhysSelect_CacheList(self, strObject):
        """ 
        Function Name: Remove_Two_ConnectorPhysSelect_CacheList
        Function Description: This function removes objects in the Two Connector Physical Selection list
        """    
        self.aTwoConnectorPhysSelectCache.remove(strObject)

    def Get_Two_ConnectorPhysSelect_CacheList_Obj(self):
        """ 
        Function Name: Get_Two_ConnectorPhysSelect_CacheList_Obj
        Function Description: This function gets all the objects in the Two Connector Physical Selection list
        """    
        return self.aTwoConnectorPhysSelectCache 
                            
    def Delete_ConnectorPhysSelectList_Data(self):
        """ 
        Function Name: Delete_ConnectorPhysSelectList_Data
        Function Description: This function removes all the objects in the Connector Visual Selection class
        """    
        ConnectorPhysSelection.aintConnectorPhysMetalSelectID = []
        ConnectorPhysSelection.astrConnectorPhysMetalSelect = []
        ConnectorPhysSelection.astrSecondConnectorPhysMetalSelect = []
        ConnectorPhysSelection.aTwoConnectorPhysSelectCache = []

    def Check_ConnectorPhysSelection_Dup(self):
        """ 
        Function Name: Check_ConnectorPhysSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        Connector physical selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intConnectorPhysMetalSelectID", "strConnectorPhysMetalSelect")   
        sqlTableName = "TConnectorPhysTextSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strConnectorPhysMetalSelect in sqlDupValues[i]:
                self.intConnectorPhysMetalSelectID = sqlDupValues[i][0]
                self.strConnectorPhysMetalSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag

    def Set_TwoConnectorPhysicalSelect_Data(self):
        """ 
        Function Name: Set_TwoConnectorPhysicalSelect_Data
        Function Description: This function sets all the objects in the Connector Physical Selection class
        """ 
        # Check if there is a duplicate, if so, only add one entry to the database
        if ConnectorPhysSelection.aTwoConnectorPhysSelectCache[0][0] != ConnectorPhysSelection.aTwoConnectorPhysSelectCache[1][0]:
            for p in ConnectorPhysSelection.aTwoConnectorPhysSelectCache:
                self.intConnectorPhysMetalSelectID = p[0]
                self.strConnectorPhysMetalSelect = p[1]
                self.strConnectorPhysStatus = p[2]
            
                # Execute the stored procedure
                ConnectorPhysSelection.Add_ConnectorPhysSelectList_Query(ConnectorPhysSelection)
        else:
            self.intConnectorPhysMetalSelectID = ConnectorPhysSelection.aTwoConnectorPhysSelectCache[0][0]
            self.strConnectorPhysMetalSelect = ConnectorPhysSelection.aTwoConnectorPhysSelectCache[0][1]
            self.strConnectorPhysStatus = ConnectorPhysSelection.aTwoConnectorPhysSelectCache[0][2]
            
            # Execute the stored procedure
            ConnectorPhysSelection.Add_ConnectorPhysSelectList_Query(ConnectorPhysSelection)
                            
    def Add_ConnectorPhysSelectList_Query(self):
        """ 
        Function Name: Add_ConnectorPhysSelectList_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewConnectorPhysSelection
        """    
        # Create the sql query params
        sqlTableCol = ("intConnectorPhysMetalSelectID", "strConnectorPhysMetalSelect")   
        sqlTableName = "TConnectorPhysMetalSelects"
        sqlTableValues = (ConnectorPhysSelection.intConnectorPhysMetalSelectID, ConnectorPhysSelection.strConnectorPhysMetalSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams) 
        
    def Clear_ConnectorPhysSel_Attributes(self):
        """ 
        Function Name: Clear_ConnectorPhysSel_Attributes
        Function Description: This function clears the Connector Physical Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intConnectorPhysMetalSelectID", "strConnectorPhysMetalSelect")   
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)

            
            
class ConnectorPhysicalInspect(Connectors, InspectionType, ConnectorPhysSelection, InspectionStatus):
    """
    Class Name: ConnectorPhysicalInspect
    Class Description: This class gets and sets all of the Connector Physical Inspection attributes. 
    """
    # Create class variable shared amongst all Connector Physical Inspection methods
    aintConnectorPhysicalInspectionID = []
    aConnectorPhysicalCache = []
        
    # Instantiate the following attributes
    def __init__(self, intConnectorPhysicalInspectionID, intConnectorID, intInspectionTypeID, intConnectorPhysMetalSelectID, intInspectionStatusID):
        self.intConnectorPhysicalInspectionID = intConnectorPhysicalInspectionID
        # Inherits the child class with all the necessary objects
        Connectors.__init__(intConnectorID)
        InspectionType.__init__(intInspectionTypeID)
        ConnectorPhysSelection.__init__(intConnectorPhysMetalSelectID)
        InspectionStatus.__init__(intInspectionStatusID)

    # property decorator object get function to access private intConnectorPhysicalInspectionID
    @property
    def intConnectorPhysicalInspectionID(self):
        return self._intConnectorPhysicalInspectionID

    # setter method 
    @intConnectorPhysicalInspectionID.setter 
    def intConnectorPhysicalInspectionID(self, intConnectorPhysicalInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intConnectorPhysicalInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Connector Physical Inspection ID to value
        if intConnectorPhysicalInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intConnectorPhysicalInspectionID = intConnectorPhysicalInspectionID 

    def Append_ConnectorPhysicalIDList(self, intObject):
        """ 
        Function Name: Append_ConnectorPhysicalIDList
        Function Description: This function appends objects to the Connector Physical Inspection ID list
        """    
        self.aintConnectorPhysicalInspectionID.append(intObject)

    def Remove_ConnectorPhysicalIDList(self, intObject):
        """ 
        Function Name: Remove_ConnectorPhysicalIDList
        Function Description: This function removes objects in the Connector Physical Inspection ID list
        """    
        self.aintConnectorPhysicalInspectionID.remove(intObject)

    def Get_ConnectorPhysicalIDList_Obj(self):
        """ 
        Function Name: Get_ConnectorPhysicalIDList_Obj
        Function Description: This function gets all the objects in the Connector Physical Inspection ID list
        """    
        return self.aintConnectorPhysicalInspectionID
                
    def Delete_ConnectorPhysicalInspect_Data(self):
        """ 
        Function Name: Delete_ConnectorPhysicalInspect_Data
        Function Description: This function removes all the objects in the Connector Physical Inspection ID class
        """    
        ConnectorPhysicalInspect.aintConnectorPhysicalInspectionID = []
        ConnectorPhysicalInspect.aConnectorPhysicalCache = []

    def Set_ConnectorPhysicalInspect_Data(self):
        """ 
        Function Name: Set_ConnectorPhysicalInspect_Data
        Function Description: This function sets all the objects in the Connector Physical Inspection class
        """    
        self.intConnectorPhysicalInspectionID = ConnectorPhysicalInspect.aConnectorPhysicalCache[0]
        self.intConnectorID = ConnectorPhysicalInspect.aConnectorPhysicalCache[1]
        self.intInspectionTypeID = ConnectorPhysicalInspect.aConnectorPhysicalCache[2]
        self.intConnectorPhysMetalSelectID = ConnectorPhysicalInspect.aConnectorPhysicalCache[3]
        self.intInspectionStatusID = ConnectorPhysicalInspect.aConnectorPhysicalCache[4]

    def Add_ConnectorPhysicalInspect_Query(self):
        """ 
        Function Name: Add_ConnectorPhysicalInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewConnectorVisualInspection
        """    
        # Set the class variables before dumping the data to the database
        ConnectorPhysicalInspect.Set_ConnectorPhysicalInspect_Data(self)
        
        # Create the sql query string       
        sqlTableCol = ("intConnectorPhysicalInspectionID", "intConnectorID", "intInspectionTypeID", "intConnectorPhysMetalSelectID", "intInspectionStatusID")     
        sqlTableName = "TConnectorPhysicalInspections"
        sqlTableValues = (self.intConnectorPhysicalInspectionID, self.intConnectorID, self.intInspectionTypeID, self.intConnectorPhysMetalSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Add_TwoConnectorPhysicalInspect_Query(self):
        """ 
        Function Name: Add_TwoConnectorPhysicalInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Set the class variables before dumping the data to the database
        for pi in ConnectorPhysicalInspect.aConnectorPhysicalCache:
            self.intConnectorPhysicalInspectionID = pi[0]
            self.intConnectorID = pi[1]
            self.intInspectionTypeID = pi[2]
            self.intConnectorPhysMetalSelectID = pi[3]
            self.intInspectionStatusID = pi[4]
            
            # Create the sql query string       
            sqlTableCol = ("intConnectorPhysicalInspectionID", "intConnectorID", "intInspectionTypeID", "intConnectorPhysMetalSelectID", "intInspectionStatusID")     
            sqlTableName = "TConnectorPhysicalInspections"
            sqlTableValues = (self.intConnectorPhysicalInspectionID, self.intConnectorID, self.intInspectionTypeID, self.intConnectorPhysMetalSelectID, self.intInspectionStatusID)
            sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

            # Execute the stored procedure
            Queries.dbExeUSP_AddValues(Queries, sqlParams)
        
    def Clear_ConnectorPhysInspect_Attributes(self):
        """ 
        Function Name: Clear_ConnectorPhysInspect_Attributes
        Function Description: This function clears the Connector Physical Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intConnectorPhysicalInspectionID", "intConnectorID", "intInspectionTypeID", "intConnectorPhysMetalSelectID", "intInspectionStatusID")     
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)


class ConnectorFunctSelection():
    """
    Class Name: ConnectorFunctSelection
    Class Description: This class gets and sets all of the Connector Function Selections. 
    """
    # Create class variable shared amongst all Connector Function methods
    aintConnectorFunctSelectID = []
    astrConnectorFunctSelect = []
    astrSecondConnectorFunctSelect = []
    aTwoConnectorFunctSelectCache = []
        
    # Instantiate the following attributes
    def __init__(self, intConnectorFunctSelectID, strConnectorFunctSelect, strConnectorFunctStatus):
        self.intConnectorFunctSelectID = intConnectorFunctSelectID
        self.strConnectorFunctSelect = strConnectorFunctSelect
        self.strConnectorFunctStatus = strConnectorFunctStatus

    # Property decorator object get function to access private intConnectorFunctSelectID
    @property
    def intConnectorFunctSelectID(self):
        return self._intConnectorFunctSelectID

    # Property decorator object get function to access private strConnectorFunctSelect
    @property
    def strConnectorFunctSelect(self):
        return self._strConnectorFunctSelect

    # Property decorator object get function to access private strConnectorFunctStatus
    @property
    def strConnectorFunctStatus(self):
        return self._strConnectorFunctStatus

    # setter method 
    @intConnectorFunctSelectID.setter 
    def intConnectorFunctSelectID(self, intConnectorFunctSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intConnectorFunctSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intConnectorFunctSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intConnectorFunctSelectID = intConnectorFunctSelectID 
        
    # setter method 
    @strConnectorFunctSelect.setter 
    def strConnectorFunctSelect(self, strConnectorFunctSelect): 
        # Return true if specified object is of str type
        if not isinstance(strConnectorFunctSelect, str): 
            raise TypeError('Connector function input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strConnectorFunctSelect.isspace(): 
            raise ValueError('Connector function input cannot be empty') 
        # Set the attribute to the value if true
        elif strConnectorFunctSelect.isascii():
            self._strConnectorFunctSelect = strConnectorFunctSelect

    # setter method 
    @strConnectorFunctStatus.setter 
    def strConnectorFunctStatus(self, strConnectorFunctStatus): 
        # Return true if specified object is of str type
        if not isinstance(strConnectorFunctStatus, str): 
            raise TypeError('Connector function status input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strConnectorFunctStatus.isspace(): 
            raise ValueError('Connector function status input cannot be empty') 
        # Set the attribute to the value if true
        elif strConnectorFunctStatus.isascii():
            self._strConnectorFunctStatus = strConnectorFunctStatus

    def Append_ConnectorFunctIDList(self, intObject):
        """ 
        Function Name: Append_ConnectorFunctIDList
        Function Description: This function appends objects to the Connector Function Selection ID list
        """    
        self.aintConnectorFunctSelectID.append(intObject)

    def Remove_ConnectorFunctIDList(self, intObject):
        """ 
        Function Name: Remove_ConnectorFunctIDList
        Function Description: This function removes objects in the Connector Function Selection ID list
        """    
        self.aintConnectorFunctSelectID.remove(intObject)

    def Get_ConnectorFunctIDList_Obj(self):
        """ 
        Function Name: Get_ConnectorFunctIDList_Obj
        Function Description: This function gets all the objects in the Connector Function Selection ID list
        """    
        return self.aintConnectorFunctSelectID
    
    def Append_ConnectorFunctSelectList(self, strObject):
        """ 
        Function Name: Append_ConnectorFunctSelectList
        Function Description: This function appends objects to the Connector Function Selection list
        """    
        self.astrConnectorFunctSelect.append(strObject)

    def Remove_ConnectorFunctSelectList(self, strObject):
        """ 
        Function Name: Remove_ConnectorFunctSelectList
        Function Description: This function removes objects in the Connector Function Selection list
        """    
        self.astrConnectorFunctSelect.remove(strObject)

    def Get_ConnectorFunctSelectList_Obj(self):
        """ 
        Function Name: Get_ConnectorFunctSelectList_Obj
        Function Description: This function gets all the objects in the Connector Function Selection list
        """    
        return self.astrConnectorFunctSelect   

    def Append_Second_ConnectorFunctSelectList(self, strObject):
        """ 
        Function Name: Append_Second_ConnectorFunctSelectList
        Function Description: This function appends objects to the Second Connector Function Selection list
        """    
        self.astrSecondConnectorFunctSelect.append(strObject)

    def Remove_Second_ConnectorFunctSelectList(self, strObject):
        """ 
        Function Name: Remove_Second_ConnectorFunctSelectList
        Function Description: This function removes objects in the Second Connector Function Selection list
        """    
        self.astrSecondConnectorFunctSelect.remove(strObject)

    def Get_Second_ConnectorFunctSelectList_Obj(self):
        """ 
        Function Name: Get_Second_ConnectorFunctSelectList_Obj
        Function Description: This function gets all the objects in the Second Connector Function Selection list
        """    
        return self.astrSecondConnectorFunctSelect       

    def Append_Two_ConnectorFunctSelect_CacheList(self, strObject):
        """ 
        Function Name: Append_Two_ConnectorFunctSelect_CacheList
        Function Description: This function appends objects to the Two Connector Functional Selection list
        """    
        self.aTwoConnectorFunctSelectCache.append(strObject)

    def Remove_Two_ConnectorFunctSelect_CacheList(self, strObject):
        """ 
        Function Name: Remove_Two_ConnectorFunctSelect_CacheList
        Function Description: This function removes objects in the Two Connector Functional Selection list
        """    
        self.aTwoConnectorFunctSelectCache.remove(strObject)

    def Get_Two_ConnectorFunctSelect_CacheList_Obj(self):
        """ 
        Function Name: Get_Two_ConnectorFunctSelect_CacheList_Obj
        Function Description: This function gets all the objects in the Two Connector Functional Selection list
        """    
        return self.aTwoConnectorFunctSelectCache
                        
    def Delete_ConnectorFunctSelection_Data(self):
        """ 
        Function Name: Delete_ConnectorFunctSelection_Data
        Function Description: This function removes all the objects in the Connector Function Selection class
        """    
        ConnectorFunctSelection.aintConnectorFunctSelectID = []
        ConnectorFunctSelection.astrConnectorFunctSelect = []
        ConnectorFunctSelection.astrSecondConnectorFunctSelect = []
        ConnectorFunctSelection.aTwoConnectorFunctSelectCache = []

    def Check_ConnectorFunctSelection_Dup(self):
        """ 
        Function Name: Check_ConnectorFunctSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        Connector function selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intConnectorFunctSelectID", "strConnectorFunctSelect")   
        sqlTableName = "TConnectorFunctSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strConnectorFunctSelect in sqlDupValues[i]:
                self.intConnectorFunctSelectID = sqlDupValues[i][0]
                self.strConnectorFunctSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag

    def Set_TwoConnectorFunctionalSelect_Data(self):
        """ 
        Function Name: Set_TwoConnectorFunctionalSelect_Data
        Function Description: This function sets all the objects in the Connector Functional Selection class
        """ 
        # Check if there is a duplicate, if so, only add one entry to the database
        if ConnectorFunctSelection.aTwoConnectorFunctSelectCache[0][0] != ConnectorFunctSelection.aTwoConnectorFunctSelectCache[1][0]:
            for f in ConnectorFunctSelection.aTwoConnectorFunctSelectCache:
                self.intConnectorFunctSelectID = f[0]
                self.strConnectorFunctSelect = f[1]
                self.strConnectorFunctStatus = f[2]
            
                # Execute the stored procedure
                ConnectorFunctSelection.Add_ConnectorFunctSelection_Query(ConnectorFunctSelection)
        else:
            self.intConnectorFunctSelectID = ConnectorFunctSelection.aTwoConnectorFunctSelectCache[0][0]
            self.strConnectorFunctSelect = ConnectorFunctSelection.aTwoConnectorFunctSelectCache[0][1]
            self.strConnectorFunctStatus = ConnectorFunctSelection.aTwoConnectorFunctSelectCache[0][2]
            
            # Execute the stored procedure
            ConnectorFunctSelection.Add_ConnectorFunctSelection_Query(ConnectorFunctSelection)
                        
    def Add_ConnectorFunctSelection_Query(self):
        """ 
        Function Name: Add_ConnectorFunctSelection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewConnectorFunctSelection
        """    
        # Create the sql query string
        sqlTableCol = ("intConnectorFunctSelectID", "strConnectorFunctSelect")   
        sqlTableName = "TConnectorFunctSelects"
        sqlTableValues = (ConnectorFunctSelection.intConnectorFunctSelectID, ConnectorFunctSelection.strConnectorFunctSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)                            

    def Clear_ConnectorFuncSel_Attributes(self):
        """ 
        Function Name: Clear_ConnectorFuncSel_Attributes
        Function Description: This function clears the Connector Function Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intConnectorFunctSelectID", "strConnectorFunctSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None) 
                    
                
class ConnectorFunctionInspect(Connectors, InspectionType, ConnectorFunctSelection, InspectionStatus):
    """
    Class Name: ConnectorFunctionInspect
    Class Description: This class gets and sets all of the Connector Function Inspection  attributes. 
    """
    # Create class variable shared amongst all Connector Function Inspection methods
    aintConnectorFunctionInspectID = []
    aConnectorFunctCache = []
        
    # Instantiate the following attributes
    def __init__(self, intConnectorFunctionInspectID, intConnectorID, intInspectionTypeID, intConnectorFunctSelectID, intInspectionStatusID):
        self.intConnectorFunctionInspectID = intConnectorFunctionInspectID
        # Inherits the child class with all the necessary objects
        Connectors.__init__(intConnectorID)
        InspectionType.__init__(intInspectionTypeID)
        ConnectorFunctSelection.__init__(intConnectorFunctSelectID)
        InspectionStatus.__init__(intInspectionStatusID)

    # Property decorator object get function to access private intConnectorFunctionInspectID
    @property
    def intConnectorFunctionInspectID(self):
        return self._intConnectorFunctionInspectID

    # setter method 
    @intConnectorFunctionInspectID.setter 
    def intConnectorFunctionInspectID(self, intConnectorFunctionInspectID): 
        # Return true if specified object is of int type
        if not isinstance(intConnectorFunctionInspectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the Connector Function Inspection ID to value
        if intConnectorFunctionInspectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intConnectorFunctionInspectID = intConnectorFunctionInspectID 

    def Append_ConnectorFunctIDList(self, intObject):
        """ 
        Function Name: Append_ConnectorFunctIDList
        Function Description: This function appends objects to the Connector Function Inspection ID list
        """    
        self.aintConnectorFunctionInspectID.append(intObject)

    def Remove_ConnectorFunctIDList(self, intObject):
        """ 
        Function Name: Remove_ConnectorFunctIDList
        Function Description: This function removes objects in the Connector Function Inspection ID list
        """    
        self.aintConnectorFunctionInspectID.remove(intObject)

    def Get_ConnectorFunctIDList_Obj(self):
        """ 
        Function Name: Get_ConnectorFunctIDList_Obj
        Function Description: This function gets all the objects in the Connector Function Inspection ID list
        """    
        return self.aintConnectorFunctionInspectID
                
    def Delete_ConnectorFunctInspect_Data(self):
        """ 
        Function Name: Delete_ConnectorFunctInspect_Data
        Function Description: This function removes all the objects in the Connector Function Inspection ID class
        """    
        ConnectorFunctionInspect.aintConnectorFunctionInspectID = []
        ConnectorFunctionInspect.aConnectorFunctCache = []

    def Set_ConnectorFunctInspect_Data(self):
        """ 
        Function Name: Set_ConnectorFunctInspect_Data
        Function Description: This function sets all the objects in the Connector Function Inspection class
        """    
        self.intConnectorFunctionInspectID = ConnectorFunctionInspect.aConnectorFunctCache[0]
        self.intConnectorID = ConnectorFunctionInspect.aConnectorFunctCache[1]
        self.intInspectionTypeID = ConnectorFunctionInspect.aConnectorFunctCache[2]
        self.intConnectorFunctSelectID = ConnectorFunctionInspect.aConnectorFunctCache[3]
        self.intInspectionStatusID = ConnectorFunctionInspect.aConnectorFunctCache[4]
                
    def Add_ConnectorFunctInspect_Query(self):
        """ 
        Function Name: Add_ConnectorFunctInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewConnectorFunctionInspection
        """    
        # Set the class variables before dumping the data to the database
        ConnectorFunctionInspect.Set_ConnectorFunctInspect_Data(self)
                
        # Create the sql query string
        sqlTableCol = ("intConnectorFunctionInspectID", "intConnectorID", "intInspectionTypeID", "intConnectorFunctSelectID", "intInspectionStatusID")     
        sqlTableName = "TConnectorFunctionInspections"
        sqlTableValues = (self.intConnectorFunctionInspectID, self.intConnectorID, self.intInspectionTypeID, self.intConnectorFunctSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)           

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Add_TwoConnectorFunctInspect_Query(self):
        """ 
        Function Name: Add_TwoConnectorFunctInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Set the class variables before dumping the data to the database
        for fi in ConnectorFunctionInspect.aConnectorFunctCache:
            self.intConnectorFunctionInspectID = fi[0]
            self.intConnectorID = fi[1]
            self.intInspectionTypeID = fi[2]
            self.intConnectorFunctSelectID = fi[3]
            self.intInspectionStatusID = fi[4]
                
            # Create the sql query string
            sqlTableCol = ("intConnectorFunctionInspectID", "intConnectorID", "intInspectionTypeID", "intConnectorFunctSelectID", "intInspectionStatusID")     
            sqlTableName = "TConnectorFunctionInspections"
            sqlTableValues = (self.intConnectorFunctionInspectID, self.intConnectorID, self.intInspectionTypeID, self.intConnectorFunctSelectID, self.intInspectionStatusID)
            sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)           

            # Execute the stored procedure
            Queries.dbExeUSP_AddValues(Queries, sqlParams)        

    def Clear_ConnectorFuncInspect_Attributes(self):
        """ 
        Function Name: Clear_ConnectorFuncInspect_Attributes
        Function Description: This function clears the Connector Function Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intConnectorFunctionInspectID", "intConnectorID", "intInspectionTypeID", "intConnectorFunctSelectID", "intInspectionStatusID")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)        
                
                                
class StandardConnectorInspect(ConnectorVisualInspect, ConnectorPhysicalInspect, ConnectorFunctionInspect):
    """
    Class Name: StandardConnectorInspect
    Class Description: This class gets and sets all of the Standard Connector Inspection attributes. 
    Pass in the Connector Visual and Physical classes. 
    """
    # Create class variable shared amongst all Standard Connector Inspection methods
    aintStandardConnectorInspectionID = []
    aStandardConnectorInsCache = []
        
    # Instantiate the following attributes
    def __init__(self, intStandardConnectorInspectionID, intConnectorVisualInspectionID, intConnectorPhysicalInspectionID, intConnectorFunctionInspectID):
        self.intStandardConnectorInspectionID = intStandardConnectorInspectionID
        # Inherits the child class with all the necessary objects
        ConnectorVisualInspect.__init__(intConnectorVisualInspectionID)
        ConnectorPhysicalInspect.__init__(intConnectorPhysicalInspectionID)
        ConnectorFunctionInspect.__init__(intConnectorFunctionInspectID)
        
    # Property decorator object get function to access private intStandardConnectorInspectionID
    @property
    def intStandardConnectorInspectionID(self):
        return self._intStandardConnectorInspectionID
    
    # setter method 
    @intStandardConnectorInspectionID.setter 
    def intStandardConnectorInspectionID(self, intStandardConnectorInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intStandardConnectorInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intStandardConnectorInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intStandardConnectorInspectionID = intStandardConnectorInspectionID    

    def Append_StandConnectorInspectIDList(self, intObject):
        """ 
        Function Name: Append_StandConnectorInspectIDList
        Function Description: This function appends objects to the Standard Connector Inspection ID list
        """    
        self.aintStandardConnectorInspectionID.append(intObject)

    def Remove_StandConnectorInspectIDList(self, intObject):
        """ 
        Function Name: Remove_StandConnectorInspectIDList
        Function Description: This function removes objects in the Standard Connector Inspection ID list
        """    
        self.aintStandardConnectorInspectionID.remove(intObject)

    def Get_StandConnectorInspectIDList_Obj(self):
        """ 
        Function Name: Get_StandConnectorInspectIDList_Obj
        Function Description: This function gets all the objects in the Standard Connector Inspection ID list
        """    
        return self.aintStandardConnectorInspectionID     

    def Add_StandConnectorInspect_Query(self):
        """ 
        Function Name: Add_StandConnectorInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewStandardConnectorInspection
        """    
        # Create the sql query string
        sqlTableNames = ("TStandardConnectorInspections")
        sqlTableCol = ("intStandardConnectorInspectionID", "intConnectorVisualInspectionID", "intConnectorPhysicalInspectionID", 
                        "intConnectorFunctionInspectID", "intInspectionStatusID") 
        # Set the primary key values from the cached array object
        aPrimKeyValues = [item for item in StandardConnectorInspect.aStandardConnectorInsCache]        

        # Get the visual, physical status IDs
        VisStatusID = InspectionStatus.astrInspectionStatusDesc.index(ConnectorVisSelection.strConnectorVisStatus) + 1
        PhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(ConnectorPhysSelection.strConnectorPhysStatus) + 1
        FunctStatusID = InspectionStatus.astrInspectionStatusDesc.index(ConnectorFunctSelection.strConnectorFunctStatus) + 1
        aInsStatusID = [VisStatusID, PhysStatusID, FunctStatusID]

        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(aInsStatusID)

        # Append the Connector Status array 
        ConnectorInspect.aConnectorInspectStatus.append(intOverallStatus)
                    
        # Append the primary key list with the new over status ID
        aPrimKeyValues.append(intOverallStatus)                      
        
        # Set the parameters
        sqlParams = (sqlTableNames, sqlTableCol, tuple(aPrimKeyValues))

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)        

    def Add_TwoStandConnectorInspect_Query(self):
        """ 
        Function Name: Add_TwoStandConnectorInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Create the sql query string
        sqlTableNames = ("TStandardConnectorInspections")
        sqlTableCol = ("intStandardConnectorInspectionID", "intConnectorVisualInspectionID", "intConnectorPhysicalInspectionID", 
                        "intConnectorFunctionInspectID", "intInspectionStatusID") 
        
        # Set the primary key values from the cached array object
        for i, item in enumerate(StandardConnectorInspect.aStandardConnectorInsCache):
            self.intStandardConnectorInspectionID = item[0]
            self.intConnectorVisualInspectionID = item[1]
            self.intConnectorPhysicalInspectionID = item[2]
            self.intConnectorFunctionInspectID = item[3]
            
            aPrimKeyValues = [self.intStandardConnectorInspectionID, self.intConnectorVisualInspectionID, 
                            self.intConnectorPhysicalInspectionID, self.intConnectorFunctionInspectID]        

            # Get the visual, physical status IDs
            VisStatusID = InspectionStatus.astrInspectionStatusDesc.index(ConnectorVisSelection.aTwoConnectorVisSelectCache[i][2]) + 1
            PhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(ConnectorPhysSelection.aTwoConnectorPhysSelectCache[i][2]) + 1
            FunctStatusID = InspectionStatus.astrInspectionStatusDesc.index(ConnectorFunctSelection.aTwoConnectorFunctSelectCache[i][2]) + 1
            aInsStatusID = [VisStatusID, PhysStatusID, FunctStatusID]

            # Determine the overall status
            intOverallStatus = BaseFunctions.Check_Overall_Status(aInsStatusID)

            # Append the Connector Status array 
            ConnectorInspect.aConnectorInspectStatus.append(intOverallStatus)
                        
            # Append the primary key list with the new over status ID
            aPrimKeyValues.append(intOverallStatus)                      
            
            # Set the parameters
            sqlParams = (sqlTableNames, sqlTableCol, tuple(aPrimKeyValues))

            # Execute the stored procedure
            Queries.dbExeUSP_AddValues(Queries, sqlParams) 
        
    def Delete_StandConnectorInspect_Data(self):
        """ 
        Function Name: Delete_StandCarabInspect_Data
        Function Description: This function removes all the objects in the Standard Carabiner Inspection class
        """    
        StandardConnectorInspect.aStandardConnectorInsCache = []                
        StandardConnectorInspect.aintStandardConnectorInspectionID = []

    def Clear_ConnectorStandardInspect_Attributes(self):
        """ 
        Function Name: Clear_ConnectorStandardInspect_Attributes
        Function Description: This function clears the Connector Standard Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intStandardConnectorInspectionID", "intConnectorVisualInspectionID", "intConnectorPhysicalInspectionID", 
                    "intConnectorFunctionInspectID", "intInspectionStatusID") 
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None) 

    def Reset_Connector_Data(self):
        """ 
        Function Name: Reset_Connector_Data
        Function Description: This function clears the Connector data attributes 
        """  
        # Clear the class attributes
        ConnectorVisSelection.Clear_ConnectorVisSel_Attributes(self)
        ConnectorPhysSelection.Clear_ConnectorPhysSel_Attributes(self)
        ConnectorFunctSelection.Clear_ConnectorFuncSel_Attributes(self)
        ConnectorVisualInspect.Clear_ConnectorVisInspect_Attributes(self)
        ConnectorPhysicalInspect.Clear_ConnectorPhysInspect_Attributes(self)
        ConnectorFunctionInspect.Clear_ConnectorFuncInspect_Attributes(self)
        StandardConnectorInspect.Clear_ConnectorStandardInspect_Attributes(self)
                                    
    def Delete_Connector_Data(self):
        """ 
        Function Name: Delete_Connector_Data
        Function Description: This function clears the Connector data arrays 
        """  
        # Clear the class arrays
        ConnectorVisSelection.Delete_ConnectorVisSelectList_Data(self)
        ConnectorPhysSelection.Delete_ConnectorPhysSelectList_Data(self)
        ConnectorFunctSelection.Delete_ConnectorFunctSelection_Data(self)
        ConnectorVisualInspect.Delete_ConnectorVisualInspect_Data(self)
        ConnectorPhysicalInspect.Delete_ConnectorPhysicalInspect_Data(self)
        ConnectorFunctionInspect.Delete_ConnectorFunctInspect_Data(self)
        StandardConnectorInspect.Delete_StandConnectorInspect_Data(self) 
                                

class ConnectorInspect(WallLocation, StandardConnectorInspect, Inspector):
    """
    Class Name: ConnectorInspect
    Class Description: This class gets and sets all of the Connector Inspection attributes. 
    """
    # Create class variable shared amongst all Connector Inspection methods
    aintConnectorInspectionID = []
    aConnectorInspectStatus = []
        
    # Instantiate the following attributes
    def __init__(self, intConnectorInspectionID, intWallLocationID, intStandardConnectorInspectionID, 
                intInspectorID, strComment):
        self.intConnectorInspectionID = intConnectorInspectionID
        self.strComment = strComment
        # Inherits the child class with all the necessary objects
        WallLocation().__init__(intWallLocationID)
        StandardConnectorInspect().__init__(intStandardConnectorInspectionID)
        Inspector().__init__(intInspectorID)

    # Property decorator object get function to access private intConnectorInspectionID
    @property
    def intConnectorInspectionID(self):
        return self._intConnectorInspectionID

    # Property decorator object get function to access private strComment
    @property
    def strComment(self):
        return self._strComment
            
    # setter method 
    @intConnectorInspectionID.setter 
    def intConnectorInspectionID(self, intConnectorInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intConnectorInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intConnectorInspectionID < 0: 
            raise ValueError('ID cannot be negative') 
        self._intConnectorInspectionID = intConnectorInspectionID    

    # setter method 
    @strComment.setter 
    def strComment(self, strComment): 
        # Return true if specified object is of str type
        if not isinstance(strComment, str): 
            raise TypeError('Comment must be a string') 
        # Set the attribute to the value if true
        elif strComment.isascii():
            self._strComment = strComment   

    def Append_ConnectorInspectIDList(self, intObject):
        """ 
        Function Name: Append_ConnectorInspectIDList
        Function Description: This function appends objects to the Connector Inspection ID list
        """    
        self.aintConnectorInspectionID.append(intObject)

    def Remove_ConnectorInspectIDList(self, intObject):
        """ 
        Function Name: Remove_ConnectorInspectIDList
        Function Description: This function removes objects in the Connector Inspection ID list
        """    
        self.aintConnectorInspectionID.remove(intObject)

    def Get_ConnectorInspectIDList_Obj(self):
        """ 
        Function Name: Get_ConnectorInspectIDList_Obj
        Function Description: This function gets all the objects in the Connector Inspection ID list
        """    
        return self.aintConnectorInspectionID   

    def Join_ConnectorInspectComm_Obj(self, strObject):
        """ 
        Function Name: Join_ConnectorInspectComm_Obj
        Function Description: This function joins the string objects in the Connector Inspection comment
        """    
        self.strComment = self.strComment + " " + strObject

    def Get_MaxStandardConnectorInspectID(self, table_name, id_column_name):
        """
        Function Name: Get_MaxStandardConnectorInspectID
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)

    def Delete_ConnectorInspect_Data(self):
        """ 
        Function Name: Delete_ConnectorInspect_Data
        Function Description: This function removes all the objects in the Connector Inspect class
        """    
        ConnectorInspect.aintConnectorInspectionID = []
        ConnectorInspect.aConnectorInspectStatus = []
                            
    def Add_ConnectorInspection_Query(self):
        """ 
        Function Name: Add_ConnectorInspection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewConnectorInspection
        """
        # Create the sql query string
        sqlTableCol = ("intConnectorInspectionID", "intConnectorID", "intWallLocationID", "intStandardConnectorInspectionID", 
                "intInspectorID", "intInspectionStatusID", "dtmLastInspectionDate", "dtmNextInspectionDate", 
                "strComment")
        sqlTableName = "TConnectorInspections"
        
        # Get the max primary key value for the table
        sqlMaxPrimKeyID = ConnectorInspect.Get_MaxStandardConnectorInspectID(self, sqlTableName, sqlTableCol[0])
        self.intConnectorInspectionID = sqlMaxPrimKeyID

        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(ConnectorInspect.aConnectorInspectStatus)

        # For testing purposes, set the inspector ID to 1
        Inspector.intInspectorID = 1
                    
        # Set the inspector ID
        # print(UserLogins.aCurrentUserLogin)
        # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID
        
        # Perform the insert query
        sqlTableValues = (self.intConnectorInspectionID, Connectors.intConnectorID, WallLocation.intWallLocationID, StandardConnectorInspect.aStandardConnectorInsCache[0], 
                        Inspector.intInspectorID, intOverallStatus, Connectors.dtmLastInspectionDate, Connectors.dtmNextInspectionDate, ConnectorInspect.strComment)
                        
        # Set the parameters
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Add_TwoConnectorInspection_Query(self):
        """ 
        Function Name: Add_TwoConnectorInspection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure for two connectors.
        """
        # Create the sql query string
        sqlTableCol = ("intConnectorInspectionID", "intConnectorID", "intWallLocationID", "intStandardConnectorInspectionID", 
                "intInspectorID", "intInspectionStatusID", "dtmLastInspectionDate", "dtmNextInspectionDate", 
                "strComment")
        sqlTableName = "TConnectorInspections"

        # Get the two connectors data
        aTwoConnectorList = Connectors.Get_TwoConnector_StageList_Obj(Connectors)
        
        for i, item in enumerate(aTwoConnectorList):    
            connectorID = item[0]
                    
            # Get the max primary key value for the table
            sqlMaxPrimKeyID = ConnectorInspect.Get_MaxStandardConnectorInspectID(self, sqlTableName, sqlTableCol[0])
            self.intConnectorInspectionID = sqlMaxPrimKeyID

            # Determine the overall status
            intOverallStatus = BaseFunctions.Check_Overall_Status(ConnectorInspect.aConnectorInspectStatus)

            # For testing purposes, set the inspector ID to 1
            Inspector.intInspectorID = 1
                        
            # Set the inspector ID
            # print(UserLogins.aCurrentUserLogin)
            # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID
            
            # Perform the insert query
            sqlTableValues = (self.intConnectorInspectionID, connectorID, WallLocation.intWallLocationID, StandardConnectorInspect.aStandardConnectorInsCache[i][0], 
                            Inspector.intInspectorID, intOverallStatus, Connectors.dtmLastInspectionDate, Connectors.dtmNextInspectionDate, ConnectorInspect.strComment)
                            
            # Set the parameters
            sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

            # Execute the stored procedure
            Queries.dbExeUSP_AddValues(Queries, sqlParams)
                
    def Add_ConnectorInspector_Query(self):
        """ 
        Function Name: Add_ConnectorInspector_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewConnectorInspector
        """    
        # Create the sql query string
        sqlTableCol = ("intConnectorInspectorID", "intInspectorID", "intConnectorID")
        sqlTableName = "TConnectorInspectors"
        
        # Get the max primary key value for the table
        sqlMaxPrimKeyID = ConnectorInspect.Get_MaxStandardConnectorInspectID(self, sqlTableName, sqlTableCol[0])

        # For testing purposes, set the inspector ID to 1
        Inspector.intInspectorID = 1
                    
        # Set the inspector ID
        # print(UserLogins.aCurrentUserLogin)
        # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID
        
        # Perform the insert query
        sqlTableValues = (sqlMaxPrimKeyID, Inspector.intInspectorID, Connectors.intConnectorID)
                
        # Set the parameters
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)          

    def Add_TwoConnectorInspector_Query(self):
        """ 
        Function Name: Add_TwoConnectorInspector_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure for two connectors.
        """    
        # Create the sql query string
        sqlTableCol = ("intConnectorInspectorID", "intInspectorID", "intConnectorID")
        sqlTableName = "TConnectorInspectors"
        

        # Get the two connectors data
        aTwoConnectorList = Connectors.Get_TwoConnector_StageList_Obj(Connectors)
        
        for i in aTwoConnectorList:    
            connectorID = i[0]
                        
            # Get the max primary key value for the table
            sqlMaxPrimKeyID = ConnectorInspect.Get_MaxStandardConnectorInspectID(self, sqlTableName, sqlTableCol[0])

            # For testing purposes, set the inspector ID to 1
            Inspector.intInspectorID = 1
                        
            # Set the inspector ID
            # print(UserLogins.aCurrentUserLogin)
            # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID
            
            # Perform the insert query
            sqlTableValues = (sqlMaxPrimKeyID, Inspector.intInspectorID, connectorID)
                    
            # Set the parameters
            sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

            # Execute the stored procedure
            Queries.dbExeUSP_AddValues(Queries, sqlParams)   
                
    def Add_ConnectorLocation_Query(self):
        """ 
        Function Name: Add_ConnectorLocation_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewConnectorWallLocation
        """    
        # Declare Local Variables
        blnFlag = False
        
        # Create the sql query string
        sqlTableAttr = ("TConnectorWallLocations", "intConnectorWallLocationID", "intWallLocationID", "intConnectorID")
        
        try:
            # Get the max primary key value for the table
            idList = (WallLocation.intWallLocationID, Connectors.intConnectorID)
            sqlMaxPrimKeyID = ConnectorInspect.Get_Or_Create_ID(ConnectorInspect, idList, sqlTableAttr)

            # For testing purposes, set the inspector ID to 1
            Inspector.intInspectorID = 1
                        
            # Set the inspector ID
            # print(UserLogins.aCurrentUserLogin)
            # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID

            # Get the values
            sqlTableValues = (sqlMaxPrimKeyID, idList[0], idList[1])
                    
            # Set the parameters
            sqlParams = (sqlTableAttr[0], sqlTableAttr[1:], sqlTableValues)
            
            # Get the id list from TConnectorWallLocations
            aidReturnList = Queries.Get_All_DB_Values(Queries, sqlTableAttr[0])
            
            # Check if the max ID is in the aidReturnList object
            if aidReturnList:
                for i in aidReturnList:
                    # Extract the IDs from the current entry for clarity
                    current_ids = i[1:3]

                    # Check if the current entry's IDs match the idList
                    if idList == current_ids:
                        # If the device is in use and IDs match, set flag to true to skip adding/updating
                        if Connectors.strEquipInUse == 'Yes':
                            blnFlag = True
                        # If the device is not in use, remove the entry from the database
                        else:
                            Queries.Remove_Attribute_Query(Queries, sqlTableAttr[0], sqlTableAttr[1], i[0])
                    elif idList[1] == current_ids[1]:
                        # If the connector ID matches the current entry's connector ID, remove the entry from the database
                        Queries.Remove_Attribute_Query(Queries, sqlTableAttr[0], sqlTableAttr[1], i[0])

            # Add or update the database if needed
            if not blnFlag and Connectors.strEquipInUse == 'Yes':
                Queries.dbExeUSP_AddValues(Queries, sqlParams)
                    
        except Exception as e:
            print(f"Error in Add_ConnectorLocation_Query: {e}")

    def Add_TwoConnectorLocation_Query(self):
        """ 
        Function Name: Add_ConnectorLocation_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewConnectorWallLocation
        """    
        # Declare Local Variables
        blnFlag = False
        
        # Create the sql query string
        sqlTableAttr = ("TConnectorWallLocations", "intConnectorWallLocationID", "intWallLocationID", "intConnectorID")
        
        # Get the two connectors data
        aTwoConnectorList = Connectors.Get_TwoConnector_StageList_Obj(Connectors)
        
        for i in aTwoConnectorList:    
            connectorID = i[0]
            equipmentInUse = i[9]
                    
            # Get the max primary key value for the table
            idList = (WallLocation.intWallLocationID, connectorID)
            sqlMaxPrimKeyID = ConnectorInspect.Get_Or_Create_ID(ConnectorInspect, idList, sqlTableAttr)

            # For testing purposes, set the inspector ID to 1
            Inspector.intInspectorID = 1
                        
            # Set the inspector ID
            # print(UserLogins.aCurrentUserLogin)
            # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID

            # Get the values
            sqlTableValues = (sqlMaxPrimKeyID, idList[0], idList[1])
                    
            # Set the parameters
            sqlParams = (sqlTableAttr[0], sqlTableAttr[1:], sqlTableValues)
            
            # Get the id list from TConnectorWallLocations
            aidReturnList = Queries.Get_All_DB_Values(Queries, sqlTableAttr[0])
            
            # Check if the max ID is in the aidReturnList object
            if aidReturnList:
                for i in aidReturnList:
                    # Compare current IDs with the item's IDs
                    if idList == i[1:3]:
                        if equipmentInUse == 'Yes':
                            # If device is in use and IDs match, no need to update.
                            blnFlag = True
                        else:
                            # If device is not in use, remove the item.
                            Queries.Remove_Attribute_Query(Queries, sqlTableAttr[0], sqlTableAttr[1], i[0])

            # Add or update the database if needed
            if blnFlag == False and equipmentInUse == 'Yes':
                Queries.dbExeUSP_AddValues(Queries, sqlParams)            

    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = ConnectorInspect.Check_Duplicate(ConnectorInspect, item_list, sql_tuple)
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


class ConnectorsRetiredReport(ConnectorInspect):
    """
    Class Name: ConnectorsRetiredReport
    Class Description: This class gets and sets all of the Connector Retired Report attributes. 
    """
    # Create class variable shared amongst all Connector Retired methods
    aintConnectorsRetiredReportID = []

    # Instantiate the following attributes
    def __init__(self, intConnectorsRetiredReportID, intConnectorInspectionID, intInspectorID, dtmReportDate):
        self.intConnectorsRetiredReportID = intConnectorsRetiredReportID
        self.dtmReportDate = dtmReportDate
        # Inherits the child class with all the necessary objects
        ConnectorInspect().__init__(intConnectorInspectionID)
        Inspector().__init__(intInspectorID)

    # Property decorator object get function to access private intConnectorsRetiredReportID
    @property
    def intConnectorsRetiredReportID(self):
        return self._intConnectorsRetiredReportID

    # Property decorator object get function to access private dtmReportDate
    @property
    def dtmReportDate(self):
        return self._dtmReportDate
            
    # setter method 
    @intConnectorsRetiredReportID.setter 
    def intConnectorsRetiredReportID(self, intConnectorsRetiredReportID): 
        # Return true if specified object is of int type
        if not isinstance(intConnectorsRetiredReportID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intConnectorsRetiredReportID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intConnectorsRetiredReportID = intConnectorsRetiredReportID    

    # setter method 
    @dtmReportDate.setter 
    def dtmReportDate(self, dtmReportDate):              
        # Return true if specified object is of str type
        if not isinstance(dtmReportDate, str): 
            raise TypeError('Report Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmReportDate.isspace(): 
            raise ValueError('Report Date cannot be empty')       
        # Convert the date to string
        dtmReportDate = datetime.strptime(dtmReportDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmReportDate, date): 
            raise TypeError('Report Date must be a valid date') 
        # Convert the date back to string
        dtmReportDate = str(dtmReportDate)

        self._dtmReportDate = dtmReportDate  

    def Append_Connector_RetiredReportID_List(self, intObject):
        """ 
        Function Name: Append_Connector_RetiredReportID_List
        Function Description: This function appends objects to the Connector Retired Report ID list
        """    
        self.aintConnectorsRetiredReportID.append(intObject)

    def Remove_Connector_RetiredReportID_List(self, intObject):
        """ 
        Function Name: Remove_Connector_RetiredReportID_List
        Function Description: This function removes objects in the Connector Retired Report ID list
        """    
        self.aintConnectorsRetiredReportID.remove(intObject)

    def Get_Connector_RetiredReportID_List_Obj(self):
        """ 
        Function Name: Get_Connector_RetiredReportID_List_Obj
        Function Description: This function gets all the objects in the Connector Retired Report ID list
        """    
        return self.aintConnectorsRetiredReportID   

    def Delete_Connector_RetiredReport_Data(self):
        """ 
        Function Name: Delete_Connector_RetiredReport_Data
        Function Description: This function removes all the objects in the Connector Retired Report class
        """    
        ConnectorsRetiredReport.aintConnectorsRetiredReportID = []

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
                                
    def Add_Connector_RetiredReport_Query(self):
        """ 
        Function Name: Add_Connector_RetiredReport_Query
        Function Description: This function updated the database with all of the necessary objects
        """
        # Get todays date
        dtmToday = datetime.now().date()
        self.dtmReportDate = str(dtmToday)
                
        # Create the sql query string
        sqlTableCol = ("intConnectorRetiredReportID", "intConnectorInspectionID", "intInspectorID", "dtmReportDate")
        sqlTableName = "TConnectorRetiredReports"
        
        # Get the max primary key value for the table
        sqlMaxPrimKeyID = ConnectorsRetiredReport.Get_Max_Primary_Key(self, sqlTableName, sqlTableCol[0])

        # For testing purposes, set the inspector ID to 1
        Inspector.intInspectorID = 1
        
        # Set the inspector ID
        # print(UserLogins.aCurrentUserLogin)
        # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID
        
        # Perform the insert query
        sqlTableValues = (sqlMaxPrimKeyID, self.intConnectorInspectionID, Inspector.intInspectorID, self.dtmReportDate)

        # Set the parameters
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Update_Connector_RetiredReport_Query(self):
        """ 
        Function Name: Update_Connector_RetiredReport_Query
        Function Description: This function updated the database with all of the necessary objects
        """
        # Get todays date
        dtmToday = datetime.now().date()
        self.dtmReportDate = str(dtmToday)
                
        # Create the sql query string
        sqlTableCol = ("intConnectorsRetiredReportID", "intConnectorInspectionID", "intInspectorID", "dtmReportDate")
        sqlTableName = "TConnectorsRetiredReports"
        sqlViewName = "vConnectorInspectID_OutOfService"
        
        # Get the max primary key value for the table
        sqlConnectorInspectValues = Queries.Get_All_DB_Values(self, sqlViewName)
        sqlConnectorRetiredReportValues = Queries.Get_All_DB_Values(self, sqlTableName)
        
        # For testing purposes, set the inspector ID to 1
        Inspector.intInspectorID = 1
        
        # Set the inspector ID
        # print(UserLogins.aCurrentUserLogin)
        # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID

        # Process each inspection value
        for inspectValue in sqlConnectorInspectValues:
            inspectionID = inspectValue[0]
            if inspectionID not in [report[0] for report in sqlConnectorRetiredReportValues]:
                # Inspection ID not found in the report, consider adding it
                self.intConnectorInspectionID = inspectionID
                ConnectorsRetiredReport.Add_Connector_RetiredReport_Query(self)

            elif self.strEquipInUse != "Retired":
                # Remove the report if the device is no longer in service
                Queries.Remove_Attribute_Query(Queries, sqlTableName, sqlTableCol[0], inspectionID)

            else:
                # Update the existing report
                sqlTableValues = (inspectionID, self.intConnectorInspectionID, Inspector.intInspectorID, self.dtmReportDate)
                sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], inspectionID)
                Queries.dbExeUSP_UpdateValues(Queries, sqlParams)

    def Get_Last_Two_Connectors_Data(self):
        """ 
        Function Name: Get_Last_Two_Connectors_Data
        Function Description: Retrieves the last two entries from the Connectors table.
        """
        # Assuming 'intConnectorID' is the auto-incrementing primary key of the TConnectors table
        primaryKeyColumn = "intConnectorInspectionID"
        sqlQuery = f"""SELECT * FROM TConnectorInspections ORDER BY {primaryKeyColumn} DESC LIMIT 2"""
        
        # Execute the query and get the results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
        
        # Since the results are in reverse order, reverse them before returning
        return QueryResultList[::-1]

            
class BelayDevices():
    """
    Class Name: BelayDevices
    Class Description: This class gets and sets all of the BelayDevices attributes. 
    """
    # Create class variable shared amongst all BelayDevices methods
    aintBelayDeviceIDCache = []
    astrBelayDeviceNameCache = []
    astrSerialNumCache = []
    astrBumperNumCache = []
    astrManufactureNameCache = []
    adtmManufactureDateCache = []
    adtmInstallationDateCache = []
    adtmLastInspectionDateCache = []
    adtmNextInspectionDateCache = []
    astrDeviceTypeCache = []
    astrEquipInUseCache = []

    # Instantiate the following attributes
    def __init__(self, intBelayDeviceID, strBelayDeviceName, strSerialNum, strBumperNum, strManufactureName,
                    dtmManufactureDate, dtmInstallationDate, dtmLastInspectionDate, dtmNextInspectionDate, 
                    strDeviceType, strEquipInUse):
        self.intBelayDeviceID = intBelayDeviceID
        self.strBelayDeviceName = strBelayDeviceName
        self.strSerialNum = strSerialNum
        self.strBumperNum = strBumperNum
        self.strManufactureName = strManufactureName
        self.dtmManufactureDate = dtmManufactureDate
        self.dtmInstallationDate = dtmInstallationDate
        self.dtmLastInspectionDate = dtmLastInspectionDate
        self.dtmNextInspectionDate = dtmNextInspectionDate
        self.strDeviceType = strDeviceType
        self.strEquipInUse = strEquipInUse

    # Property decorator object get function to access private intBelayDeviceID
    @property
    def intBelayDeviceID(self):
        return self._intBelayDeviceID

    # Property decorator object get function to access private strBelayDeviceName
    @property
    def strBelayDeviceName(self):
        return self._strBelayDeviceName
    
    # Property decorator object get function to access private strSerialNum
    @property
    def strSerialNum(self):
        return self._strSerialNum

    # Property decorator object get function to access private strBumperNum
    @property
    def strBumperNum(self):
        return self._strBumperNum

    # Property decorator object get function to access private strManufactureName
    @property
    def strManufactureName(self):
        return self._strManufactureName
        
    # Property decorator object get function to access private dtmManufactureDate
    @property
    def dtmManufactureDate(self):
        return self._dtmManufactureDate

    # Property decorator object get function to access private dtmInstallationDate
    @property
    def dtmInstallationDate(self):
        return self._dtmInstallationDate

    # Property decorator object get function to access private dtmLastInspectionDate
    @property
    def dtmLastInspectionDate(self):
        return self._dtmLastInspectionDate

    # Property decorator object get function to access private dtmNextInspectionDate
    @property
    def dtmNextInspectionDate(self):
        return self._dtmNextInspectionDate

    # Property decorator object get function to access private strDeviceType
    @property
    def strDeviceType(self):
        return self._strDeviceType
    
    # Property decorator object get function to access private strEquipInUse
    @property
    def strEquipInUse(self):
        return self._strEquipInUse

    # setter method 
    @intBelayDeviceID.setter 
    def intBelayDeviceID(self, intBelayDeviceID): 
        # Return true if specified object is of int type
        if not isinstance(intBelayDeviceID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intBelayDeviceID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBelayDeviceID = intBelayDeviceID    

    # setter method 
    @strBelayDeviceName.setter 
    def strBelayDeviceName(self, strBelayDeviceName): 
        # Return true if specified object is of str type
        if not isinstance(strBelayDeviceName, str): 
            raise TypeError('Belay Device Name must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strBelayDeviceName.isspace(): 
            raise ValueError('Belay Device Name cannot be empty') 
        # Set the attribute to the value if true
        if strBelayDeviceName.isascii():
            self._strBelayDeviceName = strBelayDeviceName  

    # setter method 
    @strSerialNum.setter 
    def strSerialNum(self, strSerialNum): 
        # Return true if specified object is of str type
        if not isinstance(strSerialNum, str): 
            raise TypeError('Serial Number must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strSerialNum.isspace(): 
            raise ValueError('Serial Number cannot be empty') 
        # Set the attribute to the value if true
        if strSerialNum.isascii():
            self._strSerialNum = strSerialNum  
            # Set the global class bool to true
            Bool_Flag.Set_BelayDevice_Bool_Value_True(Bool_Flag)

    # setter method 
    @strBumperNum.setter 
    def strBumperNum(self, strBumperNum): 
        # Return true if specified object is of str type
        if not isinstance(strBumperNum, str): 
            raise TypeError('Bumper Number must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha numeric
        if strBumperNum.isspace(): 
            raise ValueError('Bumper Number cannot be empty') 
        # Set the attribute to the value if true
        if strBumperNum.isascii():
            self._strBumperNum = strBumperNum   

    # setter method 
    @strManufactureName.setter 
    def strManufactureName(self, strManufactureName):   
        # Return true if specified object is of str type
        if not isinstance(strManufactureName, str): 
            raise TypeError('Manufacture Name must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if strManufactureName.isspace(): 
            raise ValueError('Manufacture Name cannot be empty') 
        # Set the attribute to the value if true
        if strManufactureName.isascii():
            self._strManufactureName = strManufactureName   
                        
    # setter method 
    @dtmManufactureDate.setter 
    def dtmManufactureDate(self, dtmManufactureDate): 
        # Return true if specified object is of str type
        if not isinstance(dtmManufactureDate, str): 
            raise TypeError('Manufacture Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmManufactureDate.isspace(): 
            raise ValueError('Manufacture Date cannot be empty')       
        # Convert the date to string
        dtmManufactureDate = datetime.strptime(dtmManufactureDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmManufactureDate, date): 
            raise TypeError('Manufacture Date must be a valid date') 
        # Convert the date back to string
        dtmManufactureDate = str(dtmManufactureDate)

        self._dtmManufactureDate = dtmManufactureDate                 
    # setter method 
    @dtmInstallationDate.setter 
    def dtmInstallationDate(self, dtmInstallationDate): 
        # Return true if specified object is of str type
        if not isinstance(dtmInstallationDate, str): 
            raise TypeError('Install Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmInstallationDate.isspace(): 
            raise ValueError('Install Date cannot be empty')       
        # Convert the date to string
        dtmInstallationDate = datetime.strptime(dtmInstallationDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmInstallationDate, date): 
            raise TypeError('Install Date must be a valid date') 
        # Convert the date back to string
        dtmInstallationDate = str(dtmInstallationDate)

        self._dtmInstallationDate = dtmInstallationDate   
        
    # setter method 
    @dtmLastInspectionDate.setter 
    def dtmLastInspectionDate(self, dtmLastInspectionDate): 
        # Return true if specified object is of str type
        if not isinstance(dtmLastInspectionDate, str): 
            raise TypeError('Last Inspection Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmLastInspectionDate.isspace(): 
            raise ValueError('Last Inspection Date cannot be empty')       
        # Convert the date to string
        dtmLastInspectionDate = datetime.strptime(dtmLastInspectionDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmLastInspectionDate, date): 
            raise TypeError('Last Inspection Date must be a valid date') 
        # Convert the date back to string
        dtmLastInspectionDate = str(dtmLastInspectionDate)

        self._dtmLastInspectionDate = dtmLastInspectionDate   

    # setter method 
    @dtmNextInspectionDate.setter 
    def dtmNextInspectionDate(self, dtmNextInspectionDate): 
        # Return true if specified object is of str type
        if not isinstance(dtmNextInspectionDate, str): 
            raise TypeError('Next Inspection Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmNextInspectionDate.isspace(): 
            raise ValueError('Next Inspection Date cannot be empty')       
        # Convert the date to string
        dtmNextInspectionDate = datetime.strptime(dtmNextInspectionDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmNextInspectionDate, date): 
            raise TypeError('Next Inspection Date must be a valid date') 
        # Convert the date back to string
        dtmNextInspectionDate = str(dtmNextInspectionDate)

        self._dtmNextInspectionDate = dtmNextInspectionDate   
                
    # setter method 
    @strDeviceType.setter
    def strDeviceType(self, strDeviceType):
        # Check if the input is a string
        if not isinstance(strDeviceType, str):
            raise TypeError('Device Type must be a string')

        # Check if the string is empty or consists only of whitespace
        if strDeviceType.isspace() or not strDeviceType:
            raise ValueError('Device Type Status cannot be empty')

        # Split the string by spaces and check each word
        words = strDeviceType.split()
        for word in words:
            # Check if the word is alpha or hyphenated
            if not all(subpart.isalpha() for subpart in word.split('-')):
                raise ValueError('Device Type must be a string of letters, hyphenated words, or multiple words separated by spaces')

        self._strDeviceType = strDeviceType  
                            
    # setter method 
    @strEquipInUse.setter 
    def strEquipInUse(self, strEquipInUse): 
        # Return true if specified object is of str type
        if not isinstance(strEquipInUse, str): 
            raise TypeError('In Use Status must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if strEquipInUse.isspace(): 
            raise ValueError('In Use Status cannot be empty') 
        # Set the attribute to the value if true
        elif strEquipInUse.isalpha():
            self._strEquipInUse = strEquipInUse   

    def Append_BelayDeviceIDList(self, intObject):
        """ 
        Function Name: Append_BelayDeviceIDList
        Function Description: This function appends objects to the BelayDevice ID list
        """    
        self.aintBelayDeviceIDCache.append(intObject)

    def Remove_BelayDeviceIDList(self, intObject):
        """ 
        Function Name: Remove_BelayDeviceIDList
        Function Description: This function removes objects in the BelayDevice ID list
        """    
        self.aintBelayDeviceIDCache.remove(intObject)

    def Get_BelayDeviceIDList_Obj(self):
        """ 
        Function Name: Get_BelayDeviceIDList_Obj
        Function Description: This function gets all the objects in the BelayDevice ID list
        """    
        return self.aintBelayDeviceIDCache            

    def Append_BelayDevice_NameList(self, strObject):
        """ 
        Function Name: Append_BelayDevice_NameList
        Function Description: This function appends objects to the Serial Num list
        """    
        self.astrBelayDeviceNameCache.append(strObject)

    def Remove_BelayDevice_NameList(self, strObject):
        """ 
        Function Name: Remove_BelayDevice_NameList
        Function Description: This function removes objects in the Serial Num list
        """    
        self.astrBelayDeviceNameCache.remove(strObject)

    def Get_BelayDevice_NameList_Obj(self):
        """ 
        Function Name: Get_BelayDevice_NameList_Obj
        Function Description: This function gets all the objects in the Serial Num list
        """    
        return self.astrBelayDeviceNameCache 
    
    def Append_BelayDevice_SerialNumList(self, strObject):
        """ 
        Function Name: Append_SerialNumList
        Function Description: This function appends objects to the Serial Num list
        """    
        self.astrSerialNumCache.append(strObject)

    def Remove_BelayDevice_SerialNumList(self, strObject):
        """ 
        Function Name: Remove_SerialNumList
        Function Description: This function removes objects in the Serial Num list
        """    
        self.astrSerialNumCache.remove(strObject)

    def Get_BelayDevice_SerialNumList_Obj(self):
        """ 
        Function Name: Get_SerialNumList_Obj
        Function Description: This function gets all the objects in the Serial Num list
        """    
        return self.astrSerialNumCache 

    def Append_BelayDevice_BumperNumList(self, strObject):
        """ 
        Function Name: Append_BumperNumList
        Function Description: This function appends objects to the Bumper Num list
        """    
        self.astrBumperNumCache.append(strObject)

    def Remove_BelayDevice_BumperNumList(self, strObject):
        """ 
        Function Name: Remove_BumperNumList
        Function Description: This function removes objects in the Bumper Num list
        """    
        self.astrBumperNumCache.remove(strObject)

    def Get_BelayDevice_BumperNumList_Obj(self):
        """ 
        Function Name: Get_BumperNumList_Obj
        Function Description: This function gets all the objects in the Bumper Num list
        """    
        return self.astrBumperNumCache 

    def Append_BelayDevice_ManuNameList(self, strObject):
        """ 
        Function Name: Append_BelayDevice_ManuNameList
        Function Description: This function appends objects to the ManuFacture Name list
        """    
        self.astrManufactureNameCache.append(strObject)

    def Remove_BelayDevice_ManuNameList(self, strObject):
        """ 
        Function Name: Remove_BelayDevice_ManuNameList
        Function Description: This function removes objects in the ManuFacture Name list
        """    
        self.astrManufactureNameCache.remove(strObject)

    def Get_BelayDevice_ManuNameList_Obj(self):
        """ 
        Function Name: Get_BelayDevice_ManuNameList_Obj
        Function Description: This function gets all the objects in the ManuFacture Name list
        """    
        return self.astrManufactureNameCache

    def Append_BelayDevice_ManuDateList(self, strObject):
        """ 
        Function Name: Append_BelayDevice_ManuDateList
        Function Description: This function appends objects to the ManuFacture Date list
        """    
        self.adtmManufactureDateCache.append(strObject)

    def Remove_BelayDevice_ManuDateList(self, strObject):
        """ 
        Function Name: Remove_BelayDevice_ManuDateList
        Function Description: This function removes objects in the ManuFacture Date list
        """    
        self.adtmManufactureDateCache.remove(strObject)

    def Get_BelayDevice_ManuDateList_Obj(self):
        """ 
        Function Name: Get_BelayDevice_ManuDateList_Obj
        Function Description: This function gets all the objects in the ManuFacture Date list
        """    
        return self.adtmManufactureDateCache

    def Append_BelayDevice_InstallDateList(self, strObject):
        """ 
        Function Name: Append_BelayDevice_InstallDateList
        Function Description: This function appends objects to the Install Date list
        """    
        self.adtmInstallationDateCache.append(strObject)

    def Remove_BelayDevice_InstallDateList(self, strObject):
        """ 
        Function Name: Remove_BelayDevice_InstallDateList
        Function Description: This function removes objects in the Install Date list
        """    
        self.adtmInstallationDateCache.remove(strObject)

    def Get_BelayDevice_InstallDateList_Obj(self):
        """ 
        Function Name: Get_BelayDevice_InstallDateList_Obj
        Function Description: This function gets all the objects in the Install Date list
        """    
        return self.adtmInstallationDateCache

    def Append_BelayDevice_LastInspectDateList(self, strObject):
        """ 
        Function Name: Append_BelayDevice_LastInspectDateList
        Function Description: This function appends objects to the Last Inspect Date list
        """    
        self.adtmLastInspectionDateCache.append(strObject)

    def Remove_BelayDevice_LastInspectDateList(self, strObject):
        """ 
        Function Name: Remove_BelayDevice_LastInspectDateList
        Function Description: This function removes objects in the Last Inspect Date list
        """    
        self.adtmLastInspectionDateCache.remove(strObject)

    def Get_BelayDevice_LastInspectDateList_Obj(self):
        """ 
        Function Name: Get_BelayDevice_LastInspectDateList_Obj
        Function Description: This function gets all the objects in the Last Inspect Date list
        """    
        return self.adtmLastInspectionDateCache

    def Append_BelayDevice_NextInspectDateList(self, strObject):
        """ 
        Function Name: Append_BelayDevice_NextInspectDateList
        Function Description: This function appends objects to the Next Inspect Date list
        """    
        self.adtmNextInspectionDateCache.append(strObject)

    def Remove_BelayDevice_NextInspectDateList(self, strObject):
        """ 
        Function Name: Remove_BelayDevice_NextInspectDateList
        Function Description: This function removes objects in the Next Inspect Date list
        """    
        self.adtmNextInspectionDateCache.remove(strObject)

    def Get_BelayDevice_NextInspectDateList_Obj(self):
        """ 
        Function Name: Get_BelayDevice_NextInspectDateList_Obj
        Function Description: This function gets all the objects in the Next Inspect Date list
        """    
        return self.adtmNextInspectionDateCache

    def Append_BelayDevice_TypeList(self, strObject):
        """ 
        Function Name: Append_Device_Type_EquipInUseList
        Function Description: This function appends objects to the Device Type list
        """    
        self.astrDeviceTypeCache.append(strObject)

    def Remove_BelayDevice_TypeList(self, strObject):
        """ 
        Function Name: Remove_Device_Type_EquipInUseList
        Function Description: This function removes objects in the Device Type list
        """    
        self.astrDeviceTypeCache.remove(strObject)

    def Get_BelayDevice_Type_List_Obj(self):
        """ 
        Function Name: Get_Device_Type_List_Obj
        Function Description: This function gets all the objects in the Device Type list
        """    
        return self.astrDeviceTypeCache
    
    def Append_BelayDevice_EquipInUseList(self, strObject):
        """ 
        Function Name: Append_BelayDevice_EquipInUseList
        Function Description: This function appends objects to the Equipment In Use list
        """    
        self.astrEquipInUseCache.append(strObject)

    def Remove_BelayDevice_EquipInUseList(self, strObject):
        """ 
        Function Name: Remove_BelayDevice_EquipInUseList
        Function Description: This function removes objects in the Equipment In Use list
        """    
        self.astrEquipInUseCache.remove(strObject)

    def Get_BelayDevice_EquipInUseList_Obj(self):
        """ 
        Function Name: Get_BelayDevice_EquipInUseList_Obj
        Function Description: This function gets all the objects in the Equipment In Use list
        """    
        return self.astrEquipInUseCache

    def Get_BelayDevices_Data(self):
        """ 
        Function Name: Get_BelayDevices_Data
        Function Description: This function gets all the objects in the BelayDevices table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TBelayDevices"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # First check if the contents are found and if yes, proceed to get the contents of the table
        if QueryResultList is not None:
            # Append the Auto Belay Data List
            for i in range(len(QueryResultList)):
                BelayDevices.Append_BelayDeviceIDList(self, QueryResultList[i][0])
                BelayDevices.Append_BelayDevice_NameList(self, QueryResultList[i][1]) 
                BelayDevices.Append_BelayDevice_SerialNumList(self, QueryResultList[i][2]) 
                BelayDevices.Append_BelayDevice_BumperNumList(self, QueryResultList[i][3]) 
                BelayDevices.Append_BelayDevice_ManuNameList(self, QueryResultList[i][4]) 
                BelayDevices.Append_BelayDevice_ManuDateList(self, QueryResultList[i][5]) 
                BelayDevices.Append_BelayDevice_InstallDateList(self, QueryResultList[i][6]) 
                BelayDevices.Append_BelayDevice_LastInspectDateList(self, QueryResultList[i][7]) 
                BelayDevices.Append_BelayDevice_NextInspectDateList(self, QueryResultList[i][8]) 
                BelayDevices.Append_BelayDevice_TypeList(self, QueryResultList[i][9]) 
                BelayDevices.Append_BelayDevice_EquipInUseList(self, QueryResultList[i][10]) 
                
    def Set_BelayDevices_Selection(self):
        """ 
        Function Name: Set_BelayDevices_Selection
        Function Description: This function will set the selection name from the user and will update the 
        class objects with the data from the database.
        """    
        # First get the selection from the user 
        for i, item in enumerate(self.astrSerialNumCache):
            if self.strSerialNum == item:
                # Assign the iterable num to the ID num and assign the objects to the desired data sets    
                self.intBelayDeviceID = self.aintBelayDeviceIDCache[i]
                self.strBelayDeviceName = self.astrBelayDeviceNameCache[i]
                if not self.strSerialNum:                    
                    self.strSerialNum = self.astrSerialNumCache[i]
                self.strBumperNum = self.astrBumperNumCache[i]
                self.strManufactureName = self.astrManufactureNameCache[i]
                self.dtmManufactureDate = self.adtmManufactureDateCache[i]
                self.dtmInstallationDate = self.adtmInstallationDateCache[i]
                self.dtmLastInspectionDate = self.adtmLastInspectionDateCache[i]
                self.dtmNextInspectionDate = self.adtmNextInspectionDateCache[i]
                self.strDeviceType = self.astrDeviceTypeCache[i]
                if not self.strEquipInUse:
                    self.strEquipInUse = self.astrEquipInUseCache[i]    
                
                break

    def Set_BelayDevices_Data(self):
        """ 
        Function Name: Set_BelayDevices_Data
        Function Description: This function will set the class objects for the device when selected
        """    
        # First get the selection from the user 
        for i, item in enumerate(self.astrSerialNumCache):
            if self.strSerialNum == item:
                # Assign the iterable num to the ID num and assign the objects to the desired data sets    
                self.intBelayDeviceID = self.aintBelayDeviceIDCache[i]  
                self.strBelayDeviceName = self.astrBelayDeviceNameCache[i]                
                self.strSerialNum = self.astrSerialNumCache[i]
                self.strBumperNum = self.astrBumperNumCache[i]
                self.strManufactureName = self.astrManufactureNameCache[i]
                self.dtmManufactureDate = self.adtmManufactureDateCache[i]
                self.dtmInstallationDate = self.adtmInstallationDateCache[i]
                self.dtmLastInspectionDate = self.adtmLastInspectionDateCache[i]
                self.dtmNextInspectionDate = self.adtmNextInspectionDateCache[i]
                self.strDeviceType = self.astrDeviceTypeCache[i]
                self.strEquipInUse = self.astrEquipInUseCache[i]
                # Set the global class bool to true
                Bool_Flag.Set_BelayDevice_Bool_Value_True(Bool_Flag)    
                
                break

    def Add_BelayDevices_Query(self):
        """ 
        Function Name: Add_BelayDevices_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Create the sql query string
        sqlTableCol = ("intBelayDeviceID","strBelayDeviceName", "strSerialNum", "strBumperNum", "strManufactureName", "dtmManufactureDate", 
                        "dtmInstallationDate", "dtmLastInspectionDate", "dtmNextInspectionDate", "strDeviceType", "strEquipInUse")   
        sqlTableName = "TBelayDevices"  

        # Set the Table values and the params tuple
        sqlTableValues = (self.intBelayDeviceID, self.strBelayDeviceName, self.strSerialNum, self.strBumperNum, self.strManufactureName, 
                            self.dtmManufactureDate, self.dtmInstallationDate, self.dtmLastInspectionDate, self.dtmNextInspectionDate, 
                            self.strDeviceType, self.strEquipInUse)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

        # Reload the data after user submits entry
        BelayDevices.Delete_BelayDevices_Data(BelayDevices)
        BelayDevices.Get_BelayDevices_Data(BelayDevices)

    def Update_BelayDevices_Inspect_Dates(self):
        """ 
        Function Name: Update_BelayDevices_Inspect_Dates
        Function Description: This function updated the database with inspection dates last and next
        """    
        # Create the sql query string
        sqlTableCol = ("intBelayDeviceID", "dtmLastInspectionDate", "dtmNextInspectionDate")   
        sqlTableName = "TBelayDevices"  

        # Set the last and next inspection date based off of the current date
        aDateResult = BaseFunctions.Update_Inspection_Date()
        self.dtmLastInspectionDate = datetime.strftime(aDateResult[0], '%Y-%m-%d')
        self.dtmNextInspectionDate = datetime.strftime(aDateResult[1], '%Y-%m-%d')
        
        # Set the Table values and the params tuple
        sqlTableValues = (self.intBelayDeviceID, self.dtmLastInspectionDate, self.dtmNextInspectionDate)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], sqlTableValues[0])         

        # Execute the stored procedure
        Queries.dbExeUSP_UpdateValues(Queries, sqlParams)

    def Update_BelayDevices_InUse_Status(self):
        """ 
        Function Name: Update_BelayDevices_InUse_Status
        Function Description: This function updated the database with in use status of the BelayDevice
        """ 
        # Declare Local Variables
        intFailStatus = int(3)
        
        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(BelayDeviceInspect.aBelayDeviceInspectStatus)
            
        if intOverallStatus == intFailStatus:
            # Check if the user knows about the BelayDevice being failed. If the user removed from wall, the BelayDevice is not longer in use
            messagebox.showwarning(message='ATTENTION! \n\nWe have identified an overall status --> FAIL <-- for this Belay Device. \n\nPlease remove the retired device from future use.')
            self.strEquipInUse = "Retired"
            Bool_Flag.Set_BelayDeviceRetired_Bool_Value_True(Bool_Flag)              
            
        # Create the sql query string
        sqlTableCol = ("intBelayDeviceID", "strEquipInUse")   
        sqlTableName = "TBelayDevices"  

        # Set the Table values and the params tuple
        sqlTableValues = (self.intBelayDeviceID, self.strEquipInUse)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], sqlTableValues[0])         

        # Execute the stored procedure
        Queries.dbExeUSP_UpdateValues(Queries, sqlParams)
                
    def Update_NewBelayDevices_Query(self):
        """ 
        Function Name: Update_NewBelayDevices_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Create the sql query string
        sqlTableCol = ("intBelayDeviceID", "strBelayDeviceName", "strSerialNum", "strBumperNum", "strManufactureName", 
                        "dtmManufactureDate", "dtmInstallationDate", "dtmLastInspectionDate", 
                        "dtmNextInspectionDate", "strDeviceType", "strEquipInUse")   
        sqlTableName = "TBelayDevices"  

        # Set the Table values and the params tuple
        sqlTableValues = (self.intBelayDeviceID, self.strBelayDeviceName, self.strSerialNum, self.strBumperNum, self.strManufactureName, 
                            self.dtmManufactureDate, self.dtmInstallationDate, self.dtmLastInspectionDate, self.dtmNextInspectionDate, 
                            self.strDeviceType, self.strEquipInUse)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], sqlTableValues[0])       

        # Execute the stored procedure
        Queries.dbExeUSP_UpdateValues(Queries, sqlParams)

        # Reload the data after user submits entry
        BelayDevices.Delete_BelayDevices_Data(BelayDevices)
        BelayDevices.Get_BelayDevices_Data(BelayDevices)
        
    def Set_Global_BelayDevices_Attributes(self):
        """ 
        Function Name: Set_Global_BelayDevices_Attributes
        Function Description: This function set BelayDevices attributes once the user proceeds with adding a new
        BelayDevices to the database.
        """    
        BelayDevices.strBelayDeviceName = self.strBelayDeviceName
        BelayDevices.strSerialNum = self.strSerialNum
        BelayDevices.strBumperNum = self.strBumperNum
        BelayDevices.strManufactureName = self.strManufactureName
        BelayDevices.dtmManufactureDate = self.dtmManufactureDate
        BelayDevices.dtmInstallationDate = self.dtmInstallationDate
        BelayDevices.dtmLastInspectionDate = self.dtmLastInspectionDate
        BelayDevices.dtmNextInspectionDate = self.dtmNextInspectionDate
        BelayDevices.strDeviceType = self.strDeviceType
        BelayDevices.strEquipInUse = self.strEquipInUse

    def Delete_BelayDevices_Data(self):
        """ 
        Function Name: Delete_BelayDevices_Data
        Function Description: This function removes all the objects in the BelayDevices class
        """    
        BelayDevices.aintBelayDeviceIDCache = [] 
        BelayDevices.astrBelayDeviceNameCache = []  
        BelayDevices.astrSerialNumCache = []
        BelayDevices.astrBumperNumCache = []
        BelayDevices.astrManufactureNameCache = []
        BelayDevices.adtmManufactureDateCache = []
        BelayDevices.adtmInstallationDateCache = []
        BelayDevices.adtmLastInspectionDateCache = []
        BelayDevices.adtmNextInspectionDateCache = []
        BelayDevices.astrDeviceTypeCache = []
        BelayDevices.astrEquipInUseCache = []    
        
class BelayDeviceFunction():
    """
    Class Name: BelayDeviceFunction
    Class Description: This class gets and sets all of the BelayDevice Function attributes. 
    """
    # Create class variable shared amongst all BelayDevice Function methods
    aintBelayDeviceFunctionID = []
    astrBelayDeviceFunctionDesc = []
        
    # Instantiate the following attributes
    def __init__(self, intBelayDeviceFunctionID, strBelayDeviceFunctionDesc):
        self.intBelayDeviceFunctionID = intBelayDeviceFunctionID
        self.strBelayDeviceFunctionDesc = strBelayDeviceFunctionDesc

    # Property decorator object get function to access private intBelayDeviceFunctionID
    @property
    def intBelayDeviceFunctionID(self):
        return self._intBelayDeviceFunctionID

    # Property decorator object get function to access private strBelayDeviceFunctionDesc
    @property
    def strBelayDeviceFunctionDesc(self):
        return self._strBelayDeviceFunctionDesc
        
    # setter method 
    @intBelayDeviceFunctionID.setter 
    def intBelayDeviceFunctionID(self, intBelayDeviceFunctionID): 
        # Return true if specified object is of int type
        if not isinstance(intBelayDeviceFunctionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intBelayDeviceFunctionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBelayDeviceFunctionID = intBelayDeviceFunctionID 
        
    # setter method 
    @strBelayDeviceFunctionDesc.setter 
    def strBelayDeviceFunctionDesc(self, strBelayDeviceFunctionDesc): 
        # Return true if specified object is of str type
        if not isinstance(strBelayDeviceFunctionDesc, str): 
            raise TypeError('Hose Length must be a string') 
        # Check if the value is empty, otherwise check if the value is alpha 
        if strBelayDeviceFunctionDesc.isspace(): 
            raise ValueError('Hose Length cannot be empty') 
        # Set the attribute to the value if true
        elif strBelayDeviceFunctionDesc.isascii():
            self._strBelayDeviceFunctionDesc = strBelayDeviceFunctionDesc

    def Append_BelayDeviceFunctIDList(self, intObject):
        """ 
        Function Name: Append_BelayDeviceFunctIDList
        Function Description: This function appends objects to the BelayDevice Function ID list
        """    
        self.aintBelayDeviceFunctionID.append(intObject)

    def Remove_BelayDeviceFunctIDList(self, intObject):
        """ 
        Function Name: Remove_BelayDeviceFunctIDList
        Function Description: This function removes objects in the BelayDevice Function ID list
        """    
        self.aintBelayDeviceFunctionID.remove(intObject)

    def Get_BelayDeviceFunctIDList_Obj(self):
        """ 
        Function Name: Get_BelayDeviceFunctIDList_Obj
        Function Description: This function gets all the objects in the BelayDevice Function ID list
        """    
        return self.aintBelayDeviceFunctionID
    
    def Append_BelayDeviceFunctList(self, strObject):
        """ 
        Function Name: Append_BelayDeviceFunctList
        Function Description: This function appends objects to the BelayDevice Function list
        """    
        self.astrBelayDeviceFunctionDesc.append(strObject)

    def Remove_BelayDeviceFunctList(self, strObject):
        """ 
        Function Name: Remove_BelayDeviceFunctList
        Function Description: This function removes objects in the BelayDevice Function list
        """    
        self.astrBelayDeviceFunctionDesc.remove(strObject)

    def Get_BelayDeviceFunctList_Obj(self):
        """ 
        Function Name: Get_BelayDeviceFunctList_Obj
        Function Description: This function gets all the objects in the BelayDevice Function list
        """    
        return self.astrBelayDeviceFunctionDesc   

    def Get_BelayDeviceFunct_Data(self):
        """ 
        Function Name: Get_BelayDeviceFunct_Data
        Function Description: This function gets all the objects in the BelayDevice Functions table
        """    
        # Create the sql query string
        sqlQuery = """SELECT * FROM TBelayDeviceFunctions"""
        
        # Get the query results
        QueryResultList = Database.dbExeQuery(Database, sqlQuery)
    
        # Append the housing Data List
        for i in range(len(QueryResultList)):
            BelayDeviceFunction.Append_BelayDeviceFunctIDList(self, QueryResultList[i][0])
            BelayDeviceFunction.Append_BelayDeviceFunctList(self, QueryResultList[i][1]) 

    def Delete_BelayDeviceFunct_Data(self):
        """ 
        Function Name: Delete_BelayDeviceFunct_Data
        Function Description: This function removes all the objects in the BelayDevice Function class
        """    
        BelayDeviceFunction.aintBelayDeviceFunctionID = []
        BelayDeviceFunction.astrBelayDeviceFunctionDesc = []
                    

class BelayDeviceVisSelection():
    """
    Class Name: BelayDeviceVisSelection
    Class Description: This class gets and sets all of the BelayDevice Visual Selections. 
    """
    # Create class variable shared amongst all BelayDevice visual methods
    aintBelayDeviceVisMetalSelectID = []
    astrBelayDeviceVisMetSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intBelayDeviceVisMetalSelectID, strBelayDeviceVisMetSelect, strBelayDeviceVisStatus):
        self.intBelayDeviceVisMetalSelectID = intBelayDeviceVisMetalSelectID
        self.strBelayDeviceVisMetSelect = strBelayDeviceVisMetSelect    
        self.strBelayDeviceVisStatus = strBelayDeviceVisStatus

    # Property decorator object get function to access private intBelayDeviceVisMetalSelectID
    @property
    def intBelayDeviceVisMetalSelectID(self):
        return self._intBelayDeviceVisMetalSelectID

    # Property decorator object get function to access private strBelayDeviceVisMetSelect
    @property
    def strBelayDeviceVisMetSelect(self):
        return self._strBelayDeviceVisMetSelect

    # Property decorator object get function to access private strBelayDeviceVisStatus
    @property
    def strBelayDeviceVisStatus(self):
        return self._strBelayDeviceVisStatus
                
    # setter method 
    @intBelayDeviceVisMetalSelectID.setter 
    def intBelayDeviceVisMetalSelectID(self, intBelayDeviceVisMetalSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intBelayDeviceVisMetalSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intBelayDeviceVisMetalSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBelayDeviceVisMetalSelectID = intBelayDeviceVisMetalSelectID 

    # setter method 
    @strBelayDeviceVisMetSelect.setter 
    def strBelayDeviceVisMetSelect(self, strBelayDeviceVisMetSelect): 
        # Return true if specified object is of str type
        if not isinstance(strBelayDeviceVisMetSelect, str): 
            raise TypeError('BelayDevice visual input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBelayDeviceVisMetSelect.isspace(): 
            raise ValueError('BelayDevice visual input cannot be empty') 
        # Set the attribute to the value if true
        elif strBelayDeviceVisMetSelect.isascii():
            self._strBelayDeviceVisMetSelect = strBelayDeviceVisMetSelect
                    
    # setter method 
    @strBelayDeviceVisStatus.setter 
    def strBelayDeviceVisStatus(self, strBelayDeviceVisStatus): 
        # Return true if specified object is of str type
        if not isinstance(strBelayDeviceVisStatus, str): 
            raise TypeError('BelayDevice visual status input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBelayDeviceVisStatus.isspace(): 
            raise ValueError('BelayDevice visual status input cannot be empty') 
        # Set the attribute to the value if true
        elif strBelayDeviceVisStatus.isascii():
            self._strBelayDeviceVisStatus = strBelayDeviceVisStatus

    def Append_BelayDeviceVisIDList(self, intObject):
        """ 
        Function Name: Append_BelayDeviceVisIDList
        Function Description: This function appends objects to the BelayDevice Visual Selection ID list
        """    
        self.aintBelayDeviceVisMetalSelectID.append(intObject)

    def Remove_BelayDeviceVisIDList(self, intObject):
        """ 
        Function Name: Remove_BelayDeviceVisIDList
        Function Description: This function removes objects in the BelayDevice Visual Selection ID list
        """    
        self.aintBelayDeviceVisMetalSelectID.remove(intObject)

    def Get_BelayDeviceVisIDList_Obj(self):
        """ 
        Function Name: Get_BelayDeviceVisIDList_Obj
        Function Description: This function gets all the objects in the BelayDevice Visual Selection ID list
        """    
        return self.aintBelayDeviceVisMetalSelectID

    def Append_BelayDeviceVisSelectList(self, strObject):
        """ 
        Function Name: Append_BelayDeviceVisSelectList
        Function Description: This function appends objects to the BelayDevice Visual Selection list
        """    
        self.astrBelayDeviceVisMetSelect.append(strObject)

    def Remove_BelayDeviceVisSelectList(self, strObject):
        """ 
        Function Name: Remove_BelayDeviceVisSelectList
        Function Description: This function removes objects in the BelayDevice Visual Selection list
        """    
        self.astrBelayDeviceVisMetSelect.remove(strObject)

    def Get_BelayDeviceVisSelectList_Obj(self):
        """ 
        Function Name: Get_BelayDeviceVisSelectList_Obj
        Function Description: This function gets all the objects in the BelayDevice Visual Selection list
        """    
        return self.astrBelayDeviceVisMetSelect   

    def Delete_BelayDeviceVisSelection_Data(self):
        """ 
        Function Name: Delete_BelayDeviceVisSelection_Data
        Function Description: This function removes all the objects in the BelayDevice Visual Selection class
        """    
        BelayDeviceVisSelection.aintBelayDeviceVisMetalSelectID = []
        BelayDeviceVisSelection.astrBelayDeviceVisMetSelect = []

    def Check_BelayDeviceVisSelection_Dup(self):
        """ 
        Function Name: Check_BelayDeviceVisSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        BelayDevice visual selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intBelayDeviceVisMetalSelectID", "strBelayDeviceVisMetSelect")   
        sqlTableName = "TBelayDeviceVisMetalSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strBelayDeviceVisMetSelect in sqlDupValues[i]:
                self.intBelayDeviceVisMetalSelectID = sqlDupValues[i][0]
                self.strBelayDeviceVisMetSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag
                    
    def Add_BelayDeviceVisSelection_Query(self):
        """ 
        Function Name: Add_BelayDeviceVisSelection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewBelayDeviceVisSelection
        """    
        # Create the sql query params
        sqlTableCol = ("intBelayDeviceVisMetalSelectID", "strBelayDeviceVisMetSelect")   
        sqlTableName = "TBelayDeviceVisMetalSelects"
        sqlTableValues = (BelayDeviceVisSelection.intBelayDeviceVisMetalSelectID, BelayDeviceVisSelection.strBelayDeviceVisMetSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)                               

    def Clear_BelayDeviceVisSel_Attributes(self):
        """ 
        Function Name: Clear_BelayDeviceVisSel_Attributes
        Function Description: This function clears the BelayDevice Visual Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intBelayDeviceVisMetalSelectID", "strBelayDeviceVisMetSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None) 


class BelayDevicePlasticVisSelection():
    """
    Class Name: BelayDevicePlasticVisSelection
    Class Description: This class gets and sets all of the BelayDevice Visual Plastic Selections. 
    """
    # Create class variable shared amongst all BelayDevice Plastic visual methods
    aintBelayDeviceVisPlasticSelectID = []
    astrBelayDeviceVisPlastSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intBelayDeviceVisPlasticSelectID, strBelayDeviceVisPlastSelect, strBelayDeviceVisStatus):
        self.intBelayDeviceVisPlasticSelectID = intBelayDeviceVisPlasticSelectID
        self.strBelayDeviceVisPlastSelect = strBelayDeviceVisPlastSelect      
        self.strBelayDeviceVisStatus = strBelayDeviceVisStatus

    # Property decorator object get function to access private intBelayDeviceVisPlasticSelectID
    @property
    def intBelayDeviceVisPlasticSelectID(self):
        return self._intBelayDeviceVisPlasticSelectID

    # Property decorator object get function to access private strBelayDeviceVisPlastSelect
    @property
    def strBelayDeviceVisPlastSelect(self):
        return self._strBelayDeviceVisPlastSelect

    # Property decorator object get function to access private strBelayDeviceVisStatus
    @property
    def strBelayDeviceVisStatus(self):
        return self._strBelayDeviceVisStatus
                
    # setter method 
    @intBelayDeviceVisPlasticSelectID.setter 
    def intBelayDeviceVisPlasticSelectID(self, intBelayDeviceVisPlasticSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intBelayDeviceVisPlasticSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intBelayDeviceVisPlasticSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBelayDeviceVisPlasticSelectID = intBelayDeviceVisPlasticSelectID 
        
    # setter method 
    @strBelayDeviceVisPlastSelect.setter 
    def strBelayDeviceVisPlastSelect(self, strBelayDeviceVisPlastSelect): 
        # Return true if specified object is of str type
        if not isinstance(strBelayDeviceVisPlastSelect, str): 
            raise TypeError('BelayDevice visual input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBelayDeviceVisPlastSelect.isspace(): 
            raise ValueError('BelayDevice visual input cannot be empty') 
        # Set the attribute to the value if true
        elif strBelayDeviceVisPlastSelect.isascii():
            self._strBelayDeviceVisPlastSelect = strBelayDeviceVisPlastSelect

    # setter method 
    @strBelayDeviceVisStatus.setter 
    def strBelayDeviceVisStatus(self, strBelayDeviceVisStatus): 
        # Return true if specified object is of str type
        if not isinstance(strBelayDeviceVisStatus, str): 
            raise TypeError('BelayDevice visual status input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBelayDeviceVisStatus.isspace(): 
            raise ValueError('BelayDevice visual status input cannot be empty') 
        # Set the attribute to the value if true
        elif strBelayDeviceVisStatus.isascii():
            self._strBelayDeviceVisStatus = strBelayDeviceVisStatus

    def Append_BelayDevice_Plastic_VisIDList(self, intObject):
        """ 
        Function Name: Append_BelayDevice_Plastic_VisIDList
        Function Description: This function appends objects to the BelayDevice Visual Plastic Selection ID list
        """    
        self.aintBelayDeviceVisPlasticSelectID.append(intObject)

    def Remove_BelayDevice_Plastic_VisIDList(self, intObject):
        """ 
        Function Name: Remove_BelayDevice_Plastic_VisIDList
        Function Description: This function removes objects in the BelayDevice Visual Plastic Selection ID list
        """    
        self.aintBelayDeviceVisPlasticSelectID.remove(intObject)

    def Get_BelayDevice_Plastic_VisIDList_Obj(self):
        """ 
        Function Name: Get_BelayDevice_Plastic_VisIDList_Obj
        Function Description: This function gets all the objects in the BelayDevice Visual Plastic Selection ID list
        """    
        return self.aintBelayDeviceVisPlasticSelectID

    def Append_BelayDevice_Plastic_VisSelectList(self, strObject):
        """ 
        Function Name: Append_BelayDevice_Plastic_VisSelectList
        Function Description: This function appends objects to the BelayDevice Visual Selection list
        """    
        self.astrBelayDeviceVisPlastSelect.append(strObject)

    def Remove_BelayDevice_Plastic_VisSelectList(self, strObject):
        """ 
        Function Name: Remove_BelayDevice_Plastic_VisSelectList
        Function Description: This function removes objects in the BelayDevice Visual Selection list
        """    
        self.astrBelayDeviceVisPlastSelect.remove(strObject)

    def Get_BelayDevice_Plastic_VisSelectList_Obj(self):
        """ 
        Function Name: Get_BelayDevice_Plastic_VisSelectList_Obj
        Function Description: This function gets all the objects in the BelayDevice Visual Selection list
        """    
        return self.astrBelayDeviceVisPlastSelect  
                        
    def Delete_BelayDevice_Plastic_VisSelection_Data(self):
        """ 
        Function Name: Delete_BelayDevice_Plastic_VisSelection_Data
        Function Description: This function removes all the objects in the BelayDevice Visual Selection class
        """    
        BelayDevicePlasticVisSelection.aintBelayDeviceVisPlasticSelectID = []
        BelayDevicePlasticVisSelection.astrBelayDeviceVisPlastSelect = []

    def Check_BelayDevice_Plastic_VisSelection_Dup(self):
        """ 
        Function Name: Check_BelayDevice_Plastic_VisSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        BelayDevice visual Plastic selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intBelayDeviceVisPlasticSelectID", "strBelayDeviceVisPlastSelect")   
        sqlTableName = "TBelayDeviceVisPlasticSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strBelayDeviceVisPlastSelect in sqlDupValues[i]:
                self.intBelayDeviceVisPlasticSelectID = sqlDupValues[i][0]
                self.strBelayDeviceVisPlastSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag
                                                
    def Add_BelayDeviceVis_Plastic_Selection_Query(self):
        """ 
        Function Name: Add_BelayDeviceVis_Plastic_Selection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Create the sql query params
        sqlTableCol = ("intBelayDeviceVisPlasticSelectID", "strBelayDeviceVisPlastSelect")   
        sqlTableName = "TBelayDeviceVisPlasticSelects"
        sqlTableValues = (BelayDevicePlasticVisSelection.intBelayDeviceVisPlasticSelectID, BelayDevicePlasticVisSelection.strBelayDeviceVisPlastSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)  

    def Clear_BelayDevice_Plastic_VisSel_Attributes(self):
        """ 
        Function Name: Clear_BelayDevice_Plastic_VisSel_Attributes
        Function Description: This function clears the BelayDevice Visual Plastic Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intBelayDeviceVisPlasticSelectID", "strBelayDeviceVisPlastSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None) 
                
                
class BelayDeviceVisualInspect(BelayDevices, InspectionType, BelayDeviceVisSelection, BelayDevicePlasticVisSelection, InspectionStatus):
    """
    Class Name: BelayDeviceVisualInspect
    Class Description: This class gets and sets all of the BelayDevice Visual Inspection attributes. 
    """
    # Create class variable shared amongst all BelayDevice Visual Inspection methods
    aintBelayDeviceVisualInspectionIDCache = []
    aBelayDeviceVisualInspectionCache = []
        
    # Instantiate the following attributes
    def __init__(self, intBelayDeviceVisualInspectionID, intBelayDeviceID, intInspectionTypeID, intBelayDeviceVisMetalSelectID, 
                intBelayDeviceVisPlasticSelectID, intInspectionStatusID):
        self.intBelayDeviceVisualInspectionID = intBelayDeviceVisualInspectionID
        # Inherits the child class with all the necessary objects
        BelayDevices.__init__(intBelayDeviceID)
        InspectionType.__init__(intInspectionTypeID)
        BelayDeviceVisSelection.__init__(intBelayDeviceVisMetalSelectID)
        BelayDevicePlasticVisSelection.__init__(intBelayDeviceVisPlasticSelectID)
        InspectionStatus.__init__(intInspectionStatusID)
        
    # Property decorator object get function to access private intBelayDeviceVisualInspectionID
    @property
    def intBelayDeviceVisualInspectionID(self):
        return self._intBelayDeviceVisualInspectionID

    # setter method 
    @intBelayDeviceVisualInspectionID.setter 
    def intBelayDeviceVisualInspectionID(self, intBelayDeviceVisualInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intBelayDeviceVisualInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the BelayDevice Visual Inspection ID to value
        if intBelayDeviceVisualInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBelayDeviceVisualInspectionID = intBelayDeviceVisualInspectionID 

    def Append_BelayDeviceVisualIDList(self, intObject):
        """ 
        Function Name: Append_BelayDeviceVisualIDList
        Function Description: This function appends objects to the BelayDevice Visual Inspection ID list
        """    
        self.aintBelayDeviceVisualInspectionIDCache.append(intObject)

    def Remove_BelayDeviceVisualIDList(self, intObject):
        """ 
        Function Name: Remove_BelayDeviceVisualIDList
        Function Description: This function removes objects in the BelayDevice Visual Inspection ID list
        """    
        self.aintBelayDeviceVisualInspectionIDCache.remove(intObject)

    def Get_BelayDeviceVisualIDList_Obj(self):
        """ 
        Function Name: Get_BelayDeviceVisualIDList_Obj
        Function Description: This function gets all the objects in the BelayDevice Visual Inspection ID list
        """    
        return self.aintBelayDeviceVisualInspectionIDCache
                
    def Delete_BelayDeviceVisualInspect_Data(self):
        """ 
        Function Name: Delete_BelayDeviceVisualInspect_Data
        Function Description: This function removes all the objects in the BelayDevice Visual Inspection ID class
        """    
        BelayDeviceVisualInspect.aintBelayDeviceVisualInspectionIDCache = []
        BelayDeviceVisualInspect.aBelayDeviceVisualInspectionCache = []

    def Set_BelayDeviceVisualInspect_Data(self):
        """ 
        Function Name: Set_BelayDeviceVisualInspect_Data
        Function Description: This function sets all the objects in the BelayDevice Visual Inspection class
        """    
        self.intBelayDeviceVisualInspectionID = BelayDeviceVisualInspect.aBelayDeviceVisualInspectionCache[0]
        self.intBelayDeviceID = BelayDeviceVisualInspect.aBelayDeviceVisualInspectionCache[1]
        self.intInspectionTypeID = BelayDeviceVisualInspect.aBelayDeviceVisualInspectionCache[2]
        self.intBelayDeviceVisMetalSelectID = BelayDeviceVisualInspect.aBelayDeviceVisualInspectionCache[3]
        self.intBelayDeviceVisPlasticSelectID = BelayDeviceVisualInspect.aBelayDeviceVisualInspectionCache[4]
        self.intInspectionStatusID = BelayDeviceVisualInspect.aBelayDeviceVisualInspectionCache[5]
        
    def Add_BelayDeviceVisualInspect_Query(self):
        """ 
        Function Name: Add_BelayDeviceVisualInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewBelayDeviceVisualInspection
        """    
        # Set the class variables before dumping the data to the database
        BelayDeviceVisualInspect.Set_BelayDeviceVisualInspect_Data(self)
        
        # Create the sql query string       
        sqlTableCol = ("intBelayDeviceVisualInspectionID", "intBelayDeviceID", "intInspectionTypeID", "intBelayDeviceVisMetalSelectID", 
                    "intBelayDeviceVisPlasticSelectID", "intInspectionStatusID")     
        sqlTableName = "TBelayDeviceVisualInspections"
        sqlTableValues = (self.intBelayDeviceVisualInspectionID, self.intBelayDeviceID, self.intInspectionTypeID, self.intBelayDeviceVisMetalSelectID,
                        self.intBelayDeviceVisPlasticSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)           

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)         
                                
    def Clear_BelayDeviceVisInspect_Attributes(self):
        """ 
        Function Name: Clear_BelayDeviceVisInspect_Attributes
        Function Description: This function clears the BelayDevice Visual Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intBelayDeviceVisualInspectionID", "intBelayDeviceID", "intInspectionTypeID", "intBelayDeviceVisMetalSelectID",
                        "intBelayDeviceVisPlasticSelectID", "intInspectionStatusID")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            
            
class BelayDevicePhysSelection():
    """
    Class Name: BelayDevicePhysSelection
    Class Description: This class gets and sets all of the BelayDevice Physical Selections. 
    """
    # Create class variable shared amongst all BelayDevice physical methods
    aintBelayDevicePhysMetalSelectID = []
    astrBelayDevicePhysMetSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intBelayDevicePhysMetalSelectID, strBelayDevicePhysMetSelect, strBelayDevicePhysStatus):
        self.intBelayDevicePhysMetalSelectID = intBelayDevicePhysMetalSelectID
        self.strBelayDevicePhysMetSelect = strBelayDevicePhysMetSelect
        self.strBelayDevicePhysStatus = strBelayDevicePhysStatus

    # Property decorator object get function to access private intBelayDevicePhysMetalSelectID
    @property
    def intBelayDevicePhysMetalSelectID(self):
        return self._intBelayDevicePhysMetalSelectID

    # Property decorator object get function to access private strBelayDevicePhysMetSelect
    @property
    def strBelayDevicePhysMetSelect(self):
        return self._strBelayDevicePhysMetSelect
        
    # Property decorator object get function to access private strBelayDevicePhysStatus
    @property
    def strBelayDevicePhysStatus(self):
        return self._strBelayDevicePhysStatus
                
    # setter method 
    @intBelayDevicePhysMetalSelectID.setter 
    def intBelayDevicePhysMetalSelectID(self, intBelayDevicePhysMetalSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intBelayDevicePhysMetalSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intBelayDevicePhysMetalSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBelayDevicePhysMetalSelectID = intBelayDevicePhysMetalSelectID 
        
    # setter method 
    @strBelayDevicePhysMetSelect.setter 
    def strBelayDevicePhysMetSelect(self, strBelayDevicePhysMetSelect): 
        # Return true if specified object is of str type
        if not isinstance(strBelayDevicePhysMetSelect, str): 
            raise TypeError('BelayDevice physical input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBelayDevicePhysMetSelect.isspace(): 
            raise ValueError('BelayDevice physical input cannot be empty') 
        # Set the attribute to the value if true
        elif strBelayDevicePhysMetSelect.isascii():
            self._strBelayDevicePhysMetSelect = strBelayDevicePhysMetSelect

    # setter method 
    @strBelayDevicePhysStatus.setter 
    def strBelayDevicePhysStatus(self, strBelayDevicePhysStatus): 
        # Return true if specified object is of str type
        if not isinstance(strBelayDevicePhysStatus, str): 
            raise TypeError('BelayDevice physical status input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBelayDevicePhysStatus.isspace(): 
            raise ValueError('BelayDevice physical status input cannot be empty') 
        # Set the attribute to the value if true
        elif strBelayDevicePhysStatus.isascii():
            self._strBelayDevicePhysStatus = strBelayDevicePhysStatus

    def Append_BelayDevicePhysIDList(self, intObject):
        """ 
        Function Name: Append_BelayDevicePhysIDList
        Function Description: This function appends objects to the BelayDevice Physical Selection ID list
        """    
        self.aintBelayDevicePhysMetalSelectID.append(intObject)

    def Remove_BelayDevicePhysIDList(self, intObject):
        """ 
        Function Name: Remove_BelayDevicePhysIDList
        Function Description: This function removes objects in the BelayDevice Physical Selection ID list
        """    
        self.aintBelayDevicePhysMetalSelectID.remove(intObject)

    def Get_BelayDevicePhysIDList_Obj(self):
        """ 
        Function Name: Get_BelayDevicePhysIDList_Obj
        Function Description: This function gets all the objects in the BelayDevice Physical Selection ID list
        """    
        return self.aintBelayDevicePhysMetalSelectID
    
    def Append_BelayDevicePhysSelectList(self, strObject):
        """ 
        Function Name: Append_BelayDevicePhysSelectList
        Function Description: This function appends objects to the BelayDevice Physical Selection list
        """    
        self.astrBelayDevicePhysMetSelect.append(strObject)

    def Remove_BelayDevicePhysSelectList(self, strObject):
        """ 
        Function Name: Remove_BelayDevicePhysSelectList
        Function Description: This function removes objects in the BelayDevice Physical Selection list
        """    
        self.astrBelayDevicePhysMetSelect.remove(strObject)

    def Get_BelayDevicePhysSelectList_Obj(self):
        """ 
        Function Name: Get_BelayDevicePhysSelectList_Obj
        Function Description: This function gets all the objects in the BelayDevice Physical Selection list
        """    
        return self.astrBelayDevicePhysMetSelect   
                    
    def Delete_BelayDevicePhysSelection_Data(self):
        """ 
        Function Name: Delete_BelayDevicePhysSelection_Data
        Function Description: This function removes all the objects in the BelayDevice Physical Selection class
        """    
        BelayDevicePhysSelection.aintBelayDevicePhysMetalSelectID = []
        BelayDevicePhysSelection.astrBelayDevicePhysMetSelect = []

    def Check_BelayDevicePhysSelection_Dup(self):
        """ 
        Function Name: Check_BelayDevicePhysSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        BelayDevice physical selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intBelayDevicePhysMetalSelectID", "strBelayDevicePhysMetSelect")   
        sqlTableName = "TBelayDevicePhysMetalSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strBelayDevicePhysMetSelect in sqlDupValues[i]:
                self.intBelayDevicePhysMetalSelectID = sqlDupValues[i][0]
                self.strBelayDevicePhysMetSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag
            
    def Add_BelayDevicePhysSelection_Query(self):
        """ 
        Function Name: Add_BelayDevicePhysSelection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewBelayDevicePhysSelection
        """    
        # Create the sql query string
        sqlTableCol = ("intBelayDevicePhysMetalSelectID", "strBelayDevicePhysMetSelect")   
        sqlTableName = "TBelayDevicePhysMetalSelects"
        sqlTableValues = (BelayDevicePhysSelection.intBelayDevicePhysMetalSelectID, BelayDevicePhysSelection.strBelayDevicePhysMetSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams) 
        
    def Clear_BelayDevicePhysSel_Attributes(self):
        """ 
        Function Name: Clear_BelayDevicePhysSel_Attributes
        Function Description: This function clears the BelayDevice Physical Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intBelayDevicePhysMetalSelectID", "strBelayDevicePhysMetSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            

class BelayDevicePlasticPhysSelection():
    """
    Class Name: BelayDevicePlasticPhysSelection
    Class Description: This class gets and sets all of the BelayDevice Physical Plastic Selections. 
    """
    # Create class variable shared amongst all BelayDevice Plastic Physical methods
    aintBelayDevicePhysPlasticSelectID = []
    astrBelayDevicePhysPlastSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intBelayDevicePhysPlasticSelectID, strBelayDevicePhysPlastSelect, strBelayDevicePhysStatus):
        self.intBelayDevicePhysPlasticSelectID = intBelayDevicePhysPlasticSelectID
        self.strBelayDevicePhysPlastSelect = strBelayDevicePhysPlastSelect      
        self.strBelayDevicePhysStatus = strBelayDevicePhysStatus

    # Property decorator object get function to access private intBelayDevicePhysPlasticSelectID
    @property
    def intBelayDevicePhysPlasticSelectID(self):
        return self._intBelayDevicePhysPlasticSelectID

    # Property decorator object get function to access private strBelayDevicePhysPlastSelect
    @property
    def strBelayDevicePhysPlastSelect(self):
        return self._strBelayDevicePhysPlastSelect

    # Property decorator object get function to access private strBelayDevicePhysStatus
    @property
    def strBelayDevicePhysStatus(self):
        return self._strBelayDevicePhysStatus
                
    # setter method 
    @intBelayDevicePhysPlasticSelectID.setter 
    def intBelayDevicePhysPlasticSelectID(self, intBelayDevicePhysPlasticSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intBelayDevicePhysPlasticSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intBelayDevicePhysPlasticSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBelayDevicePhysPlasticSelectID = intBelayDevicePhysPlasticSelectID 
        
    # setter method 
    @strBelayDevicePhysPlastSelect.setter 
    def strBelayDevicePhysPlastSelect(self, strBelayDevicePhysPlastSelect): 
        # Return true if specified object is of str type
        if not isinstance(strBelayDevicePhysPlastSelect, str): 
            raise TypeError('BelayDevice Physical input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBelayDevicePhysPlastSelect.isspace(): 
            raise ValueError('BelayDevice Physical input cannot be empty') 
        # Set the attribute to the value if true
        elif strBelayDevicePhysPlastSelect.isascii():
            self._strBelayDevicePhysPlastSelect = strBelayDevicePhysPlastSelect

    # setter method 
    @strBelayDevicePhysStatus.setter 
    def strBelayDevicePhysStatus(self, strBelayDevicePhysStatus): 
        # Return true if specified object is of str type
        if not isinstance(strBelayDevicePhysStatus, str): 
            raise TypeError('BelayDevice Physical status input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBelayDevicePhysStatus.isspace(): 
            raise ValueError('BelayDevice Physical status input cannot be empty') 
        # Set the attribute to the value if true
        elif strBelayDevicePhysStatus.isascii():
            self._strBelayDevicePhysStatus = strBelayDevicePhysStatus

    def Append_BelayDevice_Plastic_PhysIDList(self, intObject):
        """ 
        Function Name: Append_BelayDevice_Plastic_PhysIDList
        Function Description: This function appends objects to the BelayDevice Physical Plastic Selection ID list
        """    
        self.aintBelayDevicePhysPlasticSelectID.append(intObject)

    def Remove_BelayDevice_Plastic_PhysIDList(self, intObject):
        """ 
        Function Name: Remove_BelayDevice_Plastic_PhysIDList
        Function Description: This function removes objects in the BelayDevice Physical Plastic Selection ID list
        """    
        self.aintBelayDevicePhysPlasticSelectID.remove(intObject)

    def Get_BelayDevice_Plastic_PhysIDList_Obj(self):
        """ 
        Function Name: Get_BelayDevice_Plastic_PhysIDList_Obj
        Function Description: This function gets all the objects in the BelayDevice Physical Plastic Selection ID list
        """    
        return self.aintBelayDevicePhysPlasticSelectID

    def Append_BelayDevice_Plastic_PhysSelectList(self, strObject):
        """ 
        Function Name: Append_BelayDevice_Plastic_PhysSelectList
        Function Description: This function appends objects to the BelayDevice Physical Selection list
        """    
        self.astrBelayDevicePhysPlastSelect.append(strObject)

    def Remove_BelayDevice_Plastic_PhysSelectList(self, strObject):
        """ 
        Function Name: Remove_BelayDevice_Plastic_PhysSelectList
        Function Description: This function removes objects in the BelayDevice Physical Selection list
        """    
        self.astrBelayDevicePhysPlastSelect.remove(strObject)

    def Get_BelayDevice_Plastic_PhysSelectList_Obj(self):
        """ 
        Function Name: Get_BelayDevice_Plastic_PhysSelectList_Obj
        Function Description: This function gets all the objects in the BelayDevice Physical Selection list
        """    
        return self.astrBelayDevicePhysPlastSelect  
                        
    def Delete_BelayDevice_Plastic_PhysSelection_Data(self):
        """ 
        Function Name: Delete_BelayDevice_Plastic_PhysSelection_Data
        Function Description: This function removes all the objects in the BelayDevice Physical Selection class
        """    
        BelayDevicePlasticPhysSelection.aintBelayDevicePhysPlasticSelectID = []
        BelayDevicePlasticPhysSelection.astrBelayDevicePhysPlastSelect = []

    def Check_BelayDevice_Plastic_PhysSelection_Dup(self):
        """ 
        Function Name: Check_BelayDevice_Plastic_PhysSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        BelayDevice Physical Plastic selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intBelayDevicePhysPlasticSelectID", "strBelayDevicePhysPlastSelect")   
        sqlTableName = "TBelayDevicePhysPlasticSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strBelayDevicePhysPlastSelect in sqlDupValues[i]:
                self.intBelayDevicePhysPlasticSelectID = sqlDupValues[i][0]
                self.strBelayDevicePhysPlastSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag
                                                
    def Add_BelayDevicePhys_Plastic_Selection_Query(self):
        """ 
        Function Name: Add_BelayDevicePhys_Plastic_Selection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure 
        """    
        # Create the sql query params
        sqlTableCol = ("intBelayDevicePhysPlasticSelectID", "strBelayDevicePhysPlastSelect")   
        sqlTableName = "TBelayDevicePhysPlasticSelects"
        sqlTableValues = (BelayDevicePlasticPhysSelection.intBelayDevicePhysPlasticSelectID, BelayDevicePlasticPhysSelection.strBelayDevicePhysPlastSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)  

    def Clear_BelayDevice_Plastic_PhysSel_Attributes(self):
        """ 
        Function Name: Clear_BelayDevice_Plastic_PhysSel_Attributes
        Function Description: This function clears the BelayDevice Physical Plastic Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intBelayDevicePhysPlasticSelectID", "strBelayDevicePhysPlastSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None) 
                
                                    
class BelayDevicePhysicalInspect(BelayDevices, InspectionType, BelayDevicePhysSelection, BelayDevicePlasticPhysSelection, InspectionStatus):
    """
    Class Name: BelayDevicePhysicalInspect
    Class Description: This class gets and sets all of the BelayDevice Physical Inspection  attributes. 
    """
    # Create class variable shared amongst all BelayDevice Physical Inspection methods
    aintBelayDevicePhysicalInspectionID = []
    aBelayDevicePhysicalCache = []
        
    # Instantiate the following attributes
    def __init__(self, intBelayDevicePhysicalInspectionID, intBelayDeviceID, intInspectionTypeID, intBelayDevicePhysMetalSelectID, 
                intBelayDevicePhysPlasticSelectID, intInspectionStatusID):
        self.intBelayDevicePhysicalInspectionID = intBelayDevicePhysicalInspectionID
        # Inherits the child class with all the necessary objects
        BelayDevices.__init__(intBelayDeviceID)
        InspectionType.__init__(intInspectionTypeID)
        BelayDevicePhysSelection.__init__(intBelayDevicePhysMetalSelectID)
        BelayDevicePlasticPhysSelection.__init__(intBelayDevicePhysPlasticSelectID)
        InspectionStatus.__init__(intInspectionStatusID)
        
    # Property decorator object get function to access private intBelayDevicePhysicalInspectionID
    @property
    def intBelayDevicePhysicalInspectionID(self):
        return self._intBelayDevicePhysicalInspectionID

    # setter method 
    @intBelayDevicePhysicalInspectionID.setter 
    def intBelayDevicePhysicalInspectionID(self, intBelayDevicePhysicalInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intBelayDevicePhysicalInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the BelayDevice Physical Inspection ID to value
        if intBelayDevicePhysicalInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBelayDevicePhysicalInspectionID = intBelayDevicePhysicalInspectionID 

    def Append_BelayDevicePhysicalIDList(self, intObject):
        """ 
        Function Name: Append_BelayDevicePhysicalIDList
        Function Description: This function appends objects to the BelayDevice Physical Inspection ID list
        """    
        self.aintBelayDevicePhysicalInspectionID.append(intObject)

    def Remove_BelayDevicePhysicalIDList(self, intObject):
        """ 
        Function Name: Remove_BelayDevicePhysicalIDList
        Function Description: This function removes objects in the BelayDevice Physical Inspection ID list
        """    
        self.aintBelayDevicePhysicalInspectionID.remove(intObject)

    def Get_BelayDevicePhysicalIDList_Obj(self):
        """ 
        Function Name: Get_BelayDevicePhysicalIDList_Obj
        Function Description: This function gets all the objects in the BelayDevice Physical Inspection ID list
        """    
        return self.aintBelayDevicePhysicalInspectionID
                
    def Delete_BelayDevicePhysicalInspect_Data(self):
        """ 
        Function Name: Delete_BelayDevicePhysicalInspect_Data
        Function Description: This function removes all the objects in the BelayDevice Physical Inspection ID class
        """    
        BelayDevicePhysicalInspect.aintBelayDevicePhysicalInspectionID = []
        BelayDevicePhysicalInspect.aBelayDevicePhysicalCache = []

    def Set_BelayDevicePhysicalInspect_Data(self):
        """ 
        Function Name: Set_BelayDeviceVisualInspect_Data
        Function Description: This function sets all the objects in the BelayDevice Physical Inspection class
        """    
        self.intBelayDevicePhysicalInspectionID = BelayDevicePhysicalInspect.aBelayDevicePhysicalCache[0]
        self.intBelayDeviceID = BelayDevicePhysicalInspect.aBelayDevicePhysicalCache[1]
        self.intInspectionTypeID = BelayDevicePhysicalInspect.aBelayDevicePhysicalCache[2]
        self.intBelayDevicePhysMetalSelectID = BelayDevicePhysicalInspect.aBelayDevicePhysicalCache[3]
        self.intBelayDevicePhysPlasticSelectID = BelayDevicePhysicalInspect.aBelayDevicePhysicalCache[4]
        self.intInspectionStatusID = BelayDevicePhysicalInspect.aBelayDevicePhysicalCache[5]
                
    def Add_BelayDevicePhysicalInspect_Query(self):
        """ 
        Function Name: Add_BelayDevicePhysicalInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewBelayDevicePhysicalInspection
        """    
        # Set the class variables before dumping the data to the database
        BelayDevicePhysicalInspect.Set_BelayDevicePhysicalInspect_Data(self)
                
        # Create the sql query string
        sqlTableCol = ("intBelayDevicePhysicalInspectionID", "intBelayDeviceID", "intInspectionTypeID", "intBelayDevicePhysMetalSelectID", 
                    "intBelayDevicePhysPlasticSelectID", "intInspectionStatusID")     
        sqlTableName = "TBelayDevicePhysicalInspections"
        sqlTableValues = (self.intBelayDevicePhysicalInspectionID, self.intBelayDeviceID, self.intInspectionTypeID, self.intBelayDevicePhysMetalSelectID, 
                        self.intBelayDevicePhysPlasticSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)           

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)       

    def Clear_BelayDevicePhysInspect_Attributes(self):
        """ 
        Function Name: Clear_BelayDevicePhysInspect_Attributes
        Function Description: This function clears the BelayDevice Physical Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intBelayDevicePhysicalInspectionID", "intBelayDeviceID", "intInspectionTypeID", "intBelayDevicePhysMetalSelectID", 
                        "intBelayDevicePhysPlasticSelectID", "intInspectionStatusID")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                    

class BelayDeviceFunctSelection():
    """
    Class Name: BelayDeviceFunctSelection
    Class Description: This class gets and sets all of the BelayDevice Function Selections. 
    """
    # Create class variable shared amongst all BelayDevice Function methods
    aintBelayDeviceFunctSelectID = []
    astrBelayDeviceFunctSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intBelayDeviceFunctSelectID, strBelayDeviceFunctSelect, strBelayDeviceFunctStatus):
        self.intBelayDeviceFunctSelectID = intBelayDeviceFunctSelectID
        self.strBelayDeviceFunctSelect = strBelayDeviceFunctSelect
        self.strBelayDeviceFunctStatus = strBelayDeviceFunctStatus

    # Property decorator object get function to access private intBelayDeviceFunctSelectID
    @property
    def intBelayDeviceFunctSelectID(self):
        return self._intBelayDeviceFunctSelectID

    # Property decorator object get function to access private strBelayDeviceFunctSelect
    @property
    def strBelayDeviceFunctSelect(self):
        return self._strBelayDeviceFunctSelect

    # Property decorator object get function to access private strBelayDeviceFunctStatus
    @property
    def strBelayDeviceFunctStatus(self):
        return self._strBelayDeviceFunctStatus

    # setter method 
    @intBelayDeviceFunctSelectID.setter 
    def intBelayDeviceFunctSelectID(self, intBelayDeviceFunctSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intBelayDeviceFunctSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intBelayDeviceFunctSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBelayDeviceFunctSelectID = intBelayDeviceFunctSelectID 
        
    # setter method 
    @strBelayDeviceFunctSelect.setter 
    def strBelayDeviceFunctSelect(self, strBelayDeviceFunctSelect): 
        # Return true if specified object is of str type
        if not isinstance(strBelayDeviceFunctSelect, str): 
            raise TypeError('BelayDevice function input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBelayDeviceFunctSelect.isspace(): 
            raise ValueError('BelayDevice function input cannot be empty') 
        # Set the attribute to the value if true
        elif strBelayDeviceFunctSelect.isascii():
            self._strBelayDeviceFunctSelect = strBelayDeviceFunctSelect

    # setter method 
    @strBelayDeviceFunctStatus.setter 
    def strBelayDeviceFunctStatus(self, strBelayDeviceFunctStatus): 
        # Return true if specified object is of str type
        if not isinstance(strBelayDeviceFunctStatus, str): 
            raise TypeError('BelayDevice function status input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBelayDeviceFunctStatus.isspace(): 
            raise ValueError('BelayDevice function status input cannot be empty') 
        # Set the attribute to the value if true
        elif strBelayDeviceFunctStatus.isascii():
            self._strBelayDeviceFunctStatus = strBelayDeviceFunctStatus

    def Append_BelayDeviceFunctIDList(self, intObject):
        """ 
        Function Name: Append_BelayDeviceFunctIDList
        Function Description: This function appends objects to the BelayDevice Function Selection ID list
        """    
        self.aintBelayDeviceFunctSelectID.append(intObject)

    def Remove_BelayDeviceFunctIDList(self, intObject):
        """ 
        Function Name: Remove_BelayDeviceFunctIDList
        Function Description: This function removes objects in the BelayDevice Function Selection ID list
        """    
        self.aintBelayDeviceFunctSelectID.remove(intObject)

    def Get_BelayDeviceFunctIDList_Obj(self):
        """ 
        Function Name: Get_BelayDeviceFunctIDList_Obj
        Function Description: This function gets all the objects in the BelayDevice Function Selection ID list
        """    
        return self.aintBelayDeviceFunctSelectID
    
    def Append_BelayDeviceFunctSelectList(self, strObject):
        """ 
        Function Name: Append_BelayDeviceFunctSelectList
        Function Description: This function appends objects to the BelayDevice Function Selection list
        """    
        self.astrBelayDeviceFunctSelect.append(strObject)

    def Remove_BelayDeviceFunctSelectList(self, strObject):
        """ 
        Function Name: Remove_BelayDeviceFunctSelectList
        Function Description: This function removes objects in the BelayDevice Function Selection list
        """    
        self.astrBelayDeviceFunctSelect.remove(strObject)

    def Get_BelayDeviceFunctSelectList_Obj(self):
        """ 
        Function Name: Get_BelayDeviceFunctSelectList_Obj
        Function Description: This function gets all the objects in the BelayDevice Function Selection list
        """    
        return self.astrBelayDeviceFunctSelect   
                    
    def Delete_BelayDeviceFunctSelection_Data(self):
        """ 
        Function Name: Delete_BelayDeviceFunctSelection_Data
        Function Description: This function removes all the objects in the BelayDevice Function Selection class
        """    
        BelayDeviceFunctSelection.aintBelayDeviceFunctSelectID = []
        BelayDeviceFunctSelection.astrBelayDeviceFunctSelect = []

    def Check_BelayDeviceFunctSelection_Dup(self):
        """ 
        Function Name: Check_BelayDeviceFunctSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        BelayDevice function selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intBelayDeviceFunctSelectID", "strBelayDeviceFunctSelect")   
        sqlTableName = "TBelayDeviceFunctSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strBelayDeviceFunctSelect in sqlDupValues[i]:
                self.intBelayDeviceFunctSelectID = sqlDupValues[i][0]
                self.strBelayDeviceFunctSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag
            
    def Add_BelayDeviceFunctSelection_Query(self):
        """ 
        Function Name: Add_BelayDeviceFunctSelection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewBelayDeviceFunctSelection
        """    
        # Create the sql query string
        sqlTableCol = ("intBelayDeviceFunctSelectID", "strBelayDeviceFunctSelect")   
        sqlTableName = "TBelayDeviceFunctSelects"
        sqlTableValues = (BelayDeviceFunctSelection.intBelayDeviceFunctSelectID, BelayDeviceFunctSelection.strBelayDeviceFunctSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)                            

    def Clear_BelayDeviceFuncSel_Attributes(self):
        """ 
        Function Name: Clear_BelayDeviceFuncSel_Attributes
        Function Description: This function clears the BelayDevice Function Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intBelayDeviceFunctSelectID", "strBelayDeviceFunctSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None) 
                    

class BelayDevicePlasticFunctSelection():
    """
    Class Name: BelayDevicePlasticFunctSelection
    Class Description: This class gets and sets all of the BelayDevice Plastic Function Selections. 
    """
    # Create class variable shared amongst all BelayDevice Function methods
    aintBelayDevicePlasticFunctSelectID = []
    astrBelayDevicePlasticFunctSelect = []
        
    # Instantiate the following attributes
    def __init__(self, intBelayDeviceFunctPlastSelectID, strBelayDeviceFunctPlastSelect, strBelayDeviceFunctStatus):
        self.intBelayDeviceFunctPlastSelectID = intBelayDeviceFunctPlastSelectID
        self.strBelayDeviceFunctPlastSelect = strBelayDeviceFunctPlastSelect
        self.strBelayDeviceFunctStatus = strBelayDeviceFunctStatus

    # Property decorator object get function to access private intBelayDeviceFunctPlastSelectID
    @property
    def intBelayDeviceFunctPlastSelectID(self):
        return self._intBelayDeviceFunctPlastSelectID

    # Property decorator object get function to access private strBelayDeviceFunctPlastSelect
    @property
    def strBelayDeviceFunctPlastSelect(self):
        return self._strBelayDeviceFunctPlastSelect

    # Property decorator object get function to access private strBelayDeviceFunctStatus
    @property
    def strBelayDeviceFunctStatus(self):
        return self._strBelayDeviceFunctStatus

    # setter method 
    @intBelayDeviceFunctPlastSelectID.setter 
    def intBelayDeviceFunctPlastSelectID(self, intBelayDeviceFunctPlastSelectID): 
        # Return true if specified object is of int type
        if not isinstance(intBelayDeviceFunctPlastSelectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intBelayDeviceFunctPlastSelectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBelayDeviceFunctPlastSelectID = intBelayDeviceFunctPlastSelectID 
        
    # setter method 
    @strBelayDeviceFunctPlastSelect.setter 
    def strBelayDeviceFunctPlastSelect(self, strBelayDeviceFunctPlastSelect): 
        # Return true if specified object is of str type
        if not isinstance(strBelayDeviceFunctPlastSelect, str): 
            raise TypeError('BelayDevice function input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBelayDeviceFunctPlastSelect.isspace(): 
            raise ValueError('BelayDevice function input cannot be empty') 
        # Set the attribute to the value if true
        elif strBelayDeviceFunctPlastSelect.isascii():
            self._strBelayDeviceFunctPlastSelect = strBelayDeviceFunctPlastSelect

    # setter method 
    @strBelayDeviceFunctStatus.setter 
    def strBelayDeviceFunctStatus(self, strBelayDeviceFunctStatus): 
        # Return true if specified object is of str type
        if not isinstance(strBelayDeviceFunctStatus, str): 
            raise TypeError('BelayDevice function status input must be a string') 
        # Check if the value is empty, otherwise check if the value is ascii 
        if strBelayDeviceFunctStatus.isspace(): 
            raise ValueError('BelayDevice function status input cannot be empty') 
        # Set the attribute to the value if true
        elif strBelayDeviceFunctStatus.isascii():
            self._strBelayDeviceFunctStatus = strBelayDeviceFunctStatus

    def Append_BelayDeviceFunctIDList(self, intObject):
        """ 
        Function Name: Append_BelayDeviceFunctIDList
        Function Description: This function appends objects to the BelayDevice Function Selection ID list
        """    
        self.aintBelayDevicePlasticFunctSelectID.append(intObject)

    def Remove_BelayDeviceFunctIDList(self, intObject):
        """ 
        Function Name: Remove_BelayDeviceFunctIDList
        Function Description: This function removes objects in the BelayDevice Function Selection ID list
        """    
        self.aintBelayDevicePlasticFunctSelectID.remove(intObject)

    def Get_BelayDeviceFunctIDList_Obj(self):
        """ 
        Function Name: Get_BelayDeviceFunctIDList_Obj
        Function Description: This function gets all the objects in the BelayDevice Function Selection ID list
        """    
        return self.aintBelayDevicePlasticFunctSelectID
    
    def Append_BelayDeviceFunctSelectList(self, strObject):
        """ 
        Function Name: Append_BelayDeviceFunctSelectList
        Function Description: This function appends objects to the BelayDevice Function Selection list
        """    
        self.astrBelayDevicePlasticFunctSelect.append(strObject)

    def Remove_BelayDeviceFunctSelectList(self, strObject):
        """ 
        Function Name: Remove_BelayDeviceFunctSelectList
        Function Description: This function removes objects in the BelayDevice Function Selection list
        """    
        self.astrBelayDevicePlasticFunctSelect.remove(strObject)

    def Get_BelayDeviceFunctSelectList_Obj(self):
        """ 
        Function Name: Get_BelayDeviceFunctSelectList_Obj
        Function Description: This function gets all the objects in the BelayDevice Function Selection list
        """    
        return self.astrBelayDevicePlasticFunctSelect   
                    
    def Delete_BelayDevicePlasticFunctSelection_Data(self):
        """ 
        Function Name: Delete_BelayDevicePlasticFunctSelection_Data
        Function Description: This function removes all the objects in the BelayDevice Function Selection class
        """    
        BelayDevicePlasticFunctSelection.aintBelayDevicePlasticFunctSelectID = []
        BelayDevicePlasticFunctSelection.astrBelayDevicePlasticFunctSelect = []

    def Check_BelayDevicePlasticFunctSelection_Dup(self):
        """ 
        Function Name: Check_BelayDevicePlasticFunctSelection_Dup
        Function Description: This function checks the database for any duplicates in the columns/rows for the 
        BelayDevice function selection. Returns the duplicate ID and value.
        """    
        # Declare Local Variables
        blnFlag = bool(False)
        
        # Create the sql query params
        sqlTableCol = ("intBelayDeviceFunctPlastSelectID", "strBelayDeviceFunctPlastSelect")   
        sqlTableName = "TBelayDeviceFunctPlasticSelects"
        
        # Execute the search for duplicates
        sqlDupValues = Queries.Get_Duplicate_Data(Queries, (sqlTableCol[0], sqlTableCol[1], sqlTableName))    
        for i in range(len(sqlDupValues)):
            if self.strBelayDeviceFunctPlastSelect in sqlDupValues[i]:
                self.intBelayDeviceFunctPlastSelectID = sqlDupValues[i][0]
                self.strBelayDeviceFunctPlastSelect = sqlDupValues[i][1]
                blnFlag = bool(True)
                break

        return blnFlag
            
    def Add_BelayDevicePlasticFunctSelection_Query(self):
        """ 
        Function Name: Add_BelayDevicePlasticFunctSelection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewBelayDevicePlasticFunctSelection
        """    
        # Create the sql query string
        sqlTableCol = ("intBelayDeviceFunctPlastSelectID", "strBelayDeviceFunctPlastSelect")   
        sqlTableName = "TBelayDeviceFunctPlasticSelects"
        sqlTableValues = (BelayDevicePlasticFunctSelection.intBelayDeviceFunctPlastSelectID, BelayDevicePlasticFunctSelection.strBelayDeviceFunctPlastSelect)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)         

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)                            

    def Clear_BelayDeviceFuncPlasticSel_Attributes(self):
        """ 
        Function Name: Clear_BelayDeviceFuncPlasticSel_Attributes
        Function Description: This function clears the BelayDevice Function Plastic Selection attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intBelayDeviceFunctPlastSelectID", "strBelayDeviceFunctPlastSelect")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
                
                                
class BelayDeviceFunctionInspect(BelayDevices, InspectionType, BelayDeviceFunctSelection, BelayDevicePlasticFunctSelection, InspectionStatus):
    """
    Class Name: BelayDeviceFunctionInspect
    Class Description: This class gets and sets all of the BelayDevice Function Inspection  attributes. 
    """
    # Create class variable shared amongst all BelayDevice Function Inspection methods
    aintBelayDeviceFunctionInspectID = []
    aBelayDeviceFunctCache = []
        
    # Instantiate the following attributes
    def __init__(self, intBelayDeviceFunctionInspectID, intBelayDeviceID, intInspectionTypeID, intBelayDeviceFunctSelectID, 
                intBelayDeviceFunctPlastSelectID, intInspectionStatusID):
        self.intBelayDeviceFunctionInspectID = intBelayDeviceFunctionInspectID
        # Inherits the child class with all the necessary objects
        BelayDevices.__init__(intBelayDeviceID)
        InspectionType.__init__(intInspectionTypeID)
        BelayDeviceFunctSelection.__init__(intBelayDeviceFunctSelectID)
        BelayDevicePlasticFunctSelection.__init__(intBelayDeviceFunctPlastSelectID)
        InspectionStatus.__init__(intInspectionStatusID)

    # Property decorator object get function to access private intBelayDeviceFunctionInspectID
    @property
    def intBelayDeviceFunctionInspectID(self):
        return self._intBelayDeviceFunctionInspectID

    # setter method 
    @intBelayDeviceFunctionInspectID.setter 
    def intBelayDeviceFunctionInspectID(self, intBelayDeviceFunctionInspectID): 
        # Return true if specified object is of int type
        if not isinstance(intBelayDeviceFunctionInspectID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the BelayDevice Function Inspection ID to value
        if intBelayDeviceFunctionInspectID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBelayDeviceFunctionInspectID = intBelayDeviceFunctionInspectID 

    def Append_BelayDeviceFunctIDList(self, intObject):
        """ 
        Function Name: Append_BelayDeviceFunctIDList
        Function Description: This function appends objects to the BelayDevice Function Inspection ID list
        """    
        self.aintBelayDeviceFunctionInspectID.append(intObject)

    def Remove_BelayDeviceFunctIDList(self, intObject):
        """ 
        Function Name: Remove_BelayDeviceFunctIDList
        Function Description: This function removes objects in the BelayDevice Function Inspection ID list
        """    
        self.aintBelayDeviceFunctionInspectID.remove(intObject)

    def Get_BelayDeviceFunctIDList_Obj(self):
        """ 
        Function Name: Get_BelayDeviceFunctIDList_Obj
        Function Description: This function gets all the objects in the BelayDevice Function Inspection ID list
        """    
        return self.aintBelayDeviceFunctionInspectID
                
    def Delete_BelayDeviceFunctInspect_Data(self):
        """ 
        Function Name: Delete_BelayDeviceFunctInspect_Data
        Function Description: This function removes all the objects in the BelayDevice Function Inspection ID class
        """    
        BelayDeviceFunctionInspect.aintBelayDeviceFunctionInspectID = []
        BelayDeviceFunctionInspect.aBelayDeviceFunctCache = []

    def Set_BelayDeviceFunctInspect_Data(self):
        """ 
        Function Name: Set_BelayDeviceFunctInspect_Data
        Function Description: This function sets all the objects in the BelayDevice Function Inspection class
        """    
        self.intBelayDeviceFunctionInspectID = BelayDeviceFunctionInspect.aBelayDeviceFunctCache[0]
        self.intBelayDeviceID = BelayDeviceFunctionInspect.aBelayDeviceFunctCache[1]
        self.intInspectionTypeID = BelayDeviceFunctionInspect.aBelayDeviceFunctCache[2]
        self.intBelayDeviceFunctSelectID = BelayDeviceFunctionInspect.aBelayDeviceFunctCache[3]
        self.intBelayDeviceFunctPlastSelectID = BelayDeviceFunctionInspect.aBelayDeviceFunctCache[4]
        self.intInspectionStatusID = BelayDeviceFunctionInspect.aBelayDeviceFunctCache[5]
                
    def Add_BelayDeviceFunctInspect_Query(self):
        """ 
        Function Name: Add_BelayDeviceFunctInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewBelayDeviceFunctionInspection
        """    
        # Set the class variables before dumping the data to the database
        BelayDeviceFunctionInspect.Set_BelayDeviceFunctInspect_Data(self)
                
        # Create the sql query string
        sqlTableCol = ("intBelayDeviceFunctionInspectID", "intBelayDeviceID", "intInspectionTypeID", "intBelayDeviceFunctSelectID", 
                    "intBelayDeviceFunctPlastSelectID", "intInspectionStatusID")     
        sqlTableName = "TBelayDeviceFunctionInspections"
        sqlTableValues = (self.intBelayDeviceFunctionInspectID, self.intBelayDeviceID, self.intInspectionTypeID, self.intBelayDeviceFunctSelectID,
                        self.intBelayDeviceFunctPlastSelectID, self.intInspectionStatusID)
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)           

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Clear_BelayDeviceFuncInspect_Attributes(self):
        """ 
        Function Name: Clear_BelayDeviceFuncInspect_Attributes
        Function Description: This function clears the BelayDevice Function Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intBelayDeviceFunctionInspectID", "intBelayDeviceID", "intInspectionTypeID", "intBelayDeviceFunctSelectID", 
                        "intBelayDeviceFunctPlastSelectID", "intInspectionStatusID")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)
            
                                                                                                    
class StandardBelayDeviceInspect(BelayDeviceVisualInspect, BelayDevicePhysicalInspect, BelayDeviceFunctionInspect):
    """
    Class Name: StandardBelayDeviceInspect
    Class Description: This class gets and sets all of the Standard BelayDevice Inspection attributes. 
    Pass in the BelayDevice Visual, Physical, and Function Inspection Status classes. 
    """
    # Create class variable shared amongst all StandardBelayDeviceInspect methods
    aintStandardBelayDeviceInspectionID = []
    aStandardBelayDeviceInsCache = []
        
    # Instantiate the following attributes
    def __init__(self, intStandardBelayDeviceInspectionID, intBelayDeviceVisualInspectionID, intBelayDevicePhysicalInspectionID, intBelayDeviceFunctionInspectID):
        self.intStandardBelayDeviceInspectionID = intStandardBelayDeviceInspectionID
        BelayDeviceVisualInspect.__init__(self, intBelayDeviceVisualInspectionID)
        BelayDevicePhysicalInspect.__init__(self, intBelayDevicePhysicalInspectionID)
        BelayDeviceFunctionInspect.__init__(self, intBelayDeviceFunctionInspectID)
        
    # Property decorator object get function to access private intStandardBelayDeviceInspectionID
    @property
    def intStandardBelayDeviceInspectionID(self):
        return self._intStandardBelayDeviceInspectionID

    # setter method 
    @intStandardBelayDeviceInspectionID.setter 
    def intStandardBelayDeviceInspectionID(self, intStandardBelayDeviceInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intStandardBelayDeviceInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intStandardBelayDeviceInspectionID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intStandardBelayDeviceInspectionID = intStandardBelayDeviceInspectionID 
        
    def Append_StandBelayDeviceInspectIDList(self, intObject):
        """ 
        Function Name: Append_StandBelayDeviceInspectIDList
        Function Description: This function appends objects to the Standard BelayDevice Inspection ID list
        """    
        self.aintStandardBelayDeviceInspectionID.append(intObject)

    def Remove_StandBelayDeviceInspectIDList(self, intObject):
        """ 
        Function Name: Remove_StandBelayDeviceInspectIDList
        Function Description: This function removes objects in the Standard BelayDevice Inspection ID list
        """    
        self.aintStandardBelayDeviceInspectionID.remove(intObject)

    def Get_StandBelayDeviceInspectIDList_Obj(self):
        """ 
        Function Name: Get_StandBelayDeviceInspectIDList_Obj
        Function Description: This function gets all the objects in the Standard BelayDevice Inspection ID list
        """    
        return self.aintStandardBelayDeviceInspectionID

    def Add_StandBelayDeviceInspect_Query(self):
        """ 
        Function Name: Add_StandBelayDeviceInspect_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewStandardBelayDeviceInspection
        """    
        # Create the sql query string
        sqlTableNames = ("TStandardBelayDeviceInspections")
        sqlTableCol = ("intStandardBelayDeviceInspectionID", "intBelayDeviceVisualInspectionID", "intBelayDevicePhysicalInspectionID", 
                    "intBelayDeviceFunctionInspectID", "intInspectionStatusID")
        # Set the primary key values from the cached array object
        aPrimKeyValues = [item for item in StandardBelayDeviceInspect.aStandardBelayDeviceInsCache]

        # Get the visual, physical, and functional status IDs
        VisStatusID = InspectionStatus.astrInspectionStatusDesc.index(BelayDeviceVisSelection.strBelayDeviceVisStatus) + 1
        PhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(BelayDevicePhysSelection.strBelayDevicePhysStatus) + 1
        FunctStatusID = InspectionStatus.astrInspectionStatusDesc.index(BelayDeviceFunctSelection.strBelayDeviceFunctStatus) + 1
        plastVisStatusID = InspectionStatus.astrInspectionStatusDesc.index(BelayDevicePlasticVisSelection.strBelayDeviceVisStatus) + 1
        plastPhysStatusID = InspectionStatus.astrInspectionStatusDesc.index(BelayDevicePlasticPhysSelection.strBelayDevicePhysStatus) + 1
        plastFunctStatusID = InspectionStatus.astrInspectionStatusDesc.index(BelayDevicePlasticFunctSelection.strBelayDeviceFunctStatus) + 1        
        aInsStatusID = [VisStatusID, PhysStatusID, FunctStatusID, plastVisStatusID, plastPhysStatusID, plastFunctStatusID]

        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(aInsStatusID)
        
        # Append the AutoBelay Status array 
        BelayDeviceInspect.aBelayDeviceInspectStatus.append(intOverallStatus)

        # Append the primary key list with the new over status ID
        aPrimKeyValues.append(intOverallStatus)                      
        
        # Set the parameters
        sqlParams = (sqlTableNames, sqlTableCol, tuple(aPrimKeyValues))

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Delete_StandBelayDeviceInspect_Data(self):
        """ 
        Function Name: Delete_StandBelayDeviceInspect_Data
        Function Description: This function removes all the objects in the Standard BelayDevice Inspection class
        """    
        StandardBelayDeviceInspect.aintStandardBelayDeviceInspectionID = []
        StandardBelayDeviceInspect.aStandardBelayDeviceInsCache = []

    def Clear_BelayDeviceStandardInspect_Attributes(self):
        """ 
        Function Name: Clear_BelayDeviceStandardInspect_Attributes
        Function Description: This function clears the BelayDevice Standard Inspect attributes once the user proceeds with adding a new
        unit to the database.
        """    
        # Set the objects in a tuple to run through the list and set each object back to None
        attribute_names = ("intStandardBelayDeviceInspectionID", "intBelayDeviceVisualInspectionID", "intBelayDevicePhysicalInspectionID", 
                    "intBelayDeviceFunctionInspectID", "intInspectionStatusID")
                        
        # Set each attribute to None
        for i, attr_name in enumerate(attribute_names):
                setattr(self, attr_name, None)

    def Reset_BelayDevice_Data(self):
        """ 
        Function Name: Reset_BelayDevice_Data
        Function Description: This function clears the BelayDevice data attributes 
        """  
        # Clear the class attributes
        BelayDeviceVisSelection.Clear_BelayDeviceVisSel_Attributes(self)
        BelayDevicePlasticVisSelection.Clear_BelayDevice_Plastic_VisSel_Attributes(self)
        BelayDevicePhysSelection.Clear_BelayDevicePhysSel_Attributes(self)
        BelayDevicePlasticPhysSelection.Clear_BelayDevice_Plastic_PhysSel_Attributes(self)
        BelayDeviceFunctSelection.Clear_BelayDeviceFuncSel_Attributes(self)
        BelayDevicePlasticFunctSelection.Clear_BelayDeviceFuncPlasticSel_Attributes(self)
        BelayDeviceVisualInspect.Clear_BelayDeviceVisInspect_Attributes(self)
        BelayDevicePhysicalInspect.Clear_BelayDevicePhysInspect_Attributes(self)
        BelayDeviceFunctionInspect.Clear_BelayDeviceFuncInspect_Attributes(self)
        StandardBelayDeviceInspect.Clear_BelayDeviceStandardInspect_Attributes(self)

    def Delete_BelayDevice_Data(self):
        """ 
        Function Name: Delete_Brake_Data
        Function Description: This function clears the Brake data arrays 
        """  
        # Clear the class arrays
        BelayDeviceVisSelection.Delete_BelayDeviceVisSelection_Data(self)
        BelayDevicePlasticVisSelection.Delete_BelayDevice_Plastic_VisSelection_Data(self)
        BelayDevicePhysSelection.Delete_BelayDevicePhysSelection_Data(self)
        BelayDevicePlasticPhysSelection.Delete_BelayDevice_Plastic_PhysSelection_Data(self)
        BelayDeviceFunctSelection.Delete_BelayDeviceFunctSelection_Data(self)
        BelayDevicePlasticFunctSelection.Delete_BelayDevicePlasticFunctSelection_Data(self)
        BelayDevicePhysicalInspect.Delete_BelayDevicePhysicalInspect_Data(self)
        BelayDeviceVisualInspect.Delete_BelayDeviceVisualInspect_Data(self)
        BelayDeviceFunctionInspect.Delete_BelayDeviceFunctInspect_Data(self)
        StandardBelayDeviceInspect.Delete_StandBelayDeviceInspect_Data(self)          
        

class BelayDeviceInspect(WallLocation, StandardBelayDeviceInspect, Inspector):
    """
    Class Name: BelayDeviceInspect
    Class Description: This class gets and sets all of the BelayDevice Inspection attributes. 
    """
    # Create class variable shared amongst all BelayDevice Inspection methods
    aintBelayDeviceInspectionID = []
    aBelayDeviceInspectStatus = []
        
    # Instantiate the following attributes
    def __init__(self, intBelayDeviceInspectionID, intWallLocationID, intStandardBelayDeviceInspectionID, 
                intInspectorID, strComment):
        self.intBelayDeviceInspectionID = intBelayDeviceInspectionID
        self.strComment = strComment
        # Inherits the child class with all the necessary objects
        WallLocation().__init__(intWallLocationID)
        StandardBelayDeviceInspect().__init__(intStandardBelayDeviceInspectionID)
        Inspector().__init__(intInspectorID)

    # Property decorator object get function to access private intBelayDeviceInspectionID
    @property
    def intBelayDeviceInspectionID(self):
        return self._intBelayDeviceInspectionID

    # PBelayDevicerty decorator object get function to access private strComment
    @property
    def strComment(self):
        return self._strComment
            
    # setter method 
    @intBelayDeviceInspectionID.setter 
    def intBelayDeviceInspectionID(self, intBelayDeviceInspectionID): 
        # Return true if specified object is of int type
        if not isinstance(intBelayDeviceInspectionID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intBelayDeviceInspectionID < 0: 
            raise ValueError('ID cannot be negative') 
        self._intBelayDeviceInspectionID = intBelayDeviceInspectionID    

    # setter method 
    @strComment.setter 
    def strComment(self, strComment): 
        # Return true if specified object is of str type
        if not isinstance(strComment, str): 
            raise TypeError('Comment must be a string') 
        # Set the attribute to the value if true
        elif strComment.isascii():
            self._strComment = strComment   

    def Append_BelayDeviceInspectIDList(self, intObject):
        """ 
        Function Name: Append_BelayDeviceInspectIDList
        Function Description: This function appends objects to the BelayDevice Inspection ID list
        """    
        self.aintBelayDeviceInspectionID.append(intObject)

    def Remove_BelayDeviceInspectIDList(self, intObject):
        """ 
        Function Name: Remove_BelayDeviceInspectIDList
        Function Description: This function removes objects in the BelayDevice Inspection ID list
        """    
        self.aintBelayDeviceInspectionID.remove(intObject)

    def Get_BelayDeviceInspectIDList_Obj(self):
        """ 
        Function Name: Get_BelayDeviceInspectIDList_Obj
        Function Description: This function gets all the objects in the BelayDevice Inspection ID list
        """    
        return self.aintBelayDeviceInspectionID   

    def Join_BelayDeviceInspectComm_Obj(self, strObject):
        """ 
        Function Name: Join_BelayDeviceInspectComm_Obj
        Function Description: This function joins the string objects in the BelayDevice Inspection comment
        """    
        self.strComment = self.strComment + " " + strObject

    def Get_MaxStandardBelayDeviceInspectID(self, table_name, id_column_name):
        """
        Function Name: Get_MaxStandardBelayDeviceInspectID
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)

    def Delete_BelayDeviceInspect_Data(self):
        """ 
        Function Name: Delete_BelayDeviceInspect_Data
        Function Description: This function removes all the objects in the BelayDevice Inspect class
        """    
        BelayDeviceInspect.aintBelayDeviceInspectionID = []
        BelayDeviceInspect.aBelayDeviceInspectStatus = []
                            
    def Add_BelayDeviceInspection_Query(self):
        """ 
        Function Name: Add_BelayDeviceInspection_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewBelayDeviceInspection
        """
        # Create the sql query string
        sqlTableCol = ("intBelayDeviceInspectionID", "intBelayDeviceID", "intWallLocationID", "intStandardBelayDeviceInspectionID", 
                "intInspectorID", "intInspectionStatusID", "dtmLastInspectionDate", "dtmNextInspectionDate", "strComment")
        sqlTableName = "TBelayDeviceInspections"
        
        # Get the max primary key value for the table
        sqlMaxPrimKeyID = BelayDeviceInspect.Get_MaxStandardBelayDeviceInspectID(self, sqlTableName, sqlTableCol[0])
        self.intBelayDeviceInspectionID = sqlMaxPrimKeyID

        # Determine the overall status
        intOverallStatus = BaseFunctions.Check_Overall_Status(BelayDeviceInspect.aBelayDeviceInspectStatus)
            
        # For testing purposes, set the inspector ID to 1
        Inspector.intInspectorID = 1
                    
        # # Set the inspector ID
        # # print(UserLogins.aCurrentUserLogin)
        # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID
        
        # Perform the insert query
        sqlTableValues = (self.intBelayDeviceInspectionID, BelayDevices.intBelayDeviceID, WallLocation.intWallLocationID, StandardBelayDeviceInspect.aStandardBelayDeviceInsCache[0], 
                        Inspector.intInspectorID, intOverallStatus, BelayDevices.dtmLastInspectionDate, BelayDevices.dtmNextInspectionDate, BelayDeviceInspect.strComment)
                        
        # Set the parameters
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)
        
    def Add_BelayDeviceInspector_Query(self):
        """ 
        Function Name: Add_BelayDeviceInspector_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewBelayDeviceInspector
        """    
        # Create the sql query string
        sqlTableCol = ("intBelayDeviceInspectorID", "intInspectorID", "intBelayDeviceID")
        sqlTableName = "TBelayDeviceInspectors"
        
        # Get the max primary key value for the table
        sqlMaxPrimKeyID = BelayDeviceInspect.Get_MaxStandardBelayDeviceInspectID(self, sqlTableName, sqlTableCol[0])

        # For testing purposes, set the inspector ID to 1
        Inspector.intInspectorID = 1
                    
        # # Set the inspector ID
        # # print(UserLogins.aCurrentUserLogin)
        # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID
        
        # Perform the insert query
        sqlTableValues = (sqlMaxPrimKeyID, Inspector.intInspectorID, BelayDevices.intBelayDeviceID)
                
        # Set the parameters
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)          
        
    def Add_BelayDeviceLocation_Query(self):
        """ 
        Function Name: Add_BelayDeviceLocation_Query
        Function Description: This function updated the database with all of the necessary objects executing
        the stored procedure uspAddNewBelayDeviceWallLocation
        """    
        # Declare Local Variables
        blnFlag = False
        
        # Create the sql query string
        sqlTableAttr = ("TBelayDeviceWallLocations", "intBelayDeviceWallLocationID", "intWallLocationID", "intBelayDeviceID")
        
        try:
            # Get the max primary key value for the table
            idList = (WallLocation.intWallLocationID, BelayDevices.intBelayDeviceID)
            sqlMaxPrimKeyID = BelayDeviceInspect.Get_Or_Create_ID(BelayDeviceInspect, idList, sqlTableAttr)

            # For testing purposes, set the inspector ID to 1
            Inspector.intInspectorID = 1
                        
            # Set the inspector ID
            # print(UserLogins.aCurrentUserLogin)
            # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID

            # Get the values
            sqlTableValues = (sqlMaxPrimKeyID, idList[0], idList[1])
                    
            # Set the parameters
            sqlParams = (sqlTableAttr[0], sqlTableAttr[1:], sqlTableValues)
            
            # Get the id list from TBelayDeviceWallLocations
            aidReturnList = Queries.Get_All_DB_Values(Queries, sqlTableAttr[0])
            
            # Check if the max ID is in the aidReturnList object
            if aidReturnList:
                for i in aidReturnList:
                    # Extract the IDs from the current entry for clarity
                    current_ids = i[1:3]

                    # Compare current IDs with the item's IDs
                    if idList == current_ids:
                        if BelayDevices.strEquipInUse == 'Yes':
                            # If device is in use and IDs match, no need to update.
                            blnFlag = True
                        else:
                            # If device is not in use, remove the item.
                            Queries.Remove_Attribute_Query(Queries, sqlTableAttr[0], sqlTableAttr[1], i[0])
                    elif idList[0] == current_ids[0] or idList[1] == current_ids[1]:
                        # If the connector ID matches the current entry's connector ID, remove the entry from the database
                        Queries.Remove_Attribute_Query(Queries, sqlTableAttr[0], sqlTableAttr[1], i[0])
                    
            # Add or update the database if needed
            if not blnFlag and BelayDevices.strEquipInUse == 'Yes':
                Queries.dbExeUSP_AddValues(Queries, sqlParams)
                    
        except Exception as e:
            print(f"Error in Add_BelayDeviceLocation_Query: {e}")

    def Get_Or_Create_ID(self, item_list, sql_tuple):
        """
        Function Name: Get_Or_Create_ID
        Function Purpose: Check if there is a duplicate in the database for the item list. If not, create a new ID.
        """
        aReturn = BelayDeviceInspect.Check_Duplicate(BelayDeviceInspect, item_list, sql_tuple)
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
    
    
class BelayDevicesRetiredReport(BelayDeviceInspect):
    """
    Class Name: BelayDevicesRetiredReport
    Class Description: This class gets and sets all of the BelayDevice Retired Report attributes. 
    """
    # Create class variable shared amongst all BelayDevice Retired methods
    aintBelayDevicesRetiredReportID = []

    # Instantiate the following attributes
    def __init__(self, intBelayDevicesRetiredReportID, intBelayDeviceInspectionID, intInspectorID, dtmReportDate):
        self.intBelayDevicesRetiredReportID = intBelayDevicesRetiredReportID
        self.dtmReportDate = dtmReportDate
        # Inherits the child class with all the necessary objects
        BelayDeviceInspect().__init__(intBelayDeviceInspectionID)
        Inspector().__init__(intInspectorID)

    # Property decorator object get function to access private intBelayDevicesRetiredReportID
    @property
    def intBelayDevicesRetiredReportID(self):
        return self._intBelayDevicesRetiredReportID

    # Property decorator object get function to access private dtmReportDate
    @property
    def dtmReportDate(self):
        return self._dtmReportDate
            
    # setter method 
    @intBelayDevicesRetiredReportID.setter 
    def intBelayDevicesRetiredReportID(self, intBelayDevicesRetiredReportID): 
        # Return true if specified object is of int type
        if not isinstance(intBelayDevicesRetiredReportID, int): 
            raise TypeError('ID must be an integer') 
        # Check if the value is less than zero, otherwise return true and set the ID to value
        if intBelayDevicesRetiredReportID < 0: 
            raise ValueError('ID cannot be negative') 

        self._intBelayDevicesRetiredReportID = intBelayDevicesRetiredReportID    

    # setter method 
    @dtmReportDate.setter 
    def dtmReportDate(self, dtmReportDate):              
        # Return true if specified object is of str type
        if not isinstance(dtmReportDate, str): 
            raise TypeError('Report Date must first be a string') 
        # Check if the value is empty, otherwise check if the value is date type
        if dtmReportDate.isspace(): 
            raise ValueError('Report Date cannot be empty')       
        # Convert the date to string
        dtmReportDate = datetime.strptime(dtmReportDate, '%m/%d/%Y').date()
        # Return true if specified object is of date type
        if not isinstance(dtmReportDate, date): 
            raise TypeError('Report Date must be a valid date') 
        # Convert the date back to string
        dtmReportDate = str(dtmReportDate)

        self._dtmReportDate = dtmReportDate  

    def Append_BelayDevice_RetiredReportID_List(self, intObject):
        """ 
        Function Name: Append_BelayDevice_RetiredReportID_List
        Function Description: This function appends objects to the BelayDevice Retired Report ID list
        """    
        self.aintBelayDevicesRetiredReportID.append(intObject)

    def Remove_BelayDevice_RetiredReportID_List(self, intObject):
        """ 
        Function Name: Remove_BelayDevice_RetiredReportID_List
        Function Description: This function removes objects in the BelayDevice Retired Report ID list
        """    
        self.aintBelayDevicesRetiredReportID.remove(intObject)

    def Get_BelayDevice_RetiredReportID_List_Obj(self):
        """ 
        Function Name: Get_BelayDevice_RetiredReportID_List_Obj
        Function Description: This function gets all the objects in the BelayDevice Retired Report ID list
        """    
        return self.aintBelayDevicesRetiredReportID   

    def Delete_BelayDevice_RetiredReport_Data(self):
        """ 
        Function Name: Delete_BelayDevice_RetiredReport_Data
        Function Description: This function removes all the objects in the BelayDevice Retired Report class
        """    
        BelayDevicesRetiredReport.aintBelayDevicesRetiredReportID = []

    def Get_Max_Primary_Key(self, table_name, id_column_name):
        """
        Function Name: Get_Max_Primary_Key
        Function Purpose: Get the maximum primary key value for the specified table.
        """
        return Queries.Get_MaxPrimaryKeys(Queries, table_name, id_column_name)
                                
    def Add_BelayDevice_RetiredReport_Query(self):
        """ 
        Function Name: Add_BelayDevice_RetiredReport_Query
        Function Description: This function updated the database with all of the necessary objects
        """
        # Get todays date
        dtmToday = datetime.now().date()
        self.dtmReportDate = str(dtmToday)
                
        # Create the sql query string
        sqlTableCol = ("intBelayDevicesRetiredReportID", "intBelayDeviceInspectionID", "intInspectorID", "dtmReportDate")
        sqlTableName = "TBelayDevicesRetiredReports"
        
        # Get the max primary key value for the table
        sqlMaxPrimKeyID = BelayDevicesRetiredReport.Get_Max_Primary_Key(self, sqlTableName, sqlTableCol[0])

        # For testing purposes, set the inspector ID to 1
        Inspector.intInspectorID = 1
        
        # # Set the inspector ID
        # # print(UserLogins.aCurrentUserLogin)
        # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID
        
        # Perform the insert query
        sqlTableValues = (sqlMaxPrimKeyID, self.intBelayDeviceInspectionID, Inspector.intInspectorID, self.dtmReportDate)

        # Set the parameters
        sqlParams = (sqlTableName, sqlTableCol, sqlTableValues)

        # Execute the stored procedure
        Queries.dbExeUSP_AddValues(Queries, sqlParams)

    def Update_BelayDevice_RetiredReport_Query(self):
        """ 
        Function Name: Update_BelayDevice_RetiredReport_Query
        Function Description: This function updated the database with all of the necessary objects
        """
        # Get todays date
        dtmToday = datetime.now().date()
        self.dtmReportDate = str(dtmToday)
                
        # Create the sql query string
        sqlTableCol = ("intBelayDevicesRetiredReportID", "intBelayDeviceInspectionID", "intInspectorID", "dtmReportDate")
        sqlTableName = "TBelayDevicesRetiredReports"
        sqlViewName = "vBelayDeviceInspectID_OutOfService"
        
        # Get the max primary key value for the table
        sqlBelayDeviceInspectValues = Queries.Get_All_DB_Values(self, sqlViewName)
        sqlBelayDeviceRetiredReportValues = Queries.Get_All_DB_Values(self, sqlTableName)
        
        # For testing purposes, set the inspector ID to 1
        Inspector.intInspectorID = 1
        
        # # Set the inspector ID
        # # print(UserLogins.aCurrentUserLogin)
        # UserLogins.aCurrentUserLogin[1] = Inspector.intInspectorID

        # Process each inspection value
        for inspectValue in sqlBelayDeviceInspectValues:
            inspectionID = inspectValue[0]
            if inspectionID not in [report[0] for report in sqlBelayDeviceRetiredReportValues]:
                # Inspection ID not found in the report, consider adding it
                self.intBelayDeviceInspectionID = inspectionID
                BelayDevicesRetiredReport.Add_BelayDevice_RetiredReport_Query(self)

            elif self.strEquipInUse != "Retired":
                # Remove the report if the device is no longer in service
                Queries.Remove_Attribute_Query(Queries, sqlTableName, sqlTableCol[0], inspectionID)

            else:
                # Update the existing report
                sqlTableValues = (inspectionID, self.intBelayDeviceInspectionID, Inspector.intInspectorID, self.dtmReportDate)
                sqlParams = (sqlTableName, sqlTableCol, sqlTableValues, sqlTableCol[0], inspectionID)
                Queries.dbExeUSP_UpdateValues(Queries, sqlParams)
