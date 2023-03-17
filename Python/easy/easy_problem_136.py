

class Solution(object):
    """
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.
    """
    def single_number(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            if nums.count(num) == 1:
                return num
