class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode{{val: {self.val}, left: {self.left}, right: {self.right}}}"

    def __str__(self) -> str:
        return f"TreeNode{{val: {self.val}, left: {self.left}, right: {self.right}}}"

