/**
    Given the root of a binary tree, return the inorder traversal of its nodes' values

    Constraints:
        The number of nodes in the tree is in the range [0, 100].
        -100 <= Node.val <= 100

 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
const inorderTraversal = function (root) {
    // return iterableInorderTraversal(root);

    let levels = [];
    recursiveInorderTraversal(root, levels);
    return levels;
};

/**
 *
 * @param {*} root
 * @param {*} levels running array of levels (passed by reference)
 * @returns current state of array of level values
 */
const recursiveInorderTraversal = function (root, levels) {
    if(root === null || root === undefined) {
        return levels
    }

    recursiveInorderTraversal(root.left, levels);
    levels.push(root.val);
    recursiveInorderTraversal(root.right, levels);
    return levels;
};

/**
 * Build a stack starting from the far left and print levels
 */
const iterableInorderTraversal = function (root) {
    let stack = [];
    let levels = [];

    while(root !== null || stack.length !== 0) {
        // Add all the far left nodes available from current root to the stack:
        while(root !== null) {
            stack.push(root);
            root = root.left;
        }
        // Start working backwards by popping off the top of the stack.
        root = stack.pop();
        levels.push(root.val);
        root = root.right;
    }
    return levels;
};

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
};
