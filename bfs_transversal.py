"""print out a binary tree with breadth first search (BFS)
Example:
    2
    -   3
        -   1
    -   4
        -   6
        -   5
    Output:
    2
    34
    125
"""

class BinaryNode:
    val = None
    level = None
    left = None
    right = None
    def __init__(self, val, level=None):
        self.val = val
        self.level = level
    def __str__(self):
        tree_out = "{{[Node] Level: {},\nValue: {},\nLeft: {}, Right: {}}}".format(self.level, self.val, self.left, self.right)
        return tree_out

class BinaryTree:
    def __init__(self, root_node):
        self.root_node = root_node
    def __str__(self):
        return self.root_node.__str__()
    # def add_node(self, )

if __name__ == "__main__":
    two = BinaryNode(2, 1)
    three = BinaryNode(3, 2)
    four = BinaryNode(4, 2)
    one = BinaryNode(1, 3)
    six = BinaryNode(6, 3)
    five = BinaryNode(5, 3)


    three.left = one
    four.left = six
    four.right = five

    two.left = three
    two.right = four
    # two.level = 1

    print(two)
    print(four)