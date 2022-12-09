/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
const maxDepth = function(root) {
    if (root) {
        return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
    } else {
        return 0;
    }
};

const maxDepthWithoutExistingFunctions = function(root) {
    if (root) {
        let leftDepth = maxDepth(root.left);
        let rightDepth = maxDepth(root.right)
        return leftDepth > rightDepth ? leftDepth + 1 : rightDepth + 1;
    } else {
        return 0;
    }
}



/******************************** HELPERS *************************************/
class TreeNode {
    constructor(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

/* https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/435296/How-do-I-create-the-TreeNode-from-an-array-of-numbers-using-javascript-or-java */
const buildTree = function(inputArray) {
    const root = new TreeNode(inputArray.shift());
    const queue = [root];
    while (queue.length > 0 && inputArray.length > 0) {
      const curNode = queue.shift();
      const leftVal = inputArray.shift();
      const rightVal = inputArray.shift();
      if (leftVal !== null) {
        curNode.left = new TreeNode(leftVal);
        queue.push(curNode.left);
      }
      if (rightVal !== null) {
        curNode.right = new TreeNode(rightVal);
        queue.push(curNode.right);
      }
    }

    return root;
}

/******************************* TEST CASES **********************************/

const testCase1 = function() {
    const treeValues = [3,9,20,null,null,15,7];

    const tree = buildTree(treeValues);
    const depth = maxDepth(tree);
    console.log(depth);

};

testCase1();