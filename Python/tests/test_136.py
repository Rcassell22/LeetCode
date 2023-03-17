import sys
import unittest
sys.path.append('../')

from easy.easy_problem_136 import Solution

class TestSingleNumber(unittest.TestCase):

    def test_case_1(self):
        test_nums = [2, 2, 1]
        expected_num = 1
        test_solution = Solution()
        result = test_solution.single_number(test_nums)

        self.assertEqual(expected_num, result)

    def test_case_2(self):
        test_nums = [4, 1, 2, 1, 2]
        expected_num = 4
        test_solution = Solution()
        result = test_solution.single_number(test_nums)

        self.assertEqual(expected_num, result)

    def test_case_3(self):
        test_nums = [1]
        expected_num = 1
        test_solution = Solution()
        result = test_solution.single_number(test_nums)

        self.assertEqual(expected_num, result)

if __name__ == '__main__':
    unittest.main()