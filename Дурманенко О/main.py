from shapes_app.factory.shape_factory import ShapeFactory

def main():
    red_circle = ShapeFactory.create_shape('circle', 'red', 'circle_data.txt')
    if red_circle:
        print(red_circle.display_shape_info())

    black_rectangle = ShapeFactory.create_shape('rectangle', 'black', 'rectangle_data.txt')
    if black_rectangle:
        print(black_rectangle.display_shape_info())

    white_square = ShapeFactory.create_shape('square', 'white', 'square_data.txt')
    if white_square:
        print(white_square.display_shape_info())

if __name__ == "__main__":
    main()