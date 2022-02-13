import numpy as np


def divided_differences(x, f):
    n = len(x)
    F = np.empty((n, n))
    F[:, 0] = f
    for k in range(1, n):
        F[0:n-k, k] = (F[1:n-k+1, k-1] - F[0:n-k, k-1]) / (x[k:] - x[:-k])
    print('Таблица разделенных разностей', F)
    return F


def evaluate(x, F, x0):
    n = len(x)
    P = 0
    xprod = 1.0 # (x - x1) (x - x2) ... (x - xi)
    for i in range(n):
        P += F[0, i] * xprod
        xprod *= (x0 - x[i])
    return P


x = np.array([0,1,2,3,4])
f = np.array([4,2.5,1,-1,-2])

x0 = 3.
result = evaluate(x, divided_differences(x, f), x0)
print('Значение производной', result)
