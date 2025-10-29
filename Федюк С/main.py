from color.red_color import RedColor
from color.green_color import GreenColor
from color.blue_color import BlueColor

from shape.circle import Circle
from shape.rectangle import Rectangle
from shape.square import Square

def create_shape_from_line(line):
    parts = line.strip().split()
    if not parts:
        return None

    shape_type = parts[0].lower()
    colors = [RedColor(), BlueColor(), GreenColor()]
    color = colors[len(parts) % 3]

    try:
        if shape_type == "circle":
            radius = float(parts[1])
            return Circle(radius, color)
        elif shape_type == "rectangle":
            width = float(parts[1])
            height = float(parts[2])
            return Rectangle(width, height, color)
        else:
            return None
    except (IndexError, ValueError):
        return None

def main():
    input_file = "shapes.txt"
    output_file = "results.txt"
    shapes = []

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            for line in f:
                shape = create_shape_from_line(line)
                if shape:
                    shapes.append(shape)
                    if isinstance(shape, Rectangle) and not isinstance(shape, Square):
                        shapes.append(Square(shape, GreenColor()))
    except FileNotFoundError:
        print(f"Файл '{input_file}' не знайдено.")
        return

    with open(output_file, "w", encoding="utf-8") as out:
        for s in shapes:
            try:
                info = (
                    f"{s.describe()}\n"
                    f"Площа: {s.area():.2f}\n"
                    f"Периметр: {s.perimeter():.2f}\n\n"
                )
                print(info)
                out.write(info)
            except Exception:
                continue

if __name__ == "__main__":
    main()
