import unittest
from modules.geometry import Point


class TestPoint(unittest.TestCase):
    def test_eq_method_true(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        self.assertEqual(p1, p2)

    def test_eq_method_false(self):
        p1 = Point(1, 2)
        p2 = Point(2, 3)
        self.assertNotEqual(p1, p2)
