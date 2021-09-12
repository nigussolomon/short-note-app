import tkinter as tk
from tkinter import *
import backend

def search_frontend():
    
    backend.connect()
    backend.create()
    
    def searching():
        diplay.delete("1.0", END)
        for par in backend.search(searchval.get()):
            diplay.insert(END, par)
            diplay.insert(END, "\n")

    
    search_window = tk.Tk()
    search_window.geometry("690x235+380+250")
    search_window['background'] = '#00EEEE'
    search_window.resizable(width=False, height=False)
    search_window.title("Short Note Organizer")
    
    display_frame = LabelFrame(search_window)
    display_frame.grid(row=1, column=0, sticky=tk.N, pady=20)
    display_frame['relief'] = 'sunken'
    
    diplay = Text(display_frame, width=50, height=10)
    diplay.pack()
    
    search_menu = LabelFrame(search_window, bg="#00EEEE")
    search_menu.grid(row=1, column=1, padx=10, pady=15)
    search_menu['relief'] = 'flat'
    
    searchval = StringVar(search_window)
    search_box = Entry(search_menu,textvariable=searchval, width=40)
    search_box.pack()
    
    search_btn = Button(search_menu, text="SEARCH", command=searching)
    search_btn.pack(pady=3, padx=(183,0))