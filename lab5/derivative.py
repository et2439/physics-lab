import numpy as np

def calculate_derivative(x, y):
    n = len(x)
    derivative = np.zeros(n)

    for i in range(1, n - 1):
        h = x[i + 1] - x[i - 1]
        derivative[i] = (y[i + 1] - y[i - 1]) / (2 * h)

    derivative[0] = (y[1] - y[0]) / (x[1] - x[0])
    derivative[-1] = (y[-1] - y[-2]) / (x[-1] - x[-2])

    return np.abs(derivative)

file_path = str(input())

with open(file_path, 'r') as file:
    lines = file.readlines()

data = [list(map(float, line.strip().split())) for line in lines]
data = np.array(data)

x_values = data[:, 0]
y_values = data[:, 1]

derivative_values = calculate_derivative(x_values, y_values)

print("Значения модуля производной:", derivative_values)
print("Среднее значение модуля производной:", np.mean(derivative_values))
