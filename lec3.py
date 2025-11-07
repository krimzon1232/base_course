import lec1
import numpy as np
g = lec1.g
x0=12
y0 = 5
v0x = 4
v0y = 8
list = []
for t in np.arange(0, 5.5, 0.5):
    x = x0 + v0x * t
    y = y0 + v0y*t - (g*t**2 / 2)
    list.append([t, x, y])
print(np.array(list))