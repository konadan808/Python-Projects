# Web Page Generator                              pageScript_GUI


import webbrowser
import time
from tkinter import *
import tkinter as tk
from tkinter import messagebox


# Be sure to import our other modules 
# so we can have access to them
import pageScript_main
import pageScript_func



def load_gui(self):
    
    self.lbl_info = tk.Label(self.master,text="Please enter the text you'd like to appear on your website")
    self.lbl_info.grid(row = 1, column = 0, columnspan=2, padx=(50,50),pady=(20,20))

    self.btn_submit = tk.Button(self.master, width=14, height=2, text="Create Webpage",command=lambda: pageScript_func.pageGenerate(self))
    self.btn_submit.grid(row=3,column=0, padx=(50,50), pady=(20,20))
    self.btn_closeProgram = tk.Button(self.master, width=12, height=2, text="Close Program",command=lambda: pageScript_func.close(self))
    self.btn_closeProgram.grid(row=3,column=1, padx=(50,50),pady=(20,20))

    self.txt_contentEnt = tk.Entry(self.master, text = "")
    self.txt_contentEnt.grid(row=2, column = 0, columnspan=2, padx=(20,20), pady =(0,0), ipadx=100, ipady=2)
    
   
if __name__ == "__main__":
    pass


