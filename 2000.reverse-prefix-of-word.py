#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
class reverseString:
    def reversePrefix(self, word: str, ch: str) -> str:
        if word.find(ch) == -1:
            return word
        
        first_idx = word.find(ch)

        to_reverse = word[0:first_idx+1]
        reversed = ""

        for i in range(len(to_reverse)):
            reversed += to_reverse[-(i+1)]

        return reversed + word[first_idx+1:]

        # word[:idx][::-1] + word[idx+1:]

# @lc code=end
if __name__ == "__main__":
    reverseString = reverseString()
    reverseString.reversePrefix("abcdefd", ch="d")
