def team_novy():
    nazov_teamu = input('Zadaj nazov teamu: ')
    if nazov_teamu in zoznam.keys():
        print('Team už je v zozname!')
        main()        
    skore = []
    tip = input('Počet gólov: ')
    skore.append(tip)
    zoznam[nazov_teamu] = skore

def team_vypis():
    for nazov_teamu in sorted(zoznam.keys()):
        print("{}".format(nazov_teamu), end=' ')
        print(' ')

def vypis_podla_golov():
    for nazov_teamu, skore in sorted(zoznam.items(), key=lambda podla: podla[1]):
        print("{}".format(nazov_teamu), end=' ')
        for i in range(len(skore)):
            print('{}'.format(skore[i]))

zoznam = {}

def main():
    while True:
        print(' ')
        print('Vyber položku z ponuky:')
        print('Novy team..........1')
        print('Výpis teamov.......2')
        print('Výpis podľa gólov..3')
        print('Koniec.............0')
        volba = int(input())
        if volba == 1:
            team_novy()
        elif volba == 2:
            team_vypis()
        elif volba == 3:
            vypis_podla_golov()
        else:
            break

if __name__ == "__main__":
    main()