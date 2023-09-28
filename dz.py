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
