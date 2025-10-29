class Color:
    def __init__(self, color: str = None):
        self.color = color

    def color_getter(self):
        return self.color


class Purple(Color):    # -> super() method to call father class
    def __init__(self):
        super().__init__("purple")

class Black(Color):
    def __init__(self):
        super().__init__("black")

class White(Color):
    def __init__(self):
        super().__init__("white")


class Shape:
    def __init__(self, color: Color):
        self.color = color

    def area(self):
        raise NotImplementedError("error: method is not Implemented.")

    def perimeter(self):
        raise NotImplementedError("error: method is not Implemented.")


class Circle(Shape):
    def __init__(self, color: Color, radius: float):
        super().__init__(color)
        self.radius = radius

    def area(self):
        pi = 3.142
        return pi * (self.radius * self.radius)

    def perimeter(self):
        pi = 3.142
        return 2 * pi * self.radius

class Square(Shape):
    def __init__(self, color: Color, side: float):
        super().__init__(color)
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4

class Rectangle(Shape):
    def __init__(self, color: Color, first_side: float, second_side: float):
        super().__init__(color)
        self.first_side = first_side
        self.second_side = second_side

    def area(self):
        return self.first_side * self.second_side

    def perimeter(self):
        return 2 * (self.first_side + self.second_side)

def check_shape_type(line, n):
    data = [d.strip() for d in line.split(",")]
    available_shapes = {"circle": 3, "square": 3, "rectangle": 4}
    available_colors = ["purple", "black", "white"]

    shape_type = data[0].lower()
    if shape_type not in available_shapes:
        raise ValueError(f"error: unknown shape in line idx-{n}: {shape_type}.")

    expected_len = available_shapes[shape_type]
    if len(data) != expected_len:
        raise ValueError(f"error: unexpected size: {len(data)} arguments, size of line idx-{n} must be: {expected_len} arguments.")

    shape_color = data[1]
    if shape_color not in available_colors:
        raise ValueError(f"error: unexpected color in line idx-{n}: {shape_color}, available colors: {available_colors}.")

    for i, parameter in enumerate(data[2:], start=2):
        try:
            float(parameter)
            int(parameter)
        except ValueError:
            raise ValueError(f"error: parameter in line idx-{n}, parameter: {data[i]} must be <int or float> type.")


def read_file(file):
    three_lines = []
    n = 0
    with open(file, "r") as r:
        for n, line in enumerate(r):
            line = line.strip()
            try:
                check_shape_type(line, n)
                data = [d.strip() for d in line.split(",")]
                three_lines.append(data)
                n += 1
            except ValueError as e:
                raise ValueError(f"{e}")

    return three_lines

def what_color(color):
    if color == "purple":
        return Purple()
    elif color == "white":
        return White()
    else:
        return Black()

def call_methods(shapes_data):
    results = {}
    n = 3
    for i in range(n):
        if shapes_data[i][0] == "circle":
            color = what_color(shapes_data[i][1])
            radius = float(shapes_data[i][2])
            circle = Circle(color, radius)
            results["circle"] = f"color: {circle.color.color_getter()}, area: {circle.area()}, perimeter: {circle.perimeter()}."
        elif shapes_data[i][0] == "square":
            color = what_color(shapes_data[i][1])
            side = float(shapes_data[i][2])
            square = Square(color, side)
            results["square"] = f"color: {square.color.color_getter()}, area: {square.area()}, perimeter: {square.perimeter()}."
        else:
            color = what_color(shapes_data[i][1])
            first_side = float(shapes_data[i][2])
            second_side = float(shapes_data[i][3])
            rectangle = Rectangle(color, first_side, second_side)
            results["rectangle"] = f"color: {rectangle.color.color_getter()}, area: {rectangle.area()}, perimeter: {rectangle.perimeter()}."

    return results

def write_file(file, message):
    with open(file, "a") as a:
        for key, value in message.items():
            a.write(f"Shape: {key}, {value} \n")
if __name__=="__main__":

    try:
        shapes_data = read_file("shapes_data.txt")
    except ValueError as e:
        print(f"{e}")
        exit(1)
    print(shapes_data)

    results = call_methods(shapes_data)
    print(results)

    write_file("shapes_result.txt", results)

