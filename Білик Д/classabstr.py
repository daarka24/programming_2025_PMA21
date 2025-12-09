from abc import ABC, abstractmethod

class Color(ABC):
    @abstractmethod
    def choose(self):
        pass
class RedColor(Color):
    def choose(self):
        return "червоний колір"
class GreenColor(Color):
    def choose(self):
        return "зелений колір"
class WhiteColor(Color):
    def choose(self):
        return "білий колір"
class Figure(ABC):
    def __init__(self, color: Color):
        self.color = color
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def peint(self):
        print (f"Обрано {self.color.choose()} для фігури: {self.__class__.__name__}\n Периметр = {self.perimeter()}, а площа = {self.area()}")