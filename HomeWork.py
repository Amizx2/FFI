#Домашняя работа 6
#1 Дан двумерный массив размером 3x3. Определить максимальное значение среди элементов третьего столбца массива; максимальное значение среди элементов второй строки массива. Вывести полученные значения.
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
#2 Дан двумерный массив размером mxn. Сформировать новый массив заменив положительные элементы единицами, а отрицательные нулями. Вывести оба массива.
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


#3 Дана целая квадратная матрица n-го порядка. Определить, является ли она магическим квадратом, т. е. такой матрицей, в которой суммы элементов во всех строках и столбцах одинаковы.
matrix = [
    [3, 8, 7],
    [10, 6, 2],
    [5, 4, 9]
]
n = len(matrix)
expected_sum = sum(matrix[0])

for row in matrix:
    if sum(row) != expected_sum:
        flag_magic = False
        break
else:
    flag_magic = True
    
if flag_magic:
    for j in range(n):
        column_sum = sum(matrix[i][j] for i in range(n))
        if column_sum != expected_sum:
            flag_magic = False
            break
            
if flag_magic:
    diagonal1_sum = sum(matrix[i][i] for i in range(n))
    if diagonal1_sum != expected_sum:
        flag_magic = False
        
if flag_magic:
    diagonal2_sum = sum(matrix[i][n - i - 1] for i in range(n))
    if diagonal2_sum != expected_sum:
        flag_magic = False
        
if flag_magic:
    print(f"Матрица является магическим квадратом. Сумма эллементов равна: {expected_sum} ")
else:
    print("Матрица не является магическим квадратом.")
    
    
#4 Определить, является ли заданная целая квадратная матрица n-го порядка симметричной (относительно главной диагонали).
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]
n = len(matrix)
flag_symmetric = True

for i in range(n):
    for j in range(i, n):
        if matrix[i][j] != matrix[j][i]:
            flag_symmetric = False
            break
            
if flag_symmetric:
    print("Матрица является симметричной относительно главной диагонали.")
else:
    print("Матрица не является симметричной относительно главной диагонали.")


#5 Дана прямоугольная матрица. Найти строку с наибольшей и строку с наименьшей суммой элементов. Вывести на печать найденные строки и суммы их элементов.
matrix = [
    [5, 3, 3],
    [4, 6, 6],
    [7, 23, 9]
]
sums = []

for i, row in enumerate(matrix):
    row_sum = sum(row)
    sums.append(row_sum)
    max_sum_row = sums.index(max(sums)) + 1
    min_sum_row = sums.index(min(sums)) + 1

print(f"Строка с наибольшей суммой элементов: Строка {max_sum_row}, сумма = {max(sums)}")
print(f"Строка с наименьшей суммой элементов: Строка {min_sum_row}, сумма = {min(sums)}")
#6 Дана действительная матрица размером n х m, все элементы которой различны. В каждой строке выбирается элемент с наименьшим значением. Если число четное, то заменяется нулем, нечетное - единицей. Вывести на экран новую матрицу.
matrix = [
    [3, 1, 4],
    [7, 2, 9],
    [6, 5, 8]
]

n = len(matrix)
m = len(matrix[0])

new_matrix = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    min_value = min(matrix[i])
    for j in range(m):
        if matrix[i][j] == min_value and min_value % 2 == 0:
            new_matrix[i][j] = 0
        if matrix[i][j] == min_value and min_value % 2 != 0:
            new_matrix[i][j] = 1

for row in new_matrix:
    print(row)


#4 домашняя работа, я не успел вам отправить, прошу прощения :)
# 1 Дана строка. Подсчитать самую длинную последовательность подряд идущих букв «н». Преобразовать ее, заменив точками все восклицательные знаки.
st = str(input('Введите строку:'))
st = st.replace('!', '.')
k = 1
kmax = 0
for i in range(len(st) - 1):
    for g in range(i + 1, len(st)):
        if st[i] == 'н' and st[g] == 'н':
            k += 1
            kmax = max(k, kmax)
        else:
            k = 1
print(f'Ваше количество букв(н):{kmax}, измененная строка:{st}')


#2 Дана строка символов, среди которых есть одна открывающаяся и одна закрывающаяся скобки. Вывести на экран все символы, расположенные внутри этих скобок.
st = str(input('Введите строку:'))
opn = st.find('(')
cls = st.find(')')
print(opn)
if opn != -1 and cls != -1:
    insk = st[opn + 1:cls]
    print(insk)
else:
    print('Скобки не найдены')


#3 Дана строка. Вывести все слова, начинающиеся на букву "а" и слова оканчивающиеся на букву "я".
st = str(input('Введите строку:'))
words = st.split()
for word in words:
    if word.lower().startswith('а') and word.lower().endswith('я'):
        print(word)


