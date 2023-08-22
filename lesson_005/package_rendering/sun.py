# -*- coding: utf-8 -*-

import simple_draw as sd

def draw_sun():
    point = sd.get_point(x=150, y=550)
    color = sd.COLOR_YELLOW

    sd.circle(center_position=point, radius=50, color=color, width=0)

    sd.line(start_point=sd.get_point(x=150, y=600),  end_point=sd.get_point(x=150, y=650), color=sd.COLOR_YELLOW, width=4)
    sd.line(start_point=sd.get_point(x=170, y=570), end_point=sd.get_point(x=220, y=625), color=sd.COLOR_YELLOW, width=4)
    sd.line(start_point=sd.get_point(x=190, y=550), end_point=sd.get_point(x=245, y=558), color=sd.COLOR_YELLOW, width=4)
    sd.line(start_point=sd.get_point(x=170, y=520), end_point=sd.get_point(x=230, y=500), color=sd.COLOR_YELLOW, width=4)
    sd.line(start_point=sd.get_point(x=150, y=500), end_point=sd.get_point(x=150, y=450), color=sd.COLOR_YELLOW, width=4)
    sd.line(start_point=sd.get_point(x=120, y=520), end_point=sd.get_point(x=70, y=500), color=sd.COLOR_YELLOW, width=4)
    sd.line(start_point=sd.get_point(x=100, y=550), end_point=sd.get_point(x=45, y=558), color=sd.COLOR_YELLOW, width=4)
    sd.line(start_point=sd.get_point(x=120, y=570), end_point=sd.get_point(x=70, y=625), color=sd.COLOR_YELLOW, width=4)