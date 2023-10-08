// https://leetcode.com/problems/add-two-numbers/
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     // Define the structure for a singly-linked list node.
 *     this.val = (val === undefined ? 0 : val);
 *     this.next = (next === undefined ? null : next);
 * }
 */

var addTwoNumbers = function(l1, l2) {
    // Initialize a dummy node with a value of `0`. This will be the starting point of our result linked list.
    let dummyHead = new ListNode(0);
    
    // Create a pointer `current` to keep track of the last node in the result linked list.
    let current = dummyHead;
    
    // Initialize a variable `carry` to keep track of any overflow from adding two digits.
    let carry = 0;

    // Use a loop to traverse both linked lists. If one linked list is shorter, we only traverse the longer one, 
    // and consider the values of the shorter list as `0`.
    while (l1 !== null || l2 !== null) {
        let sum = carry;  // Start with the carry from the previous iteration
        
        // If the current node in l1 is not null, add its value to the sum and move to the next node.
        if (l1 !== null) {
            sum += l1.val;
            l1 = l1.next;
        }
        
        // If the current node in l2 is not null, add its value to the sum and move to the next node.
        if (l2 !== null) {
            sum += l2.val;
            l2 = l2.next;
        }

        // Update the carry for the next iteration.
        carry = Math.floor(sum / 10);
        
        // Create a new node with the current sum modulo 10 (this gives the least significant digit of the sum).
        current.next = new ListNode(sum % 10);
        
        // Move the `current` pointer to the newly added node.
        current = current.next;
    }

    // If there's a carry left after both linked lists are traversed, add a new node with the carry value.
    if (carry > 0) {
        current.next = new ListNode(carry);
    }

    // Return the next node of the dummy node, which is the head of the result linked list.
    return dummyHead.next;
};
