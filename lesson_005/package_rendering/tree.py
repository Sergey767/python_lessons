# -*- coding: utf-8 -*-

import simple_draw as sd

def draw_branches(point, angle, length):
    vector = sd.get_vector(start_point=point, angle=angle, length=length)
    if length < 7:
        vector.draw(sd.COLOR_GREEN)
        return
    vector.draw()
    next_point = vector.end_point
    right_angle = angle - 30
    left_angle = angle + 30
    next_length = length * .75
    draw_branches(point=next_point, angle=right_angle, length=next_length)
    draw_branches(point=next_point, angle=left_angle, length=next_length)