import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.setup(240,320)
s.colormode(255)
s.bgcolor('black')
t.hideturtle()
def setturt(linenum):
    t.up()
    t.setx(-97)
    t.sety(125)
    t.right(90)
    t.forward(30*linenum)
    t.left(90)
    t.down()
    
def turtlefun(tempx, feelsx, precipx, humidx, scorex, typex, pixelx):
    #Change color based on temperature
    if tempx<32:
        t.color('cyan')
    elif tempx>32 and tempx<=40:
        t.color('blue')
    elif tempx>40 and tempx<=60:
        t.color(180,255,0)
    elif tempx>60 and tempx<=75:
        t.color(255,75,0)
    else:
        t.color(57,255,70)
    t.up()
    t.setx(-97)
    t.sety(125)
    t.down()
    t.write('Temperature', font=("Times", 16, "normal"))
    t.up()
    t.forward(130)
    t.down()
    t.write(tempx, font=("Times", 16, "normal"))
    setturt(1)
    if feelsx<32:
        t.color('cyan')
    elif feelsx>32 and feelsx<=40:
        t.color('blue')
    elif feelsx>40 and feelsx<=60:
        t.color(180,255,0)
    elif feelsx>60 and feelsx<=75:
        t.color(255,75,0)
    else:
        t.color(57,255,70)
    t.write('Feels Like', font=("Times", 16, "normal"))
    t.up()
    t.forward(130)
    t.down()
    t.write(feelsx, font=("Times", 16, "normal"))
    setturt(2)
    t.color(55,95,255)
    t.write('Preciptitation',  font=("Times", 16, "normal"))
    t.up()
    t.forward(130)
    t.down()
    t.write(precipx, font=("Times", 16, "normal"))
    t.up()
    t.forward(20)
    t.down()
    t.write('%',  font=("Times", 16, "normal"))
    setturt(3)
    t.color(192,192,192)
    t.write('Humidity', font=("Times", 16, "normal"))
    t.up()
    t.forward(130)
    t.down()
    t.write(humidx, font=("Times", 16, "normal"))
    setturt(4)
    t.color(220, 47, 0)
    t.write('Score', font=("Times", 16, "normal"))
    t.up()
    t.forward(60)
    t.down()
    t.write(scorex, font=("Times", 16, "normal"))
    setturt(5)
    t.write('Type', font=("Times", 16, "normal"))
    t.up()
    t.forward(60)
    t.down()
    t.write(typex, font=("Times", 16, "normal"))
    setturt(6)
    t.write('Pixel', font=("Times", 16, "normal"))
    t.up()
    t.forward(60)
    t.down()
    t.write(pixelx, font=("Times", 16, "normal"))
    
    
