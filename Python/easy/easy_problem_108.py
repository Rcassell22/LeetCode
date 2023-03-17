
from typing import List, Optional
from util.data_classes import TreeNode



class EasyProblem108:
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
        root.left = EasyProblem108.sorted_array_to_bst(nums[:len(nums) / 2])
        root.right = EasyProblem108.sorted_array_to_bst(nums[(len(nums) / 2) + 1:])
        return root



def main():
    test_nums_1 = [-10,-3,0,5,9]
    print('Test Case 1: ', EasyProblem108.sorted_array_to_bst(test_nums_1))

    test_nums_2 = [1,3]
    print('Test Case 1: ', EasyProblem108.sorted_array_to_bst(test_nums_2))

if __name__ == "__main__":
    main()
