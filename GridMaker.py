import tkinter as tk

class GridMaker:

    def __init__(self, parent, size):
        # Creating the frames for the other content
        self.top_frame = tk.Frame(parent)
        self.top_frame.grid(row=0, column=0, sticky="NESW")
        self.bottom_frame = tk.Frame(parent, relief="ridge", borderwidth=2)
        self.bottom_frame.grid(row=1, column=0, sticky="NESW")

        # Buttons for the top toolbar
        self.clear_button = tk.Button(self.top_frame, text="Clear", command=self.clear)
        self.clear_button.grid(row=0, column=0, sticky="NESW")
        self.edit_button = tk.Button(self.top_frame, text="Edit", command=self.toggle_edit)
        self.edit_button.grid(row=0, column=1, sticky="NESW")

        self.editing_enabled = False

        # The grid and grid display
        # Max dimensions are 30*30
        # Grid format is a 3d array, with the first two coords specifying the cell-
        #-and the third whether the actual tile or its variable are accessed
        # i.e. self.tile_grid[x][y][0] is the 'tile' checkbutton, self.tile_grid[x][y][1] is the variable for that tile
        self.tile_grid = []

        if size > 30:
            self.size = 30
        elif size < 0:
            self.size = 1
        else:
            self.size = size
        
        for x in range(self.size):
            self.tile_grid.append([])
            for y in range(self.size):
                self.tile_val = tk.IntVar()
                self.tile = tk.Checkbutton(
                    self.bottom_frame, bd=1, padx=0, pady=0, width=2, indicatoron=False,
                    bg="black", selectcolor="white", state="disabled", variable=self.tile_val)
                self.tile.grid(row=y, column=x, sticky="NESW")
                self.tile_grid[x].append([])
                self.tile_grid[x][y].append(self.tile)
                self.tile_grid[x][y].append(self.tile_val)

        # Grid weight configuration
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(1, weight=19)

        self.top_frame.grid_columnconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(1, weight=1)
        self.top_frame.grid_rowconfigure(0, weight=1)

        for i in range(self.size):
            self.bottom_frame.grid_columnconfigure(i, weight=1)
            self.bottom_frame.grid_rowconfigure(i, weight=1)


    def clear(self):
        # Clears the selection grid by de-selecting all the tile checkbuttons
        for x in self.tile_grid:
            for y in x:
                y[0].deselect()

    def toggle_edit(self):
        # Toggles between editing and not, disabled or enabling the checkbuttons are appropriate
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