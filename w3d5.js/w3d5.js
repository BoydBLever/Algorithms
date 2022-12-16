//From Morning Algo Friday December 16
/**
 * Class to represent a Node for a DoublyLinkedList.
 */
class DLLNode {
    /**
     * Executed when the new keyword is used to construct a new node instance.
     * @param {any} data The data the new node will store.
     */
    constructor(data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

/**
 * A class to represent a doubly linked list and contain all of it's methods.
 * A doubly linked list is a singly linked list that can be traversed in both
 * directions.
 */
class DoublyLinkedList {
    /**
     * Executed when the new keyword is used to construct a new DoublyLInkedList
     * instance that inherits these methods and properties.
     */
    constructor() {
        this.head = null;
        this.tail = null;
    }

    isEmpty() {
        return this.head === null;
    }
    toArray() {
        const vals = [];
        let runner = this.head;

        while (runner) {
            vals.push(runner.data);
            runner = runner.next;
        }
        return vals;
    }

    insertAtBack(data) {
        const newTail = new DLLNode(data);

        if (this.isEmpty()) {
            // if no head set the newTail to be both the head and the tail
            this.head = newTail;
            this.tail = newTail;
        } else {
            this.tail.next = newTail;
            newTail.prev = this.tail;

            this.tail = newTail;
        }
        return this;
    }
    /**
   * Converts this list to an array of the node's data.
   * - Time: O(n) linear, n = list length.
   * - Space: O(n) linear, array grows as list length increases.
   * @returns {Array<any>} All the data of the nodes.
   */
    toArray() {
        const vals = [];
        let runner = this.head;

        while (runner) {
            vals.push(runner.data);
            runner = runner.next;
        }
        return vals;
    }

    /**
     * Adds all the given items to the back of this list.
     * @param {Array<any>} items Items to be added to the back of this list.
     * @returns {DoublyLinkedList} This list.
     */
    insertAtBackMany(items = []) {
        items.forEach((item) => this.insertAtBack(item));
        return this;
    }

    /**
     * Inserts a new node with the given newVal after the node that has the
     * given targetVal as it's data.
     * - Time: O(?).
     * - Space: O(?).
     * @param {any} targetVal The node data to find.
     * @param {any} newVal Data for the new node.
     * @returns {boolean} Indicates if the new node was added.
     */
    // 1. Create the new node
    // 2. search for the targetVal by loop through the list (while loop)
    // 3. when the targetVal is found, move around the pointers

    insertAfter(targetVal, newVal) {

        var newNode = new DLLNode(newVal)


        let runner = this.head
        while (runner.data !== targetVal) {
            runner = runner.next;
        }
        let temp = runner.next;
        runner.next = newNode;
        newNode.next = temp;
        newNode.prev = runner
        // temp.prev = newNode

        return temp


    }

    /**
     * Inserts a new node with the given newVal before the node that has the
     * given targetVal as it's data.
     * - Time: O(?).
     * - Space: O(?).
     * @param {any} targetVal The node data to find.
     * @param {any} newVal Data for the new node.
     * @returns {boolean} Indicates if the new node was added.
     */
    insertBefore(targetVal, newData) {
        let newNode = new DLLNode(newData);
        //nextNode is our runner
        let nextNode = this.head
        while (nextNode.data !== targetVal) {
            nextNode = nextNode.next
        }
        newNode.prev = nextNode.prev;
        nextNode.prev = newNode;
        newNode.next = nextNode;
        if (newNode.prev != null) {
            newNode.prev.next = newNode;
        }

        else {
            head = newNode;
        }
        return nextNode
    }

    /**
     * Finds the given node in this list and removes it.
     * - Time: O(1) constant.
     * - Space: O(1) constant.
     * @param {DLLNode} node A node in this list.
     * @returns {DoublyLinkedList} This list.
     */
    removeData(data) {

        let runner = this.head
        while (runner.next.data !== data) {
            runner = runner.next;
        }
        runner.next = runner.next.next;
        runner.next.prev = runner.prev;
    }
}
const list1 = new DoublyLinkedList();
list1.insertAtBackMany([5, 7, 1, 4, 7])
console.log(list1.toArray())
list1.insertBefore(7, 8)


list1.removeData(7)

console.log(list1.toArray())
