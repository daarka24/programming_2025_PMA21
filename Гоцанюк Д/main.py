import sys
from figures import Circle, Square, Rectangle
from colors import Red, Blue, Green

FILE_IN = "input.txt"
FILE_OUT = "output.txt"


def process_data():
    figure_list = []

    color_map = {
        "red": Red,
        "blue": Blue,
        "green": Green
    }

    try:
        with open(FILE_IN, "r", encoding='utf-8') as file_handle:
            lines = file_handle.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue

            tokens = line.split()
            type_str = tokens[0].lower()
            color_str = tokens[-1].lower()

            color_class = color_map.get(color_str, Blue)
            current_color = color_class()

            try:
                new_figure = None
                args_count = len(tokens)

                if type_str == "circle" and args_count == 3:
                    radius = float(tokens[1])
                    new_figure = Circle(current_color, radius)

                elif type_str == "square" and args_count == 3:
                    side = float(tokens[1])
                    new_figure = Square(current_color, side)

                elif type_str == "rectangle" and args_count == 4:
                    w = float(tokens[1])
                    h = float(tokens[2])
                    new_figure = Rectangle(current_color, w, h)
                else:
                    print(f"Помилковий рядок (неправильна к-сть аргументів): {line}")
                    continue

                figure_list.append(new_figure)

            except ValueError:
                print(f"Помилковий рядок (неправильні числа): {line}")
                continue

    except FileNotFoundError:
        print(f"Помилка: Не можу знайти файл '{FILE_IN}'.")
        return
    except Exception as err:
        print(f"Сталася неочікувана помилка: {err}")
        return

    if not figure_list:
        print("Не знайдено жодної фігури у файлі.")
        return

    print("---- фігури ----")
    for item in figure_list:
        print("---------")
        print(f"Фігура: {item}")
        print(f"Інфо про колір: {item.get_color_info()}")
        print(f"Площа: {item.calc_area():.2f}")
        print(f"Периметр: {item.calc_perimeter():.2f}")

    try:
        with open(FILE_OUT, "w", encoding='utf-8') as f_out:
            for item in figure_list:
                f_out.write(f"Shape: {item}\n")
                f_out.write(f"Area: {item.calc_area():.2f}\n")
                f_out.write(f"Perimeter: {item.calc_perimeter():.2f}\n")
                f_out.write(f"Color info: {item.get_color_info()}\n\n")

        print(f"\nУспішно збережено {len(figure_list)} фігур у файл '{FILE_OUT}'")

    except IOError:
        print(f"Помилка: Не можу записати у файл '{FILE_OUT}'.")


if __name__ == "__main__":
    process_data()