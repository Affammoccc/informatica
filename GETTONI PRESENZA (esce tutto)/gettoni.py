# ESCE TUTTO TRANNE SOMMA IMPORTO
import csv
# leggo e apro il file
def leggi_testo(nome_file):
    lista=[]
    try:
        file=open(nome_file,"r",newline='',encoding="utf-8")
        reader=csv.DictReader(file,delimiter=";")
        for riga in reader:
            riga["sedute_liquidate"]=int(riga["sedute_liquidate"])
            riga["importo_lordo"]=float(riga["importo_lordo"])
            lista.append(riga)
        file.close()
    except OSError:
        print("il file non esiste")
    return lista

# trovo e stampo coloro che non si sono mai presentati, i 5 con piu presenze e il loro guadagno
def assenti(lista):
    dizionario_nome_presenze={}
    dizionario_guadagno={}
    lista_assenti=[]
    # se il nome non e presente aggiungo il numero di presenze di quel nome, senno le 
    # sommo a quelle presenti (molto utile questa struttura).Stessa cosa con il guadagno
    for dizionario in lista:
        nome=dizionario["nominativo"]
        if nome not in dizionario_nome_presenze.keys():
            dizionario_nome_presenze[nome] = dizionario["sedute_liquidate"]
            dizionario_guadagno[nome] = dizionario["importo_lordo"]
        else:
            dizionario_nome_presenze[nome] += dizionario["sedute_liquidate"]
            dizionario_guadagno[nome] += dizionario["importo_lordo"]
    # ordino il dizionario in base al numero di presenze decrescenti
    dizonario_ordinato = dict(sorted(dizionario_nome_presenze.items(), key=lambda item : item[1], reverse=True))
    # bellezza in output
    for chiave,valore in dizonario_ordinato.items():
        guadagno = dizionario_guadagno[chiave]
        print(f"{chiave:<30} {valore/11:.2f}   {guadagno:.2f}")
    # se il valore associato alla chiave presenze e 0, allora aggiungo il nome alla lista degli assenti
    for chiave,valore in dizionario_nome_presenze.items():
        if valore == 0:
            lista_assenti.append(chiave)          
    # stampo i nomi di coloro che non si sono mai presentati
    for elemento in lista_assenti:
        print(f"Il consigliere {elemento} non ha mai partecipato ad alcuna seduta")
    return 
    
def main():
    testo=leggi_testo("presenze_short.csv")
    #print(testo)
    elenco_assenti=assenti(testo)
    print(elenco_assenti)
main()

