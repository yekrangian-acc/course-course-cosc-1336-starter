import unittest
from src.homework.b_in_proc_out.output import multiply_numbers 

class TestMultiplyNumbers(unittest.TestCase):
    
    def test_multiply_numbers_1(self):
        self.assertEqual(multiply_numbers(5, 5), 25)

    def test_multiply_numbers_2(self):
        self.assertEqual(multiply_numbers(10, 10), 100)

if __name__ == '__main__':
    unittest.main()