#1 Дан двумерный массив размером 3x3. Определить максимальное значение среди элементов третьего столбца массива; максимальное значение среди элементов второй строки массива. Вывести полученные значения.
import random
rows = 3
cols = 3
matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
print("Случайная матрица:")
for row in matrix:
    print(row)
max_in_third_column = max(row[2] for row in matrix)
max_in_second_row = max(matrix[1])
print("Максимальное значение в третьем столбце:", max_in_third_column)
print("Максимальное значение во второй строке:", max_in_second_row)


#2 Дан двумерный массив размером mxn. Сформировать новый массив заменив положительные элементы единицами, а отрицательные нулями. Вывести оба массива.
import random
rows = random.randint(1, 10)
cols = random.randint(1, 10)
matrix = [[random.randint(-9, 9) for _ in range(cols)] for _ in range(rows)]
print("Случайная матрица и изначальная матрица:")
for row in matrix:
    print(row)
print("Новая матрица:")
new_matrix = [[1 if x > 0 else 0 for x in row] for row in matrix]
for row in new_matrix:
    print(row)


#3 Дана целая квадратная матрица n-го порядка. Определить, является ли она магическим квадратом, т. е. такой матрицей, в которой суммы элементов во всех строках и столбцах одинаковы.
import random
def is_magic_square(matrix):
    n = len(matrix)
    expected_sum = sum(matrix[0])
    # Проверка суммы строк
    for row in matrix:
        if sum(row) != expected_sum:
            return False
    # Проверка суммы столбцов
    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != expected_sum:
            return False
    # Проверка суммы диагоналей
    if sum(matrix[i][i] for i in range(n)) != expected_sum:
        return False

    if sum(matrix[i][n - 1 - i] for i in range(n)) != expected_sum:
        return False
    return True
# Размер квадратной матрицы
n = 3
# Создание случайной квадратной матрицы
matrix = [[random.randint(1, 9) for _ in range(n)] for _ in range(n)]
# Вывод сгенерированной матрицы
print("Сгенерированная квадратная матрица:")
for row in matrix:
    print(row)
# Проверка, является ли матрица магическим квадратом
if is_magic_square(matrix):
    print("Это магический квадрат.")
else:
    print("Это не магический квадрат.")


#4 Определить, является ли заданная целая квадратная матрица n-го порядка симметричной (относительно главной диагонали).
def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]
if is_symmetric(matrix):
    print("Матрица симметрична относительно главной диагонали.")
else:
    print("Матрица не симметрична относительно главной диагонали.")


#5 Дана прямоугольная матрица. Найти строку с наибольшей и строку с наименьшей суммой элементов. Вывести на печать найденные строки и суммы их элементов.
# Пример прямоугольной матрицы
import random
rows = 4
cols = 4
matrix = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
for row in matrix:
    print(row)
max_row = max(matrix, key=sum)
min_row = min(matrix, key=sum)
print("Строка с наибольшей суммой элементов:", max_row)
print("Сумма элементов в этой строке:", sum(max_row))
print("Строка с наименьшей суммой элементов:", min_row)
print("Сумма элементов в этой строке:", sum(min_row))


#6 Дана действительная матрица размером n х m, все элементы которой различны. В каждой строке выбирается элемент с наименьшим значением. Если число четное, то заменяется нулем, нечетное - единицей. Вывести на экран новую матрицу
# Простите, не могу приложить ума, как это сделать. К сожалению, я это не осилил... :(