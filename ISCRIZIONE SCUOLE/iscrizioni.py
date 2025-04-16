# VEDI COME TOGLIERE LE VIRGOLETTE CHE NON VANNO VIA, IL RESTO DOVREBBE ESSERE OK (VEDI ULTIMO PUNTO SOLO)

# apro e stampo il file csv come lista di dizionari

def leggi_testo(nome_file):
    lista = []
    try:
        file = open(nome_file,"r",encoding="utf-8")
        file.readline()
        for riga in file:
            campi = riga.strip().split(",")
            dizionario = {
                "annoscolastico":campi[0],
                "provincia":campi[1],
                "comune":campi[2],
                "gradoscolastico":campi[3],
                "numeroscuole":campi[4],
                "numeroclassi":campi[5],
                "numerifemmine":campi[6],
                "numeromaschi":campi[7],
                "numeroiscritti":campi[8]
                                                }
            lista.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return lista

# crea l'elenco delle province, in ordine alfabetico
# non capisco perche non tolga le " "
def province(lista):
    lista_province = []
    for dizionario in lista:
        province = dizionario["provincia"]
        lista_province.append(province)
    lista_province_singole = sorted(set(lista_province))

    print("Le province per le quali sono state fornite le statistiche sono:")

    for parola in lista_province_singole:
        print(f"{parola}")

    return lista_province_singole

# per ogni provincia fare la somma degli studenti iscritti
# non riuscendo a togliere le "", non fa la somma ma e giusto
def iscrizioni_per_provincia(lista):
    diz={}
    for dizionario in lista:
        if dizionario["provincia"] not in diz.keys():
            diz[dizionario["provincia"]] = dizionario["numeroiscritti"]
        else:
            diz[dizionario["provincia"]] += dizionario["numeroiscritti"]

    dizionario_ordinato = dict(sorted(diz.items(), key=lambda item : item[0]))
    
    for chiave,valore in dizionario_ordinato.items():
        print(f"Totale studenti iscritti {chiave}:{valore}")

# elenco studenti dell'infanzia del piemonte
# non va ma penso a causa sempre delle " " che non riesco a togliere
def studenti_infanzia_piemonte(lista):
    lista_infanzia = []
    for dizionario in lista:
        if dizionario["gradoscolastico"] == "1 - Scuola dell'infanzia":
            lista_infanzia.append(dizionario["numeroiscritti"])
        
    return lista_infanzia

def main():
    testo=leggi_testo("iscrizioni.csv")
    #print(testo)

    elenco_province = province(testo)
    #print(elenco_province)

    elenco_iscritti = iscrizioni_per_provincia(testo)
    #print(elenco_iscritti)

    infanzia = studenti_infanzia_piemonte(testo)
    print(infanzia)
main()
