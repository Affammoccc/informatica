import csv

# apro e stampo il file
def leggi_partite(nome_file):
    partite = []
    try:
        file=open(nome_file, "r", encoding="utf-8")
        for riga in file:
            riga = riga.strip()
            squadre, punteggi = riga.split(" : ")
            squadra1, squadra2 = squadre.split(" - ")
            punteggio1, punteggio2 = punteggi.split(" - ")
            dizionario = {
                "squadra1": squadra1.strip(),
                "squadra2": squadra2.strip(),
                "punteggio1": int(punteggio1.strip()),
                "punteggio2": int(punteggio2.strip())
                                                           }
            partite.append(dizionario)
        file.close()
    except OSError:
        print("il file non esiste")
    return partite

def classifica(partite):
    statistiche = {}
    for partita in partite:
        squadra1 = partita["squadra1"]
        squadra2 = partita["squadra2"]
        punteggio1 = partita["punteggio1"]
        punteggio2 = partita["punteggio2"]

        for squadra in [squadra1, squadra2]:
            if squadra not in statistiche:
                statistiche[squadra] = {
                    "giocate": 0, "punti": 0, "pf": 0, "ps": 0
                                                                }

        statistiche[squadra1]["giocate"] += 1
        statistiche[squadra2]["giocate"] += 1
        statistiche[squadra1]["pf"] += punteggio1
        statistiche[squadra1]["ps"] += punteggio2
        statistiche[squadra2]["pf"] += punteggio2
        statistiche[squadra2]["ps"] += punteggio1

        if punteggio1 > punteggio2:
            statistiche[squadra1]["punti"] += 3
            statistiche[squadra2]["punti"] += 1
        elif punteggio2 > punteggio1:
            statistiche[squadra2]["punti"] += 3
            statistiche[squadra1]["punti"] += 1
        else:
            statistiche[squadra1]["punti"] += 2
            statistiche[squadra2]["punti"] += 2

    classifica = []
    for squadra, dati in statistiche.items():
        pf = dati["pf"]
        ps = dati["ps"]
        q = pf / ps if ps != 0 else pf  # Evita divisione per zero
        classifica.append({
            "squadra": squadra,
            "giocate": dati["giocate"],
            "punti": dati["punti"],
            "q": q,
            "pf": pf,
            "ps": ps
                                            })

    # Ordina per punti decrescenti, poi per Q decrescente, poi per nome squadra
    classifica.sort(key=lambda x: (-x["punti"], -x["q"], x["squadra"]))

    print(f"{'SQUADRA':<22}{'GIOCATE':>7}{'PUNTI':>7}{'Q':>8}{'PF':>7}{'PS':>7}")
    print("-" * 55)
    for riga in classifica:
        print(f"{riga['squadra']:<22}{riga['giocate']:>7}{riga['punti']:>7}{riga['q']:>8.3f}{riga['pf']:>7}{riga['ps']:>7}")

    return classifica

def main():
    torneo = leggi_partite("torneo.txt")
    print(torneo)

    classifica(torneo)
main()

