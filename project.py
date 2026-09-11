lista=[]

with open("lakossag_2025.csv", "r", encoding="UTF-8") as celfajl:
    celfajl.readline()  
    for fajl in celfajl:
        oszlop = fajl.strip().split(";")
        k = {
            "megyekod" : oszlop[0],
            "telepules" : oszlop[1],
            "tipus" : oszlop[2],
            "ferfi" : oszlop[3].replace(" ", ""),
            "no" : oszlop[4].replace(" ", ""),
        }
        lista.append(k)


while True:
    print("[1] Megye adatai")
    print("[2] Település típusai")
    print("[X] Kilépés a programból")

    valasztas = input("Kérem válasszon a fenti menüpontok közül: ")

    if valasztas.upper() == "X":
        print("Kilépés a programból...")
        break

    if valasztas == "1":
        megye_kod = input("Kérem adja meg a megye kódját: ")
        for megye in lista:
            if megye_kod in lista["megyekod"]:
                print(f"Település: {megye['telepules']}, Típus: {megye['tipus']}, Férfiak száma: {megye['ferfi']}, Nők száma: {megye['no']}")