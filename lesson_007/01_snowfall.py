# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

class Snowflake:
    def __init__(self):
        self.y = sd.random_number(a=500, b=600)
        self.x = sd.random_number(a=100, b=1000)
        self.point = None

    def clear_previous_picture(self):
        sd.clear_screen()

    def move(self):
        self.y -= 10
        self.x += 10

    def draw(self, color=sd.COLOR_WHITE):
        self.point = sd.get_point(self.x, self.y)
        sd.snowflake(center=self.point, length=50, color=color)

    def can_fall(self):
        return self.y


flake = Snowflake()

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:


def get_flakes(count):
    snowflakes = []
    while len(snowflakes) < count:
        snowflake = Snowflake()
        snowflakes.append(snowflake)
    return snowflakes


def get_fallen_flakes():
    fallen_flakes_count = 0
    for _ in flakes:
        if flake.y < 0:
            fallen_flakes_count += 1
    return fallen_flakes_count


def append_flakes(count):
    for _ in range(count):
        flakes.append(Snowflake())


flakes = get_flakes(count=20)  # создать список снежинок


while True:
    for flake in flakes:
        sd.start_drawing()
        flake.draw(color=sd.background_color)
        flake.move()
        flake.draw()
        sd.finish_drawing()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
