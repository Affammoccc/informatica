# apro e stampo il file della favola 
def leggi_favola(nome_file):
    lista_favola= []
    try:
        file1 = open(nome_file,"r", encoding="utf-8")
        righe = file1.readlines()
        for riga in righe:
            lista_favola.append(riga.strip())
        file1.close()
    except OSError:
        print("il file non esiste")
    return lista_favola

#leggo e apro il file dei personaggi   
def lista_personaggi(nome_file):
    lista_personaggi=[]
    try:
        file2=open(nome_file,"r",encoding="utf-8")
        righe= file2.readlines()
        for riga in righe:
            lista_personaggi.append(riga.strip())
        file2.close()
    except OSError:
        print("il file non esiste")
    
    return lista_personaggi


#lista contenente quante volte compaiono i nomi dei personaggi
def conteggio_personaggi(lista_personaggi, lista_favola):
    conteggio_personaggi = []
    for personaggio in lista_personaggi:
        contatore = 0
        for riga in lista_favola:
            if personaggio.lower() in riga.lower():
                contatore += 1
        if contatore > 0:
            conteggio_personaggi.append((personaggio, contatore))
            print(f"{personaggio}: {contatore}")
    
    return conteggio_personaggi


def main():
    favola=leggi_favola("favola.txt")
    print(favola)

    personaggi=lista_personaggi("personaggi.txt")
    print(personaggi)
    
    elenco_personaggi=conteggio_personaggi(favola,personaggi)
    print(elenco_personaggi)
main()

