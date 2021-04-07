def h(i, x):
    return x[i] - x[i - 1]


def lambda_mu(i, x):
    if i == 0:
        alpha = 0
    else:
        alpha = (x[i] - x[i - 1]) / (x[i] - x[i - 2])

    if i == len(x):
        mu = 0
    else:
        mu = 1 - alpha

    return alpha, mu


def d(n, y, x):
    if n == 0 or n == len(x):
        return 0
    return 6 / h(n, x) * (y[n] - (y[n] - y[n - 1]) / h(n, x))


def calculate_interpolated_value(coefficients, xj, x):
    # (c1,c2,c3,c4) = coefficients
    h = x - xj
    sum = 0
    for i in range(4):
        sum += float(coefficients[i]) * h ** i
    return sum


def find_closest_x(x, value):
    if value > x[-1]:
        return x[-1], len(x)-2

    if value <= x[0]:
        return x[0], 0

    for i in range(len(x) - 1):
        if x[i] <= value <= x[i + 1]:
            return x[i], i


def calculate_interpolated_value_with_x(coefficients, x_set, x_point):
    (closest_x, closest_index) = find_closest_x(x_set, x_point)
    return calculate_interpolated_value(coefficients[closest_index], closest_x, x_point)
