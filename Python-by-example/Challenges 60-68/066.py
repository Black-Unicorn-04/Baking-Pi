import random
import turtle



for i in range(8):
    color = random.choice(['red','orange','pink','purple','green','blue','yellow'])
    turtle.color(color)
    turtle.forward(100)
    turtle.right(45)



turtle.exitonclick()