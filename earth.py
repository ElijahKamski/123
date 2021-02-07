import turtle as tt 
from random import randint as rnd 
from random import choice as ch

t = tt.Turtle()
tt.tracer(0, 0)

def goto_up(x, y):
	t.up()
	t.goto(x, y)
	t.down()

s = 300

goto_up(-s, -s)
t.color("Black")
t.begin_fill()
t.goto(s, -s)
t.goto(s, s)
t.goto(-s, s)
t.goto(-s, -s)
t.end_fill()

for k in range(10000):
	goto_up(rnd(-s, s), rnd(-s, s))

	t.color("Green" if rnd(0, 100) == 12 else "White")
	t.dot(rnd(2, 4))

tt.mainloop()