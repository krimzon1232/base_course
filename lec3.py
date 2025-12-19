import numpy as np
from matplotlib import pyplot as plt
from math import pi
def chettam(rx = 1, ry = 1, N=1000):
    t = np.linspace(0, 2*pi, N)
    plt.plot(rx*np.cos(t), ry*np.sin(t))
    plt.axis("equal")
    plt.savefig("lec3.jpg")
chettam(5, 30)