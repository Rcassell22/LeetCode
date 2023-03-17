import sys
import unittest
#sys.path.append('../')

from easy.easy_problem_168 import Solution

class TestConvertToTitle(unittest.TestCase):

    def test_case_1(self):
        test_column_number = 1
        expected_column_title = "A"

        test_solution = Solution()
        result = test_solution.convert_to_title(test_column_number)
        self.assertEqual(expected_column_title, result)

    def test_case_2(self):
        test_column_number = 28
        expected_column_title = "AB"

        test_solution = Solution()
        result = test_solution.convert_to_title(test_column_number)
        self.assertEqual(expected_column_title, result)

    def test_case_3(self):
        test_column_number = 701
        expected_column_title = "ZY"

        test_solution = Solution()
        result = test_solution.convert_to_title(test_column_number)
        self.assertEqual(expected_column_title, result)

if __name__ == '__main__':
    unittest.main()