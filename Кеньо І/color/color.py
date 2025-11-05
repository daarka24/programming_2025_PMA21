import math
from abc import ABC, abstractmethod

class Color(ABC):
    @abstractmethod
    def apply_color(self) -> str:
        pass



