import random

hidden_numbers = ''


def make_number():
    global hidden_numbers
    hidden_numbers = random.sample("1234567890", 4)
    while hidden_numbers[0] == '0':
        random.shuffle(hidden_numbers)
    return int(''.join(hidden_numbers))


def check_number(user_numbers):
    quantity_cows_bulls = dict()
    indices_cows = []
    indices_bulls = []

    for index in range(len(hidden_numbers)):
        if user_numbers[index] == hidden_numbers[index]:
            indices_bulls.append(index)
        elif hidden_numbers[index] in user_numbers:
            indices_cows.append(index)
        quantity_cows_bulls['bulls'] = len(indices_bulls)
        quantity_cows_bulls['cows'] = len(indices_cows)
    return quantity_cows_bulls.values()

