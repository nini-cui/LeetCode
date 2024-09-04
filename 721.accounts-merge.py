#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
from collections import defaultdict
class Solution:
    # def combine_res(self, dict_res):
    #     outer_lst = []
    #     for (key, val) in dict_res.items():
    #         inner_lst = []
    #         inner_lst.append(key)
    #         inner_lst.extend(sorted(val))
    #         outer_lst.append(inner_lst)

    #     return outer_lst
    
    # def accountsMerge(self, accounts):
    #     res_dict = dict()
    #     dup_res_dict = dict()

    #     for i in accounts:
    #         name = i[0]
    #         emails = i[1:]
    #         if name not in res_dict:
    #             res_dict[name] = emails
    #         else:
    #             if bool(set(res_dict[name]) & set(emails)):
    #                 res_dict[name].extend(emails)
    #                 res_dict[name] = list(set(res_dict[name]))
    #             else:
    #                 dup_res_dict[name] = emails

    #     non_dup = self.combine_res(res_dict)
    #     dup = self.combine_res(dup_res_dict)
    #     final_res = non_dup + dup

    #     return final_res
    def accountsMerge(self, accounts):     
        visited_accounts = [False] * len(accounts)
        emails_accounts_map = defaultdict(list)
        res = []
        # Build up the graph.
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                emails_accounts_map[email].append(i)
        # DFS code for traversing accounts.
        def dfs(i, emails):
            if visited_accounts[i]:
                return
            visited_accounts[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in emails_accounts_map[email]:
                    dfs(neighbor, emails)
        # Perform DFS for accounts and add to results.
        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    solution.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])


    account             email
    -------------------------
    # 0                   johnsmith@mail.com
    # 0                   john00@mail.com
    # 1                   johnnybravo@mail.com
    # 2                   johnsmith@mail.com
    2                   john_newyork@mail.com
    3                   mary@mail.com

"johnsmith@mail.com": [0, 2]
"john00@mail.com": [1]
"johnnybravo@mail.com": [1]
"john_newyork@mail.com": [2]
"mary@mail.com": [3]

aggregate_res = []
for key, val in dict.items():
    aggregate_res.append([key, val])



    



    
