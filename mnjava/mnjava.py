import tkinter as tk
from turtle import RawTurtle, TurtleScreen
# This game uses Steve
# Create the main window
root = tk.Tk()
root.title("Green Terrain")

# Create a canvas and add it to the window
canvas = tk.Canvas(root, width=800, height=600, bg="green")
canvas.pack()

# Create a turtle screen and add it to the canvas
screen = TurtleScreen(canvas)
screen.setworldcoordinates(0, 0, 800, 600)

# Create a turtle
turtle = RawTurtle(screen)
turtle.speed(0)
turtle.shape("square")
turtle.shapesize(1)
turtle.color("blue")

# Draw Steve's head
head = RawTurtle(screen)
head.speed(0)
head.shape("circle")
head.shapesize(0.5)
head.color("blue")
head.penup()
head.goto(turtle.xcor(), turtle.ycor() + 20)

# Draw Steve's arms
left_arm = RawTurtle(screen)
left_arm.speed(0)
left_arm.shape("square")
left_arm.shapesize(0.2, 1)
left_arm.color("blue")
left_arm.penup()
left_arm.goto(turtle.xcor() - 10, turtle.ycor() + 10)

right_arm = RawTurtle(screen)
right_arm.speed(0)
right_arm.shape("square")
right_arm.shapesize(0.2, 1)
right_arm.color("blue")
right_arm.penup()
right_arm.goto(turtle.xcor() + 10, turtle.ycor() + 10)

# Draw Steve's legs
left_leg = RawTurtle(screen)
left_leg.speed(0)
left_leg.shape("square")
left_leg.shapesize(0.2, 1)
left_leg.color("blue")
left_leg.penup()
left_leg.goto(turtle.xcor() - 5, turtle.ycor() - 20)

right_leg = RawTurtle(screen)
right_leg.speed(0)
right_leg.shape("square")
right_leg.shapesize(0.2, 1)
right_leg.color("blue")
right_leg.penup()
right_leg.goto(turtle.xcor() + 5, turtle.ycor() - 20)

# Function to move the turtle
def move_turtle(dx, dy):
    turtle.goto(turtle.xcor() + dx, turtle.ycor() + dy)
    head.goto(head.xcor() + dx, head.ycor() + dy)
    left_arm.goto(left_arm.xcor() + dx, left_arm.ycor() + dy)
    right_arm.goto(right_arm.xcor() + dx, right_arm.ycor() + dy)
    left_leg.goto(left_leg.xcor() + dx, left_leg.ycor() + dy)
    right_leg.goto(right_leg.xcor() + dx, right_leg.ycor() + dy)

# Function to handle key presses
def handle_key_press(event):
    if event.keysym == "w":
        move_turtle(0, 1)
    elif event.keysym == "a":
        move_turtle(-1, 0)
    elif event.keysym == "s":
        move_turtle(0, -1)
    elif event.keysym == "d":
        move_turtle(1, 0)

# Bind the key press event to the handle_key_press function
root.bind("<Key>", handle_key_press)

# Start the main loop
root.mainloop()