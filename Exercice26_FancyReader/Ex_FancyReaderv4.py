import csv


class Row:
    def __init__(self,**kwargs):
        for name,val in kwargs.items():
            setattr(self,name,val)

    def __iter__(self):
        yield from self.__dict__.values()

    def __repr__(self):
        args = ", ".join([
            f"{key}={repr(val)}"
            for key,val in self.__dict__.items()
        ])
        return f"Row({args})"


class FancyReader:

    def __init__(self,lines, fieldnames=None):
        self.lines_iterator = csv.reader(lines)

        if fieldnames is None:
            self.fieldnames = next(self.lines_iterator)
            self.line_num = 1
        else:
            self.fieldnames = fieldnames
            self.line_num = 0

    def __next__(self):
        self.line_num += 1
        values = next(self.lines_iterator)
        attrs = dict(zip(self.fieldnames,values))
        return Row(**attrs)

    def __iter__(self):
        return self