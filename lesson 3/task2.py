# 2. Выполнить функцию, которая принимает несколько параметров, описывающих
# данные пользователя: имя, фамилия, год рождения, город проживания, email,
# телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.


def pers_data(firstname, lastname, year_of_birth, city, email, phone):
    return print(f'Имя: {firstname}, Фамилия: {lastname}, '
                 f'Год рождения: {year_of_birth}, Город проживания: {city}, '
                 f'Email: {email}, Телефон: {phone}')

pers_data(
    firstname=input('Имя: '),
    lastname=input('Фамилия: '),
    year_of_birth=input('Год Рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '),
)
