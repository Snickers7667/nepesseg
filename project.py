lista=[]

with open("lakossag_2025.csv", "r", encoding="UTF-8") as celfajl:
    for fajl in celfajl:
        oszlop = fajl.strip().split(";")
        k = {
            "megyekod" : oszlop[0],
            "telepules" : oszlop[1],
            "tipus" : oszlop[2],
            "ferfi" : oszlop[3],
            "no" : oszlop[4]
        }
        lista.append(k)

print(lista)