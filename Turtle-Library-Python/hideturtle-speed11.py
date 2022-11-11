import turtle
t = turtle.Turtle()
t.hideturtle() # through this the turtle get hide
t.speed(0) # speed of the turtle/cursor :- 'fastest' : 0 ;'fast' : 10 ; 'normal' : 6 ; 'slow' : 3 ; 'slowest' :  1
for i in range(4):
  t.forward(100)
  t.left(90)
