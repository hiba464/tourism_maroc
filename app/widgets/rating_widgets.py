import tkinter as tk

class RatingWidget:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        self.stars = []
        self.rating = 0

        for i in range(5):
            btn = tk.Button(self.frame, text="☆",
                            command=lambda i=i: self.set_rating(i+1))
            btn.pack(side="left")
            self.stars.append(btn)

    def set_rating(self, value):
        self.rating = value
        for i in range(5):
            self.stars[i].config(text="★" if i < value else "☆")