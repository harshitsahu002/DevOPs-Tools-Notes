import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")
t.begin_fill() # this is the tool which is used to fill the square, it begins here ; by default it is turtle's color
t.fillcolor("red") # from this function we can set the fill color
t.shape("circle")
t.color("red")
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill() # here the filling of square end's

# OR 

t.begin_fill() 
t.fillcolor("red")
for i in range(4):
  t.forward(100)
  t.left(90)
t.end_fill()
  

