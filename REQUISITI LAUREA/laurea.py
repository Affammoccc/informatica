from pprint import pprint

def leggi_esami(nome_file):
    esami=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(",")
            dizionario_esami={
                "matricola":campi[0],
                "data":campi[1],
                "codice":campi[2],
                "voto":campi[3]
                                            }
            esami.append(dizionario_esami)
        file.close()
    except OSError:
        print("il file non esiste")
    return esami

def leggi_cfu(nome_file):
    cfu=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(",")
            dizionario_cfu={
                "codice":campi[0],
                "cfu":int(campi[1]),
                "obbligatorio":campi[2]=='1'
                                            }
            cfu.append(dizionario_cfu)
        file.close()
    except OSError:
        print("il file non esiste")
    return cfu

def statistiche(esami,cfu):
    dizionario_matricola_totale_cfu={}
    for esame in esami:
        for c in cfu:
            if esame["matricola"] not in dizionario_matricola_totale_cfu.keys():
                dizionario_matricola_totale_cfu[esame["matricola"]]=c["cfu"]
            else:
                dizionario_matricola_totale_cfu[esame["matricola"]]+=c["cfu"]
    pprint(dizionario_matricola_totale_cfu)
    return 


def main():
    esami=leggi_esami("REQUISITI LAUREA//esami.log")
    #pprint(esami)

    cfu=leggi_cfu("REQUISITI LAUREA//cfu.dati")
    #pprint(cfu)

    svolgimento=statistiche(esami,cfu)
    pprint(svolgimento,cfu)

    
main()


