import tkinter as tk

class CafeWindow:
    def __init__(self, root, app):
        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Cafes", font=("Arial", 16)).pack(pady=10)

        cafes = ["Cafe Central", "Cafe Relax", "Cafe Atlas"]

        for c in cafes:
            tk.Label(self.frame, text=c).pack()

        tk.Button(self.frame, text="Back", command=app.show_home).pack(pady=20)