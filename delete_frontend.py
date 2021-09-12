import tkinter as tk
from tkinter import *
import category


def delete_func():
    
    def back():
        category.category()
        del_window.wm_withdraw()
    
    del_window = Tk()
    del_window.title("Short Note Organizer")
    del_window.geometry("650x205+380+250")
    del_window['background'] = '#add8e6'
    
    back_btn = Button(del_window, text="BACK", command=back)
    back_btn.grid(row=0, column=0)
    
    del_view_frame = LabelFrame(del_window)
    del_view_frame.grid(row=1, column=0, padx=10)
    del_view_frame['relief'] = 'sunken'
    
    view_note = Text(del_view_frame, width=50, height=10)
    view_note.grid(row=0, column=0)
    
    del_menu_frame = LabelFrame(del_window, bg="#add8e6")
    del_menu_frame.grid(row=1, column=1)
    del_menu_frame['relief'] = 'flat'
    
    del_text = Label(del_menu_frame, text="Delete Notes\nHere you can look at your\nnotes and check weather you want\nto keep them or not and you\ncan delete any note you wish to delete.\n\nEnter your Title", bg="#add8e6")
    del_text.grid(row=0, column=0)
    
    del_value = StringVar()
    del_title = Entry(del_menu_frame, textvariable=del_value, width=26)
    del_title.grid(row=1, column=0, pady=2)
    
    del_choice = Button(del_menu_frame, text="VIEW", bg="black", fg="#add8e6", width=10)
    del_choice.grid(row=2, column=0, padx=(0,80), pady=3)
    del_btn = Button(del_menu_frame, text="DELETE", bg="black", fg="#add8e6", width=10)
    del_btn.grid(row=2, column=0, padx=(80,0), pady=3)