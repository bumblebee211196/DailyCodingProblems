class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def solution(head, k):
    curr1, curr2 = head, head
    for _ in range(k - 1):
        curr2 = curr2.next
    while curr2.next:
        curr1 = curr1.next
        curr2 = curr2.next
    return curr1.val


head = Node(10, Node(11, Node(12, Node(13, Node(14, Node(15, Node(16, Node(17))))))))

assert solution(head, 1) == 17
assert solution(head, 2) == 16
assert solution(head, 3) == 15
assert solution(head, 4) == 14
assert solution(head, 5) == 13
assert solution(head, 6) == 12
assert solution(head, 7) == 11
assert solution(head, 8) == 10
