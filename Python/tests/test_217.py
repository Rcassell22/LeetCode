import unittest

from Python.easy.easy_problem_217 import Solution

class TestContainsDuplicate(unittest.TestCase):

    def test_case_1(self):
        test_nums = [1,2,3,1]
        expected_result = True

        result = Solution().contains_duplicate(test_nums)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_nums = [1,2,3,4]
        expected_result = False

        result = Solution().contains_duplicate(test_nums)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        test_nums = [1,1,1,3,3,4,3,2,4,2]
        expected_result = True

        result = Solution().contains_duplicate(test_nums)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()