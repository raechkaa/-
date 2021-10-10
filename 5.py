#  модифицированный метод ньютона
from sympy import diff, symbols, cos, sin, lambdify


def func(x):
    y = x**3 + 4.01*(x**2)-x-4
    return y


def differentiation1(x1):
    x = symbols('x')
    y = x**3 + 4.01*(x**2)-x-4
    dif1 = diff(y, x)
    exp = lambdify(x, dif1)
    return exp(x1)


def differentiation2(x2):
    x = symbols('x')
    y = x**3 + 4.01*(x**2)-x-4
    dif1 = diff(y, x)
    dif2 = diff(dif1, x)
    exp = lambdify(x, dif2)
    return exp(x2)


x0 = 1.5
print(differentiation2(x0))
print(func(x0))
if func(x0) * differentiation2(x0) > 0:  # func(0.5) = -0.292 < 0 ; differentiation2(0.5) = 2.3 > 0
    n = 0
    print(n, x0, func(x0), differentiation1(x0))
    temp = x0
    for i in range(20):
        i += 1
        xn = temp - func(temp)/differentiation1(x0)
        temp = xn
        print(i, xn, round(func(xn),5), round(differentiation1(xn),5))

else:
    print('не подходит')