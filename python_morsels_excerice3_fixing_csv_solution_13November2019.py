import csv
from argparse import ArgumentParser
from dataclasses import dataclass

# @dataclass
# class Argumenciki:
#     stary_plik: str
#     nowy_plik: str
#     delim: str
#     quote: str

# argumenciki = Argumenciki("original.csv","nowiutkie.csv",None,None)
arguments = {}
parser = ArgumentParser()
parser.add_argument("stary_Plik")
parser.add_argument("nowy_plik")
parser.add_argument('--in-delimiter', dest="delim")
parser.add_argument('--in-quote', dest='quote')

argumenciki = parser.parse_args()

with open(argumenciki.stary_plik) as stary:
    arguments = {}
    if arguments.delim:
        arguments['delimiter'] = arguments.delim
    if arguments.quote:
        arguments['quotechar'] = arargumentsgs.quote
    if not args.delim and not args.quote:
        arguments['dialect'] = csv.Sniffer().sniff(old_file.read())
        old_file.seek(0)
    with open(argumenciki.nowy_plik, mode = "wt", newline="") as nowy:
        csv.writer(nowy).writerows(linie)
