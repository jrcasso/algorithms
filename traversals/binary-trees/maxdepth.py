# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        queue = [(0, root)]
        results = []
        if root:
            while queue:
                (depth, node) = queue.pop(0)
                try:
                    if results[depth] is not None:
                        results[depth].append(node.val)
                except IndexError:
                    results.append([node.val])

                if node.left is not None:
                    queue.append((depth + 1, node.left))
                if node.right is not None:
                    queue.append((depth + 1, node.right))
            return len(results)
        else:
            return 0
