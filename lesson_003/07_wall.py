# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

side_a = 100
side_b = 49

for j in range(1, 800, side_b):
    if j % 2 == 0:
        for i in range(0, 800, side_a):
            point_bottom = sd.get_point(i, j)
            point_up = sd.get_point(i + side_a, j + side_b)
            sd.rectangle(left_bottom=point_bottom, right_top=point_up, color=sd.COLOR_ORANGE, width=2)
    else:
        for i in range(side_a // 2 - side_a, 800, side_a):
            point_bottom = sd.get_point(i, j)
            point_up = sd.get_point(i + side_a, j + side_b)
            sd.rectangle(left_bottom=point_bottom, right_top=point_up, color=sd.COLOR_ORANGE, width=2)

sd.pause()
