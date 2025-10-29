from figures import Shape, Circle, Square, Rectangle
from colors import Color, Red, Blue, Green


def get_color(color_name: str) -> Color:
    colors = {
        "red": Red(),
        "blue": Blue(),
        "green": Green()
    }
    return colors.get(color_name.lower(), Blue())


def main():
    shapes = []
    input_file = "in.txt"
    output_file = "out.txt"

    try:
        with open(input_file, "r") as f:
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
                        print(f"Помилковий рядок (неправильна к-сть аргументів): {line.strip()}")
                        continue

                    shapes.append(shape)

                except ValueError:
                    print(f"Помилковий рядок (неправильні числа): {line.strip()}")
                    continue

    except FileNotFoundError:
        print(f"Помилка: Не можу знайти файл '{input_file}'.")
        return
    except Exception as e:
        print(f"Сталася неочікувана помилка: {e}")

    if not shapes:
        print("Не знайдено жодної фігури у файлі.")
        return

    print("---- фігури ----")
    for s in shapes:
        print("---------")
        print(f"Фігура: {s.get_name()}")
        print(f"Інфо про колір: {s.draw()}")
        print(f"Площа: {s.area():.2f}")
        print(f"Периметр: {s.perimeter():.2f}")

    try:
        with open(output_file, "w") as fil:
            for shape in shapes:
                fil.write(f"Shape: {shape.get_name()}\n")
                fil.write(f"Area: {shape.area():.2f}\n")
                fil.write(f"Perimeter: {shape.perimeter():.2f}\n")
                fil.write(f"Color info: {shape.draw()}\n\n")

        print(f"\nУспішно збережено {len(shapes)} фігур у файл '{output_file}'")

    except IOError:
        print(f"Помилка: Не можу записати у файл '{output_file}'.")


if __name__ == "__main__":
    main()