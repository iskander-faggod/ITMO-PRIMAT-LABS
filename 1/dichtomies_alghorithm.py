import math


def dichotomies_algorithm(function: (float, float), a: float, b: float, eps=1e-5):
    n = 0
    while abs(b - a) > eps:
        n += 1
        x = (a + b) / 2.0
        if x == 0:
            print("x равен нулю ", x)
        function_with_x_result = function(x)
        function_with_a_result = function(a)
        if (function_with_x_result < 0 and function_with_a_result < 0) \
                or (function_with_x_result > 0 and function_with_a_result > 0):
            a = x
        else:
            b = x
    return x, n
