import turtle
def setpen(x, y):
    # taibi
    turtle.penup()
    #
    turtle.goto(x, y)
    # luobi
    turtle.pendown()
    turtle.setheading(0)

def circle(x, y, r, color):
    n = 36
    angle = 360 / n
    pi = 3.1415926
    
    # zhouchang
    c = 2 * pi * r
    # meitiaobiandechangdu
    l = c / n
    # qishiweizhi
    start_x = x - 1 / 2
    start_y = y + r
    
    setpen( start_x, start_y )
    turtle.pencolor( color )
    turtle.fillcolor( color )
    #tianchong
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(l)
        turtle.right(angle)
    turtle.end_fill()

def five_star(l):
    setpen(0, 0)
    turtle.setheading(162)
    turtle.forward(150)
    turtle.setheading(0)
    turtle.fillcolor('WhiteSmoke')
    turtle.begin_fill()
    turtle.hideturtle()
    turtle.penup()
    for i in range(5):
        turtle.forward(l)
        turtle.right(144)
    turtle.end_fill()

def sheild():
    circle(0, 0, 300, 'red' )
    circle(0, 0, 250, 'white' )
    circle(0, 0, 200, 'red' )
    circle(0, 0, 150, 'blue' )
    five_star(234)
    #five_star(284)
    
if __name__ == '__main__':
    sheild()
    turtle.done()
