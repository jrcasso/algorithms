# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.traverse(None, None, root)

    def traverse(self, grandparent: TreeNode, parent: TreeNode, root: TreeNode):
        total = 0
        try:
            if root.left:
                total += self.traverse(parent, root, root.left)
            if root.right:
                total += self.traverse(parent, root, root.right)
            if grandparent.val % 2 == 0:
                return total + root.val
            return total
        except AttributeError:
            # Occurs with null node reference (e.g. the first node has no grandparent) 
            return total
