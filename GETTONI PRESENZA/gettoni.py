# ESCE TUTTO TRANNE SOMMA IMPORTO

# leggo e apro il file

def leggi_testo(nome_file):
    lista=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        file.readline()
        for riga in file:
            campi=riga.strip().split(";")
            dizionario ={
                "nominativo":campi[0],
                "periodo":campi[1],
                "sedute":int(campi[2]),
                "importo":int(campi[3])
                                        }
            lista.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return lista

# trovo e stampo coloro che non si sono mai presentati

def assenti(lista):
    diz={}
    lista_assenti=[]
    for dizionario in lista:
        if dizionario["nominativo"] not in diz.keys():
            diz[dizionario["nominativo"]] = dizionario["sedute"]
        else:
            diz[dizionario["nominativo"]] += dizionario["sedute"]

    dizonario_ordinato = dict(sorted(diz.items(), key=lambda item : item[1], reverse=True))

    for chiave,valore in dizonario_ordinato.items():
        print(f"{chiave:<30} {valore/11:.2f} ")
    
    for chiave,valore in diz.items():
        if valore == 0:
            lista_assenti.append(chiave)
    
    for elemento in lista_assenti:
        print(f"Il consigliere {elemento} non ha mai partecipato ad alcuna seduta")

    return 
    


def main():
    testo=leggi_testo("presenze_short.csv")
    #print(testo)

    elenco_assenti=assenti(testo)
    print(elenco_assenti)
main()
