#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
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
    
    def create_tree(self, values):
        for val in values:
            self.insert(self.root, val)
        return self.root
    
    def insert(self, root, val):
        if not root:
            self.root = TreeNode(val)
            return self.root
    
        q = []
        q.append(root)

        while len(q):
            node = q[0]
            q.pop(0)

            if not node.left:
                node.left = TreeNode(val)
                break
            else:
                q.append(node.left)

            if not node.right:
                node.right = TreeNode(val)
                break
            else:
                q.append(node.right)


    def minDepth(self, root):
        if not root:
            return 0

        q = deque()
        q.append(root)
        min_depth = 0

        while q: 
            # store all nodes on each level in ans
            ans = []
            min_depth += 1
            for element in q:
                if element.left:
                    ans.append(element.left)

                if element.right:
                    ans.append(element.right)

                if not element.left and not element.right:
                    return min_depth

            q = ans

        return min_depth

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    res = solution.create_tree([1, 2, 3, 4, 5])
    solution.minDepth(res)


