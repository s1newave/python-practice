import math
from tkinter import *
from tkinter import ttk


def calculate_circle_area(r):
    return math.pi * r ** 2

def calculate_rectangle_area(a, b):
    return a * b

def calculate_triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


root = Tk()
root.title("FigArea")

main_frame = ttk.Frame(root, padding=10)
main_frame.grid(row=0, column=0, sticky=(N, W, E, S))

circle_frame = ttk.Frame(main_frame)


rectangle_frame = ttk.Frame(main_frame)


triangle_frame = ttk.Frame(main_frame)

root.mainloop()
