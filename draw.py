from display import *

def draw_line(x0, y0, x1, y1, screen, color ):
	x0 = int(x0)
	x1 = int(x1)
	y0 = int(y0)
	y1 = int(y1)
    dy = y1 - y0
    dx = x1 - x0
    ##print("x0: {} y0: {} x1: {} y1: {} dx: {} dy: {}".format(x0, y0, x1, y1, dx, dy))
    if (x0 >= 0 and y0 >= 0 and x1 >= 0 and y1 >= 0 and dx > dy 
    or x0 <= 0 and y0 <= 0 and x1 <= 0 and y1 <= 0 and dx > dy): 
        draw_line_oct1(x0, y0, x1, y1, screen, color)
        return
    if (x0 >= 0 and y0 >= 0 and x1 >= 0 and y1 >= 0 and dx < dy
    or x0 <= 0 and y0 <= 0 and x1 <= 0 and y1 <= 0 and dx < dy):
        draw_line_oct2(x0, y0, x1, y1, screen, color)
        return
    if (x0 > 0 and y0 > 0 and x1 > 0 and y1 > 0 and dx < dy):
        return
    #if x0 > 0 and y0 > 0 and x1 > 0 and y1 > 0 and dx < dy:
    #if x0 > 0 and y0 > 0 and x1 > 0 and y1 > 0 and dx < dy:
    #if x0 > 0 and y0 > 0 and x1 > 0 and y1 > 0 and dx < dy:

def draw_line_oct1(x0, y0, x1, y1, screen, color):
    b = -x1 + x0
    a = y1 - y0
    D = 2*b + a
    y = y0
    for x in range(x0, x1):
        plot(screen, color, x, y)
        if D > 0:
               y += 1
               D -= 2*b
        D += 2*a

def draw_line_oct2(x0, y0, x1, y1, screen, color):
    b = -x1 + x0
    a = y1 - y0
    D = a + 2*b
    x = x0
    y0 = int(y0)
    y1 = int(y1)
    for y in range(y0, y1):
    	plot(screen, color, x, y)
    	if D < 0:
    		x += 1
    		D += 2*a
    	D += 2*b
    
    # x = x0
    # y = y0
    # a = y1 - y0
    # b = -(x1 - x0)
    # d = a + .5*b
    # a = 2*a
    # b = 2*b
    # while (x <= x1):
    #     plot(screen,"#0000FF", x, y)
    #     if (d > 0):
    #         y = y + 1
    #         d = d + b
    #     x = x + 1
    #     d = d + a
