# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Вода + Камень = Галечник
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Воздух + Камень = Песок
#   Огонь + Земля = Лава
#   Огонь + Камень = Металл
#   Камень + Земля = Грунт

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Steam(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Dirt(part1=self, part2=other)
        elif isinstance(other, Stone):
            return Pebble(part1=self, part2=other)
        return


class Air:

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Lightning(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Dust(part1=self, part2=other)
        elif isinstance(other, Stone):
            return Sand(part1=self, part2=other)
        return


class Storm:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Шторм'


class Fire:

    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam(part1=self, part2=other)
        elif isinstance(other, Air):
            return Lightning(part1=self, part2=other)
        elif isinstance(other, Earth):
            return Lava(part1=self, part2=other)
        elif isinstance(other, Stone):
            return Metal(part1=self, part2=other)
        return


class Steam:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пар'


class Earth:

    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt(part1=self, part2=other)
        elif isinstance(other, Air):
            return Dust(part1=self, part2=other)
        elif isinstance(other, Fire):
            return Lava(part1=self, part2=other)
        elif isinstance(other, Stone):
            return Priming(part1=self, part2=other)
        return


class Dirt:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Грязь'


class Lightning:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Молния'


class Dust:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Пыль'


class Lava:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Лава'


print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.


class Stone:
    def __str__(self):
        return 'Камень'

    def __add__(self, other):
        if isinstance(other, Water):
            return Pebble(part1=self, part2=other)
        if isinstance(other, Air):
            return Sand(part1=self, part2=other)
        if isinstance(other, Fire):
            return Metal(part1=self, part2=other)
        if isinstance(other, Earth):
            return Priming(part1=self, part2=other)
        return


class Pebble:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Галечник'


class Sand:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Песок'


class Metal:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Металл'


class Priming:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

    def __str__(self):
        return 'Грунт'


print(Water(), '+', Stone(), '=', Water() + Stone())
print(Air(), '+', Stone(), '=', Air() + Stone())
print(Fire(), '+', Stone(), '=', Fire() + Stone())
print(Stone(), '+', Earth(), '=', Stone() + Earth())
print(Earth(), '+', Stone(), '=', Earth() + Stone())