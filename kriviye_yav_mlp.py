import matplotlib.pyplot as plt
import numpy as np

def parabola(a = 1, b = 1, c = 0):
    x = np.arange(-15, 15, 0.01)
    y = a*x**2 + b*x + c
    

    plt.plot(x, y, label="Parabola")
    plt.legend()
    plt.xlabel("x")
    plt.xlabel("y")
    plt.savefig("img.jpg")
    
if __name__ == "__main__":
    parabola()




