


import tkinter as tk
from app.main_window import MainWindow

if __name__ == "__main__":
    print("STEP 1 - START")

    root = tk.Tk()

    print("STEP 2 - ROOT CREATED")

    app = MainWindow(root)

    print("STEP 3 - MAINWINDOW CREATED")


    root.mainloop()