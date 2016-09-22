class Figure:
    # constructor
    def __init__(self, **params):
        self.center_x = params['center_x']
        self.center_y = params['center_y']
        self.color = params['color']

    def __str__(self):
        return "{} - center_x={} , center_y={}, color={}".format(
            self.__class__.__name__, self.center_x, self.center_y, self.color
        )

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and self.center_x == other.center_x
                    and self.center_y == other.center_y and self.color == other.color)

    def draw(self, turtle):
        turtle.color(self.color)

    def jump_to(self, turtle, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
