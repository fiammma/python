# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.



def divis():
    try:
        num1 = int(input('Введите делимое: '))
        num2 = int(input('Введите делитель: '))
        if num2 != 0:
            return num1 / num2
        else:
            print("Делить на 0 нельзя!")
    except ValueError:
        return 'Введено некорректное значение'
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'

print(f'Division result {divis()}')

