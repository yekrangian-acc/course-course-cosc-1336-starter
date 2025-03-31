import unittest
from src.homework.g_lists_and_tuples.lists import get_lowest_list_value, get_highest_list_value

class TestListsAndTuples(unittest.TestCase):
    def test_get_lowest_list_value(self):
        test_list = [8, 10, 1, 50, 20]
        self.assertEqual(get_lowest_list_value(test_list), 1)

    def test_get_highest_list_value(self):
        test_list = [8, 10, 1, 50, 20]
        self.assertEqual(get_highest_list_value(test_list), 50)

if __name__ == '__main__':
    unittest.main()