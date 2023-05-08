class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Given two integer arrays nums1 and nums2, return an array of their intersection.

        Each element in the result must appear as many times as it shows in both arrays
        and you may return the result in any order.
        """
        nums1.sort()
        nums2.sort()

        intersecting_array = []

        nums1_index = 0
        nums2_index = 0

        while(nums1_index < len(nums1) and nums2_index < len(nums2)):
            if nums1[nums1_index] < nums2[nums2_index]:
                nums1_index += 1
            elif nums2[nums2_index] < nums1[nums1_index]:
                nums2_index += 1
            else:
                intersecting_array.append(nums1[nums1_index])
                nums1_index +=1
                nums2_index +=1
        return intersecting_array

