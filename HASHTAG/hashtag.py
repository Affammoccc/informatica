# NON RIESCO

# E UN FILE DOVE I CAMPI HANNO LUNGHEZZE DIVERSE
# apro e leggo il file
# creo una lista di dizionari, dove ogni dizionario contiene le varie parti di ogni riga
def leggi_testo(nome_file):
    lista=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split()
            if riga:
                data = campi[0]
                ora=campi[1]
                hashtag=campi[2:]
                lista.append({"data":data, "ora":ora, "hashtag":hashtag})
        file.close()
    except OSError:
        print("il file non esiste")
    return lista

# stampala in ordine decrescente e visualizzare l'aumento in % dell'utilizzo degli hashtag popolari
# un hashtag e popolare se vi e un aumento di utilizzo del 50% ripetto al giorno prima
def conteggio_hashtag(lista):
    conteggio = {}
    for data,hashtag in lista:







def main():
    testo=leggi_testo("hashtag.csv")
    print(testo)
main()



        

    

