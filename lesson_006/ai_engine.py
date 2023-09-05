import random
from mastermind_engine import make_number

computer_numbers = ''
indices_cows = []
indices_bulls = []
hidden_numbers = str(make_number())


def issue_variant_number():
    global computer_numbers
    computer_numbers = random.sample('1234567890', 4)
    while computer_numbers[0] == '0':
        random.shuffle(computer_numbers)
    return int(''.join(computer_numbers))


def get_number_cows_bulls(numbers):
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




