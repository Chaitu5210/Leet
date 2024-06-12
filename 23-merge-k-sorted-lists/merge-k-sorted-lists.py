# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        while(len(lists)>1):
            mergedlists=[]
            for i in range(0,len(lists),2):
                list1=lists[i]
                list2=lists[i+1] if i+1 < len(lists) else None
                mergedlists.append(self.merge(list1,list2))
            lists=mergedlists
        return lists[0]


    def merge(self,list1,list2):
        head=ListNode()
        tail=head
        while list1 and list2:
            if list1.val<list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        if list1:
            tail.next=list1
        if list2:
            tail.next=list2
        return head.next