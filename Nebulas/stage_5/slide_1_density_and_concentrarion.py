import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import shapely.geometry as geom

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
points_numper_per_side = 100
x_pictures_limits = [-0.5, 2]
y_pictures_limits = [-1, 1]

points_coords = []

for x_point_coord in np.linspace(*x_pictures_limits, points_numper_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_numper_per_side):
        p = geom.Point(x_point_coord, y_point_coord)
        if p.within(polygon):
            points_coords.append(x_point_coord)
            points_coords.append(y_point_coord)

x_p = np.array(points_coords[0::2]) + 0.5 # Центрирование объекта на графике по оси Х
y_p = np.array(points_coords[1::2]) + 1 # Центрирование объекта на графике по оси Y

x_unit_length = 5 / 1.5 # м (см. документацию)
y_unit_length = 7 / 2 # м (см. документацию)

x_real_size = x_p * x_unit_length
y_real_size = y_p * y_unit_length

fig, ax = plt.subplots()
sc_plot = ax.scatter(x_real_size, y_real_size, s=0.5)
ax.set_ylabel('Координата Х, пк')
ax.set_xlabel('Координата Y, пк')
plt.axis('equal')
plt.savefig('slide_1_normalization.png')
plt.close()

# Данные астрономических наблюдений. Может быть дана концентрация вещества, а может и плотность
m = 2*1.6735575*10**(-27) # масса молекулы водорода в килограммах
n = 2*10**11 # характерная концентрация частиц на м^3 в плотных областях туманностей
len_unit = 3.0856776*10**16 # единица длины (1 парсек в метрах)

rho_v_in_m = m * n # плотность водорода в кг/м^3
print('rho_v_in_m: ', rho_v_in_m)
rho_v_in_pc = m * n * len_unit**3 # плотность водорода в кг/пк^3
print('rho_v_in_pc: ', rho_v_in_pc)

scale = 0.1 * len_unit ** 3 # характерная толщина туманности (10% от объёма туманности), которую можно варьировать
rho_s_in_pc = m * n * scale # плотность водорода в кг/пк^2

def density_dist(x, y, x0=0, y0=0, intensity=1, dec_rate=[0.5, 0.5]):
    scalar_func = intensity * np.exp(- dec_rate[0] * (x - x0)**2 - dec_rate[1] * (y - y0)**2) 
    return scalar_func

fig, ax = plt.subplots()
sc_plot = ax.scatter(x_p, y_p, c=density_dist(x_p, y_p, 1.6, 1, rho_s_in_pc, [6.0, 6.5]))
ax.set_ylabel('Координата Х, м')
ax.set_xlabel('Координата Y, м')

cbar = fig.colorbar(sc_plot)
cbar.set_label("Поле плотности, кг/пк^2")

plt.axis('equal')
plt.savefig('slide_1_density_field.png')