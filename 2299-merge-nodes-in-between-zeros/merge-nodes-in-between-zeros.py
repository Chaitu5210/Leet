# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result=ListNode()
        temp=result
        sum=0
        while head:
            if head.val==0 and sum!=0:
                temp.next=ListNode(sum)
                temp=temp.next
                sum=0
            else:
                sum=sum+head.val
            head=head.next
        return result.next
        