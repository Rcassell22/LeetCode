/*

Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Constraints:
    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
const deleteDuplicates = function(head) {
    let workingArray = [];

    // Convert to array:
    while (head) {
        workingArray.push(head.val);
        head = head.next;
    }

    // Remove duplicates:
    const uniqueArray = [...new Set(workingArray)];

    // Return to a ListNode:
    let newHead = uniqueArray.reverse().reduce((node, val) => {
        if (node == null) {
            node = new ListNode(val);
        } else {
            node = new ListNode(val, node);
        }
        return node;
    }, null);
    return newHead;
};

function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}