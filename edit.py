#######################################################################################################
# Copyable Password Dialog Class
#######################################################################################################

class CopyablePasswordDialog_UiComposable(simpledialog.Dialog):
    """
    Class Name: CopyablePasswordDialog
    Class Description: This class is the dialog box that appears when the user generates a new password. The user
    can copy the password to the clipboard or click 'OK' to close the dialog box.
    """
    def __init__(self, parent, title, password):
        """ 
        Function Name: __init__
        Function Purpose: Instantiate the class objects and attributes for the Tkinter GUI
        """      
        self.password = password
        # Create the root tkinter variable  
        super().__init__(parent, title)

    def body(self, frame):
        """
        Function Name: body
        Function Purpose: This function creates the body of the dialog box
        """
        tk.Label(frame, text="The newly generated password is:").pack(padx=5, pady=5)
        self.entry = tk.Entry(frame, width=40)
        self.entry.pack(padx=5, pady=5)
        self.entry.insert(0, self.password)
        self.entry.focus()
        return self.entry

    def buttonbox(self):
        """
        Function Name: buttonbox
        Function Purpose: This function creates the buttons for the dialog box
        """
        box = tk.Frame(self)
        w = tk.Button(box, text="Copy", width=10, command=self.copy_password)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = tk.Button(box, text="OK", width=10, command=self.ok)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        box.pack()

    def copy_password(self):
        """
        Function Name: copy_password
        Function Purpose: This function copies the password to the clipboard
        """
        self.clipboard_clear()
        self.clipboard_append(self.password)
        self.entry.selection_range(0, tk.END)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

    def ok(self, event=None):
        """
        Function Name: ok
        Function Purpose: This function closes the dialog box
        """
        self.withdraw()
        self.update_idletasks()
        self.cancel()

    def cancel(self, event=None):
        """
        Function Name: cancel
        Function Purpose: This function closes the dialog box
        """
        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()