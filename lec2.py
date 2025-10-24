import numpy as np
import lec1_phisconst as phis

u = (phis.g*100*np.tan(35)/(2*(np.cos(45)**2)*(1-np.tan(35)*np.tan(45))))**0.5
print(u)

N = (2/(np.pi)**0.5) * (phis.h)**0.5 * (200*phis.k)**(3/2) * phis.ee**(300 / (phis.k*200)) * 300**(200/2)
print(N) #OverflowError: (34, 'Numerical result out of range'less 3 #abobaimport numpy as np
trigonometry_array = []
n = int(input("Vvedite chislo n: "))
m = int(input("Vvedite chislo m: "))
i = int(input("Vvedite chislo i: "))
j = int(input("Vvedite chislo j: "))

for a in range(n):
    list = []
    for b in range(m):
        o = np.sin(a*i + b*j + 1)
        if o < 0:
            o = 0
        list.append(o)
    trigonometry_array.append(list)
    
trigonometry_array = np.array(trigonometry_array)
print(trigonometry_array)) 