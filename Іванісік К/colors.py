from abc import ABC, abstractmethod


class Color(ABC):

    @abstractmethod
    def apply_color(self) -> str:
        pass


class Red(Color):
    def apply_color(self) -> str:
        return "Applying Red color"


class Blue(Color):
    def apply_color(self) -> str:
        return "Applying Blue color"


class Green(Color):
    def apply_color(self) -> str:
        return "Applying Green color"