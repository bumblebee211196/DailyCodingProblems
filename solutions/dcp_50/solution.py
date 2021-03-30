class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solution(root):

    def helper(node):
        if not node:
            return
        left = helper(node.left)
        right = helper(node.right)
        if left and right:
            if node.val == '+':
                return left + right
            if node.val == '-':
                return left - right
            if node.val == '*':
                return left * right
            if node.val == '/':
                return left / right
        return node.val

    return helper(root)


d = Tree(3)
e = Tree(2)
f = Tree(4)
g = Tree(5)

b = Tree("+")
b.left = d
b.right = e

c = Tree("+")
c.left = f
c.right = g

a = Tree("*")
a.left = b
a.right = c


assert solution(a) == 45
assert solution(c) == 9
assert solution(b) == 5
assert solution(d) == 3
