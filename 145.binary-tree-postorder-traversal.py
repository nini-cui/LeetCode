#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class postorderTraversal:
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

    def postorderTraversal(self, root):
        if root == None:
            return None
        
        stack1 = []
        stack1.append(self.root)
        stack2 = []
        res = []

        while len(stack1) != 0:
            node = stack1.pop()
            if node is not None:
                stack2.append(node)
            if node.left is not None:
                stack1.append(node.left)
            if node.right is not None:
                stack1.append(node.right)
                
        while True:
            if root == None or len(stack2) == 0:
                break

            node = stack2.pop()
            res.append(node.val)

        return res
# @lc code=end
if __name__ == "__main__":
    postorderTraversal = postorderTraversal()
    postorderTraversal.add_nodes([1, 2, 3, 4, 5, 6])
    postorderTraversal.postorderTraversal()
