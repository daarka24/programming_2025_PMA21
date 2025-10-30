from abc import ABC, abstractmethod

class Color(ABC):
    def apply_color(self, shape_name: str) -> str:
        pass
    def name(self) -> str:
        return self.__class__.__name__.lower()
