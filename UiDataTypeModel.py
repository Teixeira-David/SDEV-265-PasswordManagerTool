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
from enum import Enum

# Import Project Libraries
from ObjectClass import Connectors, Bool_Flag

#######################################################################################################
# Ui Data Type State Class
#######################################################################################################  
class ItemType(Enum):
    """
    Class Name: ItemType
    Class Description: This Enum class sets the enumeration types for the items
    """    
    ROPES = ("Ropes", "Rope")
    CONNECTORS = ("Connectors", "Device")
    AUTOBELAYS = ("AutoBelays", "Device")
    BELAYDEVICES = ("BelayDevices", "Device")
    HARNESS = ("Harness", "Harness")
    ROUTESETTINGEQUIP = ("RouteSettingEquip", "Device")
    
    def __init__(self, type_name, label):
        self.type_name = type_name
        self.label = label

class ItemType_Serial_BumperNum_CacheMap():
    """
    Class Name: ItemType_Serial_BumperNum_CacheMap
    Class Description: This class sets the serial and bumper cached types for the items
    """ 
    itemData = {
        ItemType.CONNECTORS: {
            'serialNumCache': Connectors.astrSerialNumCache,
            'bumperNumCache': Connectors.astrBumperNumCache
        },
        
    }
    
class ItemType_DropMap():
    """
    Class Name: ItemType_DropMap
    Class Description: This class sets the serial, bumper, and equip in use types for the items
    """ 
    itemData = {
        ItemType.CONNECTORS: {
            'serialNum': Connectors.strSerialNum,
            'bumperNum': Connectors.strBumperNum,
            'equipInUse' : Connectors.strEquipInUse
        },
        
    }

class ItemType_BoolMap():
    """
    Class Name: ItemType_BoolMap
    Class Description: This class sets the bool types for the items
    """ 
    itemData = {
        ItemType.CONNECTORS: {
            'complexWithConnectorFlag': Bool_Flag.blnComplexWithConnectorFlag,
            'itemPersistFlag': Bool_Flag.blnConnectorPersistFlag,
            'serialNumRadioSelect' : Bool_Flag.blnSerialNumRadioSelect
        },
        
    }

class ItemType_SetSerial_InUse_Selection():
    """
    Class Name: ItemType_SetSerial_InUse_Selection
    Class Description: This class sets the serial and equip in use types for the items
    """ 
    # Define a mapping of ItemType to their corresponding values
    itemData = {
        ItemType.CONNECTORS: {
            'serialNum': Connectors.strSerialNum,
            'equipInUse' : Connectors.strEquipInUse
        },
        
    }
    
    # Define a mapping of ItemType to their corresponding actions
    actionMap = {
        ItemType.CONNECTORS: Connectors.Set_Connectors_Selection,

    }
    
    @classmethod
    def update_ItemData(cls, item_type, serial_num=None, equip_in_use=None):
        """
        Class Method Name: update_ItemData
        Description: Updates the data for a given item type.
        """
        if item_type in cls.itemData:
            if serial_num is not None:
                cls.itemData[item_type]['serialNum'] = serial_num
            if equip_in_use is not None:
                cls.itemData[item_type]['equipInUse'] = equip_in_use
                
            # After updating, call class method to handle further actions
            cls.execute_ItemSelection(item_type)
        else:
            print(f"ItemType {item_type} not recognized.")
            
    @classmethod
    def execute_ItemSelection(cls, item_type):
        """
        Class method Name: execute_ItemSelection
        Description: Executes the corresponding method based on the ItemType.
        """
        # Get the action for the given item type
        action = cls.actionMap.get(item_type)
        if action:
            # Execute the action
            action()  
            print(f"{item_type} action executed.")
        else:
            print(f"No action defined for {item_type}.")
            