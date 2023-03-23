import random
salainen_luku = random.randint(0, 10)
kayttajan_syote = -1
a = 0

while kayttajan_syote != salainen_luku:
    print("Arvaa salainen luku (0 - 10)")
    kayttajan_syote = int( input() )
    a =  a + 1

print('Oikein! Arvasit', a, 'kertaa')