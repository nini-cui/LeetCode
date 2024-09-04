#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class sortedArrayToBST:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        
        mid = len(nums)//2

        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
        
# @lc code=end

if __name__ == "__main__":
    sorted = sortedArrayToBST()
    sorted.sortedArrayToBST([-10, -3, 0, 5, 9])