# VEDI COME TOGLIERE LE VIRGOLETTE CHE NON VANNO VIA, IL RESTO DOVREBBE ESSERE OK (VEDI ULTIMO PUNTO SOLO)

import csv
# apro e stampo il file csv come lista di dizionari
def leggi_testo(nome_file):
    lista = []
    try:
        file = open(nome_file,"r",encoding="utf-8")
        reader=csv.DictReader(file, delimiter=",")
        for riga in reader:
            lista.append(riga)
        file.close()
    except OSError:
        print("il file non esiste")
    return lista

# crea l'elenco delle province, in ordine alfabetico
def province(lista):
    lista_province = []
    for dizionario in lista:
        province = dizionario["Provincia"]
        lista_province.append(province)
    lista_province_singole = sorted(set(lista_province))

    print("Le province per le quali sono state fornite le statistiche sono:")

    for parola in lista_province_singole:
        print(f"{parola}")

    return lista_province_singole

# per ogni provincia fare la somma degli studenti iscritti
def iscrizioni_per_provincia(lista):
    diz={}
    for dizionario in lista:
        provincia= dizionario["Provincia"]
        iscritti=int(dizionario["Numtotaleiscritti"])
        if  provincia not in diz:
            diz[provincia]=iscritti
        else:
            diz[provincia] += iscritti

    dizionario_ordinato = dict(sorted(diz.items(), key=lambda item : item[0]))
    
    for chiave,valore in dizionario_ordinato.items():
        print(f"Totale studenti iscritti {chiave}: {valore}")

# elenco studenti dell'infanzia del piemonte
def studenti_infanzia_piemonte(lista):
    totale=0
    for dizionario in lista:
        if dizionario["GradoScolastico"] == "1 - Scuola dell'infanzia":
            totale+= int(dizionario["Numtotaleiscritti"])
    print(f"Il totale degli studenti iscritti alla scuola dell'infanzia in Piemonte e {totale}")
        
    return 

def main():
    testo=leggi_testo("iscrizioni.csv")
    #print(testo)

    elenco_province = province(testo) 
    #print(elenco_province)
    print(" ")
    elenco_iscritti = iscrizioni_per_provincia(testo)
    #print(elenco_iscritti)
    print(" ")
    infanzia = studenti_infanzia_piemonte(testo)
    print(infanzia)
main()
