# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1300, 800)

# нарисовать ветку дерева из точки (300, 5) вертикально вверх длиной 100

point_0 = sd.get_point(300, 5)

# vector_1 = sd.get_vector(start_point=point_0, angle=90, length=100)
# vector_1.draw()

# сделать функцию рисования ветки из заданной точки,
# заданной длины, с заданным наклоном
length = 150
angle = 90

# def draw_branch(point, angle, length):
#     vector_1 = sd.get_vector(start_point=point, angle=angle, length=length)
#     vector_1.draw()
#     return vector_1.end_point
#
# next_point = draw_branch(point=point_0, angle=angle, length=length)
# next_angle = angle - 30
# next_length = length * .75
# next_point = draw_branch(point=next_point, angle=next_angle, length=next_length)
# next_angle -= 30
# next_length *= .75
# next_point = draw_branch(point=next_point, angle=next_angle, length=next_length)
# next_angle -= 30
# next_length *= .75
# next_point = draw_branch(point=next_point, angle=next_angle, length=next_length)

# написать цикл рисования ветвей с постоянным уменьшением длины на 25% и отклонением на 30 градусов

# next_angle = angle
# next_length = length
# next_point = point_0
#
# while next_length > 1:
#     next_point = draw_branch(point=next_point, angle=next_angle, length=next_length)
#     next_angle -= 30
#     next_length *= .75

# сделать функцию branch рекурсивной

def draw_branch_recursive(point, angle, length, delta):
    if length < 1:
        return
    vector_1 = sd.get_vector(start_point=point, angle=angle, length=length)
    vector_1.draw()
    next_point = vector_1.end_point
    next_angle = angle - delta
    next_length = length * .75
    draw_branch_recursive(point=next_point, angle=next_angle, length=next_length, delta=delta)

for delta in range(0, 51, 10):
    draw_branch_recursive(point=point_0, angle=angle, length=length, delta=delta)
for delta in range(-50, 1, 10):
    draw_branch_recursive(point=point_0, angle=angle, length=length, delta=delta)


sd.pause()

