# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        secound = slow.next
        prev = slow.next = None
        while secound:
            temp = secound.next
            secound.next = prev
            prev = secound
            secound = temp
        
        first, secound = head, prev
        while secound:
            temp1 , temp2 = first.next, secound.next
            first.next = secound
            secound.next = temp1
            first, secound = temp1, temp2
        