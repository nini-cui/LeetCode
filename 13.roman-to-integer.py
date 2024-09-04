#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class RomanToInt:
    def romanToInt(self, s: str) -> int:
        # MMMXLV
        symbol_val = {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000,
                    "IV": 4,
                    "IX": 9,
                    "XL": 40,
                    "XC": 90,
                    "CD": 400,
                    "CM": 900
        }

        sum = 0

        i = 0
        while i < (len(s) - 1):
            if s[i] + s[i+1] in symbol_val:
                sum += symbol_val[s[i]+s[i+1]]
                i += 2
            else:
                sum += symbol_val[s[i]]
                i += 1
            
        if i == len(s) - 1:
            sum += symbol_val[s[i]]

        return sum

        # symbol_val = {
        #             "I": 1,
        #             "V": 5,
        #             "X": 10,
        #             "L": 50,
        #             "C": 100,
        #             "D": 500,
        #             "M": 1000,
        #             "IV": 4,
        #             "IX": 9,
        #             "XL": 40,
        #             "XC": 90,
        #             "CD": 400,
        #             "CM": 900
        # }

        # res_sum = 0
        # i = 0
        
        # while i < (len(s) - 1):
        #     concatenate_str = s[i] + s[i+1]
        #     if concatenate_str in symbol_val:
        #         res_sum += symbol_val[concatenate_str]
        #         # move index 
        #         i  += 2
        #     else:
        #         res_sum += symbol_val[s[i]]
        #         i += 1  

        # if i == len(s) - 1:
        #     res_sum += symbol_val[s[i]]        
                
        # return res_sum 

if __name__ == '__main__':
    print(RomanToInt().romanToInt("MMMXLV"))
    # print(RomanToInt().romanToInt("LVIII"))
    # print(RomanToInt().romanToInt("MCMXCIV"))

# @lc code=end

