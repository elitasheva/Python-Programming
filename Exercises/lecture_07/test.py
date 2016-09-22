import importlib
from turtle import Turtle, done as turtle_done

params = {'center_x': 5, 'center_y': 2, 'radius': 50, 'side': 100, 'color': "blue"}

t = Turtle()
figures_str = ["Circle", "Square", "Triangle", "Polygon"]
for figure in figures_str:
    name_module = figure.lower()
    my_module = importlib.import_module(name_module, "lecture_07")
    current_class = getattr(my_module, figure)
    instance = current_class(**params)
    instance.draw(t)
turtle_done()

# circle = Circle(**params)
# square = Square(**params)
# circle.draw(t)
# square.draw(t)

# print(circle == square)
# print(getattr(circle, 'radius', "no attribute radius"))
# print(getattr(circle, 'side', "no attribute side"))
# print(getattr(square, 'side', "no attribute side"))
# # checks classes not instances
# print(issubclass(Circle, Figure))
# print(issubclass(Square, Figure))