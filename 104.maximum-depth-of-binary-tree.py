#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class maxDepth:
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
        
    # def maxDepth(self, root) -> int:
    #     if not root:
    #         return 0
        
    #     left_depth = self.maxDepth(root.left)
    #     right_depth = self.maxDepth(root.right)

    #     return max(left_depth, right_depth) + 1

    def maxDepth(self, root):
        if not root:
            return 0

        q = deque()
        q.append(root)
        max_depth = 0

        while q:
            max_depth += 1

            for i in range(len(q)):
                current_node = q.popleft()
                if current_node.left:
                    q.append(current_node.left)

                if current_node.right:
                    q.append(current_node.right)

        return max_depth

        
# @lc code=end

if __name__ == "__main__":
    maxdepth = maxDepth()
    res = maxdepth.create_tree([3, 9, 20, None, None, 15, 7])
    maxdepth.maxDepth(res)