import numpy as np

xi = int(input("введите размер масивов по x: "))
yi = int(input("введите размер масивов по y: "))
ls = []
for yd in range(yi):
    yls = []
    
    for xd in range(xi):
        inp = int(input(f"введите число {xd} строки {yd}: "))
        yls.append(inp)
        
    ls.append(yls)
    
print("Ввод завершен \n")
mass1=(np.array(ls))

ls = []
for yd in range(yi):
    yls = []
    
    for xd in range(xi):
        inp = int(input(f"введите число {xd} строки {yd}: "))
        yls.append(inp)
        
    ls.append(yls)
    
print("Ввод завершен \n")
mass2=(np.array(ls))



ls = []
for yd in range(yi):
    yls = []
    
    for xd in range(xi):
        if mass1[yd][xd] >= mass2[yd][xd]:
            i = mass1[yd][xd]
        else:
            i = mass2[yd][xd]
        yls.append(i)
    
    ls.append(yls)
    
mass3 = (np.array(ls))


print("mass1")
print(mass1)
print("mass2")
print(mass2)
print("mass3")
print(mass3)