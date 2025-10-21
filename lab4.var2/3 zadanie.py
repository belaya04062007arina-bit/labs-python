import matplotlib.pyplot as plt

# Данные о предпочтениях пользователей
labels = ['Музыка', 'Фильмы', 'Спорт', 'Путешествия', 'Чтение']
sizes = [25, 30, 15, 20, 10]
colors = ['gold', 'lightblue', 'lightgreen', 'coral', 'violet']
explode = (0.1, 0, 0, 0, 0)  # Выделим 'Музыка'

# Построение круговой диаграммы
plt.figure(figsize=(6,6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Предпочтения пользователей по категориям')
plt.axis('equal')  # Круглая форма

plt.savefig('pie_chart.png')
plt.show()