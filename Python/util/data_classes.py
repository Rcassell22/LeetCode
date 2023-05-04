class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_tree(self):
        '''
        Taken from https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
        '''
        if self.left:
            self.left.print_tree()
        print(self.val),
        if self.right:
            self.right.print_tree()

    def return_tree_as_array(self):
        '''
        Taken from https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
        '''
        tree_array = []
        if self.left:
            self.left.print_tree()
        print(self.val),
        if self.right:
            self.right.print_tree()