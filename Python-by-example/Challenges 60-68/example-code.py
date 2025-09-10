import turtle
import random

turtle.shape("turtle")

def gem ():
    

    color1 = random.choice(['black', 'grey', 'green', 'red'])
    color2 = random.choice(['yellow', 'pink', 'orange'])

    turtle.begin_fill()
    turtle.color(color1, color2)
    
    for i in range(10):
        turtle.right(36)
        for i in range(0,5):
            turtle.forward(100)
            turtle.right(72)

    turtle.end_fill()

scr = turtle.Screen()



turtle.pendown()

turtle.pensize(1)

gem()



turtle.penup()

turtle.pensize(5)

turtle.right(10)
turtle.forward(150)


turtle.pendown()

gem()





turtle.exitonclick()