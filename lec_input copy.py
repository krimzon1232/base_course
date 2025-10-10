"""a = str(input("text: "))
try:
    b, c = map(float, input("Введите 2 числа через запятую:\n> ").split())
except: print("чтото не так")

print(a, b, c)
print(b+c)
print(str(b) + str(c))"""

import random
import time
t1 = "good"
t2 = "bad"
ls = [t1, t2]
try:
    while True:
        print(f"------\n{t1} или {t2}?")
        print(random.choice(ls))
        time.sleep(2)
except: print("ошибка")