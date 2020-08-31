

def alias(att):
    return property(lambda self: getattr(self, attr))

class DataRecord:
    title = alias('serial')
    def __init__(self, serial):
        self.serial = serial



if __name__ == "__main__":
    record = DataRecord("148X")
    print(record.title)
    record.serial = "149S"
    print(record.title)
    print(getattr(record,"title"))