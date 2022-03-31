import math


def golden_ratio_algorithm(a: float, b: float, eps: float, func: ()):
    function_count_iterations = 0
    algo_iterations = 0
    segment_delta = b - a
    segment_delta_array = [segment_delta]

    first_point = a + 0.382 * (b - a)
    second_point = b - 0.382 * (b - a)
    f_first_point = func(first_point)
    f_second_point = func(second_point)
    function_count_iterations += 2

    while b - a > eps:
        algo_iterations += 1
        if f_first_point < f_second_point:
            b = second_point
            second_point = first_point
            f_second_point = f_first_point
            first_point = a + 0.382 * (b - a)
            f_first_point = func(first_point)
        else:
            a = first_point
            first_point = second_point
            f_first_point = f_second_point
            second_point = b - 0.382 * (b - a)
            f_second_point = func(second_point)

        segment_delta = abs(b - a)
        segment_delta_array.append(segment_delta)
        function_count_iterations += 1

    return func((a + b) / 2), function_count_iterations, algo_iterations, segment_delta_array


