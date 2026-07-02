import turtle
"""
turtle.forward(100)
turtle.exitonclick()

#turtle.shape("turtle")

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)



#turtle.speed(1)
for i in range (4):
    turtle.forward(100)
    if i%2 == 0:
      turtle.left(60)
    else:
     turtle.left(120)

turtle.exitonclick()




for i in range(10):
    i +=1
    print(i)


for i in range (4):
    #turtle.forward(100)
    for i2 in range(10):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(3)
        turtle.pendown()
    if i%2 == 0:
      turtle.left(60)
    else:
     turtle.left(120)
    
turtle.color("red")
turtle.shape("turtle")
for side_len in range(50,410,10):
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(10)
 """


for i2 in range(5):
    for i in range(5):
        turtle.penup()
        turtle.forward(20)
        turtle.dot(10, "red")
    if i2 % 2 == 0:

      turtle.right(90)
    else:
     turtle.right(90)
     turtle.forward(20)

turtle.exitonclick()