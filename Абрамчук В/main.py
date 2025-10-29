import math
class Color:
    def __init__(self, name):
        self.name = name

class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        if radius <= 0:
            raise ValueError(f"Радіус має бути додатнім числом, отримано: {radius}")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def info(self):
        return f"Коло {self.color.name}, радіус: {self.radius}"

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        if width <= 0:
            raise ValueError(f"Ширина має бути додатнім числом, отримано: {width}")
        if height <= 0:
            raise ValueError(f"Висота має бути додатнім числом, отримано: {height}")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def info(self):
        return f"Прямокутник {self.color.name}, ширина: {self.width}, висота: {self.height}"

class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        if side <= 0:
            raise ValueError(f"Сторона має бути додатнім числом, отримано: {side}")
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def info(self):
        return f"Квадрат {self.color.name}, сторона: {self.side}"

def read_shapes(filename):
    shapes = []
    errors = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue

                try:
                    parts = line.split(',')
                    shape_type = parts[0].strip()
                    color_name = parts[1].strip()
                    color = Color(color_name)

                    if shape_type == "коло":
                        radius = float(parts[2].strip())
                        shapes.append(Circle(color, radius))
                    elif shape_type == "прямокутник":
                        width = float(parts[2].strip())
                        height = float(parts[3].strip())
                        shapes.append(Rectangle(color, width, height))
                    elif shape_type == "квадрат":
                        side = float(parts[2].strip())
                        shapes.append(Square(color, side))
                except ValueError as e:
                    errors.append(f"Рядок {line_num}: {e}")
                except IndexError:
                    errors.append(f"Рядок {line_num}: Неправильний формат даних")
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено!")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")

    if errors:
        print("\nЗнайдено помилки:")
        for error in errors:
            print(f"  - {error}")

    return shapes

def write_results(shapes, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=== Результати обчислень ===\n\n")
        for i, shape in enumerate(shapes, 1):
            f.write(f"{i}. {shape.info()}\n")
            f.write(f"   Площа: {shape.area():.2f}\n")
            f.write(f"   Периметр: {shape.perimeter():.2f}\n\n")

def main():
    input_file = 'figures.txt'
    output_file = 'result.txt'

    shapes = read_shapes(input_file)

    if shapes:
        print(f"Прочитано {len(shapes)} фігур з файлу {input_file}")

        write_results(shapes, output_file)
        print(f"Результати записано в файл {output_file}")
    else:
        print("Не вдалося прочитати фігури з файлу")
        print(f"\nСтворіть файл {input_file} з таким форматом:")
        print("коло, червоний, 5")
        print("прямокутник, синій, 4, 6")
        print("квадрат, зелений, 3")

if __name__ == "__main__":
    main()