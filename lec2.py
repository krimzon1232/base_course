import lec1
import numpy as np

#1
h = 100
a = 45
b = 35
g = lec1.g
v = ((g*h*(np.tan(b))**2)/(2*(np.cos(a))**2 * (1-(np.tan(b)*np.tan(a)))))**0.5
print(v)

#2
T = 200
Eq = 300
k = lec1.k
e = lec1.e
h = lec1.h

N = 2/(np.pi**0.5) * h**0.5 * (k*T)**(3/2) * e**(Eq/(k*T)) * Eq**(T/2) #OverflowError: (34, 'Numerical result out of range')
print(N)
