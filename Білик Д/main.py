import math
from classabstr import Figure, Color, RedColor, GreenColor, WhiteColor # Імпортуємо оновлені класи
from data_reader import read_one_float, read_two_floats
from rectangle import Rectangle
from square import Square
from circle import Circle

def rectangle_from_file(color: Color, filename="rectangle.txt"):
    try:
        height, width = read_two_floats(filename)
        return Rectangle(color, height, width)
    except (FileNotFoundError, ValueError) as e:
        print(f"Помилка створення прямокутника з файлу '{filename}': {e}")
        return Rectangle(color, 0, 0)

def square_from_file(color: Color, filename="square.txt"):
    try:
        side = read_one_float(filename)
        return Square(color, side)
    except (FileNotFoundError, ValueError) as e:
        print(f"Помилка створення квадрата з файлу '{filename}': {e}")
        return Square(color, 0)


def circle_from_file(color: Color, filename="circle.txt"):
    try:
        radius = read_one_float(filename)
        return Circle(color, radius)
    except (FileNotFoundError, ValueError) as e:
        print(f"Помилка створення кола з файлу '{filename}': {e}")
        return Circle(color, 0)

def main():
    red = RedColor()
    green = GreenColor()
    white = WhiteColor()
    squareRed = square_from_file(color=red)
    squareRed.peint()
    rectangleGreen = rectangle_from_file(color=green)
    rectangleGreen.peint()
    circleWhite = circle_from_file(color=white)
    circleWhite.peint()

if __name__ == "__main__":
    main()