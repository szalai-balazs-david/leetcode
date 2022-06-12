class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printListNode(prefix: str, node: ListNode):
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


def createListNode(values: list[int]) -> ListNode:
    result = ListNode(0)
    tail = result

    for value in values:
        tail.next = ListNode(value)
        tail = tail.next

    return result.next


def listNode2list(head: ListNode) -> list[int]:
    if not head:
        return []

    result = []
    i = 0
    while True:
        result.append(head.val)
        i += 1
        if i >= 10:
            break
        if head.next == None:
            break
        else:
            head = head.next

    return result
