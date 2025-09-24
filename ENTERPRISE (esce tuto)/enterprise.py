#MANCANO LE TOP 3 LINGUE

# apro e leggo il file
def leggi_viaggi(nome_file):
    viaggio=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(",")
            dizionario={
                "destinazione":campi[0],
                "durata":int(campi[1]),
                "passeggeri":int(campi[2])
                                                 }
            viaggio.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return viaggio

# apro e leggo il file
def leggi_lingue_pianeti(nome_file):
    lingue_pianeti=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(",")
            dizionario={
                "pianeta":campi[0],
                "lingua":campi[1:]
                                                 }
            lingue_pianeti.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return lingue_pianeti

# calcolo il tempo medio e il numero totale dei passeggeri       
def tempo_medio_viaggi(viaggio):
    somma_passeggeri=0
    somma_durata=0
    for dizionario in viaggio:
        somma_passeggeri+=dizionario["passeggeri"]
        somma_durata+=dizionario["durata"]
    durata_media=somma_durata/len(viaggio)

    return durata_media,somma_passeggeri

#se un luogo compare sia in viaggio che in pietre preziose luoghi, stampa prima il luogo e poi tuttte le pietre 
def lingue_nel_mondo(viaggio,lingue_pianeti): 
    risultato=[]
    for dizionario in viaggio:
        luoghi=dizionario["destinazione"]
        for dizionario2 in lingue_pianeti:
            if dizionario2["pianeta"]==luoghi:
                lingue = ", ".join(dizionario2["lingua"])
                risultato.append(f"- {dizionario2['pianeta']}: {lingue}")
        
    return risultato

def main():
    viaggi=leggi_viaggi("viaggi_enterprise.txt")
    #print(viaggi)

    lingue_pianeti=leggi_lingue_pianeti("lingue_pianeti.txt")
    #print(lingue_pianeti)

    tempo_passeggeri=tempo_medio_viaggi(viaggi)
    print(f"Durata media dei viaggi: {tempo_passeggeri[0]}")
    print(f"Numero totale dei passeggeri: {tempo_passeggeri[1]}")

    print("Lingue parlate nei pianeti visitati:")
    lingue=lingue_nel_mondo(viaggi,lingue_pianeti)
    for lingua in lingue:
        print(lingua)

main()
