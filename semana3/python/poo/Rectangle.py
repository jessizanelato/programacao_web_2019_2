from Shape import Shape

class Rectangle(Shape):
    
    def __init__(self, length, breadth, color="Black", filled=False):
        super().__init__(color, filled)
        self.__length = length
        self.__breadth = breadth
    
    def get_length(self):
        return self.__length
    
    def set_length(self, length):
        self.__length = length
    
    def get_breadth(self):
        return self.__breadth
    
    def set_breadth(self, breadth):
        self.__breadth = breadth

    def get_area(self):
        return self.__length * self.__breadth
    
    def get_perimeter(self):
        return 2 * (self.__length + self.__breadth)