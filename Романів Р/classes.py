from math import pi, sqrt


class Color:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return self.color

    def __str__(self):
        return self.color


class Red(Color):
    def __init__(self):
        Color.__init__(self, "червоний")


class Blue(Color):
    def __init__(self):
        Color.__init__(self, "синій")


class Yellow(Color):
    def __init__(self):
        Color.__init__(self, "жовтий")





class Polygon:
    def __init__(self, angles, sides=None, color=None):
        self.angels = angles
        if sides:
            if len(sides) == angles:
                self.sides = sides
            else:
                raise ValueError("Кількість кутів не сходиться з кількістю сторін")
        else:
            self.sides = [0] * angles
        self.color = color

    @property
    def perimeter(self):
        return sum(self.sides)

    @property
    def area(self):
        raise ValueError("Невідома фігура")

    def __repr__(self):
        if self.color:
            return f"{str(self.color).title()} многокутник з периметром {self.perimeter}."
        return f"Многокутник з периметром {self.perimeter}."


    def __str__(self):
        return self.__repr__()





class Triangle(Polygon):
    def __init__(self, sides=None, color=None):
        if sides and len(sides) != 3:
            raise ValueError("Трикутник має мати 3 сторони")
        Polygon.__init__(self, 3, sides, color)

    def __repr__(self):
        if self.color:
            return f"{str(self.color).title()} трикутник з периметром {self.perimeter} і площею {self.area}."
        return f"Трикутник з периметром {self.perimeter} і площею {self.area}."

    @property
    def area(self):
        p = self.perimeter / 2
        return sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))




class Quadrangle(Polygon):
    def __init__(self, sides=None, color=None):
        if sides and len(sides) != 4:
            raise ValueError("Чотирикутник має мати 4 сторони")
        Polygon.__init__(self, 4, sides, color)

    def __repr__(self):
        if self.color:
            return f"{str(self.color).title()} чотирикутник з периметром {self.perimeter}."
        return f"Чотирикутник з периметром {self.perimeter}."




class Rectangle(Quadrangle):
    def __init__(self,sides=None,color=None):
        if sides and len(sides) != 2:
            raise ValueError("Неправильно введено параметриб довжина списку має бути 2")
        Polygon.__init__(self,4, sides * 2, color)

    def __repr__(self):
        if self.color:
            return f"{str(self.color).title()} прямокутник з периметром {self.perimeter} та площею {self.area}."
        return f"Прямокутник з периметром {self.perimeter} та площею {self.area}."

    @property
    def area(self):
        return self.sides[0] * self.sides[1]




class Square(Rectangle):
    def __init__(self, side=None, color=None):
        if not isinstance(side, int) and not isinstance(side, float):
            raise ValueError("Сторона має бути числом")
        Rectangle.__init__(self, [side] * 2, color)

    def __repr__(self):
        if self.color:
            return f"{str(self.color).title()} квадрат з периметром {self.perimeter} та площею {self.area}."
        return f"Квадрат з периметром {self.perimeter} та площею {self.area}."

    @property
    def area(self):
        return self.sides[0] ** 2




class Circle(Polygon):
    def __init__(self, r, color=None):
        Polygon.__init__(self, 0, sides=None, color=color)
        self.radius = r

    def __repr__(self):
        if self.color:
            color = str(self.color)[:-2] + "е" if str(self.color).endswith("ий") else str(self.color)[:-2] + "є"
            return f"{color.title()} коло з периметром {self.perimeter} та площею {self.area}."
        return f"Коло з периметром {self.perimeter} та площею {self.area}."

    @property
    def perimeter(self):
        return 2 * self.radius * pi

    @property
    def area(self):
        return  (self.radius ** 2) * pi