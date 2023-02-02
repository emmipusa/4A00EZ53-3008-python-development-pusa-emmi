print("Anna kuukausi:")
kk = int(input())

print("Anna päivä:")

pv = int(input())

if pv == 1 and kk == 5 or pv == 6 and kk == 12:
    print("Nyt on vappu tai itsenäisyyspäivä")
else:
    print("Nyt ei ole vappu tai itsenäisyyspäivä")