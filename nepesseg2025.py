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
    print("Visszatérés a főmenübe...")
    print()
    

def main():
    lista = fajlolvasas()
    while True:
        print()
        print("\t[1] Megye adatai - [2] Település típusok - [X] Kilépés a programból")
        print()

        valasztas = input("Kérem válasszon a fenti menüpontok közül: ").strip()

        if valasztas.upper() == "X":
            print()
            print("Kilépés a programból...")
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
                        print(f"Település neve: {t['telepules']}")
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
    while True:
        print()
        print("\t[a] község - [b] város - [c] nagyközség - [d] fővárosi kerület - [e] vármegye székhely - [f] vármegyei jogú város")
        print()
        valasztott_tipus = input("Kérem adja meg a keresett település típusát (kilépéshez - X): ").strip().lower()
        print()
        if valasztott_tipus == "x":
            kilepes()
            break
            
        tipusok = {
            "a": "község",
            "b": "város",
            "c": "nagyközség",
            "d": "fővárosi kerület",
            "e": "vármegye székhely",
            "f": "vármegyei jogú város",
        }

        keresett_tipus = tipusok.get(valasztott_tipus)

        if valasztott_tipus not in ["a", "b", "c", "d", "e", "f"]:
            print("Érvénytelen parancs. Kérem próbálja újra.")
            kilepes()
            break

        if keresett_tipus is not None:
            for telepules in lista:
                if telepules["tipus"] == keresett_tipus:
                    lakossag = telepules["ferfi"] + telepules["no"]
                    print(
                        f"{telepules['telepules']} - {telepules['tipus']} - {lakossag} fő")






                

main()