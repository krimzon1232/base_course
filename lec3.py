import lec1_phisconst as ph
import numpy as np

#x0 = 0 y0 = 0
vx = 10
vy = 5

inp = [["t", "x", "y"]]

for t in range(5):
    x = vx*t
    y = vy*t - ph.g*t**2/2
    inp.append([t, x, y])

print(np.array(inp))less 3 #aboba