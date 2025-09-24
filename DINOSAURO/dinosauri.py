# NON CAPISCO COME FARLO

numero_carte=30
punteggio={
    "Rosso":5,
    "Giallo":3,
    "Verde":1
                }

#apro e stampo il file con READLINES()
def leggi_mazzo(nome_file):
    mazzo=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        righe=file.readlines()
        for riga in righe:
            mazzo.append(riga.strip())
        file.close()
    except OSError:
        print("il file non esiste")
    return mazzo

# distribuisco le carte del mazzo 
# in ogni lista ci sono le carte ricevute da ogni giocatore
def distribuzione(mazzo):
    carte1=[]
    carte2=[]
    for i in range(0,len(mazzo),2):
        carte1.append(mazzo[i])
        carte2.append(mazzo[i+1])
    return carte1,carte2

def partita(carte1,carte2):
    punti1=0
    punti2=0

    while len(carte1)>0 and len(carte2)>0: #finche ho delle carte
        c1=carte1.pop(0) #toglie la prima carta dalla lista 
        c2=carte2.pop(0) #toglie la prima carta dalla lista 
    

    
def main():
    mazzo=leggi_mazzo("mazzo.txt")
    #print(mazzo)

    (carte1,carte2)=distribuzione(mazzo)
    #print((carte1,carte2))

    (punti1,punti2)=partita(carte1,carte2)
    print(punti1,punti2)



main()
