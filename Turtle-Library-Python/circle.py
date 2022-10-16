# to get the full info about the circle features run the following command in the shell:-
# >>> import turtle
# >>> help(turtle.circle)

import turtle 
t = turtle.Turtle()
t.circle(20)  # this will make a circle of 20 radius in anti-clockwise
t.circle(-50) # this will make a circle of 50 radius in clockwise

t.reset()  # this will reset the whole changes and drop you at home layout
t.circle(100,180)  # this will make a semi-circle with radius 100

t.reset()
t.circle(100,steps=3)  # this will make a triangle because through this it will complete the circle with three steps

t.reset()
t.circle(70, steps=5)  # this will make a pentagon


