import turtle
turtle.setup(666,666)
for i in range(3):
 turtle.fd(81)
 turtle.left(120)
turtle.penup()
turtle.goto(81,81)
turtle.pendown()
for i in range(4):
 turtle.penup()
 turtle.fd(39)
 turtle.pendown()
 turtle.fd(81)
 turtle.penup()
 turtle.fd(39)
 turtle.left(90)
turtle.exitonclick()
