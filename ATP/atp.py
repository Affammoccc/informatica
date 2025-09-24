import random
# apro e stmapo il file
def leggi_qualificatori(nome_file):
    qualificatori=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(",")
            dizionario={
                "numero_testa":int(campi[0]),
                "cognome":campi[1]
                                               }
            qualificatori.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return qualificatori

def sorteggio_gironi(qualificatori):
    verde=[]
    verde.append(qualificatori[0])
    rosso=[]
    rosso.append(qualificatori[1])

    coppie=qualificatori[2:]
    for coppia in coppie:
        primo=random.choice(coppia)
        seconda= coppia[0] if primo==coppia[1] else coppia[1]
    verde.append(primo)
    rosso.append(seconda)

    verde.sort(key=lambda x: x["numero_testa"])
    rosso.sort(key=lambda x: x["numero_testa"])

    return verde,rosso




def main():
    qualificatori=leggi_qualificatori("qualificatori.txt")
    print(qualificatori)
    
    girone_rosso,girone_verde=sorteggio_gironi(qualificatori)
    print(girone_rosso,girone_verde)
main()


            