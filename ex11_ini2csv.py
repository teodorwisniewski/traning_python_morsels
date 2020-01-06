
import sys
import csv
from argparse import ArgumentParser
import re
from collections import namedtuple

parser = ArgumentParser() # dzielimy argumenty na podzbiory
parser.add_argument("konfiguracja")
parser.add_argument("wyjscie_plik")
argumenciki = parser.parse_args()
# Argumenty = namedtuple("Argumenty","konfiguracja wyjscie_plik")
# argumenciki = Argumenty(".editorconfig", "blabla.csv")
# print(argumenciki.konfiguracja)
# print(argumenciki.wyjscie_plik)

def czysc_to(elemncik):
    return re.sub("\n|\r|\t", "",  elemncik)

def eliminuj_zbedne(element):
    if not element:
        return False
    return True

with open(argumenciki.konfiguracja) as pliczek:
    with open(argumenciki.wyjscie_plik, mode="wt") as pliczek_wyjsciowy:
        linijki = pliczek.readlines()
        print(linijki)
        linijki = list(map(czysc_to,linijki))
        linijki = list(filter(eliminuj_zbedne,linijki))
        print(linijki)
    
        writer = csv.writer(pliczek_wyjsciowy)
        dodaj_to = ""
        for linijka in linijki:    
            if bool(re.match(r"\[.*?\]",linijka)):
                naglowek = [re.sub(r"\[(.*)\]",r"\1",linijka)]
            if not naglowek[0] in linijka:
                podziel = linijka.split(" = ")
                row = naglowek+podziel
                pliczek_wyjsciowy.write(f'{row[0]},{row[1]},{row[2]}\n')






