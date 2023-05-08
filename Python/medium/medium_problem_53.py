class Solution(object):
    def max_sub_array(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Given an integer array nums, find the subarray with the largest sum,
        and return its sum.
        """
        current_max = nums[0]
        working_max = nums[0]

        index = 1
        while index < len(nums):
            current_max = max(nums[index], current_max + nums[index])
            working_max = max(working_max, current_max)
            index += 1
        return working_max