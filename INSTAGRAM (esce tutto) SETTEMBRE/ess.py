def leggi_file(nome_file):
    lista = []
    try:
        file = open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi = riga.rstrip().split(";") #rstrip toglie spazi e \n a dx, split toglie il ;
            dizionario = {
                "nome_account" : campi[0],
                "nome_reale" : campi[1],
                "followers" : float(campi[2]),
                "professione" : campi[3]
                                                }
            lista.append(dizionario) 
        file.close()
    except OSError: 
        print("il file non esiste")
    return lista        


def svolgimento(lista):

    diz={}
    professione=dizionario["professione"]
    followers=dizionario["followers"]

    for dizionario in lista:
        if professione not in dizionario.values():
            diz["professione"]=followers
        else:
            diz["professione"]+=followers
    return diz

        






def main():
    testo=leggi_file("instagram.csv")
    print(testo)

    svolgimento(testo)
main()  