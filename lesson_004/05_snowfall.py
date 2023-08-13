# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

n = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

x_list = []
y_list = []
length_list = []

def add_lists():
    y_points = sd.random_number(a=500, b=600)
    x_points = sd.random_number(a=100, b=1000)
    x_list.append(x_points)
    y_list.append(y_points)
    lengths = sd.random_number(a=10, b=100)
    length_list.append(lengths)

while True:
    for i in range(n):
        add_lists()
        sd.start_drawing()
        snowflake_length = length_list[i]
        point = sd.get_point(x=x_list[i], y=y_list[i])
        sd.snowflake(center=point, length=snowflake_length, color=sd.background_color)
        y_list[i] -= 10
        x_list[i] += sd.random_number(-10, 10)
        next_point = sd.get_point(x=x_list[i], y=y_list[i])
        sd.snowflake(center=next_point, length=snowflake_length, color=sd.COLOR_WHITE)
        if y_list[i] < 100:
            y_list[i] = 600
            continue
        sd.finish_drawing()
        sd.sleep(0.01)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


