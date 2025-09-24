# leggo e apro il file come lista di dizionari
def leggi_prodotti(nome_file):
    prodotti=[]
    try: 
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split()
            
            dizionario={
                "id_prodotto":campi[0],
                "id_rivenditore":campi[1]
                                            }
            
            prodotti.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return prodotti

# apro e stampo il file come lista di dizionari
def legggi_acquisti(nome_file):
    acquisti=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split()
            dizionario={
                "id_prodotto":campi[0],
                "id_rivenditore":campi[1]
                                            }
            
            acquisti.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    
    return acquisti
    
# per ogni dizionario in prodotti metto le variabili per facilitare
# per ogni dizionario in acquisti:
#   se hanno stesso id prodotto ma id venditore diversi inserisco id rivenditore nella lista dei
#   rivenditori sospetti, poi se ho dei rivenditori sospetti stampo le varie cose
def segnalazione(prodotti,acquisti):
    
    print("elenco transazioni sospette")
    for prodotto in prodotti:
        id_prodotto=prodotto["id_prodotto"]
        rivenditore_autorizzato=prodotto["id_rivenditore"]

        rivenditori_non_autorizzati=[]
        rivenditori=set()

        for dizionario in acquisti:
            if dizionario["id_prodotto"]==id_prodotto:
                rivenditori.add(dizionario["id_rivenditore"])
                if dizionario["id_rivenditore"] != rivenditore_autorizzato:
                    rivenditori_non_autorizzati.append(dizionario["id_rivenditore"])
        
        if rivenditori_non_autorizzati:
            print(f"codice prodotto: {id_prodotto}")
            print(f"rivenditore autorizzato: {rivenditore_autorizzato}")
            print(f" lista rivenditori: {rivenditori}")
    
    return

def main():
    prodotti=leggi_prodotti("prodotti.txt")
    #print(prodotti)

    acquisti=legggi_acquisti("acquisti.txt")
    #print(acquisti)

    segnalazione(prodotti,acquisti)
main()
