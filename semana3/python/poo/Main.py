from Shape import Shape
from Rectangle import Rectangle
from Circle import Circle

shapes = []
shapes.append(Rectangle(10, 4))
shapes.append(Circle(4, "Red", True))

template_header = "{:10} {:6} {:10} {:6} {:7}"
template_row = "{:10} {:6.2f} {:10.2f} {:6} {:7}"
print(template_header.format("", "Area", "Perimeter", "Color", "Filled"))

for shape in shapes:
    print(template_row.format(shape.__class__.__name__, shape.get_area(),
    shape.get_perimeter(), shape.get_color(),
    ("Yes" if shape.get_filled() else "No")))