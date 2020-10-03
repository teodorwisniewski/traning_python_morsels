import csv

class Row:

    def __init__(self,**kwargs):
        for key,val in kwargs.items():
            setattr(self,key,val)


class FancyReader:

    def __init__(self,lines,*,fieldnames=None,**kwargs):
        self.csv_reader_iter = csv.reader(lines)
        self.fieldnames = fieldnames

    def __next__(self):
        values = next(self.csv_reader_iter)
        attributes_values = dict(zip(self.fieldnames,values))
        return Row(**attributes_values)

    def __iter__(self):
        return self


if __name__ == "__main__":

    lines = ['my,fake,file', 'has,two,rows']
    reader = FancyReader(lines, fieldnames=['w1', 'w2', 'w3'])
    for row in reader:
        print(row.w1, row.w2, row.w3)
    # ...
    # my
    # fake
    # file
    # has
    # two
    # rows