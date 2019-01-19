import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.setup(240,320)
s.bgcolor('black')
def turtlefun(tempx, feelsx):
    #Change color based on temperature
    if tempx<32:
        t.color('cyan')
    elif tempx>32&tempx<=40:
        t.color('blue')
    elif tempx>40&tempx<=60:
        t.color('yellow')
    elif tempx>60&tempx<=75:
        t.color('orange')
    else:
        t.color('green')
    t.up()
    t.setx(-85)
    t.sety(120)
    t.down()
    t.write(tempx, font=("Times", 16, "normal"))
    t.up()
    t.forward(30)
    t.down()
    t.write('Temperature', font=("Times", 16, "normal"))
    t.up()
    t.setx(-85)
    t.sety(120)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.down()
    t.write(feelsx, font=("Times", 16, "normal"))
    t.up()
    t.forward(30)
    t.down()
    t.write('Feels Like', font=("Times", 16, "normal"))
