from shape import Shape, Circle, Square, Rectangle
from color import Color, Pink, Brown, White
def get_color(color_name: str) -> Color:
    colors={
        "pink": Pink(),
        "brown": Brown(),
        "white": White()
    }
    return colors.get(color_name.lower(), Pink())
def main():
    shapes = []
    try:
        with open("in.txt", "r") as f:
            for line in f:
                parts = line.strip().split()
                if not parts:
                   continue
                shape_type = parts[0].lower()
                color_name = parts[-1].lower()
                color = get_color(color_name)
                try:
                    if shape_type == "circle" and len(parts) == 3:
                        shape = Circle(color, float(parts[1]))
                    elif shape_type == "square" and len(parts) == 3:
                        shape = Square(color, float(parts[1]))
                    elif shape_type == "rectangle" and len(parts) == 4:
                        shape = Rectangle(color, float(parts[1]), float(parts[2]))
                    else:
                        print("Not correct line")
                        continue
                    shapes.append(shape)
                except ValueError:
                    print("Not correct info line")
                    continue
    except FileNotFoundError:
        print("File not found")
        return
    except Exception as e:
        print(f"Unknown problem {e}")
    if not shapes:
        print("No shapes found")
        return
    print("----All shapes----")
    for s in shapes:
        print("---------")
        print(s.name())
        print(s.draw())
        print(f"Area: {s.area():.2f}")
        print(f"Perimetr: {s.perimeter():.2f}")
    try:
        with open("out.txt", "w") as fil:
            for shape in shapes:
                fil.write(f"Shape: {shape.name()}\n"
                          f"Area: {shape.area():.2f}\n" f"Perimeter: {shape.perimeter():.2f}\n" f"Color: {shape.color.name()}\n\n")
        print("Save to file")
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
