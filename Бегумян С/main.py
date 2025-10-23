from circle import Circle
from square import Square
from color import Red, Green, Blue
from rectangle import Rectangle
circle = Circle(5, Red())
rectangle = Rectangle(4, 6, Blue())
square = Square(3, Green())

shapes = [circle, rectangle, square]

with open("shapes_output.txt", "w") as file:
    for shape in shapes:
        file.write(shape.describe() + "\n")
        file.write("Area: " + str(round(shape.area(), 2)) + "\n")
        file.write("Perimeter: " + str(round(shape.perimeter(), 2)) + "\n")