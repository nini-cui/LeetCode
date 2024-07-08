#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
from collections import deque
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class isSymmetric:
    def __init__(self):
        self.root = None

    def create_tree(self, values):
        for value in values:
            self.insert(self.root, value)
        return self.root
    
    def insert(self, node, value):
        if not node:
            self.root = TreeNode(value, None, None)
            return self.root
        
        q = []

        q.append(node)

        while (len(q)):
            node = q[0]
            q.pop(0)

            if not node.left:
                node.left = TreeNode(value, None, None)
                break
            else:
                q.append(node.left)

            if not node.right:
                node.right = TreeNode(value, None, None)
                break
            else:
                q.append(node.right)
        
    def add_node(self, node, value):
        if node.left is None:
            node.left = TreeNode(value)
        elif node.right is None:
            node.right = TreeNode(value)
        
        return node

    def isSymmetric(self) -> bool:
        return self.isTreeSymmetric(self.root.left, self.root.right)
    
    def isTreeSymmetric(self, leftRoot, rightRoot):
        if leftRoot is None and rightRoot is None:
            return True
        if (leftRoot is None and rightRoot is not None) or (leftRoot is not None and rightRoot is None):
            return False
        if leftRoot.val != rightRoot.val:
            return False
        return self.isTreeSymmetric(leftRoot.left, rightRoot.right) and self.isTreeSymmetric(leftRoot.right, rightRoot.left)

# @lc code=end
if __name__ == "__main__":
    isSymmetric = isSymmetric()
    isSymmetric.create_tree([1, 2, 2, None, 4, 5, None])
    isSymmetric.isSymmetric()