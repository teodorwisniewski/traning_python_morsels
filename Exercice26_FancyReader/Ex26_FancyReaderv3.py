import csv


class Row:

    def __init__(self,**kwargs):

        for key,val in kwargs.items():
            setattr(self,key,val)

    def __repr__(self):
        keys_vals = ", ".join([
            f"{key}={val!r}"
            for key,val in self.__dict__.items()
        ])
        return f"Row({keys_vals})"

    def __iter__(self):
        yield from self.__dict__.values()



class FancyReader:

    def __init__(self,lines,fieldnames=None):
        self.line_num = 0
        self.arguments_iterator = csv.reader(lines)
        if fieldnames is None:
            self.fieldnames = next(self.arguments_iterator)
            self.line_num += 1
        else:
            self.fieldnames = fieldnames

    def __next__(self):
        self.line_num += 1
        values = next(self.arguments_iterator)
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
    # Expected output
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
    
    #Bonus 2

    lines = ['w1,w2,w3', 'my,fake,file', 'has,two,rows']
    reader = FancyReader(lines)
    for row in reader:
        print(row.w1, row.w2, row.w3)
    # my fake file
    # has two rows

    # Bonus 3
    lines = 'red,1\nblue,2\ngreen,3'.splitlines()
    reader = FancyReader(lines, fieldnames=['color', 'numbers'])
    print(next(reader))
    # Row(color='red', number=1)
    print(reader.line_num)
    #1
    print(next(reader))
    #(Row(color='red', number=1))
    print(reader.line_num)
    #2
    text = "a,b,c\n1,2,3\n4,5,6"
    # Reader with fieldnames
    reader = FancyReader(
        text.splitlines(),
        fieldnames=['a', 'b', 'c'],
    )
    assert reader.line_num == 0
    print(next(reader))
    assert reader.line_num == 1
    print(next(reader))
    assert reader.line_num == 2

    # Reader without fieldnames
    reader = FancyReader(text.splitlines())
    print(next(reader))
    assert reader.line_num == 2
    print(next(reader))
    assert reader.line_num == 3