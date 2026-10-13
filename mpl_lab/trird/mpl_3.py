import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('students.csv', sep=';', header=None,
                 names=['teacher', 'group', 'grade'])


by_teacher = df.groupby(['teacher', 'grade']).size().unstack(fill_value=0)
by_group   = df.groupby(['group', 'grade']).size().unstack(fill_value=0)


def score(table):
    grades = table.columns
    total = table.sum(axis=1)
    avg = sum(table[g] * g for g in grades) / total
    return avg.sort_values(ascending=False)

t, g = score(by_teacher), score(by_group)
most_lenient = t.index[0]
most_strict  = t.index[-1]
worst_group  = g.index[-1]


grade_colors = {
    3: '#d32f2f',  # тёмно-красный
    4: '#f44336',  # красный
    5: '#ff9800',  # оранжевый
    6: '#ffc107',  # жёлтый
    7: '#cddc39',  # лаймовый
    8: '#8bc34a',  # светло-зелёный
    9: '#4caf50',  # зелёный
    10: '#2e7d32', # тёмно-зелёный
}


all_grades = list(range(3, 11))
by_teacher = by_teacher.reindex(columns=all_grades, fill_value=0)
by_group   = by_group.reindex(columns=all_grades, fill_value=0)


colors = [grade_colors[g] for g in all_grades]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

by_teacher.plot(kind='bar', stacked=True, ax=ax1, color=colors)
ax1.set_title('Распределение оценок по преподавателям')
ax1.set_xlabel('Преподаватель')
ax1.set_ylabel('Студентов')
ax1.tick_params(axis='x', rotation=45)

by_group.plot(kind='bar', stacked=True, ax=ax2, color=colors)
ax2.set_title('Распределение оценок по группам')
ax2.set_xlabel('Группа')
ax2.set_ylabel('Студентов')
ax2.tick_params(axis='x', rotation=45)


for label in ax1.get_xticklabels():
    if label.get_text() == most_lenient:
        label.set_bbox(dict(facecolor='lightgreen', edgecolor='green', pad=3))
    elif label.get_text() == most_strict:
        label.set_bbox(dict(facecolor='lightcoral', edgecolor='red', pad=3))

for label in ax2.get_xticklabels():
    if label.get_text() == worst_group:
        label.set_bbox(dict(facecolor='khaki', edgecolor='orange', pad=3))

plt.tight_layout(rect=[0, 0.10, 1, 1])


fig.text(0.5, 0.03,
         f'Самый халявный: {most_lenient}    |    '
         f'Самый строгий: {most_strict}    |    '
         f'Самая раздолбайская: {worst_group}',
         ha='center', va='center', fontsize=13,
         bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow'))

plt.savefig('grades.png', dpi=120, bbox_inches='tight')
plt.show()