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

def separa_conti(scontrino, lista):
    # Conta le quantità acquistate per ogni prodotto
    quantita_acquistata = {}
    prezzo_unitario = {}
    for dizionario in scontrino:
        nome = dizionario["nome"]
        costo = float(dizionario["costo"])
        if nome in quantita_acquistata:
            quantita_acquistata[nome] += 1
        else:
            quantita_acquistata[nome] = 1
            prezzo_unitario[nome] = costo  # salva il prezzo solo la prima volta

    totale_dovuto = 0
    prodotti_mancanti = []

    for elemento in lista:
        nome = elemento["nome"]
        quantita_richiesta = int(elemento["quantita"])
        if nome in quantita_acquistata:
            qta_acq = quantita_acquistata[nome]
            prezzo = prezzo_unitario[nome]
            qta_utilizzata = min(quantita_richiesta, qta_acq)
            totale_dovuto += qta_utilizzata * prezzo
            if quantita_richiesta > qta_acq:
                prodotti_mancanti.append((quantita_richiesta - qta_acq, nome))
        else:
            prodotti_mancanti.append((quantita_richiesta, nome))

    print(f"Totale dovuto: {totale_dovuto:.2f} euro")
    print("Prodotti mancanti:")
    for quantita, nome in prodotti_mancanti:
        print(f"{quantita} {nome}")

def main():
    scontrino=leggi_scontrino("scontrino.csv")
    #print(scontrino)
 
    lista=leggi_lista("lista.csv")
    #print(lista)

    separa_conti(scontrino, lista) 
main()
