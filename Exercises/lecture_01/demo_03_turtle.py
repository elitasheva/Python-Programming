import turtle
t = turtle.Turtle()
colors = ['red', 'green', 'blue', 'purple', 'yellow', 'orange']

i = 10
t.setx(0)
t.sety(0)
while True:
    t.color(colors[i % 6])
    t.right(i % 60)
    t.forward(10)
    i += 5

t.done