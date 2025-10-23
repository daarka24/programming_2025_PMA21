from shapes_class import Circle, Rectangle, Square, Red, Blue, Green

color_map = {
    "red": Red,
    "blue": Blue,
    "green": Green
}

shape_map = {
    "circle": Circle,
    "rectangle": Rectangle,
    "square": Square
}

def load_shapes(filename):
    shapes = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue

            shape_name = parts[0].lower()
            color_name = parts[-1].lower()
            params = parts[1:-1]

            if shape_name not in shape_map or color_name not in color_map:
                print(f"Невідомий тип або колір: {line.strip()}")
                continue

            color = color_map[color_name]()
            shape = shape_map[shape_name](*params, color)
            shapes.append(shape)

    return shapes


def main():
    shapes = load_shapes("data.txt")

    for shape in shapes:
        print(f"{shape.describe()}: area = {shape.area():.2f}, perimeter = {shape.perimeter():.2f}")


if __name__ == "__main__":
    main()
