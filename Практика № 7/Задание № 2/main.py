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
main_frame.grid(row=0, column=0, sticky=(N, S, W, E))

circle_frame = ttk.Frame(main_frame)

rectangle_frame = ttk.Frame(main_frame)

triangle_frame = ttk.Frame(main_frame)

figure_frames = {
    "круг": circle_frame,
    "прямоугольник": rectangle_frame,
    "треугольник": triangle_frame
}

(ttk.Label(main_frame, text="Фигура:")
    .grid(row=0, column=0, sticky=(N, S, E)))

figure = StringVar(figure_frames[0])
(ttk.Combobox(main_frame, textvariable=figure, values=list(figure_frames.keys()))
    .grid(row=0, column=1, sticky=(N, S, W)))

def on_select_figure(event):
    pass


#(ttk.Button(main_frame, text="Вычислить", command=calculate_figure_area))

main_frame.rowconfigure(1, weight=1)
for column in range(2):
    main_frame.columnconfigure(column, weight=1)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()
