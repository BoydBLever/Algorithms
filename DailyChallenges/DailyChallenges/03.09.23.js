/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 */
var Solution = function(head) {
    this.head = head;
};

/**
 * Returns a random node's value.
 * @return {number}
 */
Solution.prototype.getRandom = function() {
    let count = 1;
    let result = this.head.val;
    let node = this.head.next;
    
    while (node) {
        const random = Math.floor(Math.random() * (count + 1));
        if (random === 0) {
            result = node.val;
        }
        count++;
        node = node.next;
    }
    
    return result;
};
// To solve this problem, we can use reservoir sampling technique. In reservoir sampling, we need to maintain a sample set of size 1. Then for each element in the linked list, we generate a random number between 0 and i (i is the index of the current element) inclusive. If the generated random number is 0, then we replace the element in the sample set with the current element.

// The probability of each element being selected is 1/i. When we reach the end of the linked list, the element in the sample set is the random node.

// The time complexity of this solution is O(n) and the space complexity is O(1).