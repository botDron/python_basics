"""
Задание 2.

Реализовать проект расчета суммарного расхода ткани на производство одежды.

Единственный класс этого проекта — одежда (класс Clothes).

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57

Два класса: абстрактный и Clothes
"""

from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def common(self):
        pass


class Clothes(AbstractClass):

    def __init__(self, name, size):
        self.name = name
        self.size = float(size)

    @property
    def common(self):
        if self.name == 'Пальто':
            return round(self.size / 6.5 + 0.5, 2)
        if self.name == 'Костюм':
            return round(self.size * 2 + 0.3, 2)
        return 'неправильный расчет'


p = Clothes('Пальто', 56)
c = Clothes('Костюм', 175)

print(f'Расход ткани на пальто = {p.common}')
print(f'Расход ткани на костюм = {c.common}')
print(f'Общий расход ткани = {p.common + c.common}')