
# apro e stampo il file come lista di dizionari
def leggi_partecipanti(nome_file):
    partecipanti=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(":")
            dizionario={
                "numero_pettorale":campi[0],
                "nome":campi[1]
                                            }
            partecipanti.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return partecipanti

# apro e stampo il file come lista di dizionari
def leggi_penalita(nome_file):
    penalita=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(":")
            dizionario={
                "numero_pettorale":campi[0],
                "penalita":campi[1:]
                                            }
            penalita.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return penalita

# creo una lista di dizionari con i nomi dei partecipanti e la somma della penalita
# per ogni partecipante, per ogni penalita, se il numero di pettorale dei due dizionari e uguale
# sommo le penalita ed inserisco in un dizionario nuovo il nome del partecipante e la somma delle penalita per ogni partecipante
def classifica(penalita,partecipanti):
    lista_classifica=[]
    for partecipante in partecipanti:
        for pen in penalita:
            if partecipante["numero_pettorale"]==pen["numero_pettorale"]:
                somma_penalita=0
                for p in pen["penalita"]:
                    somma_penalita+=int(p)
                dizionario={
                    "nome":partecipante["nome"],
                    "somma_penalita":somma_penalita
                                            }
                lista_classifica.append(dizionario)
    # ordino la lista in base alla somma delle penalita crescente
    lista_classifica.sort(key=lambda x: x["somma_penalita"])
    print("Classifica:")
    # stampo la classifica in bella
    for elemento in lista_classifica:
        print(f"{elemento['nome']:<20} {elemento['somma_penalita']}  penalita")

    return lista_classifica

def main():
    partecipanti=leggi_partecipanti("partecipanti.txt")
    #print(partecipanti)

    penalita=leggi_penalita("penalita.txt")
    #print(penalita)
    
    lista_classifica=classifica(penalita,partecipanti)
    #print(lista_classifica)
main()

