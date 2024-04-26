#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Tribonacci:
    def tribonacci(self, n: int) -> int:
        a, b, c = 1, 0, 0

        for _ in range(n):
            a, b, c = b, c, a + b + c

        return c
        

# @lc code=end
if __name__ == '__main__':
    tribonacci_ins = Tribonacci()
    tribonacci_ins.tribonacci(4)

