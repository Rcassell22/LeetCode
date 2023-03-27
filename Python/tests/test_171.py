import sys
import unittest
#sys.path.append('../')

from easy.easy_problem_171 import Solution

class TestTitleToNumber(unittest.TestCase):

    def test_case_1(self):
        test_column_title = "A"
        expected_result = 1

        test_solution = Solution()
        result = test_solution.title_to_number(test_column_title)

        self.assertEqual(expected_result, result)

    def test_case_2(self):
        test_column_title = "AB"
        expected_result = 28

        test_solution = Solution()
        result = test_solution.title_to_number(test_column_title)

        self.assertEqual(expected_result, result)

    def test_case_3(self):
        test_column_title = "ZY"
        expected_result = 701

        test_solution = Solution()
        result = test_solution.title_to_number(test_column_title)

        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    unittest.main()