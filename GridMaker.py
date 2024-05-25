import tkinter as tk
from tkinter import Button

class GridMaker:

    def __init__(self, parent, size):
        self.top_frame = tk.Frame(parent)
        self.top_frame.grid(row=0, column=0)
        self.bottom_frame = tk.Frame(parent, relief="ridge", borderwidth=2)
        self.bottom_frame.grid(row=1, column=0)

        #button for the top toolbar
        #clear button should be left justified, other two should be right
        #Buttons also still need commands
        self.clear_button = Button(self.top_frame, text="Clear", command=self.clear)
        self.clear_button.grid(row=0, column=0)
        self.entrance_button = Button(self.top_frame, text="Place entrances")
        self.entrance_button.grid(row=0, column=1)
        self.edit_button = Button(self.top_frame, text="Edit", command=self.toggle_edit)
        self.edit_button.grid(row=0, column=2)

        self.editing_enabled = False

        #The grid window itself
        # Default maximum dimensions are 30x30
        self.tile_grid = []

        for x in range(size):
            self.tile_grid.append([])
            for y in range(size):
                self.tile = tk.Checkbutton(self.bottom_frame, bd=1, padx=0, pady=0, width=2, indicatoron=False, bg="black", selectcolor="white", state="disabled")
                self.tile.grid(row=y, column=x)
                self.tile_grid[x].append(self.tile)

    def clear(self):
        for x in self.tile_grid:
            for y in x:
                y.deselect()

    def toggle_edit(self):
        if self.editing_enabled:
            self.editing_enabled = False
            self.edit_button.config(text="Edit")
            for x in self.tile_grid:
                for y in x:
                    y.config(state="disabled")
        else:
            self.editing_enabled = True
            self.edit_button.config(text="Stop editing")
            for x in self.tile_grid:
                for y in x:
                    y.config(state="normal")