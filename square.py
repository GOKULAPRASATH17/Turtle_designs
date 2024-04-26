import turtle
import random as r
t=turtle.Turtle()
t.begin_fill()
t.speed(0)
h=int(input())
m=3
color=["red","green","blue","yellow","skyblue","pink","orange","purple"]
for i in range(h,0,-1):
    #print(i)
    t.begin_fill()
    for j in range(4):
        t.forward((100*m)-abs(m*(h-i))*2)
        #print(200-abs(m*(h-i)))
        t.left(90)
    t.fillcolor(r.choice(color))
    t.up()
    t.goto(m*(h+1-i),m*(h+1-i))
    t.down()
    t.end_fill()
