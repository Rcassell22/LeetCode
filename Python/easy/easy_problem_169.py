class Solution(object):
    """
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.
    """
    def majority_element(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maj_ele = nums[0]
        maj_ele_count = 0
        nums_set = set(nums)
        for num in nums_set:
            num_count = nums.count(num)
            if num_count > maj_ele_count:
                maj_ele = num
                maj_ele_count = num_count
        return maj_ele