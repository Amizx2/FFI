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

#Домашняя работа 5
#Три точки заданы своими координатами X(x1, x2), Y(y1, y2) и Z(z1, z2). Найти и напечатать координаты точки, для которой угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный. Вычисления оформить в виде процедуры.
import math

def min_angle(x1, x2, y1, y2, z1, z2):
    angle_x = math.atan2(x2, x1)
    angle_y = math.atan2(y2, y1)
    angle_z = math.atan2(z2, z1)

    min_angle = min(angle_x, angle_y, angle_z)

    if min_angle == angle_x:
        return x1, x2
    elif min_angle == angle_y:
        return y1, y2
    else:
        return z1, z2
x1 = float(input('Введите координату x1 для точки X: '))
x2 = float(input('Введите координату x2 для точки X: '))
y1 = float(input('Введите координату y1 для точки Y: '))
y2 = float(input('Введите координату y2 для точки Y: '))
z1 = float(input('Введите координату z1 для точки Z: '))
z2 = float(input('Введите координату z2 для точки Z: '))
result_x, result_y = min_angle(x1, x2, y1, y2, z1, z2)
print('Координаты точки с минимальным углом', result_x, result_y)


n = int(input('Введите колличество чисел: '))
print('Числа, которые являются палиндромами')
for num in range(1, n + 1):
    bin_num = bin(num)[2:]
    if bin_num == bin_num[::-1]:
        print(num)





