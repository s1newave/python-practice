from tkinter import *
from tkinter import ttk

from area_calculator import (
    calculate_circle_area,
    calculate_rectangle_area,
    calculate_triangle_area
)


class CircleFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.radius_var = StringVar()

        ttk.Label(self, text="Радиус:").grid(row=0, column=0, sticky=E)
        ttk.Entry(self, textvariable=self.radius_var).grid(row=0, column=1, sticky=W)

    def get_inputs(self):
        return (self.radius_var.get(),)


class RectangleFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.side_a_var = StringVar()
        self.side_b_var = StringVar()

        ttk.Label(self, text="Сторона A:").grid(row=0, column=0, sticky=E)
        ttk.Entry(self, textvariable=self.side_a_var).grid(row=0, column=1, sticky=W)
        ttk.Label(self, text="Сторона B:").grid(row=1, column=0, sticky=E)
        ttk.Entry(self, textvariable=self.side_b_var).grid(row=1, column=1, sticky=W)

    def get_inputs(self):
        return (self.side_a_var.get(), self.side_b_var.get())


class TriangleFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.side_a_var = StringVar()
        self.side_b_var = StringVar()
        self.side_c_var = StringVar()

        ttk.Label(self, text="Сторона A:").grid(row=0, column=0, sticky=E)
        ttk.Entry(self, textvariable=self.side_a_var).grid(row=0, column=1, sticky=W)
        ttk.Label(self, text="Сторона B:").grid(row=1, column=0, sticky=E)
        ttk.Entry(self, textvariable=self.side_b_var).grid(row=1, column=1, sticky=W)
        ttk.Label(self, text="Сторона C:").grid(row=2, column=0, sticky=E)
        ttk.Entry(self, textvariable=self.side_c_var).grid(row=2, column=1, sticky=W)

    def get_inputs(self):
        return (self.side_a_var.get(), self.side_b_var.get(), self.side_c_var.get())


class FigureAreaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FigArea")

        self.figure = StringVar()
        self.area = StringVar()

        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.grid(row=0, column=0)

        self.figure_frame = ttk.Frame(self.main_frame)
        self.figure_frame.grid(row=1, column=0, columnspan=2)

        self.circle_frame = CircleFrame(self.figure_frame)
        self.rectangle_frame = RectangleFrame(self.figure_frame)
        self.triangle_frame = TriangleFrame(self.figure_frame)

        self.figure_frames = {
            "круг": self.circle_frame,
            "прямоугольник": self.rectangle_frame,
            "треугольник": self.triangle_frame
        }

        figure_label = ttk.Label(self.main_frame, text="Фигура:")
        figure_label.grid(row=0, column=0, sticky=E)
        self.figure_combobox = ttk.Combobox(
            self.main_frame,
            textvariable=self.figure,
            values=list(self.figure_frames),
            state="readonly"
        )
        self.figure_combobox.current(0)
        self.figure_combobox.grid(row=0, column=1, sticky=W)
        self.figure_combobox.bind("<<ComboboxSelected>>", self.on_select_figure)

        area_label = ttk.Label(self.main_frame, text="Площадь:")
        area_label.grid(row=2, column=0, sticky=E)
        area_value_label = ttk.Label(self.main_frame, textvariable=self.area)
        area_value_label.grid(row=2, column=1, sticky=W)

        calculate_button = ttk.Button(
            self.main_frame,
            text="Вычислить",
            command=self.calculate_figure_area
        )
        calculate_button.grid(row=3, column=0, columnspan=2)

        self.main_frame.rowconfigure(1, weight=1)
        for frame in (self.main_frame, self.circle_frame, self.rectangle_frame, self.triangle_frame):
            for child in frame.winfo_children():
                child.grid_configure(padx=5, pady=5)

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.on_select_figure(None)

    def on_select_figure(self, event):
        for frame in self.figure_frames.values():
            frame.grid_forget()
        self.figure_frames[self.figure.get()].grid(row=0, column=0, sticky="nsew")
        self.area.set("")

    def calculate_figure_area(self):
        try:
            match self.figure.get():
                case "круг":
                    r = float(self.circle_frame.get_inputs()[0])
                    result = calculate_circle_area(r)
                case "прямоугольник":
                    a, b = map(float, self.rectangle_frame.get_inputs())
                    result = calculate_rectangle_area(a, b)
                case "треугольник":
                    a, b, c = map(float, self.triangle_frame.get_inputs())
                    result = calculate_triangle_area(a, b, c)
            self.area.set(str(round(result, 3)))
        except ValueError:
            pass


if __name__ == "__main__":
    root = Tk()
    FigureAreaApp(root)
    root.mainloop()
