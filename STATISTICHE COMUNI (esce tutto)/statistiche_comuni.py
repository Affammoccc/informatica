# GREZZO MA FATTO

# leggo e apro il file come lista di dizionari inserendo nei dizionari solo 
# la coppia chiave valore di comune e regione
def leggi_statistiche_comuni(nome_file):
    comuni=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        file.readline()
        for riga in file:
            campi=riga.split(";")
            comune=campi[6]
            regione=campi[10]
            dizionario={
                "comune":comune,
                "regione":regione
                                    }
            comuni.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return comuni


# apro e stampo il file come lista
def leggi_regioni(nome_file):
    regioni=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split()
            dizionario={
                "nome_regione":" ".join(campi)
                                            }
            regioni.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return regioni


#estraggo i comuni delle regioni contenute nella lista regioni
def estrai_comuni(comuni,regioni):
    comuni_filtrati=[]
    for comune in comuni:
        for regione in regioni:
            if comune["regione"] == regione["nome_regione"]:
                dizionario_filtrato={
                    "comune":comune["comune"],
                    "regione":regione["nome_regione"]
                                                        }
                comuni_filtrati.append(dizionario_filtrato)

    comune_min= min(comuni_filtrati, key=lambda item: len(item["comune"]))
    comune_max = max(comuni_filtrati, key=lambda item: len(item["comune"]))

    print(f"il nome piu breve è {comune_min} e quello più lungo è {comune_max}")
   
    return comuni_filtrati


def main():
    comuni=leggi_statistiche_comuni("elenco_comuni_italiani.csv")
    #print(statistiche_comuni)

    regioni=leggi_regioni("regioni.txt")
    #print(regioni)

    comuni=estrai_comuni(comuni,regioni)
    #print(comuni)
main()



