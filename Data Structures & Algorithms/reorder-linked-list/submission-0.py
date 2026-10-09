class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current = head
        t = []

        while current:
            t.append(current)
            current = current.next

        res = node = ListNode()
        left = 0
        right = len(t) - 1

        while left <= right:
            node.next = t[left]
            node = node.next

            if left != right:
                node.next = t[right]
                node = node.next

            left += 1
            right -= 1

        node.next = None