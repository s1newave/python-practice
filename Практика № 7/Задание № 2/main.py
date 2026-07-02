from tkinter import *
from tkinter import ttk

from area_calculator import (
    calculate_circle_area,
    calculate_rectangle_area,
    calculate_triangle_area
)


root = Tk()
root.title("FigArea")

main_frame = ttk.Frame(root, padding=10)
main_frame.grid(row=0, column=0)

figure_frame = ttk.Frame(main_frame)
figure_frame.grid(row=1, column=0, columnspan=2)

circle_frame = ttk.Frame(figure_frame)

circle_radius = StringVar()
circle_radius_label = ttk.Label(circle_frame, text="Радиус:")
circle_radius_label.grid(row=0, column=0, sticky=E)
circle_radius_entry = ttk.Entry(circle_frame, textvariable=circle_radius)
circle_radius_entry.grid(row=0, column=1, sticky=W)

rectangle_frame = ttk.Frame(figure_frame)

rectangle_side_a = StringVar()
rectangle_side_a_label = ttk.Label(rectangle_frame, text="Сторона A:")
rectangle_side_a_label.grid(row=0, column=0, sticky=E)
rectangle_side_a_entry = ttk.Entry(rectangle_frame, textvariable=rectangle_side_a)
rectangle_side_a_entry.grid(row=0, column=1, sticky=W)

rectangle_side_b = StringVar()
rectangle_side_b_label = ttk.Label(rectangle_frame, text="Сторона B:")
rectangle_side_b_label.grid(row=1, column=0, sticky=E)
rectangle_side_b_entry = ttk.Entry(rectangle_frame, textvariable=rectangle_side_b)
rectangle_side_b_entry.grid(row=1, column=1, sticky=W)

triangle_frame = ttk.Frame(figure_frame)

triangle_side_a = StringVar()
triangle_side_a_label = ttk.Label(triangle_frame, text="Сторона A:")
triangle_side_a_label.grid(row=0, column=0, sticky=E)
triangle_side_a_entry = ttk.Entry(triangle_frame, textvariable=triangle_side_a)
triangle_side_a_entry.grid(row=0, column=1, sticky=W)

triangle_side_b = StringVar()
triangle_side_b_label = ttk.Label(triangle_frame, text="Сторона B:")
triangle_side_b_label.grid(row=1, column=0, sticky=E)
triangle_side_b_entry = ttk.Entry(triangle_frame, textvariable=triangle_side_b)
triangle_side_b_entry.grid(row=1, column=1, sticky=W)

triangle_side_c = StringVar()
triangle_side_c_label = ttk.Label(triangle_frame, text="Сторона C:")
triangle_side_c_label.grid(row=2, column=0, sticky=E)
triangle_side_c_entry = ttk.Entry(triangle_frame, textvariable=triangle_side_c)
triangle_side_c_entry.grid(row=2, column=1, sticky=W)

figure_frames = {
    "круг": circle_frame,
    "прямоугольник": rectangle_frame,
    "треугольник": triangle_frame
}

def on_select_figure(event):
    for frame in figure_frames.values():
        frame.grid_forget()
    figure_frames[figure.get()].grid(row=0, column=0, sticky="nsew")

figure = StringVar()
figure_label = ttk.Label(main_frame, text="Фигура:")
figure_label.grid(row=0, column=0, sticky=E)
figure_combobox = ttk.Combobox(
    main_frame,
    textvariable=figure,
    values=list(figure_frames),
    state="readonly"
)
figure_combobox.current(0)
figure_combobox.grid(row=0, column=1, sticky=W)
figure_combobox.bind("<<ComboboxSelected>>", on_select_figure)

area = StringVar()

area_label = ttk.Label(main_frame, text="Площадь:")
area_label.grid(row=2, column=0)

area_value_label = ttk.Label(main_frame, textvariable=area)
area_value_label.grid(row=2, column=1)

def calculate_figure_area():
    try:
        match figure.get():
            case "круг":
                result = calculate_circle_area(float(circle_radius.get()))
                area.set(str(result))
            case "прямоугольник":
                result = calculate_rectangle_area(
                    float(rectangle_side_a.get()),
                    float(rectangle_side_b.get())
                )
                area.set(str(result))
            case "треугольник":
                result = calculate_triangle_area(
                    float(triangle_side_a.get()),
                    float(triangle_side_b.get()),
                    float(triangle_side_c.get())
                )
                area.set(str(result))
    except ValueError:
        pass

calculate_button = ttk.Button(
    main_frame,
    text="Вычислить",
    command=calculate_figure_area
)
calculate_button.grid(row=3, column=0, columnspan=2)

main_frame.rowconfigure(1, weight=1)
for column in range(2):
    main_frame.columnconfigure(column, weight=1)

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

on_select_figure(None)

root.mainloop()
