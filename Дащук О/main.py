from factory.shape_factory import ShapeFactory


def main():
    circle_path = "data/circle_data.txt"
    rect_path = "data/rectangle_data.txt"
    square_path = "data/square_data.txt"

    red_circle = ShapeFactory.create_shape('circle', 'red', circle_path)
    if red_circle:
        print(red_circle.display_shape_info())
        print("-" * 30)

    black_rectangle = ShapeFactory.create_shape('rectangle', 'black', rect_path)
    if black_rectangle:
        print(black_rectangle.display_shape_info())
        print("-" * 30)

    white_square = ShapeFactory.create_shape('square', 'white', square_path)
    if white_square:
        print(white_square.display_shape_info())
        print("-" * 30)


if __name__ == "__main__":
    main()
