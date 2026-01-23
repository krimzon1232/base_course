import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def circle_mov(R, angle_vel, time):
    
    alpha = angle_vel * np.pi / 180 * time
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y

fig, ax = plt.subplots()
obj, = plt.plot([], [], "o", color="r", label="ball", lw = 6)
obj_line, = plt.plot([], [], "-", color="g", label="ball", lw = 2)


frames = 360
coords = np.zeros((frames, 2))

def animate(i):
    coords[i] = circle_mov(R=2, angle_vel=1, time=i)
    obj.set_data([coords[i][0]], [coords[i][1]])
    obj_line.set_data(coords[:i, 0], coords[:i, 1])
    return obj, obj_line

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