class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next == None:           # <- still needed after your fix? trace [1], n=1
            return None

        length = 0
        temp = head
        while temp != None:
            length += 1
            temp = temp.next

        prev = None
        curr = head
        while length > n:
            prev = curr
            curr = curr.next
            length -= 1

        if prev == None:
            head = curr.next                 # <- removing the head and reassigning to the next node
        else:
            prev.next = curr.next

        return head