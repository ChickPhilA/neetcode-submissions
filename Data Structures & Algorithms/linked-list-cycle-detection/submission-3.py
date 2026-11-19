# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None:
            return False

        slow = head
        fast = head.next

        if fast == None:
            return False

        if fast.next == None:
            return False

        while (slow != fast):
            if fast.next == None:
                return False

            slow = slow.next
            fast = fast.next.next

            if fast == None:
                return False
        
        return True
        