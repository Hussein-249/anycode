'''
Name:       applicationwindow.py
Updated:    18-10-2023

This file will contain the necessary code for a login form upon program startup.
'''

import tkinter as tk
import logging
import time

import app

window = tk.Tk()

def login_command(keyboard_event = None):
    if username_entry.get() == "admin" or password_entry.get() == "password":
        logging.debug("Admin credentials entered, now logging in.")
        
        for widget in login_frame.winfo_children():
            widget.destroy()

        time.sleep(1)

        loggingin_label = tk.Label(
        master= login_frame,
        text="Logging in...",
        font=("Garamond", 12),
        bg="#303030",
        fg="white",
        )

        loggingin_label.place(relx=0.5, rely=0.5, anchor='center')

        time.sleep(1)

        window.destroy()

        app.openApp()
        return 0

    else:
        logging.debug("Invalid credentials")

        return 1
        
# Creating 3 frames

left_frame = tk.Frame(
    master=window,
    width=500,
    height=360,
    bg="#303030",
    padx=50
    )

left_frame.pack(
    fill=tk.BOTH,
    side=tk.LEFT,
    expand=True,              
    )

login_frame = tk.Frame(master=window, width=320, height=360, bg="#303030")

login_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

padding_frame = tk.Frame(master=window, width=20, height=360, bg="#303030")

padding_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

welcome_label = tk.Label(
    master= left_frame,
    text="Welcome to the Fleet Manager",
    font=("Garamond", 12),
    bg="#303030",
    fg="white",
    )

welcome_label.place(relx=0.5, rely=0.5, anchor='center', )

image = tk.PhotoImage(file="media/login_icon2.png")

# Create a label and add the image to it
image_label = tk.Label(
    master=left_frame,
    image=image,
    bg="#303030")

image_label.pack()

# This is for a login form
# Username and password forms

username_label = tk.Label(
    master=login_frame,
    text="Username",
    font=("Garamond", 12),
    )

password_label = tk.Label(
    master=login_frame,
    text="Login",
    font=("Garamond", 12),
    )

login_button = tk.Button(
    master=login_frame,
    activebackground="#202020",
    activeforeground="white",
    text="LOGIN",
    font=("Tahoma", 12),
    width=20,
    height=3,
    bg="#303030",
    fg="white",
    command=login_command
)

#  Entry forms

username_entry = tk.Entry(
    master=login_frame,
    text="Username",
    width=25,
    )

username_entry.bind('<Return>', login_command)

password_entry = tk.Entry(
    master=login_frame,
    text="Password",
    width=25,
    )

# ALL PACKING

username_label.pack()

username_entry.pack()

password_label.pack()

password_entry.pack()

# login_button.place(relx=0.5, rely=0.5, anchor='center')

login_button.grid(row=0)

window.mainloop()

logging.debug("Tkinter window mainloop started.")