//Friday December 2, 2022
//Room 5 w1d5.js

//Jump to line 123 for the second morning algo, to remove data from SLL.
// class Node 
class ListNode {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

// class SLL - Singly Linked List
class SLL {
    constructor() {
        this.head = null;
    }

    insertAtBack(data) {
        var newNode = new ListNode(data);
        if (this.head) {
            var runner = this.head;
            while (runner.next) {
                runner = runner.next;
            }
            runner.next = newNode;
        } else {
            this.head = newNode;
        }
    }
    //given
    printList() {
        if (!this.head) {
            console.log("Empty list");
            return
        }
        var runner = this.head;
        while (runner) {
            console.log(runner.data);
            runner = runner.next;
        }
    }
    // HEIDI HELP? not sure why runner.next or runner.next.next is not running properly/ getitng undefined
    /**
     * Retrieves the data of the second to last node in this list.
     * @returns {any} The data of the second to last node or null 
     *   if there is no second to last node.
     */
    secondToLast() {
        // EMPTY LIST: this.head ==null
        if (!this.head || !this.head.next) {
            // console.log("Empty list");
            return
        }

        var runner = this.head;
        while (runner.next.next) {
            runner = runner.next;
        }
        return runner.data
    }

    // NULL

    // (3) --> (5) --> (8) --> (10) --> NULL
    //                R      .next   .next 

    /**
     * Removes the node that has the matching given val as it's data.
     * @param {any} val The value to compare to the node's data 
     *   to find the node to be removed.
     * @returns {boolean} Indicates if a node was removed or not.
     */
    removeData(data) {
        if (!this.head) {
            console.log("Empty list");
            return
        }
        if (this.head.data == data) {
            this.head = this.head.next;
            return
        }
        var runner = this.head;
        if (runner.next) {
            while (runner) {
                if (runner.next.data == data) {
                    runner.next = runner.next.next;
                }
                runner = runner.next;
            }
        }
        return
    }
    // prev, curr
    // Base case : remove a middle node
    // Edge case1: remove the node if it is tail
    // Edge case2: remove the node if it is head

    // level1 : only remove the first matching item
    // level 2: remove all matching items
}


var list1 = new SLL();

var list2 = new SLL();
list2.insertAtBack(5);
list2.insertAtBack(6);
list2.insertAtBack(7);
list2.insertAtBack(8);
// console.log(list2.secondToLast());
//       HEAD
// list2: (1) --> (2) --> (3) --> null


// list1.printList();
list2.printList();
list2.removeData(6);
list2.printList();

//Friday December 2, 2022
//Morning Algo
//Room 1
// class Node 
// class ListNode {
//     constructor(data) {
//       this.data = data;
//       this.next = null;
//     }
//   }
  
//   // class SLL - Singly Linked List
//   class SLL {
//     constructor() {
//       this.head = null;
//     }
  
//     insertAtBack(data) {
//       var newNode = new ListNode(data);
//       if (this.head) {
//         var runner = this.head;
//         while (runner.next) {
//           runner = runner.next;
//         }
//         runner.next = newNode;
//       } else {
//         this.head = newNode;
//       }
//     }
//     //given
//     printList() {
//       if (!this.head) {
//         console.log("Empty list");
//         return
//       }
//       var runner = this.head;
//       while (runner) {
//         console.log(runner.data);
//         runner = runner.next;
//       }
//     }
  
//     /**
//      * Retrieves the data of the second to last node in this list.
//      * @returns {any} The data of the second to last node or null 
//      *   if there is no second to last node.
//      */
//     secondToLast() {
//       if (this.head){
//         if (this.head.next){
//           var runner = this.head;
//           while (runner.next.next) {
//             runner = runner.next;
//           }
//           return runner.data;
//         }
  
//         else{
//           return "Only one value."
//         }
//       }
  
//       else{
//         return "Empty list."
//       }
//     }
  
//     /**
//      * Removes the node that has the matching given val as it's data.
//      * @param {any} val The value to compare to the node's data 
//      *   to find the node to be removed.
//      * @returns {boolean} Indicates if a node was removed or not.
//      */
//     removeData(data) {
//       //HINT: The list is constructed by connecting nodes with pointers
//       // Play with the pointers so that you can remove that node from the list. 
//       if (this.head.data == data){
//         //if head is to be removed
//         // this.head = this.head.next;
//         //sets head.data = null
//         this.head.data = null;
//         //stores .next address
//         temp = this.head.next;
//         //clears .next address of head
//         this.head.next = null;
//         //sets head address to next node
//         this.head = temp;
//       }
  
//         //traverse list until desired node
//         var runner = this.head;
//         var sllChange = false;
//         while (runner != null && runner.next != null){
//           if (runner.next.data == data){
//             //address to the one after the deleted node
//             var temp = runner.next.next;
    
//             runner.next.data = null;
//             runner.next.next = null;
//             runner.next = temp;
    
//             sllChange = true;
//           }
//           else{
//           runner = runner.next;
//           }
//         }
//         //runner is either null or the nodeValue before the one to be removed
//         return sllChange;
      
//     }// prev, curr
//     // Base case : remove a middle node
//     // Edge case1: remove the node if it is tail
//     // Edge case2: remove the node if it is head
  
//     // level1 : only remove the first matching item
//     // level 2: remove all matching items
//   }
  
  
//   var list1 = new SLL();
  
//   var list2 = new SLL();
//   list2.insertAtBack(7);
//   list2.insertAtBack(5);
//   list2.insertAtBack(6);
//   list2.insertAtBack(7);
//   list2.insertAtBack(8);
//   list2.insertAtBack(7);
  
//   var list3 = new SLL();
//   list3.insertAtBack(5);
//   //       HEAD
//   // list2: (1) --> (2) --> (3) --> null
  
  
//   list1.printList();
//   list2.printList();
  
//   console.log(list1.secondToLast());
//   console.log(list2.secondToLast());
//   console.log(list3.secondToLast());
  
//   console.log(list2.removeData(7));
//   list2.printList();
  