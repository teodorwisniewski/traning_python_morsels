

import sys
import csv
from argparse import ArgumentParser
# from dataclasses import dataclass

# @dataclass
# class Argumenciki:
#     stary_plik: str
#     nowy_plik: str
#     delim: str
#     quote: str

# argumenciki = Argumenciki("original.csv","nowiutkie.csv",None,None)
parser = ArgumentParser() # dzielimy argumenty na podzbiory
parser.add_argument("stary_plik")
parser.add_argument("nowy_plik")
parser.add_argument("--in-delimiter", dest="rodzielacz")
parser.add_argument("--in-quote", dest="cudzyslow")
argumenciki = parser.parse_args()

# print((stary_plik+" ")*20)

with open(argumenciki.stary_plik, newline='') as pliczek:
    arguments = {}
    if argumenciki.rodzielacz:
        arguments['delimiter'] = argumenciki.rodzielacz
    if argumenciki.cudzyslow:
        arguments['quotechar'] = argumenciki.cudzyslow
    if not argumenciki.rodzielacz and not argumenciki.cudzyslow:
        arguments['dialect'] = csv.Sniffer().sniff(pliczek.read())
        pliczek.seek(0) # "przejscie na peirwsza strone ksiazki"
    linijki = list(csv.reader(pliczek, **arguments))
    with open(argumenciki.nowy_plik, mode="wt", newline='') as pliczek_wyjsciowy:
        csv.writer(pliczek_wyjsciowy).writerows(linijki)



