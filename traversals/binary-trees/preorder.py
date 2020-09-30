from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = self.dfs(root, [])
        return result

    def dfs(self, root, result) -> List[int]:
        if root != None:
            result.append(root.val)

            if root.left != None:
                result = self.dfs(root.left, result)

            if root.right != None:
                result = self.dfs(root.right, result)

        return result
