# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        if list1 and list2 and list1.val <= list2.val:
            head1 = list1
            head2 = list2
        else:
            head1 = list2
            head2 = list1
        prev = None
        head = head1

        while head1 and head2:
            while head1 and head2 and head1.val <= head2.val:
                prev = head1
                head1 = head1.next
            
            prev.next = head2
            head2 = head2.next
            prev = prev.next
            prev.next = head1
        
        if head2:
            prev.next = head2
        return head
            
