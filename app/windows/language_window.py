import tkinter as tk

class LanguageWindow:
    def __init__(self, root, app):
        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Choose Language", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.frame, text="Arabic").pack(pady=5)
        tk.Button(self.frame, text="French").pack(pady=5)
        tk.Button(self.frame, text="English").pack(pady=5)

        tk.Button(self.frame, text="Back", command=app.show_home).pack(pady=20)