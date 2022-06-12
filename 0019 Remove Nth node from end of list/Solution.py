from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        previous = head
        while True:
            if previous.next is None:
                break
            length += 1
            previous = previous.next

        if length == n:
            if length == 1:
                return None
            else:
                return head.next

        mini_head = head
        for i in range(length - n - 1):
            mini_head = mini_head.next

        to_drop = mini_head.next
        new_child = to_drop.next
        if new_child is None:
            mini_head.next = None
        else:
            mini_head.next = new_child

        return head