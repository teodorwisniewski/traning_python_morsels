import pytest
from Exercice26_FancyReader.Ex_FancyReaderv4 import FancyReader


@pytest.fixture
def reader():
    lines = ['my,fake,file', 'has,two,rows']
    reader = FancyReader(lines, fieldnames=['w1', 'w2', 'w3'])
    return reader


def test_base_problem(reader):
    row = next(reader)
    assert ("my", "fake", "file") == (row.w1, row.w2, row.w3)
    row = next(reader)
    assert ("has", "two", "rows") == (row.w1, row.w2, row.w3)


def test_bonus1(reader):
    row = next(reader)
    assert repr(row) == "Row(w1='my', w2='fake', w3='file')"
    w1, w2, w3 = row
    assert w3 == "file"


def test_bonus2():
    lines = ['w1,w2,w3', 'my,fake,file', 'has,two,rows']
    reader = FancyReader(lines)
    row = next(reader)
    assert ("my", "fake", "file") == (row.w1, row.w2, row.w3)
    row = next(reader)
    assert ("has", "two", "rows") == (row.w1, row.w2, row.w3)


def test_bonus3():
    lines = 'red,1\nblue,2\ngreen,3'.splitlines()
    reader = FancyReader(lines, fieldnames=['color', 'numbers'])
    assert repr(next(reader)) == "Row(color='red', numbers='1')"
    assert reader.line_num == 1
    next(reader)
    assert reader.line_num == 2
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