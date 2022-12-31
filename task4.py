# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


num = int(input('Введите целое положительное число: '))
biggest_digit = 0
while num > 0:
    last_digit = num % 10
    if last_digit > biggest_digit:
        biggest_digit = last_digit
    num //= 10
print('Самая большая цифра в числе: ', biggest_digit)
