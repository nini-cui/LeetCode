#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        split_res = path.split('/')

        for res in split_res:
            if res == "." or not res:
                continue
            elif res == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(res)

        return '/' + '/'.join(stack)
        
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    solution.simplifyPath("/home//foo/")
