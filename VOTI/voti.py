# DEVO SOLO CAPIRE COME STAMAPRE SU UN FIL ECHE MI CREO

# apro e stampo il primo appello come lista di dizionari
def primo_appello(nome_file):
    primo_appello=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        file.readline()
        for riga in file:
            campi=riga.strip().split(",")
            dizioario_primo={
                "nome":campi[0],
                "cognome":campi[1],
                "voto":int(campi[2]),
                "anno_nascita":campi[3],
                "media_voti":float(campi[4])
                                            }
            primo_appello.append(dizioario_primo)
        file.close()
    except OSError:
        print("il file non esiste")
    return primo_appello

# apro e stampo il primo appello come lista di dizionari
def secondo_appello(nome_file):
    secondo_appello=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        file.readline()
        for riga in file:
            campi=riga.strip().split(",")
            dizioario_secondo={
                "nome":campi[0],
                "cognome":campi[1],
                "voto":int(campi[2]),
                "anno_nascita":campi[3],
                "media_voti":float(campi[4])
                                                }
            secondo_appello.append(dizioario_secondo)
        file.close()
    except OSError:
        print("il file non esiste")
    return secondo_appello

# unisco le liste di dizionari, le ordino per voto e cognome decrescente e calcolo
def sessione(primo_appello,secondo_appello):
    
    sessione = primo_appello + secondo_appello
    sessione_ordinata_voto_cognome=(sorted(sessione, key=lambda item : (item["voto"], item["cognome"]), reverse=True))
    top_5=sessione_ordinata_voto_cognome[:5]
    print("nome,cognome,voto,anno_nascita,media_esami_precedenti")

    totale_voti=0
    totale_media_voti=0
    for elemento in top_5:
        valori = list(elemento.values())
        
        voto=valori[2]/5
        totale_voti+=voto
        
        media_voti=valori[4]/5
        totale_media_voti+=media_voti
        
        print(f"{valori[0]},{valori[1]},{valori[2]},{valori[3]},{valori[4]}")
    differenza_media_voti= totale_voti-totale_media_voti
    print(f"La media tra le differenze tra voto e media pregressa per i cinque studenti con voto maggiore nella sessione è : {differenza_media_voti:.2f}")
    
    return 


def main():
    primo_ap=primo_appello("primo_appello.csv")
    #print(primo_ap)

    secondo_ap=secondo_appello("secondo_appello.csv")
    #print(secondo_ap)

    sess=sessione(primo_ap,secondo_ap)
    #print(sess)

main()
