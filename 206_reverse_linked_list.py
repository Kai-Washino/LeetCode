# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = None
        tmp = head
        while tmp != None:
            answer = ListNode(tmp.val, answer)
            tmp = tmp.next    
        return answer