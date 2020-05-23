import turtle
# import scipy.integrate


def koch(size, n):
    if n == 0:
        m.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)


def main():
    turtle.setup(1000, 1000)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 2
    koch(600, level)
    # turtle.right(120)
    # koch(600, level)
    # turtle.right(120)
    # koch(600, level)
    # turtle.hideturtle()
    turtle.done()


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)


main()
