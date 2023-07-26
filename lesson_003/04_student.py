# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

percent = 3 / 100
academic_year = 10
number_month = 0
percent_expenses = 0
high_expenses = expenses

while number_month < academic_year:
    number_month += 1
    if number_month == 1:
        continue
    percent_expenses = (high_expenses * percent) + expenses
    high_expenses += percent_expenses
amount_money = high_expenses - (educational_grant * 10)
print(f'Студенту надо попросить {amount_money} рублей')




