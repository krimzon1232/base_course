import numpy as np


inp = input("Введите числа массива: ").split()
for i in range(len(inp)):
    inp[i] = int(inp[i])
ms = np.array(inp)
print(ms)

new_num = int(input("Введите новое число: "))
new_pos = int(input("Введите позицию новое число: ")) - 1

nms = []

for i in range(len(ms)):
    if i == new_pos:
        nms.append(new_num)
        nms.append(ms[i])
    else:
        nms.append(ms[i])
        
nmsa = np.array(nms)
print(nmsa)

