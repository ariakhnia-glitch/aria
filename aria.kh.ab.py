import turtle
t=turtle.turtle

aria = turtle.screen()
aria.title("کنترل ترتل با کيبورد")


def move_forward():
    t.forward(30)


def move_backward():
    t.backward(30)


def turn_left():
    t.left(30)


def turn_right():
    t.right(30)

aria.listen()
aria.onkeypress(move_forward, "Up")
aria.onkeypress(move_backward, "down")
aria.onkeypress(turn_left, "left")
aria.onkeypress(turn_right, "right")


aria.listen()
