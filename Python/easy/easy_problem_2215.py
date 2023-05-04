class Solution(object):
    def find_difference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        distinct_nums1 = []
        distinct_nums2 = []
        for num1 in nums1:
            if num1 not in nums2 and num1 not in distinct_nums1:
                distinct_nums1.append(num1)
        for num2 in nums2:
            if num2 not in nums1 and num2 not in distinct_nums2:
                distinct_nums2.append(num2)
        return [distinct_nums1, distinct_nums2]