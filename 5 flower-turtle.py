import turtle
tao = turtle.Pen()
tao.shape('turtle')

def flower():
    '''for drawing flower'''
    for i in range(10):
        tao.circle(50)
        tao.left(36)

    for i in range(10):
        tao.penup()
        tao.goto(200,200)
        tao.pendown()
        tao.circle(50)
        tao.left(36)
        tao.penup()
        tao.goto(0,0)

    for i in range(10):
        tao.penup()
        tao.goto(-200,200)
        tao.pendown()
        tao.circle(50)
        tao.left(36)
        tao.penup()
        tao.goto(0,0)

    for i in range(10):
        tao.penup()
        tao.goto(200,-200)
        tao.pendown()
        tao.circle(50)
        tao.left(36)
        tao.penup()
        tao.goto(0,0)

    for i in range(10):
        tao.penup()
        tao.goto(-200,-200)
        tao.pendown()
        tao.circle(50)
        tao.left(36)
        tao.penup()
        tao.goto(0,0)
 
