import turtle

# Create the turtle screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create the turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.pensize(5)

# Draw a square
for i in range(4):
    t.forward(150)
    t.right(90)

# Keep the window open
turtle.done()