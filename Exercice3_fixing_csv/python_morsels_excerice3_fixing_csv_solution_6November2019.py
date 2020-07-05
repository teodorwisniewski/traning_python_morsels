import sys
import csv

nom_ancien_fichier = "original_cars.csv"#sys.argv[1]
nom_nouveau_file = "cpstam.csv"#sys.argv[2]

print("Weszlem do programu")

with open(nom_ancien_fichier) as fichier:
    reader = csv.reader(fichier, delimiter='|')
    with open(nom_nouveau_file, mode='wt', newline='') as new_file:
        csv.writer(new_file).writerows(reader)
    


