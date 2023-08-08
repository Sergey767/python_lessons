# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

angle = 20
length = 100

figure_user = int(input(
    "1 - треугольник\n2 - квадрат\n3 - пятиугольник\n4 - шестиугольник\n\nВведите желаемую фигуру: "))

def draw_figure(count_sides, angle, point, length):
    for side in range(count_sides):
        vector = sd.get_vector(start_point=point, angle=angle, length=length)
        vector.draw()
        if count_sides == 3:
            angle += 120
        elif count_sides == 4:
            angle += 90
        elif count_sides == 5:
            angle += 72.2
        elif count_sides == 6:
            angle += 60.1
        point = vector.end_point

def draw_triangle(point, angle, length):
    count_sides = 3
    draw_figure(count_sides=count_sides, angle=angle, point=point, length=length)

def draw_square(point, angle, length):
    count_sides = 4
    draw_figure(count_sides=count_sides, angle=angle, point=point, length=length)

def draw_pentagon(point, angle, length):
    count_sides = 5
    draw_figure(count_sides=count_sides, angle=angle, point=point, length=length)

def draw_hexagon(point, angle, length):
    count_sides = 6
    draw_figure(count_sides=count_sides, angle=angle, point=point, length=length)

def select_figure(figure_user):
    point_figure = sd.get_point(300, 250)

    if figure_user == 1:
        draw_triangle(point=point_figure, angle=angle, length=length)
    elif figure_user == 2:
        draw_square(point=point_figure, angle=angle, length=length)
    elif figure_user == 3:
        draw_pentagon(point=point_figure, angle=angle, length=length)
    elif figure_user == 4:
        draw_hexagon(point=point_figure, angle=angle, length=length)
    else:
        if 1 > figure_user or figure_user > 4:
            print('Вы ввели некорректный номер!')
            figure_user = int(input('Введите желаемую фигуру: '))
            select_figure(figure_user=figure_user)

select_figure(figure_user=figure_user)

sd.pause()
