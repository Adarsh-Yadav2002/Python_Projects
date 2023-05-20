import turtle as t
t.speed(0)
t.bgcolor('black')
t.pencolor('red')
for i in range(300):
    t.rt(i)
    t.circle(120,i)
    t.fd(i)
    t.rt(90)
t.done()