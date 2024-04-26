#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class validParentheses:
    def isValid(self, s: str) -> bool:
        stack = [] 
        for c in s: 
            if c in '([{': 
                stack.append(c) 
            else: 
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False 
                stack.pop() 
        return not stack 

        # if len(s) % 2 != 0:
        #     return False
        
        # combo_parentheses = {"(": ")", "{": "}", "[": "]", ")": "(", "}": "{", "]": "["}

        # for i in range(int(len(s)/ 2)):
        #     mid_idx = int(len(s)/2)
        #     target_parenthese = combo_parentheses[s[mid_idx]]
        #     left_idx = s[0:mid_idx].rfind(target_parenthese)
        #     right_idx = s[mid_idx:].find(target_parenthese)

        #     if left_idx != -1:
        #         s = s[:left_idx] + s[left_idx+1:mid_idx] + s[mid_idx+1:]
        #     elif right_idx != -1:
        #         s = s[:mid_idx] + s[mid_idx+1:mid_idx+right_idx] + s[mid_idx+right_idx+1:]
        #     else:
        #         return False
        
        # if not s:
        #     return True
        # else:
        #     return False

# @lc code=end
if __name__ == "__main__":
    validParentheses = validParentheses()
    # validParentheses.isValid("([)]")
    # validParentheses.isValid("()[]{}")
    validParentheses.isValid("(([]){})")