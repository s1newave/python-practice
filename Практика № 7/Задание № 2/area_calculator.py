import math


def calculate_circle_area(r):
    return math.pi * r ** 2

def calculate_rectangle_area(a, b):
    return a * b

def calculate_triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
