from graphics import *
from random import *

# h = [5,3,2,1,4,4,7,1,3,8]
# count = len(h)

h = []
count = 100


def landscape(i, j):
    mid = (i + j) // 2
    if mid > i:
        h[mid] = (h[i] + h[j]) // 2 + round(gauss(0, j - i))
        if h[mid] < 0:
            h[mid] = 0
        if (h[mid]) >= count:
            h[mid] = count - 1
        landscape(i, mid)
        landscape(mid, j)


for x in range(0, 100):
    h.append(0)
h[0] = h[-1] = len(h) // 2
landscape(0, len(h) - 1)

scale = 5
win = GraphWin('rain', count * scale, count * scale)


def rect(left, bottom, right, top, color):
    re = Rectangle(Point(left * scale, (count - top - 1) * scale), Point((right + 1) * scale, (count - bottom) * scale))
    re.setWidth(0)
    re.setFill(color)
    re.draw(win)


for x in range(0, len(h)):
    rect(x, 0, x, h[x], 'black')

win.getMouse()

drops = []

area1 = 0

for x in range(0, len(h) - 1):
    if h[x + 1] < h[x]:
        drops.append(x)
    elif h[x + 1] > h[x]:
        bottom = h[x] + 1
        while len(drops) > 0:
            dropHigher = h[drops[-1]] > h[x + 1]
            top = h[x + 1] if dropHigher else h[drops[-1]]
            rect(drops[-1] + 1, bottom, x, top, 'blue')
            area1 += (x - drops[-1]) * (top - bottom + 1)
            bottom = top + 1
            if dropHigher:
                break
            else:
                drops.pop()

print("area1: ", area1)
win.getMouse()

print("simpler approach")

area2 = 0
maxOnLeft = []
currentMax = h[0]
for x in range(0, len(h)):
    if h[x] > currentMax:
        currentMax = h[x]
    maxOnLeft.append(currentMax)
currentMax = h[-1]
for x in range(len(h) - 2, -1, -1):
    if h[x] < currentMax:
        if h[x] < maxOnLeft[x]:
            top = min(currentMax, maxOnLeft[x])
            rect(x, h[x] + 1, x, top, "red")
            area2 += top - h[x]
    else:
        currentMax = h[x]

print("area2: ", area2)

win.getMouse()
win.close()
