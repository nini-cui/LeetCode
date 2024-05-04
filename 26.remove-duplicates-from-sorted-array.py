#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
from typing import List
# @lc code=start
class Deduplicates:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1

        while fast in range(len(nums)):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow+1] = nums[fast]
                fast += 1
                slow += 1

        return slow + 1

        # unique_nums_lst = list(set(nums))

        # return len(unique_nums_lst)
        
# @lc code=end
if __name__ == "__main__":
    Deduplicates = Deduplicates()
    Deduplicates.removeDuplicates([1, 1, 2, 3, 3, 4])
