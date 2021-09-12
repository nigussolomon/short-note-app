import tkinter as tk
from tkinter import *
import category
import backend


def delete_func():
    def viewer():
        view_note.delete("1.0", END)
        for par in backend.search(del_value.get()):
            view_note.insert(END, par)
            view_note.insert(END, "\n")
    
    
    def back():
        category.category()
        del_window.wm_withdraw()
        
    def removing():
        backend.det(del_value.get())
    
    del_window = Tk()
    del_window.title("Short Note Organizer")
    del_window.geometry("690x235+380+250")
    del_window['background'] = '#00EEEE'
    
    back_btn = Button(del_window, text="BACK", command=back, bg="#00EEEE")
    back_btn.grid(row=0, column=0, sticky=tk.W, padx=3, pady=3)
    back_btn.config(font=('Helvetica', 6, 'bold'))
    
    del_view_frame = LabelFrame(del_window)
    del_view_frame.grid(row=1, column=0, padx=10)
    del_view_frame['relief'] = 'sunken'
    
    view_note = Text(del_view_frame, width=50, height=10)
    view_note.grid(row=0, column=0)
    
    del_menu_frame = LabelFrame(del_window, bg="#00EEEE")
    del_menu_frame.grid(row=1, column=1)
    del_menu_frame['relief'] = 'flat'
    
    del_text = Label(del_menu_frame, text="Delete Notes\nHere you can look at your\nnotes and check weather you want\nto keep them or not and you\ncan delete any note you wish to delete.\n\nEnter your Title", bg="#00EEEE", justify=LEFT)
    del_text.config(font=('Helvetica', 10, 'bold'))
    del_text.grid(row=0, column=0)
    
    
    del_value = StringVar(del_window)
    del_title = Entry(del_menu_frame, textvariable=del_value, width=36)
    del_title.grid(row=1, column=0, pady=2)
    
    del_choice = Button(del_menu_frame, text="VIEW", bg="black", fg="#00EEEE", width=10, command=viewer)
    del_choice.config(font=('Helvetica', 8, 'bold'))
    del_choice.grid(row=2, column=0, padx=(0,80), pady=3)
    del_btn = Button(del_menu_frame, text="DELETE", bg="black", fg="#00EEEE", width=10, command=removing)
    del_btn.config(font=('Helvetica', 8, 'bold'))
    del_btn.grid(row=2, column=0, padx=(80,0), pady=3)