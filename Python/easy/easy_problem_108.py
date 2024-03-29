from typing import List, Optional
from Python.util.data_classes import TreeNode

class Solution:
    from util.data_classes import TreeNode
    '''
    Given an integer array nums where the elements are sorted in ascending order, convert it to a
    height-balanced binary search tree.
    '''
    @staticmethod
    def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[len(nums) / 2])
        # split the array, one half on one side, one half on the other
        root.left = Solution.sorted_array_to_bst(nums[:len(nums) / 2])
        root.right = Solution.sorted_array_to_bst(nums[(len(nums) / 2) + 1:])
        return root

