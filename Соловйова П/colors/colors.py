from abc import ABC, abstractmethod

class Color(ABC):
    @abstractmethod
    def get_color_name(self):
        pass

    @abstractmethod
    def get_color_code(self):
        pass

class RedColor(Color):
    def get_color_name(self):
        return "Red"
    def get_color_code(self):
        return "#FF0000"

class BlueColor(Color):
    def get_color_name(self):
        return "Blue"
    def get_color_code(self):
        return "#0000FF"

class GreenColor(Color):
    def get_color_name(self):
        return "Green"
    def get_color_code(self):
        return "#00FF00"
