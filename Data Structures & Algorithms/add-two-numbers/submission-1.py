# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2
        r = 0
        output = ListNode(None)
        head3 = output

        while head1 or head2:
            tmp = 0
            if head1:
                tmp += head1.val
                head1 = head1.next
            if head2:
                tmp += head2.val
                head2 = head2.next
            if r:
                tmp += r
            
            if tmp>10:
                r = tmp%10
                curr = tmp//10
            elif tmp == 10:
                curr = 0
                r = 1
            else:
                r = 0
                curr = tmp
            
            if r and tmp!=10:
                head3.next = ListNode(r)
                r = curr
            else:
                head3.next = ListNode(curr)
            head3 = head3.next
        
        if r:
            head3.next = ListNode(r)
        
        return output.next