#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def create_list(self, values):
        root = dummy = ListNode(0)

        for value in values:
            root.next = ListNode(value)
            root = root.next
        
        return dummy.next

    def deleteDuplicates(self, head):
        if not head:
            return None

        temp = head

        while temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    linked_lst = solution.create_list([1,1,2, 3, 3])
    solution.deleteDuplicates(linked_lst)
