import turtle

def tree(t, l, w, ang):
    if l > 5:
        if l-10 < 5:
            t.color('green')
        t.width(w)
        t.rt(20)
        t.fd(l)
        tree(t,l-10,w-1,ang)
        t.bk(l)
        t.lt(40)
        t.fd(l)
        tree(t,l-10,w-1,ang)
        t.bk(l)
        t.rt(20)
        t.width(w+1)
        t.color('black')


if __name__ == '__main__':
    kolyan = turtle.Turtle()
    kolyan.speed(30)
    tree(kolyan,60,6,30)
