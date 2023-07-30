# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def draw_smile(x, y, color):
    point = sd.get_point(x, y)
    color_ears = sd.COLOR_DARK_YELLOW

    sd.circle(center_position=point, radius=60, color=color, width=2)
    sd.line(sd.get_point(x - 20, y - 5), sd.get_point(x - 10, y - 20), color, width=2)
    sd.line(sd.get_point(x - 10, y - 20), sd.get_point(x + 10, y - 20), color, width=2)
    sd.line(sd.get_point(x + 10, y - 20), sd.get_point(x + 20, y - 5), color, width=2)

    eyes_left_point = sd.get_point(x - 15, y + 20)
    eyes_right_point = sd.get_point(x + 15, y + 20)
    sd.circle(center_position=eyes_left_point, radius=5, color=color, width=2)
    sd.circle(center_position=eyes_right_point, radius=5, color=color, width=2)

    sd.line(sd.get_point(x - 15, y + 55), sd.get_point(x - 18, y + 72), color, width=2)
    sd.line(sd.get_point(x - 2, y + 58), sd.get_point(x - 2, y + 75), color, width=2)
    sd.line(sd.get_point(x + 15, y + 55), sd.get_point(x + 18, y + 72), color, width=2)

    sd.line(sd.get_point(x - 35, y + 50), sd.get_point(x - 35, y + 70), color_ears, width=2)
    sd.line(sd.get_point(x - 30, y + 52), sd.get_point(x - 35, y + 70), color_ears, width=2)

    sd.line(sd.get_point(x + 35, y + 50), sd.get_point(x + 30, y + 70), color_ears, width=2)
    sd.line(sd.get_point(x + 26, y + 50), sd.get_point(x + 31, y + 70), color_ears, width=2)

for i in range(10):
    random_point = sd.random_point()
    x = random_point.x
    y = random_point.y
    color = sd.COLOR_GREEN
    draw_smile(x=x, y=y, color=color)

sd.pause()

