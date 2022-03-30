import random
import tkinter
from typing import List

from tkinter import *
from tkinter import ttk

from sorters.base import BaseSorter
from sorters.bubble_sort import BubbleSorter

root = Tk()
root.title("Sorting Visualisation")
root.geometry('1200x800+50+50')

# Frame for user inputs
input_frame = Frame(root)
input_frame.grid(row=0, column=0, padx=0, pady=5)

# Canvas for visulisation
canvas = Canvas(root, width=1100, height=700, bg="white")
canvas.grid(row=1, column=0, padx=50, pady=20)

# Add input label
Label(input_frame, text="Algorithm: ").grid(
    row=0, column=0
)

# Sorting algo buttons
bsort_button = Button(input_frame, text="Bubble sort", command=print(3))
bsort_button.grid(row=0, column=1)

def display_list(l: List[int], colors: List[str]):
    
    # Clear the canvas
    canvas.delete("all")

    canvas_height = 700
    canvas_width = 1100

    bar_width = canvas_width / len(l) + 1
    spacing = 1

    # MinMax scale
    minmax_l = [x / max(l) for x in l]

    for i, height in enumerate(minmax_l):

        canvas.create_rectangle(
            i * bar_width + spacing, 
            canvas_height - (height * canvas_height), 
            ((i + 1) * bar_width), 
            canvas_height, 
            fill=colors[i]
        )
    root.update()

def create_unsorted(n_elements: int) -> List[int]:
    """Creates unsorted array of unique integers

    Args:
        n_elements (int): length of array to be created

    Returns:
        List[int]: unsorted list
    """
    unsorted = list(range(n_elements))
    random.shuffle(unsorted)
    return unsorted

def run_sorter(sorter: BaseSorter, l: List[int]):
    sorter = sorter(l)
    sorter.sort()

    def _get_colors(i0, i1):
        colors = ["grey" for _ in range(len(sorter.l))]
        colors[i0] = "red"
        colors[i1] = "green"
        return colors

    for i0, i1 in sorter.swap_history:
        print(i0, i1)
        l[i0], l[i1] = l[i1], l[i0]
        colors = _get_colors(i0, i1)
        display_list(l, colors=colors)

run_sorter(BubbleSorter, create_unsorted(100))

# keep the window displaying
root.mainloop()
