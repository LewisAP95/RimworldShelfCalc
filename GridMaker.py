import tkinter as tk

class GridMaker:

    def __init__(self, parent, size):
        self.top_frame = tk.Frame(parent)
        self.top_frame.grid(row=0, column=0)
        self.bottom_frame = tk.Frame(parent, relief="ridge", borderwidth=2)
        self.bottom_frame.grid(row=1, column=0)

        #button for the top toolbar
        #clear button should be left justified, other should be right
        self.clear_button = tk.Button(self.top_frame, text="Clear", command=self.clear)
        self.clear_button.grid(row=0, column=0)
        self.edit_button = tk.Button(self.top_frame, text="Edit", command=self.toggle_edit)
        self.edit_button.grid(row=0, column=1)

        self.TEST_BUTTON = tk.Button(self.top_frame, text="OUTPUT VALS", command=self.test_dump_vals)
        self.TEST_BUTTON.grid(row=0, column=2)

        self.editing_enabled = False

        #The grid window itself
        # Default maximum dimensions are 30x30
        self.tile_grid = []

        for x in range(size):
            self.tile_grid.append([])
            for y in range(size):
                self.tile_val = tk.IntVar()
                self.tile = tk.Checkbutton(
                    self.bottom_frame, bd=1, padx=0, pady=0, width=2, indicatoron=False,
                    bg="black", selectcolor="white", state="disabled", variable=self.tile_val)
                self.tile.grid(row=y, column=x)
                self.tile_grid[x].append([])
                self.tile_grid[x][y].append(self.tile)
                self.tile_grid[x][y].append(self.tile_val)

    def test_dump_vals(self):        
        for x in range(len(self.tile_grid)):
            for y in range(len(self.tile_grid)):
                print(f"X:{x}, y:{y}, state:{self.tile_grid[x][y][1].get()}")

    def clear(self):
        for x in self.tile_grid:
            for y in x:
                y[0].deselect()

    def toggle_edit(self):
        if self.editing_enabled:
            self.editing_enabled = False
            self.edit_button.config(text="Edit")
            for x in self.tile_grid:
                for y in x:
                    y[0].config(state="disabled")
        else:
            self.editing_enabled = True
            self.edit_button.config(text="Stop editing")
            for x in self.tile_grid:
                for y in x:
                    y[0].config(state="normal")