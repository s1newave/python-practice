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

figure_frames = {
    "круга": circle_frame,
    "прямоугольника": rectangle_frame,
    "треугольника": triangle_frame
}

#ttk.Combobox(main_frame, values=figure_frames.keys())


#(ttk.Button(main_frame, text="Вычислить", command=calculate_figure_area))

main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=4)
main_frame.rowconfigure(2, weight=1)
for column in range(3):
    root.columnconfigure(column, weight=1)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()
