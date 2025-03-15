import tkinter as tk
from tkinter import ttk
import math

def calculate_area():
    shape = shape_combobox.get()
    if shape == "Square":
        side_length = side_length_entry.get()
        if side_length.isdigit() and int(side_length) > 0:
            area = float(side_length) ** 2
            result_label.config(text=f"Area: {area:.2f}")
        else:
            result_label.config(text="Invalid input! Please enter a positive integer for side length.")
    elif shape == "Rectangle":
        length = length_entry.get()
        width = width_entry.get()
        if length.isdigit() and width.isdigit() and int(length) > 0 and int(width) > 0:
            area = float(length) * float(width)
            result_label.config(text=f"Area: {area:.2f}")
        else:
            result_label.config(text="Invalid input! Please enter positive integers for length and width.")
    elif shape == "Circle":
        radius = radius_entry.get()
        if radius.isdigit() and int(radius) > 0:
            area = math.pi * float(radius) ** 2
            result_label.config(text=f"Area: {area:.2f}")
        else:
            result_label.config(text="Invalid input! Please enter a positive integer for radius.")
    elif shape == "Triangle":
        base = base_entry.get()
        height = height_entry.get()
        if base.isdigit() and height.isdigit() and int(base) > 0 and int(height) > 0:
            area = 0.5 * float(base) * float(height)
            result_label.config(text=f"Area: {area:.2f}")
        else:
            result_label.config(text="Invalid input! Please enter positive integers for base and height.")
    elif shape == "Parallelogram":
        base = base_entry.get()
        height = height_entry.get()
        if base.isdigit() and height.isdigit() and int(base) > 0 and int(height) > 0:
            area = float(base) * float(height)
            result_label.config(text=f"Area: {area:.2f}")
        else:
            result_label.config(text="Invalid input! Please enter positive integers for base and height.")
    elif shape == "Trapezoid":
        base1 = base1_entry.get()
        base2 = base2_entry.get()
        height = height_entry.get()
        if base1.isdigit() and base2.isdigit() and height.isdigit() and int(base1) > 0 and int(base2) > 0 and int(height) > 0:
            area = 0.5 * (float(base1) + float(base2)) * float(height)
            result_label.config(text=f"Area: {area:.2f}")
        else:
            result_label.config(text="Invalid input! Please enter positive integers for bases and height.")
    elif shape == "Rhombus":
        diagonal1 = diagonal1_entry.get()
        diagonal2 = diagonal2_entry.get()
        if diagonal1.isdigit() and diagonal2.isdigit() and int(diagonal1) > 0 and int(diagonal2) > 0:
            area = 0.5 * float(diagonal1) * float(diagonal2)
            result_label.config(text=f"Area: {area:.2f}")
        else:
            result_label.config(text="Invalid input! Please enter positive integers for diagonals.")
    elif shape == "Regular Polygon":
        num_sides = num_sides_entry.get()
        side_length = side_length_entry.get()
        if num_sides.isdigit() and side_length.isdigit() and int(num_sides) >= 3 and int(side_length) > 0:
            area = (int(num_sides) * int(side_length) ** 2) / (4 * math.tan(math.pi / int(num_sides)))
            result_label.config(text=f"Area: {area:.2f}")
        else:
            result_label.config(text="Invalid input! Please enter a positive integer for the number of sides and side length (sides >= 3).")
    elif shape == "Ellipse":
        major_axis = major_axis_entry.get()
        minor_axis = minor_axis_entry.get()
        if major_axis.isdigit() and minor_axis.isdigit() and int(major_axis) > 0 and int(minor_axis) > 0:
            area = math.pi * float(major_axis) * float(minor_axis)
            result_label.config(text=f"Area: {area:.2f}")
        else:
            result_label.config(text="Invalid input! Please enter positive integers for major and minor axes.")
    elif shape == "Sector of a Circle":
        radius = radius_entry.get()
        angle = angle_entry.get()
        if radius.isdigit() and angle.isdigit() and int(radius) > 0 and 0 <= float(angle) <= 360:
            area = 0.5 * float(radius) ** 2 * float(angle)
            result_label.config(text=f"Area: {area:.2f}")
        else:
            result_label.config(text="Invalid input! Please enter a positive integer for radius and an angle between 0 and 360.")

