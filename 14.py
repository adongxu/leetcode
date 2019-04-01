"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs or " " in strs:
            return ""
        i = 0
        # 最小的字符串的长度就是循环截止的标志
        while i < min([len(s) for s in strs]):
            # 标识当前字母是否相同
            cur_i_same = True
            # 当前字母
            cur_letter = strs[0][i]
            for s in strs[1:]:
                if s[i] == cur_letter:
                    continue
                else:
                    cur_i_same = False
                    break
            # 当前相同，i++
            if cur_i_same:
                i += 1
            else:
                break
        return "" if i == 0 else strs[0][:i]



