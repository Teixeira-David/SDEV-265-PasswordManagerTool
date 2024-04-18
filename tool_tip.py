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
import tkinter as tk

# Import project modules


#######################################################################################################
# Tool Tip Class
#######################################################################################################       
class CreateToolTip(object):
    """
    Class Name: CreateToolTip
    Description: This class is used to create a tooltip for a widget.
    """
    def __init__(self, widget, text='widget info'):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """   
        self.waittime = 500     # miliseconds
        self.wraplength = 180   # pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        """
        Function Name: enter
        Description: This function is used to display the tooltip when the mouse enters the widget.
        """
        # Schedule the display of the tooltip
        self.schedule()

    def leave(self, event=None):
        """
        Function Name: leave
        Description: This function is used to hide the tooltip when the mouse leaves the widget.
        """
        self.unschedule()
        self.hidetip()

    def schedule(self):
        """
        Function Name: schedule
        Description: This function is used to schedule the display of the tooltip.
        """
        # unschedule the tooltip
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        """
        Function Name: unschedule
        Description: This function is used to unschedule the display of the tooltip.
        """
        # id is the id of the tooltip
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        """
        Function Name: showtip
        Description: This function is used to display the tooltip.
        """
        # This function is used to display the tooltip.
        x = self.widget.winfo_rootx() + self.widget.winfo_width() / 2  # Center of the widget horizontally
        if self.text == "Settings":
            y = self.widget.winfo_rooty() - 25  # Just above the widget
        else:
            y = self.widget.winfo_rooty() + self.widget.winfo_height()  # Just below the widget
        # Creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                    background="#ffffff", relief='solid', borderwidth=1,
                    wraplength=self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        """
        Function Name: hidetip
        Description: This function is used to hide the tooltip.
        """
        # tw is the tooltip window
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()
