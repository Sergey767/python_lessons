# -*- coding: utf-8 -*-

import simple_draw as sd


n = 25

x_list = []
y_list = []
length_list = []

def add_lists():
    y_points = sd.random_number(a=70, b=90)
    x_points = sd.random_number(a=30, b=200)
    x_list.append(x_points)
    y_list.append(y_points)
    lengths = sd.random_number(a=10, b=30)
    length_list.append(lengths)

def draw_snowfall():
    while True:
        for i in range(n):
            add_lists()
            snowflake_length = length_list[i]
            point = sd.get_point(x=x_list[i], y=y_list[i])
            sd.snowflake(center=point, length=snowflake_length, color=sd.COLOR_WHITE)
        if sd.user_want_exit():
            break
