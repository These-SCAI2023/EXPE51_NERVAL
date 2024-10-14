import csv

def lire_csv(chemin):
    liste_exclude = []
    liste_ok = []
    with open(chemin, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            # print(len(row))
            if row[0] == "" or row[0] == "|" or row[0] == " " or "\n" in row[0] :
                liste_exclude.append(row)
                # print(liste_exclude)
            else:
                liste_ok.append(row)
        # print(liste_ok)
        return liste_ok

def stocker_csv(chemin, contenu):
    with open(chemin, 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(contenu)



path = "small-ELTeC-por_REN/DINIZ/DINIZ_REF/NER/DINIZ_Familia-Inglezia_REF.txt_spacy-lg-3.7.5.bio"

data = lire_csv(path)
# print(data)

for d in data:
    print(d)
    stocker_csv(f"{path}_clean.bio", d)