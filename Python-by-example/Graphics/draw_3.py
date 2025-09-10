import turtle

scr = turtle.Screen()
scr.bgcolor("pink") #color of the screen
turtle.pensize(3)   #size of the pen

#Shape one

for i in range(0,10): #specifies the number of times it will be repeated
    turtle.right(36)
    for i in range(0,5):
        turtle.forward(60)
        turtle.right(72)


#Switch location

#turtle.penup()
turtle.forward(200)
#turtle.pendown()

#scrbgcolor("purple") this code spoils it all. : (
#turtle.pensize(4)

#Shape two
for i in range(0,10):
    turtle.right(36)
    for i in range(0,5):
        turtle.forward(20)
        turtle.right(72)
'''
for i in range(0,10): #specifies the number of times it will be repeated
    turtle.right(36)
    for i in range(0,5):
        turtle.forward(60)
        turtle.right(72)'''

turtle.exitonclick()
