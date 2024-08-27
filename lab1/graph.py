import pandas as pd
import matplotlib.pyplot as plt

file_path = 'монетки.xlsx'
data = pd.read_excel(file_path)

plt.figure(figsize=(10, 6))
plt.scatter(data['год чеканки'], data['масса'], color='blue', alpha=0.7)

plt.xlabel('год чеканки')
plt.ylabel('масса')
plt.title('зависимость массы от года чеканки')

plt.savefig('graph.png')
