from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    def printNode(self, prefix: str, node: ListNode):
        if not node:
            print(f"{prefix} None")
        received = []
        i = 0
        while True:
            i += 1
            if i > 10:
                break
            received.append(node.val)
            if node.next == None:
                break
            else:
                node = node.next

        print(f"{prefix} {received}")
