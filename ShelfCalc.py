import tkinter as tk
from GridMaker import GridMaker
from OptionsPane import OptionsPane

class MainWindow:

    def __init__(self):
        # Main window and internal frames setup
        self.app = tk.Tk()
        self.app.title("RimWorld Shelf Layout Calculator")
        self.app.geometry("700x400")
        self.app.minsize(500, 200)

        self.left_frame = tk.Frame(self.app, relief="groove", borderwidth=3)
        self.left_frame.grid(row=0, column=0, sticky="NESW")

        self.right_frame = tk.Frame(self.app, relief="groove", borderwidth=3)
        self.right_frame.grid(row=0, column=1, sticky="NESW")

        # Grid weight configuration
        self.app.grid_columnconfigure(0, weight=3)
        self.app.grid_columnconfigure(1, weight=1)
        self.app.grid_rowconfigure(0, weight=1)

        self.grid_maker = GridMaker(self.left_frame, 10)
        self.options_pane = OptionsPane(self, self.right_frame)

    def begin(self):
        self.app.mainloop()

    def enter_entrance_placement(self):
        print(".< A")

if __name__=="__main__":
    w = MainWindow()
    w.begin()