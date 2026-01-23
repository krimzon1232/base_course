import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], "-", lw=5)

x, y = [], []
frames_interval = np.linspace(0, 2*np.pi, 1000)

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)

def update(frame):
    x.append(frame)
    y.append(np.sin(frame))
    
    anim_object.set_data(x, y)
    
    return anim_object


ani = FuncAnimation(
                    fig,
                    update,
                    frames=frames_interval,
                    interval=1/24*1000
                    )
ani.save("ani.gif", writer="pillow")