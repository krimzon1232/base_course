import numpy as np
def kaktof(a, b, n):
    return (float(x**2) for x in np.arange(a, b, (b-a)/n))

print(list(kaktof(2, 10, 4)))