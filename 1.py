# f(x) = exp(2x) + 3x - 4 = 0
# метод деления пополам
import math


def f(x):
    a = math.exp(2*x) + 3*x - 4
    return a


def f2(x):
    b = 4*math.exp(2*x)
    return b


def f1(x):
    c = 2*math.exp(2*x) + 3
    return c


# n = 0


print(f(0.4))
print(f(1))
print((0.4+1)/2)
print(f((0.4+1))/2)

print(f2(0.4))
print(f1(0.4))
