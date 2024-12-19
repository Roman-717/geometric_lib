import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_area_first(self):
        self.assertEqual(area(3, 4), 6)
    
    def test_area_second(self):
        self.assertAlmostEqual(area(1, 5), 2.5, places=1)

    def test_perimeter_first(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_second(self):
        self.assertEqual(perimeter(2, 6, 7), 15)

if __name__ == '__main__':
    unittest.main()
