import random

hidden_numbers = ''
indices_cows = []
indices_bulls = []


def make_number():
    global hidden_numbers
    hidden_numbers = random.sample("1234567890", 4)
    while hidden_numbers[0] == '0':
        random.shuffle(hidden_numbers)
    return int(''.join(hidden_numbers))


def check_number(numbers):
    global indices_cows, indices_bulls
    quantity_cows_bulls = dict()
    indices_cows = []
    indices_bulls = []

    for index in range(len(hidden_numbers)):
        if numbers[index] == hidden_numbers[index]:
            indices_bulls.append(index)
        elif hidden_numbers[index] in numbers:
            indices_cows.append(index)
        quantity_cows_bulls['bulls'] = len(indices_bulls)
        quantity_cows_bulls['cows'] = len(indices_cows)
    return quantity_cows_bulls.values()

