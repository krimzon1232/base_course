import matplotlib.pyplot as plt
import numpy as np

def circle(R=3):
    alpha = np.arange(-2*np.pi, 2*np.pi, 0.01) #Параметр
    
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    
    plt.plot(x, y, ls="--", lw=3)
    plt.axis('equal')
    plt.savefig("img.jpg")
    
if __name__ == '__main__':
    circle()
    
    