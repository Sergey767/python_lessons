# -*- coding: utf-8 -*-
import my_burger

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

print('Рецепт двойного чизбургера:')
my_burger.add_bun()
my_burger.add_cutlet()
my_burger.add_cheese()
my_burger.add_onion()
my_burger.add_cutlet()
my_burger.add_cheese()
my_burger.add_cucumber()
my_burger.add_ketchup()
my_burger.add_mustard()
my_burger.add_salt()
my_burger.add_bun()

print('Рецепт бургера "Гранд Де Люкс":')
my_burger.add_bun()
my_burger.add_cheese()
my_burger.add_cutlet()
my_burger.add_cheese()
my_burger.add_tomato()
my_burger.add_salad()
my_burger.add_cucumber()
my_burger.add_ketchup()
my_burger.add_onion()
my_burger.add_mayonnaise()
my_burger.add_mustard()
my_burger.add_salt()
my_burger.add_bun()

