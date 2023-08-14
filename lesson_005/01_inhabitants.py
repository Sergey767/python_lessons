# -*- coding: utf-8 -*-
import room_1
from room_2 import folks
# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

folks1 = ''
folks2 = ''

for name in room_1.folks:
    folks1 += name + ', '
print(f'В комнате room_1 живут:', folks1)

for name in folks:
    folks2 += name + ', '
print(f'В комнате room_2 живут:', folks2)


