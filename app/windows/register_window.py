import tkinter as tk


class RegisterWindow(tk.Frame):

    def __init__(self, root, app, controller):

        super().__init__(root)

        self.app = app
        self.controller = controller

        # BACKGROUND
        self.configure(bg="#020617")

        # START POSITION
        self.place(
            x=1000,
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

        # CARD
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
            text="Register",
            font=("Arial", 30, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=20)

        # NAME
        tk.Label(
            self.card,
            text="Name",
            font=("Arial", 12),
            bg="#0f172a",
            fg="#cbd5e1"
        ).pack(anchor="w")

        self.name = tk.Entry(
            self.card,
            width=35,
            font=("Arial", 13),
            bg="#1e293b",
            fg="white",
            insertbackground="white",
            relief="flat"
        )

        self.name.pack(
            pady=10,
            ipady=8
        )

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

        # REGISTER BUTTON
        self.register_btn = tk.Button(
            self.card,
            text="Register",
            font=("Arial", 14, "bold"),
            bg="#7c3aed",
            fg="white",
            activebackground="#6d28d9",
            activeforeground="white",
            width=20,
            height=2,
            bd=0,
            cursor="hand2",
            command=self.register
        )

        self.register_btn.pack(pady=20)

        # BACK BUTTON
        self.back_btn = tk.Button(
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

        self.back_btn.pack()

        # MESSAGE
        self.msg = tk.Label(
            self.card,
            text="",
            font=("Arial", 11),
            bg="#0f172a",
            fg="white"
        )

        self.msg.pack(pady=20)

        # HOVER
        self.register_btn.bind(
            "<Enter>",
            lambda e: self.register_btn.config(
                bg="#6d28d9"
            )
        )

        self.register_btn.bind(
            "<Leave>",
            lambda e: self.register_btn.config(
                bg="#7c3aed"
            )
        )

        # ANIMATIONS
        self.dx = 2

        self.animate_background()

        self.animate_page()

    # PAGE ANIMATION
    def animate_page(self):

        x = 1000

        def slide():

            nonlocal x

            if x > 0:

                x -= 25

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

    # BACKGROUND
    def animate_background(self):

        self.canvas.move(
            self.circle2,
            self.dx,
            0
        )

        pos = self.canvas.coords(
            self.circle2
        )

        if pos[2] >= 1400 or pos[0] <= 500:
            self.dx *= -1

        self.after(
            30,
            self.animate_background
        )

    # REGISTER
    def register(self):

        name = self.name.get().strip()

        email = self.email.get().strip()

        password = self.password.get().strip()

        try:

            result = self.controller.register(
                name,
                email,
                password
            )

            self.msg.config(
                text=result,
                fg="#22c55e"
            )

        except Exception as e:

            self.msg.config(
                text=str(e),
                fg="red"
            )