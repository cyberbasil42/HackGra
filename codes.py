from const import *
import turtle as t


def line():
    t.pensize(3)
    pup()
    t.setposition(-400, 90)
    pdo()
    t.setposition(380, 90)
    t.pensize(5)

#todo x values
hx = 370
ax = 218
cx = 30
kx = 90
Ex = 170
rx = 270
def h():
    pup()
    t.setposition(-hx, 190)
    r90()
    pdo()
    f(100)
    l90()
    f(38)
    l90()
    f(35)
    r90()
    f(45)
    r90()
    f(35)
    l90()
    f(38)
    l90()
    f(100)
    l90()
    f(38)
    l90()
    f(35)
    r90()
    f(45)
    r90()
    f(35)
    l90()
    f(38)


def a():
    pup()
    t.setposition(-ax, 90)
    pdo()
    t.right(120)
    f(120)
    t.right(113)
    f(132)
    t.right(130)
    f(33)

    t.right(45)
    f(30)
    t.left(48)

    f(40)
    t.left(52)
    f(28)
    t.right(50)
    f(27)
    #todo triangle
    pup()
    t.setposition(-(ax-47), 125)
    pdo()
    t.right(182)
    f(36)
    t.left(120)
    f(40)
    t.left(124)
    f(38)


def c():
    pup()
    t.setposition(cx, 190)
    t.right(64)
    pdo()
    f(80)
    l90()
    f(100)
    l90()
    f(80)
    l90()
    f(25)
    l90()
    f(50)
    r90()
    f(50)
    r90()
    f(50)
    l90()
    f(25)


def k():
    pup()
    t.setposition(kx, 190)
    pdo()
    l90()
    f(27)
    l90()
    pdo()
    f(100)
    l90()
    f(25)
    l90()
    f(30)
    t.right(130)
    f(43)
    t.left(40)
    f(18)
    t.left(134.8)
    f(60)
    t.right(84)
    f(75)
    t.left(130)
    f(22)
    t.left(53)
    f(55)
    t.right(144)
    f(39)


def E():
    pup()
    t.setposition(Ex, 190)
    pdo()
    t.right(180)
    f(100)
    l90()
    f(68)
    l90()
    f(20)
    l90()
    f(40)
    r90()
    f(20)
    r90()
    f(40)
    l90()
    f(20)
    l90()
    f(40)
    r90()
    f(20)
    r90()
    f(40)
    l90()
    f(20)
    l90()
    f(68)


def r():
    pup()
    t.setposition(rx, 190)
    pdo()
    l90()
    f(100)
    pup()
    t.right(180)
    f(100)
    pdo()
    r90()
    f(70)
    r90()
    f(40)
    r90()
    f(30)
    t.left(120)
    f(69)
    t.right(120)
    f(30)
    t.right(60)
    f(45)
    t.left(150)
    f(40)
    r90()
    f(20)
    #todo : Rectangle
    pup()
    t.setposition(rx+20, 172)
    pdo()
    l = 10
    b = 20
    l90()
    f(l)
    l90()
    f(b)
    l90()
    f(l)
    l90()
    f(b)
    l90()










































