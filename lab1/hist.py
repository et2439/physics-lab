import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

file_path = 'монетки.xlsx'
data = pd.read_excel(file_path, header=0, usecols=['плотность', 'год'])

filtered_data = data[data['год'] > 2006]

plt.figure(figsize=(10, 6))
sns.histplot(filtered_data['плотность'], bins=6, kde=True, color='skyblue', stat='density')
sns.kdeplot(filtered_data['плотность'], color='red')

mu, std = norm.fit(filtered_data['плотность'])
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)


plt.xlabel('плотность')
plt.ylabel('количество монет')

print(f'Среднее: {mu:.2f}, Стандартное отклонение: {std:.2f}')

plt.savefig('histogram_plot3.png')
