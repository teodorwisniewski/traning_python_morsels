import csv

class Row:
    def __init__(self,**kwargs):
        for key,val in kwargs.items():
            setattr(self,key,val)

    def __repr__(self):
        keys_values_str = ", ".join([
            f"{key}={val!r}"
            for key,val in self.__dict__.items()
        ])
        return f"Row({keys_values_str})"


class FancyReader:

    def __init__(self,lines,*,fieldnames=None):
        self.iter_lines = csv.reader(lines)
        if fieldnames is None:
            fieldnames = next(self.iter_lines )
        self.fieldnames = fieldnames


    def __next__(self):
        values = next(self.iter_lines)
        kwargs = dict(zip(self.fieldnames,values))
        return Row(**kwargs)

    def __iter__(self):
        return self


if __name__ == "__main__":

    #Basic solution
    lines = ['my,fake,file', 'has,two,rows']
    reader = FancyReader(lines, fieldnames=['w1', 'w2', 'w3'])
    print("Here we have our first Fancy reader")
    print(reader.fieldnames)
    for row in reader:
        print(row.w1, row.w2, row.w3)
    # my fake file
    # has two rows

    # Bonus 1
    #
    lines = ['my,fake,file', 'has,two,rows']
    reader = FancyReader(lines, fieldnames=['w1', 'w2', 'w3'])
    row = next(reader)
    print(row)
    # Row(w1='my', w2='fake', w3='file')
    print(repr(row )=="Row(w1='my', w2='fake', w3='file')")
    w1, w2, w3 = row
    print(w3)
    # 'file'

