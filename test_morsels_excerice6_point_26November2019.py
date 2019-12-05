
from morsels_excerice6_point_26November2019 import Point
import pytest

@pytest.fixture
def point1():
    return Point(1,2,3)
@pytest.fixture
def point2():
    return Point(1,2,3)




def test_Point(point1,point2):
    assert point1 == point2
    point2.x = 4
    assert not point1 == point2
    assert str(point2) == "Point(x=4, y=2, z=3)"


def test_Point_bonus1(point1):
    p1 = point1
    p2 = Point(4, 5, 6)
    assert str(p1 + p2) == "Point(x=5, y=7, z=9)"
    p3 = p2 - p1
    print(p3)
    assert str(p3) == "Point(x=3, y=3, z=3)"

def test_Point_bonus2(point1):
    p2 = point1*2
    print(point1)
    assert str(p2) == "Point(x=2, y=4, z=6)"

def test_Point_bonus3(point1):
    x, y, z  = point1
    print((x, y, z))
    assert (x, y, z) == (1, 2, 3)


if __name__ == "__main__":
    # test_Point(point1,point2)
    p1  = Point(1,2,3)
    p2 = Point(4, 5, 6)
    print(p1)
    print(p2)
    
    print(p1+p2)
    print(p2-p1)

    p1 = Point(1, 2, 3)
    x, y, z = p1
    print((x, y, z))