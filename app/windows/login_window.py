import tkinter as tk
import webbrowser
import os


class LoginWindow(tk.Frame):

    def __init__(self, root, app, controller):

        super().__init__(root)

        self.app = app
        self.controller = controller

        # BACKGROUND
        self.configure(bg="#020617")

        # ANIMATION START POSITION
        self.place(
            x=-1000,
            y=0,
            relwidth=1,
            relheight=1
        )

        # CANVAS
        self.canvas = tk.Canvas(
            self,
            bg="#020617",
            highlightthickness=0
        )

        self.canvas.pack(
            fill="both",
            expand=True
        )

        # ANIMATED CIRCLES
        self.circle1 = self.canvas.create_oval(
            50, 50, 350, 350,
            fill="#2563eb",
            outline=""
        )

        self.circle2 = self.canvas.create_oval(
            900, 400, 1300, 800,
            fill="#7c3aed",
            outline=""
        )

        # LOGIN CARD
        self.card = tk.Frame(
            self.canvas,
            bg="#0f172a",
            padx=50,
            pady=50
        )

        self.card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # TITLE
        tk.Label(
            self.card,
            text="Login",
            font=("Arial", 30, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=20)

        # EMAIL
        tk.Label(
            self.card,
            text="Email",
            font=("Arial", 12),
            bg="#0f172a",
            fg="#cbd5e1"
        ).pack(anchor="w")

        self.email = tk.Entry(
            self.card,
            width=35,
            font=("Arial", 13),
            bg="#1e293b",
            fg="white",
            insertbackground="white",
            relief="flat"
        )

        self.email.pack(
            pady=10,
            ipady=8
        )

        # PASSWORD
        tk.Label(
            self.card,
            text="Password",
            font=("Arial", 12),
            bg="#0f172a",
            fg="#cbd5e1"
        ).pack(anchor="w")

        self.password = tk.Entry(
            self.card,
            show="*",
            width=35,
            font=("Arial", 13),
            bg="#1e293b",
            fg="white",
            insertbackground="white",
            relief="flat"
        )

        self.password.pack(
            pady=10,
            ipady=8
        )

        # LOGIN BUTTON
        self.login_btn = tk.Button(
            self.card,
            text="Login",
            font=("Arial", 14, "bold"),
            bg="#2563eb",
            fg="white",
            activebackground="#1d4ed8",
            activeforeground="white",
            width=20,
            height=2,
            bd=0,
            cursor="hand2",
            command=self.login
        )

        self.login_btn.pack(pady=20)

        # REGISTER BUTTON
        self.register_btn = tk.Button(
            self.card,
            text="Back",
            font=("Arial", 12, "bold"),
            bg="#334155",
            fg="white",
            activebackground="#475569",
            activeforeground="white",
            width=20,
            height=2,
            bd=0,
            cursor="hand2",
            command=self.app.show_home
        )

        self.register_btn.pack()

        # MESSAGE
        self.msg = tk.Label(
            self.card,
            text="",
            font=("Arial", 11),
            bg="#0f172a",
            fg="white"
        )

        self.msg.pack(pady=20)

        # HOVER EFFECTS
        self.login_btn.bind(
            "<Enter>",
            lambda e: self.login_btn.config(
                bg="#1d4ed8"
            )
        )

        self.login_btn.bind(
            "<Leave>",
            lambda e: self.login_btn.config(
                bg="#2563eb"
            )
        )

        # START ANIMATIONS
        self.dx = 2

        self.animate_background()

        self.animate_page()

    # PAGE SLIDE ANIMATION
    def animate_page(self):

        x = -1000

        def slide():

            nonlocal x

            if x < 0:

                x += 25

                self.place(
                    x=x,
                    y=0,
                    relwidth=1,
                    relheight=1
                )

                self.after(
                    10,
                    slide
                )

        slide()

    # BACKGROUND ANIMATION
    def animate_background(self):

        self.canvas.move(
            self.circle1,
            self.dx,
            0
        )

        pos = self.canvas.coords(
            self.circle1
        )

        if pos[2] >= 600 or pos[0] <= 0:
            self.dx *= -1

        self.after(
            30,
            self.animate_background
        )

    # LOGIN
    def login(self):

        email = self.email.get().strip()

        password = self.password.get().strip()

        try:

            user = self.controller.login(
                email,
                password
            )

            print("USER:", user)

            if user:

                self.msg.config(
                    text=f"Welcome {user['name']} ✅",
                    fg="#22c55e"
                )

                path = os.path.abspath(
                    "app/web/index.html"
                )

                webbrowser.open(path)

            else:

                self.msg.config(
                    text="❌ Invalid email or password",
                    fg="red"
                )

        except Exception as e:

            print("ERROR:", e)

            self.msg.config(
                text=str(e),
                fg="red"
            )