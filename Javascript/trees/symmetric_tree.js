/**
 * Given the root of a binary tree,
 * check whether it is a mirror of itself (i.e., symmetric around its center).
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
const isSymmetric = function(root) {
    let symmetricTrees = false;
    const leftSide = root.left;
    const rightSide = root.right;

    symmetricTrees = isSymmetricTree(leftSide, rightSide);

    return symmetricTrees
};

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

/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
const isSymmetricTree = function(p, q) {
    let treesAreSymmetric = false;

    if (p === null && q === null) { // If both trees are empty, they're equal
        treesAreSymmetric = true;
    } else if (p !== null && q !== null) { // If both aren't empty, compare them
        treesAreSymmetric = p.val === q.val && isSymmetricTree(p.left, q.right) && isSymmetricTree(p.right, q.left);
    }

    return treesAreSymmetric;
};


/******************************* TEST CASES **********************************/

const testCase1 = function() {
    const treeValues = [1,2,2,3,4,4,3];

    const tree = buildTree(treeValues);
    const symmetric = isSymmetric(tree);
    console.log(symmetric);

};

testCase1();