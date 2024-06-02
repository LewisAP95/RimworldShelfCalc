import tkinter as tk
from tkinter import ttk

class OptionsPane:

    def __init__(self, parent):
        # Creating the frames for the other content
        self.top_frame = tk.Frame(parent, relief="groove", borderwidth=2)
        self.top_frame.grid(row=0, column=0, sticky="NESW")
        self.bottom_frame = tk.Frame(parent)
        self.bottom_frame.grid(row=1, column=0, sticky="NESW")

        # Top frame UI elements
        self.cut_corners_choice = tk.IntVar()
        self.cut_corners_button =  tk.Checkbutton(self.top_frame, text="Allow corner cutting?", variable=self.cut_corners_choice)
        self.cut_corners_button.grid(row=0, column=0, columnspan=2, sticky="NESW")

        self.allow_climbing_choice = tk.IntVar()
        self.allow_climbing_button = tk.Checkbutton(self.top_frame, text="Allow climbing?", variable=self.allow_climbing_choice)
        self.allow_climbing_button.grid(row=1, column=0, columnspan=2, sticky="NESW")

        self.respect_paths_choice = tk.IntVar()
        self.respect_paths_button = tk.Checkbutton(self.top_frame, text="Respect other paths?", variable=self.respect_paths_choice)
        self.respect_paths_button.grid(row=2, column=0, columnspan=2, sticky="NESW")

        self.method_label = tk.Label(self.top_frame, text="Method:")
        self.method_label.grid(row=3, column=0, sticky="NESW")
        self.method_box = ttk.Combobox(self.top_frame, state="readonly", values=["Best first", "Worst first", "Random", "Grid fill"])
        self.method_box.grid(row=3, column=1, sticky="NESW")

        self.placement_steps_label = tk.Label(self.top_frame, text="Max placement attempts:")
        self.placement_steps_label.grid(row=4, column=0, sticky="NESW")
        self.placement_steps_box = ttk.Combobox(self.top_frame, state="readonly", values=list(range(101)))
        self.placement_steps_box.grid(row=4, column=1, sticky="NESW")

        self.time_limit_label = tk.Label(self.top_frame, text="Global time limit:")
        self.time_limit_label.grid(row=5, column=0, sticky="NESW")
        self.time_limit_choice = tk.IntVar()
        self.time_limit_entrybox = tk.Entry(self.top_frame, textvariable=self.time_limit_choice, exportselection=0)
        self.time_limit_entrybox.grid(row=5, column=1, sticky="NESW")

        # Bottom frame UI elements
        self.back_button = tk.Button(self.bottom_frame, text="Go back", state="disabled")
        self.back_button.grid(row=0, column=0, sticky="NESW")

        self.default_button = tk.Button(self.bottom_frame, text="Reset to default")
        self.default_button.grid(row=0, column=1, sticky="NESW")

        self.proceed_button = tk.Button(self.bottom_frame, text="Proceed")
        self.proceed_button.grid(row=0, column=2, sticky="NESW")

        # Grid weight configuration

        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=8)
        parent.grid_rowconfigure(1, weight=2)

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
        self.bottom_frame.grid_rowconfigure(0, weight=1)