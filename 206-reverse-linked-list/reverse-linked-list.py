# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node=None
        next_node=None
        while head != None:
            next_node=head.next
            head.next=prev_node
            prev_node=head
            head=next_node
        head=prev_node
        return head