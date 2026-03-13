import numpy as np
from scipy import interpolate
import shapely.geometry as geom
import matplotlib.pyplot as plt


phi = np.linspace(0, 2*np.pi, 40)
r = 0.5 + np.cos(phi)
x = r * np.cos(phi)
y = r * np.sin(phi)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

curve_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])

polygon = geom.Polygon(curve_coords)
points_numper= 5000
x_pictures_limits = [-0.5, 2]
y_pictures_limits = [-1, 1]


def density(x, y, x0=0, y0=0, intensity=[5, 5]):  
        return np.exp(- intensity[0] * (x - x0)**2 - intensity[1] * (y - y0)**2)


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

# Коэффициент отображения координат в расстояние [0, 1] (максимальное расстояние в координатах)
normal_dimention = 2.5 
box_size =  1

# Центрирование объекта
x_p = np.array(points_coords[0::2]) / normal_dimention + box_size / 2
y_p = np.array(points_coords[1::2]) / normal_dimention + box_size / 2

plt.plot(x_p, y_p, 'go', ms=0.5)
plt.axis('equal')
plt.savefig('slide_2_normalize_size.png')
plt.close()

# Учет реальных размеров объекта в парсеках
real_size = 7.66503 # Размер туманности Ориона в парсеках

box_size = real_size * box_size
x_p = x_p * real_size
y_p = y_p * real_size

plt.plot(x_p, y_p, 'go', ms=0.5)
plt.axis('equal')
plt.savefig('slide_2_normalize_size.png')
plt.close()

