import unittest

from Python.medium.medium_problem_1035 import Solution

class TestMaxUncrossedLines(unittest.TestCase):

    def test_case_1(self):
        test_nums1 = [1,4,2]
        test_nums2 = [1,2,4]

        expected_result = 2
        result = Solution().max_uncrossed_lines(test_nums1, test_nums2)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_nums1 = [2,5,1,2,5]
        test_nums2 = [10,5,2,1,5,2]

        expected_result = 3
        result = Solution().max_uncrossed_lines(test_nums1, test_nums2)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        test_nums1 = [1,3,7,1,7,5]
        test_nums2 = [1,9,2,5,1]

        expected_result = 2
        result = Solution().max_uncrossed_lines(test_nums1, test_nums2)

        self.assertEqual(result, expected_result)





if __name__ == '__main__':
    unittest.main()