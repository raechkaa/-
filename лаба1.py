#  метод секущих
import math

a = float(input())
b = float(input())


def func(x):
    y = x**3 + 4.01*(x**2)-x-4   #  y = x*(2**x) - 1
    return y


xn = (a*func(b)-b*func(a))/(func(b)-func(a))
print(round(func(a),5))
print(round(func(b),5))
print(round(xn,5))
print(round(func(xn),5))
