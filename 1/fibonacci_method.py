import math


# Собственно, главный метод
def fibonacci_method(func: (), a: float, b: float, eps: float) -> (int, int):
    start_interval = a
    end_interval = b

    '''
    preset_values() ето расчёт значений на первом шаге, то есть первых чисел фибоначчи
    формулы первых фибоначчи не с потолка, это есть в теоретической части, просто взял оттуда
    '''
    total_amount_of_iterations, localization_segment, x_1, x_2 = preset_values(a, b, eps)

    iterations_count = 1  # один пушто preset_values() считается за первую итерацию алгоритма
    function_usage_count = 2
    f_x1 = func(x_1)
    f_x2 = func(x_2)
    segment_delta_array = [b - a]
    # крутимся, пока количество итераций не станет равно тому к-ву, которое мы посчитали, исходя из длины интервала и заданной точности
    while iterations_count != total_amount_of_iterations:
        iterations_count += 1
        # тут собственно происходит сам метод фибоначчи
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

        # здесь мы занимаемся данными, которые нам надо вернуть, динамику измемения интервала, количество вычислений ф-ии и к-во итераций алгоритма
        segment_delta = abs(end_interval - start_interval)
        segment_delta_array.append(segment_delta)
        function_usage_count += 1
    return func((x_1 + x_2) / 2), iterations_count, function_usage_count, segment_delta_array


'''
считаем первый шаг
'''
def preset_values(a: float, b: float, eps: float):
    """
    n это порядковый номер первого числа фибоначчи, большего (b - a) / eps
    из теоретической части
    """
    n = find_n((b - a) / eps)

    length = (b - a) / find_fib_on(n)
    x_1 = a + length * find_fib_on(n - 2)
    x_2 = b - length * find_fib_on(n - 2)

    return n, length, x_1, x_2

# ето просто часть формулы, мне лень было дважды её переписывать в главном методе
def complement(total_iterations: int, cur_iterations: int, localization_segment: float) -> float:
    return localization_segment * find_fib_on(total_iterations - cur_iterations - 1)


# ищем n-ое (position-ое) число фибоначчи
def find_fib_on(position: int) -> int:
    if position <= 1:
        return position
    else:
        return find_fib_on(position - 1) + find_fib_on(position - 2)


# ищем первое число фибоначчи, которое больше number
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



