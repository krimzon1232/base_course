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
            points_coords.append(x_point_coord)
            points_coords.append(y_point_coord)

x_p = np.array(points_coords[0::2])
y_p = np.array(points_coords[1::2])


def concentrarion(x, y, x0=0, y0=0, dec_rate=[5, 5]):  
        return np.exp(- dec_rate[0] * (x - x0)**2 - dec_rate[1] * (y - y0)**2)


def points_generator(x0=0, y0=0, points_numper=5000, intensity=[5, 5]):
    points_counter = 0

    while points_counter < points_numper:
        x_point_coord = np.random.uniform(-0.5, 2)
        y_point_coord = np.random.uniform(-1, 1)
        
        p = geom.Point(x_point_coord, y_point_coord)
        w = np.random.uniform(0.0, 1.0)

        if w <= density(x_point_coord, y_point_coord, x0, y0, intensity) and p.within(polygon):
            points_coords.append(x_point_coord)
            points_coords.append(y_point_coord)
            points_counter += 1


points_coords = []
points_generator(0.8, 0, 5000, [5, 5])
points_generator(0.8, 0.8, 5000, [5, 5])

x_p = np.array(points_coords[0::2])
y_p = np.array(points_coords[1::2]) 

plt.plot(x_p, y_p, 'go', ms=0.5)
plt.axis('equal')
plt.savefig('slide_1_concentration_and_density.png')
plt.close()

