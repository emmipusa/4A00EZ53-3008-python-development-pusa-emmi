import random

def generate_lotto_numbers(start, end):
    if not (isinstance(start, int) and isinstance(end, int)):
        raise TypeError("Wrong value as argument")
    elif start < 1 and (end > 40 or end > 50):
        raise Exception("Number must be between 0-40")

    lotto = set()
    while len(lotto) < 7:
        lotto.add(random.randint(start, end))
    return lotto

print(generate_lotto_numbers(1, 50))