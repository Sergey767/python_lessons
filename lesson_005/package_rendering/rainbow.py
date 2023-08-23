# -*- coding: utf-8 -*-

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

def draw_rainbow():
    point = sd.get_point(350, 30)
    radius = 900

    for color in rainbow_colors:
        sd.start_drawing()
        radius += 15
        sd.circle(center_position=point, radius=radius, width=20, color=sd.background_color)
        sd.circle(center_position=point, radius=radius, width=20, color=color)
        if radius > 990:
            radius = 900
            continue
        sd.finish_drawing()
        sd.sleep(0.05)