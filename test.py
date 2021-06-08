import unittest
from main import MiniCalculator


class TestCal(unittest.TestCase):

    def test_add(self):
        mini_instance = MiniCalculator()
        self.assertEqual(mini_instance.add(2,2), 4, "Adding 2 t0 2 should = 4")
