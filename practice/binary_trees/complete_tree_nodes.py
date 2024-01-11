# Definition for a binary tree node.
from math import ceil
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countNodes(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    reached = False
    bottom_level = -1
    bottom_pos = 0

    # Find the depest level O(log n)
    root_node = root
    while root_node:
        root_node = root_node.left
        bottom_level += 1

    # Search for the existance of a node at level and pos
    def exists_node(root, target, level) -> bool:
        node = root
        cur_level = level
        for i in range(level):
            if not node:
                return False
            # Left = True, Right = False
            dummy = [(2 ** (cur_level - 1)) - 1, target]
            direction = (2 ** (cur_level - 1)) - 1 >= target if level != 0 else target == 0
            if not direction:
                target -= (2 ** (cur_level - 1))
                node = node.right
            else:
                node = node.left
            cur_level -= 1

        return not (node is None)

    l = 0
    r = 2 ** bottom_level - 1
    bottom_level_nodes = 0

    while l <= r:
        mid = ceil((l + r) / 2)

        if l == r:
            bottom_level_nodes = r
            break

        if exists_node(root, mid, bottom_level):
            l = mid
        else:
            r = mid - 1

    print(bottom_level)
    return bottom_level_nodes + 2 ** (bottom_level - 1)


print(countNodes(TreeNode(0,
                          TreeNode(0,
                                   TreeNode(0,
                                            TreeNode(0),
                                            TreeNode(1)),
                                   TreeNode(1,
                                            TreeNode(2),
                                            TreeNode(3))),
                          TreeNode(1,
                                   TreeNode(2,
                                            TreeNode(4),
                                            TreeNode(5)),
                                   TreeNode(3,
                                            TreeNode(6),
                                            TreeNode(7)
                                            )))))
