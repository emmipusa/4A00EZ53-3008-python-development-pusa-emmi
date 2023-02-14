import random

def generate_lotto_numbers(min = 0, max = 40, amount = 7):
    if not (isinstance(min, int) and isinstance(max, int)):
        raise TypeError("Wrong value as argument")
    elif min < 1 and max > 40:
        raise Exception("Number must be between 0-40")
    elif max < amount:
        raise Exception("Max is more than amount")

    lotto = set()
    while len(lotto) < amount:
            lotto.add(random.randint(min, max))
    return lotto

print(generate_lotto_numbers())