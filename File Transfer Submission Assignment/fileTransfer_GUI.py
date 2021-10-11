# File Transfer Submission Assignment                  fileTransfer_GUI

import time
import shutil
import time
import os
import tkinter as tk
from tkinter import *
import tkinter.filedialog
from tkinter import filedialog as fd

# module imports
import fileTransfer_main
import fileTransfer_func

def load_gui(self):
    #Button Layout
    self.btn_source = tk.Button(self.master, width=12, height=2, text="File Source",command=lambda: fileTransfer_func.setSrc(self))
    self.btn_source.grid(row=0, column=0, padx=(10,10),pady=(50,10), sticky=W)
    self.btn_destination = tk.Button(self.master, width=12, height=2, text="File Destination",command=lambda: fileTransfer_func.setDest(self))
    self.btn_destination.grid(row=1, column=0, padx=(10,10),pady=(10,10), sticky=W)
    self.btn_check = tk.Button(self.master, width=12, height=2, text="Check Files", command=lambda: fileTransfer_func.transferFiles(self))
    self.btn_check.grid(row=2, column=1, padx=(10,10),pady=(10,10), sticky=W+E)
    self.btn_close = tk.Button(self.master, width=12, height=2, text="Close Program", command=lambda: fileTransfer_func.close(self))
    self.btn_close.grid(row=2, column=2, padx=(10,10),pady=(10,10), sticky=W+E)
    #Text Entry Layout
    self.txt_source = tk.Entry(self.master, text="")
    self.txt_source.grid(row=0, column=1, columnspan=2, padx=(10,10),pady=(50,10),ipadx=100, ipady=5)
    self.txt_destination = tk.Entry(self.master, text="")
    self.txt_destination.grid(row=1, column=1, columnspan=2, padx=(10,10),pady=(10,10),ipadx=100, ipady=5)
    



if __name__ == "__main__":
    pass
