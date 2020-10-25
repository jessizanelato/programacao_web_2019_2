from Shape import Shape
from math import pi as PI

class Circle(Shape):
    def __init__(self, radius, color="Black", filled=False):
        super().__init__(color, filled)
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return PI * self.__radius ** 2

    def get_perimeter(self):
        return 2 * PI * self.__radius