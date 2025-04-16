#ESCE TUTTO

# apri e stampo il file

def leggi_testo(nome_file):
    lista=[]
    try:
        file = open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(",")
            dizionario={
                "data":campi[0],
                "ora":campi[1],
                "paese":campi[2],
                "forma":campi[3],
                "durata":campi[4],
                "descrizione":campi[5]
                                        }
            lista.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return lista


# avvistamento piu lungo descrizione (durata, forma)
def avvistamento_lungo(lista):
    avvistamento=[]
    for dizionario in lista:
        avvistamento.append(int(dizionario["durata"]))
    avvistamento_maggiore=max(avvistamento)
    for dizionario in lista:
        if avvistamento_maggiore==int(dizionario["durata"]):
            print(f"Avvistamento di durata piu lunga: {dizionario["descrizione"]} (Durata:{avvistamento_maggiore} secondi, Forma:{dizionario["forma"]})")
    return avvistamento_maggiore

#dizionario dove la chiave e lo stato e il valore e il numero di avvistamenti
#.values() indico solo i valori del dizionario
#.keys() indico solo le chiavi del dizionario
#.items() indico la coppia chiave-valore del dizionario 
def paese(lista):
    stati={}
    for dizionario in lista:
        if dizionario["paese"] in stati.keys():
            stati[dizionario["paese"]] += 1
        else:
            stati[dizionario["paese"]] = 1
    
    return stati

# stato con maggior numero di avvistamenti
def avvistamento_max_stato(stati):
    valori= stati.values()
    massimo=max(valori)
    for chiave,valore in stati.items():
        if massimo == valore:
            print(f"Lo stato con maggior avvistamenti e: {chiave}")

def main():
    testo = leggi_testo("ufo.csv")
    #print(testo)
    
    avvistamento_piu_lungo=avvistamento_lungo(testo)
    #print(avvistamento_piu_lungo)
    
    elenco_avvistamenti=paese(testo)
    #print(elenco_avvistamenti)

    massimo=avvistamento_max_stato(elenco_avvistamenti)
    #print(massimo)
main()
