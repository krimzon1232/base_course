import numpy as np

ar = np.array([[1, 3], [2, 4], [7, round(np.pi, 2)]])
print(ar)
print(type(ar))


print(ar * 2)
print(ar[0] + ar[1])
print()
print(ar[-1::-1])