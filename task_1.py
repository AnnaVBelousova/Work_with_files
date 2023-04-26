# Задание 2.

# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).

# Значения данных атрибутов должны передаваться при создании экземпляра класса.

# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.

# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
# Массу и толщину сделать публичными атрибутами.
# Проверить работу метода.

# Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т

class NonNegative:

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Значение должно быть числом")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    width = NonNegative()
    length = NonNegative()
    mass = 25
    thickness = 0.05

    def __init__(self, width, length):  # mass, thickness):
        self.length = length
        self.width = width

    def counting_mass(self):
        total_mass = self.length * self.width * Road.mass * Road.thickness
        return total_mass


width = 5
length = 3

mass_of_material = Road(width, length)  # , mass, thickness)
print(f'{mass_of_material.counting_mass()} кг')
