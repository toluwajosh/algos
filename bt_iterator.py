"""bt_iterator




["BSTIterator","hasNext"]
[[[]],[null]]


["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]
[[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]
"""


def treeToList(tree):
    if tree is None:
        return []
    tree_list = [tree.val]
    if tree.left:
        tree_list = treeToList(tree.left) + tree_list
    if tree.right:
        tree_list = treeToList(tree.right) + tree_list
    return tree_list


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.root = root
        self.tree_list = []
        self.tree_iter = self.itGen()

    def itGen(self):
        self.tree_list = treeToList(self.root)
        self.tree_list = sorted(self.tree_list)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            return self.tree_list.pop(0)
        else:
            return None

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.tree_list) > 0:
            return True
        return False


# class BSTIterator:
#     def __init__(self, root):
#         self.root = root
#         self.tree_list = []
#         self.tree_iter = self.itGen()

#     def itGen(self):
#         # self.tree_list = treeToList(self.root)
#         self.tree_list = [1, 2, 3, 4, 5, 6]
#         self.tree_list = sorted(self.tree_list)

#     def next(self) -> int:
#         """
#         @return the next smallest number
#         """
#         if self.hasNext():
#             return self.tree_list.pop(0)
#         else:
#             return None

#     def hasNext(self) -> bool:
#         """
#         @return whether we have a next smallest number
#         """
#         if len(self.tree_list) > 0:
#             return True
#         return False


if __name__ == "__main__":
    bt_iter = BSTIterator(0)
    print(bt_iter.next())
    print(bt_iter.next())
    print(bt_iter.next())
    print(bt_iter.next())
    print(bt_iter.next())
    print(bt_iter.next())
    print(bt_iter.next())
    print(bt_iter.hasNext())
