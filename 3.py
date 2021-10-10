#  метод простой итерации
import math
import numpy as np
#  y = x*(2**x) - 1


def fi(x):
    return 1/(2**x)   #  подходит т.к. |fi'(x)| = 0,46 < 1


x0 = 0.6
n = 0
print(n, x0, fi(x0))
for i in range(20):
        n += 1
        x0 = fi(x0)
        print(n, x0,fi(x0))


