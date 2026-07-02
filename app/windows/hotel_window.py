import tkinter as tk

class HotelWindow(tk.Frame):
    def __init__(self, root, app):
        super().__init__(root)

        self.app = app

        self.configure(bg="#0f172a")

        self.pack(fill="both", expand=True)

        tk.Label(
            self,
            text="🏨 Hotels",
            font=("Arial", 28, "bold"),
            bg="#0f172a",
            fg="white"
        ).pack(pady=30)

        hotels = [
            ("Hotel Atlas", "Marrakech"),
            ("Rabat Palace", "Rabat"),
            ("Casablanca View", "Casablanca")
        ]

        for name, city in hotels:
            card = tk.Frame(
                self,
                bg="#1e293b",
                padx=20,
                pady=20
            )

            card.pack(pady=15, padx=40, fill="x")

            tk.Label(
                card,
                text=name,
                font=("Arial", 18, "bold"),
                bg="#1e293b",
                fg="white"
            ).pack(anchor="w")

            tk.Label(
                card,
                text=city,
                font=("Arial", 12),
                bg="#1e293b",
                fg="#cbd5e1"
            ).pack(anchor="w")

            tk.Button(
                card,
                text="Book Now",
                bg="#2563eb",
                fg="white",
                bd=0
            ).pack(anchor="e", pady=10)

        tk.Button(
            self,
            text="Back",
            bg="#334155",
            fg="white",
            width=20,
            command=self.app.show_home
        ).pack(pady=30)