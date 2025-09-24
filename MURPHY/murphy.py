# apro e stampo il file
def leggi_massime(nome_file):
    frasi={}
    frase=""
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            riga=riga.strip()
            massima= file.readlines()
            while massima != "":
                frase += massima + " "
                massima = file.readlines()
                
        frasi[riga]= frase
        frase =" "
        file.close()
    except OSError:
        print("il file non esiste")
    return frasi

def leggi_argomenti(nome_file):
    lista_argomenti=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        righe=file.readlines()
        for riga in righe:
            lista_argomenti.append(riga.strip())
        file.close()
    except OSError:
        print("il file non esiste")
    return lista_argomenti

def main():
    contenuto=leggi_massime("leggi_murphy.txt")
    print(contenuto)

    argomenti=leggi_argomenti("argomenti.txt")
    print(argomenti)
    
main()
