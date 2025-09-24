def leggi_editori(nome_file):
    editori=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(";")
            dizionario_editori={
                "nome":campi[0],
                "costo":float(campi[1]),
                                            }
            editori.append(dizionario_editori)
        file.close()
    except OSError:
        print("il file non esiste")
    return editori

def leggi_pubblicazioni(nome_file):
    pubblicazioni=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(";")
            dizionario_pubblicazioni={
                "DOI":campi[0],
                "nome_editore":campi[1],
                "indicazione_pubblicazione":campi[2],
                "anno":int(campi[3])
                                                            }
            pubblicazioni.append(dizionario_pubblicazioni)
        file.close()
    except OSError:
        print("il file non esiste")
    return pubblicazioni


# RAGIONAMENTO
#   Per ogni editore stampare qunati articoli ha pubblicato e la percentuale di articoli pubblicati open access
#   Per la percentuale, visto che puo essere T o F, conviene fare tipo:
#       se vale T faccio la somma e poi la divido per il numero di articoli * 100  
def svolgimento(editori,pubblicazioni):
    diz={}
    editori_comuni=[]
    for dizionario_editore in editori:
        for dizionario_pubblicazione in pubblicazioni:
            if dizionario_editore["nome"]==dizionario_pubblicazione["nome_editore"]:
                editori_comuni.append(dizionario_pubblicazione)
    
    for editore in editori_comuni:
        if editore["nome_editore"] not in diz.keys():
            diz[editore["nome_editore"]]=1
        else: 
            diz[editore["nome_editore"]]+=1 

    dizionario_ordinato=dict(sorted(diz.items(), key=lambda item: item[0]))
    
    for chiave,valore in dizionario_ordinato.items():
        print(f"{chiave:<15} : {valore:>4} articoli,        % open source")

    return 
                


def main():
    editori=leggi_editori("publisher_fees.txt")
    #print(editori)

    pubblicazioni=leggi_pubblicazioni("data_pubblicazione.csv")
    #print(pubblicazioni) 

    finale=svolgimento(editori,pubblicazioni)
    print(finale)       
main()

            