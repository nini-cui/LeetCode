#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
from typing import List
from collections import deque
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class inorderTraversal:
    def __init__(self):
        self.root = None

    def contains(self, node, elem):
        if node == None:
            return False
        
        if node.val == elem:
            return True
        elif (elem < node.val):
            return self.contains(node.left, elem)
        else:
            return self.contains(node.right, elem)
        
    def add(self, elem):
        if self.contains(self.root, elem):
            return False
        else:
            self.root = self.__add(self.root, elem)
            return True
        
    def __add(self, node, elem):
        if node == None:
            node = TreeNode(elem, None, None)
        else:
            if elem < node.val:
                node.left = self.__add(node.left, elem)
            elif elem > node.val:
                node.right = self.__add(node.right, elem)
                
        return node
            
    def add_nodes(self, nodes_lst):
        for _ in nodes_lst:
            self.add(_)

    def inorderTraversal(self) -> List[int]:
        res = []

        stack = deque()

        stack.append(self.root)

        trav = self.root
        while True:
            if self.root == None or len(stack) == 0:
                break

            while trav != None and trav.left != None:
                stack.append(trav.left)
                trav = trav.left

            node = stack.pop()
            
            if node.right != None:
                stack.append(node.right)
                trav = node.right

            res.append(node.val)

        # res, stack = [], []

        # while True:
        #     while self.root:
        #         stack.append(self.root)
        #         self.root = self.root.left

        #     if not stack:
        #         return res
            
        #     node = stack.pop()
        #     res.append(node.val)
        #     self.root = node.right


# @lc code=end
if __name__ == "__main__":
    inorderTraversal = inorderTraversal()
    inorderTraversal.add_nodes([4, 2, 6, 3, 1, 7, 5])
    inorderTraversal.inorderTraversal()