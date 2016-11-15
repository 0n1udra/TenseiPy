from turtle import *


def sqr(tF=100, tL=90):  # this prints a square with default paremieters
    print("Making square... ")
    for i in range(4):  # loops four time, to build the four sides
        forward(tF)
        left(tL)


def tri(tF=100, tL=120):  # makes a triangle
    print("Making triangle... ")
    begin_fill()

    for i in range(3):
        forward(tF)
        left(tL)
    end_fill()

def house():  # makes a house
    print("Making house... ")
    sqr()
    left(90)
    forward(100)
    right(90)
    tri()

def draw_Tally():
    tF = 20
    tL = 90
    left(tL)
    forward(tF)
    backward(tF)
    right(tL)

def pickup():
    for i in range(4):
        pu()
        forward(5)
        pd()
        draw_Tally()

def divide():
    amount = int(input("Input number to tally > "))
    x = amount // 5
    for i in range(x):
        pickup()


stuff = [sqr, tri, house, divide]

def Main():
    for i in range(len(stuff)):
        x = str(stuff[i]).split(" ")  # only prints the function name, without this, it prints memory location and type()
        print(str(i) + ")", x[1])
    inp = int(input("choose > "))
    stuff[inp]()

def Main2():
    color('blue', 'purple')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

if __name__ == '__main__':
    Main()
    input("")
