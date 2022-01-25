###############################
# Create a hover over window  #
###############################
import tkinter as tk

class HoverWindow(object):
    '''Create a new window when hovering over a widget'''
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)

    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 40
        y += self.widget.winfo_rooty() + 70
        # creates a toplevel window
        self.hoverWindow = tk.Toplevel(self.widget)
        # Remove title bar of the window
        self.hoverWindow.wm_overrideredirect(True)
        self.hoverWindow.wm_geometry("+%d+%d" % (x, y))
        hoverText = tk.Label(self.hoverWindow, text=self.text, justify='left',
                        background='white', borderwidth=1,
                        font=("Courier", "15"), wraplength = 250)
        hoverText.pack(ipadx=1)

    def leave(self, event=None):
        self.hoverWindow.destroy()