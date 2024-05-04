#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
from typing import List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class preorderTraversal:
    def __init__(self):
        self.root = None

    def add_nodes(self, node_lst:List):
        for _ in node_lst:
            self.add(_)

    def contains(self, node, elem):
        if node == None:
            return False
        
        if node.val == elem:
            return True
        elif (node.val > elem):
            return self.contains(node.left, elem)
        else:
            return self.contains(node.right, elem)

    def __add(self, node, elem):
        if node == None:
            node = TreeNode(elem, None, None)
        else: 
            if node.val > elem:
                node.left = self.__add(node.left, elem)
            elif node.val < elem:
                node.right = self.__add(node.right, elem)

        return node

    def add(self, elem):
        if self.contains(self.root, elem):
            return False
        else:
            self.root = self.__add(self.root, elem)
            return True

    def preorderTraversalExec(self) -> List[int]:
        if self.root == None:
            return None
        
        stack, res = [], []

        stack.append(self.root)

        while True:
            if self.root is None or len(stack) == 0:
                break

            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

            res.append(node.val)

        return res




# @lc code=end
if __name__ == "__main__":
    preorderTraversal = preorderTraversal()
    preorderTraversal.add_nodes([1, None, 2, 3])
    preorderTraversal.preorderTraversalExec()