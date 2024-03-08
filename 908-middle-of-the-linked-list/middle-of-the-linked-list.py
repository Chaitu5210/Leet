# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first=head
        second=head
        while(second is not None and second.next is not None):
            first = first.next
            second = second.next.next
        return first


        
        