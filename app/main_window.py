import tkinter as tk

from app.windows.home_window import HomeWindow
from app.windows.login_window import LoginWindow
from app.windows.register_window import RegisterWindow

from app.controllers.user_controller import UserController


class MainWindow:

    def __init__(self, root):

        self.root = root

        self.root.title("Tourism Maroc")
        self.root.geometry("1000x700")
        self.root.configure(bg="#0f172a")

        self.user_controller = UserController()

        self.current_frame = None

        self.show_home()

    # CLEAR WINDOW
    def clear(self):

        if self.current_frame:

            self.current_frame.pack_forget()

            self.current_frame.destroy()

    # HOME
    def show_home(self):

        self.clear()

        self.current_frame = HomeWindow(
            self.root,
            self
        )

    # LOGIN
    def show_login(self):

        print("OPEN LOGIN")

        self.clear()

        self.current_frame = LoginWindow(
            self.root,
            self,
            self.user_controller
        )

    # REGISTER
    def show_register(self):

        print("OPEN REGISTER")

        self.clear()

        self.current_frame = RegisterWindow(
            self.root,
            self,
            self.user_controller
        )