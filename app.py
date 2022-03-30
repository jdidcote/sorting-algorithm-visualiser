from time import sleep
from typing import List

from tkinter import *
from tkinter import ttk

from sorters.base import BaseSorter
from sorters.bubble_sort import BubbleSorter
from utils import create_unsorted, matching_elements

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("Sorting Visualisation")
        self.geometry('1200x800+50+50')

        # Frame for user inputs
        self.input_frame = Frame(self)
        self.input_frame.grid(row=0, column=0, padx=0, pady=5)

        # Canvas for visualisation
        self.canvas = Canvas(self, width=1100, height=700, bg="white")
        self.canvas.grid(row=1, column=0, padx=50, pady=20)

        # Add input label
        Label(self.input_frame, text="Algorithm: ").grid(
            row=0, column=0
        )

        self.set_graph()

        sort_options = {
            "Bubble Sort": BubbleSorter
        }
        
        def _sort_func(option):
            self.run_sorter(sort_options[option], self.l)

        var = StringVar()
        var.set('Bubble sort')
        OptionMenu(self.input_frame, var, *sort_options, command=_sort_func).grid(row=0, column=1)

        # Reset button
        Button(
            self.input_frame,
            text="Reset",
            command=self.set_graph,
        ).grid(row=0, column=2)

    def set_graph(self):
        self.l = create_unsorted(50)
        self.display_list(self.l, ["grey" for _ in range(len(self.l))])

    def display_list(
        self, 
        l: List[int], 
        colors: List[str]
    ):
        # Clear the canvas
        self.canvas.delete("all")

        canvas_height = 700
        canvas_width = 1100

        bar_width = canvas_width  * 0.95 / len(l) + 1
        spacing = 0

        # MinMax scale
        minmax_l = [x / max(l) for x in l]

        for i, height in enumerate(minmax_l):

            self.canvas.create_rectangle(
                i * bar_width + spacing, 
                canvas_height, 
                ((i + 1) * bar_width), 
                canvas_height - (height * canvas_height), 
                fill=colors[i]
            )
        self.update()
    
    def run_sorter(self, Sorter: BaseSorter, l: List[int]):
        sorter = Sorter(l)
        sort_generator = sorter.sort()

        while not sorter.is_sorted:
            cur_iter = next(sort_generator)
            l = cur_iter.l

            colors = ["grey" for _ in range(len(sorter.l))]
            if len(cur_iter.swaps) > 0:
                for swap_index in cur_iter.swaps:
                    # Make swapped elements red
                    colors[swap_index] = "red"
            
            for matching in matching_elements(l, sorted(l)):
                colors[matching] = "green"

            # Make currently accessed element blue
            colors[cur_iter.index] = "blue"
            self.display_list(l, colors=colors)

            # sleep(0.002)

if __name__ == "__main__":
    app = App()
    app.mainloop()