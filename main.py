from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def rotate_left():
    turtle.left(10)


def rotate_right():
    turtle.right(10)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(rotate_left, "a")
screen.onkey(rotate_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
