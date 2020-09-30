import turtle
counter=0

while counter <32 :
    for i in range(3):
        turtle.forward(50)
        turtle.right(90)
    turtle.right(10)
    counter+=1

turtle.exitonclick()