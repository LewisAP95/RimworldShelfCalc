import tkinter as tk
from GridMaker import GridMaker

class MainWindow:

    def __init__(self):
        self.app = tk.Tk()
        self.app.title("RimWorld Shelf Layout Calculator")

        self.left_frame = tk.Frame(self.app, relief="groove", borderwidth=3)
        self.left_frame.grid(row=0, column=0)

        self.right_frame = tk.Frame(self.app, relief="groove", borderwidth=3)
        self.right_frame.grid(row=0, column=1)

        self.grid_maker = GridMaker(self.left_frame, 10)

        self.testlabel3 = tk.Label(self.right_frame, text="main right")
        self.testlabel3.pack()

    def begin(self):
        self.app.mainloop()

if __name__=="__main__":
    w = MainWindow()
    w.begin()