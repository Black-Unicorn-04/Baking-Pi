import random
import turtle


for j in range(10):
    color = random.choice(['red','orange','pink','purple','green','blue','yellow'])
    turtle.color(color)

    for i in range(8):
        turtle.forward(100)
        turtle.right(45)
    turtle.right(36)



turtle.exitonclick()