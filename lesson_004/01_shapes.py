# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

point_triangle = sd.get_point(100, 100)
length = 100
angle = 0

def draw_triangle(point, angle, length):
    vector_1 = sd.get_vector(start_point=point, angle=angle + 20, length=length)
    vector_1.draw()

    vector_2 = sd.get_vector(start_point=vector_1.end_point, angle=angle + 140, length=length)
    vector_2.draw()

    vector_3 = sd.get_vector(start_point=vector_2.end_point, angle=angle + 260, length=length)
    vector_3.draw()

point_square = sd.get_point(400, 100)
def draw_square(point, angle, length):
    vector_1 = sd.get_vector(start_point=point, angle=angle + 20, length=length)
    vector_1.draw()

    vector_2 = sd.get_vector(start_point=vector_1.end_point, angle=angle + 110, length=length)
    vector_2.draw()

    vector_3 = sd.get_vector(start_point=vector_2.end_point, angle=angle + 200, length=length)
    vector_3.draw()

    vector_4 = sd.get_vector(start_point=vector_3.end_point, angle=angle + 290, length=length)
    vector_4.draw()

point_pentagon = sd.get_point(100, 350)
def draw_pentagon(point, angle, length):
    vector_1 = sd.get_vector(start_point=point, angle=angle + 30, length=length)
    vector_1.draw()

    vector_2 = sd.get_vector(start_point=vector_1.end_point, angle=angle + 102, length=length)
    vector_2.draw()

    vector_3 = sd.get_vector(start_point=vector_2.end_point, angle=angle + 174, length=length)
    vector_3.draw()

    vector_4 = sd.get_vector(start_point=vector_3.end_point, angle=angle + 246, length=length)
    vector_4.draw()

    vector_5 = sd.get_vector(start_point=vector_4.end_point, angle=angle + 320, length=length)
    vector_5.draw()

point_hexagon = sd.get_point(400, 350)
def draw_hexagon(point, angle, length):
    vector_1 = sd.get_vector(start_point=point, angle=angle + 20, length=length)
    vector_1.draw()

    vector_2 = sd.get_vector(start_point=vector_1.end_point, angle=angle + 80, length=length)
    vector_2.draw()

    vector_3 = sd.get_vector(start_point=vector_2.end_point, angle=angle + 140, length=length)
    vector_3.draw()

    vector_4 = sd.get_vector(start_point=vector_3.end_point, angle=angle + 200, length=length)
    vector_4.draw()

    vector_5 = sd.get_vector(start_point=vector_4.end_point, angle=angle + 260, length=length)
    vector_5.draw()

    vector_6 = sd.get_vector(start_point=vector_5.end_point, angle=angle + 322, length=length)
    vector_6.draw()

draw_triangle(point=point_triangle, angle=angle, length=length)
draw_square(point=point_square, angle=angle, length=length)
draw_pentagon(point=point_pentagon, angle=angle, length=length)
draw_hexagon(point=point_hexagon, angle=angle, length=length)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

sd.pause()
