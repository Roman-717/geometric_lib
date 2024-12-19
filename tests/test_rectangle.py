import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_first(self):
        self.assertEqual(area(2, 3), 6)
    
    def test_area_second(self):
        self.assertEqual(area(13, 17), 221)

    def test_perimeter_first(self):
        self.assertEqual(perimeter(2, 3), 10)
    
    def test_perimeter_second(self):
        self.assertEqual(perimeter(4, 9), 26)

if __name__ == '__main__':
    unittest.main()
