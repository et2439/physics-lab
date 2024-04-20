import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

data = np.loadtxt('data.txt')

x = data[:, 0]
y = data[:, 1]
y_err = data[:, 2]

def approx_func(x, k):
    return np.sqrt(2 * k / x)

popt, pcov = curve_fit(approx_func, x, y, sigma=y_err)

k = popt[0]

plt.errorbar(x, y, yerr=y_err, fmt='o', color='b', ecolor='r', capsize=5)
plt.plot(x, approx_func(x, k), 'g--', label='sqrt(2*k/m)')
plt.xlabel('m')
plt.ylabel('V')
plt.legend()
plt.grid(True)
plt.show()

