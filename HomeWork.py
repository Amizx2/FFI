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