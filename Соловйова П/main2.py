from colors.colors import RedColor, BlueColor, GreenColor
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.square import Square

def main():
    print("Демонстрація")
    print("Фігури з різними кольорами\n")

    red = RedColor()
    blue = BlueColor()
    green = GreenColor()

    shapes = [
        Circle(5, red),
        Circle(3, blue),
        Rectangle(4, 6, green),
        Rectangle(8, 3, red),
        Square(5, blue),
        Square(7, green)
    ]

    for i, shape in enumerate(shapes, 1):
        print(f"{i}. {shape.get_info()}")

    print("\nДетальна інформація")
    for shape in shapes:
        print(f"\n{shape.__class__.__name__} ({shape.color.get_color_name()}):")
        print(f"  - Код кольору: {shape.color.get_color_code()}")
        print(f"  - Периметр: {shape.calculate_perimeter():.2f}")
        print(f"  - Площа: {shape.calculate_area():.2f}")
        if hasattr(shape, 'radius'):
            print(f"  - Радіус: {shape.radius}")
        elif hasattr(shape, 'width') and hasattr(shape, 'height'):
            print(f"  - Ширина: {shape.width}, Висота: {shape.height}")

if __name__ == "__main__":
    main()
