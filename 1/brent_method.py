import math as m


def brent_method(a: float, b: float, eps: float, func: ()):
    function_calls = 0
    segments = []
    ratio = (3 - m.sqrt(5)) / 2
    x = w = v = (a + b) / 2
    f_x = f_w = f_v = func(x)
    iteration_count = 1
    d_prev = d_curr = b - a
    u_real: float

    count = 20
    while b - a > eps:
        g = d_prev
        d_prev = d_curr
        iteration_count += 1
        # Determine what 'u' to choose. Either with paraboloidic minimization
        # or with golden ratio.

        u_inter = find_u(x, w, v, f_x, f_w, f_v)
        # if 'u' satisfies criterias for paraboloidic method, then we "accept" 'u' and use it in further calculations
        if u_inter is not None and a + eps <= u_inter <= b - eps and abs(u_inter - x) < g / 2:
            u_real = u_inter
        # if not -- calculating 'u' using golden ratio method
        else:
            if x < (a + b) / 2:
                u_real = x + ratio * (b - x)
                d_prev = b - x
            else:
                u_real = x - ratio * (x - a)
                d_prev = x - a

        f_u = func(u_real)
        function_calls += 1

        # Updating values
        if f_u <= f_x:
            if u_real < x:
                b = x
            else:
                a = x
            v = w
            w = x
            x = u_real
            f_v = f_w
            f_w = f_x
        else:
            if u_real < x:
                a = u_real
            else:
                b = u_real
            if f_u < f_w or w == x:
                v = w
                w = u_real
                f_v = f_w
                f_w = f_u
            elif f_u <= f_v or v == x or v == w:
                v = u_real
                f_v = f_u
        segments.append(b - a)
    return func((a + b) / 2), iteration_count, function_calls, segments


def find_u(x, w, v, f_x, f_w, f_v):
    if 2 * ((w - x) * (f_w - f_v) - (w - v) * (f_w - f_x)) == 0:
        return None
    return w - (((w - x) ** 2) * (f_w - f_v) - ((w - v) ** 2) * (f_w - f_x)) / (
            2 * ((w - x) * (f_w - f_v) - (w - v) * (f_w - f_x)))


def function(argument: float) -> float:
    return m.log10(argument ** 2) + 1 - m.sin(argument)


print(brent_method(-100, 99, 0.01, function))
