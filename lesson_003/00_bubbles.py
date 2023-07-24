# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(500, 300)
radius = 65

for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def draw_bubble(point, step):
    radius = 65
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius)

point = sd.get_point(600, 400)
draw_bubble(point, 15)

# Нарисовать 10 пузырьков в ряд

for x in range(100, 1010, 100):
    point = sd.get_point(x, 200)
    draw_bubble(point=point, step=10)

# Нарисовать три ряда по 10 пузырьков

for y in range(100, 310, 100):
    for x in range(100, 1010, 100):
        point = sd.get_point(x, y)
        draw_bubble(point=point, step=10)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()
