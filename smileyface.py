#smileyface.py lb
import turtle

def half(t,size,x,y,color):
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.color(color)
	for i in range (2,15):
		t.forward(size)
		t.left(5)
	for l in range (2,28):
		t.backward(size)
		t.right(5)
	for l in range (2,15):
		t.forward(size)
		t.left(6.75)





def circle(t,size,x,y,color):
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.color(color)
	for i in range (1,61):
		t.forward(size)
		t.right(6)

def logan():
	twin = turtle.Screen()
	twin.clear()
	t = turtle.Turtle()
	circle(t,5,100,100,"#ff0000")
	circle(t,5,-100,100,"#0000ff")
	circle(t,3,0,0,"#0000ff")
	half(t,10
	,0,-100,"#0000ff")


logan()
holdit = input("press to exit")
