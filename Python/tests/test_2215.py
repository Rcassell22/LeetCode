import sys
import unittest
sys.path.append('../')

from easy.easy_problem_2215 import Solution

class TestFindDifference(unittest.TestCase):

    def test_case_1(self):
        test_nums1 = [1, 2, 3]
        test_nums2 = [2, 4, 6]

        expected_result = [
            [1, 3],
            [4, 6]
        ]

        test_solution = Solution()
        result = test_solution.find_difference(test_nums1, test_nums2)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_nums1 = [1, 2, 3, 3]
        test_nums2 = [1, 1, 2, 2]

        expected_result = [
            [3],
            []
        ]

        test_solution = Solution()
        result = test_solution.find_difference(test_nums1, test_nums2)

        self.assertEqual(result, expected_result)

