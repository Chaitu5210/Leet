# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head.val
        maximum_value=-1
        minimum_value=1000000
        head=head
        array=[]
        temp=1
        while head.next:
            if head.val>prev and head.val>head.next.val or head.val < prev and head.val < head.next.val:
                array.append(temp)
            prev=head.val
            head=head.next
            temp=temp+1
        if len(array)<2:
            return [-1,-1]
        maximum_value=array[len(array)-1]-array[0]
        for i in range(len(array)-1):
            minimum_value=min(minimum_value,array[i+1]-array[i])
        return [minimum_value,maximum_value]