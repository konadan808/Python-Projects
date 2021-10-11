# File Transfer Submission Assignment                  fileTransfer_func

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
import fileTransfer_GUI
    #Closes window function
def close(self):
    self.master.destroy()
    #Center window function
def center_window(self,w,h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry("{}x{}+{}+{}".format(w,h,x,y))
    return centerGeo
    #Set source folder function
def setSrc(self):
    source = fd.askdirectory()
    self.txt_source.insert(0,source)
    return source
    #Set destination folder function
def setDest(self):
    destination = fd.askdirectory()
    self.txt_destination.insert(0,destination)
    return destination
    #File transfer function
def transferFiles(self):
    seconds_in_day = 24*60*60
    now = time.time()
    before = now - seconds_in_day
    source = self.txt_source.get()
    destination = self.txt_destination.get()
    def last_mod_time(fname):
        return os.path.getmtime(fname)
    for fname in os.listdir(source):
        src_fname = os.path.join(source, fname)
        if last_mod_time(src_fname) > before:
            dst_fname = os.path.join(destination, fname)
            shutil.move(src_fname, dst_fname)    










if __name__ == "__main__":
    pass
