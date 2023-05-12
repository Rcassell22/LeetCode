import unittest
from Python.medium.medium_problem_2140 import Solution

class TestMostPoints(unittest.TestCase):

    def test_case_1(self):
        test_questions = [[3,2],[4,3],[4,4],[2,5]]

        expected_result = 5
        result = Solution().most_points(test_questions)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]

        expected_result = 7
        result = Solution().most_points(test_questions)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        test_questions = [[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]

        expected_result = 157
        result = Solution().most_points(test_questions)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()