# ESCE TUTTO MA L'IVA ESCE SBAGLIATA

# apro e stampo il menu come lista di dizionari
def leggi_menu(nome_file):
    menu=[]
    try:
        file=open(nome_file,"r",newline="",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(",")
            dizionario={
                "ID":campi[0],
                "descrizione":" ".join(campi[1:-2]),
                "costo":campi[-2],
                "IVA":campi[-1]
                                            }
            menu.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")

    return menu

#apro e stampo l'ordine come lista di dizionari   
def leggi_ordine(nome_file):
    ordine=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(",")
            dizionario={
                "ID":campi[0],
                "quantita":int(campi[1])
                                            }
            ordine.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")

    return ordine

def conto(menu,ordine):
    conto=[]
    for dizionario1 in menu:
        for dizionario2 in ordine:
            if dizionario1["ID"] == dizionario2["ID"]:
                dizionario_conto={
                    "quantita":dizionario2["quantita"],
                    "descrizione":dizionario1["descrizione"],
                    "costo":dizionario1["costo"],
                    "IVA":dizionario1["IVA"]
                                                                }
                conto.append(dizionario_conto)
    
    print("RICEVUTA")
    totale=0
    totale_con_iva=0
    for piatto in conto:
        valori = list(piatto.values())
        prezzo=float(valori[2])
        iva=int(valori[3])
        
        print(f"{valori[0]}  {valori[1]:<23}  {float(valori[2]):<10.2f}   IVA {valori[3]}% ")
        totale+=prezzo*(valori[0])
        totale_con_iva+=prezzo*(1+iva/100)*(valori[0])
        totale_iva=totale_con_iva-totale
        
    print(f"Totale: {totale} euro")
    print(f"Di cui IVA: {totale_iva:.2f} euro")

def main():
    menu=leggi_menu("menu.txt")
    #print(menu)

    ordine=leggi_ordine("ordine.txt")
    #print(ordine)

    conto_ordine=conto(menu,ordine)
    print(conto_ordine)

main()
