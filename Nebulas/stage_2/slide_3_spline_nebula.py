import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

img = plt.imread("image.png")
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 640, 0, 640])


def circle(R, x0, y0, starst, stop, step):
    t=np.arange(starst, stop, step)
    x = x0 + R * np.cos(t)
    y = y0 + R * np.sin(t)
    return x, y


x = np.array([235, 380]) # Очень важно, чтобы точки не повторялись 
y = np.array([300, 625]) # иначе будет ошибка интерполяции

coords = circle(125, 380, 500, np.pi/2 - np.pi/16, 0, -0.1)
x = np.append(x, coords[0])
y = np.append(y, coords[1])


coords = circle(75, 625-125-135, 400, 0, -np.pi / 2 + np.pi / 16, -0.2)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

coords = circle(75, 625-125-190, 400-95, 0, -np.pi, -0.2)
x = np.append(x, coords[0])
y = np.append(y, coords[1])

x = np.append(x, 235)
y = np.append(y, 300)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.plot(x, y, 'bo')
plt.plot(spline_curve[0], spline_curve[1], 'g')

plt.savefig('slide_2_spline_nebula.png')