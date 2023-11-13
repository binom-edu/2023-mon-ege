import turtle

turtle.speed(0)
k = 20
turtle.left(90)

turtle.pendown()
for i in range(20):
    turtle.right(60)
    turtle.forward(10 * k)
    turtle.right(60)

turtle.penup()
for x in range(10):
    for y in range(-5, 5):
        turtle.goto(x * k, y * k)
        turtle.dot(5)

turtle.mainloop()
