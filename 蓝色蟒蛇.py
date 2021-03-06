# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 19:53:58 2017

@author: Richard祥
"""

import turtle


def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+5,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0)
    pythonsize = 15
    turtle.speed(12)
    turtle.pensize(pythonsize)
    turtle.pencolor('blue')
    turtle.seth(-40)
    drawSnake(40,80,4,pythonsize/2)
    turtle.done()
main()    
