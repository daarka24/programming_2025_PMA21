from shape.circle import Circle
from shape.rectangle import Rectangle
from shape.square import Square
from color.black import Black
from color.purple import Purple
from color.yellow import Yellow
from color.colorclass import Color



def make_color(name):
    try:
        if name.lower() == "purple":
            return Purple()
        elif name.lower() == "yellow":
            return Yellow()
        elif name.lower() == "black":
            return Black()
        else:
            return Color()
    except Exception as error:
        print("can't make color", error)
        return Color()




shapes = []

try:
    with open("starter.txt", "r") as file:
        lines = file.readlines()
except Exception as error:
    print("can`t read from file", error)
    lines = []

for line in lines:
    try:
        parts = line.strip().split()
        if len(parts) < 2:
            continue

        shape_type = parts[0].lower()
        color = make_color(parts[1])

        if shape_type == "circle" and len(parts) == 3:
            shapes.append(Circle(color, parts[2]))
        elif shape_type == "rectangle" and len(parts) == 4:
            shapes.append(Rectangle(color, parts[2], parts[3]))
        elif shape_type == "square" and len(parts) == 3:
            shapes.append(Square(color, parts[2]))
        else:
            print("Not correct data", line)
    except Exception as error:
        print("can`t create a shape", error)


try:
    with open("result.txt", "w") as out:
        for s in shapes:
            try:
                out.write(f"Shape: {s.__class__.__name__}\n")
                out.write(f"color: {s.color.get_color()}\n")
                out.write(f"area: {s.area()}\n")
                out.write(f"perimeter: {s.perimeter()}\n")
                out.write("-" * 30 + "\n")
            except Exception as error:
                out.write(f"something went wrong: {error}\n")
except Exception as error:
    print("error with file:", error)
