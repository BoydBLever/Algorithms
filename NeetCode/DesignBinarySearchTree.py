from typing import List

class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)
        else:
            current = self.root
            while True:
                if key < current.key:
                    if current.left is None:
                        current.left = TreeNode(key, val)
                        break
                    else:
                        current = current.left
                elif key > current.key:
                    if current.right is None:
                        current.right = TreeNode(key, val)
                        break
                    else:
                        current = current.right
                else:  # key == current.key
                    current.val = val  # Update the value if key already exists
                    break
        self.size += 1

    def get(self, key: int) -> int:
        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val
        return None  # If key not found

    def getMin(self) -> int:
        current = self.root
        while current.left is not None:
            current = current.left
        return current.val

    def getMax(self) -> int:
        current = self.root
        while current.right is not None:
            current = current.right
        return current.val

    def remove(self, key: int) -> None:
        self.root = self._removeNode(self.root, key)

    def _removeNode(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._removeNode(node.left, key)
        elif key > node.key:
            node.right = self._removeNode(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            temp_val = self._getMinValueNode(node.right)
            node.key = temp_val.key
            node.val = temp_val.val
            node.right = self._removeNode(node.right, node.key)
        return node

    def _getMinValueNode(self, node):
        while node.left is not None:
            node = node.left
        return node

    def getInorderKeys(self) -> List[int]:
        keys = []
        self._inorderTraversal(self.root, keys)
        return keys

    def _inorderTraversal(self, node, keys):
        if node is not None:
            self._inorderTraversal(node.left, keys)
            keys.append(node.key)
            self._inorderTraversal(node.right, keys)

# Usage
tree_map = TreeMap()
tree_map.insert(10, 'Value for 10')
tree_map.insert(5, 'Value for 5')
tree_map.insert(20, 'Value for 20')

print(tree_map.get(10))  # Should print 'Value for 10'
print(tree_map.getMin())  # Should print 'Value for 5'
print(tree_map.getMax())  # Should print 'Value for 20'

tree_map.remove(10)
print(tree_map.get(10))  # Should print None
print(tree_map.getInorderKeys())  # Should print [5, 20]