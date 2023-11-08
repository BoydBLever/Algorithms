# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
            # Since the list is singly linked, you can't access nodes randomly by index, so we need to know how far to iterate to reach the middle.
            # 1. Find the length of the list
            length = 0
            cur = head
            while cur:
                length += 1
                cur = cur.next
            
            # 2. Find the index of the middle node
            # middle represents the index of the middle node, and integer division is used to round down to the nearest whole number. If the list has an even number of nodes, the middle node is the second of the two middle nodes.
            middle = length // 2
            cur = head
            # The purpose of the second while loop is to move the cur pointer from the head of the list to the middle node. The loop starts with cur at the head, and middle holds the index of the middle node. Each iteration of the loop moves cur one node closer to the middle node. When middle reaches zero, cur will be at the middle node.
            while middle:
                cur = cur.next
                # middle variable is decremented to zero, the loop will terminate and cur will be returned.
                middle -= 1
            # Returns a single ListNode object representing the middle node of the list. This list if often represented by showing the values of all nodes starting from the returned node to the end of the list. The linked list is still a chain of ListNode objects, each with a .val and .next property.
            return cur # cur is the middle node i.e. the node with the value 3, and the output is displayed as [3,4,5] for head = [1,2,3,4,5]