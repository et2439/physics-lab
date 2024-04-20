import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

data = np.loadtxt('data_1.txt')

x = data[:, 0]
y = data[:, 1]
y_err = data[:, 2]

def approx_func(x, k):
    return k / x

popt, pcov = curve_fit(approx_func, x, y, sigma=y_err)

optimal_k = popt[0]

plt.errorbar(x, y, yerr=y_err, fmt='o', color='b', ecolor='r', capsize=5)
plt.plot(x, approx_func(x, optimal_k), 'g--', label=f' {optimal_k:.2f}/x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
