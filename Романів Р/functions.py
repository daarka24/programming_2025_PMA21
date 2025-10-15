from classes import *
import csv

def make_color_class(color):
    lowercase_color = color.lower()
    if lowercase_color == "червоний":
        return Red()
    elif lowercase_color == "жовтий":
        return Yellow()
    elif lowercase_color == "синій":
        return Blue()
    return Color(lowercase_color)


def is_digit(n):
    try:
        float(n)
        return True
    except:
        return False



def read_triangles_or_shapes(filename, shape=False):
    shapes = []
    with open(filename, encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                if shape:
                    angles = int(row["Angles"])

                if row["Sides"].lower() == "none":
                    sides = None
                else:
                    sides = [float(el) for el in row["Sides"].split() if is_digit(el)]

                if row["Color"].lower() == "none":
                    color = None
                else:
                    color = make_color_class(row["Color"])

                if shape:
                    shapes.append(Polygon(angles,sides,color))
                else:
                    shapes.append(Triangle(sides, color))
            except:
                print("invalid data to read:", row)
                continue

    return shapes


def read_squares_or_circles(filename, circle=False):
    shapes = []
    with open(filename, encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                if row["Color"].lower() == "none":
                    color = None
                else:
                    color = make_color_class(row["Color"])

                if circle:
                    radius = float(row["Radius"])
                    shapes.append(Circle(radius, color))
                else:
                    side = float(row["Side"])
                    shapes.append(Square(side, color))
            except Exception as e:
                print("invalid data to read:", row, e)
                continue
    return shapes


def read_rectangles(filename):
    shapes = []
    with open(filename, encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                if row["Sides"].lower() == "none":
                    sides = None
                else:
                    sides = [float(el) for el in row["Sides"].split() if is_digit(el)]

                if row["Color"].lower() == "none":
                    color = None
                else:
                    color = make_color_class(row["Color"])

                shapes.append(Rectangle(sides, color))
            except:
                print("invalid data to read:", row)
                continue

    return shapes

def read_from_file():
    return read_triangles_or_shapes("input_shapes.csv", shape=True) + \
        read_triangles_or_shapes("input_triangles.csv") + \
        read_squares_or_circles("input_circles.csv", circle=True) + \
        read_squares_or_circles("input_squares.csv") + read_rectangles("input_rectangles.csv")
