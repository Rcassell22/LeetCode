import unittest

from Python.easy.easy_problem_121 import Solution

class TestMaxProfit(unittest.TestCase):

    def test_case_1(self):
        test_prices = [7,1,5,3,6,4]
        expected_result = 5

        result = Solution().max_profit(test_prices)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_prices = [7,6,4,3,1]
        expected_result = 0

        result = Solution().max_profit(test_prices)

        self.assertEqual(result, expected_result)



if __name__ == '__main__':
    unittest.main()