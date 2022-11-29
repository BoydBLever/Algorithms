/** 
 * A class to represents a single item of a SinglyLinkedList that can be
 * linked to other Node instances to form a list of linked nodes.
 https://kalkicode.com/data-structure/single-linked-list-visualization
 */
class ListNode {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

/**
 * SLL(Singly Linked List) 
 * keeps track of the start (head) of the list and to store all the
 * functionality (methods) that each list should have.
 */
class SLL {
    constructor() {
        this.head = null;
    }

    /**
     * Determines if this list is empty.
     * @returns {boolean}
     */
    isEmpty() {
        if (this.head !== null) {
            return false;
        } else {
            return true;
        }
    }

    /**
     * Creates a new node with the given data and inserts it at the back of
     * this list.
     * @param {any} data The data to be added to the new node.
     * @returns {SinglyLinkedList} This list.
     */
    insertAtBack(data) {
        // Create a new node with the given value 
        // inserts it at the back of the list
        var newNode = new ListNode(data);
        // if(runner === null){
        //   runner.head = newNode;
        // }
        // HINT: How to find the last node of a Singly Linked List?
        var runner = this.head
        while (runner !== null) {
            if (runner.next == null) {
                runner.next = newNode;
                return this
            }
            runner = runner.next;

        }
        // level 1: insert a new node into list1
        // level 2: insert a new node into emptyList
    }


    insertAtBack2(data) {
        // Create a new node with the given value 
        // inserts it at the back of the list
        var newNode = new ListNode(data);
        if (this.isEmpty()) {
            runner.head = newNode;
            return this
        }
        // HINT: How to find the last node of a Singly Linked List?
        var runner = this.head
        while (!runner.next) {
            runner = runner.next;
        }
        runner.next = newNode;
        return this
        // level 1: insert a new node into list1
        // level 2: insert a new node into emptyList
    }

    // woww.. good job!! Looks like it's working?
    // need to test still
    //  ** BONUS: 
    //  * Calls insertAtBack on each item of the given array.
    //  * - Time: O(n * m) n = list length, m = arr.length.
    //  * - Space: O(1) constant.
    //  * @param {Array<any>} vals The data for each new node.
    //  * @returns {SinglyLinkedList} This list.
    // */
    nsertAtBackMany(vals) {
    }

    //given
    printList() {
        // if the list is empty?
        if (this.head === null) {
            console.log("this is an empty list")
            return this
        }
        // how to traverse through different nodes?
        // while-loop (as long as the node.next is not null)
        var runner = this.head
        while (runner !== null) {
            console.log(runner.data)
            runner = runner.next
        }
        return this

        // Can I chain all the methods?

    }
}

// instantiate nodes
var node1 = new ListNode(3)
var node2 = new ListNode(5)
var node3 = new ListNode(8)

node1.next = node2 // .next points to another node (not data)
node2.next = node3

// create empty list
var emptyList = new SLL();
// Head: NULL

var list1 = new SLL();
// head: (3) -> (5) -> (8) -> NULL
list1.head = node1;
// list1.insertAtBack(8)

// emptyList.printList()
// list1.printList()


list1.insertAtBack(10).insertAtBack(11).printList()
  // the above code will need chaining
  // emptyList.insertAtBack(10).insertAtBack(11).printList()








