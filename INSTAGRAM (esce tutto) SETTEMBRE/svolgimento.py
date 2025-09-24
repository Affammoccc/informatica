# apro il file, conviene come lista di dizionari
def leggi_file(nome_file):
    lista=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(";") #.strip() rimuove spazi, \n; .split(";") rimuove ; e divide in sottostringhe 
            dizionario={
                "nome_account":campi[0],
                "nome_persona":campi[1],
                "followers":float(campi[2]),
                "professione":campi[3]
                                                }
            lista.append(dizionario)
        file.close()
    except OSError: 
        print("il file non esiste")
    return lista

def elabora_testo(lista):
    dizionario_ordinato={}
    for dizionario in lista:
        if dizionario["professione"] not in dizionario_ordinato.keys():
            dizionario_ordinato[dizionario["professione"]] =dizionario["followers"]
        else:
            dizionario_ordinato[dizionario["professione"]]+= dizionario["followers"]
    
    dizionario_finale= dict(sorted(dizionario_ordinato.items(), key=lambda item: item[1], reverse=True))
    top_5=dict(list(dizionario_finale.items())[:5])
    for chiave,valore in top_5.items():
        print(f"{chiave:<23} {valore:.1f} M")
    return 

def main():
    testo=leggi_file("instagram.csv")
    #print(testo)

    bella=elabora_testo(testo)
    print(bella)
main()


        