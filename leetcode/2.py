from functools import reduce

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num_one = []
        num_two = []
        _sum = 0
        
        while l1:
            num_one.append(l1.val)
            l1 = l1.next
        while l2:
            num_two.append(l2.val)
            l2 = l2.next
        
        for i in range(len(num_one)):
            _sum += num_one[i] * (10 ** i)
            
        for i in range(len(num_two)):
            _sum += num_two[i] * (10 ** i)
            
        lst = list(map(int, list(str(_sum))))
        
        prev = None
        node = None
        
        for l in lst:
            node = ListNode(l)
            node.next = prev
            prev = node
        
        return node
            