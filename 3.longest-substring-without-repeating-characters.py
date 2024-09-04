#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == 1:
            return 1

        ans = ""
        max_count = 0
        cur_count = 0
        for i in s:
            if i in ans:
                max_count = max(max_count, cur_count)
                ans = ans[ans.index(i)+1:] + i
                cur_count = len(ans)
            else:
                ans += i
                cur_count += 1

        return max(max_count, cur_count)
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.lengthOfLongestSubstring("pwwkew")














# if len(set(s)) == 1:
#             return 1

#         max_count = 0
#         current_count = 0
#         ans = ""

#         for i in s:
#             if i in ans:
#                 max_count = max(max_count, current_count)
#                 # get index then reset ans
#                 ans = ans[ans.index(i)+1:] + i
#                 current_count = len(ans)
#             else:
#                 ans += i
#                 current_count += 1

#         return max(max_count, current_count)