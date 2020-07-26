import unittest
from vector import Vector
from math import pi

class TestVector(unittest.TestCase):

    def test_vector(self):
        v1 = Vector(3,5,7)
        v2 = Vector(3,5,7)
        x,y,z = v1
        self.assertEqual((x,y,z),(3,5,7))
        self.assertEqual(v1,v2)

    def test_value_type(self):
        
        
        self.assertRaises(TypeError,Vector,3,5,"a")


