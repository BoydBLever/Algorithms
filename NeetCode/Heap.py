# leftChild of i = heap[2 * i]
# rightChild of i = heap[(2 * i) + 1] 
# parent of i = heap[i // 2]

# pseudocode:
class Heap:
     heap = a list of integers, objects etc.
     constrtuctor():
        heap = intialize the list 
        heap.add(0)
