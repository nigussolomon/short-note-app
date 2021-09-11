import tkinter as tk
from tkinter import *
import backend
import category


def add_frontend():
    backend.connect()
    backend.create()

    def put():
        backend.insert_val(add_val.get().lower(),add_data.get("1.0", "end-1c").lower())
    
    def back():
        category.category()
        window.wm_withdraw()

    window = tk.Tk()
    
    window.title('Short Note Organizer')
    window['background'] = 'light blue'
    window.geometry("650x235+380+250")
    window.resizable(width=False, height=False)
    
    frame_back = LabelFrame(window, bg= "#add8e6")
    frame_back.grid(row=0, column=0,padx=10)
    frame_back['relief'] = 'flat'
    
    back = Button(frame_back, text="BACK", command=back)
    back.grid(row=0, column=0)
    
    frame_data = LabelFrame(window, text="Welcome", bg='#add8e6')
    frame_data.grid(row=1, column=0, padx=10, pady=8)
    frame_data['relief'] = 'sunken'

    add_data = Text(frame_data, width=50, height=10)
    add_data.grid(row=0, column=0, padx=3, pady=3)

    frame_2 = LabelFrame(window, bg='light blue')
    frame_2.grid(row=1, column=1, padx=10, pady=10)
    frame_2['relief']='flat'

    add = Label(frame_2, text='ADD NOTES \n Here you can store your \n notes and you can add them to the \n database so you can access it later. \n \n \n Add your title', justify=LEFT, bg='#ADD8E6')
    add.grid(row=0, column=0)

    add_val = StringVar()
    add_view = Entry(frame_2, textvariable=add_val, width=32)
    add_view.grid(row=1, column=0, pady=5)

    add_btn = Button(frame_2, text='Add Note', command= put, bg="black", fg="light blue")
    add_btn.grid(row=3, column=0, pady=2,  sticky=tk.E)
    add_btn['relief']='raised'
