import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = [1, 2, 3]
y = [7, 9, 7]
ax.plot(x, y, '-', linewidth=2, color='k')

t = np.linspace(np.pi/2+np.pi/6, np.pi/2-np.pi/6, 20)
x = 4 + 2 * np.cos(t)
y = 5.25 + 2 * np.sin(t)
ax.plot(x, y, '-', linewidth=2, color='k')

x = [5, 6, 7]
y = [7, 9, 7]
ax.plot(x, y, '-', linewidth=2, color='k')

t = np.linspace(2*np.pi, np.pi, 20)
x = 4 + 3 * np.cos(t)
y = 7 + 5 * np.sin(t)
ax.plot(x, y, '-', linewidth=2, color='k')

x = [5, 6, 7]
y = [7, 9, 7]
ax.plot(x, y, '-', linewidth=2, color='k')

plt.axis('equal')
plt.savefig('slide_1_appoximation_paint.png')