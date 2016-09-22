import turtle

t = turtle.Turtle()
turtle.speed("fast")

colors = ['red', 'green', 'blue', 'purple', 'yellow', 'orange']

radius = 20
for a in colors:
    count = 3
    radius += 20
    t.color(a)
    while count > 0:
        count -= 1
        t.circle(radius)
t.done

