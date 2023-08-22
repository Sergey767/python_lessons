# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 700)

angle = 0
length = 500


def draw_triangle(point, angle):
    vector_1 = sd.get_vector(start_point=point, angle=angle, length=500, width=4)
    vector_1.draw(sd.COLOR_PURPLE)

    vector_2 = sd.get_vector(start_point=vector_1.end_point, angle=angle + 140, length=327, width=4)
    vector_2.draw(sd.COLOR_PURPLE)

    vector_3 = sd.get_vector(start_point=vector_1.start_point, angle=angle + 40, length=327, width=4)
    vector_3.draw(sd.COLOR_PURPLE)

point_triangle = sd.get_point(150, 347)
draw_triangle(point=point_triangle, angle=angle)

def draw_wall():
    side_a = 100
    side_b = 49

    point_bottom = sd.get_point(x=200, y=50)
    point_top = sd.get_point(x=600, y=345)
    sd.rectangle(left_bottom=point_bottom, right_top=point_top, color=sd.COLOR_ORANGE, width=2)

    for j in range(50, 300, side_b):
        if j % 2 == 0:
            for i in range(0, 300, side_a):
                point_bottom = sd.get_point(i + 250, j)
                point_up = sd.get_point((i + side_a) + 250, (j + side_b))
                sd.rectangle(left_bottom=point_bottom, right_top=point_up, color=sd.COLOR_ORANGE, width=2)
        else:
            for i in range(side_a // 2 - side_a, 300, side_a):
                point_bottom = sd.get_point(i + 250, j)
                point_up = sd.get_point((i + side_a) + 250, (j + side_b))
                sd.rectangle(left_bottom=point_bottom, right_top=point_up, color=sd.COLOR_ORANGE, width=2)
