import turtle

# Setup
t = turtle.Turtle()
turtle.bgcolor("#f9f5f0")   # soft background
t.speed(10)

# Colors to cycle through
colors = ["#ff6f61", "#ffcc00", "#6c63ff", "#00b894", "#fd79a8"]

# Draw a flower/star pattern
for i in range(36):  # 36 petals
    t.color(colors[i % len(colors)])
    t.circle(100)    # draw circle as a petal
    t.right(10)      # rotate slightly

# Draw a cute center
t.penup()
t.goto(0, -50)
t.pendown()
t.color("#3a3a3a")
t.begin_fill()
t.circle(50)
t.end_fill()

t.hideturtle()
turtle.done()
