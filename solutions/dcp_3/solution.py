import json


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    node_serialized = {}
    if root:
        node_serialized["val"] = root.val
        if root.left:
            node_serialized["left"] = serialize(root.left)
        if root.right:
            node_serialized["right"] = serialize(root.right)
    return json.dumps(node_serialized)


def deserialize(root_serialized):
    node_serialized = json.loads(root_serialized)
    root = None
    if node_serialized["val"]:
        root = Node(node_serialized["val"])
        if "left" in node_serialized:
            root.left = deserialize(node_serialized["left"])
        if "right" in node_serialized:
            root.right = deserialize(node_serialized["right"])
    return root


node = Node("root", Node("left", Node("left.left")), Node("right"))
assert deserialize(serialize(node)).left.left.val == "left.left"
