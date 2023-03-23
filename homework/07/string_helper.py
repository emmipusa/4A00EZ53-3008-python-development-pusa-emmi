def csv_to_list(input):
    lista = input.split("\n")
    loppulista = []

    for i in range(len(lista)):
        muuttuja = lista[i].split(",")
        loppulista.append(muuttuja)
    return loppulista

def main():
    my_csv = "1,Jussi,Virtanen\n2,Pekka,Keinänen"
    loppulista = csv_to_list(my_csv)
    print(loppulista)

if __name__ == '__main__':
    main()