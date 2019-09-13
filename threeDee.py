from graphics import *
from math import *

wx = 1000
wy = 800

scale = min(wx, wy)/20

cx = wx * 0.5
cy = wy * 0.5

uxx = scale
uxy = 0

uyx = -scale*0.4
uyy = scale*0.3

uzx = 0
uzy = -scale


win = GraphWin('Evil', wx, wy, False)


def project(x, y, z):
    return Point(cx + x * uxx + y * uyx + z * uzx, cy + x * uxy + y * uyy + z * uzy)


# Line(project(-10, 0, 0), project(10, 0, 0)).draw(win)
# Line(project(0, -10, 0), project(0, 10, 0)).draw(win)
# Line(project(0, 0, -10), project(0, 0, 10)).draw(win)


count = 20
step = 10.0/count


def foo(x, y):
#    return (x*x - y*y) * 0.1
    dist = sqrt(x * x + y * y)
    return 5 * (sin(dist) / dist if dist != 0 else 1)

for yInt in range(-count, count):
    for xInt in range(-count, count):
        x1 = xInt * step
        y1 = yInt * step
        x2 = (xInt + 1) * step
        y2 = (yInt + 1) * step

        za = foo(x1, y1)
        zb = foo(x1, y2)
        zc = foo(x2, y1)

        p11 = project(x1, y1, za)
        p12 = project(x1, y2, zb)
        p21 = project(x2, y1, zc)

        Line(p11, p12).draw(win)
        Line(p11, p21).draw(win)

        if xInt == count - 1 or yInt == count - 1:
            zd = foo(x2, y2)
            p22 = project(x2, y2, zd)
            if xInt == count - 1:
                Line(p21, p22).draw(win)
            if yInt == count - 1:
                Line(p12, p22).draw(win)


win.update()


win.getMouse()
win.close()
