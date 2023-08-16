# -*- coding: utf-8 -*-
from district.central_street.house1.room1 import folks as folks_1
from district.soviet_street.house1.room1 import folks as folks_2
from room_1 import folks as folks_3
from room_2 import folks as folks_4


# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

folks = ', '.join(folks_1 + folks_2 + folks_3 + folks_4)

print(folks)




