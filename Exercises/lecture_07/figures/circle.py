from turtle import Turtle

from lecture_07.figures.figure import Figure


class Circle(Figure):

    def __init__(self, **params):
        super().__init__(**params)
        self.radius = params['radius']

    def __str__(self):
        return super().__str__()

    def draw(self, turtle: Turtle):
        super().draw(turtle)
        self.jump_to(turtle, self.center_x, self.center_y - self.radius)
        turtle.circle(self.radius)
        self.jump_to(turtle, 0, 0)
