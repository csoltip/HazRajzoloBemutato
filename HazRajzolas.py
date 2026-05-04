import turtle

turtle.color("red")
turtle.speed(0)
turtle.pensize(2)

# négyzet
i = 0
while i < 4:
    turtle.forward(100)
    turtle.left(-90)
    i += 1

turtle.done()
