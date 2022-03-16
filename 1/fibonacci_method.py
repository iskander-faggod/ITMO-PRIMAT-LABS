import math


def fibonacci_method(func: (), a: float, b: float, eps: float) -> (int, int):
    start_interval = a
    end_interval = b

    total_amount_of_iterations, localization_segment, x_1, x_2 = preset_values(a, b, eps)

    iterations_count = 1  # один пушто preset_values() считается за первую итерацию алгоритма
    function_usage_count = 2
    f_x1 = func(x_1)
    f_x2 = func(x_2)
    segment_delta = b - a
    segment_delta_array = []

    while iterations_count != total_amount_of_iterations:
        iterations_count += 1
        if f_x1 < f_x2:
            end_interval = x_2
            x_2 = x_1
            f_x2 = f_x1
            x_1 = start_interval + complement(total_amount_of_iterations, iterations_count, localization_segment)
            f_x1 = func(x_1)
        else:
            start_interval = x_1
            x_1 = x_2
            f_x1 = f_x2
            x_2 = end_interval - complement(total_amount_of_iterations, iterations_count, localization_segment)
            f_x2 = func(x_2)

        segment_delta = abs(segment_delta - (start_interval + end_interval) / 2)
        segment_delta_array.append(segment_delta)
        function_usage_count += 1

    return min(func(x_1), func(x_2)), iterations_count, function_usage_count, segment_delta_array


def preset_values(a: float, b: float, eps: float):
    n = find_n((b - a) / eps)

    length = (b - a) / find_fib_on(n)
    x_1 = a + length * find_fib_on(n - 2)
    x_2 = b - length * find_fib_on(n - 2)

    return n, length, x_1, x_2


def complement(total_iterations: int, cur_iterations: int, localization_segment: float) -> float:
    return localization_segment * find_fib_on(total_iterations - cur_iterations - 1)


def find_fib_on(position: int) -> int:
    if position <= 1:
        return position
    else:
        return find_fib_on(position - 1) + find_fib_on(position - 2)


def find_n(number: float) -> int:
    prev_1 = 1
    prev_2 = 1
    num_fib = 0
    count = 0
    while num_fib <= number:
        num_fib = prev_1 + prev_2
        prev_1 = prev_2
        prev_2 = num_fib
        count += 1

    return count


def function(argument: float) -> float:
    return math.log10(argument ** 2) + 1 - math.sin(argument)