import unittest
from main import MiniCalculator


class TestCal(unittest.TestCase):

    def test_add(self):
        mini_instance = MiniCalculator()
        self.assertEqual(mini_instance.add(2,2), 4, "Adding 2 t0 2 should = 4")

    def test_subtract(self):
        mini_instances = MiniCalculator()
        self.assertEqual(mini_instances.subtract(2,2), 0, "it should be 0")