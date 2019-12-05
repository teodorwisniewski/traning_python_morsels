import sys 
import csv

stary_plik = sys.argv[1]
nowy_plik = sys.argv[2] 

print(100*stary_plik)

with open(stary_plik) as plik_csv:
    csv_reader = csv.reader(plik_csv, delimiter="|")
    line_count = 0
    lines = list(csv_reader)
    with open(nowy_plik, 'w', newline='') as new_file:
        new_file_writer = csv.writer(new_file, delimiter=',', quotechar='"')    
        new_file_writer.writerows(lines)
            
    
