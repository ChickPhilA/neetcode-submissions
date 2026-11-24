# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        if head.next == None:
            return head

        prev = None
        curr = head

        while curr != None:
            if curr.next != None:
                temp = curr.next
            else:
                temp = None

            curr.next = prev # going backwards
            prev = curr
            curr = temp

        return prev
