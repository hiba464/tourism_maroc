import tkinter as tk

class CardWidget:
    def __init__(self, parent, title, description):
        self.frame = tk.Frame(parent, bd=2, relief="groove", padx=10, pady=10)

        tk.Label(self.frame, text=title, font=("Arial", 14, "bold")).pack(anchor="w")
        tk.Label(self.frame, text=description, wraplength=200).pack(anchor="w")
