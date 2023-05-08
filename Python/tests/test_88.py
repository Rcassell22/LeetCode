import unittest

from Python.easy.easy_problem_88 import Solution

class TestMerge(unittest.TestCase):

    def test_case_1(self):
        test_nums_1 = [1,2,3,0,0,0]
        test_m = 3
        test_nums_2 = [2,5,6]
        test_n = 3

        expected_result = [1,2,2,3,5,6]
        result = Solution().merge(test_nums_1, test_m, test_nums_2, test_n)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_nums_1 = [1]
        test_m = 1
        test_nums_2 = []
        test_n = 0

        expected_result = [1]
        result = Solution().merge(test_nums_1, test_m, test_nums_2, test_n)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        test_nums_1 = [0]
        test_m = 0
        test_nums_2 = [1]
        test_n = 1

        expected_result = [1]
        result = Solution().merge(test_nums_1, test_m, test_nums_2, test_n)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()