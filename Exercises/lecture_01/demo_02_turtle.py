import turtle

turtle.speed("slow")

g = 134
l = 120
count = input("Enter the count: ")
count_int = int(count)
while count_int > 0:
    count_int -= 1
    turtle.left(g)
    turtle.forward(l)
