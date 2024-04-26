#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class firstIdx:
    def strStr(self, haystack: str, needle: str) -> int:
        first_needle_char = needle[0]
        first_needle_char_idx = [i for i, ltr in enumerate(haystack) if ltr == first_needle_char]

        if not first_needle_char_idx:
            return -1

        needle_len = len(needle)
        haystack_len =len(haystack)

        for i in first_needle_char_idx:
            if (i + needle_len - 1) > haystack_len:
                continue

            if haystack[i:(i+needle_len)] == needle:
                return i
            
        return -1
# @lc code=end
if __name__ == "__main__":
    getIdx = firstIdx()
    # getIdx.strStr("sadbutsad", "sad")
    getIdx.strStr("mississippi", "issip")
