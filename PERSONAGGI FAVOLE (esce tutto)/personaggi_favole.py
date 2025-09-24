# FUNZIONA TUTTO TRANNE RE CHE ME LO CONTA NELLE OCCORRENZE MA NON DOVREBBE

# apro e stampo il file della favola 
def leggi_dati(nome_file):
    dati= []
    try:
        file = open(nome_file,"r", encoding="utf-8")
        righe = file.readlines()
        for riga in righe:
            dati.append(riga.strip())
        file.close()
    except OSError:
        print("il file non esiste")
    return dati

# lista contenente quante volte compaiono i nomi dei personaggi
# lista contenente i personaggi che non compaiono#    
#    per ogni personaggio, per ogni riga, aggiungo il personaggio e aumento di 1 il contatore, senno aggiungo alla lista assenti

def conteggio_personaggi(lista_personaggi, lista_favola):
    conteggio_personaggi = []
    non_presenti=[]
    for personaggio in lista_personaggi:
        contatore = 0
        for riga in lista_favola:
                contatore += riga.lower().count(personaggio.lower())
        if contatore > 0:
            conteggio_personaggi.append((personaggio, contatore))
            print(f"{personaggio}: {contatore} occorrenze")
        else:
            non_presenti.append(personaggio)
    conteggio_personaggi.sort(key=lambda x: x[1], reverse=True)
    personaggio_minimo=conteggio_personaggi[-1]
    personaggio_max=conteggio_personaggi[0]
    print(f"Il personaggio piu ricorrente e {personaggio_max[0]}, quello meno ricorrente e {personaggio_minimo[0]}")
    return conteggio_personaggi,non_presenti
 
def personaggi_mancanti(nome_file,non_presenti):
    file=open(nome_file,"w",encoding="utf-8")
    for personaggio in non_presenti:
        file.write(personaggio + "\n")
    file.close()

def main():
    favola=leggi_dati("favola.txt")
    #print(favola)
    personaggi=leggi_dati("personaggi.txt")
    #print(personaggi)
    conteggio,non_presenti=conteggio_personaggi(personaggi,favola)
    personaggi_mancanti("personaggi_mancanti.txt",non_presenti)  
main()

