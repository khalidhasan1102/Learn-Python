import turtle

# setup
screen = turtle.Screen()
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(1)

# function to draw square/rectangle
def draw_rect(color, width, height):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# ground
t.penup()
t.goto(-200, -150)
t.pendown()
draw_rect("green", 400, 100)

# house base
t.penup()
t.goto(-100, -50)
t.pendown()
draw_rect("burlywood", 200, 150)

# roof
t.penup()
t.goto(-120, 100)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.goto(0, 200)
t.goto(120, 100)
t.goto(-120, 100)
t.end_fill()

# door
t.penup()
t.goto(-20, -50)
t.pendown()
draw_rect("saddlebrown", 40, 80)

# left window
t.penup()
t.goto(-80, 20)
t.pendown()
draw_rect("white", 40, 40)

# right window
t.penup()
t.goto(40, 20)
t.pendown()
draw_rect("white", 40, 40)

# window cross
def window_cross(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x + 40, y + 40)
    t.penup()
    t.goto(x + 40, y)
    t.pendown()
    t.goto(x, y + 40)

window_cross(-80, 20)
window_cross(40, 20)

# sun
t.penup()
t.goto(150, 150)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(30)
t.end_fill()

t.hideturtle()
turtle.done()