#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wrapLines(self, words, count):
        # get the length of all words in a list
        # if i add another one and the length is < count
            # then I will add this word to the list
        # otherwise
            # I will concatenate all words in this list with a hypen, push it to res
            # I will update the len var
            # I will clear the current list, i will set the current i to be the only ele in the list
        
        res = []
        current_res = []
        current_len = 0

        for word in words:
            word_len = len(word)

            if current_res:
                word_len += 1

            if current_len + word_len > count:
                res.append("-".join(current_res))
                current_res = [word]
                current_len = word_len - 1
            else:
                current_res.append(word)
                current_len += word_len

        if current_res:
            res.append("-".join(current_res))

        print(res)

# [ "The-day-began",
#     "as-still-as",
#     "the-night",
#     "abruptly",
#     "lighted-with",
#     "brilliant",
#     "flame" ]

# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    solution.wrapLines(["The","day","began","as","still","as","the","night","abruptly","lighted","with","brilliant","flame"], 13)

'''
We are building a word processor and we would like to implement a "word-wrap" functionality.

Given a list of words followed by a maximum number of characters in a line, return a collection of strings where each string element represents a line that contains as many words as possible, 
with the words in each line being concatenated with a single '-' (representing a space, but easier to see for testing). The length of each string must not exceed the maximum character length per line.

Your function should take in the maximum characters per line and return a data structure representing all lines in the indicated max length.

Examples:

words1 = [ "The", "day", "began", "as", "still", "as", "the",
          "night", "abruptly", "lighted", "with", "brilliant",
          "flame" ]

wrapLines(words1, 13) "wrap words1 to line length 13" =>

  [ "The-day-began",
    "as-still-as",
    "the-night",
    "abruptly",
    "lighted-with",
    "brilliant",
    "flame" ]

wrapLines(words1, 12) "wrap words1 to line length 12" =>

  [ "The-day",
    "began-as",
    "still-as-the",
    "night",
    "abruptly",
    "lighted-with",
    "brilliant",
    "flame" ]    


wrapLines(words1, 20) "wrap words1 to line length 20" =>

  [ "The-day-began-as",
    "still-as-the-night",
    "abruptly-lighted",
    "with-brilliant-flame" ]

words2 = [ "Hello" ]

wrapLines(words2, 5) "wrap words2 to line length 5" =>

  [ "Hello" ]


wrapLines(words2, 30) "wrap words2 to line length 30" =>

  [ "Hello" ]  

words3 = [ "Hello", "Hello" ]

wrapLines(words3, 5) "wrap words3 to line length 5" =>

  [ "Hello",
  "Hello" ]

words4 = ["Well", "Hello", "world" ]

wrapLines(words4, 5) "wrap words4 to line length 5" =>

  [ "Well",
  "Hello",
  "world" ]

words5 = ["Hello", "HelloWorld", "Hello", "Hello"]

wrapLines(words5, 20) "wrap words 5 to line length 20 =>

  [ "Hello-HelloWorld",
    "Hello-Hello" ]


words6 = [ "a", "b", "c", "d" ]
wrapLines(words6, 20) "wrap words 6 to line length 20 =>

  [ "a-b-c-d" ]

wrapLines(words6, 4) "wrap words 6 to line length 4 =>

  [ "a-b",
    "c-d" ]

wrapLines(words6, 1) "wrap words 6 to line length 1 =>

  [ "a",
    "b",
    "c",
    "d" ]

All Test Cases:
          words,  max line length
wrapLines(words1, 13)
wrapLines(words1, 12)
wrapLines(words1, 20)
wrapLines(words2, 5)
wrapLines(words2, 30)
wrapLines(words3, 5)
wrapLines(words4, 5)
wrapLines(words5, 20)
wrapLines(words6, 20)
wrapLines(words6, 4)
wrapLines(words6, 1)

n = number of words OR total characters
'''

# words1 = ["The","day","began","as","still","as","the","night","abruptly","lighted","with","brilliant","flame"]
# words2 = ["Hello"]
# words3 = ["Hello", "Hello"]
# words4 = ["Well", "Hello", "world"]
# words5 = ["Hello", "HelloWorld", "Hello", "Hello"]
# words6 = ["a", "b", "c", "d"]

# # Note: built-in functions like the Python textwrap module should not be used as solutions to this problem.

# def wrapLines(words, count):
#     i = 0
#     res = []
#     ans = ""

#     while i < len(words):
#         if len(ans + words[i]) > count:
#             res.append(ans)
#             ans = ""
#         else:
#             ans += words[i]
#             ans += "-"
#             i += 1

#         if i == len(words):
#             res.append(ans)

#     final_res = [i[:-1] for i in res]
#     print(final_res)
    
# wrapLines(words1, 12)

# res = []
        # cur_res = []
        # cur_len = 0

        # for word in words:
        #     word_len = len(word)
        #     if cur_res:
        #         word_len += 1

        #     if word_len + cur_len > count:
        #         res.append("-".join(cur_res))
        #         cur_res = [word]
        #         cur_len = word_len - 1
        #     else:
        #         cur_res.append(word)
        #         cur_len += word_len
        
        # if cur_res:
        #     res.append("-".join(cur_res))

        # print(res)
