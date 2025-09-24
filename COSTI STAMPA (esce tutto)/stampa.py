# apro e stampo il file
def lista_libri(nome_file):
    libri=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            riga=riga.strip()
            titolo,numero_pagine = riga.split(";")
            dizionario={
                "titolo": titolo.strip(),
                "numero_pagine": int(numero_pagine.strip())
                                                            }
            libri.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return libri

# apro e stampo il file
def costo_pagine(nome_file):
    costo=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            riga=riga.strip()        
            numero_minimo, numero_massimo, prezzo = riga.split(";")
            dizionario={
                "numero_minimo": int(numero_minimo.strip()),
                "numero_massimo": int(numero_massimo.strip()),
                "costo": prezzo.strip()
                                                            }
            costo.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return costo

def listino(costo):
    listino_ordinato=sorted(costo, key=lambda x: x["numero_massimo"])
    print("LISTINO PREZZI")
    for c in listino_ordinato:
        print(f"Fino a {c['numero_massimo']} pagine: {c['costo']}/pagina")
    print(" ")
    return

def costi_stampa(libri,costo):
    print("COSTI DI STAMPA")
    totale=0
    for libro in libri:
        for c in costo:
            if libro["numero_pagine"] >= c["numero_minimo"] and libro["numero_pagine"] <= c["numero_massimo"]:
                prezzo_unitario=float(c["costo"].replace("$","").replace(",","."))
                prezzo=libro["numero_pagine"]*prezzo_unitario
                totale+=prezzo
                
                print(f"{libro['titolo']} - Pagine: {libro['numero_pagine']} - Costo: {prezzo:.2f}$")
    print(f"Totale: {totale:.2f}$")
    return

def main():
    libri=lista_libri("libri.txt")
    #print(libri)

    costo=costo_pagine("costo_pagine.txt")
    #print(costo)

    listino(costo)

    costi_stampa(libri,costo)
main()
