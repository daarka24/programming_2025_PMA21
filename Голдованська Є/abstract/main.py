from abstract import *

def read_color(color):
    if color == "pink":
        return Pink()
    elif color == "blue":
        return Blue()
    elif color == "green":
        return Green()
    return "Unknown color"


with open("in.txt") as file:
    data = file.read().split("\n")

shapes = []
for shape in data:
    shape = shape.split()
    try:
        if shape[0] == "square":
            shapes.append(Square([float(shape[2])], read_color(shape[1])))

        elif shape[0] == "circle":
            shapes.append(Circle(float(shape[2]), read_color(shape[1])))

        elif shape[0] == "rectangle":
            shapes.append(Rectangle([float(shape[2]), float(shape[3])], read_color(shape[1])))

    except Exception as e:
        print(e)

with open("out.txt", "w") as file:
    for shape in shapes:
        file.write(f"{shape}\n")