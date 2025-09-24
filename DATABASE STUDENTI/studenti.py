#ESCE SBAGLIATO MA NON CAPISCO COME FARLO QUADRARE

import csv
# apro e stampo il file
def leggi_studenti(nome_file):
    studenti=[]
    try:
        file=open(nome_file,"r",newline="",encoding="utf-8")
        reader=csv.DictReader(file,delimiter=",")
        for riga in reader:
            studenti.append(riga)
        file.close()
    except OSError:
        print("il file non esiste")
    return studenti

def leggi_criteria(nome_file):
    criteria=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            elemento=riga.strip()
            criteria.append(elemento)
        file.close()
    except OSError:
        print("il file non esiste")
    return criteria

def calcolo(studenti,criteria):
    for studente in studenti:
        if criteria[0]==studente["ID"]:
                print(studente)
        if criteria[1]==studente["cognome_studente"]:
                print(studente)

    for studente in studenti:
        somma=0
        numero_studenti=0
        if criteria[2]==studente["grado"]:
            somma+=float(studente["GPA"])
            numero_studenti+=1
        if numero_studenti>0:
            media=somma/numero_studenti
            print(f"Media del GPA per il grado {criteria[2]} e {media}")
    return

def main():
    studenti=leggi_studenti("studenti.csv")
    #print(studenti)
    criteria=leggi_criteria("criteria.txt")
    #print(criteria)

    calcolo(studenti,criteria)
main()
