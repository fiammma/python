"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта
заработной платы сотрудника. Используйте в нём формулу: (выработка в
часах*ставка в час) + премия. Во время выполнения расчёта для конкретных
значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, time, salary, bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f'Заработная плата сотрудника составляет: {res}')
except ValueError:
    print('Введено некорректное значение')