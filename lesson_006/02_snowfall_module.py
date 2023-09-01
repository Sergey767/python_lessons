# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall import create_snowfall, draw_snowfall_color, move_snowfall, numbers_reached_bottom_screen, remove_snowfall

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
n = 6
create_snowfall(n=n)
while True:
    sd.start_drawing()
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    draw_snowfall_color(color=sd.background_color)
    #  сдвинуть_снежинки()
    move_snowfall()
    #  нарисовать_снежинки_цветом(color)
    draw_snowfall_color(color=sd.COLOR_GREEN)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    if len(numbers_reached_bottom_screen()) > 0:
        remove_snowfall(numbers_snow=numbers_reached_bottom_screen())
        create_snowfall(n=n)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
