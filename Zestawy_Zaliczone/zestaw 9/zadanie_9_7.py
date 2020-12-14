class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def bst_max(top):
    if top == None:
        return None
    node = top
    while node.right:
        node = node.right
    return node


def bst_min(top):
    if top == None:
        return None
    node = top
    while node.left:
        node = node.left
    return node


root = Node(10)            #            10
root.left = Node(5)        #     5              12
root.right = Node(12)      # 4      6        11     13
root.left.left = Node(4)
root.left.right = Node(6)
root.right.left = Node(11)
root.right.right = Node(13)

print("bst_max: ", bst_max(root))
print("bst_min: ", bst_min(root))
