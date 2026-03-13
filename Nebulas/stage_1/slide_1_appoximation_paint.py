import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = [0, 0, 10, 10, 0]
y = [0, 3, 3, 0, 0]
ax.plot(x, y, '-', linewidth=2, color='k')

x = [4, 4, 6, 6, 4]
y = [0, 2, 2, 0, 0]
ax.plot(x, y, '-', linewidth=2, color='k')

x = [0, 5, 10]
y = [3, 5, 3]
ax.plot(x, y, '-', linewidth=2, color='k')

t = np.linspace(0, np.pi*2, 40)
x = 1.5 + np.cos(t)
y = 1.8 + np.sin(t)
ax.plot(x, y, '-', linewidth=2, color='k')

t = np.linspace(0, np.pi*2, 40)
x = 8.5 + 0.5*np.cos(t)
y = 1.3 + np.sin(t)
ax.plot(x, y, '-', linewidth=2, color='k')

# x = [5, 6, 7]
# y = [7, 9, 7]
# ax.plot(x, y, '-', linewidth=2, color='k')

# t = np.linspace(2*np.pi, np.pi, 20)
# x = 4 + 3 * np.cos(t)
# y = 7 + 5 * np.sin(t)
# ax.plot(x, y, '-', linewidth=2, color='k')

# x = [5, 6, 7]
# y = [7, 9, 7]
# ax.plot(x, y, '-', linewidth=2, color='k')

plt.axis('equal')
plt.savefig('slide_1_appoximation_paint.png')