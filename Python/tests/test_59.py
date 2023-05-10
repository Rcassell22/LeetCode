import unittest

from Python.medium.medium_problem_59 import Solution

class TestGenerateMatrix(unittest.TestCase):

    def test_case_1(self):
        test_n = 3
        expected_result = [[1,2,3],[8,9,4],[7,6,5]]

        result = Solution().generate_matrix(test_n)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_n = 1
        expected_result = [[1]]

        result = Solution().generate_matrix(test_n)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()