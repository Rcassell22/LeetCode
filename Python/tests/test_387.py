import unittest

from Python.easy.easy_problem_387 import Solution

class TestFirstUniqChar(unittest.TestCase):

    def test_case_1(self):
        test_s = "leetcode"

        expected_result = 0
        result = Solution().first_uniq_char(test_s)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_s = "loveleetcode"

        expected_result = 2
        result = Solution().first_uniq_char(test_s)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        test_s = "aabb"

        expected_result = -1
        result = Solution().first_uniq_char(test_s)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()