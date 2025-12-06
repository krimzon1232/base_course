import os
import math


def circ():
    r = float(input("Введите радиус\n> "))
    a = math.pi * r**2
    input(f"полщадь = {a}\nНажмите Enter для продолжения")
def rect():
    a = float(input("Введите сторону a\n> "))
    b = float(input("Введите сторону b\n> "))
    x = a*b
    input(f"полщадь = {x}\nНажмите Enter для продолжения")
def trg():
    a = float(input("Введите основание\n> "))
    b = float(input("Введите высоту\n> "))
    x = a*b
    input(f"полщадь = {x}\nНажмите Enter для продолжения")

def menu():
    i = 0
    while i == 0:
        os.system("clear")
        match input("1-круг\n2-прямоугольник\n3-треугольник\n0-выход\n> "):
            case "1": a = circ()
            case "2": a = rect()
            case "3": a = trg()
            case "0": i = 1
            case _: print("неверная команда")  

            
            
menu()