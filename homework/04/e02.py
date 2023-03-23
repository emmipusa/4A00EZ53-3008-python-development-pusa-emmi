import random

lotto = set()

while len(lotto) < 7:
    lotto.add(random.randint(1, 40))

print(lotto)