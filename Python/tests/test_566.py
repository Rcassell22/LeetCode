import unittest

from Python.easy.easy_problem_566 import Solution

class TestMatrixReshape(unittest.TestCase):

    def test_case_1(self):
        test_mat = [[1,2],[3,4]]
        test_r = 1
        test_c = 4

        expected_result = [[1,2,3,4]]
        result = Solution().matrix_reshape(test_mat, test_r, test_c)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_mat = [[1,2],[3,4]]
        test_r = 2
        test_c = 4

        expected_result = [[1,2],[3,4]]
        result = Solution().matrix_reshape(test_mat, test_r, test_c)

        self.assertEqual(result, expected_result)



if __name__ == '__main__':
    unittest.main()