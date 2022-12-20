//Tuesday, December 20, 2022
//Queue data structure
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

/**
 * Follows a FIFO (First In First Out) order where new items are added to the
 * back and items are removed from the front.
 */
class Queue {
    constructor() {
        this.front = null;
        this.rear = null;
    }

    /**
   * Returns whether or not this queue is empty.
   * - Time: O(1) constant.
   * - Space: O(1) constant.
   * @returns {boolean}
   */
    isEmpty() {
        if (this.front == null) {
            return true;
        }
        return false;
    }

    /**
   * Retrieves the first item without removing it.
   * - Time: O(1) constant.
   * - Space: O(1) constant.
   * @returns {any} The first item or undefined if empty.
   */
    getFront() {
        //return the front data
        if (this.isEmpty() == true) {
            return "List is empty."
        }
        return this.front;

    }

    /**
   * Adds a new given item to the back of this queue.
   * - Time: O(1) constant.
   * - Space: O(1) constant.
   * @param {any} item The new item to add to the back.
   */
    enqueue(newNode) {
        if (newNode == null) {
            return false
        }
        if (this.front == null) {
            this.front = newNode;
            this.rear = newNode;
            return 1;
        }
        this.rear.next = newNode
        this.rear = newNode;
        var count = 0;
        var current = this.front;
        while (current) {
            count++;
            current = current.next;
        }
        return count;
    }
    /**
     * Removes and returns the first item of this queue.
     * - Time: O(n) linear, due to having to shift all the remaining items to
     *    the left after removing first elem.
     * - Space: O(1) constant.
     * @returns {any} The first item or undefined if empty.
     */
    dequeue() {
        //if empty return NULL
        if (this.front == null)
            return;
        //Store previous front and move front one node ahead
        let temp = this.front;
        this.front = this.front.next;
        //the front becomes null, change rear to null
        if (this.front == null)
            rear = null;
    }

    // bonus
    /**
     Check if the target value exists in the queue using the basic queue operations
   * @returns {Boolean } 
   */
    contains(targetVal) {
        var q2 = new Queue();
        var foundVal = false;

        while (this.front) {
            if (this.front.data == targetVal) {
                foundVal = true;
            }
            q2.enqueue(this.dequeue());
        }

        while (q2.front) {
            this.enqueue(q2.dequeue());
        }
        return foundVal;
    }

    printQueue() { //for learning puspose
        console.log("Front: " + this.front.data);
        var runner = this.front;
        while (runner) {
            console.log(runner.data)
            runner = runner.next;
        }
        console.log("Rear: " + this.rear.data);
    }
}


var q = new Queue();
q.enqueue(new Node("a"));
q.enqueue(new Node("b"));
q.enqueue(new Node("c"));
q.enqueue(new Node("d"));
q.printQueue(); //expected: front: "a", rear : "d"
q.enqueue();
q.dequeue();
q.printQueue(); //expected: front: "b", rear : "d"

