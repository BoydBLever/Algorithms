// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/?envType=study-plan&id=algorithm-ii
// Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

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
// var deleteDuplicates = function(head) {
    
// };

// class ListNode {
//   constructor(val, next = null) {
//     this.val = val;
//     this.next = next;
//   }
// }

var deleteDuplicates = function(head) {
    if (!head) return head;
    
    const dummy = new ListNode(0, head);
    let prev = dummy;
    let current = head;
    
    while (current) {
      while (current.next && current.val === current.next.val) {
        current = current.next;
      }
      if (prev.next === current) {
        prev = prev.next;
      } else {
        prev.next = current.next;
      }
      current = current.next;
    }
    
    return dummy.next;
  };