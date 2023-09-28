#1 Написать программу, которая будет делить введенные пользователем два вещественных числа и выводить результат на экран, сообщая об ошибке в случае деления на ноль.
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if num2 == 0:
    print("Ошибка: Деление на ноль невозможно.")
else:
    result = num1 / num2
    print("Результат:", result)

#2 Рассчитать стоимость покупки с учетом скидки в 35%, которая предоставляется покупателю, если сумма покупки превышает 20 у.е. Сумму покупки ввести с клавиатуры, а результаты округлить до сотых (копейки, центы и т.д.). Вывести на экран итоговую стоимость и размер предоставленной скидки.
total = float(input("Введите сумму покупки: "))
if total > 20:
    sale = total * 0.65
    print("Сумма со скидкой: ", (round(sale, 2)))
else:
    print("Сумма недостаточна для скидки: ", total)

#3 Напишите скрипт, который по введенному пользователем числу от 1 до 12, будет выводить на экран сообщение в виде названия месяца и времени года. Если пользователь введет недопустимое число, программа должна выдавать сообщение об ошибке.

month_number = int(input("Введите число от 1 до 12: "))

months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

seasons = ["Зима", "Весна", "Лето", "Осень"]

if 1 <= month_number <= 12:
        month = months[month_number - 1]
        season = seasons[(month_number % 12) // 3]
        print("Вы выбрали месяц",month , "и это",season)
else:
    print("Ошибка: Введите число от 1 до 12.")


#ДОП ЗАДАНИЕ
#Представьте вещественные числа 275.4, 0.0032 и 3.45 в коде Python в стандартном виде. Напомним, что в математике число в такой форме имеет вид a*10**n, где 1 ≤ a < 10, а n – целое число. Например, для числа 0.123 получим 1.23*10-1
num1 = 275.4
num2 = 0.0032
num3 = 3.45
def StandardForm(num):
    stepen = 0
    if num != 0:
        while abs(num) >= 10:
            num = num / 10
            stepen += 1
        while abs(num) < 1:
            num = num * 10
            stepen -= 1

    formatted_num = f"{num:.2f} * 10^{stepen}"
    return formatted_num
format_num1 = StandardForm(num1)
format_num2 = StandardForm(num2)
format_num3 = StandardForm(num3)

print(format_num1)
print(format_num2)
print(format_num3)


