from Utilities.ListNode import ListNode
from typing import Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        if k == 0:
            return head

        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next

        if k >= len(nodes):
            k = k % len(nodes)
        if k == 0:
            return head

        new_head = nodes[-k]
        front_tail = nodes[-(k+1)]
        front_tail.next = None
        tail = nodes[-1]
        tail.next = head

        return new_head
