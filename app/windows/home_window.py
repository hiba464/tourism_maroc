import tkinter as tk
import webbrowser
import os


class HomeWindow(tk.Frame):

    def __init__(self, root, app):

        super().__init__(root)

        self.app = app

        self.configure(bg="#020617")

        self.pack(
            fill="both",
            expand=True
        )

        # TITLE
        tk.Label(

            self,

            text="Morocco Travel ✈",

            font=("Arial", 35, "bold"),

            bg="#020617",

            fg="white"

        ).pack(pady=80)

        # DESCRIPTION
        tk.Label(

            self,

            text=
            "Luxury Tourism Platform",

            font=("Arial", 16),

            bg="#020617",

            fg="#94a3b8"

        ).pack(pady=10)

        # OPEN LOGIN BUTTON
        tk.Button(

            self,

            text="Open Login",

            font=("Arial", 14, "bold"),

            bg="#2563eb",

            fg="white",

            width=20,

            height=2,

            bd=0,

            cursor="hand2",

            command=self.open_login

        ).pack(pady=40)

    def open_login(self):

        path = os.path.abspath(
            "app/web/login.html"
        )

        webbrowser.open(path)