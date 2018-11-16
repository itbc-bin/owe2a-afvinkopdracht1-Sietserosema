# Naam:
# Datum:
# Versie:
# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.


def main():
    bestand = "alpaca.txt"
    try:
        headers, seqs = lees_inhoud(bestand)
    except TypeError:
        print("Het bestand staat in het verkeerde formaat")
    else:
        zoekwoord = input("Geef een zoekwoord op: ")
        for i in range(len(headers)):
            if zoekwoord in headers[i]:
                print("Header:", headers[i])
                check_is_dna = is_dna(seqs[i])
                if check_is_dna:
                    print("Sequentie is DNA")
                    knipt(seqs[i])
                else:
                    print("Sequentie is geen DNA. Er is iets fout gegaan.")


def lees_inhoud(bestands_naam):
    """
    open een bestand en haalt de headers en sequenties uit het bestand op fasta formaat
    :param bestands_naam: bestands pad
    :return: twee lijsten met headers en sequenties
    """
    try:
        bestand = open(bestands_naam)
        headers = []
        seqs = []
        seq = []
        for line in bestand:
            line = line.strip()
            if ">" in line:
                if seq != "":
                    seqs.append(seq)
                    seq = ""
                headers.append(line)
            else:
                seq += line.strip()
        seqs.append(seq)
        return headers, seqs
    except FileNotFoundError:
        print("Het bestand is niet gevonden")
    except NameError:
        print("Het bestand in lees_inhoud kan niet geopend worden")


def is_dna(seq):
    """
    de functie controleert of het een dna sequentie is
    :param seq:
    :return: een boolean
    """
    try:
        dna = False
        a = seq.count("A")
        t = seq.count("T")
        c = seq.count("C")
        g = seq.count("G")
        total = a+t+c+g
        if total == len(seq):
            dna = True
        return dna
    except NameError:
        print("De functie is_Dna returned een string en geen boolean")


def knipt(alpaca_seq):
    """
    de functie kijkt of een enzym uit een bestand in de sequentie knipt
    :param alpaca_seq:
    :return: returnt niks
    """
    try:
        bestand = open("enzymen.txt")
        for line in bestand:
            naam, seq = line.split(" ")
            seq = seq.strip().replace("^", "")
            if seq in alpaca_seq:
                print(naam, "knipt in sequentie")
    except IOError:
        print("Het bestand kan niet geopent worden")


main()
