import matplotlib.pyplot as plt

# Данные
categories = ['Музыка', 'Фильмы', 'Спорт', 'Путешествия', 'Чтение']
values = [25, 30, 15, 20, 10]

# Построение горизонтальной столбчатой диаграммы
plt.figure(figsize=(8, 5))
plt.barh(categories, values, color='skyblue')
plt.xlabel('Популярность (%)')
plt.title('Предпочтения пользователей по категориям')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('digrama.png')
plt.show()