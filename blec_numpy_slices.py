import numpy as np

ar = np.arange(2, 21, 2)
new_ar = ar[-1::-1] * 2
mat = np.array([ar, new_ar])
print(ar)
print(new_ar)
print("matrix")
print(mat)
print(mat[::-1])
print(mat[::, 5:1:-1])