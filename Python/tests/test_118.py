import unittest

from Python.easy.easy_problem_118 import Solution

class TestGenerate(unittest.TestCase):

    def test_case_1(self):
        test_num_rows = 5
        expected_result = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

        result = Solution().generate(test_num_rows)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_num_rows = 1
        expected_result = [[1]]

        result = Solution().generate(test_num_rows)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()