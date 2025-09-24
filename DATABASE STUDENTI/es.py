import csv

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
            criteria.append(riga.strip())
        file.close()
    except OSError:     
        print("il file non esiste") 

    return criteria

def classifica(studenti,criteria):

    print("Studenti trovati per ID:")
    for dizionario in studenti:
        for valore in dizionario.values():
            if valore in criteria[0]:
                print(dizionario)

    print("Studenti trovati per cognome:")
    for dizionario in studenti:
        for valore in dizionario.values():
            if valore in criteria[1]:
                print(dizionario)

    somma=0
    for dizionario in studenti:
        for valore in dizionario.values():
            if valore in criteria[2]:
                somma+=float(dizionario["GPA"])
                media=somma/len(dizionario["GPA"])
    print(f"Media del GPA per il grado 10A: {media:.2f}")

    return 

def main():
    studenti=leggi_studenti("studenti.csv")
    #print(studenti)

    criteri=leggi_criteria("criteria.txt")
    #print(criteri)

    finale=classifica(studenti,criteri) 
    print(finale)
main()  
