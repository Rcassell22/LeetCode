import unittest

from Python.easy.easy_problem_1 import Solution

class TestTwoSum(unittest.TestCase):

    def test_case_1(self):
        test_nums = [2, 7, 11, 15]
        test_target = 9

        expected_result = [0,1]
        result = Solution().two_sum(test_nums, test_target)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_nums = [3,2,4]
        test_target = 6

        expected_result = [1,2]
        result = Solution().two_sum(test_nums, test_target)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        test_nums = [3,3]
        test_target = 6

        expected_result = [0,1]
        result = Solution().two_sum(test_nums, test_target)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()