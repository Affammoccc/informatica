import csv

# apro e stampo il file
def leggi_magazzini(nome_file):
    magazzini=[]
    try:
        file=open(nome_file,"r",newline="",encoding="utf-8")
        reader=csv.DictReader(file,delimiter=";")
        for riga in reader:
            magazzini.append(riga)
        file.close()
    except OSError:
        print("il file non esiste")
    return magazzini

def main():
    magazzini = leggi_magazzini("magazzini.csv")
    print(magazzini)
main()   
    
    

   
