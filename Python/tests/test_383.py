import unittest

from Python.easy.easy_problem_383 import Solution

class TestCanConstruct(unittest.TestCase):

    def test_case_1(self):
        test_ransom_note = "a"
        test_magazine = "b"

        expected_result = False
        result = Solution().can_construct(test_ransom_note, test_magazine)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        test_ransom_note = "aa"
        test_magazine = "ab"

        expected_result = False
        result = Solution().can_construct(test_ransom_note, test_magazine)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        test_ransom_note = "aa"
        test_magazine = "aabb"

        expected_result = True
        result = Solution().can_construct(test_ransom_note, test_magazine)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()