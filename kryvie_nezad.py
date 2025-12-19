import matplotlib.pyplot as plt
import numpy as np

def okrugnost(R = 10):
    x = np.arange(-2*R, 2*R, 0.01)
    y = np.arange(-2*R, 2*R, 0.01)
    
    X, Y = np.meshgrid(x, y)
    
    fxy = X**2 + Y**2 - R**2
    
    plt.contour(X, Y, fxy, levels=[0])
    
    plt.axis("equal")
    plt.savefig("img.jpg")
    
okrugnost()