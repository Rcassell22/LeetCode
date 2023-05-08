import unittest

from Python.medium.medium_problem_53 import Solution

class TestMaxSubArray(unittest.TestCase):

    def test_case_1(self):
        test_nums = [-2,1,-3,4,-1,2,1,-5,4]
        expected_result = 6

        result = Solution().max_sub_array(test_nums)
        self.assertEquals(result, expected_result)

    def test_case_2(self):
        test_nums = [1]
        expected_result = 1

        result = Solution().max_sub_array(test_nums)
        self.assertEquals(result, expected_result)


    def test_case_3(self):
        test_nums = [5,4,-1,7,8]
        expected_result = 23

        result = Solution().max_sub_array(test_nums)
        self.assertEquals(result, expected_result)

if __name__ == '__main__':
    unittest.main()