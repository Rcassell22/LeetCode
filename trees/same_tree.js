/**
 *
 * Given the roots of two binary trees p and q, write a function to check if they are the same or not.
 * Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
 *
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
const isSameTree = function(p, q) {
    let treesAreTheSame = false;

    if (p === null && q === null) { // If both trees are empty, they're equal
        treesAreTheSame = true;
    } else if (p !== null && q !== null) { // If both aren't empty, compare them
        treesAreTheSame = p.val === q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }

    return treesAreTheSame;
};

/******************************** HELPERS *************************************/
function TreeNode(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
}

/** https://stackoverflow.com/questions/48744012/how-to-make-binary-tree-from-array-in-javascript */
function insertNode(tree, value) {
    let node = tree, key;
    while (node.value !== value) {
         key = value < node.value ? 'left' : 'right';
         if (!node[key]) {
             node[key] = new TreeNode(value);
             break;
         }
         node = node[key];
    }
    return tree;
}


/******************************* TEST CASES **********************************/

const testCase1 = function() {
 const firstTreeValues = [1, 1];
 const secondTreeValues = [1, null, 1];

 const firstTree = firstTreeValues.reduce((t, v) => t ? insertNode(t, v) : new TreeNode(v), null);
 const secondTree = secondTreeValues.reduce((t, v) => t ? insertNode(t, v) : new TreeNode(v), null);


 const same = isSameTree(firstTree, secondTree);
 console.log(same);

};

testCase1();



