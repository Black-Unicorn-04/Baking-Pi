import turtle

turtle.shape("turtle")
#medium sized shape

for i in range(0,10):
    turtle.right(36)
    for i in range(0,5):
        turtle.forward(100)
        turtle.right(72)

#small shape

for i in range(0,10):
    turtle.right(36)
    for i in range(0,5):
        turtle.forward(50)
        turtle.right(72)

#big shape

for i in range(0,10):
    turtle.right(36)
    for i in range(0,5):
        turtle.forward(200)
        turtle.right(72)
        
#slightly smaller than the one before
for i in range(0,10):
    turtle.right(36)
    for i in range(0,5):
        turtle.forward(150)
        turtle.right(72)

turtle.exitonclick()
