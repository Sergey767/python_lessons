# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 8, 9
# проверить для
# paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)

if envelop_x >= paper_x and envelop_y >= paper_y:
    print('Да')
elif envelop_x >= paper_y and envelop_y >= paper_x:
    print('Да')
else:
    print('Нет')

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

hole_x, hole_y = 8, 9
brick_x, brick_y, brick_z = 11, 10, 2
# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6   #да
# brick_x, brick_y, brick_z = 3, 6, 5 #да
# brick_x, brick_y, brick_z = 6, 3, 5 #да
# brick_x, brick_y, brick_z = 6, 5, 3 #да
# brick_x, brick_y, brick_z = 5, 6, 3 #да
# brick_x, brick_y, brick_z = 5, 3, 6 # да
# brick_x, brick_y, brick_z = 11, 3, 6 #да
# brick_x, brick_y, brick_z = 11, 6, 3 #да
# brick_x, brick_y, brick_z = 6, 11, 3 #да
# brick_x, brick_y, brick_z = 6, 3, 11 #да
# brick_x, brick_y, brick_z = 3, 6, 11 #да
# brick_x, brick_y, brick_z = 3, 11, 6 #да
# (просто раскоментировать нужную строку и проверить свой код)

if brick_x <= hole_x >= brick_y and brick_x <= hole_y >= brick_y:
    print('Да')
elif brick_y <= hole_x >= brick_z and brick_y <= hole_y >= brick_z:
    print('Да')
elif brick_x <= hole_x >= brick_z and brick_x <= hole_y >= brick_z:
    print('Да')
else:
    print('Нет')

