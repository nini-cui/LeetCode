#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts):
        graph = defaultdict(set)
        names = {}
        visited = []
        res = []

        for account in accounts:
            name = account[0]

            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)
                names[email] = name

        def dfs(email, ans):
            if email not in visited:
                visited.append(email)
                ans.append(email)

                for ele in graph[email]:
                    dfs(ele, ans)

            return ans

        for email in graph:
            if email not in graph:
                return None
            
            ans = []
            ans = dfs(email, ans)
            if not ans:
                continue
            
            res.append([names[email]] + ans)

        return res

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    
    solution.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])



    



    
