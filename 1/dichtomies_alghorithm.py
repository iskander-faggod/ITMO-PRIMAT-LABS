from math import sin, cos, log
import matplotlib.pyplot as plt


eps = 0.001  # точность
f = lambda x: x**2 + 3   # функция
a = -1  # левая граница
b = 1  # правая граница

a, b = min(a, b), max(a, b)
plt.plot([i / 1000 + a for i in range((b - a) * 1000)],
         [f(i / 1000 + a) for i in range((b - a) * 1000)])
plt.show()

def dichtomy(a: float, b: float, eps: float):
    iteration_counter : int = 0
    while abs(a - b) > eps:
        iteration_counter += 1
        c = (a + b) / 2
        if f(c - eps) <= f(c + eps):
            b = c
        else:
            a = c
    return c, iteration_counter, c*2

print(dichtomy(a,b,eps))
