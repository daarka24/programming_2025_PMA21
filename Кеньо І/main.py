import math
from abc import ABC, abstractmethod

from shape import Circle, Rectangle, Square
from color import Pink, Violet, Purple

def write_to_file(filename, data):
    with open(filename, 'a') as file_one:
        file_one.write(data)
        file_one.write('\n')

if __name__ == "__main__":
    print("demonstrate")
    pink = Pink()
    purple = Purple()
    violet = Violet()

    pink_circle = Circle(10, pink)
    purple_square = Square(5, purple)
    violet_rectangle = Rectangle(4, 7, violet)

    pink_circle.show_details('output.txt')
    purple_square.show_details('output.txt')
    violet_rectangle.show_details('output.txt')


