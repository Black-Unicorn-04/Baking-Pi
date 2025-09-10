# import turtle
# import random

# length = int(random.choice(['10','20','30','40','50']))
# angle = int(random.choice(['10','20','30','40','50']))
# num = int(random.choice(['4','6','8','12']))


# for i in range(num):
#     turtle.forward(length)
#     turtle.right(angle)

# turtle.exitonclick()


import turtle
import random
lines = random.randint(5,40)

for i in range(lines):
    length = random.randint(25,100)
    rotate = random.randint(1,365)
    turtle.forward(length)
    turtle.right(rotate)

turtle.exitonclick()