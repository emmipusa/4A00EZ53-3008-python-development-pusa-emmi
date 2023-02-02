# Luodaan kilpikonna
import turtle
kilpikonna = turtle.Turtle()
kilpikonna.shape("turtle")

sade = 10
maara = 100
while sade < maara:
  kilpikonna.circle(sade)
  sade = sade * 1.5
  maara = maara * 2