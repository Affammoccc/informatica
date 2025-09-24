# Ho un grande file csv, conviene aprirlo usando un csv.DictReader
import csv

# RAGIONAMENTO:
#   Leggo e stampo il fil eusando un csv.DictReader che salva il file come lista di dizionari
def leggi_file(nome_file):
    australian=[]
    try:
        file=open(nome_file,"r",newline="",encoding="utf-8")
        reader=csv.DictReader(file,delimiter=";")
        for riga in reader:
            australian.append(riga)
        file.close()
    except OSError:
        print("il file non esiste")
    return australian


# RAGIONAEMTO:
#   Per ogni dizionario della lista di dizionari, inserirsco i nomi dei giocatori in una lista
#   Elimino i doppiioni della lista appena creata
#   Ordino la lista senza doppioni in ordine alfabetico
#   Dalla lista ordinata, uso enumerate per ordinarla in modo da avere una forma del tipo: 1. Nome
#   Stampo sotto forma di elenco
def giocatori(australian):
    giocatori=[]
    for dizionario in australian:
        for chiave,valore in dizionario.items():
            if chiave=="Player_1" or chiave=="Player_2":
                giocatori.append(valore)

    giocatori_senza_doppioni=[]
    for giocatore in giocatori:
        if giocatore not in giocatori_senza_doppioni:
            giocatori_senza_doppioni.append(giocatore)

    giocatori_senza_doppioni_ordinati=sorted(giocatori_senza_doppioni)
    giocatori_finale=[]
    for indice,nomi in enumerate(giocatori_senza_doppioni_ordinati, start=1):
        giocatori_finale.append((indice,nomi))  
        print(f"{indice}. {nomi}")  

    return giocatori_finale


# RAGIONAMENTO:
#   Chiedo all'utente di scegliere un numero, ossia l'indice di un nome di un giocaotre della lista
#   Per ogni indice e nome nell'elenco dei giocatori, se il numero corrisponde ad un indice dell'elenco, stampa le info richieste
def chiedi_info(australian,giocatori_finale):
    richiesta=int(input("Scegli il giocatore : "))
    for indice,nome in giocatori_finale:
        if richiesta==indice:
            for dizionario in australian:
                for valore in dizionario.values():
                    if valore == nome:
                        print(f"{dizionario["Player_1"]} vs {dizionario["Player_2"]}   {dizionario["Score"]}")

    return


def main():
    australian=leggi_file("australian.csv")
    #print(australian)

    giocatori_finale=giocatori(australian)
    #print(giocatori_finale)

    statistiche=chiedi_info(australian,giocatori_finale)
    #print(statistiche)
main()  

