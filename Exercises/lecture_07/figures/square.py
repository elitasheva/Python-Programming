from turtle import Turtle

from lecture_07.figures.figure import Figure


class Square(Figure):
    def __init__(self, **params):
        super().__init__(**params)
        self.side = params['side']

    def draw(self, turtle: Turtle):
        super().draw(turtle)
        self.jump_to(turtle, self.center_x - self.side/2, self.center_y - self.side/2)

        for _ in range(4):
            turtle.forward(self.side)
            turtle.left(90)

        self.jump_to(turtle, 0, 0)