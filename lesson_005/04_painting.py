# -*- coding: utf-8 -*-
import simple_draw as sd

from package_rendering.earth import draw_earth
from package_rendering.brick_house import draw_wall
from package_rendering.rainbow import draw_rainbow
from package_rendering.smile import draw_smile
from package_rendering.tree import draw_branches
from package_rendering.snowfall import draw_snowfall
from package_rendering.sun import draw_sun
from package_rendering.airplane import draw_airplane

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

draw_wall()
draw_rainbow()
draw_sun()
draw_airplane()
draw_smile(x=750, y=230, color=sd.COLOR_GREEN)
root_point = sd.get_point(1000, 30)
draw_branches(point=root_point, angle=90, length=80)
draw_earth()
draw_snowfall()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

sd.pause()
