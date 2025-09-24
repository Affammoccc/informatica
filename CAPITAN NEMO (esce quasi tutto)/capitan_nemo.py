#STAMPA DUE VOLTE ATLANTIDE E MANCA LA TOP NUMERO DI PETRE

# apro e stampo il file
def leggi_viaggio(nome_file):
    viaggio=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(",")
            dizionario={
                "luogo":campi[0],
                "durata":int(campi[1]),
                "passeggeri":int(campi[2])
                                                }
            viaggio.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return viaggio

# apro e stampo il file
def leggi_pietre_preziose_luoghi(nome_file):
    pietre_preziose_luoghi=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(",")
            dizionario={
                "luogo":campi[0],
                "pietra_preziosa":campi[1:]
                                                }
            pietre_preziose_luoghi.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return pietre_preziose_luoghi

# calcolo il tempo medio e il numero totale dei passeggeri       
def tempo_medio_passeggeri(viaggio):
    somma_passeggeri=0
    somma_durata=0
    for dizionario in viaggio:
        somma_passeggeri+=dizionario["passeggeri"]
        somma_durata+=dizionario["durata"]
    durata_media=somma_durata/len(viaggio)

    return durata_media,somma_passeggeri

#se un luogo compare sia in viaggio che in pietre preziose luoghi, stampa prima il luogo e poi tuttte le pietre 
def pietre_nei_luoghi(viaggio,pietre_preziose_luoghi): 
    risultato=[]
    for dizionario in viaggio:
        luoghi=dizionario["luogo"]
        for dizionario2 in pietre_preziose_luoghi:
            if dizionario2["luogo"]==luoghi:
                pietre = ", ".join(dizionario2["pietra_preziosa"])
                risultato.append(f"- {dizionario2['luogo']}: {pietre}")
    
    return risultato


def main():
    viaggio=leggi_viaggio("viaggio.txt")
    #print(viaggio)

    pietre_preziose_luoghi=leggi_pietre_preziose_luoghi("pietre_preziose_luoghi.txt") 
    #print(pietre_preziose_luoghi)

    tempo_passeggeri=tempo_medio_passeggeri(viaggio)
    print(f"Durata media dei viaggi: {tempo_passeggeri[0]}")
    print(f"Numero totale di passeggeri: {tempo_passeggeri[1]}")

    print("Tipi di pietre preziose nei luoghi visitati:")
    risultato=pietre_nei_luoghi(viaggio,pietre_preziose_luoghi)
    for riga in risultato:
        print(riga)
    
main()

    
