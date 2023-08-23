# -*- coding: utf-8 -*-

import simple_draw as sd

point = sd.get_point(x=150, y=600)

def draw_sun():
    angle = 0
    for _ in range(10):
        sd.start_drawing()
        angle += 30
        vector = sd.get_vector(start_point=point, angle=angle, length=50, width=4)
        vector.draw(sd.background_color)
        sd.circle(center_position=point, radius=30, color=sd.COLOR_YELLOW, width=0)
        next_angle = angle + 30
        vector_1 = sd.get_vector(start_point=point, angle=next_angle, length=50, width=4)
        vector_1.draw(sd.COLOR_YELLOW)
        sd.finish_drawing()
        sd.sleep(0.03)