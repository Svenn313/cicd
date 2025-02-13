#!/usr/bin/env python3

import unittest
from calc import addition, soustraction, multiplication, division

class testCalc(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2,4),6)
        self.assertEqual(addition(0,8),8)
        self.assertEqual(addition(-1,1),0)
        self.assertEqual(addition(-1,-3),-4)
        self.assertEqual(addition(-3,8),5)

    def test_soustraction(self):
        self.assertEqual(soustraction(4,2),2)
        self.assertEqual(soustraction(10,6),4)
        self.assertEqual(soustraction(0,3),-3)
        self.assertEqual(soustraction(-8,-3),-5)
        self.assertEqual(soustraction(-2,-4),2)

    def test_multiplication(self):
        self.assertEqual(multiplication(3,5),15)
        self.assertEqual(multiplication(-3,8),-24)
        self.assertEqual(multiplication(3,0),0)
        self.assertEqual(multiplication(-3,-4),12)

    def test_division(self):
        self.assertEqual(division(4,2),2)
        self.assertEqual(division(5,2),2.5)
        self.assertEqual(division(-4,2),-2)
        self.assertEqual(division(-4,-2),2)
        self.assertEqual(division(6,1),6)
        with self.assertRaises(ValueError):
            division(1, 0)






if __name__ == "__main__":
    unittest.main()
