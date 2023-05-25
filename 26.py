# Напишите программу, которая на вход принимает два числа A и B, и возводит
# число А в целую степень B с помощью рекурсии.

def power_recursive(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        p = power_recursive(a, b // 2)
        return p * p
    else:
        p = power_recursive(a, (b - 1) // 2)
        return a * p * p

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

print(f"{a} в степени {b} равно {power_recursive(a, b)}")