import numpy as np
import matplotlib.pyplot as plt
import math

# Создаем данные
x = np.linspace(0, 5, 100)
z1 = [math.cos(a) + math.cos(3*a) + math.sin(a) for a in x]
z2 = [2 * math.sqrt(2) * (math.cos(a) * math.sin(math.pi + 2*a)) for a in x]

# Строим график
fig, ax1 = plt.subplots()

# Первая ось Y
ax1.plot(x, z1, 'b-', label='z1 = cos(a) + cos(3a) + sin(a)')
ax1.set_xlabel('x')
ax1.set_ylabel('z1', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Вторая ось Y
ax2 = ax1.twinx()
ax2.plot(x, z2, 'r--', label='z2 = 2√2·cos(a)·sin(π+2a)')
ax2.set_ylabel('z2', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Легенда
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
fig.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper right')

# Аннотации
ax1.annotate('Пик z1', xy=(x[np.argmax(z1)], max(z1)),
             xytext=(x[np.argmax(z1)]+0.5, max(z1)+0.5),
             arrowprops=dict(facecolor='blue', shrink=0.05))

ax2.annotate('Пик z2', xy=(x[np.argmax(z2)], max(z2)),
             xytext=(x[np.argmax(z2)]+0.5, max(z2)+0.5),
             arrowprops=dict(facecolor='red', shrink=0.05))

plt.savefig('dual_axis_plot.png')
plt.title('Графики функций z1 и z2 с двумя осями Y')
plt.tight_layout()
plt.show()
