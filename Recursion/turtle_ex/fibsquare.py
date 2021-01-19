import turtle


def square(t, i_size):
    if i_size > 1:
        for i in range(4):
            t.fd(i_size)
            t.rt(90)
        t.lt(90)
        square(t, i_size / 2)


if __name__ == '__main__':
    t = turtle.Turtle()
    sc = turtle.Screen()
    square(t, 100)
    sc.exitonclick()

