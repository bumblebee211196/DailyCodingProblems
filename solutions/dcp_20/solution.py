class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def array_to_llist(arr):
    head = temp = None
    for i, v in enumerate(arr):
        node = Node(v)
        if not head:
            head = node
            temp = head
        else:
            temp.next = node
            temp = node
    return head


def get_llist_len(head):
    temp = head
    count = 0
    while temp:
        count += 1
        temp = temp.next
    return count


def skip_nodes(head, n):
    for i in range(n):
        head = head.next
    return head


def solution(head1, head2):
    if not head1 or not head2:
        return
    l1, l2 = get_llist_len(head1), get_llist_len(head2)
    diff = abs(l1 - l2)
    if l1 >= l2:
        head1 = skip_nodes(head1, diff)
    else:
        head2 = skip_nodes(head2, diff)
    while head1 and head2:
        if head1.val == head2.val:
            return head1.val
        head1, head2 = head1.next, head2.next
    return


assert solution(array_to_llist([0, 3, 2, 7, 8, 10]), array_to_llist([99, 1, 8, 10])) == 8
assert solution(array_to_llist([7, 8, 10]), array_to_llist([99, 1, 8, 10])) == 8
assert not solution(array_to_llist([]), array_to_llist([]))
assert not solution(array_to_llist([1, 2]), array_to_llist([3, 4]))
