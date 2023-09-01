# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)

y_list = []
x_list = []
length_list = []
snowflake_length = []
point = sd.get_point(x=0, y=0)
snowflake_color = 0
numbers_snowflake = []

snowflakes_count = 0


def create_snowfall(n):
    global snowflakes_count
    snowflakes_count = n
    for i in range(n):
        y_points = sd.random_number(a=500, b=600)
        x_points = sd.random_number(a=100, b=1000)
        x_list.append(x_points)
        y_list.append(y_points)
        lengths = sd.random_number(a=10, b=100)
        length_list.append(lengths)


def draw_snowfall_color(color):
    global point, snowflake_length, snowflake_color
    for i in range(snowflakes_count):
        point = sd.get_point(x=x_list[i], y=y_list[i])
        snowflake_length = length_list[i]
        snowflake_color = color
        sd.snowflake(center=point, length=snowflake_length, color=snowflake_color)


def move_snowfall():
    for i in range(snowflakes_count):
        y_list[i] -= 10
        x_list[i] += sd.random_number(-10, 10)
        next_point = sd.get_point(x=x_list[i], y=y_list[i])
        sd.snowflake(center=next_point, length=snowflake_length, color=snowflake_color)


def numbers_reached_bottom_screen():
    for number in range(0, snowflakes_count):
        if y_list[number] < 0:
            y_list[number] = 600
            numbers_snowflake.append(number)
            print(numbers_snowflake)
    return numbers_snowflake


def remove_snowfall(numbers_snow):
    for number in reversed(range(len(numbers_snowflake))):
        del numbers_snow[number]

