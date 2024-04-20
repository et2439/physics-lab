import pandas as pd
import matplotlib.pyplot as plt

# Загрузите данные из файла Excel
file_path = 'монетки.xlsx'
data = pd.read_excel(file_path)

# Создайте график зависимости
plt.figure(figsize=(10, 6))
plt.scatter(data['год чеканки'], data['масса'], color='blue', alpha=0.7)

# Добавьте метки осей и заголовок
plt.xlabel('год чеканки')
plt.ylabel('масса')
plt.title('зависимость массы от года чеканки')

# Отобразите график
plt.savefig('graph.png')

