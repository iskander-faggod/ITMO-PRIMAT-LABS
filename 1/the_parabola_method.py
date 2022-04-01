from math import sin
from math import log1p
from math import pi


def function(x):
    return log1p(x ** 2) + 1 - (sin(x))


def method(left, right, eps):
    iteration = 0
    calls = 0
    segments = []

    while right - left > eps:
        middle = (left + right) / 2
        f_l = function(left)
        f_m = function(middle)
        f_r = function(right)

        calls += 3

        u = abs(middle - (((middle - left) ** 2) * ((f_m - f_r) - ((middle - right) ** 2) * (f_r - f_l))
                          / (2 * ((middle - left) * (f_m - f_r) - (middle - right) * (f_m - f_l)))))

        f_u = function(u)
        calls += 1

        if middle < u:
            if f_m < f_u:
                right = u
            else:
                left = middle

        if middle >= u:
            if f_m < f_u:
                left = u
            else:
                right = middle

        iteration += 1
        segments.append(right - left)

    print(calls, iteration, segments)
    print(f_u)
    return segments, calls, (iteration, (left + right) / 2)


method(16 * pi / 2, 17 * pi / 2, 0.001)
