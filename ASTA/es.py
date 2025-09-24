def main():
    nome_file = "offerte.txt"
    (oggetti, offerte) = leggi_file(nome_file)
   
    stampa_oggetti_non_assegnati(oggetti, offerte)
    stampa_acquisti_partecipanti(oggetti, offerte)
    stampa_spesa_maggiore(offerte)



def leggi_file(nome_file):
    infile = open(nome_file, "r")
    oggetti = set()
    offerte = list()

    for riga in infile:
        info = riga.strip().split(", ")
        partecipante = dict()
        partecipante["nome"] = info[0]

        for indice in range(1, len(info), 2):
            partecipante[info[indice]] = int(info[indice+1])
            oggetti.add(info[indice])


        offerte.append(partecipante)


    infile.close()
    return (oggetti, offerte)


def stampa_oggetti_non_assegnati(oggetti, offerte):
    oggetti_non_assegnati = set()
    for oggetto in oggetti:
        offerta_max = -1
        non_assegnato = True
        uguali_offerenti = list()

        for partecipante in offerte:
            if oggetto in partecipante and partecipante[oggetto] > offerta_max:
                offerta_max = partecipante[oggetto]
                non_assegnato = False
                uguali_offerenti = list()
                uguali_offerenti.append(partecipante["nome"])

            elif oggetto in partecipante and partecipante[oggetto] == offerta_max:
                non_assegnato = True
                uguali_offerenti.append(partecipante["nome"])

        if non_assegnato:
            oggetti_non_assegnati.add(oggetto)

            print(f"Stessa offerta per {oggetto} ({offerta_max}) da parte di: ", end="")
            for indice in range(len(uguali_offerenti)):
                nome = uguali_offerenti[indice]
                if indice != len(uguali_offerenti) - 1:
                    print(f"{nome}, ", end="")
                else:
                    print(f"{nome}.")

    for oggetto_non_assegnato in oggetti_non_assegnati:
        oggetti.remove(oggetto_non_assegnato)
    
    print()


def stampa_acquisti_partecipanti(oggetti, offerte):
    for partecipante in offerte:
        partecipante["acquistato_qualcosa"] = False
        partecipante["acquisti"] = list()
        partecipante["spesa_totale"] = 0

        for oggetto in oggetti:
            if oggetto in partecipante:
                miglior_offerta = True
                for altro_partecipante in offerte:
                    if oggetto in altro_partecipante and altro_partecipante[oggetto] > partecipante[oggetto]:
                        miglior_offerta = False
        

                if miglior_offerta:
                    partecipante["acquistato_qualcosa"] = True
                    partecipante["acquisti"].append(oggetto)
                    partecipante["spesa_totale"] += partecipante[oggetto]
        



        # Alice Walton: Pendola Boulle in tartaruga e ottone 60, Moneta d'oro romana "Aureo di Traiano" 31, Quadretto sacro fiammingo con cornice in legno dorato 110, totale 201.
        if partecipante["acquistato_qualcosa"]:
            print(f"{partecipante['nome']}: ", end="")
            for oggetto in partecipante["acquisti"]:
                print(f"{oggetto} {partecipante[oggetto]}, ", end = "")
            print(f"totale {partecipante['spesa_totale']}")
        
        else:
            print(f"{partecipante['nome']}: nessun oggetto aggiudicato")

    print()
    



def stampa_spesa_maggiore(offerte):
    partecipante_max = ""
    spesa_max = 0
    for partecipante in offerte:
        if partecipante["spesa_totale"] > spesa_max:
            spesa_max = partecipante["spesa_totale"]
            partecipante_max = partecipante["nome"]
        
    print(f"L'offerente che ha speso di più è {partecipante_max}.")












main()