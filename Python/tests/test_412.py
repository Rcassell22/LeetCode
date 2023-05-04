import unittest

from Python.easy.easy_problem_412 import Solution

class TestFizzBuzz(unittest.TestCase):

    def test_case_1_decider(self):
        test_n = 3
        expected_result = "Fizz"

        result = Solution().fizz_buzz_decider(test_n)

        self.assertEqual(result, expected_result)

    def test_case_2_decider(self):
        test_n = 5
        expected_result = "Buzz"

        result = Solution().fizz_buzz_decider(test_n)

        self.assertEqual(result, expected_result)

    def test_case_3_decider(self):
        test_n = 15
        expected_result = "FizzBuzz"

        result = Solution().fizz_buzz_decider(test_n)

        self.assertEqual(result, expected_result)

    def test_case_1(self):
        test_n = 3
        expected_result = ["1", "2", "Fizz"]

        result = Solution().fizz_buzz(test_n)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_n = 5
        expected_result = ["1", "2", "Fizz", "4", "Buzz"]

        result = Solution().fizz_buzz(test_n)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        test_n = 15
        expected_result = ["1","2","Fizz","4","Buzz","Fizz",
                           "7","8","Fizz","Buzz","11","Fizz",
                           "13","14","FizzBuzz"]

        result = Solution().fizz_buzz(test_n)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()