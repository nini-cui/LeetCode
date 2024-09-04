#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.root = None

    def create_tree(self, lst):
        for ele in lst:
            self.insert(self.root, ele)
        
        return self.root

    def insert(self, root, ele):
        if not root:
            self.root = TreeNode(ele)
            return self.root
        
        q = []
        q.append(root)

        while q:
            node = q[0]
            q.pop(0)

            if not node.left:
                node.left = TreeNode(ele)
                break
            else:
                q.append(node.left)

            if not node.right:
                node.right = TreeNode(ele)
                break
            else:
                q.append(node.right)

    def levelOrder(self, root):
        if not root:
            return None

        q = deque()
        q.append(root)
        res = []

        while q:
            ans = []
            for i in range(len(q)):
                current_node = q.popleft()
                ans.append(current_node.val)

                if current_node.left:
                    q.append(current_node.left)

                if current_node.right:
                    q.append(current_node.right)
                    
            res.append(ans)
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    tree = solution.create_tree([3,9,20,None,None,15,7])
    solution.levelOrder(tree)
