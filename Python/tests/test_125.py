import unittest

from Python.easy.easy_problem_125 import Solution

class TestValidPalindrome(unittest.TestCase):

    def test_case_1(self):
        test_string = "A man, a plan, a canal: Panama"
        test_solution = Solution()
        result = test_solution.is_palindrome(test_string)
        self.assertTrue(result)

    def test_case_2(self):
        test_string = "race a car"
        test_solution = Solution()
        result = test_solution.is_palindrome(test_string)
        self.assertFalse(result)

    def test_case_3(self):
        test_string = " "
        test_solution = Solution()
        result = test_solution.is_palindrome(test_string)
        self.assertTrue(result)

    def test_case_4(self):
        test_string = "0P"
        test_solution = Solution()
        result = test_solution.is_palindrome(test_string)
        self.assertFalse(result)