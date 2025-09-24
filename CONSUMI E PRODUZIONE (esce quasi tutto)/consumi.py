# MANCANO LE TOP 3 CASE 

import csv
# apro e stampo i vari file (faccio 1 sola funzione perche dovrei farne 3 uguali)
def leggi_csv(nome_file):
    dati=[]
    try:
        file=open(nome_file,"r",newline="",encoding="utf-8")
        reader=csv.DictReader(file,delimiter=";")
        for riga in reader:
            dati.append(riga)
        file.close()
    except OSError:
        print("il file non esiste")
    return dati

# svolgo tutte le cose richieste usando le formule che mi vengono date
def produzioni(consumi,impianti,meteo):

    #faccio un dizionario contenente solo id abitazione dalla lista di dizionari impianti (unica cosa che mi serve)
    impianti_dict={}
    for i in impianti:
        impianti_dict[i["ID_Abitazione"]] = i

    #faccio un dizionario contente solo data e ora dalla lista di dizionari meteo (unica cosa che mi serve)
    meteo_dict={}
    for m in meteo:
        meteo_dict[(m["DATA"], m["ORA"])] = m
    
    energia_prodotta_totale = 0
    energia_autoconsumata_totale = 0
    energia_immessa_totale = 0
    consumo_energetico_totale = 0

    for consumo in consumi:
        #estraggo le cose che mi servono dai vari file aperti prima
        id_abitazione = consumo["ID_Abitazione"]
        data = consumo["Data"]
        ora = consumo["Ora"]
        consumo_energetico = float(consumo["Consumo_energetico"])
        consumo_energetico_totale += consumo_energetico
        
        impianto = impianti_dict.get(id_abitazione)
        dimensione = float(impianto["Dimensione_impianto"])
        efficienza = float(impianto["Eta"])
        
        tempo = meteo_dict.get((data, ora))
        ghi = float(tempo["GHI"])

        #svolgo i calcoli richiesti
        energia_prodotta = efficienza * dimensione * ghi
        energia_autoconsumata = min(energia_prodotta, consumo_energetico)
        energia_immessa = max(energia_prodotta - consumo_energetico, 0)

        energia_prodotta_totale += energia_prodotta
        energia_autoconsumata_totale += energia_autoconsumata
        energia_immessa_totale += energia_immessa

    autoconsumo = (energia_autoconsumata_totale / energia_prodotta_totale) * 100 
    autosufficienza = (energia_autoconsumata_totale / consumo_energetico_totale) * 100

    print("Report aggregato:")
    print(f" Energia Prodotta: {energia_prodotta_totale:.2f} kWh")
    print(f" Energia Consumata: {consumo_energetico_totale:.2f} kWh")
    print(f" Energia autoconsumata: {energia_autoconsumata_totale:.2f} kWh")
    print(f" Energia Immessa: {energia_immessa_totale:.2f} kWh")
    print(f" Percentuale Autoconsumo: {autoconsumo:.2f}%")
    print(f" Percentuale Autosufficienza: {autosufficienza:.2f}%")
    
    return 

def main(): 
    
    lista_consumi = leggi_csv("consumi.txt")
    #print(lista_consumi)
    lista_impianti = leggi_csv("impianti.txt")
    #print(lista_impianti)
    lista_meteo = leggi_csv("meteo.txt")
    #print(lista_meteo)

    produzioni(lista_consumi,lista_impianti,lista_meteo)
main()

    
        