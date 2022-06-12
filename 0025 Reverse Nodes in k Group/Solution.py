from typing import Optional
from Utilities.ListNode import ListNode, printListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        result = ListNode(0)
        result_end = result
        current = head

        while current:
            node = current
            nodes = [node]
            done = False
            for i in range(k - 1):
                node = node.next
                nodes.append(node)
                if not node:
                    done = True
                    break

            if done:
                break
            current = None if not node else node.next

            for i in range(k):
                result_end.next = nodes[k - i - 1]
                result_end = result_end.next

            result_end.next = None

        result_end.next = current
        return result.next
