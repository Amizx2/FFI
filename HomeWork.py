#Дополнительное задание Welcome. In this kata, you are asked to square every digit of a number and concatenate them.For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)Note: The function accepts an integer and returns an integer.
num = str(input('Enter a number: ' ))
result_num = ''
for x in num:
    result_num += str(int(x) ** 2)
print('Result: ', result_num)

#small варинат
num = input('Enter a number: ')
print(''.join(str(int(x) ** 2) for x in num))

#1 Вычислить и вывести на экран сумму кубов натуральных чисел от 1 до n включительно. Верхний предел должен вводиться с клавиатуры и не должен превышать числа 100.
n = int(input("Введите верхний предел (не более 100): "))
if n > 100:
    print("Верхний предел не должен превышать 100..")
else:
    summ = 0
    for i in range(1, n + 1):
        summ += i ** 3
    print(f"Сумма кубов натуральных чисел от 1 до {n} равна {summ}.")


#2 Выведите на экран таблицу умножения чисел от одного до девяти.
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end='\t')
    print()
