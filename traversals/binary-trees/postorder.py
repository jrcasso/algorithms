from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self.search(root, [])

    def search(self, root, result) -> List[int]:
        if root is not None:
            if root.left is not None:
                self.search(root.left, result)

            if root.right is not None:
                self.search(root.right, result)

            if root.val is not None:
                result.append(root.val)
        
            return result
        else:
            return []
