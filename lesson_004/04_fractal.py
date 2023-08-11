# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1600, 800)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# point_0 = sd.get_point(300, 5)
# point_1 = sd.get_point(300, 155)
# angle = 90
# length = 150

# def draw_branches(point, angle, length):
#     vector = sd.get_vector(start_point=point, angle=angle, length=length)
#     vector.draw()
#     return vector.end_point
#
# next_point = draw_branches(point=point_0, angle=angle, length=length)
# right_angle = angle - 30
# left_angle = angle + 30
# next_length = length * .75
# next_point = draw_branches(point=next_point, angle=right_angle, length=next_length)
# next_point = draw_branches(point=point_1, angle=left_angle, length=next_length)

# def draw_branches(point, angle, length):
#     if length < 10:
#         return
#     vector = sd.get_vector(start_point=point, angle=angle, length=length)
#     vector.draw()
#     next_point = vector.end_point
#     right_angle = angle - 30
#     left_angle = angle + 30
#     next_length = length * .75
#     draw_branches(point=next_point, angle=right_angle, length=next_length)
#     draw_branches(point=next_point, angle=left_angle, length=next_length)
#
# root_point = sd.get_point(300, 30)
# draw_branches(point=root_point, angle=90, length=100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()
angle_percent = 30 * .4 + 30
length_percent = .75 * .2 + .75

def draw_branches(point, angle, length):
    if length < 10:
        return
    vector = sd.get_vector(start_point=point, angle=angle, length=length)
    vector.draw()
    next_point = vector.end_point
    right_angle = angle - sd.random_number(a=30, b=angle_percent)
    left_angle = angle + sd.random_number(a=30, b=angle_percent)
    next_length = length * random.uniform(.75, length_percent)
    draw_branches(point=next_point, angle=right_angle, length=next_length)
    draw_branches(point=next_point, angle=left_angle, length=next_length)

root_point = sd.get_point(300, 30)
draw_branches(point=root_point, angle=90, length=100)

sd.pause()


