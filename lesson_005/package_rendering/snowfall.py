# -*- coding: utf-8 -*-

import simple_draw as sd

n = 25

x_list = []
y_list = []
length_list = []

def add_lists():
    y_points = sd.random_number(a=200, b=300)
    x_points = sd.random_number(a=30, b=150)
    x_list.append(x_points)
    y_list.append(y_points)
    lengths = sd.random_number(a=10, b=30)
    length_list.append(lengths)

def draw_snowfall():
    for i in range(n):
        add_lists()
        sd.start_drawing()
        snowflake_length = length_list[i]
        point = sd.get_point(x=x_list[i], y=y_list[i])
        sd.snowflake(center=point, length=snowflake_length, color=sd.background_color)
        y_list[i] -= 10
        next_point = sd.get_point(x=x_list[i], y=y_list[i])
        sd.snowflake(center=next_point, length=snowflake_length, color=sd.COLOR_WHITE)
        if y_list[i] < 60:
            y_list[i] = 300
            continue
        sd.finish_drawing()
        sd.sleep(0.05)

