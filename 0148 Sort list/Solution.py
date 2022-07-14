from Utilities.ListNode import ListNode, printListNode
from typing import Optional


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        current = head
        while current.next is not None:
            point = current
            lowest = current
            while point is not None:
                if lowest.val > point.val:
                    lowest = point
                point = point.next
            current.val, lowest.val = lowest.val, current.val
            current = current.next

        return head
