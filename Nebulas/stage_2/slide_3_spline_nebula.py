import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

img = plt.imread("Barnard_68_nebula.jpg")
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 640, 0, 640])


def circle(R, x0, y0, starst, stop, step):
    t=np.arange(starst, stop, step)
    x = x0 + R * np.cos(t)
    y = y0 + R * np.sin(t)
    return x, y


x = np.array([230, 240]) # Очень важно, чтобы точки не повторялись 
y = np.array([420, 290]) # иначе будет ошибка интерполяции

coords = circle(35, 180, 210, np.pi/2+np.pi/4, 3*np.pi/2, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

x = np.append(x, [180, 280])
y = np.append(y,  [175, 220])

coords = circle(150, 300, 370, np.pi+np.pi/2.15, 2*np.pi-np.pi/6, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(120, 320, 345, 2*np.pi-np.pi/6, 2*np.pi+np.pi/1.27, 0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.plot(x, y, 'bo')
plt.plot(spline_curve[0], spline_curve[1], 'g')

plt.savefig('slide_2_spline_nebula.png')