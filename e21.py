#!/bin/python3

print("Anna suorakaiteen korkeus")
korkeus = int( input() )
print("Anna suorakaiteen leveys")
leveys = int( input() )
x = 0
while x < leveys:
  
  sarake = 0
  while sarake < korkeus or sarake < leveys:
    # Tulosta "X" ilman enter painallusta
    # Huom! tämä vaatii python3 - tulkin joka asetettu päälle rivillä 1
    print("X", end='')
    sarake = sarake + 1
  
  # Tulosta enter
  print()
  x = x + 1