from cubic_spline_math import *
from numpy import linalg
def setup(x, y):
    n = len(x)
    matrix = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        matrix[i][i] = 2

    # lambdas
    for i in range(n - 1):
        matrix[i][i + 1] = lambda_mu(i, x)[0]

    # mu s
    for i in range(1, n):
        matrix[i][i - 1] = lambda_mu(i, x)[1]

    d_matrix = []
    for i in range(n):
        d_matrix.append(d(i, y, x))


    M_matrix = linalg.solve(matrix, d_matrix)

    coefficients = []
    for j in range(n - 1):
        new_coefficients = []
        new_coefficients.append(y[j])
        new_coefficients.append((y[j + 1] - y[j]) / h(j + 1, x) - (2 * M_matrix[j] + M_matrix[j + 1]) / 6 * h(j + 1, x))
        new_coefficients.append(M_matrix[j] / 2)
        new_coefficients.append((M_matrix[j + 1] - M_matrix[j]) / 6 / h(j + 1, x))
        coefficients.append(new_coefficients)

    return coefficients