def pocet_suborov():
    while True:
        pocet = input("Zadaj počet súborov: ")
        try:
            return int(pocet)
        except ValueError:
            print("Musíš zadať číselnú hodnotu!")


pocet_slov = []

with open("basnicka.txt", encoding="utf-8") as subor:
    for riadok in subor:
        pocet_slov += riadok.split()

for i in range(pocet_suborov()):
    subor = open("Súbor" + str(i + 1) + ".txt", mode="w", encoding="utf-8")
    subor.write(pocet_slov[i])
    subor.close()
