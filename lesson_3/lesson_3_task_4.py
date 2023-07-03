from turtle import *
from coordinates import cat

t = Turtle()

t.screen.setup(800, 800)
t.up()
t.goto(cat[0])
t.down()
for i in range(1, len(cat)):
    t.goto(cat[i])

t.screen.exitonclick()
t.screen.mainloop()
