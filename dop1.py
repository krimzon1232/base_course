import numpy as np

def ms_inp(x, y):
    ls = []
    for yd in range(y):
        yls = []
        
        for xd in range(x):
            inp = int(input(f"введите число {xd} строки {yd}: "))
            yls.append(inp)
            
        ls.append(yls)
        
    print("Ввод завершен \n")
    return(np.array(ls))

def ms_checker(m1, m2, x, y):
    ls = []
    for yd in range(y):
        yls = []
        
        for xd in range(x):
            if m1[yd][xd] >= m2[yd][xd]:
                i = m1[yd][xd]
            else:
                i = m2[yd][xd]
            yls.append(i)
        
        ls.append(yls)
        
    return(np.array(ls))


xi, yi = map(int, input("введите размер масивов через пробел: ").split())


mass1 = ms_inp(xi, yi)
mass2 = ms_inp(xi, yi)
mass3 = ms_checker(mass1, mass2, xi, yi)

print(mass3)