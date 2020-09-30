from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root:
            return self.bfs((0, root), [], [])
        else:
            return []
    def bfs(self, nextItem, result, queue):
        depth = nextItem[0]
        root = nextItem[1]
        
        try:
            if result[depth] is not None:
                result[depth].append(root.val)
        except IndexError:
                result.append([root.val])

        if root is not None:
            if root.left is not None:
                queue.append((depth + 1, root.left))
            if root.right is not None:
                queue.append((depth + 1, root.right))
        
        if len(queue) > 0:
            nextItem = queue.pop(0)
            return self.bfs(nextItem, result, queue)
        else:
            return result

