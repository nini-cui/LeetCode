#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
from collections import defaultdict, deque
class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        t, graph, q = [0] + [float("inf")] * n, defaultdict(list), deque([(0, k)])
        for u, v, w in times:
            graph[u].append((v, w))
        while q:
            time, node = q.popleft()
            if time < t[node]:
                t[node] = time
                for v, w in graph[node]:
                    q.append((time + w, v))
        mx = max(t)
        return mx if mx < float("inf") else -1
        
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
