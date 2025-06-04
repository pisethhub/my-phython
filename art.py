import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("white")
roblox = turtle.Turtle()
roblox.speed(3)

# Helper: draw filled circle
def draw_circle(x, y, r, color):
    roblox.penup()
    roblox.goto(x, y - r)
    roblox.color(color)
    roblox.begin_fill()
    roblox.pendown()
    roblox.circle(r)
    roblox.end_fill()

# Draw square head
def draw_head():
    roblox.penup()
    roblox.goto(-100, 100)
    roblox.color("gold")
    roblox.begin_fill()
    roblox.pendown()
    for _ in range(4):
        roblox.forward(200)
        roblox.right(90)
    roblox.end_fill()

# Draw eyes
def draw_eyes():
    draw_circle(-40, 30, 10, "black")
    draw_circle(40, 30, 10, "black")

# Draw mouth (smile)
def draw_mouth():
    roblox.penup()
    roblox.goto(-40, -20)
    roblox.setheading(-60)
    roblox.pendown()
    roblox.width(5)
    roblox.circle(50, 120)

# Draw all parts
draw_head()
draw_eyes()
draw_mouth()

roblox.hideturtle()
turtle.done()
