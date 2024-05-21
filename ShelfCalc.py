import tkinter as tk

class MainWindow:

    def __init__(self):
        self.app = tk.Tk()
        self.app.title("RimWorld Shelf Layout Calculator")

        self.left_frame = tk.Frame(self.app, relief="groove", borderwidth=3)
        self.left_frame.grid(row=0, column=0)

        self.right_frame = tk.Frame(self.app, relief="groove", borderwidth=3)
        self.right_frame.grid(row=0, column=1)

        self.left_frame_top = tk.Frame(self.left_frame)
        self.left_frame_top.grid(row=0, column=0)
        self.left_frame_bottom = tk.Frame(self.left_frame, relief="ridge", borderwidth=2)
        self.left_frame_bottom.grid(row=1, column=0)

        self.testlabel1 = tk.Label(self.left_frame_top, text="main left inner upper")
        self.testlabel2 = tk.Label(self.left_frame_bottom, text="main left inner lower")
        self.testlabel1.pack()
        self.testlabel2.pack()

        self.testlabel3 = tk.Label(self.right_frame, text="main right")
        self.testlabel3.pack()

    def begin(self):
        self.app.mainloop()

if __name__=="__main__":
    w = MainWindow()
    w.begin()