import tkinter as tk
from tkinter import colorchooser

window = tk.Tk()
window.title("Drawy")

canvas_width = 600
canvas_height = 400
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
canvas.pack(pady=20)

last_x = None
last_y = None
current_color = "black"
current_shape = "line"
shape_start_x = None
shape_start_y = None

def start_drawing(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y, current_color
    if last_x is not None and last_y is not None:
        canvas.create_line(last_x, last_y, event.x, event.y,
                           width=3, fill=current_color, capstyle=tk.ROUND, smooth=tk.TRUE)
    last_x, last_y = event.x, event.y

def stop_drawing(event):
    global last_x, last_y
    last_x, last_y = None, None

def choose_color():
    global current_color
    color_code = colorchooser.askcolor(title="Choose drawing color")
    if color_code:
        current_color = color_code[1]

def start_shape(event):
    global shape_start_x, shape_start_y
    shape_start_x, shape_start_y = event.x, event.y

def draw_shape(event):
    global shape_start_x, shape_start_y, current_shape, current_color
    if shape_start_x is not None and shape_start_y is not None:
        canvas.delete("current_shape")
        if current_shape == "rectangle":
            canvas.create_rectangle(shape_start_x, shape_start_y, event.x, event.y,
                                   outline=current_color, tags="current_shape")
        elif current_shape == "oval":
            canvas.create_oval(shape_start_x, shape_start_y, event.x, event.y,
                              outline=current_color, tags="current_shape")

def finish_shape(event):
    global shape_start_x, shape_start_y
    shape_start_x, shape_start_y = None, None
    canvas.dtag("current_shape")

def set_shape(shape_type):
    global current_shape
    current_shape = shape_type

def enable_shape_drawing():
    canvas.unbind("<Button-1>")
    canvas.unbind("<B1-Motion>")
    canvas.unbind("<ButtonRelease-1>")
    canvas.bind("<Button-1>", start_shape)
    canvas.bind("<B1-Motion>", draw_shape)
    canvas.bind("<ButtonRelease-1>", finish_shape)

def enable_line_drawing():
    canvas.unbind("<Button-1>")
    canvas.unbind("<B1-Motion>")
    canvas.unbind("<ButtonRelease-1>")
    canvas.bind("<Button-1>", start_drawing)
    canvas.bind("<B1-Motion>", draw)
    canvas.bind("<ButtonRelease-1>", stop_drawing)

color_button = tk.Button(window, text="Pick Color", command=choose_color)
color_button.pack(pady=5)

line_button = tk.Button(window, text="Line", command=enable_line_drawing)
line_button.pack(side=tk.LEFT, padx=5)

rect_button = tk.Button(window, text="Rectangle", command=lambda: set_shape("rectangle"))
rect_button.pack(side=tk.LEFT, padx=5)

oval_button = tk.Button(window, text="Oval", command=lambda: set_shape("oval"))
oval_button.pack(side=tk.LEFT, padx=5)

# Initially set to line drawing
enable_line_drawing()

window.mainloop()