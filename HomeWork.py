#1. Создать объект pandas Series из листа, объекта NumPy, и словаря
import pandas as pd
import numpy as np

#Список/
list_data = [10, 20, 30, 40, 50]
series_from_list = pd.Series(list_data)
print('Серия из списка:')
print(series_from_list)

#Массив NumPy
numpy_array = np.array([10, 20, 30, 40, 50])
series_from_numpy = pd.Series(numpy_array)
print('\nСерия из массива NumPy:')
print(series_from_numpy)

#Словарь
dict_data = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
series_from_dict = pd.Series(dict_data)
print('\nСерия из словаря:')
print(series_from_dict)
#2. Получить не пересекающиеся элементы в двух объектах Series
import pandas as pd

series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([4, 5, 6, 7, 8])

elements = series1.index.symmetric_difference(series2.index)

print("Не пересекающиеся элементы:")
print(series1[elements])
print(series2[elements])
#3. Узнать частоту уникальных элементов объекта Series (гистограмма)

import pandas as pd

# Создание Series
series = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5])

# Получение частоты уникальных элементов (гистограмма)
histogram = series.value_counts()

# Вывод результатов
print("Гистограмма частоты уникальных элементов:")
print(histogram )

#4. Объединить два объекта Series вертикально и горизонтально
import pandas as pd

series1 = pd.Series([1, 2, 3], name='Series1')
series2 = pd.Series([4, 5, 6], name='Series2')

# Вертикальное объединение
result_vertical = pd.concat([series1, series2], axis=0)

print("Вертикальное объединение:")
print(result_vertical)

# Горизонтальное объединение
result_horizontal = pd.concat([series1, series2], axis=1)

print("Горизонтальное объединение:")
print(result_horizontal)

#5 Найти разность между объектом Series и смещением объекта Series на n
import pandas as pd

# Создаем объект Series
data = pd.Series([1, 3, 6, 10, 15])

# Вычисляем разность между элементами и их смещением на 1 позицию
difference = data.diff(1)

print("Объект Series:")
print(data)

print("\nРазность смещения на 1 позицию:")
print(difference)

