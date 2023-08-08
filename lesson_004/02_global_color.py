# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

angle = 20
length = 100

color = 0

colors = {1 : {'color' : sd.COLOR_RED}, 2 : {'color' : sd.COLOR_ORANGE}, 3 : {'color' : sd.COLOR_YELLOW},
          4 : {'color' : sd.COLOR_GREEN}, 5 : {'color' : sd.COLOR_CYAN}, 6 : {'color' : sd.COLOR_BLUE},
          7 : {'color' : sd.COLOR_PURPLE}}

color_user = int(input(
    "1 - red\n2 - orange\n3 - yellow\n4 - green\n5 = cyan\n6 - blue\n7 - purple\n\nВведите желаемый цвет: "))

if color_user in colors:
    color = colors[color_user]['color']
else:
    while 1 > color_user or color_user > 7:
        print('Вы ввели некорректный номер!')
        color_user = int(input('Введите желаемый цвет: '))
    if color_user in colors:
        color = colors[color_user]['color']


def draw_figure(count_sides, angle, point, length, color):
    for side in range(count_sides):
        vector = sd.get_vector(start_point=point, angle=angle, length=length)
        vector.draw(color=color)
        if count_sides == 3:
            angle += 120
        elif count_sides == 4:
            angle += 90
        elif count_sides == 5:
            angle += 72.2
        elif count_sides == 6:
            angle += 60.1
        point = vector.end_point

def draw_triangle(point, angle, length, color):
    count_sides = 3
    draw_figure(count_sides=count_sides, angle=angle, point=point, length=length, color=color)

def draw_square(point, angle, length, color):
    count_sides = 4
    draw_figure(count_sides=count_sides, angle=angle, point=point, length=length, color=color)

def draw_pentagon(point, angle, length, color):
    count_sides = 5
    draw_figure(count_sides=count_sides, angle=angle, point=point, length=length, color=color)

def draw_hexagon(point, angle, length, color):
    count_sides = 6
    draw_figure(count_sides=count_sides, angle=angle, point=point, length=length, color=color)

point_triangle = sd.get_point(100, 100)
draw_triangle(point=point_triangle, angle=angle, length=length, color=color)

point_square = sd.get_point(400, 100)
draw_square(point=point_square, angle=angle, length=length, color=color)

point_pentagon = sd.get_point(100, 350)
draw_pentagon(point=point_pentagon, angle=angle, length=length, color=color)

point_hexagon = sd.get_point(400, 350)
draw_hexagon(point=point_hexagon, angle=angle, length=length, color=color)

sd.pause()
