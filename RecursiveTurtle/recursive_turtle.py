from turtle import Turtle

def stareye(x):
    if x == 0:
        return
    else:
        T.color('red')
        T.width(3)
        T.forward(45)
        T.left(45)
        T.forward(40)
        T.left(40)
        T.backward(100)
        T.left(35)
        stareye(x-10)

def circle(x):
    if x == 0:
        return
    else:    
        T.forward(2)
        T.left(2)
        circle(x-1)

def flower():
    T.color('blue')
    T.right(45)
    circle(180)
    T.color('red')
    T.right(45)
    circle(180)
    T.color('yellow')
    T.right(45)
    circle(180)
    T.color('green')
    T.right(45)
    circle(180)
    T.color('pink')
    T.right(45)
    circle(180)
    T.color('black')
    T.right(45)
    circle(180)
    T.color('brown')
    T.right(45)
    circle(180)
    T.color('orange')
    T.right(45)
    circle(180)

T = Turtle()
T.shape('turtle')
T.width(3)
T.speed(10000)

flower()
T.color('green')
T.width(5)
T.right(90)
T.forward(300)

T.color('brown')
T.right(90)
T.forward(200)
T.right(90)

T.color('green')
T.forward(300)
T.width(3)
flower()

T.right(180)
T.width(5)
T.color('green')
T.forward(300)
T.color('brown')
T.left(90)
T.forward(400)
T.left(90)
T.color('green')
T.forward(300)
T.width(3)
flower()






