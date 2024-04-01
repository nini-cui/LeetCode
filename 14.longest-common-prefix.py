#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Common_Prefix:
    def longestCommonPrefix(self, strs):
        elems_count = len(strs)
        common_prefix = ""
        if elems_count == 1:
            return strs[0]
        else:
            for i in (range(elems_count)):
                if i == 0:
                    current_elem = strs[i]
                    current_elem_len = len(current_elem)

                    next_elem = strs[i + 1]
                    next_elem_len = len(next_elem)

                    elem_len = min(current_elem_len, next_elem_len)
                    if elem_len == 0:
                        if current_elem_len == 0:
                            return current_elem
                        else:
                            return next_elem
                    else: 
                        for elem_iter in range(elem_len):
                            if current_elem[elem_iter] == next_elem[elem_iter]:
                                common_prefix += current_elem[elem_iter]
                            else:
                                break
                elif i == 1:
                    continue
                else:
                    common_prefix_len = len(common_prefix)
                    current_iter_len = len(strs[i])
                    iter_length = min(common_prefix_len, current_iter_len)
                    if iter_length == 0:
                        if common_prefix_len == 0:
                            return common_prefix
                        else:
                            return strs[i]
                    else:
                        for iter_elem in range(iter_length):
                            if strs[i][iter_elem] == common_prefix[iter_elem]:
                                if iter_elem == (iter_length - 1):
                                    common_prefix = common_prefix[0:iter_length]
                                    break
                                else:
                                    continue
                            else:
                                common_prefix = common_prefix[0:iter_elem]
                                break

            return common_prefix



if __name__ == "__main__":
    common_prefix = Common_Prefix()
    # print(common_prefix.longestCommonPrefix(["ac","ac","a", "a"]))
    print(common_prefix.longestCommonPrefix(["a","a","b"]))