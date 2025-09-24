import csv
# apro e stampo il file
def leggi_file(nome_file):
    cani=[]
    try:
        file=open(nome_file,"r",newline="",encoding="utf-8")
        reader=csv.DictReader(file, delimiter=",")
        for riga in reader:
            cani.append(riga)
        file.close()
    except OSError:
        print("il file non esiste")
    return cani 

def ordine(cani):
    dizionario={}
    for cane in cani:
        #tiro fuori le chiavi del dizionario della lista di dizionari, piu comodo e pulito dopo
        razza=cane["Breed"]
        livello=cane["Training Level"]
        punteggio=float(cane["Obedience Score"])

        #controllo se la razza e il livello sono gia presenti nel dizionario appena creato
        # se la razza non e presente la aggiungi (il valore associato alla razza e un dizionario contenente il livello e il punteggio associato ad esso che e contenuto in una lista)
        
        if razza not in dizionario:
            dizionario[razza]={}
        if livello not in dizionario[razza]:
            dizionario[razza][livello]=[] # accedo alla lista dei punteggi di tutti i cani di quella razza e di quel livello 
        dizionario[razza][livello].append(punteggio)

        for razza in dizionario:
            print(f"Razza: {razza}")
            for livello in dizionario[razza]:
                punteggi = dizionario[razza][livello]
                if len(punteggi) > 0:
                    media = sum(punteggi) / len(punteggi)
                    print(f"Livello {livello}: media {media:.2f}")
                else:
                    print(f"Livello {livello}: nessun punteggio disponibile")
    return dizionario
    
def main():
    lista_cani=leggi_file("cani.csv")
    #print(lista_cani)
    punteggi=ordine(lista_cani)
main()
