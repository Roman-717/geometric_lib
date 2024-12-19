import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_first(self):
        self.assertEqual(area(4), 16)
    
    def test_area_second(self):
        self.assertEqual(area(1), 1)

    def test_perimeter_first(self):
        self.assertEqual(perimeter(4), 16)
    
    def test_perimeter_second(self):
        self.assertEqual(perimeter(1), 4)

if __name__ == '__main__':
    unittest.main()
