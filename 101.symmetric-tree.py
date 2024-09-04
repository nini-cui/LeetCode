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
        for val in values:
            self.insert(self.root, val)
        return self.root
    
    def insert(self, root, value):
        if not root:
            self.root = TreeNode(value, None, None)
            return self.root
        
        q = deque()
        q.append(root)

        while q:
            current_node = q.popleft()

            if not current_node.left:
                current_node.left = TreeNode(value, None, None)
                break
            else:
                q.append(current_node.left)

            if not current_node.right:
                current_node.right = TreeNode(value, None, None)
                break
            else:
                q.append(current_node.right)

    def isTreeSymmetric(self, leftRoot, rightRoot):
        if not leftRoot and not rightRoot:
            return True
        
        if (not leftRoot and rightRoot) or (leftRoot and not rightRoot):
            return False
        
        if leftRoot.val != rightRoot.val:
            return False
        
        return self.isTreeSymmetric(leftRoot.left, rightRoot.right)

    def isSymmetric(self, root):
        if not root:
            return None
        
        return self.isTreeSymmetric(root.left, root.right)

# @lc code=end
if __name__ == "__main__":
    isSymmetric = isSymmetric()
    root = isSymmetric.create_tree([1, 2, 2, 3, 4, 4, 3])
    isSymmetric.isSymmetric(root)

