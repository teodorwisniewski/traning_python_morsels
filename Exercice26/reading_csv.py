import csv
#
# with open("names.csv","r") as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open("new_names2.csv","w") as new_file:
#         csv_writer = csv.writer(new_file, delimiter = '\t')
#         for line in csv_reader:
#             csv_writer.writerow(line)
#             print(line[2])
#
# tabelka = [
#             "1,2,ijfoege",
#            "sieman,Ludzie,dobrej",
#            ]
# csv_reader2 = csv.reader(tabelka)
#
# for line2 in csv_reader2:
#     print(line)


with open("names.csv","r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open("new_names3.csv","w") as new_file:
        fieldnames = ["first_name","email"]
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter="\t")
        csv_writer.writeheader()
        for line in csv_reader:
            del line["last_name"]
            csv_writer.writerow(line)


print(dir(csv))