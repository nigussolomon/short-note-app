import tkinter as tk
from tkinter import *
import category

window = tk.Tk()
window.iconbitmap(default='favicon.ico')
window.title("Short Note Organizer")
window['background'] = '#add8e6'
window.geometry("650x205+380+250")
window.resizable(width=False, height=False)

def open():
    category.category()
    window.wm_withdraw()


welcome_intro = Label(window, text="Welcome to Short Note Organizer where you can organize and arrange your notes.", bg="#add8e6")
welcome_intro.config(font=15)
welcome_intro.pack(pady=(60,10))
welcome_btn = Button(window, text="start", command=open, width=10, bg="black", fg="#add8e6")
welcome_btn.pack()

window.mainloop()