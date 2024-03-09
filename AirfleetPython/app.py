import tkinter as tk
import logging


import userClass

def openApp():

    window = tk.Tk()

    window.attributes('-fullscreen',True)

    templabel = tk.Label(
    master=window,
    text="Welcome to the manager app, Admin",
    font=("Garamond", 12),
    )

    templabel.pack()

    window.mainloop()
    
