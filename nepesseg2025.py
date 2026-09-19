import os
from colorama import Fore, Back, Style
import string

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
    print(Fore.GREEN + "Visszatérés a főmenübe...")
    print(Style.RESET_ALL)
    

def main():
    lista = fajlolvasas()
    while True:
        print()
        print(Style.DIM + "A program a 2025-ös népességadatokat tartalmazza. A program segítségével meg tudja nézni a megyék, települések és típusok adatait." + Style.RESET_ALL)
        print()
        print(Back.BLUE + "\t[1] Megye adatai - [2] Település típusok - [X] Kilépés a programból" + Style.RESET_ALL)
        print()

        valasztas = input("Kérem válasszon a fenti menüpontok közül: ").strip()

        if valasztas.upper() == "X":
            print()
            print(Fore.GREEN + "A prgogramból való kilépés megtörtént." + Style.RESET_ALL)
            break
            

        elif valasztas == "1":
            megye_adatai(lista)

        elif valasztas == "2":
            telepules_tipusok(lista)

        else:
            print()
            print(Fore.RED + "Érvénytelen parancs. Kérem próbálja újra." + Style.RESET_ALL)


def megye_adatai(lista):
    megyekod_input = input("Kérem adja meg a keresett megye kódját (kilépéshez - X): ").strip().upper()
    if megyekod_input == "X":
        kilepes()
        
    else:
        telepules_szam = 0
        megye_lakossag = 0
        varosban_elo_lakossag = 0

        for t in lista:
            if t["megyekod"] == megyekod_input:
                telepules_szam += 1
                megye_lakossag += (t["ferfi"] + t["no"])
                if "város" in t["tipus"] or t["tipus"] == "vármegye székhely":
                    varosban_elo_lakossag += (t["ferfi"] + t["no"])

        
        if telepules_szam == 0:
            print()
            print(Fore.RED + "A megadott megyekód nem található. Kérem próbálja újra." + Style.RESET_ALL)
            print()
            megye_adatai(lista)
        else:
            print()
            print("----------------")
            print(f"Települések száma a keresett megyében: {telepules_szam} db")
            print("----------------")
            print(f"Keresett megyében élők száma: {megye_lakossag} fő")
            print("----------------")
            print(f"Városban élők száma: {varosban_elo_lakossag} fő")
            print()

            megye_adatai(lista)
            
                               
def telepules_tipusok(lista):
    def betuk():
        betuk_keszlet = []
        for b in string.ascii_lowercase:
            betuk_keszlet.append(b)
        return betuk_keszlet
            
    betuk_listaja = betuk()


    tipusok = []
    for t in lista:
        if t["tipus"] not in [tipus["telepules_tipusa"] for tipus in tipusok]:
            tipus = {
                    "betujel": betuk_listaja[0],
                    "telepules_tipusa": t["tipus"],
            }
            betuk_listaja.remove(betuk_listaja[0])
            tipusok.append(tipus)

    print()
    print(Fore.BLUE + "Település típusok:" + Style.RESET_ALL)
    for tipus in tipusok:
        print(f"[{tipus['betujel']}] {tipus['telepules_tipusa']}")
        

    print()
    valasztott_tipus = input("Kérem adja meg a keresett település típusát (kilépéshez - X): ").strip().lower()
    print()
    if valasztott_tipus == "x":
        kilepes()
        return
    else:
        keresett_tipus = [tipus["telepules_tipusa"] for tipus in tipusok if tipus["betujel"] == valasztott_tipus][0]

        if valasztott_tipus not in [tipus["betujel"] for tipus in tipusok]:
            print(Fore.RED + "Érvénytelen parancs. Kérem próbálja újra." + Style.RESET_ALL)
            print()
            telepules_tipusok(lista)
            return

        if keresett_tipus is not None:
            for telepules in lista:
                if telepules["tipus"] == keresett_tipus:
                    lakossag = telepules["ferfi"] + telepules["no"]
                    print(
                        f"{telepules['telepules']} - {telepules['tipus']} - {lakossag} fő")

            telepules_tipusok(lista)
            

main()