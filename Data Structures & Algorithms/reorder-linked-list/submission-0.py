class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None or head.next.next == None:
            return None

        start, end = head, head
        length = 1

        while end.next != None:
            end = end.next
            length += 1

        # split: how many nodes stay in the first half? (test 4 and 5)
        firstHalf = length // 2
        end = head
        for num in range(firstHalf):          # walk to the LAST node of the first half
            end = end.next
        second = end.next              # save where the second half begins
        end.next = None                    # cut the first half off
        end = second

        prev = None
        while end != None:
            temp = end.next
            end.next = prev
            prev = end
            end = temp

        end = prev

        # weave: save both nexts, rewire, advance both
        while start != None and end != None:
            startNext = start.next
            endNext = end.next
            start.next = end
            end.next = startNext
            start = startNext
            end = endNext

        return None