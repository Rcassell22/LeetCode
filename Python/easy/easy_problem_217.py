class Solution(object):
    def contains_duplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Given an integer array nums, return true if any value appears at least twice
         in the array, and return false if every element is distinct.
        """
        index = 0
        nums.sort()
        duplicates = False
        nums_size = len(nums)
        if nums_size == 1:
            duplicates = False
        else:
            while index < nums_size - 1:
                if nums[index] == nums[index+1]:
                    duplicates = True
                    break
                else:
                    index += 1
        return duplicates
