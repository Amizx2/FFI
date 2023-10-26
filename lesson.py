# 1 Дан двумерный массив размером 3x3. Определить максимальное значение среди элементов третьего столбца массива; максимальное значение среди элементов второй строки массива. Вывести полученные значения.
import random

n = 3
arr = []

for i in range(n):
    row = [random.randint(-9, 9) for _ in range(n)]
    arr.append(row)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
max_column = max(arr[0][2], arr[1][2], arr[2][2])
max_row = max(arr[1][0], arr[1][1], arr[1][2])
print('')
print(max_column)
print('')
print(max_row)
# 2 Дан двумерный массив размером mxn. Сформировать новый массив заменив положительные элементы единицами, а отрицательные нулями. Вывести оба массива.
matrix = [
    [1, -2, 3],
    [-4, 5, -6]
]

new_matrix = []

for i in range(len(matrix)):
    new_row = []
    for j in range(len(matrix[0])):
        if matrix[i][j] > 0:
            new_row.append(1)
        else:
            new_row.append(0)
    new_matrix.append(new_row)

print("Исходная матрица:")
for row in matrix:
    print(row)

print("Новая матрица:")
for row in new_matrix:
    print(row)



