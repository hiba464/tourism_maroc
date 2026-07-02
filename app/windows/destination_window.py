import tkinter as tk

class DestinationWindow:
    def __init__(self, root, app):
        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Destinations", font=("Arial", 16)).pack(pady=10)

        destinations = ["Marrakech", "Casablanca", "Fes", "Rabat"]

        for d in destinations:
            tk.Label(self.frame, text=d).pack()

        tk.Button(self.frame, text="Back", command=app.show_home).pack(pady=20)