import tkinter as tk
from tkinter import *
import add_frontend
import delete_frontend
import backend

def category():
    def btn1():
        add_frontend.add_frontend()
        category_window.wm_withdraw()
    def btn2():
        delete_frontend.delete_func()
        category_window.wm_withdraw()
        

    category_window = tk.Tk()
    category_window.title("Short Note Organizer")
    category_window.geometry("650x205+380+250")
    category_window.resizable(width=False, height=False)
    category_window['background'] = "#add8e6"
    
    menu_frame = LabelFrame(category_window, text="Menu", bg="#add8e6")
    menu_frame.grid(row=0, column=0, padx=10, pady=2 )
    add_btn = Button(menu_frame, text = "Add Note", width=10, bg="black", fg="#add8e6",command=btn1 )
    add_btn.pack()
    del_btn = Button(menu_frame, text = "Delete Note", width=10, bg="black", fg="#add8e6", command=btn2)
    del_btn.pack()
    ser_btn = Button(menu_frame, text = "Search Note", width=10, bg="black", fg="#add8e6")
    ser_btn.pack()
    view_btn = Button(menu_frame, text="View Notes", width=10, bg="black", fg="#add8e6")
    view_btn.pack()
    close_btn = Button(menu_frame, text="Close", width=10, bg="black", fg="#add8e6", command=backend.close)
    close_btn.pack()
 
    
    menu_intro = LabelFrame(category_window, bg="#add8e6")
    menu_intro.grid(row=0, column=1)
    menu_intro['relief'] = 'flat'
    
    intro_text = Label(menu_intro, text="Hey welcome y'all what do you want to do today\n\nAdd Notes that you take while studying?\nDelete Notes you don't use anymore?\nSearch for Notes you stored and read them?\n\nWell you have come to the right place, \nhere you can do all these and it's completely free, Enjoy!!!", justify=CENTER, bg="#add8e6")
    intro_text.pack(padx=(65,0), pady=20)
    intro_text.config(font=15)
    