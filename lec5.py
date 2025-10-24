import numpy as np
array = np.array([[1, 2], [2, 3], [8, 12]])

new_ray = []
for a in array:
    a = a[::-1]
    new_ray.append(a)
    
print(np.array(new_ray))
#aboba