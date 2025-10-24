import numpy as np
trigonometry_array = []
n = int(input("Vvedite chislo n: "))
m = int(input("Vvedite chislo m: "))
i = int(input("Vvedite chislo i: "))
j = int(input("Vvedite chislo j: "))

for a in range(n):
    list = []import numpy as np
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
print(trigonometry_array)
    for b in range(m):
        o = np.sin(a*i + b*j + 1)
        if o < 0:
            o = 0
        list.append(o)
    trigonometry_array.append(list)
    
trigonometry_array = np.array(trigonometry_array)
print(trigonometry_array)