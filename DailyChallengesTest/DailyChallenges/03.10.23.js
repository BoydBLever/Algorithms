var sortedListToBST = function(head) {
    // Base case
    if (!head) {
        return null;
    }
    
    // Find the middle element of the linked list
    let slow = head;
    let fast = head;
    let prev = null;
    while (fast && fast.next) {
        prev = slow;
        slow = slow.next;
        fast = fast.next.next;
    }
    
    // Create a new tree node with the middle element as the root
    const root = new TreeNode(slow.val);
    
    // Recursively build the left and right subtrees
    if (prev) {
        prev.next = null;
        root.left = sortedListToBST(head);
    }
    root.right = sortedListToBST(slow.next);
    
    return root;
};
