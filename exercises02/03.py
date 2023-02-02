name = 'Matti'
bmi = 25.112312

f'Hello {name}, you have bmi = {bmi}'
print(len(name))
print(name[0], name[4])

matti = 'matti'
x = matti.capitalize()
print(x)
# muuttaa ensimmäisen kirjaimen isoksi

text = 'kahvi auttaa koodaamisessa, keitän kahvia'
x = text.count("kahvi")
print(x)
# laskee kuinka monesti annettua sanaa on käytetty

txt = "afdjkla"
x = txt.find("j")
print(x)
# etsii annetun arvon ja kertoo sen sijainnin (ensimmäinen kirjain 0, toinen kirjain 1...)

txt = ":)"
mytable = txt.maketrans(")", "(")
print(txt.translate(mytable))
# muuttaa toivotun arvon toiseksi toivotuksi arvoksi

txt = "asddljl..."
x = txt.strip(".")
print(x)
# poistaa kaikki annetut arvot

txt = ("jaa", "joo", "juu")
x = "!".join(txt)
print(x)
# liittää annetulla arvolla kaikki osat yhteen

txt = "1a"
x = txt.isnumeric()
print(x)
# jos kaikki merkit ovat numeroita, kone antaa True ja jos on yhtään muita merkkejä, kone antaa False

nimi1 = str(input())
nimi2 = str(input())

print("give a:", nimi1)
print("give b:", nimi2)

print("value", nimi1, "in memory address", id(nimi1))
print("value", nimi2, "in memory address", id(nimi2))

if nimi1 == nimi2:
    print(True)
else:
    print(False)

a = id(nimi1)
b = id(nimi2)

if a is b:
    print(True)
else:
    print(False)
