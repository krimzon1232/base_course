def step(a, n):
    aa = a
    for i in range(n-1):
        aa = aa * a
    return aa

print(step(float(input("a: ")), int(input("b: "))))