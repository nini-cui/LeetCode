#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
from typing import List
# @lc code=start
class plusOne:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        res = []
        for i in range((len(digits)-1), -1, -1):
            sum += digits[i] * int('1' + '0' * (len(digits) - (i + 1)))
        
        sum += 1

        str_sum = str(sum)

        for _ in str_sum:
            res.append(_)

        return [int(_) for _ in res]
    
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     for i in range(1, len(digits)+1):
    #         if digits[-i] < 9:
    #             digits[len(digits) - i] = digits[-i] + 1
    #             return digits
    #         else:
    #             digits[len(digits) - i] = 0

    #             if i == len(digits):
    #                 digits = [1] + digits
    #                 return digits
    #             else:
    #                 continue
                
        
# @lc code=end

if __name__ == "__main__":
    plusOne = plusOne()
    # print(plusOne.plusOne([1, 2, 3]))
    print(plusOne.plusOne([1, 2, 3, 4]))