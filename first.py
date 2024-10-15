# Запит на введення числа користувачем
from unicodedata import digit

number = int(input("Введіть 5-ти значне число: "))

# Отримання кожної цифри числа
digit1 = number % 10
digit2 = (number // 10) % 10
digit3 = (number // 100) % 10
digit4 = (number // 1000) % 10
digit5 = (number // 10000) % 10

# Формування зворотнього числа заданого користувачем
reversed_number = digit1 * 10000 + digit2 * 1000 + digit3 * 100 + digit4 * 10 + digit5

# Вивід зворотнього числа
print ("Зворотнє число: ", reversed_number)