# Задание №1
# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


num = int(input('Введите число в десятичной системе: '))
print(f'Встроенная функция hex -> {hex(num)}')


def hex(number: int) -> str:
    if not number:
        return '0x0'
    result = ''
    hex_letters = list('0123456789abcdef')
    while number > 0:
        result = hex_letters[number % 16] + result
        number //= 16
    return '0x' + result


print(f'Собственная функция hex -> {hex(num)}')




# Задание №2
# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем
# и знаменателем. Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

import re
import math
import fractions

fracs = list(map(int,
                 re.split(" |/", input('Введите две дроби формата "a/b" через пробел: '))))

sum_div = fracs[0] * fracs[3] + fracs[2] * fracs[1]
sum_denom = fracs[1] * fracs[3]
sum_nod = math.gcd(sum_div, sum_denom)
if sum_denom / sum_nod != 1:
    sum_fracs = str(int(sum_div / sum_nod)) + '/' + str(int(sum_denom / sum_nod))
else:
    sum_fracs = str(int(sum_div / sum_nod))

prod_div = fracs[0] * fracs[2]
prod_denom = fracs[1] * fracs[3]
prod_nod = math.gcd(prod_div, prod_denom)
if prod_denom / prod_nod != 1:
    prod_fracs = str(int(prod_div / prod_nod)) + '/' + str(int(prod_denom / prod_nod))
else:
    prod_fracs = str(int(prod_div / prod_nod))


print(sum_fracs, prod_fracs)

f1 = fractions.Fraction(fracs[0], fracs[1])
f2 = fractions.Fraction(fracs[2], fracs[3])
print(f1 + f2, f1 * f2)


