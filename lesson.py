#Дана строка, содержащая русскоязычный текст. Найти количество слов, начинающихся с буквы "е".
'''t = 'елозить ерошить спать идти быть жить есть ехать ехидничать ева евгений евдокия евклид евника евразия евровидение евронет европа европарламент египет екатеринбург'
w = t.split()
k = 0
for i in w:
    if i.startswith('е') or i.startswith('Е'):
        k += 1
print(k)'''

#В строке удалить символ точку (.) и подсчитать количество удаленных символов.
s = 'fdsfds. sa.fd 433.32..3'
count = 0
for i in range(len(s)):
    if s[i] == '.':
        st = s.replace('.','',)
        count += 1
print(count)