from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.search(root, [])

    def search(self, root, result) -> List[int]:
        if root is not None:
            if root.left is not None:
                self.search(root.left, result)

            if root.val is not None:
                result.append(root.val)

            if root.right is not None:
                self.search(root.right, result)
        
            return result
        else:
            return []
