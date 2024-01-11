from typing import Optional

from utility_classes.TreeNode import TreeNode


def convert_input(tree_str):
    return tree_str[1:-1].replace(" ", "").split(",")


# print(convert_input("[6, 2, 13, 1, 4, 9, 15, null, null, null, null, null, null, 14]"))
def parse_value(val):
    if val == "null":
        return None
    return int(val)


def build_binary_tree(tree_str):
    tree_arr = convert_input(tree_str)

    n = len(tree_arr)
    if n == 0:
        return None

    def inner(index: int = 0) -> Optional[TreeNode]:
        """Closure function using recursion bo build tree"""
        nonlocal tree_arr
        if n <= index or tree_arr[index] is None:
            return None

        node = TreeNode(parse_value(tree_arr[index]))
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()


# print(build_binary_tree("[6, 2, 13, 1, 4, 9, 15, null, null, null, null, null, null, 14]"))
