"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного
кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""

class Road:
    road_length = 0
    road_width = 0

    def __init__(self, road_length, road_width, weight, depth):
        self.road_length = road_length
        self.road_width = road_width
        self.weight = weight
        self.depth = depth

    def mass(self):
        leng = self.road_length
        wid = self.road_width
        w = self.weight
        dep = self.depth
        total = leng * wid * w * dep / 1000
        return print(f'Масса асфальта, необходимого для покрытия всей дороги\n '
                     f'{leng} м * {wid} м * {w} кг * {dep} см = ', total, 'т')


r = Road(20, 5000, 25, 5)
r.mass()
