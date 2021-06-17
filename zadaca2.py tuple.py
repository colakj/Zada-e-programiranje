def nazivi_ocjena(bodovi):
    if bodovi <50:
        return "Nedovoljan"
    if bodovi < 65:
        return "Dovoljan"
    elif bodovi < 80:
        return "Dobar"
    elif bodovi < 90:
        return "Vrlo dobar"
    else:
        return "Izvrstan"

from csv import reader

dat= open('rezultati.csv', 'r') 
csv_reader = reader(dat)
rezultati = list(map(tuple, csv_reader))


novi_rezultati=[]
for ime, prezime, bodovi in rezultati:
    novi_rezultati.append((prezime,ime,bodovi))
novi_rezultati.sort()
print(novi_rezultati)

rez_ocjena=[]

for student in novi_rezultati:
    rjecnik={}
    rjecnik["prezime"]=student[0]
    rjecnik["ime"]=student[1]
    rjecnik["ocjene"]=nazivi_ocjena(int(student[2]))
    rez_ocjena.append(rjecnik)
    

rezultati_ocjena=[]
for student in rez_ocjena:
    rezultati_ocjena.append((student["prezime"], student["ime"], student["ocjene"]))

print(rezultati_ocjena)
