import tkinter as tk

class ConverterWindow:
    def __init__(self, root, app):
        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame, text="Currency Converter", font=("Arial", 16)).pack(pady=10)

        self.amount = tk.Entry(self.frame)
        self.amount.pack(pady=5)

        tk.Label(self.frame, text="MAD → USD (demo)").pack()

        tk.Button(self.frame, text="Convert", command=self.convert).pack(pady=10)
        tk.Button(self.frame, text="Back", command=app.show_home).pack()

    def convert(self):
        amount = self.amount.get()
        print("Convert:", amount)