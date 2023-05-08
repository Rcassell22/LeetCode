import unittest

from Python.easy.easy_problem_744 import Solution

class TestNextGreatestLetter(unittest.TestCase):

    def test_case_1(self):
        test_letters = ["c", "f", "j"]
        test_target = "a"
        expected_result = "c"

        test_solution = Solution()
        result = test_solution.next_greatest_letter(test_letters, test_target)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_letters = ["c", "f", "j"]
        test_target = "c"
        expected_result = "f"

        test_solution = Solution()
        result = test_solution.next_greatest_letter(test_letters, test_target)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        test_letters = ["x", "x", "y", "y"]
        test_target = "z"
        expected_result = "x"

        test_solution = Solution()
        result = test_solution.next_greatest_letter(test_letters, test_target)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()