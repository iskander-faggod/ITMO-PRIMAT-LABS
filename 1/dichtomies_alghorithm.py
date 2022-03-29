from math import sin, cos, log
import matplotlib.pyplot as plt

eps = 0.001  # точность
f = lambda x: x ** 2 + 3  # функция
a = -1  # левая граница
b = 1  # правая граница

a, b = min(a, b), max(a, b)
plt.plot([i / 1000 + a for i in range((b - a) * 1000)],
         [f(i / 1000 + a) for i in range((b - a) * 1000)])
plt.show()


def dichtomy(a: float, b: float, eps: float):
    interval_sizes = []
    iteration_counter: int = 0
    while abs(a - b) > eps:
        interval_sizes.append(a - b)
        iteration_counter += 1
        c = (a + b) / 2
        if f(c - (eps / 2)) <= f(c + (eps / 2)):
            b = c
        else:
            a = c
    return c, iteration_counter, iteration_counter * 2, interval_sizes


print(dichtomy(a, b, eps))
