# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        values = []
        while head and head.next:
            values.append(head)
            for value in values:
                if value== head.next:
                    return True
            head = head.next

        return False
            