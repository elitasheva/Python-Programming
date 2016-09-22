import turtle

t = turtle.Turtle()
turtle.speed("fastest")
size = 8
side = 20


def draw_rectangle():
    for i in range(4):
        t.forward(side)
        t.right(90)

for i in range(8):
    for j in range(8):
        if i % 2 != 0:
            if j % 2 == 0:
                t.begin_fill()
            draw_rectangle()
            t.end_fill()
        else:
            if j % 2 != 0:
                t.begin_fill()
            draw_rectangle()
            t.end_fill()
        t.setx(t.xcor() + side)
    if i < 7:
        t.setx(t.xcor() - 8 * side)
        t.sety(t.ycor() + side)

turtle.exitonclick()
