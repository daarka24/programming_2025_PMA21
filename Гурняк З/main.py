from color import Red, Blue, Green
from shapes import Circle, Rectangle, Square


if __name__ == "__main__":
    red = Red()
    blue = Blue()
    green = Green()

    circle = Circle(5, red)
    rectangle = Rectangle(4, 6, blue)
    square = Square(3, green)

    shapes = [circle, rectangle, square]

    for shape in shapes:
        print(shape.draw())
        print(f"Area: {shape.calculate_area():.2f}")
        print(f"Perimeter: {shape.calculate_perimeter():.2f}")
        print()
