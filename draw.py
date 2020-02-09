#!/usr/bin/env python
from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
	if (x1 < x0):
		x1, x0 = x0, x1
		y1, y0 = y0, y1
	if(x1 == x0):
		slope = 5
		for y in range(y0, y1+1):
			screen[int(y)][int(x0)] = color
	elif(y0 == y1):
		slope = 0
	else:
		slope = (y1-y0)/(x1-x0)

	if(slope > 0):
		if(slope <= 1):
			draw_octant1( x0, y0, x1, y1, screen, color)
		else:
			draw_octant2( x0, y0, x1, y1, screen, color)
	else:
		if(slope >= -1):
			draw_octant8( x0, y0, x1, y1, screen, color)
		else:
			draw_octant7( x0, y0, x1, y1, screen, color)

def draw_octant1( x0, y0, x1, y1, screen, color ):
    a = 2*(y1-y0)
    b = (x0-x1)
    d = a + b
    while( x0 <= x1):
        plot(screen, color, x0, y0)
        if(d > 0):
            y0 = y0+1
            d = d + 2*b
        x0 = x0+1
        d = d + a

def draw_octant2(x0, y0, x1, y1, screen, color):
    a = (y1-y0)
    b = 2*(x0-x1)
    d = a + b
    while (y0 <= y1):
        plot(screen, color, x0, y0)
        if(d<0):
            x0 = x0 + 1
            d = d + 2*a
        y0 = y0 + 1
        d = d + b

def draw_octant7(x0, y0, x1, y1, screen, color):
    a = (y1-y0)
    b = 2*(x0-x1)
    d = a - b
    while( y0 >= y1):
        plot(screen, color, x0, y0)
        if(d > 0):
            x0 = x0+1
            d = d + 2*a
        y0 = y0-1
        d = d - b

def draw_octant8(x0, y0, x1, y1, screen, color):
    a = 2*(y1-y0)
    b = (x0-x1)
    d = a - b
    while( x0 <= x1):
        plot(screen, color, x0, y0)
        if(d < 0):
            y0 = y0-1
            d = d - 2*b
        x0 = x0+1
        d = d + a
