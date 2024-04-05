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
import random
import string
from PIL import Image, ImageTk

# Import project modules
from Account_object_class import Account
from password_object_class import PasswordWithPolicy
from base_methods import BaseMethods

#######################################################################################################
# Password Policy Record Table Creation
#######################################################################################################         

    def create_password_policy_table(self):
        """ 
        Function Name: create_password_policy_table
        Function Purpose: Create the password policy record Table and Z Tables inside the database
        """          
        try:
            # First check if connected to the database   
            if not self.conn:
                raise Exception("Database is not connected.")
        
            # Create the table
            sqlTable = """ 
                -- Create Password Policy Table
                CREATE TABLE IF NOT EXISTS TPasswordPolicies 
                (
                    intPolicyID                         INTEGER NOT NULL
                    ,intUserID                          INTEGER NOT NULL
                    ,intMinCharLength                   INTEGER NOT NULL
                    ,strRequiredChar                    VARCHAR(1000) NOT NULL
                    ,intExpirePeriod                    INTEGER NOT NULL
                    ,strModifiedReason                  VARCHAR(1000)
                    ,FOREIGN KEY ( intUserID ) REFERENCES TUsers ( intUserID )
                    ,CONSTRAINT TPasswordPolicies_PK PRIMARY KEY ( intPolicyID )               
                );
                """
            # Create the audit table    
            sqlAudit = f"""                
                -- Create Z Table: Password Policy Table
                CREATE TABLE IF NOT EXISTS Z_TPasswordPolicies 
                (
                    intPolicyAuditID                    INTEGER NOT NULL
                    ,intPolicyID                        INTEGER NOT NULL
                    ,intUserID                          INTEGER NOT NULL
                    ,intMinCharLength                   INTEGER NOT NULL
                    ,strRequiredChar                    VARCHAR(1000) NOT NULL
                    ,intExpirePeriod                    INTEGER NOT NULL
                    ,strUpdatedBy                       VARCHAR(225) NOT NULL DEFAULT '{self.currentAccount}'
                    ,dtmUpdatedOn                       DATETIME DEFAULT CURRENT_TIMESTAMP
                    ,strAction                          VARCHAR(1) NOT NULL
                    ,strModifiedReason                  VARCHAR(1000)
                    
                    ,CONSTRAINT Z_TPasswordPolicies_PK PRIMARY KEY (intPolicyAuditID)
                );
                """
            # Create the table trigger    
            sqlTrigger = f"""
                -- Create Trigger: Password Policy Table - Insert Trigger
                CREATE TRIGGER IF NOT EXISTS Z_TPasswordPolicies_AuditTrigger_Insert
                AFTER INSERT ON TPasswordPolicies
                BEGIN
                    INSERT INTO Z_TPasswordPolicies 
                    (
                        intPolicyID
                        ,intUserID
                        ,intMinCharLength
                        ,strRequiredChar
                        ,intExpirePeriod
                        ,strUpdatedBy
                        ,dtmUpdatedOn
                        ,strAction
                        ,strModifiedReason
                    )
                    VALUES 
                    (
                        NEW.intPolicyID
                        ,NEW.intUserID
                        ,NEW.intMinCharLength
                        ,NEW.strRequiredChar
                        ,NEW.intExpirePeriod
                        ,'{self.currentAccount}'
                        ,DATETIME('now')
                        ,'I' -- Insert
                        ,NEW.strModifiedReason
                    );
                END;

                -- Create Trigger: Password Policy Table - Update Trigger
                CREATE TRIGGER IF NOT EXISTS Z_TPasswordPolicies_AuditTrigger_Update
                AFTER UPDATE ON TPasswordPolicies
                BEGIN
                    INSERT INTO Z_TPasswordPolicies 
                    (
                        intPolicyID
                        ,intUserID
                        ,intMinCharLength
                        ,strRequiredChar
                        ,intExpirePeriod
                        ,strUpdatedBy
                        ,dtmUpdatedOn
                        ,strAction
                        ,strModifiedReason
                    )
                    VALUES 
                    (
                        NEW.intPolicyID
                        ,NEW.intUserID
                        ,NEW.intMinCharLength
                        ,NEW.strRequiredChar
                        ,NEW.intExpirePeriod
                        ,'{self.currentAccount}'
                        ,DATETIME('now')
                        ,'U' -- Update
                        ,NEW.strModifiedReason
                    );
                END;

                -- Create Trigger: Password Policy Table - Delete Trigger
                CREATE TRIGGER IF NOT EXISTS Z_TPasswordPolicies_AuditTrigger_Delete
                AFTER DELETE ON TPasswordPolicies
                BEGIN
                    INSERT INTO Z_TPasswordPolicies 
                    (
                        intPolicyID
                        ,intUserID
                        ,intMinCharLength
                        ,strRequiredChar
                        ,intExpirePeriod
                        ,strUpdatedBy
                        ,dtmUpdatedOn
                        ,strAction
                        ,strModifiedReason
                    )
                    VALUES 
                    (
                        OLD.intPolicyID
                        ,OLD.intUserID
                        ,OLD.intMinCharLength
                        ,OLD.strRequiredChar
                        ,OLD.intExpirePeriod
                        ,'{self.currentAccount}'
                        ,DATETIME('now')
                        ,'D' -- Delete
                        ,OLD.strModifiedReason
                    );
                END;
                """
                
            # Execute the SQL statements
            Database.db_exe_statement(self, sqlTable)
            Database.db_exe_statement(self, sqlAudit)
            Database.db_exe_statement(self, sqlTrigger)    
            
            # Commit the changes 
            self.conn.commit()

        except sqlite3.Error as e:
            print(f"Error creating Password Policy tables: {e}")