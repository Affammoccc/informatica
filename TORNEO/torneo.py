# apro e stampo il file 
def leggi_partite(nome_file):
    partite = []
    try:
        file=open(nome_file,"r",encoding="utf-8")
        for riga in file:
            parti = riga.strip().split(' - ')
            if len(parti) == 2:
                squadre, punteggio = parti
                squadra1, squadra2 = squadre.split(' - ')
                punteggi_separati = punteggio.split(' : ')
                if len(punteggi_separati) == 2:
                    risultato = {
                        "squadra_casa": squadra1.strip(),
                        "squadra_ospite": squadra2.strip(),
                        "punteggio_casa": int(punteggi_separati[0].strip()),
                        "punteggio_ospite": int(punteggi_separati[1].strip())
                                                                                }
                    partite.append(risultato)         
    except OSError:
        print("il file non esiste")
    return partite


def main():
    torneo=leggi_partite("torneo.txt")
    print(torneo)
main()

        