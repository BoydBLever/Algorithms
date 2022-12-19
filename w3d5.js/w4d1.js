//ref:
//https://isaaccomputerscience.org/concepts/dsa_datastruct_stack?examBoard=all&stage=all
//Stack
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}
/**
 * Class to represent a stack using a linkedlist to store the stacked items.
 * Follows a LIFO (Last In First Out) order where new items are stacked on
 * top (back of array) and removed items are removed from the top / back.
 */
class Stack {
    constructor() {
        this.top = null;
    }

    isEmpty() {
        if (this.top == null) {
            return true;
        } else {
            return false;
        }



        //check if the stack is empty
        //return a boolean 

    }

    /**
   * Adds a new given item based on the to the top of this stack.
   * - Time: O(1) constant.
   * - Space: O(1) constant.
   * @param {any} item The new item to be added to the top.
   * @returns {number} .
   */

    // push(data) {
    //   let oldTop = this.top;
    //   this.top = newNode;
    //   newNode.next = oldTop;
    //   return newNode.data;
    // }
    push(newNode) { // same here, refer to SLL insertAtFront
        newNode.next = this.top;
        this.top = newNode;
        return this.top
    }


    /**
     * Removes the top / last item from this stack.
     * - Time: O(1) constant.
     * - Space: O(1) constant.
     * @returns {any} The removed item or undefined if this stack was empty.
     */
    pop() {
        if (this.isEmpty()) {
            return undefined;
        }
        let temp = this.top;
        this.top = this.top.next;

        return temp;
    }

    /**
   * Retrieves the top / last item from this stack without removing it.
   * - Time: O(1) constant.
   * - Space: O(1) constant.
   * @returns {any} The top / last item of this stack.
   */
    peek() {
        if (this.isEmpty()) {
            return undefined;
        } else {
            return this.top.data;
        }

    }


    /**
     * Returns the size of this stack.
     * DO NOT USE .next
     * @returns {number} The length.
     */
    size() {
        let temp = new Stack();
        let count = 0;

        //while this.top exists
        while (this.top) {
            count++;
            let node = this.pop();
            temp.push(node);
        }

        //while temp.top exists
        while (temp.top) {
            this.push(temp.pop());
        }
        return count;
    }
    printStack() { // For learning purpose
        console.log("TOP")
        let runner = this.top;
        while (runner) {
            console.log(runner.data);
            runner = runner.next
        }
    }
}

let s1 = new Stack();
s1.push(new Node(1));
s1.push(new Node(2));
s1.push(new Node(3));
s1.printStack();
// console.log(s1.isEmpty());
//expected:
// TOP
// [ 3 ] 
// [ 2 ]
// [ 1 ]

console.log(s1.pop()); //expected: [ 3 ]
s1.printStack();
//expected: 3
// TOP
// [ 2 ] 
// [ 1 ]
console.log("size: " + s1.size());
