import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def circle_mov(R, vx0, vy0, time):
    
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 360, 0.1)
    x = x0 + R * np.cos(alpha)
    y = y0 + R * np.sin(alpha)
    return x, y

fig, ax = plt.subplots()
obj, = plt.plot([], [], "o", color="r", label="ball", lw = 6)
obj_line, = plt.plot([], [], ".", color="g", label="ball", lw = 2)


frames = 100
coords = np.zeros((frames, 2))

def animate(i):
    obj.set_data(circle_mov(R=4*i/2**2, vx0=0, vy0=0, time=i))
    return obj

edge = 3
plt.axis("equal")
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

    
ani = FuncAnimation(
                    fig,
                    animate,
                    frames=frames,
                    interval=30
                    )
ani.save("ani.gif", writer="pillow")