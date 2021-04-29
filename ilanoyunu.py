import turtle
import time

suret = 0.12

import random

pencere = turtle.Screen()
pencere.title("Ilan oyunu")
pencere.bgcolor("lightblue")
pencere.setup(width=600, height=600)
pencere.tracer(0)

baw = turtle.Turtle()
baw.speed(0)
baw.shape("square")
baw.color("red")
baw.penup()
baw.goto(0, 100)
baw.direction= "stop"

yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color("yellow")
yemek.penup()
yemek.goto(0, 0)
yemek.shapesize(0.80, 0.80)

quyruqlar = []
xal=0

yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape("square")
yaz.color("white")
yaz.penup()
yaz.goto(0, 260)
yaz.hideturtle()
yaz.write("xal: {}".format(xal), align = "center", font = ("Courier", 24, "normal"))

def move():
    if baw.direction == "up":
        y = baw.ycor()
        baw.sety((y + 20))
    if baw.direction == "down":
        y = baw.ycor()
        baw.sety((y - 20))
    if baw.direction == "right":
        x = baw.xcor()
        baw.setx((x + 20))
    if baw.direction == "left":
        x = baw.xcor()
        baw.setx((x - 20))


def goUp():
    if baw.direction != "down":
        baw.direction = "up"

def goDown():
    if baw.direction != "up":
        baw.direction = "down"

def goRight():
    if baw.direction != "left":
        baw.direction = "right"

def goLeft():
    if baw.direction != "right":
        baw.direction = "left"

pencere.listen()
pencere.onkey(goUp, "Up")
pencere.onkey(goDown, "Down")
pencere.onkey(goRight, "Right")
pencere.onkey(goLeft, "Left")

while True:
    pencere.update()

    if baw.xcor() > 300 or baw.xcor() < -300 or baw.ycor() > 300 or baw.ycor() < -300:
        time.sleep(0)
        baw.goto(0, 0)
        baw.direction = "stop"

        for quyruq in quyruqlar:
            quyruq.goto(1000, 1000)

        quyruqlar = []
        xal = 0
        suret = 0.12

    if baw.distance(yemek) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek.goto(x, y)

        xal = xal + 10
        yaz.clear()
        yaz.write("xal: {}".format(xal), align = "center", font = ("Courier", 24, "normal"))

        suret = suret - 0.001

        yeniQuyruq = turtle.Turtle
        yeniQuyruq.speed(0)
        yeniQuyruq.shape("square")
        yeniQuyruq.color("green")
        yeniQuyruq.penup()
        quyruqlar.append(yeniQuyruq)

    for i in range(len(quyruqlar) - 1, 0, -1):
        x = quyruqlar[i -1].xcor()
        y = quyruqlar[i -1].ycor()
        quyruqlar[i].goto(x, y)

    if len(quyruqlar) > 0:
        x = baw.xcor()
        y = baw.ycor()
        quyruqlar[0].goto(x, y)

    move()
    time.sleep(suret)