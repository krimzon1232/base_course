import numpy as np

N=7
M=3

ar = np.zeros((N, M+1))

for i in range(N):
    for j in range(M):
        n = np.sin(N*i + M*j)
        
        if n >= 0:
            ar[i, j] = n

print(ar[::, ::-1])