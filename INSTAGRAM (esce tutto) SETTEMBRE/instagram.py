# ESCE TUTTO

# Apro e leggo il file csv come lista di dizionari (apertura standard)
def leggi_testo(nome_file):
    lista = []
    try:
        file = open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi = riga.rstrip().split(";") #rstrip toglie spazi e \n a dx, split toglie il ;
            dizionario = {
                "nome_account" : campi[0],
                "nome_reale" : campi[1],
                "followers" : float(campi[2]),
                "professione" : campi[3]
                                                }
            lista.append(dizionario) 
        file.close()
    except OSError: 
        print("il file non esiste")
    return lista


# Dalla lista di dizionari devo:
#   Creare un dizionario contenente chiave e valore di professione e followers dove i followers
#   della stessa professione si sommano.
#   Ordinare in modo decrescente in base alla somma dei followers e stampare i primi 5

# RAGIONAMENTO
#   Per ogni dizionario della lista di dizionari fatta prima, se il valore associato alla chiave
#   professione non e mai comparso nel dizionario appena creato, ci associo il valore associato 
#   alla chiave followers. Se il valore associato alla chiave professione e gia comparso, sommo i
#   followers a quelli gia esistenti.
def dizionario_professione_somma_followers(lista):
    diz = {}

    for dizionario in lista:
        if dizionario["professione"] not in diz.keys():
            diz[dizionario["professione"]] = dizionario["followers"]
        else:
            diz[dizionario["professione"]] += dizionario["followers"]
 
    dizonario_ordinato = dict(sorted(diz.items(), key=lambda item : item[1], reverse=True)) # ordina decrescentemente in base al valore dei followers
    top_5 = dict(list(dizonario_ordinato.items()) [:5]) #estraggo le prime 5 coppie professione-followers
    for chiave,valore in top_5.items():
        print(f"{chiave:<23} {valore:.1f} M") #:<23 crea 23 spazi a sx di chiave, :.1f arrotonda i valori di valore ad 1 cifra dopo la virgola
    
    return top_5
 
def main():
    testo=leggi_testo("instagram.csv")
    #print(testo)
    classifica=dizionario_professione_somma_followers(testo)
    #print(classifica)
main()
    

