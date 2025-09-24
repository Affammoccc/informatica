# INCOMPLETO MA MANCA SOLO COME FARLO TORNARE INDIETRO 

# apro e leggo il file
def leggi_testo(nome_file):
    labirinto={}
    matrice=[]
    labirinto["matrice"]=matrice
    try:
        file=open(nome_file,"r",encoding="utf-8")
        contatore_riga=0
        for riga in file:
            if contatore_riga==0:
                campi=riga.strip().split(",")
                inizio={"x":int(campi[0]),"y":int(campi[1])}
                labirinto["inizio"]=inizio
            elif contatore_riga==1:
                campi=riga.strip().split(",")
                fine={"x":int(campi[0]),"y":int(campi[1])}
                labirinto["fine"]=fine
            else:
                riga_matrice=[]
                elementi_riga=riga.strip("/n")
                for elemento in elementi_riga:
                    riga_matrice.append(elemento)
                matrice.append(riga_matrice)
            contatore_riga+=1
    except OSError:
        print("il file non esiste")
    return labirinto

# lista con i movimenti (decidio io l'ordine da rispettare)
def movimento(labirinto):
    elenco_movimenti=[]
    inizio = labirinto["inizio"]
    x_inizio = inizio["x"]
    y_inizio = inizio["y"]

    fine=labirinto["fine"]
    x_fine = fine["x"]
    y_fine = fine["y"]

    attuale_x = x_inizio
    attuale_y = y_inizio

    matrice = labirinto["matrice"]

    while x_fine != attuale_x and y_fine != attuale_y:
        casella_su = matrice[attuale_x-1][attuale_y]
        casella_dx = matrice[attuale_x][attuale_y+1]
        casella_giu = matrice[attuale_x+1][attuale_y]
        casella_sx = matrice[attuale_x][attuale_y-1]

        if casella_su == " ":
            attuale_x -= 1
            elenco_movimenti.append((attuale_x,attuale_y))
        elif casella_dx == " ":
            attuale_y += 1
            elenco_movimenti.append((attuale_x,attuale_y))
        elif casella_giu == " ":
            attuale_x += 1
            elenco_movimenti.append((attuale_x,attuale_y))
        elif casella_sx == " ":
            attuale_y -= 1
            elenco_movimenti.append((attuale_x,attuale_y))
        #else: devo mettere che se devo cambiare direzione devo tornare indietro
    return elenco_movimenti

def main():
    labirinto=leggi_testo("labirinto.txt")
    print(labirinto)

    elenco_movimenti=movimento(labirinto)
    print(elenco_movimenti)
main()
 

