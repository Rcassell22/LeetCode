import unittest

from Python.easy.easy_problem_169 import Solution

class TestMajorityElement(unittest.TestCase):

    def test_case_1(self):
        test_nums = [3, 2, 3]
        expected_result = 3
        test_solution = Solution()
        result = test_solution.majority_element(test_nums)

        self.assertEqual(expected_result, result)

    def test_case_2(self):
        test_nums = [2,2,1,1,1,2,2]
        expected_result = 2
        test_solution = Solution()
        result = test_solution.majority_element(test_nums)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()