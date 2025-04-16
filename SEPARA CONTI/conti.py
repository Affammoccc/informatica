# INCOMPLETO (manca capire come aggiungere le quantita nello scontirno e poi e fatta in pratica)

# apro e stampo lo scontrino
def leggi_scontrino(nome_file):
    scontrino=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(",")
            dizionario = {
                "nome":campi[0],
                "costo":campi[1]
                                    }
            scontrino.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    
    totale=0
    for dizionario in scontrino:
        totale+=float(dizionario["costo"])
    print(f"Totale speso: {totale} euro ")


    quantita={}
    for dizionario in scontrino:
        if dizionario["nome"] in quantita:
            quantita["nome"] += 1
        else:
            quantita["nome"] = 1
        
    return scontrino

# apro e stampo la lista
def leggi_lista(nome_file):
    lista=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(",")
            dizionario = {
                "nome":campi[0],
                "quantita":campi[1]
                                    }
            lista.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")       
    return lista


def calcolo(scontrino,lista):
    
    





   """ mancanti=[]
    for dizionario_s in scontrino:
        for dizionario_l in lista:
            if dizionario_l["nome"] not in dizionario_s["nome"] and dizionario_l["quantita"] != dizionario_s["quantita"]:
                dizz_mancanti={
                    "nome":dizionario_l["nome"],
                    "quantita":dizionario_l["quantita"]
                                                            }
    mancanti.append(dizz_mancanti)
    return mancanti"""





                


def main():
    scontrino=leggi_scontrino("scontrino.csv")
    #print(scontrino)

    lista=leggi_lista("lista.csv")
    #print(lista)

    manc=calcolo(scontrino,lista)
    print(manc)
main()
