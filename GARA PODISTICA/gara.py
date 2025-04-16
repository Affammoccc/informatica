# MANCA LA PARTE DEL PR BATTUTO

# apro e stampo i risultati come lista di dizionari
def risultati(nome_file):
    risultati=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(";")
            dizionario = {
                "nome":campi[0],
                "cognome":campi[1],
                "eta":int(campi[2]),
                "categoria":campi[3],
                "tempo":campi[4],
                "ID":campi[5]
                                        }
            risultati.append(dizionario)
        file.close()
    except OSError:
        print("il fil enon esiste")
    return risultati

# apro e stampo il database come lista di dizionari
def database_atleti(nome_file):
    database=[]
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            campi=riga.strip().split(";")
            dizionario = {
                "ID":campi[0],
                "record_personale":campi[1]
                                        }
            database.append(dizionario)
        file.close()
    except OSError:
        print("il fil enon esiste")
    return database

# sostituisco il tempo con il tempo min/km
# riduco la lista dividendola per genere e stampo
def gara(risultati,database):
    M=[]
    F=[]

    distanza=10
    for dizionario in risultati:
        tempo=float(dizionario["tempo"])
        passo=tempo/distanza
        minuti=int(passo)
        secondi=int((passo-minuti)*60)
        dizionario["tempo"]=f"{minuti}:{secondi}"

    for dizionario in risultati:
        if dizionario["categoria"]=="M":
            M.append(dizionario)
        elif dizionario["categoria"]=="F":
            F.append(dizionario)
        else: None
    
    M_ridotta = []
    for dizionario in M:
        dizionario_M_ridotto = {
            "nome":dizionario["nome"],
            "cognome":dizionario["cognome"],
            "tempo":dizionario["tempo"]
                                        }
        M_ridotta.append(dizionario_M_ridotto)

    F_ridotta = []
    for dizionario in F:
        dizionario_F_ridotto={
            "nome":dizionario["nome"],
            "cognome":dizionario["cognome"],
            "tempo":dizionario["tempo"]
                                        }
        F_ridotta.append(dizionario_F_ridotto)
    
    print("Categoria : M")
    for valori in M_ridotta:
        elemento =list(valori.values())
        print(f"{elemento[0]} {elemento[1]}, {elemento[2]} min/km")

    print("Categoria : F")
    for valori in F_ridotta:
        elemento =list(valori.values())
        print(f"{elemento[0]} {elemento[1]}, {elemento[2]} min/km")


    lista_pr=[]
    for dizionario in database
        
    return 


def main():
    risultati_gara=risultati("risultati_gara.txt")
    #print(risultati_gara)

    database=database_atleti("database.txt")
    #print(database)

    calcolo_gara=gara(risultati_gara)
    print(calcolo_gara)
main()

