import turtle


turtle.pendown()
turtle.color("black", "red")
turtle.begin_fill()
for i in range(4): 
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.forward(300)

turtle.pendown()
turtle.color("black", "pink")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.backward(600)

turtle.pendown()
turtle.color("black", "orange")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()


turtle.exitonclick()