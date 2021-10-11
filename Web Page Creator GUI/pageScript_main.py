# Web Page Generator                              pageScript_main


import webbrowser
import time
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import pageScript_GUI
import pageScript_func

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
html_content = f"<html> <head> </head> <h1> Stay Tuned for our Amazing Summer Sale! </h1> <body> </body> </html>"

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        #GUI window characteristics
        self.master = master
        self.master.minsize(400,200)
        self.master.maxsize(400,200)
        self.master.title("Web Page Generator")
        self.master.configure(bg = "#F0F0F0")

        #Center GUI Window
        pageScript_func.center_window(self,500,300)
        #load GUI
        pageScript_GUI.load_gui(self)

    
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
