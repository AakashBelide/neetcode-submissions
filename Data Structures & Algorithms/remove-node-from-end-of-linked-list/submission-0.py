# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        start = head

        while start:
            start = start.next
            count += 1
        
        print(count)
        print(count - n)

        new_count = count - n
        if new_count == 0:
            head = head.next
            return head
        new_start = head

        while new_count>1:
            new_start = new_start.next
            new_count -= 1
        
        new_start.next = new_start.next.next
        return head