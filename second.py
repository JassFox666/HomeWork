from unicodedata import digit

number = int(input("Введіть 4-х значне число: "))

digit1 = number // 1000
digit2 = (number // 100) % 10
digit3 = (number // 10) % 10
digit4 = number % 10

# Вивід числа в стовпчик
print(digit1)
print(digit2)
print(digit3)
print(digit4)