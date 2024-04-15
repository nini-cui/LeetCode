#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class mergeLists:

    def list_to_linked_list(self, nums):
        if not nums:
            return None
        
        head = ListNode(nums[0])
        current = head

        for i in nums[1:]:
            current.next = ListNode(i)
            current = current.next

        return head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            cur = cur.next

        cur.next = list1 or list2
        res = dummy.next

        return res
            
# @lc code=end
if __name__ == "__main__":
    mergeLists = mergeLists()
    list1 = mergeLists.list_to_linked_list([1, 2, 4])
    list2 = mergeLists.list_to_linked_list([1, 3, 4])
    mergeLists.mergeTwoLists(list1, list2)



# class mergeLists:

#     def list_to_linked_list(self, nums):
#         if not nums:
#             return None
        
#         head = ListNode(nums[0])
#         current = head

#         for num in nums[1:]:
#             current.next = ListNode(num)
#             current = current.next

#         return head


#     def length_of_list(self, lst):
#         length = 0
#         current = lst
#         while current is not None:
#             length += 1
#             current = current.next
#         return length
    

#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if not list1 and list2:
#             return list2
        
#         if not list2 and list1:
#             return list1
        
#         if not list1 and not list2:
#             return list1
        
#         res = []

#         list1_idx = 0
#         list2_idx = 0
        
#         list1 = self.list_to_linked_list(list1)
#         list2 = self.list_to_linked_list(list2)

#         total_len = self.length_of_list(list1) + self.length_of_list(list2)

#         while len(res) != total_len:
#             if list1[list1_idx] > list2[list2_idx]:
#                 res.append(list2[list2_idx])
#                 list2_idx += 1
#             elif list1[list1_idx] < list2[list2_idx]:
#                 res.append(list1[list1_idx])
#                 list1_idx += 1
#             elif list1[list1_idx] == list2[list2_idx]:
#                 res.append(list1[list1_idx])
#                 res.append(list1[list1_idx])
#                 list1_idx += 1
#                 list2_idx += 1

#         return res
        