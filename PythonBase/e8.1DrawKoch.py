import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        # for angle in [0, 60, -120, 60]:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            # turtle.right(angle)
            koch(size/3, n-1)


def main():
    turtle.setup(600, 600)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200, 100)
    # turtle.colormode(255)
    turtle.pencolor((238,130,238))
    turtle.pendown()
    turtle.pensize(2)
    level = 5
    koch(600, level)
    turtle.right(120)
    koch(600, level)
    turtle.right(120)
    koch(600, level)
    # turtle.hideturtle()
    turtle.done()


main()
