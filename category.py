import tkinter as tk
from tkinter import *
import add_frontend
import delete_frontend
import backend
import search_frontend

def category():
    def btn1():
        add_frontend.add_frontend()
        category_window.wm_withdraw()
    def btn2():
        delete_frontend.delete_func()
        category_window.wm_withdraw()
    def btn3():
        search_frontend.search_frontend()
        category_window.wm_withdraw()
        
        

    category_window = tk.Tk()
    category_window.title("Short Note Organizer")
    category_window.geometry("690x235+380+250")
    category_window.resizable(width=False, height=False)
    category_window['background'] = "#00eeee"
    
    menu_frame = LabelFrame(category_window, text="Menu", bg="#00eeee")
    menu_frame.grid(row=0, column=0, padx=10, pady=2 )
    
    add_btn = Button(menu_frame, text = "Add Note", width=10, bg="black", fg="#00eeee",command=btn1 )
    add_btn.config(font=('Helvetica',10, 'bold'))
    add_btn.pack()
    
    del_btn = Button(menu_frame, text = "Delete Note", width=10, bg="black", fg="#00eeee", command=btn2)
    del_btn.config(font=('Helvetica',10, 'bold'))
    del_btn.pack()
    
    ser_btn = Button(menu_frame, text = "Search Note", width=10, bg="black", fg="#00eeee", command=btn3)
    ser_btn.config(font=('Helvetica',10, 'bold'))
    ser_btn.pack()
    
    view_btn = Button(menu_frame, text="View Notes", width=10, bg="black", fg="#00eeee")
    view_btn.config(font=('Helvetica',10, 'bold'))
    view_btn.pack()
    
    close_btn = Button(menu_frame, text="Close", width=10, bg="black", fg="#00eeee", command=backend.close)
    close_btn.config(font=('Helvetica',10, 'bold'))
    close_btn.pack()
 
    
    menu_intro = LabelFrame(category_window, bg="#00eeee")
    menu_intro.grid(row=0, column=1)
    menu_intro['relief'] = 'flat'
    
    intro_text = Label(menu_intro, text="Hey welcome y'all what do you want to do today\n\nAdd Notes that you take while studying?\nDelete Notes you don't use anymore?\nSearch for Notes you stored and read them?\n\nWell you have come to the right place, \nhere you can do all these and it's completely free, Enjoy!!!", justify=CENTER, bg="#00eeee")
    intro_text.pack(padx=(50,0), pady=20)
    intro_text.config(font=('Helvetica',12, 'bold'))
    