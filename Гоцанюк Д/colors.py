from abc import ABC, abstractmethod

class BaseColor(ABC):
    @abstractmethod
    def fill(self) -> str:
        pass

class Red(BaseColor):
    def fill(self) -> str:
        return "Applying Red color"

class Blue(BaseColor):
    def fill(self) -> str:
        return "Applying Blue color"

class Green(BaseColor):
    def fill(self) -> str:
        return "Applying Green color"