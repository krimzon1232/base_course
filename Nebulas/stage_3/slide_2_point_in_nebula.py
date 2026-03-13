import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import shapely.geometry as geom

img = plt.imread("Barnard_68_nebula.jpg")
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 640, 0, 640])


def circle(R, x0, y0, starst, stop, step):
    t=np.arange(starst, stop, step)
    x = x0 + R * np.cos(t)
    y = y0 + R * np.sin(t)
    return x, y


x = np.array([230, 240])
y = np.array([420, 290])

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

curve_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])

polygon = geom.Polygon(curve_coords)
points_numper_per_side = 100
x_pictures_limits = [0, 640]
y_pictures_limits = [0, 640]

for x_point_coord in np.linspace(*x_pictures_limits, points_numper_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_numper_per_side):
        p = geom.Point(x_point_coord, y_point_coord)
        if p.within(polygon):
            plt.plot(x_point_coord, y_point_coord, 'go', ms=0.7)

plt.plot(x, y, 'bo')
plt.plot(spline_curve[0], spline_curve[1], 'g')

plt.savefig('slide_2_spline_nebula.png')