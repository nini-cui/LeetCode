#
# @lc app=leetcode id=1376 lang=python3
#
# [1376] Time Needed to Inform All Employees
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager, informTime):
        if n == 1:
            return 0
        
        rel_map = defaultdict(list)
        
        # initalizing rel_map for building graph
        for emp,manager in enumerate(manager):
            rel_map[manager].append(emp)
            
        # now calculate time for each leaf node and find max
        def dfs(eid): 
            # no further subordinate
            if not rel_map.get(eid):
                return 0
            
            time = informTime[eid]
            print(f'time is: {time}') 

            max_subordinate_time = 0

            for cid in rel_map.get(eid):
                print(f'cid is {cid}')
                current_time = dfs(cid)
                
                if current_time > max_subordinate_time:
                    max_subordinate_time = current_time

            time += max_subordinate_time

            return time
        
        return dfs(headID)

        # if n <= 1:
        #     return 0
        # rst = 0
        # childs = defaultdict(list)
        # for idx, parent in enumerate(manager):
        #     childs[parent].append(idx)

        # q = deque([(headID, informTime[headID])])
        # while q:
        #     cur_id, cur_time = q.popleft()
        #     # calculate max
        #     rst = max(rst, cur_time)
        #     for child in childs[cur_id]:
        #         q.append((child, cur_time + informTime[child]))
        # return rst
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.numOfMinutes(6, 2, [2,2,-1,2,2,2,1,6], [0,1,1,0,0,1,1])
