import matplotlib.pyplot as plt
import numpy as np
import random

fig, ax = plt.subplots()

N = 10000
x, y = np.zeros(N), np.zeros(N)

for i in range(N):
    x[i] = random.uniform(-1, 1)
    y[i] = random.uniform(-1, 1)

def bell_function(x, y, intensity=1, dec_rate=[0.5, 0.5]):
    scalar_func = intensity * np.exp(- dec_rate[0]*x**2 - dec_rate[1]*y**2) 
    return scalar_func

fig, ax = plt.subplots()
sc_plot = ax.scatter(x, y, c=bell_function(x, y, 5, [9.0, 0.5]))
ax.set_ylabel('Координата Х, м')
ax.set_xlabel('Координата Y, м')

cbar = fig.colorbar(sc_plot)
cbar.set_label("Интенсивность cкалярного поля функции Белла")

plt.savefig('scalar_field_bell_func.png')



# scalar_field = 50 * np.cos(np.sqrt(x**2 + y**2))



# sc_plot = ax.scatter(x, y, c=scalar_field)
# ax.set_ylabel('Координата Х, м')
# ax.set_xlabel('Координата Y, м')

# cbar = fig.colorbar(sc_plot)
# cbar.set_label("Скалярное поле температуры, °С")

# plt.savefig('scalar_field.png')