import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_first(self):
        self.assertAlmostEqual(area(1), 3.14159, places=5)

    def test_area_second(self):
        self.assertAlmostEqual(area(15), 706.8583, places=4)
    
    def test_area_third(self):
        self.assertAlmostEqual(area(0), 0, places=5)


    def test_perimeter_first(self):
        self.assertAlmostEqual(perimeter(1), 6.283185, places=6)

    def test_perimeter_second(self):
        self.assertAlmostEqual(perimeter(7), 43.982297, places=6)
    
    def test_perimeter_third(self):
        self.assertAlmostEqual(perimeter(0), 0, places=5)

if __name__ == '__main__':
    unittest.main()
