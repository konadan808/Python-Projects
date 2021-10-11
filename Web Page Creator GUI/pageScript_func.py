# Web Page Generator                              pageScript_func


import webbrowser
import time
from tkinter import *
import tkinter as tk
from tkinter import messagebox


import pageScript_main
import pageScript_GUI

# GUI Window center function
def center_window(self,w,h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry("{}x{}+{}+{}".format(w,h,x,y))
    return centerGeo


# Webpage generating function
def pageGenerate(self):
    body=body = self.txt_contentEnt.get()
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    html_content = f"<html> <head> </head> <h1> {body} </h1> <body> </body> </html>"
    with open("index.html", "w") as html_file:
        html_file.write(html_content)
        print("HTML file created successfully!!")
    time.sleep(2)
    webbrowser.open_new_tab("index.html")

def close(self):
        self.master.destroy()
    
        

if __name__ == "__main__":
    pass
