from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        result = head.next
        current = result.next
        result.next = head
        result.next.next = current
        current = result.next

        while True:
            if current is None or current.next is None or current.next.next is None:
                break

            y = current.next
            x = current.next.next.next
            current.next = y.next
            current.next.next = y
            y.next = x
            current = y

        return result

    def printNode(self, prefix: str, node: ListNode):
        if node is None:
            print(f"{prefix} None")
            return
        received = []
        i = 0
        while True:
            received.append(node.val)
            i += 1
            if i >= 10:
                break
            if node.next is None:
                break
            else:
                node = node.next
        print(f"{prefix} {received}")
