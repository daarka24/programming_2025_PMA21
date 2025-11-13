from abc import ABC, abstractmethod


class Color(ABC):
    @abstractmethod
    def apply_color(self) -> str:
        pass


class Red(Color):
    def apply_color(self) -> str:
        return "Red"


class Blue(Color):
    def apply_color(self) -> str:
        return "Blue"


class Green(Color):
    def apply_color(self) -> str:
        return "Green"
