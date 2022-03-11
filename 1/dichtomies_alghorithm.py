import math


def func(x: float, eps=1e-5) -> float:
    if x == 0:
        x = eps
    return math.sqrt(x + 1) - 1 / x


def dichotomies_algorithm(function: (float, float), a: int, b: int, eps=1e-5):
    n = 0
    while abs(b - a) > eps:
        n += 1
        x = (a + b) / 2.0
        function_with_x_result = function(x)
        function_with_a_result = function(a)
        if (function_with_x_result < 0 and function_with_a_result < 0) \
                or (function_with_x_result > 0 and function_with_a_result > 0):
            a = x
        else:
            b = x
    return x, n


x, n = dichotomies_algorithm(func, 0, 1)
print(x)
print(n)
print(func(x))
