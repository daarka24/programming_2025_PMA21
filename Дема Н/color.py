from abc import ABC, abstractmethod
import math

class Color(ABC):
    def apply_color(self, shape_name: str) -> str:
        pass
    def name(self) -> str:
        return self.__class__.__name__.lower()
class Pink(Color):
    def apply_color(self, shape_name: str) -> str:
        return "Color: pink"
class Brown(Color):
    def apply_color(self, shape_name: str) -> str:
        return "Color: brown"
class White(Color):
    def apply_color(self, shape_name: str) -> str:
        return "Color: white"