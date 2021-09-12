import tkinter as tk
from tkinter import *
import category

window = tk.Tk()
window.iconbitmap(default='icon.ico')
window.title("Short Note Organizer")
window['background'] = '#00eeee'
window.geometry("690x235+380+250")
window.resizable(width=False, height=False)

def open():
    category.category()
    window.wm_withdraw()



welcome_intro = Label(window, text="Welcome to Short Note Organizer where you can organize and arrange your notes.", bg="#00eeee")
welcome_intro.config(font=('Helvetica',12, 'bold'))
welcome_intro.pack(pady=(80,10))
welcome_btn = Button(window, text="WELCOME", command=open, width=10, bg="black", fg="#00eeee")
welcome_btn.config(font=('Helvetica', 8,'bold'))
welcome_btn.pack()

window.mainloop()