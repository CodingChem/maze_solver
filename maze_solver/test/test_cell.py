import unittest
from modules.geometry import Cell, Point


class TestCircle(unittest.TestCase):
    def test_get_center_returns_point(self):
        p1 = Point(1, 2)
        p2 = Point(2, 3)
        cell = Cell(None, p1, p2, False, False, False, False)  # pyright: ignore
        is_point = cell.get_center()
        self.assertIsInstance(is_point, Point)

    def test_get_center_returns_center(self):
        p1 = Point(100, 100)
        p2 = Point(200, 200)
        cell = Cell(None, p1, p2, False, False, False, False)  # pyright: ignore
        actual_center = cell.get_center()
        expected_center = Point(150, 150)

        self.assertEqual(actual_center, expected_center)
