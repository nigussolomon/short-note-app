import tkinter as tk
from tkinter import *
from tkinter import font
import backend
import category

def search_frontend():
    
    backend.connect()
    backend.create()
    
    def searching():
        diplay.delete("1.0", END)
        for par in backend.search(searchval.get()):
            diplay.insert(END, par)
    
    def back():
        category.category()
        search_window.wm_withdraw()
        pass

    
    search_window = tk.Tk()
    search_window.geometry("690x235+380+250")
    search_window['background'] = '#00EEEE'
    search_window.resizable(width=False, height=False)
    search_window.title("Short Note Organizer")
    
    back_btn= Button(search_window, text="BACK", command=back, bg="#00EEEE")
    back_btn.grid(row=0, column=0, sticky=tk.W, padx=3, pady=3)
    back_btn.config(font=('Helvetica', 6, 'bold'))
    
    display_frame = LabelFrame(search_window)
    display_frame.grid(row=1, column=0, sticky=tk.N, pady=20, padx=10)
    display_frame['relief'] = 'sunken'
    
    diplay = Text(display_frame, width=70, height=15)
    diplay.config(font = ('Helvetica', 10 ,'bold'))
    diplay.pack()
    
    search_menu = LabelFrame(search_window, bg="#00EEEE")
    search_menu.grid(row=2, column=0, padx=10, pady=15)
    search_menu['relief'] = 'flat'
    
    searchval = StringVar(search_window)
    search_box = Entry(search_menu,textvariable=searchval, width=40)
    search_box.grid(row=0, column=0)
    
    search_btn = Button(search_menu, text="SEARCH", command=searching)
    search_btn.grid(row=1, column=0)