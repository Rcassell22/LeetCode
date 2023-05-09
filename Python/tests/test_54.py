import unittest

from Python.medium.medium_problem_54 import Solution

class TestIntersect(unittest.TestCase):

    def test_case_1(self):
        test_matrix = [[1,2,3],[4,5,6],[7,8,9]]
        expected_result = [1,2,3,6,9,8,7,4,5]

        result = Solution().spiral_order(test_matrix)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        expected_result = [1,2,3,4,8,12,11,10,9,5,6,7]

        result = Solution().spiral_order(test_matrix)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()