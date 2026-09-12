def fajlolvasas():
    lista = []

    with open("lakossag_2025.csv", "r", encoding="UTF-8") as celfajl:
        celfajl.readline()
        for fajl in celfajl:
            oszlop = fajl.strip().split(";")
            k = {
                "megyekod": oszlop[0],
                "telepules": oszlop[1],
                "tipus": oszlop[2],
                "ferfi": int(oszlop[3].replace(" ", "")),
                "no": int(oszlop[4].replace(" ", "")),
            }
            lista.append(k)


    return lista

def kilepes():
    print()
    print("A programból való kilépés megtörtént!")
    print()
    

def main():
    lista = fajlolvasas()
    while True:
        print()
        print("\t[1] Megye adatai - [2] Település típusok - [X] Kilépés a programból")
        print()

        valasztas = input("Kérem válasszon a fenti menüpontok közül: ").strip()

        if valasztas.upper() == "X":
            kilepes()
            break
            

        elif valasztas == "1":
            megye_adatai(lista)

        elif valasztas == "2":
            telepules_tipusok(lista)

        else:
            print()
            print("Érvénytelen parancs. Kérem próbálja újra.")

def megye_adatai(lista):
    while True:
        megyekod_input = input("Kérem adja meg a keresett megye kódját (kilépéshez - X): ").strip().upper()
        if megyekod_input == "X":
            kilepes()
            break
        else:
            telepules_szam = 0
            megye_lakossag = 0
            varosban_elo_lakossag = 0
            for t in lista:
                if t["megyekod"] == megyekod_input:
                        telepules_szam += 1
                        megye_lakossag += (t["ferfi"] + t["no"])
                        if "város" in t["tipus"] or  t["tipus"] == "vármegye székhely":
                            varosban_elo_lakossag += (t["ferfi"] + t["no"])

                        print()
                        print("----------------")
                        print(f"Települések száma a keresett megyében: {telepules_szam} db")
                        print("----------------")
                        print(f"Keresett megyében élők száma: {megye_lakossag} fő")
                        print("----------------")
                        print(f"Városban élők száma: {varosban_elo_lakossag} fő")
                        print()

        if telepules_szam == 0:
            print("------------------------------")
            print("Nem található ilyen megyekód!")

def telepules_tipusok(lista):
    tipusok = []
    for t in lista:
        if t["tipus"] not in tipusok:
            tipusok.append(t["tipus"])

    print()
    print(" - ".join(f"{i}. {elem}" for i, elem in enumerate(tipusok, start=1)))

                

main()