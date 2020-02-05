"""binary tree second minimum node
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, val):
        # Compare the new value with the parent node
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val),
        if self.right:
            self.right.print_tree()


def treeList(root):
    tree_list = [root.val]
    if root.left:
        tree_list += treeList(root.left)
    if root.right:
        tree_list += treeList(root.right)
    return tree_list


def findSecondMinimumValue(root):
    tree_list = treeList(root)
    print(tree_list)
    min_val = min(tree_list)
    print("prev_min: ", min_val)
    tree_list.remove(min_val)
    min_val = min(tree_list)
    print("prev_min: ", min_val)

try:
    pass
except expression as identifier:
    pass

if __name__ == "__main__":
    my_tree = TreeNode(2)
    # my_tree.insert(6)
    # my_tree.insert(14)
    # my_tree.insert(3)
    # # my_tree.print_tree()

    tree_list = [2, 5, 5, 7]
    for i in tree_list:
        my_tree.insert(i)

    # print(findSecondMinimumValue(my_tree))
    # print(treeList(my_tree))
    findSecondMinimumValue(my_tree)
