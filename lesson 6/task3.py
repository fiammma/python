"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров.
"""

class Worker:
    # атрибуты класса
    name = "Петр"      # имя
    surname = "Петров"   # фамилия
    position = "Аналитик"  # должность
    profit = 140000     # оклад
    bonus = 20000       # премия
    _income = {"Оклад": profit,
               "Премия": bonus
               }    # доход (защищенный атрибут)
    total_profit = 0    # доход с учетом премии


class Position(Worker):
    def get_full_name(self):
        return "{} \"{} {}\"".format(self.position, self.name, self.surname)

    def get_full_profit(self):
        self.total_profit = self.profit + self.bonus
        return ', доход с учётом премии составляет: {}'\
            .format(self.total_profit)

w = Worker()
print(w.name)       # проверка атрибутов класса
print(w.surname)    # проверка атрибутов класса
print(w.position)   # проверка атрибутов класса
print(w.profit)     # проверка атрибутов класса

p = Position()      # экземпляр класа Position
print("\nСводная информация по сотруднику: ")
print(p.get_full_name() + str(p.get_full_profit()) + " " + str(w._income))
