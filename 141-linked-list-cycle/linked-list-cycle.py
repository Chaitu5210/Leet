# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        lister = set()
        current = head

        while current is not None:
            if current in lister:
                return True

            lister.add(current)
            current = current.next

        return False