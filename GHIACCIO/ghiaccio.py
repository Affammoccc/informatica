def leggi_listino(nome_file):
    listino=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split()
            dizionario_listino={
                "lettera_identificativa":campi[0],
                "citta":campi[1],
                "distanza": campi[2]
                                                        }
            listino.append(dizionario_listino)      
        file.close()
    except OSError:
        print("il file non esiste")
    return listino

def leggi_distanze(nome_file):
    distanze=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split()
            dizionario_distanze={
                "lettera_identificativa_partenza":campi[0],
                "lettera_identificativa_arrivo":campi[1],
                "distanza":campi[2]
                                                        }
            distanze.append(dizionario_distanze)      
        file.close()
    except OSError:
        print("il file non esiste")
    return distanze 


def main():
    listino=leggi_listino("listino.txt")
    print(listino)

    distanze=leggi_distanze("distanze.txt")
    print(distanze) 
main()
