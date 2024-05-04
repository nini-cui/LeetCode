#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class powerofTwo:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 1:
            return False
        elif n % 2 == 0:
            return self.isPowerOfTwo(n / 2)
        else:
            return False
        
# @lc code=end

if __name__ == "__main__":
    powerofTwo = powerofTwo()
    powerofTwo.isPowerOfTwo(16)
