# -*- coding: utf-8 -*-
from district.central_street.house1.room1 import folks as folks_1
from district.soviet_street.house1.room1 import folks as folks_2

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

folks = ', '.join(folks_1 + folks_2)

print(folks)




