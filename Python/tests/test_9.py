import unittest

from Python.easy.easy_problem_9 import Solution

class TestIsPalindrome(unittest.TestCase):

    def test_case_1(self):
        test_x = 121

        expected_result = True
        result = Solution().is_palindrome(test_x)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_x = -121

        expected_result = False
        result = Solution().is_palindrome(test_x)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        test_x = 10

        expected_result = False
        result = Solution().is_palindrome(test_x)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()