root = tk.Tk()
root.title("Geometrical Area Calculator")

mainframe = ttk.Frame(root, padding="20")
mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

shapes = ["Square", "Rectangle", "Circle", "Triangle", "Parallelogram", "Trapezoid", "Rhombus", "Regular Polygon", "Ellipse", "Sector of a Circle"]
shape_label = ttk.Label(mainframe, text="Select a shape:")
shape_label.grid(column=0, row=0, sticky=tk.W)

shape_combobox = ttk.Combobox(mainframe, values=shapes)
shape_combobox.grid(column=1, row=0)
shape_combobox.current(0)

side_length_label = ttk.Label(mainframe, text="Side Length:")
side_length_label.grid(column=0, row=1, sticky=tk.W)
side_length_entry = ttk.Entry(mainframe)
side_length_entry.grid(column=1, row=1)

length_label = ttk.Label(mainframe, text="Length:")
length_label.grid(column=0, row=2, sticky=tk.W)
length_entry = ttk.Entry(mainframe)
length_entry.grid(column=1, row=2)

width_label = ttk.Label(mainframe, text="Width:")
width_label.grid(column=0, row=3, sticky=tk.W)
width_entry = ttk.Entry(mainframe)
width_entry.grid(column=1, row=3)

radius_label = ttk.Label(mainframe, text="Radius:")
radius_label.grid(column=0, row=4, sticky=tk.W)
radius_entry = ttk.Entry(mainframe)
radius_entry.grid(column=1, row=4)

base_label = ttk.Label(mainframe, text="Base:")
base_label.grid(column=0, row=5, sticky=tk.W)
base_entry = ttk.Entry(mainframe)
base_entry.grid(column=1, row=5)

height_label = ttk.Label(mainframe, text="Height:")
height_label.grid(column=0, row=6, sticky=tk.W)
height_entry = ttk.Entry(mainframe)
height_entry.grid(column=1, row=6)

base1_label = ttk.Label(mainframe, text="Base 1:")
base1_label.grid(column=0, row=7, sticky=tk.W)
base1_entry = ttk.Entry(mainframe)
base1_entry.grid(column=1, row=7)

base2_label = ttk.Label(mainframe, text="Base 2:")
base2_label.grid(column=0, row=8, sticky=tk.W)
base2_entry = ttk.Entry(mainframe)
base2_entry.grid(column=1, row=8)

diagonal1_label = ttk.Label(mainframe, text="Diagonal 1:")
diagonal1_label.grid(column=0, row=9, sticky=tk.W)
diagonal1_entry = ttk.Entry(mainframe)
diagonal1_entry.grid(column=1, row=9)

diagonal2_label = ttk.Label(mainframe, text="Diagonal 2:")
diagonal2_label.grid(column=0, row=10, sticky=tk.W)
diagonal2_entry = ttk.Entry(mainframe)
diagonal2_entry.grid(column=1, row=10)

num_sides_label = ttk.Label(mainframe, text="Number of Sides:")
num_sides_label.grid(column=0, row=11, sticky=tk.W)
num_sides_entry = ttk.Entry(mainframe)
num_sides_entry.grid(column=1, row=11)

angle_label = ttk.Label(mainframe, text="Angle:")
angle_label.grid(column=0, row=12, sticky=tk.W)
angle_entry = ttk.Entry(mainframe)
angle_entry.grid(column=1, row=12)

calculate_button = ttk.Button(mainframe, text="Calculate", command=calculate_area)
calculate_button.grid(column=0, row=13, columnspan=2)

result_label = ttk.Label(mainframe, text="")
result_label.grid(column=0, row=14, columnspan=2)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
