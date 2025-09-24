# ESCE TUTTO 

# apro e stampo il file
def leggi_testo(nome_file):
    lista= []
    try:
        file = open(nome_file,"r", encoding="utf-8")
        righe = file.readlines()
        for riga in righe:
            lista.append(riga.strip())
        file.close()
    except OSError:
        print("il file non esiste")
    return lista

# individuo gli indici delle righe che contengono le parole da eliminare.
# le righe che non le contengno rappresentano il testo censurato
def testo_censurato(lista):
    indici_cancellare = set()
    testo_censurato =[]
    for indice,riga in enumerate(lista):
        if  "bob" in riga or "arctor" in riga:
            for cancella in range(indice-2, indice+3):
                indici_cancellare.add(cancella)

    for indice,riga in enumerate(lista):
        if indice not in indici_cancellare:
            testo_censurato.append(riga)

    return testo_censurato

def main():
    testo = leggi_testo("intercettazioni.txt")
    #print(testo)

    censurato = testo_censurato(testo)
    print(censurato)
main()


            