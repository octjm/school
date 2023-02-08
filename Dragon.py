#imported stuff
import turtle 
t = turtle.Turtle()
s=turtle.Screen()
t.speed(0)
#color
t.color("black" , "gold")
t.begin_fill()
l=0
#start dragon wings
while l<=80:
    t.forward(5)
    t.left(1)
    l+=1
t.forward(50)
l=0
t.right(175)
t.forward(300)
t.left(85)
t.forward(300)
t.right(165)
t.forward(300)
t.left(80)
t.forward(300)
t.left(185)
t.forward(50)
#other dragon wing
while l<=82:
    t.forward(5)
    t.left(1)
    l+=1
l=0
#head
while l<=10:
    t.forward(5)
    t.left(4)
    l+=1
l=0
while l<=67:
    t.forward(5)
    t.right(4)
    l+=1
l=0
while l<=10:
    t.forward(5)
    t.left(4)
    l+=1
t.end_fill()
t.penup()
t.goto(0,-20)
l=0
t.pendown()
#spine
t.right(10)
while l<=11:
    t.forward(20)
    t.left(90)
    t.forward(6)
    t.right(90)
    l+=1
#eyes
t.penup()
t.goto(-100,20)
t.pendown()
t.circle(5)
t.penup()
t.goto(-100,-50)
t.pendown()
t.circle(5)
t.penup()
#move it away
t.goto(1000,1000)
s.exitonclick()