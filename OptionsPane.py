import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from OptionsBatch import OptionsBatch

class OptionsPane:

    def __init__(self, main_app, parent):
        # Creating the frames for the other content
        self.parent = parent
        self.main_app = main_app
        self.top_frame = tk.Frame(self.parent, relief="groove", borderwidth=2)
        self.top_frame.grid(row=0, column=0, sticky="NESW")
        self.bottom_frame = tk.Frame(self.parent)
        self.bottom_frame.grid(row=1, column=0, sticky="NESW")

        # Top frame UI elements
        self.cut_corners_choice = tk.IntVar()
        self.cut_corners_button =  tk.Checkbutton(self.top_frame, text="Allow corner cutting?", variable=self.cut_corners_choice)
        self.cut_corners_button.grid(row=0, column=0, columnspan=2, sticky="NESW")
        self.cut_corners_button.select()

        self.allow_climbing_choice = tk.IntVar()
        self.allow_climbing_button = tk.Checkbutton(self.top_frame, text="Allow climbing?", variable=self.allow_climbing_choice)
        self.allow_climbing_button.grid(row=1, column=0, columnspan=2, sticky="NESW")
        self.allow_climbing_button.select()

        self.respect_paths_choice = tk.IntVar()
        self.respect_paths_button = tk.Checkbutton(self.top_frame, text="Respect other paths?", variable=self.respect_paths_choice)
        self.respect_paths_button.grid(row=2, column=0, columnspan=2, sticky="NESW")

        self.method_label = tk.Label(self.top_frame, text="Method:")
        self.method_label.grid(row=3, column=0, sticky="NESW")
        self.method_box = ttk.Combobox(self.top_frame, state="readonly", values=["Best first", "Worst first", "Random", "Grid fill"])
        self.method_box.grid(row=3, column=1, sticky="NESW")
        self.method_box.current(0)

        self.placement_steps_label = tk.Label(self.top_frame, text="Max placement attempts:")
        self.placement_steps_label.grid(row=4, column=0, sticky="NESW")
        self.placement_steps_box = ttk.Combobox(self.top_frame, state="readonly", values=list(range(1, 101)))
        self.placement_steps_box.grid(row=4, column=1, sticky="NESW")
        self.placement_steps_box.current(4)

        self.time_limit_label = tk.Label(self.top_frame, text="Global time limit (seconds):")
        self.time_limit_label.grid(row=5, column=0, sticky="NESW")
        self.time_limit_entrybox = tk.Entry(self.top_frame, exportselection=0)
        self.time_limit_entrybox.grid(row=5, column=1, sticky="NESW")
        self.time_limit_entrybox.insert(0, "300")

        # Bottom frame UI elements
        self.back_button = tk.Button(self.bottom_frame, text="Go back", state="disabled", command=self.back)
        self.back_button.grid(row=0, column=0, sticky="NESW")

        self.help_button = tk.Button(self.bottom_frame, text="Help", command=self.display_help)
        self.help_button.grid(row=0, column=1, sticky="NESW")

        self.default_button = tk.Button(self.bottom_frame, text="Reset to default", command=self.default_options)
        self.default_button.grid(row=0, column=2, sticky="NESW")

        self.proceed_button = tk.Button(self.bottom_frame, text="Proceed", command=self.proceed)
        self.proceed_button.grid(row=0, column=3, sticky="NESW")

        # Grid weight configuration

        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.grid_rowconfigure(0, weight=8)
        self.parent.grid_rowconfigure(1, weight=2)

        self.top_frame.grid_columnconfigure(0, weight=3)
        self.top_frame.grid_columnconfigure(1, weight=1)
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_rowconfigure(1, weight=1)
        self.top_frame.grid_rowconfigure(2, weight=1)
        self.top_frame.grid_rowconfigure(3, weight=1)
        self.top_frame.grid_rowconfigure(4, weight=1)
        self.top_frame.grid_rowconfigure(5, weight=1)

        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(1, weight=1)
        self.bottom_frame.grid_columnconfigure(2, weight=1)
        self.bottom_frame.grid_columnconfigure(3, weight=1)
        self.bottom_frame.grid_rowconfigure(0, weight=1)

    def proceed(self):
        # Batches the users chosen options and disables option controls to move onto next step
        self.batched_options = OptionsBatch(
            self.cut_corners_choice.get(),
            self.allow_climbing_choice.get(),
            self.respect_paths_choice.get(),
            self.method_box.get(),
            self.placement_steps_box.get(),
            self.time_limit_entrybox.get()
            )
        
        self.cut_corners_button.configure(state="disabled")
        self.allow_climbing_button.configure(state="disabled")
        self.respect_paths_button.configure(state="disabled")
        self.method_box.configure(state="disabled")
        self.placement_steps_box.configure(state="disabled")
        self.time_limit_entrybox.configure(state="disabled")
        self.method_label.configure(state="disabled")
        self.placement_steps_label.configure(state="disabled")
        self.time_limit_label.configure(state="disabled")

        self.back_button.configure(state="normal")
        self.help_button.configure(state="disabled")
        self.default_button.configure(state="disabled")

        self.main_app.enter_entrance_placement()

    def back(self):
        # Re-enables all controls and calls method to move grid selector back to room-design mode
        self.cut_corners_button.configure(state="normal")
        self.allow_climbing_button.configure(state="normal")
        self.respect_paths_button.configure(state="normal")
        self.method_box.configure(state="normal")
        self.placement_steps_box.configure(state="normal")
        self.time_limit_entrybox.configure(state="normal")
        self.method_label.configure(state="normal")
        self.placement_steps_label.configure(state="normal")
        self.time_limit_label.configure(state="normal")

        self.back_button.configure(state="disabled")
        self.help_button.configure(state="normal")
        self.default_button.configure(state="normal")

        #<TODO>: grid selector back to normal mode method call

    def default_options(self):
        # Sets all options back to their default values
        self.cut_corners_button.select()
        self.allow_climbing_button.select()
        self.respect_paths_button.deselect()
        self.method_box.current(0)
        self.placement_steps_box.current(4)
        self.time_limit_entrybox.delete(0, tk.END)
        self.time_limit_entrybox.insert(0, "300")

    def display_help(self):
        # The help/info and explanations popup window
        self.help_box = tk.messagebox.showinfo("Help/Info", "Cut corners - Controls whether calculated paths will be allowed to traverse diagonally across object corners.\n\n"
                                               "Allow climbing - Allows paths to consider routes where climbing is allowed. In game pawns can move across the top of items like shelves at no additional cost once they've spent the extra time initially 'climbing' onto one.\n\n"
                                               "Respect paths - If this is checked the route calculation will attempt to avoid new shelf placements which intersect an existing path.\n\n"
                                               "Method - Changes the shelf placement method used in calculation:\n"
                                               "        - Best first - Prefers the lowest found path cost.\n"
                                               "        - Worst first - Prefers the highest found path cost.\n"
                                               "        - Random - Picks an empty cell at random.\n"
                                               "        - Grid fill - Attempts to place via working through the grid, from the top left to bottom right corners.\n\n"
                                               "Placement attempts - Controls how many options the placement algorithm will attempt to select from.\n\n"
                                               "Global time limit - Provides a hard cutoff where the script will simply stop and export whatever it has managed to do thus far.")