import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Генерация матрицы 10x10 случайных чисел
data = np.random.rand(10, 10)

# Построение тепловой карты
plt.figure(figsize=(8, 6))
sns.heatmap(data, annot=True, cmap='viridis')
plt.title('Тепловая карта случайных значений (10x10)')
plt.xlabel('Столбцы')
plt.ylabel('Строки')

plt.savefig('teplovaya.png')
plt.show()