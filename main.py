from numpy import *
import matplotlib.pyplot as plt
from scipy import interpolate
from cubic_spline_math import *
import cubic_spline_coefficients_setup
# task number = 12

fig, ax = plt.subplots()
ax.set_axisbelow(True)
ax.grid(zorder=-1)

x = linspace(0, 2, 5)
y = [0.0, 0.97943, 1.8415, 2.4975, 2.9093]
n = len(x)

coefficients = cubic_spline_coefficients_setup.setup(x, y)

ix = linspace(0, x[n-1], 100000)
iy = []
for x_ in ix:
    iy.append(calculate_interpolated_value_with_x(coefficients, x, x_))
    if x_ == 1.5:
        print(calculate_interpolated_value_with_x(coefficients, x, x_))


for i in range(n):
    ax.scatter(x[i], y[i], c = "red", s = 15)

y_stlib_interpolated = interpolate.splev(ix, interpolate.splrep(x, y, s=0), der=0)

ax.plot(ix, iy, zorder=0)
ax.plot(ix, y_stlib_interpolated, zorder=0)
ax.legend(["interpolation", "lib interpolation", "nodes"])
plt.show()


x_ = 1
print(f"f({x_}) is ~= ", calculate_interpolated_value_with_x(coefficients, x, x_))

print(coefficients)

