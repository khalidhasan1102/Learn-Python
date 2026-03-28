import turtle
import time
import random

# 1. Screen setup
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("1 Minute Turtle Art")

# 2. Turtle setup
t = turtle.Turtle()
t.pensize(3)
t.speed(5)

# 3. Start timer
start_time = time.time()
duration = 60  # seconds

# 4. Draw continuously for 1 minute
while time.time() - start_time < duration:
    # Random color
    t.color(random.choice(["red", "green", "blue", "orange", "purple"]))
    
    # Draw a square
    for _ in range(4):
        t.forward(50)
        t.right(90)
    
    # Rotate a bit for next square
    t.right(random.randint(10, 45))

# 5. Finish
turtle.done()