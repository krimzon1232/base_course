import numpy as np
import matplotlib.pyplot as plt

plt.arrow(0, 0, 4, 4, width=0.02)
plt.savefig("vector.png")
plt.close()

x, y = np.meshgrid(np.linspace(-5, 5, 10), np.linspace(-5, 5, 10))

u = 1
v = -1
plt.quiver(x, y, u, v)
plt.title('Векторное поле скоростей, v = {-1, 1} м/с')
plt.ylabel('Координата Х, м')
plt.xlabel('Координата Y, м')
plt.savefig("vector_field_1.png")
plt.close()

u = x / np.sqrt(x**2 + y**2)
v = y / np.sqrt(x**2 + y**2)
plt.quiver(x, y, u, v, angles='xy', scale_units='xy')
plt.title('Векторное поле скоростей, v = {y/r, x/r} м/с')
plt.ylabel('Координата Х, м')
plt.xlabel('Координата Y, м')
plt.savefig("vector_field_2.png")
plt.close()

u = -y / np.sqrt(x**2 + y**2)
v = x / np.sqrt(x**2 + y**2)
plt.quiver(x, y, u, v, angles='xy', scale_units='xy')
plt.title('Векторное поле скоростей, v = {-y/r, x/r} м/с')
plt.ylabel('Координата Х, м')
plt.xlabel('Координата Y, м')
plt.savefig("vector_field_3.png")
plt.close()

u = -y / np.sqrt(x**2 + y**2) + y
v = x / np.sqrt(x**2 + y**2)
plt.quiver(x, y, u, v, angles='xy', scale_units='xy')
plt.title('Векторное поле скоростей, v = {x/r, -y/r} м/с')
plt.ylabel('Координата Х, м')
plt.xlabel('Координата Y, м')
plt.savefig("vector_field_4.png")
plt.close()