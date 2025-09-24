def leggi_file(nome_file):
    oggetti=set()
    offerte=list()

    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(",")
            dizionario={
                "nome":campi[0],

            }
            for i in range(1,len(campi),2):
                dizionario[campi[i]]=int(campi[i+1])
                oggetti.add(campi[i])
        file.close()
    except OSError:
        print("il file non esiste")
    return



def main():
    testo=leggi_file("offerte.txt")
    print(testo)
main()



