from typing import Optional, List

from utility_classes.TreeNode import TreeNode
from utility_funcs.arr_to_tree_nodes import build_binary_tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:

        arr = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            if root.val:
                nonlocal arr
                arr.append(root.val)
            inorder(root.right)

        inorder(root)
        n = len(arr)
        ans = {}
        answer = [[] for _ in range(len(queries))]
        global_max = arr[n - 1]
        global_min = arr[0]

        for i, query in enumerate(queries):
            if query in ans:
                answer[i] = answer[ans[query]]
                continue

            if query > global_max:
                answer[i] = [global_max, -1]

            if query < global_min:
                answer[i] = [-1, global_min]

            # Min

            cur_min = -1
            was_same = False
            l = 0
            r = n - 1
            while l <= r:
                mid = (l + r) // 2

                if arr[mid] == query:
                    cur_min = arr[mid]
                    was_same = True
                    break
                elif arr[mid] > query:
                    r = mid - 1
                    # cur_node = cur_node.left
                else:
                    l = mid + 1
                    cur_min = arr[mid]
                    # cur_node = cur_node.right

            if was_same:
                answer[i] = [cur_min, cur_min]
                continue

            # Max
            l = 0
            r = n - 1
            cur_max = -1
            while l <= r:
                mid = (l + r) // 2

                if arr[mid] == query:
                    cur_max = arr[mid]
                    break
                elif arr[mid] < query:
                    l = mid + 1
                    # cur_node = cur_node.right
                else:
                    r = mid - 1
                    cur_max = arr[mid]
                    # cur_node = cur_node.left
            answer[i] = [cur_min, cur_max]
            ans[query] = i

        return answer


sol = Solution()
print(sol.closestNodes(build_binary_tree("[6,2,13,1,4,9,15,null,null,null,null,null,null,14]"), [2, 5, 16]))
