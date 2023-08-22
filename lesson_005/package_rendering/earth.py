# -*- coding: utf-8 -*-

import simple_draw as sd

def draw_earth():
    left_bottom = sd.get_point(x=0, y=0)
    right_bottom = sd.get_point(x=1200, y=50)
    sd.rectangle(left_bottom=left_bottom, right_top=right_bottom, color=sd.COLOR_DARK_YELLOW)




