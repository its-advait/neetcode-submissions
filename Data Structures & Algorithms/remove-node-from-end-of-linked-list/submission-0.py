# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = []
        cur = head
        while cur:
            l.append(cur)
            cur = cur.next
        target = l[len(l)-n]
        cur = head
        target = len(l) - n
        if target == 0:
            return head.next

        l[target - 1].next = l[target].next

        return head

            
        

