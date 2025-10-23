from abc import ABC, abstractmethod

class Color(ABC):
    @abstractmethod
    def get_color_description(self) -> str:
        pass