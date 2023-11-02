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

#5 При помощи библиотеки Pillow в директории circles (создайте ее во время выполнения функции) нарисуйте и сохраните 100 кругов радиусом 300 пикселей случайных цветов в формате jpg на белом фоне (каждый круг - отдельный файл). Для этого напишите функцию circles_generator(num_of_circles=100).
#python3 -m pip install --upgrade pip
#python3 -m pip install --upgrade Pillow
from PIL import Image, ImageDraw
import os
import random

def circles_generator(num_of_circles=100):
    if not os.path.exists('circles'):
        os.makedirs('circles')

    for i in range(1, num_of_circles + 1):
        image = Image.new('RGB', (600, 600), 'white')
        draw = ImageDraw.Draw(image)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x = random.randint(0, 300)
        y = random.randint(0, 300)
        draw.ellipse((x, y, x + 300, y + 300), fill=color, outline='black')
        file_name = os.path.join('circles', f'circle_{i}.jpg')
        image.save(file_name, 'JPEG')


circles_generator(100)

