# graphic.py
import turtle
t = turtle.Turtle()
w = turtle.Screen()
w.bgcolor("#1ba100")
g = turtle.pen()
t.speed(0)
t.color("gold")
t.penup()
t.setposition(0, -95)
t.pendown()
t.width(5 + 1)

for i in range (3):
	t.forward(250)
	t.left(120)

for x in range (2):
	t.forward(250)
	t.left(120)
	t.forward(250)

for j in range(2):
	t.left(120)
	t.forward(250)

for a in range(1):
	t.left(120)
	t.forward(500)

for l in range(2):
	t.left(120)
	t.forward(250)

import turtle
j = turtle.pen()
l = turtle.Turtle()
l.speed(0)
l.penup()
l.setposition(-125, -95)
l.pendown()
l.color("gold")
l.width(5 + 1)
l.circle(72)
l.left(90)
l.forward(213)

import turtle
a = turtle.pen()
u = turtle.Turtle()
u.speed(0)
u.penup()
u.setposition(125, -95)
u.pendown()
u.color("gold")
u.width(5 + 1)
u.circle(72)
u.left(90)
u.forward(213)

import turtle
p = turtle.pen()
o = turtle.Turtle()
o.speed(0)
o.penup()
o.setposition(0, 125)
o.pendown()
o.color("gold")
o.width(5 + 1)
o.circle(72)
o.left(90)
o.forward(213)

import turtle
def half(t,size,x,y,color):
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.color(color)
	for i in range (2,15):
		t.forward(size)
		t.left(6)
	for l in range (2,28):
		t.backward(size)
		t.right(6)
	for l in range (2,15):
		t.forward(size)
		t.left(8)





def circle(t,size,x,y,color):
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.color(color)
	for i in range (1,61):
		t.forward(size)
		t.right(6)

def logan():
	t = turtle.Turtle()
	t.width(5 + 1)
	circle(t,3,50,115,"#ffcc00")
	circle(t,3,-50,115,"#ffcc00")
	circle(t,2,0,50,"#ffcc00")
	half(t,5,0,-25,"#ffcc00")


logan()
holdit = input("press to exit")

turtle.done()
