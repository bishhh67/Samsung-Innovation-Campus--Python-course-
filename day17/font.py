import turtle
import time
import math

screen = turtle.Screen()
screen.setup(900, 600)
screen.bgcolor("skyblue")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

start_time = time.time()

# ---------- DRAW FUNCTIONS ----------

def draw_sun(y):
    t.penup()
    t.goto(300, y)
    t.color("orange", "yellow")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

def draw_cloud(x, y):
    t.color("white")
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    t.circle(20)
    t.goto(x+25, y)
    t.circle(25)
    t.goto(x+55, y)
    t.circle(20)
    t.end_fill()

def draw_mountain(x, y):
    t.color("darkgreen", "forestgreen")
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    t.goto(x+150, y+200)
    t.goto(x+300, y)
    t.goto(x, y)
    t.end_fill()

def draw_house(x, y):
    # house body
    t.color("brown", "peachpuff")
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    for _ in range(4):
        t.forward(60)
        t.left(90)
    t.end_fill()

    # roof
    t.color("black", "red")
    t.begin_fill()
    t.goto(x, y+60)
    t.goto(x+30, y+100)
    t.goto(x+60, y+60)
    t.goto(x, y+60)
    t.end_fill()

def draw_bird(x, y):
    t.penup()
    t.goto(x, y)
    t.color("black")
    t.setheading(60)
    t.circle(10, 120)
    t.setheading(120)
    t.circle(10, 120)

# ---------- ANIMATION LOOP ----------

sun_y = -200
cloud_x = -400
bird_x = -400

while time.time() - start_time < 60:

    t.clear()

    # Ground
    t.penup()
    t.goto(-450, -200)
    t.color("green", "lightgreen")
    t.begin_fill()
    t.goto(450, -200)
    t.goto(450, -300)
    t.goto(-450, -300)
    t.goto(-450, -200)
    t.end_fill()

    # Mountains
    draw_mountain(-450, -200)
    draw_mountain(-150, -200)
    draw_mountain(150, -200)

    # Houses
    draw_house(-300, -260)
    draw_house(-200, -260)
    draw_house(-100, -260)
    draw_house(0, -260)
    draw_house(100, -260)

    # Sun rising slowly
    draw_sun(sun_y)
    sun_y += 0.2

    # Clouds moving slowly
    draw_cloud(cloud_x, 180)
    draw_cloud(cloud_x + 200, 220)
    cloud_x += 0.3
    if cloud_x > 500:
        cloud_x = -500

    # Birds flying slowly
    draw_bird(bird_x, 120)
    draw_bird(bird_x + 40, 140)
    draw_bird(bird_x + 80, 120)
    bird_x += 0.5
    if bird_x > 500:
        bird_x = -500

    screen.update()
    time.sleep(0.05)

turtle.done()
