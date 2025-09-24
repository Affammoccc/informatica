# NON CAPISCO PERCHE NON ESCA (MANCA QUALCOSINA)

# apro e stampo il file come lista di dizionario usando il csv reader HIT
from operator import itemgetter
import csv

def leggi_file(nome_file):
    lista=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        reader=csv.DictReader(file)
        file.readline()
        for riga in reader:
            dizionario=dict(riga)
            lista.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return lista

def trova_indicatori(nome_file):
    indicatori=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        testo=file.readlines()
        for riga in testo:
            indicatori.append(riga.strip())
        file.close()
    except OSError:
        print("il file non esiste")
    return indicatori
    
def leggi_classifica(lista,indicatori):
    classifica=[]
    for dizionario in lista:
        if dizionario["INDICATORE".strip()]==indicatori:
            classifica.append(dizionario)
    classifica.sort(key=lambda item: float(item["VALORE"]),reverse=True)
    return classifica

def main():
    file=leggi_file("file.csv")
    #print(file)

    indicatore=trova_indicatori("indicatore.txt")
    print(indicatore)

    classifica=leggi_classifica(file,indicatore)
    print(classifica)
main()

