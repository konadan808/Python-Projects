# File Transfer Submission Assignment                  fileTransfer_main



import time
import shutil
import time
import os
import tkinter as tk
from tkinter import *
import tkinter.filedialog
from tkinter import filedialog as fd

# module imports
import fileTransfer_GUI
import fileTransfer_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        #Window characteristics
        self.master = master
        self.master.minsize(500,250)
        self.master.maxsize(500,250)
        self.master.title("File Sorter")
        self.master.configure(bg = "#F0F0F0")
        #Center Window
        fileTransfer_func.center_window(self,500,300)
        #Load GUI
        fileTransfer_GUI.load_gui(self)





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

