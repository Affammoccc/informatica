# ESCE TUTTO TRANNE I COMUNI CON ALTITUDINE MAGGIORE

# apro e stampo il file comuni
def leggi_comuni(nome_file):
    comuni=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(";")
            dizionario={
                "comune":campi[0],
                "regione":campi[1],
                "provincia":campi[2],
                "abitanti":campi[3],
                "altitudine":campi[4]
                                        }
            comuni.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return comuni
       
# creo le due liste in modo da estrarre il valore associato alla chiave altitudine delle due 
# province per poi andare ad indicare il valore maggiore
def analizza_comuni(comuni):
    AL=[]
    AT=[]

    for dizionario in comuni:
        if dizionario["provincia"]=="AL":
            AL.append(dizionario)
        elif dizionario["provincia"]=="AT":
            AT.append(dizionario)
        else:
            None
    
    valori_AL=[]
    AL_ridotta = []
    for dizionario in AL:
        dizionario_ridotto={
            "altitudine":dizionario["altitudine"]
                                                    }
        AL_ridotta.append(dizionario_ridotto)
    
    for dizionario in AL_ridotta:
        valori_AL.append(int(dizionario["altitudine"]))
        massimo=max(valori_AL)
    print(massimo)

    
    valori_AT=[]
    AT_ridotta = []
    for dizionario in AT:
        dizionario_ridotto={
            "altitudine":dizionario["altitudine"]
                                                    }
        AT_ridotta.append(dizionario_ridotto)


    for dizionario in AT_ridotta:
        valori_AT.append(int(dizionario["altitudine"]))
        massimo=max(valori_AT)
    print(massimo)

def main():
    lista_comuni=leggi_comuni("comuni.csv")
    #print(lista_comuni)

    analisi=analizza_comuni(lista_comuni)
    print(analisi)
main()