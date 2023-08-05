# -*- coding: utf-8 -*-

# pip install simple_draw

import simple_draw as sd

# нарисовать треугольник из точки (300, 300) с длиной стороны 200
length = 200
point = sd.get_point(200, 400)

# vector_1 = sd.get_vector(start_point=point, angle=0, length=length, width=3)
# vector_1.draw()
#
# vector_2 = sd.get_vector(start_point=vector_1.end_point, angle=120, length=length, width=3)
# vector_2.draw()
#
# vector_3 = sd.get_vector(start_point=vector_2.end_point, angle=240, length=length, width=3)
# vector_3.draw()


# определить функцию рисования треугольника из заданной точки с заданным наклоном

# def draw_triangle(point, color, angle=0):
#     vector_1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     vector_1.draw(color)
#
#     vector_2 = sd.get_vector(start_point=vector_1.end_point, angle=angle + 120, length=length, width=3)
#     vector_2.draw(color)
#
#     vector_3 = sd.get_vector(start_point=vector_2.end_point, angle=angle + 240, length=length, width=3)
#     vector_3.draw(color)
#
# for angle in range(0, 361, 30):
#     draw_triangle(point=point, color=sd.COLOR_RED, angle=angle)

sd.pause()

