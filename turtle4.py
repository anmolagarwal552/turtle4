import turtle

myPen = turtle.Pen()
win = turtle.Screen()
win.bgcolor('black')
myPen.speed(-200)
myPen.color('white')

side = 1
for i in range(360):
	myPen.forward(side)
	myPen.left(92)
	side+=5
	myPen.width(i/100 +1)

turtle.listen()
turtle.mainloop()
