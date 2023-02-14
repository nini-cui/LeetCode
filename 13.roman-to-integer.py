#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class RomanToInt:
    def romanToInt(self, s: str) -> int:
        symbol_value = {'I':1, 'V':5, 'X':10, 'L':50,
                        'C':100, 'D':500, 'M':1000
                        }
        symbol_value_list = {'IV': 4, 'IX': 9, 'XL': 40,
                             'XC': 90, 'CD': 400, 'CM': 900}

        i=sum=counter = 0
        
        while i < (len(s) - 1):
            current_symbol = s[i]
            next_symbol = s[i+1]
            concatenated_symbol = current_symbol + next_symbol
            if concatenated_symbol in symbol_value_list:
                current_value = symbol_value_list[concatenated_symbol]
                sum += current_value
                i += 2
                counter += 2
            else:
                current_value = symbol_value[s[i]]
                sum += current_value
                i += 1
                counter += 1

        if counter == (len(s) - 1):
            sum += symbol_value[s[len(s)-1]]

        return sum

        # for i in range(len(s)-1, 0, -2):
        #     current_value = symbol_value[s[i]]
        #     next_value = symbol_value[s[i-1]]
        #     if current_value == next_value:
        #         sum += 2*current_value
        #     elif current_value > next_value:
        #         sum += (current_value - next_value)
        #     else:
        #         sum += (current_value + next_value)
                
        # if len(s) % 2 != 0:
        #     sum += symbol_value[s[0]]
        
        return sum

if __name__ == '__main__':
    # print(RomanToInt().romanToInt("III"))
    # print(RomanToInt().romanToInt("LVIII"))
    print(RomanToInt().romanToInt("MCMXCIV"))

# @lc code=end

