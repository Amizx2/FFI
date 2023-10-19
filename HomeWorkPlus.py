#ДОП ЗАДАНИЕ 1
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

#Дополнительное задание 2 Welcome. In this kata, you are asked to square every digit of a number and concatenate them.For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)Note: The function accepts an integer and returns an integer.
num = str(input('Enter a number: ' ))
result_num = ''
for x in num:
    result_num += str(int(x) ** 2)
print('Result: ', result_num)

#small варинат
num = input('Enter a number: ')
print(''.join(str(int(x) ** 2) for x in num))

#Доп.задание 3: The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

def GenerateWords(word):
    word = word.lower()
    result = ''
    for sym in word:
        if word.count(sym) > 1:
            result += ')'
        else:
            result += '('
    return result
OrigWord = (input('Введите строку: '))

#Доп. задание 4 не понимаю как делать на Coffee script