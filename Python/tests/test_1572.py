import unittest

from Python.easy.easy_problem_1572 import Solution

class TestDiagonalSum(unittest.TestCase):

    def test_case_1(self):
        test_mat = [[1,2,3],
                    [4,5,6],
                    [7,8,9]]

        expected_result = 25

        result = Solution().diagonal_sum(test_mat)

        self.assertEquals(result, expected_result)

    def test_case_2(self):
        test_mat = [[1,1,1,1],
                    [1,1,1,1],
                    [1,1,1,1],
                    [1,1,1,1]]

        expected_result = 8

        result = Solution().diagonal_sum(test_mat)

        self.assertEquals(result, expected_result)

    def test_case_3(self):
        test_mat = [[5]]

        expected_result = 5

        result = Solution().diagonal_sum(test_mat)

        self.assertEquals(result, expected_result)

if __name__ == '__main__':
    unittest.main()