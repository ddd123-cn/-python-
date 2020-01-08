# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:55:56 2018

@author: ejiandi
"""
import turtle
import time
turtle.speed(0)
turtle.pensize(2)
turtle.setup(600,400,0,0)
turtle.penup()

'''
for x in range(100):
    turtle.forward(2*x)
    turtle.left(90)
time.sleep(3)
'''
'''
P0=[]
P1=[]
P2=[]
'''
n = int(input ("几层的塔?"))
distribute=[[],[],[]]
for i in range(n):
    distribute[0].append(i)
#distribute = [P0,P1,P2]
step = 0

def draw_rectangle(width, high):
    turtle.seth(0)
    turtle.pendown()
    turtle.fd(width)
    turtle.left(90)
    turtle.fd(high)
    turtle.left(90)
    turtle.fd(width)
    turtle.left(90)
    turtle.fd(high)
    turtle.penup()
        
def draw_disc(pillar,layer,Num):
    turtle.pensize(2)
    turtle.setpos(100*pillar-100-45+5*Num,-100+32*layer)
    draw_rectangle(90-10*Num, 30)

def draw_tower(n):
    turtle.pensize(5)
    turtle.pencolor("blue")
    turtle.setpos(-105,-100)
    draw_rectangle(10,150)
    turtle.setpos(-5,-100)
    draw_rectangle(10,150)
    turtle.setpos(95,-100)
    draw_rectangle(10,150)
    turtle.pencolor("red")
    for i in range(n):
        draw_disc(0,i,i)

def move(pillar1, pillar2):
    #global distribute
    global step
    step = step +1
    print ("步骤",step,":    从柱子",pillar1+1,"挪到柱子",pillar2+1)
    objnum = distribute[pillar1][-1]
    turtle.pencolor("white")
    draw_disc(pillar1,len(distribute[pillar1])-1,objnum)    
    time.sleep(0.1)
    turtle.pencolor("pink")
    draw_disc((pillar1+pillar2)/2,6,objnum)
    time.sleep(0.5)
    turtle.pencolor("white")
    draw_disc((pillar1+pillar2)/2,6,objnum)
    time.sleep(0.1)
    turtle.pencolor("red")
    draw_disc(pillar2,len(distribute[pillar2]),objnum)
    time.sleep(0.5)
    for i in range(3):
        if i == pillar1:
            distribute[i].remove(objnum)
        if i == pillar2:
            distribute[i].append(objnum)

def moove(n, a, b, c):
    if n == 1:
        move(a, c)
    else:
        moove(n-1,a,c,b)
        moove(1,a,b,c)
        moove(n-1,b,a,c)
    
draw_tower(n)
moove(n,0,1,2)
print("一共用了",step,"步")
turtle.penup()
turtle.goto(-100,-150)
step = str(step) + ' steps in total.'
turtle.write(step,True,font=("Arial", 30, "normal"))  
                 #这个True表示pen是不是跟着一块儿走到文字的后面,默认是False
turtle.penup()
turtle.done()
#turtle.bye()


