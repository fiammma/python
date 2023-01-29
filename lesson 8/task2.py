"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""

class Division_zero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    dividend = int(input('Введите делимое: '))
    divisor = int(input('Введите делитель: '))
    if not divisor:
        raise Division_zero('Делить на ноль нельзя!')
    print(f'Результат {dividend/divisor}')

except ValueError:
    print('Вы ввели некорректныое значение')
except Division_zero as error:
    print(error)
