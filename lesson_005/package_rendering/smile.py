# -*- coding: utf-8 -*-

import simple_draw as sd

def draw_smile(x, y, color):
    point = sd.get_point(x, y)
    color_ears = sd.COLOR_DARK_YELLOW
    radius = 0

    sd.circle(center_position=point, radius=60, color=color, width=2)
    sd.line(sd.get_point(x - 20, y - 5), sd.get_point(x - 10, y - 20), color, width=2)
    sd.line(sd.get_point(x - 10, y - 20), sd.get_point(x + 10, y - 20), color, width=2)
    sd.line(sd.get_point(x + 10, y - 20), sd.get_point(x + 20, y - 5), color, width=2)

    sd.line(sd.get_point(x - 15, y + 55), sd.get_point(x - 18, y + 72), color, width=2)
    sd.line(sd.get_point(x - 2, y + 58), sd.get_point(x - 2, y + 75), color, width=2)
    sd.line(sd.get_point(x + 15, y + 55), sd.get_point(x + 18, y + 72), color, width=2)

    sd.line(sd.get_point(x - 35, y + 50), sd.get_point(x - 35, y + 70), color_ears, width=2)
    sd.line(sd.get_point(x - 30, y + 52), sd.get_point(x - 35, y + 70), color_ears, width=2)

    sd.line(sd.get_point(x + 35, y + 50), sd.get_point(x + 30, y + 70), color_ears, width=2)
    sd.line(sd.get_point(x + 26, y + 50), sd.get_point(x + 31, y + 70), color_ears, width=2)

    point_body = sd.get_point(x=750, y=90)
    vector_body = sd.get_vector(start_point=point_body, angle=90, length=80)
    vector_body.draw(sd.COLOR_GREEN)
    point_hand = vector_body.end_point
    vector_left_hand = sd.get_vector(start_point=point_hand, angle=-30, length=50)
    vector_left_hand.draw(sd.COLOR_GREEN)
    vector_right_hand = sd.get_vector(start_point=point_hand, angle=210, length=50)
    vector_right_hand.draw(sd.COLOR_GREEN)
    point_foot = vector_body.start_point
    vector_left_foot = sd.get_vector(start_point=point_foot, angle=-50, length=50)
    vector_left_foot.draw(sd.COLOR_GREEN)
    vector_right_foot = sd.get_vector(start_point=point_foot, angle=230, length=50)
    vector_right_foot.draw(sd.COLOR_GREEN)

    for _ in range(10):
        sd.start_drawing()
        eyes_left_point = sd.get_point(x - 15, y + 20)
        eyes_right_point = sd.get_point(x + 15, y + 20)
        sd.circle(center_position=eyes_left_point, radius=radius, color=sd.background_color, width=2)
        sd.circle(center_position=eyes_right_point, radius=radius, color=sd.background_color, width=2)
        radius += 5
        if radius > 20:
            radius = 5
        sd.circle(center_position=eyes_left_point, radius=radius, color=color, width=2)
        sd.circle(center_position=eyes_right_point, radius=radius, color=color, width=2)
        sd.finish_drawing()
        sd.sleep(0.05)

