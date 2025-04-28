import unittest
from src.homework.j_classes.class_a import Die

class TestDie(unittest.TestCase):
    def test_roll_values(self):
        die = Die()
        for _ in range(3):
            value = die.roll()
            self.assertTrue(1 <= value <= 6, f"Rolled value {value} is not between 1 and 6")
            self.assertEqual(value, die.get_rolled_value(), "get_rolled_value() should return the last rolled value")

if __name__ == '__main__':
    unittest.main()