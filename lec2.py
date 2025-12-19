import matplotlib.pyplot as plt
import numpy as np

def gypr(k = 1, xs = 10, N = 1000):
    x = np.linspace(-xs, xs, N)
    y = k/x
    
    plt.plot(x, y)
    plt.savefig("lec2.jpg")

gypr(5, 10, 1000)