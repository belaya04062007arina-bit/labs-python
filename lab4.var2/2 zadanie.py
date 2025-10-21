import numpy as np
import matplotlib.pyplot as plt

# "зерно" генератора
np.random.seed(42) 

# Кластер 1: центр в точке (2, 2)
# np.random.normal(среднее, стандартное_отклонение, количество_точек)
x1 = np.random.normal(2, 0.5, 50)
y1 = np.random.normal(2, 0.5, 50)

# Кластер 2: центр в точке (6, 7)
x2 = np.random.normal(6, 0.5, 50)
y2 = np.random.normal(7, 0.5, 50)

# Кластер 3: центр в точке (4, 8)
x3 = np.random.normal(4, 0.5, 50)
y3 = np.random.normal(8, 0.5, 50)

# scatter plot

# Задаем размер фигуры для лучшей читаемости
plt.figure(figsize=(10, 8))

# Рисуем точки для каждого кластера, указывая свой цвет и метку (label)
plt.scatter(x1, y1, color='blue', label='Кластер 1')
plt.scatter(x2, y2, color='red', label='Кластер 2')
plt.scatter(x3, y3, color='green', label='Кластер 3')


#оформлениe для наглядности
# Добавляем заголовок диаграммы
plt.title('Точечная диаграмма с тремя кластерами данных')

# Подписываем оси
plt.xlabel('Значения по оси X')
plt.ylabel('Значения по оси Y')

plt.legend()

plt.grid(True)

plt.savefig('tochechnaya.png')
plt.show()