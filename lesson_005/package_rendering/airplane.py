# -*- coding: utf-8 -*-

import simple_draw as sd

def draw_wings(angle_1, angle_2, length, point):
    vector_1 = sd.get_vector(start_point=point, angle=0, length=56, width=2)
    vector_1.draw(sd.COLOR_ORANGE)

    vector_2 = sd.get_vector(start_point=vector_1.end_point, angle=angle_1, length=100, width=2)
    vector_2.draw(sd.COLOR_ORANGE)

    vector_3 = sd.get_vector(start_point=vector_2.end_point, angle=angle_2, length=length, width=2)
    vector_3.draw(sd.COLOR_ORANGE)

def draw_airplane():
    point_top = sd.get_point(x=900, y=550)
    point_bottom = sd.get_point(x=630, y=498)
    sd.rectangle(left_bottom=point_bottom, right_top=point_top, color=sd.COLOR_ORANGE, width=2)

    point_wing = sd.get_point(x=750, y=550)
    draw_wings(angle_1=140, angle_2=290, length=65, point=point_wing)
    point_right_wing = sd.get_point(x=750, y=500)
    draw_wings(angle_1=-140, angle_2=-290, length=65, point=point_right_wing)

    point_tail_top = sd.get_point(x=630, y=570)
    point_tail_bottom = sd.get_point(x=610, y=480)
    sd.rectangle(left_bottom=point_tail_bottom, right_top=point_tail_top, color=sd.COLOR_ORANGE, width=2)








