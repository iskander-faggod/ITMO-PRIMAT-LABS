import math as m

const = (3 - m.sqrt(5)) / 2


def find_min(function, a, b, eps):
    function_calls = 0
    x = w = v = (a + b) / 2
    f_x, f_w, f_v = function((a + b) / 2)
    function_calls += 1
    segments = [b - a]
    d_curr = d_prev = b - a
    middle_point = (a + b) / 2
    inside_point = (a + b) / 2

    while b - a > eps:
        g = d_prev
        d_prev = d_curr
        u = None

        if abs(a - middle_point) > eps or abs(middle_point - b) > eps:
            u = find_u(x, w, v, f_x, f_w, f_v)

        if (u is not None and abs(u - a) > eps
                and abs(b - u) > eps
                and abs(u - middle_point) < g / 2):

            d_curr = abs(inside_point - middle_point)
            if a < u < middle_point:
                b = middle_point
                inner_point = u

                right_bound_result = middle_result

            elif middle < parabola_min < right_bound:
                left_bound = middle
                inner_point = parabola_min

                left_bound_result = middle_result
        else:
            if middle <= (right_bound + left_bound) / 2:
                inner_point = middle + const * (right_bound - middle)
                current_len = right_bound - middle

            else:
                inner_point = middle + const * (left_bound - middle)
                current_len = middle - left_bound

        if m.fabs(inner_point - middle) < eps:
            inner_point = middle + eps if inner_point - middle > 0 else middle - eps

        inner_result = function(inner_point)
        calls += 1

        if inner_result <= middle_result:
            if inner_point >= middle:
                left_bound = middle
                left_bound_result = middle_result
            else:
                right_bound = middle
                right_bound_result = middle_result

            right_point, left_point, middle = left_point, middle, inner_point
            right_result, left_result, middle_result = left_result, middle_result, inner_result
            segments.append((min(left_bound, right_bound), max(left_bound, right_bound)))

        else:
            if inner_point >= middle:
                right_bound = inner_point
                right_bound_result = inner_result
            else:
                left_bound = inner_point
                left_bound_result = inner_result

            if inner_result <= left_result or left_point == middle:
                right_point, left_point = left_point, inner_point
                right_result, left_result = left_result, inner_result
                segments.append((min(left_bound, right_bound), max(left_bound, right_bound)))

            elif inner_result <= right_result or right_point == middle:
                right_point, right_result = inner_point, middle_result
                segments.append((min(left_bound, right_bound), max(left_bound, right_bound)))

    return (segments[-1][0] + segments[-1][1]) / 2, calls, segments


def find_u(x, w, v, f_x, f_w, f_v):
    if x == w or w == v or x == v:
        return None

    a1 = (f_w - f_x) / (w - x)
    a2 = 1 / (v - w) * ((f_v - f_x) / (v - x) - (w - x) / (w - x))

    if a2 == 0:
        return None

    return 1.0 / 2.0 * (x + w - a1 / a2)

def function(argument: float) -> float:
    return m.log10(argument ** 2) + 1 - m.sin(argument)


print(find_min(function, -100, 99, 0.001))