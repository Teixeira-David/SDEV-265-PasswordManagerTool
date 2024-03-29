import tkinter as tk

#######################################################################################################
# Tool Tip Class
#######################################################################################################       
class CreateToolTip(object):
    """
    Class Name: CreateToolTip
    Description: This class is used to create a tooltip for a widget.
    """
    def __init__(self, widget, text='widget info'):
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
        # This function is used to display the tooltip when the mouse enters the widget.
        self.schedule()

    def leave(self, event=None):
        # This function is used to hide the tooltip when the mouse leaves the widget.
        self.unschedule()
        self.hidetip()

    def schedule(self):
        # This function is used to schedule the display of the tooltip.
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        # This function is used to unschedule the display of the tooltip.
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        # This function is used to display the tooltip.
        x = self.widget.winfo_rootx() + self.widget.winfo_width() / 2  # Center of the widget horizontally
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
        # This function is used to hide the tooltip.
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()
