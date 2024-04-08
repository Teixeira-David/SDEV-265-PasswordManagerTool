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
import configparser
from datetime import date, datetime
import getpass
import glob
import os
import platform
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import pyzipper

# Import Project Modules



    def create_password_policy_table(self):
        """ 
        Function Name: create_password_policy_table
        Function Purpose: Create the password policy record Table and Z Tables inside the database
        """          
        # Create the table
        sql_table = """ 
            -- Create Password Policy Table
            CREATE TABLE IF NOT EXISTS TPasswordPolicies 
            (
                intPolicyID                         INTEGER NOT NULL
                ,intAccountID                       INTEGER NOT NULL
                ,intMinCharLength                   INTEGER NOT NULL
                ,strRequiredChar                    VARCHAR(1000) NOT NULL
                ,intExpirePeriod                    INTEGER NOT NULL
                ,strModifiedReason                  VARCHAR(1000)
                
                ,FOREIGN KEY ( intAccountID ) REFERENCES TAccounts ( intAccountID )
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
                ,intAccountID                       INTEGER NOT NULL
                ,intMinCharLength                   INTEGER NOT NULL
                ,strRequiredChar                    VARCHAR(1000) NOT NULL
                ,intExpirePeriod                    INTEGER NOT NULL
                ,strUpdatedBy                       VARCHAR(225) NOT NULL 
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
                    ,intAccountID
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
                    ,NEW.intAccountID
                    ,NEW.intMinCharLength
                    ,NEW.strRequiredChar
                    ,NEW.intExpirePeriod
                    ,(SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1)
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
                    ,intAccountID
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
                    ,NEW.intAccountID
                    ,NEW.intMinCharLength
                    ,NEW.strRequiredChar
                    ,NEW.intExpirePeriod
                    ,(SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1)
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
                    ,intAccountID
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
                    ,OLD.intAccountID
                    ,OLD.intMinCharLength
                    ,OLD.strRequiredChar
                    ,OLD.intExpirePeriod
                    ,(SELECT strCurrentUser FROM TSessionContext WHERE intSessionID = 1)
                    ,DATETIME('now')
                    ,'D' -- Delete
                    ,OLD.strModifiedReason
                );
            END;
            """
            
        # Execute the SQL statements
        self.db_exe_statement(sql_table)
        self.db_exe_statement(sqlAudit)
        self.db_exe_statement(sqlTrigger) 