#  метод половинного деления
import math

a = float(input())
b = float(input())


def func(x):
    y = x**3 + 4.01*(x**2)-x-4          #  y = x*(2**x) - 1
    return y


print(round(func(a),5))
print(round(func(b),5))
print(round((a+b)/2,5))
print(round(func((a+b)/2),5))