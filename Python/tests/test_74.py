import unittest

from Python.medium.medium_problem_74 import Solution

class TestSearchMatrix(unittest.TestCase):

    def test_case_1(self):
        test_matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        test_target = 3

        expected_result = True
        result = Solution().search_matrix(test_matrix, test_target)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        test_target = 13

        expected_result = False
        result = Solution().search_matrix(test_matrix, test_target)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        test_matrix = [[1]]
        test_target = 1

        expected_result = True
        result = Solution().search_matrix(test_matrix, test_target)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()