import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3,4])
y = np.array([4,2.5,1,-1,-2])

def Newton(x, y):
   if len(x) == 1:
        #print(d[x[0]])
        return d[x[0]]
   return (Newton(x[1:], y) - Newton(x[: len(x) - 1], y)) / (x[len(x) - 1] - x[0])

X = sym.symbols('X')

d = dict(zip(x, y))
P = 0
n = 1

for i in range(len(x)):
    P = P + n * Newton(x[0:i + 1], y)
    n = n * (X - x[i])
print('Interpolant: ',sym.simplify(P))

pn = sym.lambdify(X, P, "numpy")

y_new = [0] * len(x)

for i in range(len(x)):
    y_new[i] = pn(x[i])




fig, ax = plt.subplots()
ax.plot(x, y_new, '-', label='Interpolant', color='black')
ax.plot(x, y, '.', label='Starting points', color='green')
ax.legend()
plt.show()
