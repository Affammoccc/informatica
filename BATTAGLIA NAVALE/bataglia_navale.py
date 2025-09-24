# apro e stampo il file come una matrice
def read_data(nome_file):
    matrice=[]
    try:
        file=open(nome_file,'r',encoding='utf-8')
        for riga in file:
            riga_matrice=[]
            elementi_riga=riga.strip().split(",")
            for elemento in elementi_riga:
                riga_matrice.append(elemento)
            matrice.append(riga_matrice)
        file.close()
    except OSError:
        print("il file non esiste")
    return matrice

# apro e stampo il file come lista di tutple dove ogni tupla contuiene le 
# coordinate della mossa [esempio: (x,y)]
def leggi_mosse(nome_file):
    mosse=[]
    try:
        file=open(nome_file,'r',encoding='utf-8')
        for riga in file:
            campi=riga.strip().split(",")
            x=campi[0]
            y=int(campi[1])
            mosse.append((x,y))
        file.close()
    except OSError:
        print("il file non esiste")
    return mosse

def stampa_matrice(matrice):
    lettere="ABCDEFGHIJ"
    print(())
def main():
    print("Giocatore 1")
    file1 = input("Inserire il nome del file con le navi:")
    disposizione1 = read_data(file1)
    print(disposizione1)

    print("Giocatore 2")
    file2= input("Inserire il nome del file con le navi:")
    disposizione2 = read_data(file2)
    print(disposizione2)

    mosse=leggi_mosse("mosse.txt")
    print(mosse)
    
main()
