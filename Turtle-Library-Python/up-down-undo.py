import turtle
t = turtle.Turtle()
t.circle(100)

# PROGRAM 1
t.undo()    # undo the last turtle action.
t.right(90)
t.forward(100)
t.left(90)
t.circle(100)

t.reset()
t.goto(0,-100)  #  Move turtle to an absolute position with a specified coordinates (x,y)
t.circle(100)
# but in the above diagram there is a line betwee the circle

# PROGRAM 2
t.up()   # Pull the pen up -- no drawing(line) when moving here pen = Turtle
# you can write turtle.Turtle as turtle.Pen also
t.goto(0,-100)
t.circle(100)
t.down()
t.circle(100)  # Pull the pen down -- drawing(line) when moving
t.reset()
t.up()
t.goto(100,100)
t.down()
t.circle(100)
# by this we just solved that is rising in the above program



