import tkinter as tk

def create_button(parent, text, command=None):
    return tk.Button(parent, text=text, bg="#3498db", fg="white",
                     padx=10, pady=5, command=command)