import unittest

from Python.easy.easy_problem_350 import Solution

class TestIntersect(unittest.TestCase):

    def test_case_1(self):
        test_nums1 = [1, 2, 2, 1]
        test_nums2 = [2, 2]

        expected_result = [2, 2]
        result = Solution().intersect(test_nums1, test_nums2)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_nums1 = [4,9,5]
        test_nums2 = [9,4,9,8,4]

        expected_result = [4, 9]
        result = Solution().intersect(test_nums1, test_nums2)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()