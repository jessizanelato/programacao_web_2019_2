class Shape:

    def __init__(self, color="Black", filled=False):
        self._color = color
        self._filled = filled
    
    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_filled(self):
        return self._filled

    def set_filled(self, filled):
        self._filled = filled