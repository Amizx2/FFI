import os

#1 Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число). Протестируем функцию на файле article.txt со следующим содержимым:

n = int(input('Введите колличество строк: '))
if n <= 0:
    print('Количество строк должно быть положительным целым числом.')
def read_last(lines, file):
    with open(file, "r", encoding='utf-8') as f:
        all_lines = f.readlines()
        num_lines = min(lines, len(all_lines))
        for line in all_lines[-num_lines:]:
            print(line, end='')

read_last(n, "D:/article.txt")

#2 Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).


