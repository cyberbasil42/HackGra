from time import *
from codes import *
import turtle as t


def main():
    t.title("Hacker")
    t.setup(width=900, height=600)
    t.bgcolor('black')
    t.pencolor('white')
    t.speed(3)
    line()
    t.pencolor('red')
    h()
    a()
    c()
    k()
    E()
    r()
    sleep(1)
    pup()
    t.speed(1)
    t.shapesize(4)
    t.setposition(250, -130)
    t.right(180)
    t.write("By BASIL")
    sleep(5)
    t.reset()
    main()


main()
